# Evoker DPS in-depth analysis — WoW *Midnight* S1 (12.0.5, ~June 2026)

This is the **synthesis** doc: it answers the driving question — *why does
everyone run Scale Commander for both Devastation and Augmentation in high
Mythic+?* — with every claim grounded in the extracted research. Citations:

- **[abil]** `EVOKER_MIDNIGHT_ABILITIES.md` (SimC spell-data, value-resolved)
- **[tal]** `EVOKER_MIDNIGHT_TALENTS.md` (full talent catalog, value-resolved)
- **[mech]** `EVOKER_MIDNIGHT_MECHANICS.md` (incl. §0 Bombardments, §4 Essence Burst)
- **[APL]** the SimC action lists in this folder (`MID1_Evoker_Devastation*.simc`, `evoker_augmentation_apl.simc`)
- **[src]** `sc_evoker.cpp` (engine implementation; line numbers)
- **[sim]** `EVOKER_MIDNIGHT_SIM_RESULTS.md` (our own SimC 12.0.5 run, SC vs FS)
- **[meta]** Archon.gg / Murlok.io / Maxroll / Icy Veins (patch 12.0.5)

Values are current-build but patch-volatile — Wowhead spell links in the
companion docs give live numbers. `N` in those docs = spell-power-scaled or
max-stack values absent from the static dump.

---

## 1. The shared engine: Essence, Essence Burst, empowers

Both DPS specs run the same resource loop, which is what the hero trees bend.

- **Essence** regenerates ~1 per 5 s (Innate Magic +X% [tal]). The core spenders
  cost **3 Essence**: Disintegrate, Pyre (Dev) and Eruption (Aug) [abil].
- **Essence Burst (EB)** makes the next spender free; **max 1 stack → 2 with
  Essence Attunement**, and **Hoarded Power** can refund it on spend [mech §4].
- **Empower spells** (Fire Breath, Eternity Surge — Dev; Fire Breath, Upheaval —
  Aug) are the engine's heartbeat: `GCD 0.5s`, hold-to-empower to rank 1–4,
  ~30 s cooldowns [abil]. Casting an empower is *also* what grants **Mass
  Disintegrate / Mass Eruption** stacks under Scale Commander [src 4407-4411] —
  see §3.
- **Dragonrage** (Dev, 120 s / 18 s [abil]) guarantees EB on fillers and, via the
  Midnight apex **Rising Fury**, drips EB and stacks +4% haste/6 s [mech §4, tal].

**EB economy is the first place the hero trees diverge** [mech §4]:
- **Flameshaper** *adds* EB: Titanic Precision (crit → extra roll) + Essence Well
  (Fire Breath ~50% → EB) [tal, src 4933/5060].
- **Chronowarden** *adds* EB: Energy Cycles (Temporal Burst → EB every ~6 s) [src 10296].
- **Scale Commander** adds essentially **none** — only Diverted Power
  (Bombardments → ~8.5% EB [src 7823]), a choice node vs Extended Battle that is
  considered undertuned and rarely taken [meta].
- **Takeaway:** Scale Commander is *not* chosen for resource generation — it has
  the weakest EB toolkit of the three trees. Its case is throughput + mobility
  (§3–§5), and it accepts the baseline EB economy.

---

## 2. How each spec actually deals damage

