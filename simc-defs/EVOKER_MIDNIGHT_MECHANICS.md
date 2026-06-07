# Evoker DPS mechanics — WoW *Midnight* Season 1 (patch 12.0.5, ~June 2026)

Knowledge-grounding doc for analyzing this repo's M+ logs. Two evidence tiers:

- **[SimC]** = verified directly in SimulationCraft `midnight` branch source
  (`engine/class_modules/sc_evoker.cpp`, `apl_evoker.cpp`). Authoritative for
  *how the mechanic works*; line numbers cited.
- **[Guide]** = Icy Veins / Wowhead / Method / Maxroll / Archon / Murlok
  (patch 12.0.5, indexed June 2026). Authoritative for *tuning, tooltips, and
  meta*; URLs cited. Numbers are patch-volatile — spot-check live.

> **Terminology:** the Augmentation time tree is **Chronowarden** (Bronze
> dragonflight). "Chronomancer" is a common misnomer and appears in no current
> guide — use **Chronowarden**. [Guide]

---

## 0. The Bombardments correction (read this first)

A previous analysis claimed *"Bombardments is spread by Deep Breath."* **That is
wrong.** The real chain, verified in SimC source and confirmed by Wowhead's
tooltip:

1. **Cast an empower** — Fire Breath / Eternity Surge (Dev) or Fire Breath /
   Upheaval (Aug). This grants **Mass Disintegrate** / **Mass Eruption** stacks.
   [SimC `sc_evoker.cpp:4407-4411`]
2. **Spend the stack** — the next **Disintegrate** (Dev) / **Eruption** (Aug)
   gains **cleave** (strikes up to 3 targets, +damage per missing target below
   3), and **on its primary-target impact it applies the `bombardments` debuff**
   to that target. **These spells are NOT instant:** Disintegrate stays a
   **channel** (`channeled = true`, `sc_evoker.cpp:6113` — Mass Disintegrate only
   adds targets/tick-damage, it never removes the channel) and Eruption stays a
   **hard-cast**. To move while channeling/casting you need **Hover** — that is
   Evoker's mobility tool, not these spells. [SimC `sc_evoker.cpp:6250-6253`
   (Dev), `5583-5586` (Aug); channel flag `6113`]
3. **Proc the bombs** — while the debuff is up, *you and your allies* damaging
   the marked target have an **RPPM chance to trigger a Bombardment**, dealing
   Volcanic damage split among nearby enemies. [SimC proc-callback
   `sc_evoker.cpp:8336+`; `apply_bombardments` at `10922` resets the proc CD.
   The `evoker.simulate_bombardments` option approximates the allied-damage
   proc with RPPM — SimC wiki]
   Tooltip: *"…marks your primary target… You and your allies have a chance to
   trigger a Bombardment when attacking marked targets, dealing Volcanic damage
   split amongst all nearby enemies."* [Guide: wowhead.com/spell=434300]
4. **Deep Breath's actual Scale Commander role** is **Melt Armor** (applies a
   damage-taken debuff on impact — ~20% from Disintegrate/Pyre/Bombardments)
   and **Strafing Run** (lets Deep Breath be recast within ~18s). It does **not**
   apply or spread the Bombardments mark. [SimC: Deep Breath dot impact →
   `melt_armor->trigger()` `sc_evoker.cpp:5852`; execute → `strafing_run->trigger()`
   `6076`]

Relevant spell IDs [SimC]: `bombardments_debuff` 434473, `bombardments_driver`
443788 (RPPM), `bombardments_damage` 434481, `mass_disintegrate_buff` 436336,
`mass_eruption_buff` 438588, `mass_eruption_damage` 438653.

**Debuff duration is patch-volatile:** current Wowhead spell data shows ~**6s**;
older (War Within-era) guides say 10s. **Extended Battle** extends it +1s per
Essence ability. Treat 6s as the current Midnight value but verify live. [Guide]

---

## 1. Devastation Evoker

### Core kit
- **Essence / Essence Burst** — Essence regens ~1/5s; **Essence Burst** (procs
  from Living Flame/Azure Strike) makes the next spender free; guaranteed on
  fillers during Dragonrage. [Guide: Icy Veins, Method]
- **Disintegrate** — channeled single-target spender; **chained** (recast just
  after the last tick) for a DPS gain. [Guide]
- **Pyre** — instant AoE spender, 3 Essence (reduced by Imminent Destruction).
  [Guide]
- **Fire Breath** — empower; front-load + DoT; usually cast at **Empower R1**.
  [Guide]
