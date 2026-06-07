# SimulationCraft Evoker definitions — Midnight Season 1 (MID1)

Pulled 2026-06-07 from the SimulationCraft `midnight` branch
(`simulationcraft/simc`). This corrects an earlier draft that wrongly claimed
"SimC has no Augmentation profile" and that "SimC only sims Patchwerk." Both
were wrong — see below.

## Files in this folder

| File | What it is | Upstream path |
|------|-----------|---------------|
| `MID1_Evoker_Devastation_SC.simc` | Pre-built **gear+talent profile**, Scale Commander. **SimC's `source=default` Devastation build** (internal id `MID1_Evoker_Devastation_SC`). | `profiles/MID1/MID1_Evoker_Devastation.simc` |
| `MID1_Evoker_Devastation_FS.simc` | Pre-built gear+talent profile, Flameshaper alternative. | `profiles/MID1/MID1_Evoker_Devastation_FS.simc` |
| `evoker_augmentation_apl.simc` | The **default Augmentation rotation definition** (APL). This is the thing an Aug analyzer/sim is built on. | `ActionPriorityLists/default/evoker_augmentation.simc` |
| `MID1_Generate_Evoker.simc` | The generator that produces the MID1 gear profiles (emits the two Devastation builds above). | `profiles/generators/MID1/MID1_Generate_Evoker.simc` |

## Two kinds of "definition" — don't confuse them

SimC has **two** layers, and the earlier confusion came from conflating them:

1. **Pre-built gear profiles** (`profiles/MID1/*.simc`) — a specific
   character: ilvl ~289 gear, talent string, consumables. SimC only ships
   these for **Devastation** (SC default + FS). It does **not** ship a
   pre-built *gear* profile for Augmentation.
2. **Spec / rotation definitions** (`ActionPriorityLists/` +
   `engine/class_modules/apl/apl_evoker.cpp` + `sc_evoker.cpp`) — the actual
   APL and spell behavior. These **do** exist for **Augmentation**. This is
   what Raidbots/any analyzer drives when you paste your own armory string,
   and it's almost certainly what the Aug reports in this repo were built on.

So "no Aug profile" was only true for layer 1 (pre-built gear), and misleading.
The Augmentation *definition* is fully present — `evoker_augmentation_apl.simc`
in this folder.

## SimC supports Mythic+ / cleave fight styles (you were right)

SimC is **not** Patchwerk-only. Fight styles are layered on top of any profile
via `fight_style=`, and the engine ships (from `engine/util/util.cpp`):

```
Patchwerk  CastingPatchwerk  Ultraxion  Beastlord
HelterSkelter  LightMovement  HeavyMovement
CleaveAdd  HecticAddCleave  DungeonSlice  DungeonRoute
```

- **`DungeonSlice`** is exactly Raidbots' "Dungeon Slice" sim — a scripted
  mixed single-target + add-wave sequence meant to approximate M+ trash/boss
  pacing. **`DungeonRoute`** is the longer multi-pull variant.
- **`CleaveAdd` / `HecticAddCleave`** are the cleave/AoE styles.

The APLs even branch on the fight style — e.g. the Aug APL contains
`...fight_remains<=30&!fight_style.dungeonroute` (line 48 of
`evoker_augmentation_apl.simc`). So SimC profiles + a dungeon/cleave fight style
*do* produce M+-flavored numbers; that's the pipeline Raidbots exposes.

(Honest limit: even `DungeonSlice`/`DungeonRoute` are *scripted* add sequences.
They capture target count, add timing, and cleave throughput, but not routing,
boss mechanics, forced movement beyond the canned `raid_event.movement`, or
defensive checks. They're a strong proxy for M+ damage profile, not a literal
key.)

## The actual answer: SimC's own defaults encode Scale Commander for BOTH specs

The strongest evidence is that **SimC's default rotations are written around
Scale Commander mechanics for both specs** — you don't have to take a meta
report's word for it:

### Devastation
`MID1_Evoker_Devastation_SC.simc` is `source=default`. The shared APL routes by
hero tree:

```
actions+=/run_action_list,name=sc,if=talent.mass_disintegrate   # Scale Commander
actions+=/run_action_list,name=aoe_fs,if=active_enemies>=3       # Flameshaper
actions+=/run_action_list,name=st_fs
```

