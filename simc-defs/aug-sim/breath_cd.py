import subprocess, json, tempfile, os
SIMC="/tmp/simc"; HERE="/tmp/aug-sim"
builds={"Scale Commander":f"{HERE}/aug_SC.simc","Chronowarden":f"{HERE}/aug_Chrono.simc"}
scen=[("1T","Patchwerk",1),("3T","Patchwerk",3),("5T","Patchwerk",5),("8T","Patchwerk",8),("DungeonSlice","DungeonSlice",None)]
def run(pf,fs,tg):
    out=tempfile.mktemp(suffix=".json")
    cmd=[SIMC,pf,f"fight_style={fs}","threads=4","target_error=0.3","json2="+out]
    if fs=="Patchwerk": cmd+=[f"desired_targets={tg}","fight_length=300","fixed_time=1"]
    subprocess.run(cmd,capture_output=True,text=True)
    d=json.load(open(out)); os.remove(out)
    L=d["sim"]["statistics"]["simulation_length"]["mean"]
    aug=next(p for p in d["sim"]["players"] if "Aug" in p["name"])
    boe=next((s["num_executes"]["mean"] for s in aug["stats"] if s["name"]=="breath_of_eons"),0)
    return L,boe
print(f"{'Build':16}{'Scenario':14}{'BoE casts':>10}{'fight s':>9}{'casts/min':>10}{'eff CD (s)':>11}")
data={}
for name,pf in builds.items():
    for tag,fs,tg in scen:
        L,boe=run(pf,fs,tg)
        cpm=boe/(L/60); eff=L/boe if boe else 0
        data[(name,tag)]=(boe,L,eff)
        print(f"{name:16}{tag:14}{boe:>10.2f}{L:>9.0f}{cpm:>10.2f}{eff:>11.1f}",flush=True)
print("\n=== effective Breath of Eons CD (s) : SC vs Chronowarden ===")
print(f"{'Scenario':14}{'SC':>9}{'Chrono':>9}{'SC shorter by':>15}")
for tag,_,_ in [(s[0],0,0) for s in scen]:
    sc=data[("Scale Commander",tag)][2]; ch=data[("Chronowarden",tag)][2]
    print(f"{tag:14}{sc:>9.1f}{ch:>9.1f}{(ch-sc):>+13.1f}s")