- **Eternity Surge** — empower; rank = targets hit (R1–R4 = 1/2/3/4, doubled by
  **Eternity's Span**). [Guide]
- **Dragonrage** — ~2-min burst CD; Midnight Apex **Rising Fury** ramps Haste
  +4%/6s up to 20% and adds a 15% damage boost at 5 stacks. [Guide]
- **Shattering Star** — ~20% damage-taken debuff, ~15s CD, opens burst. [Guide]
- **Deep Breath** — flying AoE; Midnight **Imminent Destruction** redesign:
  reduces Essence cost of the next 4 Disintegrate/Pyre by 1, stacking to 8.
  [Guide]
- **Living Flame / Azure Strike** — fillers that farm Essence Burst. [Guide]

### Hero tree A — **Flameshaper** (the Scale Commander alternative for Dev)
**Reworked in Midnight.** The old TWW signature **Engulf was REMOVED** (so was
Firestorm) — any guide still listing Engulf is stale TWW content. [Guide:
Method, Blizzard forums]

- Grants an **extra Fire Breath charge**; the tree revolves around maximizing
  Fire Breath DoT uptime/stacking. [Guide]
- **Consume Flame** (capstone, replaces Engulf): Essence spenders **eat Fire
  Breath DoT duration and detonate it as AoE** — Disintegrate consumes ~2s,
  Pyre ~10s, detonating for ~150% of that damage in an area. [Guide: Murlok]
- **Enkindle / Ruby Embers** — extra continuous fire-DoT layers feeding the
  ramp. [Guide]
- **Playstyle:** a **channeled DoT-ramp / cash-out** spec — stack Fire Breath
  across targets, then detonate with Disintegrate/Pyre. Wants you stationary,
  wants targets to live, rewards **long, sustained AoE**.

### Hero tree B — **Scale Commander** (Dev)
- **Mass Disintegrate** — empower makes the next Disintegrate hit up to 3
  targets (+damage per missing target below 3) with no extra spec-tree cost.
  **Still a channel** — it is cleave, not an instant; move during it with Hover.
  [Guide] [SimC: stacks at `4407`, channel flag `6113`, cleave + Bombardments
  apply at `6235-6257`]
- **Bombardments** — see §0. Density-scaling, partly allied-damage-driven AoE.
- **Strafing Run** — Deep Breath hits harder and is **recastable within ~18s**.
  [Guide] [SimC `6076`]
- **Melt Armor** — Deep Breath marks enemies to take increased Disintegrate/
  Pyre/Bombardment damage (~20%). [Guide] [SimC `5852`]
- **Wingleader** — Bombardments reduce Deep Breath CD ~1s/target (≤3s). [Guide]
- **Extended Battle** (+1s Bombardments/Essence ability), **Diverted Power**
  (Bombardments → chance at Essence Burst), **Maneuverability** (steerable Deep
  Breath, Hover refund → near-unlimited movement). [Guide]
- **Playstyle:** high **channeled/cast cleave** with strong spread cleave and
  minimal loss on target swaps. Mobility is **Hover-based** — the SC edge is
  that Deep Breath/Maneuverability **refund Hover**, so you get more windows to
  channel Mass Disintegrate *while* moving (not that the spell is instant).

---

## 2. Augmentation Evoker

Augmentation is the game's only **support DPS** — most of its throughput is the
buffs/amps it gives allies, not its own damage. [Guide]

### Core kit
- **Ebon Might** — signature buff; **Midnight: raid/group-wide (100 yd) to all
  DPS, 8% primary stat** (was ~4 targets / 5%). The rotation exists to keep it
  at max uptime, refreshed by Essence spends (Eruption) and empowers (Upheaval).
  Stored damage is reduced when buffing >2 allies. [Guide]
- **Prescience** — buffs an ally's Crit (3%, 4% w/ Nozdormu Adept); can
  smart-buff random DPS if cast at an enemy. [Guide]
- **Breath of Eons** — major group multiplier: stores **15% of allied damage**
  (was 10%) on the target, then detonates. The core skill is aligning allied
  cooldowns inside the window. Midnight Apex **Duplicate** spawns a spectral
  copy after Breath. [Guide]
- **Eruption** — primary Essence spender, **replaces Disintegrate**; maintains
  Ebon Might. [Guide]
- **Upheaval** — empower; burst + maintains Ebon Might + feeds Mass Eruption.
  [Guide]
- **Blistering Scales** — defensive: grants an ally 20% of your armor. [Guide]

### Hero tree A — **Chronowarden** (the Scale Commander alternative for Aug)
Bronze-dragonflight time manipulation; smoother, **single-target / raid-leaning**.

- **Temporal Burst / Time Skip** — Tip the Scales overloads you with temporal
  energy: ramps Haste, movement, and **cooldown-recovery rate up to ~40% over
  20s**. New Midnight nodes **Chronoboon** (−30s Tip the Scales CD) and
  **Nozdormu Adept** (−2s Prescience CD, crit buff 3%→4%). [Guide]
- **Chrono Flame / Warp** — empowers fire up to 3 Chrono Flames (small chance
  to grant Essence Burst); Hover ("Warp") gains −5s CD. [Guide]
- **Threads of Fate / Interwoven Threads** — empowers amplify active Threads
  (+100% power, stacks 2). ⚠️ **Source disagreement / in flux:** at least one
  source says Threads of Fate was reworked/removed — verify for current patch.
  [Guide]
- **Playstyle:** sustained, precise; **wins by landing Breath of Eons inside
  coordinated ally burst windows** — best when the group executes perfectly.

### Hero tree B — **Scale Commander** (Aug)
- **Mass Eruption** — empower makes the next Eruption hit up to 3 targets
  (+25% per missing target below 3), stacks to 2; Aug's main AoE/personal tool
  and the gateway into Bombardments. [Guide] [SimC: stacks at `4410`, amp +
  Bombardments apply at `5560-5586`]
- **Bombardments** — see §0. Does **not** pandemic, so you can chain two Mass
  Eruptions back-to-back without losing uptime. [Guide]
- **Wingleader** — Bombardments reduce **Breath of Eons** CD, pulling it to
  ~60–90s depending on target count → more Breath casts → more **Duplicate**
  uptime. Cited as the main mechanical edge over Chronowarden in M+. [Guide]
- ⚠️ **Known bug (flag):** Mass Eruption reportedly fails to be amplified by
  Melt Armor / Imminent Destruction / Unrelenting Siege. [Guide: Maxroll]
- **Playstyle:** more personal/AoE damage, density-scaling, **forgiving of
  mis-timed group cooldowns** — better for chaotic M+.

---

## 3. Why Scale Commander dominates *high-tier* M+ for both specs

### Hard representation data [Guide: Archon.gg, top ~5%, trailing ~14d]
- **Devastation:** Scale Commander ≈ **93%** in high keys, but only ~**67%**
  across lower keys (+7–23) — **dominance grows with key level.**
- **Augmentation:** Scale Commander ≈ **99%** in M+ vs only ~**52%** in raid —
  the choice is M+-specific, not a blanket "SC is better."
- Murlok.io top-50 sampling agrees (~98% SC for both in M+).

> So your premise is correct *for high keys specifically.* Note one nuance: a
> few guides (Icy Veins) theorycraft **Flameshaper** for very-high-density
> sustained-AoE M+ via Consume Flame detonations; Maxroll/Archon data favors
> Scale Commander. The split is "does the pull last long enough for
> Flameshaper's ramp" — and in high keys (more movement, more death-driven
> short windows) it usually doesn't, which is why the data trends to SC as keys
> scale up.

