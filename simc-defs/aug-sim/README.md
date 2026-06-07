# Augmentation group-sim harness

Reproduces `../EVOKER_MIDNIGHT_AUG_SIM_RESULTS.md`. Aug is a support spec, so it
must be simmed in a group (buffs need allied actors to land on).

**Files**
- `aug_template.simc` — Aug profile scaffold (Dev SC gear + `spec=augmentation`,
  default Aug APL). `__TALENTS__` is replaced with a loadout string.
- `talents_sc.txt`, `talents_chronowarden.txt` — the two hero-tree loadout
  strings (identical class+spec tree; differ only in hero portion → clean swap).
- `sweep.py` — baseline + SC + Chrono across 1T/3T/5T/DungeonSlice; prints
  per-build raid total, Aug own DPS, and team-amplification.
- `run_aug.py` — single-scenario runner: `python run_aug.py "SC:<str>" "Chr:<str>" Patchwerk 3`.

**Allies** (not committed — copy from a SimC checkout's `profiles/MID1/`):
`MID1_Druid_Guardian.simc` (tank), `MID1_Paladin_Retribution.simc`,
`MID1_Death_Knight_Unholy.simc` → as `ally1/2/3.simc` here.
(No healer: SimC ships no Resto Shaman profile; negligible for the comparison.)

**Build SimC** (CLI, no Qt/networking):
`cmake -S simc -B build -DBUILD_GUI=OFF -DSC_NO_NETWORKING=ON && cmake --build build -j4 --target simc`