The `sc` list is built around **empower → Mass Disintegrate → Bombardments**:
casting an empower (Fire Breath / Eternity Surge) grants `mass_disintegrate_stacks`, which makes the next **Disintegrate cleave** to up to 3 targets — it
stays a **channel** (`channeled=true`, `sc_evoker.cpp:6113`; it is *not* instant,
and you move during it with **Hover**);
*spending* that Mass Disintegrate is what **applies the `bombardments` debuff to
the primary target** (`target_if=min:debuff.bombardments.remains`), and your
subsequent damage to a marked target procs the bomb explosions. **Deep Breath
does NOT apply or spread Bombardments** — its Scale Commander role is **Melt
Armor** (a ~20% damage-taken debuff) plus the **Strafing Run** recast. See
`EVOKER_MIDNIGHT_MECHANICS.md` for the full source-verified chain (an earlier
draft of this file wrongly said Deep Breath spreads Bombardments). Flameshaper's
lists are instead a `fire_breath` DoT-ramp / `pyre` / `consume_flame` pattern
that wants you stationary and wants targets to live.

### Augmentation
`evoker_augmentation_apl.simc` — the **default** Aug rotation — is likewise
written around Scale Commander:

```
actions.precombat+=/variable,name=bombardments_pooling,...,default=1
...
actions+=/eruption,target_if=min:debuff.bombardments.remains,if=buff.mass_eruption_stacks.up
actions+=/eruption,target_if=max:debuff.bombardments.remains,if=debuff.bombardments.remains>execute_time|...
```

`bombardments` and `mass_eruption` are **Scale Commander** mechanics. SimC's
default Augmentation rotation pools Eruptions and spreads them across bombarded
targets — i.e. the maintained, supported build *is* the Scale Commander one.
(Ebon Might / Prescience / Breath of Eons — the support core — are present
regardless of hero tree; the hero choice is decided by the personal/AoE damage
layer, and SimC's default picks SC.)

### Why this is the M+ pick (mechanical reasoning)
> Note: Mass Disintegrate (channel) and Mass Eruption (hard-cast) are **not
> instant** — Evoker moves while casting via **Hover**. See
> `EVOKER_MIDNIGHT_MECHANICS.md` §3 for the corrected reasoning.

1. **High cleave per cast/channel.** Mass Disintegrate / Mass Eruption make the
   main spender hit up to 3 targets, so each one does AoE as density rises — at
   no rotational cost.
2. **Bombardments scales with density.** Partly allied-damage-driven, splitting
   among nearby mobs, so its value climbs with pack size — high-key trash is
   dense, and it needs no extra casts.
3. **More mobile-casting uptime.** SC's Deep Breath / Maneuverability refund
   Hover, giving more windows to keep channeling while repositioning (the spell
   stays a channel — Hover is what covers the movement).
4. Under a `DungeonSlice`/`HecticAddCleave` fight style these mechanics are
   precisely what gets rewarded, which is why the default APLs are SC-shaped.

## Cross-check against this repo's own logs
The Augmentation reports here (`20260507_090328_Alokys.html`,
`20260508_211858_Dzin.html`) track **`Bombardments` uptime** as a metric, e.g.:

```
<span class="label">Bombardments</span><span class="value val-warn">32% ...
```

Bombardments only exists on the **Scale Commander** tree — so those Aug players
are confirmed Scale Commander, matching SimC's default Aug APL.

## Sources
- [`simc` profiles, `midnight`](https://github.com/simulationcraft/simc/tree/midnight/profiles/MID1)
- [`MID1_Evoker_Devastation.simc` (SC default)](https://github.com/simulationcraft/simc/blob/midnight/profiles/MID1/MID1_Evoker_Devastation.simc)
- [`MID1_Evoker_Devastation_FS.simc`](https://github.com/simulationcraft/simc/blob/midnight/profiles/MID1/MID1_Evoker_Devastation_FS.simc)
- [`ActionPriorityLists/default/evoker_augmentation.simc` (Aug rotation)](https://github.com/simulationcraft/simc/blob/midnight/ActionPriorityLists/default/evoker_augmentation.simc)
- [`engine/class_modules/apl/apl_evoker.cpp`](https://github.com/simulationcraft/simc/blob/midnight/engine/class_modules/apl/apl_evoker.cpp)
- [Fight styles in `engine/util/util.cpp`](https://github.com/simulationcraft/simc/blob/midnight/engine/util/util.cpp)
- This repo's Aug logs (Bombardments uptime → Scale Commander).
</content>
