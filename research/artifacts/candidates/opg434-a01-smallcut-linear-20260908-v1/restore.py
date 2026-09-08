"""Bounded integrity decoder; does not execute archived code."""
import json,base64,lzma,hashlib,sys
from pathlib import Path,PurePosixPath

def h(b):return hashlib.sha256(b).hexdigest()
root=Path(__file__).parent
index=json.loads((root/'bundle-index.json').read_text())
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
parts=[]
for x in index['payload_parts']:
    b=(root/x['path']).read_bytes()
    assert len(b)==x['bytes'] and h(b)==x['sha256'];parts.append(b)
payload=b''.join(parts)
assert h(payload)==index['payload_sha256']
dec=lzma.LZMADecompressor(memlimit=67108864)
raw=dec.decompress(base64.b64decode(payload,validate=True),max_length=1048577)
assert dec.eof and not dec.unused_data and len(raw)<=1048576
assert len(raw)==index['raw_json_bytes'] and h(raw)==index['raw_json_sha256']
data=json.loads(raw);expected={x['path']:x for x in index['files']}
assert data.keys()==expected.keys() and len(data)<=64
size=0
for name,text in data.items():
    p=PurePosixPath(name);assert not p.is_absolute() and '..' not in p.parts
    b=text.encode();r=expected[name]
    assert len(b)==r['bytes'] and len(b)<=1048576 and h(b)==r['sha256']
    dst=out.joinpath(*p.parts);dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(b);size+=len(b)
assert size==index['expanded_file_bytes'] and size<=5242880
print(json.dumps({'status':'integrity_pass','files':len(data),'bytes':size,'verdict':'candidate_only'}))
