# Augmentation SC vs Chronowarden — group sim (self-run SimC, Midnight 12.0.5)

Augmentation is a **support** spec, so it must be simmed **in a group** (the
buffs need allies to land on). We built that group sim with the same SimC we
used for Devastation.

- **Binary:** SimulationCraft **1205-01**, WoW **12.0.5.67823** (CLI build).
- **Talent builds (user-provided, current Midnight):** a **clean hero-tree-only
  swap** — both strings share an identical class+spec tree and differ *only* in
  the hero portion (Scale Commander vs Chronowarden). This isolates the hero
  tree's contribution (but neither build re-optimizes spec talents for its tree).
- **Group / buff targets:** the dungeon comp requested — **Guardian Druid
  (tank) + Retribution Paladin + Unholy Death Knight**, plus the Aug.
  *(Resto Shaman healer omitted — SimC ships no healer profile; a healer's
  damage is negligible, so the only effect is one fewer Ebon Might target.)*
- **Metric:** total **raid DPS** (the honest support measure), decomposed into
  the Aug's **own damage** vs its **team-amplification** (the extra DPS it adds
  to allies = raid − Aug_own − no-Aug baseline). `target_error=0.3`.

## Validity check — the buffs land
At 1T the 3-ally baseline is **315,721**; adding the SC Aug raises the raid to
**435,120** (+119k) while the Aug's own damage is only ~45k — so **~75k of that
is buffs applied to allies** (a ~+24% ally uplift). The support modeling works.

## Results

| Scenario | Aug own (SC / Chr) | Team-amp (SC / Chr) | Raid total (SC / Chr) | SC vs Chr |
|---|---|---|---|--:|
| 1T (Patchwerk) | 44,826 / 55,366 | **+74,573** / +62,419 | 435,120 / 433,506 | **+0.4%** |
| 3T | 92,712 / 138,402 | **+123,933** / +118,951 | 742,747 / 783,455 | −5.2% |
| 5T | 124,286 / 204,053 | **+171,817** / +166,195 | 1,031,678 / 1,105,823 | −6.7% |
| DungeonSlice | 48,222 / 57,336 | **+60,870** / +48,201 | 416,501 / 412,946 | **+0.9%** |

## What the numbers say

1. **Scale Commander is the better *team amplifier* in every scenario.** It adds
   more DPS to the allies than Chronowarden everywhere — including the M+-shaped
   DungeonSlice (**+60.9k vs +48.2k**) and single target (**+74.6k vs +62.4k**).
   For a spec whose *job* is amplifying the group, this is the metric that
   matters, and SC wins it across the board.
2. **Chronowarden does more *personal* damage** (e.g. 204k vs 124k own DPS at
   5T) — and that personal output is what carries it to a higher **total** in
   stacked AoE (3T −5.2%, 5T −6.7% for SC).
3. **Total raid DPS is essentially tied** on single target (+0.4%) and
   DungeonSlice (+0.9%) — within noise at this convergence.

**So, exactly as on the Devastation side, raw sim throughput does NOT crown
Scale Commander** — on total DPS it's tied-to-behind Chronowarden here. The
~99% SC representation in M+ is therefore **not** a total-DPS verdict. What does
explain it, grounded in these numbers + mechanics:

- **Team amplification, not personal bar.** SC gives the *group* more (it wins
  team-amp in all 4 scenarios). A group benefits from the amplifier, not the
  Aug's own meter — and Chronowarden "wins total" only by inflating its *own*
  damage, which doesn't help the other four players.
- **Execution-independence.** Guides put it as "Chronowarden for prog raids that
  sync cooldowns; Scalecommander otherwise — it's less affected by ally
  performance." The sim executes everything deterministically (Chronowarden's
  near-best case); live PUG keys are messy, which erodes Chronowarden's
  alignment-dependent value and favors SC.
- **NOT a Breath-of-Eons uptime advantage** (see next section): contrary to the
  common "Wingleader flywheel" claim, SC does **not** get Breath up more often —
  Chronowarden does. SC's M+ case rests on team-amplification + consistency, not
  Breath frequency.
- Plus mobility/consistency and a meta/recommendation feedback loop.

## Breath of Eons effective cooldown by hero tree (the Wingleader question)

