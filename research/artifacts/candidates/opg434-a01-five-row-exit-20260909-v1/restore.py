#!/usr/bin/env python3
"""Integrity-only bounded UTF-8 archive restoration; executes no stored code."""
import base64,hashlib,json,lzma,sys
from pathlib import Path,PurePosixPath
root=Path(__file__).resolve().parent
index=json.loads((root/'bundle-index.json').read_text(encoding='utf-8'))
def sha(x):return hashlib.sha256(x).hexdigest()
parts=[]
for item in index['parts']:
    data=(root/item['file']).read_bytes()
    if len(data)!=item['bytes'] or sha(data)!=item['sha256']:raise ValueError('part integrity')
    parts.append(data.strip())
packed=base64.b64decode(b''.join(parts),validate=True)
if len(packed)!=index['xz_bytes'] or sha(packed)!=index['xz_sha256']:raise ValueError('XZ integrity')
dec=lzma.LZMADecompressor(memlimit=192*1024*1024)
raw=dec.decompress(packed,max_length=index['raw_json_bytes']+1)
if not dec.eof or dec.unused_data or len(raw)!=index['raw_json_bytes'] or sha(raw)!=index['raw_json_sha256']:raise ValueError('JSON integrity')
entries=json.loads(raw)
if len(entries)!=index['logical_count']:raise ValueError('logical count')
out=Path(sys.argv[1] if len(sys.argv)>1 else root/'restored').resolve()
out.mkdir(parents=True,exist_ok=True)
manifest=[];seen=set();total=0
for e in entries:
    name=PurePosixPath(e['name'])
    if name.is_absolute() or '..' in name.parts or str(name) in seen:raise ValueError('unsafe/duplicate name')
    seen.add(str(name));b=e['text'].encode('utf-8')
    if len(b)>1048576 or len(b)!=e['bytes'] or sha(b)!=e['sha256']:raise ValueError('logical integrity')
    p=out/str(name)
    if not p.resolve().is_relative_to(out):raise ValueError('path escape')
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
    if sha(p.read_bytes())!=e['sha256']:raise ValueError('reread mismatch')
    manifest.append({'name':str(name),'bytes':len(b),'sha256':sha(b)});total+=len(b)
if total!=index['logical_bytes']:raise ValueError('logical byte count')
(out/'restored_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'integrity_only_pass','logical_files':len(entries),'logical_bytes':total,'mathematical_code_executed':False}))
