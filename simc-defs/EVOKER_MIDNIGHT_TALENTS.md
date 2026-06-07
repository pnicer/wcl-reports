# Evoker talent catalog — WoW *Midnight* Season 1 (patch 12.0.5, ~June 2026)

Complete, correctly-attributed talent reference for the two DPS Evoker specs,
auto-extracted from SimulationCraft (`midnight` branch) and lightly cleaned.
Companion to `EVOKER_MIDNIGHT_MECHANICS.md` (which carries the narrative + the
"why Scale Commander" analysis); this file is the exhaustive node list that the
mechanics doc's §6 flagged as missing.

## How to read this
- **Source of truth:** tree placement, row, spec, and tooltip text come from
  `SpellDataDump/evoker.txt`; hero/spec/class classification cross-checked
  against `sc_evoker.cpp` (`HT()`/`ST()`/`CT()`). This is authoritative for the
  current build and avoids the guide sites (which 403 our fetcher).
- **`N` = a tuning value** (a spell-effect coefficient) that the data dump does
  **not** resolve inline. Numbers are patch-volatile anyway — click the spell-id
  link (→ Wowhead) for the live value.
- **Rows** are the talent's row in its tree (proxy for how deep/gated it is).
- Preservation (healer) spec talents are excluded; the **hero trees are
  included in full** because Devastation/Augmentation use them.

## ⚠️ Hero-tree tooltips show spec-flavored text — read this
The hero trees are **shared** across specs, and the dump prints one spec's
wording:
- **Scale Commander** text says **"Breath of Eons"** (Augmentation's flying
  breath). **For Devastation, read that as "Deep Breath"** — they are the same
  spell slot for these interactions (Melt Armor, Wingleader, Slipstream,
  Command Squadron, Maneuverability all key off it).
- **Scale Commander row 1 has two spec variants:** **Mass Disintegrate**
  (Devastation) and **Mass Eruption** (Augmentation) — the same node, different
  spender.
- **Chronowarden** tooltips reference **Preservation** healing spells (Verdant
  Embrace, Dream Breath, Echo, Temporal Anomaly) because it's the Aug+Presv
  tree; for **Augmentation** the analogous effects apply to its own kit. The
  Aug-relevant Chronowarden nodes are Chrono Flame, Temporal Burst, Energy
  Cycles, Time Convergence, Instability Matrix, Afterimage, Overclock, Warp.
- **Flameshaper** is Dev+Presv; healing clauses (Dream Breath) are the Presv
  flavor.

---

## Talent catalog

### Class tree (shared by all Evoker specs) — 29 nodes