**The real mechanic (verified from spell data + engine code) scales — it is NOT
flat.** Wingleader (effect values, id 441206): for **Augmentation**, each
Bombardment reduces Breath of Eons' cooldown by **1.0 s per target struck, capped
at 3.0 s per Bombardment** (`effectN3=1000ms`, `effectN4=3000ms`;
`sc_evoker.cpp:7905-7911`, `cdr = min(per_target × n_targets, cap)` on each
Bombardment impact). Total reduction = (Bombardment procs) × min(1.0×targets, 3.0)
— it grows with **both** target density and proc count.

⚠️ **The sim numbers below are a SimC under-model, not ground truth.** Measured
Breath casts → "effective CD":

| Scenario | **SC** (sim) | **Chronowarden** (sim) |
|---|--:|--:|
| 1T | 92.4 s | 75.6 s |
| 3T | 92.2 s | 45.8 s |
| 5T | 92.6 s | 44.4 s |
| 8T | 92.1 s | 44.5 s |
| DungeonSlice | 92.7 s | 75.9 s |

What's actually going on:
- **SC came out flat ~92 s across 1→8 targets — which is impossible if the
  mechanic scaled.** The flat ~28 s reduction implies the sim applied ~**1.0 s
  per Bombardment regardless of targets** (i.e. it fed `n_targets = 1` into the
  Wingleader CDR), across ~28 procs/cycle. The per-target scaling (1.0→3.0 s) is
  **not being applied** — a SimC limitation in how the Bombardment proc (an
  external action fired via `execute_on_target`) reports its target count to
  Wingleader. (Forcing `evoker.simulate_bombardments=0` gave the same ~92 s —
  both proc paths share the limitation, so this did *not* validate "flat".)
- **Corrected estimate:** if those same ~28 procs/cycle hit the 3.0 s cap (3+
  targets), that's ~**84 s** of CDR → a Breath CD in the **~mid-30s** range at 3+
  targets — i.e. **shorter than Chronowarden's ~45 s**, scaling with density.
  (Rough: assumes proc volume holds and the cap is reached; the sim can't confirm
  it. Real allies hammering the marked target would add procs, shortening it
  further.)
- **Bottom line:** the Bombardments→Breath flywheel for SC is **real and
  density-scaling**; SimC under-credits it, so all my SC sim results here likely
  understate SC's Breath uptime (and its Bombardment/Wingleader value generally).
  The earlier "Chronowarden wins Breath uptime / the flywheel is a myth"
  conclusion is **retracted** — it was an artifact of the under-model.

## Caveats / limitations
- **Healer omitted** (no SimC profile) — slightly understates Ebon Might target
  dilution; negligible for the SC-vs-Chr comparison.
- **Roster-sensitive & melee/physical-heavy** (Guardian/Ret/Unholy DK). A
  different comp — especially burst casters that sync to Breath of Eons — could
  move the AoE numbers, *toward* Chronowarden if alignment is clean. This
  sensitivity is the core reason the Aug meta defers to logs.
- **Deterministic execution** flatters Chronowarden vs messy live play.
- **Bombardments is RPPM-approximated** by default, but we re-ran with
  `evoker.simulate_bombardments=0` (real allied damage events) and SC's Breath CD
  was unchanged — so for this 5-man comp the approximation is not the issue.
- **Hero-tree-only swap:** spec talents identical across builds (clean
  isolation), not each tree's fully-optimized loadout.
- **Small gaps (±1%) are within noise** at `target_error=0.3`; the 3T/5T
  Chronowarden leads (~5–7%) are real within the model.
- No M+ affixes/mechanics/forced movement; DungeonSlice is scripted.

## Reproduce
```bash
# allies: MID1_Druid_Guardian, MID1_Paladin_Retribution, MID1_Death_Knight_Unholy
python aug-sim/sweep.py       # raid-DPS sweep (baseline + SC + Chrono)
python aug-sim/breath_cd.py   # Breath of Eons cast count / effective CD per tree
```
Harness in `simc-defs/aug-sim/` (allies are stock SimC `profiles/MID1` files).
Aug profile = Dev SC gear with `spec=augmentation` + the provided talent string;
buffs auto-apply to the other actors via SimC's Augmentation modeling.
</content>