### The shared mechanical thesis
> **Correction:** Mass Disintegrate and Mass Eruption are **NOT instant** and
> not freely castable while moving. Disintegrate is **channeled**, Eruption is a
> **hard-cast**, and the *only* way to move while casting either is **Hover**.
> The SC edge is throughput + Hover uptime, not instant casts.

1. **High cleave per cast/channel.** Mass Disintegrate makes one Disintegrate
   channel hit up to 3 targets; Mass Eruption makes one Eruption cast hit up to
   3 — so each spender does AoE instead of single-target. That's more damage per
   GCD/channel as density rises, with no rotational cost.
2. **More mobile-casting uptime via Hover.** Evoker casts/channels are made
   mobile by **Hover**; SC's **Deep Breath + Maneuverability refund/extend
   Hover**, so you get more windows to keep channeling Mass Disintegrate *while*
   repositioning. M+ is constant movement, so this Hover economy matters — but
   the spell itself is still a channel, you're just covering it with Hover.
3. **Density-scaling AoE (Bombardments).** Partly *allied-damage-driven* and
   splits among nearby enemies — value rises directly with pack size, and
   high-key trash is dense. This is the part that needs no extra casts.
4. **Cooldown compression (Aug).** Wingleader → Bombardments → shorter Breath
   of Eons → more Duplicate uptime. More packs = more Bombardment hits = faster
   Breath. This loop is uniquely strong in M+ and absent in Chronowarden.
