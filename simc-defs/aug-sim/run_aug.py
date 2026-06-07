import subprocess, json, sys, tempfile, os
# usage: python run_aug.py "SC:<string>" "Chronowarden:<string>" [fight_style] [desired_targets]
SIMC="/tmp/simc"; HERE="/tmp/aug-sim"
allies=[f"{HERE}/ally{i}.simc" for i in (1,2,3)]
fs=sys.argv[3] if len(sys.argv)>3 else "Patchwerk"
tg=sys.argv[4] if len(sys.argv)>4 else "1"
tmpl=open(f"{HERE}/aug_template.simc").read()
# baseline (allies only)
def run(profiles):
    out=tempfile.mktemp(suffix=".json")
    cmd=[SIMC]+profiles+[f"fight_style={fs}",f"desired_targets={tg}","threads=4","target_error=0.3","json2="+out]
    if fs=="Patchwerk": cmd+=["fight_length=300","fixed_time=1"]
    subprocess.run(cmd,capture_output=True,text=True)
    d=json.load(open(out)); os.remove(out)
    ps={p['name']:p['collected_data']['dps']['mean'] for p in d["sim"]["players"]}
    return ps
base=run(allies); base_tot=sum(base.values())
print(f"Baseline raid (no Aug): {base_tot:,.0f}\n")
res={}
for arg in sys.argv[1:3]:
    label,_,tstr=arg.partition(":")
    af=f"{HERE}/aug_{label}.simc"
    open(af,"w").write(tmpl.replace("__TALENTS__",tstr.strip()))
    ps=run([af]+allies); tot=sum(ps.values())
    aug=next((v for k,v in ps.items() if "Aug" in k),0)
    res[label]=(aug,tot)
    print(f"[{label}] Aug own DPS {aug:,.0f} | raid total {tot:,.0f} | Aug value +{tot-base_tot:,.0f} ({(tot/base_tot-1)*100:+.1f}% raid)")
if len(res)==2:
    (l1,(a1,t1)),(l2,(a2,t2))=list(res.items())
    print(f"\n{l1} vs {l2}: raid {t1:,.0f} vs {t2:,.0f}  -> {l1} {(t1/t2-1)*100:+.1f}% raid DPS")
