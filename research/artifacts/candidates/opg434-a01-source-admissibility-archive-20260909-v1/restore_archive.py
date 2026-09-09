"""Integrity-only restoration of the exact supplied 36-file variant.
Does not execute archived programs or install the historical inbox packet.
"""
import base64
import hashlib
import json
import lzma
from pathlib import Path, PurePosixPath

PARTS = [
    '2afbd4e8a04cda47454daac0538bb8d8e4d0adcf31250a339aa2fbc4e43ad669',
    '68bdfdfcd780a25cd5ea0a2f0948546e16f8fe87da0718be4223aeaeb34c583a',
    'b17e45c89d69074f27241381b8a0f96cd36ad697b1ec3fd33d7bc42c757b2da8',
    '779cbebdafd5f11743b504d3c3667c04b605e307a0132df44a76b20e46097d49',
]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def restore():
    root = Path(__file__).resolve().parent
    raw_parts = [(root / ('payload-%02d.txt' % i)).read_bytes() for i in range(4)]
    if any(len(p) > 17000 or digest(p) != h for p,h in zip(raw_parts,PARTS)):
        raise ValueError('payload mismatch')
    packed = base64.b64decode(b''.join(p.strip() for p in raw_parts), validate=True)
    if len(packed) != 45848 or digest(packed) != '26f61b33877795b3fbf838ff0a2c9357c3de5540d0d4e7603575c21802088772':
        raise ValueError('compressed identity mismatch')
    dec = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
    decoded = dec.decompress(packed, max_length=421400)
    if not dec.eof or dec.unused_data or len(decoded) != 421399 or digest(decoded) != '00a763b6f8c2062f1c8ea5da7d0fb6e54490c08ceab6e406da8f4a70c4d49918':
        raise ValueError('decoded identity or bound mismatch')
    entries = json.loads(decoded)
    if len(entries) != 36 or len({e['path'] for e in entries}) != 36:
        raise ValueError('file count or uniqueness mismatch')
    checked=[]
    for entry in entries:
        name=PurePosixPath(entry['path'])
        if name.is_absolute() or '..' in name.parts or '\\' in entry['path']:
            raise ValueError('unsafe relative path')
        if not any(entry['path'].startswith(p) for p in ('research/artifacts/candidates/','research/artifacts/source-notes/','research/artifacts/web-inbox/')):
            raise ValueError('unexpected logical path')
        b=entry['text'].encode('utf-8')
        if len(b)!=entry['bytes'] or len(b)>1048576 or digest(b)!=entry['sha256']:
            raise ValueError('logical identity mismatch')
        checked.append((name,b,entry['sha256']))
    if sum(len(b) for _,b,_ in checked)!=377733:
        raise ValueError('logical total mismatch')
    target=root/'restored'
    if target.exists():
        raise FileExistsError('restore destination already exists')
    target.mkdir()
    for name,b,_ in checked:
        dest=target.joinpath(*name.parts)
        dest.parent.mkdir(parents=True,exist_ok=True)
        with dest.open('xb') as f:
            f.write(b)
    print(json.dumps({'status':'integrity_pass','file_count':36,'logical_bytes':377733,
        'files':[{'path':str(n),'bytes':len(b),'sha256':h} for n,b,h in checked]},sort_keys=True))

if __name__=='__main__':
    restore()
