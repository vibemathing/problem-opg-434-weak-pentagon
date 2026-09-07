#!/usr/bin/env python3
"""Decode supplementary transport/recheck receipts; executes no retained code."""
import argparse, base64, hashlib, json, lzma, pathlib
p=argparse.ArgumentParser(); p.add_argument('--out'); a=p.parse_args()
b=json.loads(pathlib.Path('delivery_receipts.bundle.json').read_text())
d=lzma.LZMADecompressor(memlimit=67108864)
v=d.decompress(base64.b64decode(b['xz_base64'],validate=True),max_length=262145)
assert d.eof and not d.unused_data and len(v)<=262144
files=json.loads(v); entries={x['path']:x for x in b['files']}
assert set(files)==set(entries)
for name,text in files.items():
    path=pathlib.PurePosixPath(name); raw=text.encode()
    assert not path.is_absolute() and '..' not in path.parts
    assert len(raw)==entries[name]['bytes'] and hashlib.sha256(raw).hexdigest()==entries[name]['sha256']
if a.out:
    root=pathlib.Path(a.out); assert not root.is_absolute() and '..' not in root.parts and not root.exists()
    root.mkdir()
    for name,text in files.items():
        q=root/name; q.parent.mkdir(parents=True,exist_ok=True); q.write_bytes(text.encode())
print(json.dumps({'status':'delivery_integrity_pass','files':len(files),'verdict':'candidate_only'}))
