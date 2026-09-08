#!/usr/bin/env python3
"""Bounded lossless text restoration only. Does not execute restored code."""
import argparse,base64,hashlib,json,lzma,resource,signal
from pathlib import Path,PurePosixPath

def restore(root,out):
 idx=json.loads((root/'bundle-index.json').read_text()); lim=idx['limits'];parts=[]
 for m in idx['parts']:
  raw=(root/m['file']).read_bytes()
  if len(raw)!=m['bytes'] or hashlib.sha256(raw).hexdigest()!=m['sha256']:raise ValueError('payload mismatch')
  parts.append(raw)
 b=b''.join(parts)
 if len(b)>lim['max_payload_bytes'] or hashlib.sha256(b).hexdigest()!=idx['payload_sha256']:raise ValueError('payload digest')
 d=lzma.LZMADecompressor(memlimit=268435456);raw=d.decompress(base64.b64decode(b,validate=True),max_length=lim['max_decoded_json_bytes']+1)
 if not d.eof or d.unused_data or len(raw)!=idx['decoded_json_bytes'] or hashlib.sha256(raw).hexdigest()!=idx['decoded_json_sha256']:raise ValueError('decoded digest/limit')
 files=json.loads(raw);manifest={m['file']:m for m in idx['files']}
 if set(files)!=set(manifest) or len(files)>lim['max_files']:raise ValueError('manifest mismatch')
 total=0;validated=[]
 for name,text in files.items():
  path=PurePosixPath(name)
  if path.is_absolute() or '..' in path.parts or '\\' in name or not isinstance(text,str):raise ValueError('unsafe output path')
  b=text.encode();total+=len(b);m=manifest[name]
  if len(b)>lim['max_file_bytes'] or len(b)!=m['bytes'] or hashlib.sha256(b).hexdigest()!=m['sha256']:raise ValueError('file digest')
  validated.append((name,b))
 if total>lim['max_total_file_bytes'] or out.exists():raise ValueError('output limit/existing directory')
 out.mkdir(parents=True)
 for name,b in validated:
  f=out/name;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(b)
 return {'status':'integrity_pass','files':len(files),'bytes':total,'verdict':'candidate_only','mathematical_replay':False}
if __name__=='__main__':
 resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912));resource.setrlimit(resource.RLIMIT_CPU,(10,11));signal.alarm(15)
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 print(json.dumps(restore(Path(__file__).resolve().parent,a.out),sort_keys=True))