### Devastation (selfish ranged burst)
Single-target spine is the **Disintegrate** channel (3 s, SP×1.59/tick, 3
Essence [abil]), recast-chained for uptime [mech §1]. AoE is **Pyre** (instant,
8-yd splash [abil]). Empowers (**Fire Breath** DoT, **Eternity Surge** = targets
scale with rank, doubled by Eternity's Span [tal]) are cast on cooldown, ideally
inside **Dragonrage**. **Shattering Star** is now passive (**Shattering Stars**:
Eternity Surge fires a Spellfrost bolt, SP×1.74, applies a damage-taken debuff)
— a Midnight change from the old standalone button [abil].

### Augmentation (support DPS)
Most of Aug's value is **buffing allies**, so its "damage" is indirect [meta]:
- **Ebon Might** — Midnight: **raid-wide (≤30 targets), +8% primary stat** to
  allies and **+20% to your own** damage, 10 s, refreshed constantly (cast 1.5 s,
  30 s CD) [abil, meta]. The whole rotation exists to keep it at max uptime.
- **Prescience** — instant, **2 charges/12 s**, +3% ally crit + copies 15% of
  their casts, 18 s [abil].
- **Breath of Eons** — 120 s [abil]; stores **15%** of allied damage then
  detonates; the skill ceiling is aligning ally cooldowns inside it [meta].
- Personal damage: **Eruption** (cast 2.5 s, SP×2.8, 3 Essence [abil]) maintains
  Ebon Might; **Upheaval** empower feeds Mass Eruption.

This is why **SimC ships no standalone Augmentation profile** [mech]: a solo
Patchwerk run has no allies for Ebon Might/Prescience/Breath of Eons to buff, so
it's meaningless. Aug **can** be simmed in SimC/Raidbots, but only as a **group
sim** — the engine applies its buffs across `sim->player_no_pet_list` /
`allied_augmentations` [src 1088/4645/7249] — and the result is highly sensitive
to the assumed ally roster and their cooldown alignment with Breath of Eons.
That roster-dependence (not an engine limitation) is why the Aug hero-tree
verdict leans on logs rather than a single decisive sim.

---

## 3. The Scale Commander machine (shared by both specs)

The tree's identity is a single chain, verified end-to-end in the engine
[mech §0, src]:

1. **Empower** (Fire Breath / Eternity Surge / Upheaval) → grants **Mass
   Disintegrate** / **Mass Eruption** (15 s buff window) [abil, src 4407-4411].
2. **Spend** it: the next **Disintegrate / Eruption** strikes **up to 3 targets**,
   **+10% damage per missing target below 3** [abil]. *(SimC dump resolves +10%;
   some guides cite +25% — flag, verify live [meta].)* It is **still a channel /
   cast — not instant**; the SC APL only fires it when `raid_event.movement.in>2`
   **or `buff.hover.up`** [APL] — i.e. **Hover is the mobility, not the spell**
   [mech §0].
3. On the **primary-target impact**, spending Mass Disint/Erupt **applies the
   `bombardments` debuff** (6 s) [src 5583/6250]. The APL spreads it with
   `target_if=min:debuff.bombardments.remains` [APL].
4. While the debuff is up, **you and allies** damaging the marked target have an
   **RPPM chance to fire a Bombardment** (Volcanic, **SP×4.75**, split among
   nearby enemies) [abil, src 8336]. **Extended Battle** extends it +1 s/Essence
   ability [tal].
5. **Deep Breath** (Dev) / **Breath of Eons** (Aug) layers **Melt Armor**:
   **+20% damage taken** from Disintegrate/Pyre/Bombardments for 12 s [abil].
   It does **not** apply Bombardments [mech §0]. **Wingleader** turns Bombardment
   hits into cooldown reduction — Deep Breath −0.5 s/target (≤1.5 s) for Dev;
   **Breath of Eons** for Aug [tal].
6. **Mobility kit:** **Strafing Run** (Dev spec talent — recast Deep Breath
   within ~18 s [tal]), **Slipstream/Maneuverability** (Deep Breath / Breath of
   Eons **refunds a Hover charge**, and Breath becomes steerable [tal]).

**Net:** Scale Commander converts the empower→spender loop into **3-target
cleave + a density-scaling, partly-passive Bombardment stream + a 20% group
amp + extra Hover uptime** — at the cost of adding ~no Essence Burst.

### Why Aug's SC loop is special: the Breath-of-Eons flywheel
For Augmentation specifically, **Wingleader** ties Bombardments to **Breath of
Eons cooldown reduction** [tal], pulling its 120 s CD down toward ~60–90 s in
dense pulls [meta]. More Breath casts → more **Duplicate** (Midnight apex) and
Ebon-Might uptime. The Aug APL encodes this: `bombardments_pooling` defaults on,
and Eruptions are pooled/spread via `target_if=…debuff.bombardments` [APL].
Chronowarden has no equivalent density→cooldown loop.

---

## 4. The alternatives, and what they trade away

### Flameshaper (Devastation alt) — sustained fire ramp [tal, mech §1]
+1 Fire Breath charge; **Consume Flame** capstone: Essence spenders **eat Fire
Breath DoT and detonate it as AoE** (Disintegrate ~2 s, Pyre ~10 s). Richer EB
(Titanic Precision + Essence Well). **Profile:** wants to **stand still**, keep
Fire Breath rolling across a pack, then cash out — best in **long, sustained
AoE**; a 12.0.5 buff puts it slightly ahead on **pure single target** [meta].

### Chronowarden (Augmentation alt) — temporal/single-target [tal, mech §4]
**Temporal Burst** (CD-recovery ramp), **Energy Cycles** (steady EB), **Chrono
Flame**. **Profile:** smooth, rewards **landing Breath of Eons inside
coordinated ally burst windows** — ~**4%** ahead on pure single-target raid when
the group executes perfectly [meta].

---

## 5. Answering the question: why Scale Commander in *high* M+ (both specs)

### The data (not opinion) [meta]
- **Devastation:** Scale Commander ≈ **93%** in high keys, ≈ **67%** across lower
  keys — **dominance rises with key level** (Archon top ~5%).
- **Augmentation:** Scale Commander ≈ **99%** in M+ vs only ≈ **52%** in raid —
  the choice is **M+-specific**, not a blanket "SC is better."

### The mechanical drivers, each tied to a number
1. **Cleave per cast, scaling with density.** One Disintegrate channel / Eruption
   cast hits **3 targets** (+10%/missing) [abil] — every spender becomes AoE as
   packs grow. Flameshaper's ramp and Chronowarden's window-play give this up.
2. **Partly-passive, density-scaling Bombardments** (SP×4.75, allied-damage
   driven [abil, src]) — value climbs directly with pack size; high-key trash is
   dense. Needs no extra casts.
3. **Aug's Breath-of-Eons flywheel** (Wingleader CDR → more Breath → more
   Duplicate/Ebon Might [tal, meta]) — uniquely strong in dense M+, absent on
   Chronowarden. This is the single biggest reason Aug is ~99% SC.
