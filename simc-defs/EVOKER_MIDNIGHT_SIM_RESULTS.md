# Devastation SC vs FS — sim results (self-run SimC, Midnight 12.0.5)

We built SimulationCraft from the `midnight` branch and ran the two repo
profiles head-to-head to separate **real tuning** from **meta bias**.

- **Binary:** SimulationCraft **1205-01**, WoW **12.0.5.67823** (hotfix
  2026-05-28), built CLI-only (`-DBUILD_GUI=OFF -DSC_NO_NETWORKING=ON`).
- **Profiles (identical gear, only talents differ):**
  `MID1_Evoker_Devastation_SC.simc` (Scale Commander, SimC `source=default`) vs
  `MID1_Evoker_Devastation_FS.simc` (Flameshaper).
- **Convergence:** `target_error=0.2` (M+ styles reconfirmed at `0.1` — identical),
  `threads=4`. Patchwerk runs: `fight_length=300 fixed_time=1 desired_targets=N`.
- **Caveat up front:** this is **Devastation only**. Augmentation has **no SimC
  profile** (support spec — its value is buffing allies), so its ~99% Scale
  Commander is *not* a sim-settleable question; it's log-driven (see analysis §5).

## Results (mean DPS, personal only — no Bloodlust/PI/affixes)

| Scenario | Scale Commander | Flameshaper | SC vs FS |
|---|--:|--:|--:|
| 1T (Patchwerk)   | 111,223 | 113,424 | **−1.9%** |
| 2T               | 175,551 | 150,569 | +16.6% |
| **3T**           | 232,147 | 168,006 | **+38.2%** |
| 4T               | 284,922 | 223,274 | +27.6% |
| 5T               | 330,779 | 280,803 | +17.8% |
| 6T               | 367,797 | 325,619 | +13.0% |
| 10T              | 510,827 | 486,332 | +5.0% |
| **DungeonSlice**     | 117,301 | 126,391 | **−7.2%** |
| **HecticAddCleave**  | 141,965 | 165,745 | **−14.3%** |

## What the numbers say

1. **SC's tuning edge is real but burst-/few-target-shaped.** It peaks hard at
   **3 targets (+38%)** and tapers both ways — the unmistakable signature of
   **Mass Disintegrate's 3-target cap** (4 with Concentrated Power). On stacked
   2–6T it's a large, real advantage (+13–38%). This is the **raid-cleave /
   pull-burst** tuning.
2. **On pure single target, Flameshaper is (barely) ahead** (−1.9% for SC) —
   matching the guide claim that FS edges ST after its 12.0.5 buff.
3. **The bombshell:** in the **M+-shaped fight styles**, **Flameshaper sims
   HIGHER** — DungeonSlice **−7.2%** and HecticAddCleave **−14.3%** for SC. So
   raw sim DPS in the sustained M+ abstractions **does not support** the Scale
   Commander M+ meta — if anything it favours Flameshaper.

## Reconciling sim (FS-favoured) with reality (93% SC in high keys)

The two M+ fight styles are **sustained** scripted scenarios: targets/adds live
long, and there are long single-target boss-like stretches. That environment
**over-credits Flameshaper's DoT-ramp + Consume Flame** (which need targets to
live to pay off) and its ST edge. Real **high keys are the opposite**: trash is
bursted down in seconds inside CC/cooldown windows, so:

- **FS's ramp rarely matures** — packs die before Fire Breath DoT + Consume
  Flame detonations cash out.
- **SC is front-loaded** — empower → Mass Disintegrate (3-target cleave) +
  Bombardments + Deep Breath burst lands *immediately*. The **Patchwerk 2–5T
  numbers (SC +17–38%)** are a far better proxy for a real high-key pull-burst
  than DungeonSlice's sustained model.
- Add the **un-simmable** factors (Hover-mobility through mechanics,
  instant burst-on-pull, real pull counts sitting in SC's 3–5 sweet spot,
  defensives/utility) and a likely **meta/recommendation feedback loop**.

**Conclusion on the original question.** It is **not** "the difference is
marginal" (SC is +13–38% in stacked burst) and it is **not** a clean "SC does
more M+ DPS" (the M+-shaped sims favour FS). The truth is **pacing-dependent**:
Scale Commander wins where damage must be *front-loaded onto a few targets that
die fast* — which is exactly real high-key trash, and exactly what generic
sustained fight styles fail to model. So the 93% is best read as **real
burst-window tuning + un-simmable pacing/mobility advantages + some meta bias**,
*not* as a raw-DPS verdict the sim would print.

## Caveats / limitations
- **Fixed default builds:** each profile uses one SimC-default talent string;
  per-fight-style talent optimization (esp. an M+-tuned SC build) could shift
  the DungeonSlice/HecticAddCleave numbers. Worth a follow-up.
- **Generic fight styles ≠ real dungeons:** DungeonSlice/HecticAddCleave are
  scripted abstractions — no current-season routes, affix damage, forced
  movement, deaths, or interrupt assignments.
- **Personal DPS only:** no Bloodlust/Power Infusion/external buffs (affects
  both equally, so the *relative* gap is robust) and no group context.
- **Augmentation not covered** — un-simmable (see above).

## Reproduce
```bash
# build (≈15 min, 4 cores)
git clone --depth 1 --branch midnight https://github.com/simulationcraft/simc
cmake -S simc -B build -DCMAKE_BUILD_TYPE=Release -DBUILD_GUI=OFF -DSC_NO_NETWORKING=ON
cmake --build build -j4 --target simc
# run one cell, e.g. SC at 3 targets
build/simc simc-defs/MID1_Evoker_Devastation_SC.simc \
  fight_style=Patchwerk desired_targets=3 fight_length=300 fixed_time=1 \
  threads=4 target_error=0.2
# M+ styles: fight_style=DungeonSlice  /  fight_style=HecticAddCleave
```
Batch driver used: `/tmp/run_sims.py` (loops both profiles × all scenarios,
parses `json2` for `players[0].collected_data.dps.mean`).
</content>
