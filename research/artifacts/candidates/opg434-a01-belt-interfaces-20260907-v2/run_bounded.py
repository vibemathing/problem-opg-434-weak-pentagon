#!/usr/bin/env python3
"""Candidate computation wrapper; never a trusted-verifier receipt."""
import argparse, datetime, hashlib, json, os, pathlib, platform, resource, signal, subprocess, sys, time

def main():
    p=argparse.ArgumentParser(); p.add_argument('--receipt',required=True); p.add_argument('--cpu',type=int,default=35)
    p.add_argument('--wall',type=int,default=42); p.add_argument('--input',action='append',default=[])
    p.add_argument('--output-dir',action='append',default=[]); p.add_argument('command',nargs=argparse.REMAINDER)
    a=p.parse_args(); command=a.command[1:] if a.command[:1]==['--'] else a.command
    if not command: p.error('command required')
    def info(name):
        q=pathlib.Path(name); b=q.read_bytes(); return {'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
    def setup():
        resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912)); resource.setrlimit(resource.RLIMIT_CPU,(a.cpu,a.cpu+1))
        resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576)); resource.setrlimit(resource.RLIMIT_CORE,(0,0))
        if hasattr(os,'sched_getaffinity'): os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
        os.setsid()
    rec=pathlib.Path(a.receipt); rec.parent.mkdir(parents=True,exist_ok=True)
    stdout=rec.with_suffix('.stdout.txt'); stderr=rec.with_suffix('.stderr.txt')
    inputs=[info(n) for n in a.input]; start=time.monotonic(); usage0=resource.getrusage(resource.RUSAGE_CHILDREN)
    env=os.environ.copy(); env.update(PYTHONHASHSEED='0',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
    timed=False
    with stdout.open('xb') as so,stderr.open('xb') as se:
        proc=subprocess.Popen(command,stdout=so,stderr=se,preexec_fn=setup,env=env)
        try: code=proc.wait(timeout=a.wall)
        except subprocess.TimeoutExpired:
            timed=True; os.killpg(proc.pid,signal.SIGKILL); proc.wait(); code=124
    usage1=resource.getrusage(resource.RUSAGE_CHILDREN)
    outputs=[]
    for d in a.output_dir:
        outputs.extend(info(str(q)) for q in sorted(pathlib.Path(d).rglob('*')) if q.is_file())
    report={'verdict':'candidate_only','command':command,'python':platform.python_version(),
      'implementation':platform.python_implementation(),'solver':'none; Python standard library',
      'seed':0,'limits':{'cpu_soft_seconds':a.cpu,'cpu_hard_seconds':a.cpu+1,'wall_seconds':a.wall,
      'address_space_bytes':536870912,'cpu_affinity_cores':1,'threads_requested':1,'child_processes':1,
      'max_file_and_stream_bytes':1048576,'max_total_output_bytes_checked':5242880},
      'utc_completed':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':code,'timed_out':timed,
      'wall_seconds':time.monotonic()-start,
      'cpu_seconds':usage1.ru_utime+usage1.ru_stime-usage0.ru_utime-usage0.ru_stime,
      'max_rss_kib':usage1.ru_maxrss,'inputs':inputs,'outputs':outputs,
      'stdout':info(str(stdout)),'stderr':info(str(stderr)),
      'limitations':['same generating trust domain; no EvidenceLink or admission',
      'aggregate output budget is checked after exit; per-file/stream cap is OS-enforced']}
    report['output_budget_pass']=sum(x['bytes'] for x in outputs+[report['stdout'],report['stderr']])<=5242880
    rec.write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report)); return code or (0 if report['output_budget_pass'] else 3)
if __name__=='__main__': raise SystemExit(main())
