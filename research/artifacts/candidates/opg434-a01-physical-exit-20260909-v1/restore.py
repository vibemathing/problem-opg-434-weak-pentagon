#!/usr/bin/env python3
"""Integrity-only, bounded restoration of exact candidate text. Runs no payload code."""
import argparse,base64,hashlib,json,lzma,resource,signal
from pathlib import Path
EXPECTED_INDEX='1b84c97f07ad2932db73fe2ae5ae010b55d5bce078d96df9937524b24ea8f9e6'
def sha(b):return hashlib.sha256(b).hexdigest()
def require(ok,message):
    if not ok:raise ValueError(message)
def main():
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912));resource.setrlimit(resource.RLIMIT_CPU,(10,11));resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576));signal.alarm(15)
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    here=Path(__file__).resolve().parent;out=args.out.resolve();require(out.is_relative_to(here) and out!=here,'output must be below candidate directory')
    raw=(here/'index.json').read_bytes();require(sha(raw)==EXPECTED_INDEX,'index mismatch');index=json.loads(raw);pieces=[]
    for r in index['parts']:
        b=(here/r['path']).read_bytes();require(len(b)==r['bytes'] and sha(b)==r['sha256'],'part mismatch');pieces.append(b.strip())
    packed=base64.b64decode(b''.join(pieces),validate=True);dec=lzma.LZMADecompressor(memlimit=268435456);raw=dec.decompress(packed,max_length=5242881)
    require(dec.eof and not dec.unused_data and len(raw)==index['decoded_bytes'] and sha(raw)==index['decoded_sha256'],'decode mismatch')
    entries=json.loads(raw);require(len(entries)==index['logical_count'],'count mismatch');expected={r['path']:r for r in index['files']};seen=set();total=0;writes=[]
    for r in entries:
        name=r['path'];require(Path(name).name==name and name not in ('.','..') and name not in seen,'unsafe/duplicate path');seen.add(name)
        b=r['text'].encode();require(name in expected and len(b)==r['bytes']==expected[name]['bytes'] and sha(b)==r['sha256']==expected[name]['sha256'],'file mismatch');total+=len(b)
        require(len(b)<=1048576 and total<=5242880,'output bound');p=out/name;require(not p.is_symlink(),'symlink')
        if p.exists():require(p.is_file() and p.read_bytes()==b,'different existing file')
        writes.append((p,b))
    require(seen==set(expected) and total==index['logical_total_bytes'],'manifest coverage');out.mkdir(parents=True,exist_ok=True)
    for p,b in writes:
        if not p.exists():p.write_bytes(b)
    print(json.dumps({'verdict':'candidate_only','status':'integrity_pass','logical_files':len(entries),'bytes':total,'mathematical_code_executed':False}))
if __name__=='__main__':main()
