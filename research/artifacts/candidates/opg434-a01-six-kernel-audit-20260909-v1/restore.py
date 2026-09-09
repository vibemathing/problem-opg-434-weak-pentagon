"""Integrity-only bounded decoder; no archived program is executed."""
import base64,hashlib,json,lzma
from pathlib import Path,PurePosixPath

def sha(b):return hashlib.sha256(b).hexdigest()
def restore():
 root=Path(__file__).resolve().parent;index=json.loads((root/'bundle-index.json').read_text())
 if index['format']!='r09-six-kernel-audit-bundle-v1':raise ValueError('format')
 if index['logical_count']!=9 or index['decoded_bytes']!=45321:raise ValueError('bound')
 parts=[]
 for e in index['parts']:
  name=PurePosixPath(e['file'])
  if len(name.parts)!=1 or not e['file'].startswith('payload-'):raise ValueError('path')
  b=(root/name).read_bytes()
  if len(b)!=e['bytes'] or len(b)>11000 or sha(b)!=e['sha256']:raise ValueError('part')
  if hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()!=e['git_blob']:raise ValueError('blob')
  parts.append(b''.join(b.split()))
 packed=base64.b64decode(b''.join(parts),validate=True)
 if len(packed)!=index['xz_bytes'] or sha(packed)!=index['xz_sha256']:raise ValueError('xz')
 dec=lzma.LZMADecompressor(memlimit=128*1024*1024);raw=dec.decompress(packed,max_length=45322)
 if not dec.eof or dec.unused_data or len(raw)!=45321 or sha(raw)!=index['decoded_sha256']:raise ValueError('decode')
 entries=json.loads(raw);expected={e['path']:e for e in index['files']};checked={}
 if len(entries)!=9 or len(expected)!=9:raise ValueError('count')
 for e in entries:
  name=PurePosixPath(e['path']);b=e['text'].encode()
  if len(name.parts)!=1 or name.is_absolute() or '..' in name.parts or e['path'] in checked:raise ValueError('unsafe')
  if len(b)!=e['bytes'] or sha(b)!=e['sha256'] or {k:e[k] for k in ('path','bytes','sha256')}!=expected.get(e['path']):raise ValueError('entry')
  checked[e['path']]=b
 if sum(map(len,checked.values()))!=index['logical_bytes']:raise ValueError('total')
 records=json.loads(checked['execution.json'])
 for run in records['runs']:
  for field in ('stdout','stderr'):
   if sha(run[field].encode())!=run['receipt'][field+'_sha256']:raise ValueError('stream')
 target=root/'restored'
 if target.exists():raise FileExistsError('destination exists')
 target.mkdir()
 for n,b in checked.items():(target/n).write_bytes(b)
 print(json.dumps({'status':'integrity_pass','files':len(checked),'logical_bytes':sum(map(len,checked.values())),'mathematical_execution':False},sort_keys=True))
if __name__=='__main__':restore()
