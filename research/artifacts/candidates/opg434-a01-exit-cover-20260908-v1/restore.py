#!/usr/bin/env python3
"""Restore fixed candidate bytes only. No archived program is imported or run.
From this directory: python3 restore.py --out restored
Then cd restored; use the commands in audit-state.json to request replay.
Existing differing files are rejected; identical files may be reused.
"""
import argparse,base64,hashlib,json,lzma,signal
from pathlib import Path

EXPECTED_WRAPPER = '98a1f5d39b62f03d0cb2c2f5fd4b77c682667eb4b9485fe6e4159b639c894a1a'
EXPECTED_JSON = 'e2b92aa7165590c76943d0431a49b5fc5069fe3dce86b7c98b782b0908f1a94a'
PARTS = ('15a4b1b45fdb33eb841ba8b445e5fcb471ac0c864435012c9c1d4f7bb81da472',
         '03cdfb649c76327e641a6e31db5e953f0c7e6617ccfd365c3aa81b93ae792e9b',
         '5311d11f001f9b2a2747fc99fdfa14f85e0fa33f5dbf1c975ce15aa63959fb4b')
def require(ok, message):
    if not ok:
        raise ValueError(message)
def sha(raw):
    return hashlib.sha256(raw).hexdigest()
def main():
    import resource
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
    resource.setrlimit(resource.RLIMIT_CPU,(10,11))
    resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576))
    signal.alarm(15)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    here=Path(__file__).resolve().parent
    out=args.out.resolve()
    require(out.is_relative_to(here) and out!=here,'output must be a child directory')
    parts=[]
    for i,expected in enumerate(PARTS):
        raw=(here/f'payload-{i:02}.txt').read_bytes()
        require(len(raw)<=12000 and sha(raw)==expected,'payload part integrity')
        parts.append(raw)
    raw=b''.join(parts)
    require(len(raw)==33602 and sha(raw)==EXPECTED_WRAPPER,'wrapper integrity')
    wrapper=json.loads(raw)
    packed=base64.b64decode(wrapper['data'],validate=True)
    decoder=lzma.LZMADecompressor(memlimit=268435456)
    decoded=decoder.decompress(packed,max_length=1048577)
    require(decoder.eof and not decoder.unused_data,'incomplete or concatenated stream')
    require(len(decoded)==266547 and sha(decoded)==EXPECTED_JSON,'decoded integrity')
    entries=json.loads(decoded)
    require(len(entries)==29 and wrapper['logical_count']==29,'file count')
    validated=[]; names=set(); total=0
    for entry in entries:
        name=entry['path']
        require(isinstance(name,str) and Path(name).name==name and name not in ('.','..'),'flat relative filename')
        require(name not in names,'duplicate filename'); names.add(name)
        content=entry['text'].encode('utf-8')
        require(len(content)==entry['bytes'] and len(content)<=1048576,'file length')
        require(sha(content)==entry['sha256'],'logical file integrity')
        total+=len(content); require(total<=8388608,'aggregate output bound')
        target=out/name
        require(not target.is_symlink(),'output symlink')
        if target.exists():
            require(target.is_file() and target.read_bytes()==content,'different output already exists')
        validated.append((target,content))
    require(total==242965,'aggregate exact length')
    out.mkdir(parents=True,exist_ok=True)
    for target,content in validated:
        if not target.exists():
            with target.open('xb') as stream:
                stream.write(content)
    signal.alarm(0)
    print(json.dumps({'verdict':'candidate_only','status':'integrity_pass',
                      'logical_files':29,'total_bytes':total,'math_executed':False}))
if __name__=='__main__':
    main()
