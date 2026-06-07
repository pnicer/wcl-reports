# SimulationCraft Evoker definitions — Midnight Season 1 (MID1)

Pulled on 2026-06-07 from the SimulationCraft `midnight` branch:
`simulationcraft/simc` → `profiles/MID1/`.

These are the *upstream SimC profile definitions* the user asked for, plus an
analysis of what they (and this repo's own WCL logs) say about the Scale
Commander hero-spec meta in high-tier Mythic+.

## What was actually available to pull

| Spec | Hero tree | SimC file | Status |
|------|-----------|-----------|--------|
| Devastation | **Scale Commander** | `MID1_Evoker_Devastation.simc` (internal name `MID1_Evoker_Devastation_SC`) | ✅ pulled, **this is SimC's `source=default`** build |
| Devastation | Flameshaper | `MID1_Evoker_Devastation_FS.simc` | ✅ pulled |
| Devastation | Chronomancer | — | ❌ does not exist |
| Augmentation | Scale Commander | — | ❌ does not exist |
| Augmentation | Chronomancer | — | ❌ does not exist |

Probed filenames and HTTP status (all on `midnight` branch):

```
200  MID1_Evoker_Devastation.simc        -> internal name MID1_Evoker_Devastation_SC
200  MID1_Evoker_Devastation_FS.simc
404  MID1_Evoker_Devastation_SC.simc     (no separate file; SC *is* the default)
404  MID1_Evoker_Augmentation.simc
404  MID1_Evoker_Augmentation_SC.simc
404  MID1_Evoker_Augmentation_Chrono.simc
```

So the two facts the definitions hand you *before any analysis* are:

1. **SimC ships no Augmentation Evoker profile at all** for Midnight S1.
2. **For Devastation, the build SimC blesses as the canonical default is the
   Scale Commander one** (`source=default`, internal id `..._Devastation_SC`).
   Flameshaper is shipped only as a clearly-labelled alternative.

## ⚠️ Big caveat before you read too much into these

SimulationCraft is a **single-target / fixed-add "Patchwerk" raid simulator.**
It does **not** model Mythic+ — no pull-by-pull routing, no forced movement, no
defensive/utility checks, no "kill this priority add now," no mob density that
changes shape every 10 seconds. So SimC profiles **cannot directly explain a
Mythic+ meta.** What they *can* tell you is which build the theorycrafters
treat as the baseline, and — by reading the action lists — *which mechanics the
build is built around.* The "why everyone plays SC in M+" answer below is
mechanical reasoning grounded in those action lists and in this repo's WCL
logs, **not** a number SimC printed.

## How the two Devastation profiles differ

Both files contain the **same** action-priority list. The only meaningful
difference is the `talents=` string, and the APL branches on it at the top:

```
actions+=/run_action_list,name=sc,if=talent.mass_disintegrate   # Scale Commander
actions+=/run_action_list,name=aoe_fs,if=active_enemies>=3       # Flameshaper AoE
actions+=/run_action_list,name=st_fs                            # Flameshaper ST
```

- `MID1_Evoker_Devastation_SC.simc` takes **`talent.mass_disintegrate`** →
  routes into the `sc` list.
- `MID1_Evoker_Devastation_FS.simc` does not → routes into `st_fs` / `aoe_fs`.

`mass_disintegrate` is the Scale Commander signature. The `sc` action list is
built entirely around it (verbatim from the profile):

```
actions.sc=deep_breath,if=buff.strafing_run.remains<=gcd.max*2,cancel_if=gcd.remains=0
...
actions.sc+=/disintegrate,target_if=min:debuff.bombardments.remains,
    early_chain_if=ticks_remain<=1&buff.mass_disintegrate_stacks.up,
    if=...&buff.mass_disintegrate_stacks.up&talent.mass_disintegrate,
    interrupt_if=talent.volatility&active_enemies>=8
```

Reading that line tells you exactly why the build is an AoE monster:

- **Deep Breath → Bombardments**: Deep Breath stamps the **`bombardments`**
  debuff on everything it flies over. The build then **`target_if=min:debuff.bombardments.remains`** — i.e. it actively spreads damage to refresh
  Bombardments on as many mobs as possible.
- **Mass Disintegrate**: after Deep Breath, Disintegrate becomes
  **instant-cast and cleaves to all Bombardment targets** (`buff.mass_disintegrate_stacks`). That converts the spec's biggest single-target
  spend into a multi-target nuke with no cast time → castable while moving.
- **Strafing Run** (`buff.strafing_run`): the build paces Deep Breath to keep
  this Scale Commander movement/damage window up.
- The `interrupt_if=talent.volatility&active_enemies>=8` clause only fires at
  8+ targets — the APL is explicitly tuned for big pulls.

The Flameshaper lists (`st_fs`, `aoe_fs`) instead revolve around
`fire_breath` DoT uptime, `engulf`/`consume_flame`, and `pyre` — strong, but
fundamentally a **DoT-ramp / sustained** pattern that wants targets to live and
wants you to stand still channeling.

## Why Scale Commander wins in high Mythic+ (the actual answer)

Combine the action-list mechanics above with what M+ rewards, and SC dominance
falls out for **both** specs:

1. **Instant, movement-friendly cleave.** M+ is constant movement (swirlies,
   kiting, repositioning). Flameshaper's value is locked in *channeled*
   Disintegrate and *standing* DoT ramp; every forced move is a damage loss.
   Mass Disintegrate makes the same damage **instant and AoE**, so SC loses
   almost nothing to movement. This is the single biggest reason.

2. **Front-loaded burst AoE on demand.** Deep Breath + Mass Disintegrate +
   Bombardments dumps a huge chunk of AoE the moment a pack is grabbed.
   High keys are about *bursting packs down inside a CC/cooldown window*, not
   a 4-minute Patchwerk — exactly the shape SC is built for and FS is not.

3. **Bombardments scales with pack size.** Bombardments re-fires on your hits
   across every tagged mob, so its value rises with density. Trash packs in
   high keys are dense → Bombardments is near-permanent free AoE.

4. **Built-in mobility / Deep Breath as a tool.** Deep Breath is both the
   damage enabler *and* a gap-closer/repositioning tool — double-duty that M+
   values and a raid sim never credits.

### Why Augmentation *also* goes Scale Commander

There is no SimC Aug profile, so the sim says nothing here directly — but this
repo's own logs answer it. The Augmentation reports in this repo
(`20260507_090328_Alokys.html`, `20260508_211858_Dzin.html`) **track
`Bombardments` as a damage source and uptime metric**, e.g.:

```
<span class="label">Bombardments</span><span class="value val-warn">32% ...
title="Bombardments: ~31% expected from random overlap"
```

Bombardments only exists on the **Scale Commander** tree, so those Aug players
are running Scale Commander, confirmed straight from the logs. The reasoning:

- Augmentation's job is to **buff the group** (Ebon Might, Prescience, Breath
  of Eons — all heavily present in these logs) while contributing personal
  damage. Its hero choice is therefore decided by *which tree adds the most
  low-effort personal/AoE throughput without compromising the support
  rotation* — **not** by a personal-DPS sim (which is why SimC doesn't even
  bother shipping an Aug profile).
