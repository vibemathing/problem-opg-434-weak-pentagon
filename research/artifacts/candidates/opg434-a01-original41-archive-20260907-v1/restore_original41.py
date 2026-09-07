#!/usr/bin/env python3
"""Decode and hash the original 41 logical files. No archived code is executed.
Default: verify only. --extract requires a new directory beneath candidates/.
The archived packet is historical data, never an active inbox packet.
"""
import argparse, base64, hashlib, json, lzma, struct
from pathlib import Path, PurePosixPath

def digest(data):
    return hashlib.sha256(data).hexdigest()

def inflate(data, cap):
    dec=lzma.LZMADecompressor(memlimit=128*1024*1024)
    out=dec.decompress(data,max_length=cap+1)
    if len(out)>cap or not dec.eof or dec.unused_data:
        raise ValueError('compressed size, termination or trailing-data error')
    return out

def restore(root):
    idx=json.loads((root/'index.json').read_text())
    payload=b''.join((root/name).read_bytes() for name in idx['payload_files'])
    if digest(payload)!=idx['payload_sha256']:
        raise ValueError('payload hash mismatch')
    raw=inflate(base64.b64decode(payload,validate=True),1048576)
    if digest(raw)!=idx['decoded_json_sha256']:
        raise ValueError('decoded JSON hash mismatch')
    entries=json.loads(raw); expected={}
    for name,size,sha in idx['files']:
        name=name if name.startswith('research/') else idx['path_prefix']+name
        if name in expected: raise ValueError('duplicate file index')
        expected[name]=(size,sha)
    if set(entries)!=set(expected) or len(entries)!=41:
        raise ValueError('archive coverage mismatch')
    restored={}
    for name,e in entries.items():
        path=PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or not name.startswith('research/artifacts/'):
            raise ValueError('unsafe logical path')
        if e['codec']=='utf8': data=e['text'].encode('utf-8')
        elif e['codec']=='dimacs-column-delta-i16-v1':
            stream=inflate(base64.b64decode(e['data'],validate=True),2097152)
            prev=[0]*16; pos=0; lines=[e['header']+'\n']
            if not 0<=e['rows']<=50000: raise ValueError('row budget')
            for _ in range(e['rows']):
                width=stream[pos]; pos+=1
                if not 1<=width<=16: raise ValueError('clause width')
                row=[]
                for col in range(width):
                    delta=struct.unpack_from('<h',stream,pos)[0]; pos+=2
                    value=prev[col]+delta; prev[col]=value; row.append(value)
                lines.append(' '.join(map(str,row))+' 0\n')
            if pos!=len(stream): raise ValueError('trailing numeric bytes')
            data=''.join(lines).encode('ascii')
        else: raise ValueError('unsupported codec')
        size,sha=expected[name]
        if len(data)!=size or digest(data)!=sha: raise ValueError('file hash mismatch: '+name)
        if len(data)>1048576: raise ValueError('file size budget')
        restored[name]=data
    if sum(map(len,restored.values()))!=714578: raise ValueError('total byte count')
    return restored

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--extract',type=Path)
    args=parser.parse_args(); files=restore(Path(__file__).parent)
    if args.extract:
        out=args.extract
        if out.is_absolute() or '..' in out.parts or not out.as_posix().startswith('research/artifacts/candidates/'):
            raise ValueError('extraction must stay beneath candidates/')
        if out.exists(): raise ValueError('destination already exists')
        out.mkdir(parents=True)
        for name,data in files.items():
            dest=out/name; dest.parent.mkdir(parents=True,exist_ok=True); dest.write_bytes(data)
    print(json.dumps({'status':'integrity_pass','verdict':'candidate_only','files':len(files),'bytes':sum(map(len,files.values())),'mathematical_execution':False},sort_keys=True))

if __name__=='__main__': main()