5. **Burst-on-pull amp.** Deep Breath (Melt Armor ~20% amp + Strafing Run
   recast + Hover refund) lets you set up amplified AoE on a fresh pack and keep
   Hover-mobile — matching how high keys burst packs inside a CC/cooldown window
   rather than sustaining over minutes.
6. **Lower execution variance.** Both SC builds are more forgiving — less
   reliant on allies or on perfect timing — which matters more as keys get
   deadlier.

### What SimC does and doesn't capture
- SimC's **default** Devastation profile is the Scale Commander build
  (`source=default`), and its **default Augmentation APL is written around
  Scale Commander** (`bombardments_pooling`, `mass_eruption_stacks`,
  `target_if=…debuff.bombardments`). So the theorycraft baseline already
  assumes SC. [SimC]
- SimC supports M+-flavored **fight styles** (`DungeonSlice`, `DungeonRoute`,
  `CleaveAdd`, `HecticAddCleave`) layered on these profiles — this is what
  Raidbots' "Dungeon Slice" uses, and the APLs branch on `fight_style.*`. Under
  those styles SC's cleave throughput is exactly what's rewarded. [SimC
  `engine/util/util.cpp`]
- **But:** even DungeonSlice is a *scripted* add sequence. It captures target
  count, add timing, and cleave throughput — **not** routing, boss mechanics,
  forced movement, deaths, defensives, or interrupt assignments. The biggest
  real-world SC advantages (Hover-covered cleave during movement, burst-on-pull,
  mis-timing tolerance) are therefore **under-credited** by any sim, which is
  *why the live M+ representation skews to SC harder than raw sim deltas alone
  would predict.*

---

## 4. Essence Burst generation — by spec & hero tree

