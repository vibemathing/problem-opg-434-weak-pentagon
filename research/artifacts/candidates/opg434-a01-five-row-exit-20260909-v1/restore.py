"""Bounded integrity-only recovery. Does not execute the restored programs."""
import base64
import hashlib
import json
import lzma
from pathlib import Path, PurePosixPath

def digest(data):
    return hashlib.sha256(data).hexdigest()

def restore():
    root = Path(__file__).resolve().parent
    index = json.loads((root / 'bundle-index.json').read_text(encoding='utf-8'))
    if index['format'] != 'opg434-five-row-recovery-exact-v2':
        raise ValueError('unexpected index format')
    if (index['logical_count'], index['logical_bytes'], index['raw_json_bytes'], index['xz_bytes']) != (37, 476175, 501309, 30040):
        raise ValueError('unexpected bounds')
    parts = index['parts']
    if [p['file'] for p in parts] != ['payload-%02d.txt' % i for i in range(5)]:
        raise ValueError('unexpected payload sequence')
    texts = []
    for p in parts:
        raw = (root / p['file']).read_bytes()
        blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        if len(raw) != p['bytes'] or len(raw) > 11000 or digest(raw) != p['sha256'] or blob != p['git_blob']:
            raise ValueError('payload identity mismatch: ' + p['file'])
        texts.append(b''.join(raw.split()))
    packed = base64.b64decode(b''.join(texts), validate=True)
    if len(packed) != 30040 or digest(packed) != index['xz_sha256']:
        raise ValueError('compressed identity mismatch')
    dec = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
    decoded = dec.decompress(packed, max_length=501310)
    if not dec.eof or dec.unused_data or len(decoded) != 501309 or digest(decoded) != index['raw_json_sha256']:
        raise ValueError('decoded identity or bound mismatch')
    entries = json.loads(decoded)
    if len(entries) != 37 or len({e['name'] for e in entries}) != 37:
        raise ValueError('logical count or duplicate path')
    checked = []
    for e in entries:
        p = PurePosixPath(e['name'])
        if p.is_absolute() or '..' in p.parts or '\\' in e['name'] or len(p.parts) != 1:
            raise ValueError('unsafe logical path')
        data = e['text'].encode('utf-8')
        if len(data) != e['bytes'] or len(data) > 1048576 or digest(data) != e['sha256']:
            raise ValueError('logical identity mismatch')
        checked.append((p, data, e['sha256']))
    if sum(len(data) for _, data, _ in checked) != 476175:
        raise ValueError('logical total mismatch')
    target = root / 'restored'
    if target.exists():
        raise FileExistsError('restore target must not exist')
    target.mkdir()
    for p, data, _ in checked:
        with (target / p).open('xb') as f:
            f.write(data)
    print(json.dumps({'status': 'integrity_pass', 'mathematical_execution': False,
        'logical_count': 37, 'logical_bytes': 476175,
        'files': [{'path': str(p), 'bytes': len(d), 'sha256': h} for p,d,h in checked]}, sort_keys=True))

if __name__ == '__main__':
    restore()
