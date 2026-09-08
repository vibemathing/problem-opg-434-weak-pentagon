#!/usr/bin/env python3
"""Bounded byte-exact decoder; never imports or executes restored code."""
import argparse,base64,hashlib,json,lzma,pathlib

def digest(b):return hashlib.sha256(b).hexdigest()
def main():
 a=argparse.ArgumentParser();a.add_argument('--out',required=True,type=pathlib.Path);args=a.parse_args();root=pathlib.Path(__file__).resolve().parent;out=args.out
 if out.exists():raise ValueError('use a new empty output directory')
 ix=json.loads((root/'bundle-index.json').read_text());parts=[]
 for f in ix['payload_parts']:
  p=pathlib.Path(f['path'])
  if p.is_absolute() or '..' in p.parts:raise ValueError('payload path')
  b=(root/p).read_bytes()
  if len(b)!=f['bytes'] or digest(b)!=f['sha256']:raise ValueError('payload digest')
  parts.append(b.strip())
 compressed=base64.b64decode(b''.join(parts),validate=True)
 dec=lzma.LZMADecompressor(memlimit=134217728);raw=dec.decompress(compressed,max_length=8388609)
 if not dec.eof or dec.unused_data or len(raw)>8388608:raise ValueError('decode bounds')
 if len(raw)!=ix['decoded_json_bytes'] or digest(raw)!=ix['decoded_json_sha256']:raise ValueError('decoded data digest')
 entries=json.loads(raw);spec={f['path']:f for f in ix['files']}
 if len(spec)!=ix['source_file_count'] or set(entries)!=set(spec):raise ValueError('file domain')
 values={};total=0
 for name,obj in entries.items():
  path=pathlib.Path(name)
  if path.is_absolute() or '..' in path.parts:raise ValueError('output path')
  s=obj['data'];kind=obj['codec']
  if kind=='text':data=s.encode()
  elif kind=='fixed_width_columns':
   n,w=obj['rows'],obj['width']
   if not(0<n<=131072 and 0<w<=256 and n*w==len(s)):raise ValueError('column dimensions')
   data=('\n'.join(''.join(s[i+j*n] for j in range(w)) for i in range(n))+'\n').encode()
  elif kind=='byte_offset_A':data=(bytes(ord(v)-65 for v in s).hex()+'\n').encode()
  elif kind=='parent_xor_A_S':
   n=obj['states'];bits=n.bit_length()-1
   if n!=len(s) or n!=1<<bits or n>131072:raise ValueError('parent dimensions')
   dest=[]
   for i,v in enumerate(s):
    code=ord(v)-65
    if not 0<=code<=bits+1:raise ValueError('parent delta code')
    flip=0 if code==0 else ((1<<(code-1)) if code<=bits else n-1)
    dest.append((i^flip).to_bytes(3,'little',signed=True))
   data=(b''.join(dest).hex()+'\n').encode()
  else:raise ValueError('unknown byte codec')
  f=spec[name];total+=len(data)
  if len(data)!=f['bytes'] or len(data)>1048576 or digest(data)!=f['sha256']:raise ValueError('logical file digest '+name)
  if total>8388608:raise ValueError('total limit')
  values[path]=data
 if total!=ix['source_total_bytes']:raise ValueError('total byte mismatch')
 out.mkdir(parents=True)
 for path,b in values.items():
  dest=out/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
 print(json.dumps({'verdict':'candidate_only','status':'byte_integrity_pass','logical_files':len(values),'bytes':total}))
if __name__=='__main__':main()