- **Obsidian Scales** _(row 1, [363916](https://www.wowhead.com/spell=363916))_ — Reinforce your scales, reducing damage taken by N% and causing you to be healed over N equal to the damage it prevented. Lasts
- **Expunge** _(row 1, [365585](https://www.wowhead.com/spell=365585))_ — Expunge toxins affecting an ally, removing all Poison effects
- **Natural Convergence** _(row 2, [369913](https://www.wowhead.com/spell=369913))_ — Disintegrate channels N% faster and Eruption's cast time is reduced by N%
- **Verdant Embrace** _(row 2, [360995](https://www.wowhead.com/spell=360995))_ — Fly to an ally and heal them for N, or heal yourself for the same amount
- **Forger of Mountains** _(row 3, [375528](https://www.wowhead.com/spell=375528))_ — Landslide's cooldown is reduced by N sec, and it can withstand N% more damage before breaking
- **Innate Magic** _(row 3, [375520](https://www.wowhead.com/spell=375520))_ — Essence regenerates N% faster
- **Obsidian Bulwark** _(row 3, [375406](https://www.wowhead.com/spell=375406))_ — Obsidian Scales has an additional charge
- **Enkindled** _(row 3, [375554](https://www.wowhead.com/spell=375554))_ — Living Flame deals N% more damage and healing
- **Scarlet Adaptation** _(row 3, [372469](https://www.wowhead.com/spell=372469))_ — Store N% of your effective healing, up to N. Your next damaging Living Flame consumes all stored healing to increase its damage dealt
- **Tailwind** _(row 4, [375556](https://www.wowhead.com/spell=375556))_ — Hover increases your movement speed by N% for the first N
- **Ancient Flame** _(row 5, [369990](https://www.wowhead.com/spell=369990))_ — Casting Emerald Blossom or Verdant Embrace reduces the cast time of your next Living Flame by N%
- **Instinctive Arcana** _(row 5, [376164](https://www.wowhead.com/spell=376164))_ — Your Magic damage done is increased by N%
- **Tip the Scales** _(row 5, [370553](https://www.wowhead.com/spell=370553))_ — Compress time to make your next empowered spell cast instantly at its maximum empower level
- **Attuned to the Dream** _(row 5, [376930](https://www.wowhead.com/spell=376930))_ — Your healing done and healing received are increased by N%
- **Protracted Talons** _(row 6, [369909](https://www.wowhead.com/spell=369909))_ — Azure Strike damages N additional enemies
- **Inherent Resistance** _(row 6, [375544](https://www.wowhead.com/spell=375544))_ — Magic damage taken reduced by N%
- **Draconic Legacy** _(row 6, [376166](https://www.wowhead.com/spell=376166))_ — Your Stamina is increased by N%
- **Extended Flight** _(row 6, [375517](https://www.wowhead.com/spell=375517))_ — Hover lasts N sec longer
- **Bountiful Bloom** _(row 6, [370886](https://www.wowhead.com/spell=370886))_ — Emerald Blossom heals N additional allies
- **Blast Furnace** _(row 7, [375510](https://www.wowhead.com/spell=375510))_ — Fire Breath's damage over time lasts N sec longer
- **Exuberance** _(row 7, [375542](https://www.wowhead.com/spell=375542))_ — While above 75% health, your movement speed is increased by N%
- **Panacea** _(row 7, [387761](https://www.wowhead.com/spell=387761))_ — Emerald Blossom and Verdant Embrace instantly heal you for N when cast
- **Unravel** _(row 8, [1264378](https://www.wowhead.com/spell=1264378))_ — Direct damage from Fire Breath consumes absorb shields from enemies, dealing N additional Spellfrost damage to them
- **Oppressing Roar** _(row 8, [372048](https://www.wowhead.com/spell=372048))_ — Let out a bone-shaking roar at enemies in a cone in front of you, increasing the duration of crowd controls that affect them by N% in the next
- **Lush Growth** _(row 8, [375561](https://www.wowhead.com/spell=375561))_ — Green spells restore N% more health
- **Leaping Flames** _(row 9, [369939](https://www.wowhead.com/spell=369939))_ — Fire Breath causes your next Living Flame to strike 1 additional target per empower level
- **Overawe** _(row 9, [374346](https://www.wowhead.com/spell=374346))_ — Oppressing Roar removes N Enrage effect from each enemy, and its cooldown is reduced by N sec
- **Aerial Mastery** _(row 9, [365933](https://www.wowhead.com/spell=365933))_ — Hover gains N additional charge
- **Time Spiral** _(row 10, [374968](https://www.wowhead.com/spell=374968))_ — Bend time, allowing you and your allies within yds to cast their major movement ability once in the next N, even if it is on cooldown

### Devastation spec tree — 37 nodes

- **Pyre** _(row 1, [357211](https://www.wowhead.com/spell=357211))_ — Lob a ball of flame, dealing N Fire damage to your target and all enemies within N yds
- **Ruby Essence Burst** _(row 2, [376872](https://www.wowhead.com/spell=376872))_ — Your Living Flame has a N% chance to cause an Essence Burst, making your next Disintegrate or Pyre cost no Essence
- **Azure Essence Burst** _(row 2, [375721](https://www.wowhead.com/spell=375721))_ — Azure Strike has a N% chance to cause an Essence Burst, making your next Disintegrate or Pyre cost no Essence
- **Lay Waste** _(row 3, [371034](https://www.wowhead.com/spell=371034))_ — Deep Breath's damage is increased by N%
- **Eternity Surge** _(row 3, [359073](https://www.wowhead.com/spell=359073))_ — Focus your energies to release a salvo of pure magic, dealing N Spellfrost damage to an enemy. Damages additional enemies within N yds when empowered
- **Volatility** _(row 4, [369089](https://www.wowhead.com/spell=369089))_ — Pyre has a N% chance to flare up and explode again on a nearby target
- **Dragonrage** _(row 4, [375087](https://www.wowhead.com/spell=375087))_ — Erupt with draconic fury and exhale Pyres at N enemies within N yds
- **Azure Sweep** _(row 4, [1265867](https://www.wowhead.com/spell=1265867))_ — Eternity Surge upgrades your next Azure Strike to Azure Sweep, damaging all nearby enemies and dealing N% additional damage
- **Arcane Intensity** _(row 4, [375618](https://www.wowhead.com/spell=375618))_ — Disintegrate and Azure Strike deal N% more damage
- **Ruby Embers** _(row 5, [365937](https://www.wowhead.com/spell=365937))_ — Living Flame deals N damage over N to enemies, or restores N health to allies over N. Stacks N times
- **Animosity** _(row 5, [375797](https://www.wowhead.com/spell=375797))_ — Casting an empower spell extends the duration of Dragonrage by N sec
- **Engulfing Blaze** _(row 6, [370837](https://www.wowhead.com/spell=370837))_ — Living Flame deals N% increased damage and healing and its cast time is reduced by N.1 sec
- **Heat Wave** _(row 6, [375725](https://www.wowhead.com/spell=375725))_ — Fire Breath deals N% more damage
- **Honed Aggression** _(row 6, [371038](https://www.wowhead.com/spell=371038))_ — The critical strike chance of your spells is increased by N%
- **Eternity's Span** _(row 6, [375757](https://www.wowhead.com/spell=375757))_ — Eternity Surge hits twice as many targets
- **Event Horizon** _(row 6, [411164](https://www.wowhead.com/spell=411164))_ — Eternity Surge's cooldown is reduced by N sec
- **Eye of Infinity** _(row 6, [411165](https://www.wowhead.com/spell=411165))_ — Eternity Surge deals N% increased damage to your primary target
- **Catalyze** _(row 7, [386283](https://www.wowhead.com/spell=386283))_ — While channeling Disintegrate your Fire Breath on the target deals damage N% more often
- **Tyranny** _(row 7, [376888](https://www.wowhead.com/spell=376888))_ — During Deep Breath and Dragonrage you gain the maximum benefit of Mastery: Giantkiller regardless of targets' health
- **Charged Blast** _(row 7, [370455](https://www.wowhead.com/spell=370455))_ — Your Blue damage increases the damage of your next Pyre by N%, stacking N times
- **Shattering Stars** _(row 7, [1265802](https://www.wowhead.com/spell=1265802))_ — Eternity Surge additionally releases a Shattering Star at your target that deals N% more damage per empower level reached
- **Feed the Flames** _(row 8, [369846](https://www.wowhead.com/spell=369846))_ — After casting N Pyres, your next Pyre will explode into a Firestorm
- **Burnout** _(row 8, [375801](https://www.wowhead.com/spell=375801))_ — Fire Breath damage has N% chance to cause your next Living Flame to be instant cast, stacking N times
- **Onyx Legacy** _(row 8, [386348](https://www.wowhead.com/spell=386348))_ — Deep Breath's cooldown is reduced by 1 min
- **Spellweaver's Dominance** _(row 8, [370845](https://www.wowhead.com/spell=370845))_ — Your damaging critical strikes deal N% damage instead of the usual 200%
- **Star Salvo** _(row 8, [1265826](https://www.wowhead.com/spell=1265826))_ — Increases Shattering Star damage by N%
- **Imminent Destruction** _(row 9, [370781](https://www.wowhead.com/spell=370781))_ — Deep Breath reduces the Essence costs of your next N Disintegrates and Pyres by N. Stacks up to N times
- **Font of Magic** _(row 9, [411212](https://www.wowhead.com/spell=411212))_ — Your empower spells' maximum level is increased by 1, and they reach maximum empower level N% faster
- **Titanic Wrath** _(row 9, [386272](https://www.wowhead.com/spell=386272))_ — Essence Burst increases the damage of affected spells by N.1%
- **Azure Celerity** _(row 9, [1219723](https://www.wowhead.com/spell=1219723))_ — Disintegrate deals damage N% more often, but deals N% less damage
- **Power Swell** _(row 9, [370839](https://www.wowhead.com/spell=370839))_ — Casting an empower spell increases your Essence regeneration rate by N% for N
- **Strafing Run** _(row 10, [1266151](https://www.wowhead.com/spell=1266151))_ — Deep Breath deals N% reduced damage and can be cast again within N of being used
- **Scorching Embers** _(row 10, [370819](https://www.wowhead.com/spell=370819))_ — Enemies affected by Fire Breath's damage over time effect take N% increased damage from your Red spells
- **Causality** _(row 10, [375777](https://www.wowhead.com/spell=375777))_ — Disintegrate reduces the remaining cooldown of your empower spells by N.2 sec each time it deals damage
- **Scintillation** _(row 10, [370821](https://www.wowhead.com/spell=370821))_ — Disintegrate has a N% chance each time it deals damage to launch a level 1 Eternity Surge at N% power
- **Iridescence** _(row 10, [370867](https://www.wowhead.com/spell=370867))_ — Casting an empower spell increases the damage of your next N spells of the same color by N% within N
- **Rising Fury** _(row 11, [1271687](https://www.wowhead.com/spell=1271687))_ — While Dragonrage is active you gain Rising Fury every N sec, increasing your haste by N%, stacking up to N times

### Augmentation spec tree — 50 nodes

- **Ebon Might** _(row 1, [395152](https://www.wowhead.com/spell=395152))_ — Increase all damage dealing allies' primary stat by N% of your own and increase your own damage by N% for
- **Eruption** _(row 2, [395160](https://www.wowhead.com/spell=395160))_ — Cause a violent eruption beneath an enemy's feet, dealing N Volcanic damage split between them and nearby enemies
- **Essence Burst** _(row 2, [396187](https://www.wowhead.com/spell=396187))_ — Your Living Flame has a N% chance, and your Azure Strike has a N% chance, to make your next Eruption or Emerald Blossom cost no Essence. Stacks N times
- **Quell** _(row 3, [351338](https://www.wowhead.com/spell=351338))_ — Interrupt an enemy's spellcasting and prevent any spell from that school of magic from being cast for
- **Ricocheting Pyroclast** _(row 3, [406659](https://www.wowhead.com/spell=406659))_ — Eruption deals N% more damage per enemy struck, up to N%
- **Essence Attunement** _(row 3, [375722](https://www.wowhead.com/spell=375722))_ — Essence Burst stacks N times
- **Echoing Strike** _(row 3, [410784](https://www.wowhead.com/spell=410784))_ — Azure Strike deals N% increased damage and has a N% chance per target hit to echo, casting again
- **Pupil of Alexstrasza** _(row 3, [407814](https://www.wowhead.com/spell=407814))_ — When cast at an enemy, Living Flame strikes N additional enemy for N% damage
- **Upheaval** _(row 4, [396286](https://www.wowhead.com/spell=396286))_ — Gather earthen power beneath your enemy's feet and send them hurtling upwards, dealing N Volcanic damage to the target and nearby enemies
- **Breath of Eons** _(row 4, [403631](https://www.wowhead.com/spell=403631))_ — Fly to the targeted location, exposing a on enemies in your path for N and granting Ebon Might for N sec
- **Defy Fate** _(row 4, [404195](https://www.wowhead.com/spell=404195))_ — Fatal attacks are diverted into a nearby timeline, preventing the damage, and your death, in this one
- **Ignition Rush** _(row 5, [408775](https://www.wowhead.com/spell=408775))_ — Essence Burst reduces the cast time of Eruption by N% and increases its damage by N%
- **Power Nexus** _(row 5, [369908](https://www.wowhead.com/spell=369908))_ — Increases your maximum Essence to N
- **Volcanism** _(row 5, [406904](https://www.wowhead.com/spell=406904))_ — Eruption's Essence cost is reduced by N
- **Chrono Ward** _(row 5, [409676](https://www.wowhead.com/spell=409676))_ — When allies deal damage with Temporal Wounds, they gain a shield for N% of the damage dealt. Absorption cannot exceed N% of your maximum health
- **Perilous Fate** _(row 5, [410253](https://www.wowhead.com/spell=410253))_ — Breath of Eons reduces enemies' movement speed by N%, and reduces their attack speed by N%, for N
- **Bestow Weyrnstone** _(row 5, [408233](https://www.wowhead.com/spell=408233))_ — Conjure a pair of Weyrnstones, one for your target ally and one for yourself. Only one ally may bear your Weyrnstone at a time
- **Timelessness** _(row 5, [412710](https://www.wowhead.com/spell=412710))_ — Enchant an ally to appear out of sync with the normal flow of time, reducing threat they generate by N% for . Less effective on tank-specialized allies
- **Improved Defy Fate** _(row 5, [1268881](https://www.wowhead.com/spell=1268881))_ — Defy Fate healing increased by N% and its cooldown is reduced by N min
- **Blistering Scales** _(row 6, [360827](https://www.wowhead.com/spell=360827))_ — Protect an ally with explosive dragonscales, increasing their Armor by N% of your own
- **Draconic Attunements** _(row 6, [403208](https://www.wowhead.com/spell=403208))_ — Learn to attune yourself to the essence of the Black or Bronze Dragonflights:
- **Prescience** _(row 6, [409311](https://www.wowhead.com/spell=409311))_ — Grant an ally the gift of foresight, increasing their critical strike chance by N% and occasionally copying their damage and healing spells at N% power for N
- **Tectonic Locus** _(row 7, [408002](https://www.wowhead.com/spell=408002))_ — Upheaval deals N% increased damage to the primary target, and launches them higher
- **Unyielding Domain** _(row 7, [412733](https://www.wowhead.com/spell=412733))_ — Upheaval cannot be interrupted, and has an additional N% chance to critically strike
- **Molten Blood** _(row 7, [410643](https://www.wowhead.com/spell=410643))_ — When cast, Blistering Scales grants the target a shield that absorbs up to N damage for N based on their missing health. Lower health targets gain a larger shield
- **Regenerative Chitin** _(row 7, [406907](https://www.wowhead.com/spell=406907))_ — Blistering Scales no longer loses charges and deals N% more damage
- **Momentum Shift** _(row 7, [408004](https://www.wowhead.com/spell=408004))_ — Consuming Essence Burst grants you N% Intellect for N. Stacks up to N times
- **Aspects' Favor** _(row 7, [407243](https://www.wowhead.com/spell=407243))_ — Obsidian Scales activates Black Attunement, and amplifies it to increase maximum health by N% for N
- **Arcane Reach** _(row 7, [454983](https://www.wowhead.com/spell=454983))_ — The range of your helpful magics is increased by N yards
- **Fate Mirror** _(row 7, [412774](https://www.wowhead.com/spell=412774))_ — Prescience grants the ally a chance for their spells and abilities to echo their damage or healing, dealing N% of the amount again
- **Symbiotic Bloom** _(row 7, [410685](https://www.wowhead.com/spell=410685))_ — Emerald Blossom increases targets' healing received by N% for N
- **Reactive Hide** _(row 8, [409329](https://www.wowhead.com/spell=409329))_ — Each time Blistering Scales explodes it deals N% more damage for N, stacking N times
- **Font of Magic** _(row 8, [408083](https://www.wowhead.com/spell=408083))_ — Your empower spells' maximum level is increased by 1, and they reach maximum empower level N% faster
- **Hoarded Power** _(row 8, [375796](https://www.wowhead.com/spell=375796))_ — Essence Burst has a N% chance to not be consumed
- **Motes of Possibility** _(row 8, [409267](https://www.wowhead.com/spell=409267))_ — Eruption has a N% chance to form a mote of diverted essence near you. Allies who comes in contact with the mote gain a random buff from your arsenal
- **Anachronism** _(row 8, [407869](https://www.wowhead.com/spell=407869))_ — Prescience has a N% chance to grant Essence Burst
- **Dream of Spring** _(row 8, [414969](https://www.wowhead.com/spell=414969))_ — Emerald Blossom no longer has a cooldown, deals N% increased healing, and increases the duration of your active Ebon Might effects by N sec, but costs N Essence
- **Prolong Life** _(row 8, [410687](https://www.wowhead.com/spell=410687))_ — Your effects that extend Ebon Might also extend Symbiotic Bloom
- **Accretion** _(row 9, [407876](https://www.wowhead.com/spell=407876))_ — Eruption reduces the remaining cooldown of Upheaval by N.1 sec
- **Imminent Destruction** _(row 9, [459537](https://www.wowhead.com/spell=459537))_ — Breath of Eons reduces the Essence cost of your next N Eruptions by N
- **Time Skip** _(row 9, [404977](https://www.wowhead.com/spell=404977))_ — Surge forward in time, causing your cooldowns to recover N% faster for
- **Clairvoyant** _(row 9, [1250914](https://www.wowhead.com/spell=1250914))_ — Motes of Possibility may now grant Prescience to allies and have a N% increased chance to activate
- **Inferno's Blessing** _(row 9, [410261](https://www.wowhead.com/spell=410261))_ — Fire Breath grants the inferno's blessing for N to you and a nearby ally, giving their damaging attacks and spells a high chance to deal an additional N Fire damage
- **Rumbling Earth** _(row 10, [459120](https://www.wowhead.com/spell=459120))_ — Upheaval causes an aftershock at its location, dealing N% of its damage N additional times
- **Plot the Future** _(row 10, [407866](https://www.wowhead.com/spell=407866))_ — Breath of Eons grants you Fury of the Aspects for N sec after you land, without causing Exhaustion
- **Interwoven Threads** _(row 10, [412713](https://www.wowhead.com/spell=412713))_ — The cooldowns of your spells are reduced by N%
- **Tomorrow, Today** _(row 10, [412723](https://www.wowhead.com/spell=412723))_ — Time Skip channels for N sec longer
- **Overlord** _(row 10, [410260](https://www.wowhead.com/spell=410260))_ — Breath of Eons casts an Eruption at the first N enemies struck. These Eruptions have a N% chance to create a Mote of Possibility
- **Mighty Inferno** _(row 10, [1291457](https://www.wowhead.com/spell=1291457))_ — Inferno's Blessing's damage is increased by N%, and your effects that extend Ebon Might also extend Inferno's Blessing
- **Duplicate** _(row 11, [1259173](https://www.wowhead.com/spell=1259173))_ — Breath of Eons summons a version of you from the future to assist you in battle, lasting N. Your duplicate casts Eruption, Fire Breath, and Upheaval

### Scale Commander hero tree (Devastation & Augmentation) — 18 nodes

- **Mass Eruption** _(row 1, [438587](https://www.wowhead.com/spell=438587))_ — Empower spells cause your next Eruption to strike up to N targets. When striking less than N targets, Eruption damage is increased by N% for each missing target
- **Mass Disintegrate** _(row 1, [436335](https://www.wowhead.com/spell=436335))_ — Empower spells cause your next Disintegrate to strike up to N targets. When striking fewer than N targets, Disintegrate damage is increased by N% for each missing target
- **Might of the Black Dragonflight** _(row 2, [441705](https://www.wowhead.com/spell=441705))_ — Black spells deal N% increased damage
- **Bombardments** _(row 2, [434300](https://www.wowhead.com/spell=434300))_ — Mass Disintegrate marks your primary target for destruction for the next N
- **Onslaught** _(row 2, [441245](https://www.wowhead.com/spell=441245))_ — Entering combat grants a charge of Burnout, causing your next Living Flame to cast instantly
- **Command Squadron** _(row 2, [1260745](https://www.wowhead.com/spell=1260745))_ — While flying during Breath of Eons you are assisted by a squadron of Dracthyr who assault enemies with Pyre, dealing N Fire damage to nearby enemies up to N times
- **Melt Armor** _(row 3, [441176](https://www.wowhead.com/spell=441176))_ — Breath of Eons causes enemies to take N% increased damage from Bombardments and Essence abilities for N
- **Wingleader** _(row 3, [441206](https://www.wowhead.com/spell=441206))_ — Bombardments reduce the cooldown of Deep Breath by N.1 sec for each target struck, up to N.1 sec
- **Unrelenting Siege** _(row 3, [441246](https://www.wowhead.com/spell=441246))_ — For each second you are in combat, Azure Strike, Living Flame, and Disintegrate deal N% increased damage, up to N%
- **Concentrated Power** _(row 3, [1261448](https://www.wowhead.com/spell=1261448))_ — Mass Disintegrate strikes N additional targets
- **Hardened Scales** _(row 4, [441180](https://www.wowhead.com/spell=441180))_ — Obsidian Scales reduces damage taken by an additional N%
- **Menacing Presence** _(row 4, [441181](https://www.wowhead.com/spell=441181))_ — Knocking enemies up or backwards reduces their damage done to you by N% for N
- **Diverted Power** _(row 4, [441219](https://www.wowhead.com/spell=441219))_ — Bombardments have a chance to generate Essence Burst
- **Extended Battle** _(row 4, [441212](https://www.wowhead.com/spell=441212))_ — Essence abilities extend Bombardments by N sec
- **Nimble Flyer** _(row 4, [441253](https://www.wowhead.com/spell=441253))_ — While Hovering, damage taken from area of effect attacks is reduced by N%
- **Slipstream** _(row 4, [441257](https://www.wowhead.com/spell=441257))_ — Breath of Eons resets a charge of Hover
- **Refined Essence** _(row 4, [1261452](https://www.wowhead.com/spell=1261452))_ — Essence abilities deal N% additional damage
- **Maneuverability** _(row 5, [433871](https://www.wowhead.com/spell=433871))_ — Breath of Eons can now be steered in your desired direction

### Flameshaper hero tree (Devastation) — 17 nodes

- **Legacy of the Lifebinder** _(row 1, [1264269](https://www.wowhead.com/spell=1264269))_ — Fire Breath gains an additional charge
- **Shape of Flame** _(row 2, [445074](https://www.wowhead.com/spell=445074))_ — Tail Swipe and Wing Buffet scorch enemies and blind them with ash, causing their next attack within N to miss
- **Trailblazer** _(row 2, [444849](https://www.wowhead.com/spell=444849))_ — Hover and Deep Breath travel N% faster, and Hover travels N% further
- **Ashes in Motion** _(row 2, [1264365](https://www.wowhead.com/spell=1264365))_ — Fire Breath's cooldown is reduced by N sec
- **Enkindle** _(row 2, [444016](https://www.wowhead.com/spell=444016))_ — Essence abilities are enhanced with Flame, dealing N% of healing or damage done as Fire over 8 sec
- **Expanded Lungs** _(row 2, [444845](https://www.wowhead.com/spell=444845))_ — Fire Breath's damage over time is increased by N%. Dream Breath's heal over time is increased by N%
- **Essence Well** _(row 2, [1265993](https://www.wowhead.com/spell=1265993))_ — Fire Breath has a N% chance to generate Essence Burst
- **Conduit of Flame** _(row 3, [444843](https://www.wowhead.com/spell=444843))_ — Critical strike chance against targets above N% health increased by N%
- **Burning Adrenaline** _(row 3, [444020](https://www.wowhead.com/spell=444020))_ — Fire Breath reaches its maximum empower level N% faster
- **Fulminous Roar** _(row 3, [1218447](https://www.wowhead.com/spell=1218447))_ — Fire Breath deals its damage N% more often
- **Twin Flame** _(row 3, [1265979](https://www.wowhead.com/spell=1265979))_ — Consuming Essence Burst fires a twin flame, striking your target for N Fire damage
- **Titanic Precision** _(row 4, [445625](https://www.wowhead.com/spell=445625))_ — Living Flame and Azure Strike have N extra chance to trigger Essence Burst when they critically strike
- **Deep Exhalation** _(row 4, [1264321](https://www.wowhead.com/spell=1264321))_ — Fire Breath's damage over time lasts N sec longer
- **Draconic Instincts** _(row 4, [445958](https://www.wowhead.com/spell=445958))_ — Your wounds have a small chance to cauterize, healing you for N% of damage taken. Occurs more often from attacks that deal high damage
- **Lifecinders** _(row 4, [444322](https://www.wowhead.com/spell=444322))_ — Obsidian Scales also applies to your target or N nearby injured allies at N% value
- **Fire Torrent** _(row 4, [1265992](https://www.wowhead.com/spell=1265992))_ — Twin Flame bounces to up to N additional targets
- **Consume Flame** _(row 5, [444088](https://www.wowhead.com/spell=444088))_ — Disintegrate damage consumes N.1 sec of Fire Breath from enemies it damages, detonating it for N% of the amount consumed

### Chronowarden hero tree (Augmentation) — 17 nodes

- **Energy Cycles** _(row 3, [1260568](https://www.wowhead.com/spell=1260568); not present in the SimC spell-data dump — sourced from `sc_evoker.cpp` + Wowhead)_ — While **Temporal Burst** is active you gain an Essence Burst every ~6 sec (see mechanics doc §4).

- **Chrono Flame** _(row 1, [431442](https://www.wowhead.com/spell=431442))_ — Living Flame is enhanced with Bronze magic, repeating N% of the damage or healing you dealt to the target in the last N sec as Arcane, up to N
- **Warp** _(row 2, [429483](https://www.wowhead.com/spell=429483))_ — Hover now causes you to briefly warp out of existence and appear at your destination. Hover's cooldown is also reduced by N sec
- **Temporal Burst** _(row 2, [431695](https://www.wowhead.com/spell=431695))_ — Tip the Scales overloads you with temporal energy, increasing your haste, movement speed, and cooldown recovery rate by N%, decreasing over N
- **Chronoboon** _(row 2, [1260484](https://www.wowhead.com/spell=1260484))_ — Tip the Scales' cooldown is reduced by N sec
- **Reverberations** _(row 2, [431615](https://www.wowhead.com/spell=431615))_ — Verdant Embrace heals for an additional N% over N
- **Motes of Acceleration** _(row 3, [432008](https://www.wowhead.com/spell=432008))_ — Warp leaves a trail of Motes of Acceleration. Allies who come in contact with a mote gain 20% increased movement speed for 30 sec
- **Temporality** _(row 3, [431873](https://www.wowhead.com/spell=431873))_ — Warp reduces damage taken by N%, starting high and reducing over N
- **Nozdormu Adept** _(row 3, [431715](https://www.wowhead.com/spell=431715))_ — Temporal Anomaly mana cost reduced by N% and cooldown reduced by N sec
- **Chronal Dynamo** _(row 3, [1291522](https://www.wowhead.com/spell=1291522))_ — Living Flame's cast time is reduced by N.1 sec, and it deals N% increased damage or healing when it is a non-instant cast
- **Primacy** _(row 3, [431657](https://www.wowhead.com/spell=431657))_ — For each healing over time effect from Verdant Embrace, gain N% haste, up to N%
- **Double-time** _(row 4, [431874](https://www.wowhead.com/spell=431874))_ — When Dream Breath or Fire Breath critically strike, their duration is extended by N sec, up to a maximum of N sec
- **Time Convergence** _(row 4, [431984](https://www.wowhead.com/spell=431984))_ — Non-defensive abilities with a N second or longer cooldown grant N% Intellect for N
- **Instability Matrix** _(row 4, [431484](https://www.wowhead.com/spell=431484))_ — Each time you cast an empower spell, unstable time magic reduces its cooldown by up to N sec
- **Overclock** _(row 4, [1260647](https://www.wowhead.com/spell=1260647))_ — Chrono Flames' maximum damage or healing is increased by N%, up to N Arcane
- **Golden Opportunity** _(row 4, [432004](https://www.wowhead.com/spell=432004))_ — Echo is N% more effective
- **Afterimage** _(row 5, [431875](https://www.wowhead.com/spell=431875))_ — Empower spells send up to N Chrono Flames to your targets

---

## Build-string reference (current SimC defaults)
Paste into the in-game talent UI / Raidbots. These are the `talents=` strings
from the SimC `midnight` MID1 profiles (in this folder):
- **Devastation — Scale Commander** (`MID1_Evoker_Devastation_SC.simc`):
  `CsbBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAzMDMDzgBmZGjZaYmpZMWmxMzMz8AzMzAmxMGzMLzMDMwYwCsMGN2GQmBBbYGMzghB`
- **Devastation — Flameshaper** (`MID1_Evoker_Devastation_FS.simc`):
  `CsbBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgZmZwMDGMgBjZamZmJjxyMzMzwMzMzAmxMzYmZbmZwMwMmB2ALgZYCsFsMMAmZGG`
- **Augmentation:** SimC ships **no** pre-built gear/talent profile for Aug (it
  models only the APL — see README). For current Aug loadouts use the live guide
  build pages: [Wowhead Aug Midnight S1](https://www.wowhead.com/guide/classes/evoker/augmentation/midnight-season-1),
  [Murlok Aug SC M+](https://murlok.io/evoker/augmentation/scalecommander/m+),
  [Archon Aug M+](https://www.archon.gg/wow/builds/augmentation/evoker/mythic-plus/talents/high-keys/all-dungeons/this-week).

## Sources
- SimC `midnight`: [`SpellDataDump/evoker.txt`](https://github.com/simulationcraft/simc/blob/midnight/SpellDataDump/evoker.txt) (tooltips), [`sc_evoker.cpp`](https://github.com/simulationcraft/simc/blob/midnight/engine/class_modules/sc_evoker.cpp) (classification).
- Per-talent live numbers: Wowhead spell links inline above.
- Narrative + meta context: see `EVOKER_MIDNIGHT_MECHANICS.md` and its Sources.
