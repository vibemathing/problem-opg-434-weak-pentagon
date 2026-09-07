#!/usr/bin/env python3
"""Lossless numeric-output unpacker, not a mathematical verifier.
Defaults to --check-only; --dest must be a fresh directory. Each raw SHA is checked.
"""
import argparse,base64,hashlib,json,lzma,struct
from pathlib import Path,PurePosixPath

def decode(bundle):
    assert bundle['format']=='r09-lossless-output-bundle-v1'
    text=lzma.decompress(base64.b64decode(bundle['text_xz_base64']),memlimit=134217728)
    assert len(text)<=4194304
    files={p:s.encode('utf-8') for p,s in json.loads(text).items()}
    c=bundle['cnf'];nums=lzma.decompress(base64.b64decode(c['column_deltas_xz_base64']),memlimit=134217728)
    vals=list(struct.unpack('<'+'i'*(len(nums)//4),nums));prev=[0]*17;rows=[];i=0
    while i<len(vals):
        k=vals[i];i+=1;assert 0<=k<=16
        row=[]
        for j in range(k):prev[j]+=vals[i];i+=1;row.append(prev[j])
        rows.append(' '.join(map(str,row))+(' ' if row else '')+'0\n')
    assert len(rows)==c['clauses']
    files[c['path']]=(f"p cnf {c['variables']} {c['clauses']}\n"+''.join(rows)).encode()
    assert len(files)==len(bundle['files'])
    for item in bundle['files']:
        p=item['path'];path=PurePosixPath(p)
        assert not path.is_absolute() and '..' not in path.parts
        raw=files[p]
        assert len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256'],p
    return files

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bundle',type=Path,default=Path(__file__).with_name('outputs.bundle.json'))
    ap.add_argument('--dest',type=Path);ap.add_argument('--check-only',action='store_true');a=ap.parse_args()
    files=decode(json.loads(a.bundle.read_text()))
    if a.dest is not None and not a.check_only:
        a.dest.mkdir(parents=True,exist_ok=False)
        for p,raw in files.items():
            q=a.dest/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(raw)
    print(json.dumps({'status':'all_output_bytes_match','files':len(files),'bytes':sum(map(len,files.values()))}))
if __name__=='__main__':main()
