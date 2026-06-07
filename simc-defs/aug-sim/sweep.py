import subprocess, json, tempfile, os
SIMC="/tmp/simc"; HERE="/tmp/aug-sim"
allies=[f"{HERE}/ally{i}.simc" for i in (1,2,3)]
tmpl=open(f"{HERE}/aug_template.simc").read()
for tag,s in [("SC",open(f"{HERE}/sc.txt").read().strip()),("Chrono",open(f"{HERE}/chrono.txt").read().strip())]:
    open(f"{HERE}/aug_{tag}.simc","w").write(tmpl.replace("__TALENTS__",s))
scen=[("1T","Patchwerk",1),("3T","Patchwerk",3),("5T","Patchwerk",5),("DungeonSlice","DungeonSlice",None)]
def run(profiles,fs,tg):
    out=tempfile.mktemp(suffix=".json")
    cmd=[SIMC]+profiles+[f"fight_style={fs}","threads=4","target_error=0.3","json2="+out]
    if fs=="Patchwerk": cmd+=[f"desired_targets={tg}","fight_length=300","fixed_time=1"]
    subprocess.run(cmd,capture_output=True,text=True)
    d=json.load(open(out)); os.remove(out)
    ps={p['name']:p['collected_data']['dps']['mean'] for p in d["sim"]["players"]}
    return ps
rows=[]
for tag,fs,tg in scen:
    base=run(allies,fs,tg); bt=sum(base.values())
    sc=run([f"{HERE}/aug_SC.simc"]+allies,fs,tg); sct=sum(sc.values()); sca=next(v for k,v in sc.items() if "Aug" in k)
    ch=run([f"{HERE}/aug_Chrono.simc"]+allies,fs,tg); cht=sum(ch.values()); cha=next(v for k,v in ch.items() if "Aug" in k)
    rows.append((tag,bt,sca,sct,cha,cht))
    print(f"[{tag}] base {bt:,.0f} | SC raid {sct:,.0f} (aug {sca:,.0f}) | Chrono raid {cht:,.0f} (aug {cha:,.0f})",flush=True)
print("\n=== AUG SC vs CHRONOWARDEN (group raid DPS; allies = Guardian tank + Ret + Unholy DK) ===")
print(f"{'Scenario':14}{'No-Aug':>11}{'SC raid':>12}{'Chrono raid':>13}{'SC val':>9}{'Chr val':>9}{'SC vs Chr':>11}")
for tag,bt,sca,sct,cha,cht in rows:
    print(f"{tag:14}{bt:>11,.0f}{sct:>12,.0f}{cht:>13,.0f}{sct-bt:>+9,.0f}{cht-bt:>+9,.0f}{(sct/cht-1)*100:>+10.1f}%")
print("\n(Aug own DPS — SC vs Chrono)")
for tag,bt,sca,sct,cha,cht in rows:
    print(f"  {tag:14} SC {sca:>9,.0f}   Chrono {cha:>9,.0f}")