- **Scale Commander gives Aug exactly that**: Deep Breath + Bombardments is a
  big, instant, density-scaling AoE chunk that slots around the support
  globals, where Chronomancer's value is more single-target / cooldown-window
  shaped and competes with the buffs for casts.
- **Consistency / shared muscle memory**: same hero tree, same Deep Breath
  usage across both Evoker specs.

### One-line summary
SimC's *definitions* tell you SC is the **default Devastation build** and that
Aug isn't even modelled; the *action lists* tell you SC is built around
**instant, movement-proof, density-scaling AoE** (Mass Disintegrate +
Bombardments + Deep Breath). That mechanic profile is precisely what high
Mythic+ rewards and what Flameshaper's channel/DoT-ramp pattern gives up — so
both Evoker specs converge on Scale Commander. SimC itself can't *prove* the
M+ result because it only sims Patchwerk, but the build it ships as default and
this repo's own logs both point the same way.

## Sources
- [`simc` profiles, `midnight` branch](https://github.com/simulationcraft/simc/tree/midnight/profiles)
- [`MID1_Evoker_Devastation.simc` (Scale Commander default)](https://github.com/simulationcraft/simc/blob/midnight/profiles/MID1/MID1_Evoker_Devastation.simc)
- [`MID1_Evoker_Devastation_FS.simc` (Flameshaper)](https://github.com/simulationcraft/simc/blob/midnight/profiles/MID1/MID1_Evoker_Devastation_FS.simc)
- [SimulationCraft Evoker wiki](https://github.com/simulationcraft/simc/wiki/Evokers)
- This repo's Augmentation WCL reports: `20260507_090328_Alokys.html`, `20260508_211858_Dzin.html` (both show Bombardments → Scale Commander).
</content>
</invoke>