**Essence Burst (EB)** makes the next Essence spender free (Eruption for Aug;
Disintegrate/Pyre for Dev). Base **max 1 stack → 2 with Essence Attunement**;
**Hoarded Power** gives a chance to *not* consume EB when spent. [SimC EB buff
`sc_evoker.cpp:10029-10037`, Essence Attunement `1312`, Hoarded Power `3019`]
[Guide: [Wowhead 359618](https://www.wowhead.com/spell=359618/essence-burst),
[Essence Attunement 375722](https://www.wowhead.com/spell=375722/essence-attunement)]

### Shared baseline (both specs, class/spec trees — independent of hero tree)
- **Ruby Essence Burst → Living Flame** ~20% chance (scales with Inner Flame /
  Leaping Flames). [SimC `4916, 6673, 9917`] [Guide]
- **Azure Essence Burst → Azure Strike** ~15% chance (also Inner-Flame-scaled).
  [SimC `5314`] [Guide]
- **Pupil of Alexstrasza** → extra Living Flame EB roll on single target. [SimC
  `9913-9922`]

### Devastation — EB generation **differs by hero tree**
- **Spec/class baseline:** the two fillers above **plus**:
  - **Dragonrage** — *guarantees* EB on fillers (Living Flame) while up. [SimC
    `6673`: `buff.dragonrage.up() || roll`] [Guide]
  - **Risen Fury** (Rising Fury apex, **Midnight-new**) — grants an EB every ~4s
    as it decays after Dragonrage. [SimC `10108`] [Guide: Wowhead 1271788]
- **Flameshaper ADDS** (verified under `struct flameshaper_t`, `sc_evoker.cpp:1449-1471`):
  - **Titanic Precision** — Living Flame / Azure Strike **crits** get an extra EB
    roll. [SimC `4933, 4952, 5314`]
  - **Essence Well** — **Fire Breath** has a ~50% chance to grant EB. [SimC
    `5060`] [Guide: Wowhead 1265993]
  → Flameshaper's EB is **crit- and Fire-Breath-driven**, feeding its
  Essence-hungry Consume Flame ramp.
- **Scale Commander ADDS** only **Diverted Power** — Bombardments have a chance
  (~8.5% in sim) to grant EB. [SimC `7919-7922`, declared as hero talent `9887`]
  It's a choice node (vs Extended Battle), considered undertuned and **rarely
  taken**. [Guide: Maxroll] → SC adds **almost no** EB generation in practice.

> ⚠️ **Sim-vs-guide discrepancy:** Icy Veins says **Arcane Vigor** makes
> **Shattering Star** an EB source in Midnight. The SimC `midnight` source has
> **no `arcane_vigor` talent and no Shattering Star → EB trigger** — only
> `scintillation` (Disintegrate ticks proc Eternity Surge, *not* EB). Treat
> Shattering Star → EB as unconfirmed for the current build; verify in-game.

### Augmentation — EB generation **differs by hero tree**
- **Spec/class baseline:** the two fillers above **plus**:
  - **Anachronism** — Prescience has a chance to grant EB. [SimC `7467`] [Guide]
  - **Leaping Flames** extra Living Flames (incl. ally-healing ones) each roll
    the LF EB chance. [Guide: Maxroll]
  - *(Ricocheting Pyroclast is a likely contributor — medium confidence, exact
    EB clause not pinned down. [Guide])*
- **Chronowarden ADDS** (the big one):
  - **Energy Cycles** (**Midnight-new**) — **Temporal Burst grants an EB every
    ~6s** while active. [SimC `chronowarden.energy_cycles`, `10296`] [Guide:
    Wowhead 1260568, Maxroll]
  - **Chrono Flame** inherits the Living Flame EB chance. [Guide]
  → Chronowarden adds a **steady periodic EB drip** in cooldown windows.
- **Scale Commander ADDS** only **Diverted Power** (Bombardments → EB) — same
  rarely-taken choice node as Dev. [SimC `7919`; Guide: Wowhead 441219]

### Bottom line on hero-tree EB differences
The **alternative trees are the ones that boost EB**: **Flameshaper** (Titanic
Precision + Essence Well) for Devastation and **Chronowarden** (Energy Cycles)
for Augmentation. **Scale Commander adds essentially none** (only the
rarely-taken Diverted Power) — so SC players run on the **baseline** EB economy
and lean on raw cleave/Bombardment throughput instead. In other words, Scale
Commander is *not* picked for Essence Burst generation; if anything it has the
weakest EB toolkit, and is chosen despite that for its AoE/density/Hover profile.

---

## 5. Quick War-Within-vs-Midnight flags
- **NEW in Midnight:** Devastation Rising Fury apex; Flameshaper rework (Engulf
  + Firestorm removed → Consume Flame, +1 Fire Breath charge); Deep Breath /
  Imminent Destruction Essence redesign; Pyre + Disintegrate buffs. Aug: raid-
  wide 8% Ebon Might, 15% Breath of Eons, Duplicate apex, Sense Power UI,
  Command Squadron / Concentrated Power / Chronoboon / Nozdormu Adept.
- **Carryover from TWW:** empower system, Dragonrage, Essence/Essence Burst,
  Shattering Star, the Scale Commander toolkit (Mass Disintegrate/Eruption,
  Bombardments, Strafing Run, Melt Armor), and both hero trees themselves.
- **Uncertain / verify live:** Bombardments debuff 6s vs 10s; Threads of Fate
  status; exact tier-list letters; the Mass-Eruption-amp bug.

## Sources
SimC (midnight): [`sc_evoker.cpp`](https://github.com/simulationcraft/simc/blob/midnight/engine/class_modules/sc_evoker.cpp),
[`apl_evoker.cpp`](https://github.com/simulationcraft/simc/blob/midnight/engine/class_modules/apl/apl_evoker.cpp),
[`util.cpp` fight styles](https://github.com/simulationcraft/simc/blob/midnight/engine/util/util.cpp),
[SimC Evokers wiki](https://github.com/simulationcraft/simc/wiki/Evokers).
Guides (12.0.5): [Wowhead Bombardments spell](https://www.wowhead.com/spell=434300/bombardments),
[Wowhead Dev hero talents](https://www.wowhead.com/guide/classes/evoker/devastation/hero-talents),
[Wowhead Aug Midnight S1](https://www.wowhead.com/guide/classes/evoker/augmentation/midnight-season-1),
[Method Dev talents](https://www.method.gg/guides/devastation-evoker/talents),
[Maxroll Dev M+](https://maxroll.gg/wow/class-guides/devastation-evoker-mythic-plus-guide),
[Maxroll Aug M+](https://maxroll.gg/wow/class-guides/augmentation-evoker-mythic-plus-guide),
[Icy Veins Dev builds](https://www.icy-veins.com/wow/devastation-evoker-pve-dps-spec-builds-talents),
[Archon Dev M+ high keys](https://www.archon.gg/wow/builds/devastation/evoker/mythic-plus/talents/high-keys/all-dungeons/this-week),
[Archon Aug M+ high keys](https://www.archon.gg/wow/builds/augmentation/evoker/mythic-plus/talents/high-keys/all-dungeons/this-week),
[Murlok Dev SC M+](https://murlok.io/evoker/devastation/scalecommander/m+),
[Murlok Aug SC M+](https://murlok.io/evoker/augmentation/scalecommander/m+).
</content>
