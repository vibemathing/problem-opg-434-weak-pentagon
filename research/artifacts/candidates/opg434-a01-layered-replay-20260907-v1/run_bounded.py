#!/usr/bin/env python3
"""Run a frozen local candidate control; collect bounded process facts, not Evidence."""
import argparse, hashlib, json, os, platform, resource, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

LIMITS = dict(wall_seconds=43, cpu_soft_seconds=35, cpu_hard_seconds=36,
              memory_bytes=536870912, per_file_bytes=1048576,
              stdout_bytes=1048576, stderr_bytes=1048576,
              output_bytes=4194304, single_child=True, cpu_affinity_count=1)

def digest(p):
    b=Path(p).read_bytes()
    return dict(path=Path(p).as_posix(), bytes=len(b), sha256=hashlib.sha256(b).hexdigest())

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--label', required=True);ap.add_argument('--directory', required=True)
    ap.add_argument('--input', action='append', default=[]);ap.add_argument('command', nargs=argparse.REMAINDER)
    a=ap.parse_args();command=a.command
    if command and command[0]=='--': command=command[1:]
    if not command or command[0] != 'python3': raise SystemExit('only python3 local controls')
    if any(Path(p).is_absolute() or '..' in Path(p).parts for p in a.input+[a.directory]+command[1:2]):
        raise SystemExit('repository-relative paths required')
    out=Path(a.directory);out.mkdir(parents=True,exist_ok=False)
    cpu=min(os.sched_getaffinity(0))
    def restrict():
        os.sched_setaffinity(0,{cpu})
        resource.setrlimit(resource.RLIMIT_AS,(LIMITS['memory_bytes'],)*2)
        resource.setrlimit(resource.RLIMIT_CPU,(35,36))
        resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576))
        resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.monotonic()
    env=dict(os.environ, PYTHONHASHSEED='0', OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1')
    inputs=[digest(p) for p in a.input]
    started=datetime.now(timezone.utc).isoformat()
    timed_out=False
    with (out/'stdout.txt').open('wb') as so,(out/'stderr.txt').open('wb') as se:
        proc=subprocess.Popen([sys.executable,'-B']+command[1:],stdout=so,stderr=se,stdin=subprocess.DEVNULL,
                              env=env,preexec_fn=restrict)
        try: proc.wait(timeout=LIMITS['wall_seconds'])
        except subprocess.TimeoutExpired: timed_out=True;proc.kill();proc.wait()
    used=resource.getrusage(resource.RUSAGE_CHILDREN)
    outputs=[digest(p) for p in sorted(out.rglob('*')) if p.is_file()]
    assert sum(p['bytes'] for p in outputs)<=LIMITS['output_bytes']
    report=dict(verdict='candidate_only',label=a.label,started_at_utc=started,
                status='timeout' if timed_out else ('process_pass' if proc.returncode==0 else 'process_failure'),
                exit_code=proc.returncode,timeout=timed_out,command=command,
                implementation=platform.python_implementation(),python_version=platform.python_version(),
                python_build=sys.version,solver='none; Python standard library only',seed=0,
                randomness='deterministic; no random search',limits=LIMITS,
                elapsed_wall_seconds=round(time.monotonic()-start,6),
                child_user_seconds=round(used.ru_utime-before.ru_utime,6),
                child_system_seconds=round(used.ru_stime-before.ru_stime,6),
                child_maxrss_kib=used.ru_maxrss,inputs=inputs,outputs=outputs,
                runner=digest(Path(__file__).relative_to(Path.cwd())),
                authority='User-requested local bounded candidate replay. Not a registered verifier; Web profile unchanged.',
                trusted_verifier=False,root_closed=False)
    (out/'process_receipt.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('label','status','exit_code','elapsed_wall_seconds','child_maxrss_kib')}))
    return 0 if report['status']=='process_pass' else 1
if __name__=='__main__':sys.exit(main())