4. **Group amp on demand** — Melt Armor **+20%** on a fresh pack [abil].
5. **Mobility via Hover economy** — Deep Breath/Maneuverability/Slipstream
   **refund Hover** [tal], so the channels stay castable through M+'s constant
   movement. (The spells are channels — Hover is the enabler [mech §0, APL].)
6. **Lower execution variance** — SC leans on throughput, not on allies or
   perfect timing; that matters more as keys get deadlier and rotations break.

### What the sim actually says (we ran it — see `EVOKER_MIDNIGHT_SIM_RESULTS.md`)
We built SimC (midnight, 12.0.5.67823) and ran SC vs FS head-to-head. The result
**refines — and partly contradicts — the naive "SC wins M+" story** [sim]:
- **Stacked-target Patchwerk:** SC is strongly ahead at 2–6 targets, **peaking
  +38% at 3T** (the Mass Disintegrate 3-target cap), tapering to +5% at 10T;
  FS edges pure 1T by ~2%.
- **M+-shaped fight styles:** **Flameshaper sims HIGHER** — DungeonSlice −7% and
  HecticAddCleave −14% *for SC*. So raw sim DPS in the sustained M+ abstractions
  does **not** justify the SC meta.
- SimC's **default** Dev profile is nonetheless the SC build (`source=default`)
  and the **default Aug APL is written around SC** [APL] — the theorycraft
  *baseline* assumes SC even though the sustained M+ styles favour FS.

**Reconciliation:** the M+ fight styles are *sustained* (targets live long),
over-crediting FS's DoT-ramp/Consume Flame and its ST edge. Real high keys
**burst packs down in seconds**, so FS's ramp never matures while SC's
front-loaded Mass Disintegrate + Bombardments + Deep Breath lands instantly —
the Patchwerk **2–5T (+17–38%)** numbers are the better proxy for a real
pull-burst. Net: the 93% is **real burst-window tuning + un-simmable
pacing/mobility + some meta bias**, *not* a raw-DPS verdict the sim prints. Even
DungeonSlice is scripted — it captures target count, not routing, time-to-die,
forced movement, deaths, defensives or interrupts, which is *why live M+ skews
to SC harder than the sustained sim deltas predict* [sim, meta].

---

## 6. Honest limitations & open flags
- **Channel ≠ instant** (corrected): the SC throughput is real, but it is *not*
  movement-free; it depends on Hover uptime [mech §0].
- **EB economy:** SC adds the least Essence Burst of the three trees [mech §4] —
  its case is throughput/mobility, not resources.
- **Value discrepancies to verify live:** Mass Disint/Erupt per-missing bonus
  (dump 10% vs guides 25%); Bombardments debuff 6 s vs older 10 s; Arcane Vigor /
  Shattering-Star→EB claimed by Icy Veins but **absent in the SimC source**
  [mech §4]; a reported Mass-Eruption-amp bug [meta]; max-stack counts not in the
  dump (`N`).
- **Dev M+ guide split:** Icy Veins theorycrafts Flameshaper for ultra-dense
  sustained AoE; Archon representation favors SC and rises with key level [meta].
- **Scope:** Preservation excluded; no SimC Aug gear profile exists (APL only);
  the repo's WCL logs were **not** re-parsed for per-player builds (SC inferred
  from Bombardments uptime [mech]).

## Sources
SimC `midnight`: [`sc_evoker.cpp`](https://github.com/simulationcraft/simc/blob/midnight/engine/class_modules/sc_evoker.cpp), [`apl_evoker.cpp`](https://github.com/simulationcraft/simc/blob/midnight/engine/class_modules/apl/apl_evoker.cpp), [`SpellDataDump/evoker.txt`](https://github.com/simulationcraft/simc/blob/midnight/SpellDataDump/evoker.txt), [`util.cpp`](https://github.com/simulationcraft/simc/blob/midnight/engine/util/util.cpp). Meta: [Archon Dev M+](https://www.archon.gg/wow/builds/devastation/evoker/mythic-plus/talents/high-keys/all-dungeons/this-week), [Archon Aug M+](https://www.archon.gg/wow/builds/augmentation/evoker/mythic-plus/talents/high-keys/all-dungeons/this-week), [Maxroll Dev M+](https://maxroll.gg/wow/class-guides/devastation-evoker-mythic-plus-guide), [Maxroll Aug M+](https://maxroll.gg/wow/class-guides/augmentation-evoker-mythic-plus-guide), [Icy Veins Dev](https://www.icy-veins.com/wow/devastation-evoker-pve-dps-guide). Companion docs in this folder.
</content>
