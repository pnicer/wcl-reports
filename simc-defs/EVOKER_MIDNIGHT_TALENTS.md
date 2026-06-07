# Evoker talent catalog — WoW *Midnight* Season 1 (patch 12.0.5, ~June 2026)

Complete, value-resolved talent reference for the two DPS Evoker specs,
extracted from SimulationCraft (`midnight` branch) and resolved against the
spell-effect data. Companion to `EVOKER_MIDNIGHT_MECHANICS.md` (narrative +
analysis); this file is the exhaustive, precise node list.

## How to read this
- **Source of truth:** tree/row/spec and tooltip text from
  `SpellDataDump/evoker.txt`; classification cross-checked against
  `sc_evoker.cpp` (`HT()`/`ST()`/`CT()`). Numeric values are **resolved from each
  spell's effect data** (`$s/$w/$t/$d/$A/${…}` templating evaluated), so
  percentages, chances, durations, radii, target counts, cooldowns and per-rank
  values are real numbers for the current build.
- **Remaining `N`** = a value **not present in the static spell-data dump**:
  either a **spell-power-scaled damage amount** ("deals N damage" — depends on
  your stats) or a **max-stack count** ("Stacks N times"). Click the spell-id →
  Wowhead link for those. Numbers are patch-volatile regardless — the link is
  the live source.
- **`ranks: a/b`** shows the per-rank progression for multi-rank talents (the
  headline number is the max-rank value).
- **Rows** = the talent's row in its tree. Preservation (healer) spec talents
  excluded; all three hero trees included in full.

## ⚠️ Hero-tree tooltips show spec-flavored text — read this
Hero trees are **shared**, and the dump prints one spec's wording:
- **Scale Commander** text says **"Breath of Eons"** (Augmentation's flying
  breath). **For Devastation, read that as "Deep Breath"** — same slot for Melt
  Armor, Wingleader, Slipstream, Command Squadron, Maneuverability.
- **Scale Commander row 1 has two spec variants:** **Mass Disintegrate**
  (Devastation) and **Mass Eruption** (Augmentation) — same node, different
  spender.
- **Chronowarden** tooltips reference **Preservation** healing spells (Verdant
  Embrace, Dream Breath, Echo, Temporal Anomaly) because it's the Aug+Presv
  tree; for **Augmentation** the analogous effects apply to its own kit. The
  Aug-relevant nodes are Chrono Flame, Temporal Burst, Energy Cycles, Time
  Convergence, Instability Matrix, Afterimage, Overclock, Warp.
- **Flameshaper** is Dev+Presv; healing clauses (Dream Breath) are Presv flavor.

---

## Talent catalog

### Class tree (shared by all Evoker specs) — 29 nodes

- **Obsidian Scales** _(row 1, [363916](https://www.wowhead.com/spell=363916))_ — Reinforce your scales, reducing damage taken by 30% and causing you to be healed over 8 sec equal to the damage it prevented. Lasts 12 sec
- **Expunge** _(row 1, [365585](https://www.wowhead.com/spell=365585))_ — Expunge toxins affecting an ally, removing all Poison effects
- **Natural Convergence** _(row 2, [369913](https://www.wowhead.com/spell=369913))_ — Disintegrate channels -20% faster and Eruption's cast time is reduced by 20%
- **Verdant Embrace** _(row 2, [360995](https://www.wowhead.com/spell=360995))_ — Fly to an ally and heal them for N, or heal yourself for the same amount
- **Forger of Mountains** _(row 3, [375528](https://www.wowhead.com/spell=375528))_ — Landslide's cooldown is reduced by 30 sec, and it can withstand 200% more damage before breaking
- **Innate Magic** _(row 3, 2 ranks, [375520](https://www.wowhead.com/spell=375520))_ — Essence regenerates 10% faster  _(ranks: 5/10)_
- **Obsidian Bulwark** _(row 3, [375406](https://www.wowhead.com/spell=375406))_ — Obsidian Scales has an additional charge
- **Enkindled** _(row 3, 2 ranks, [375554](https://www.wowhead.com/spell=375554))_ — Living Flame deals 6% more damage and healing  _(ranks: 3/6)_
- **Scarlet Adaptation** _(row 3, [372469](https://www.wowhead.com/spell=372469))_ — Store 20% of your effective healing, up to $<cap>. Your next damaging Living Flame consumes all stored healing to increase its damage dealt
- **Tailwind** _(row 4, [375556](https://www.wowhead.com/spell=375556))_ — Hover increases your movement speed by 70% for the first 4 sec
- **Ancient Flame** _(row 5, [369990](https://www.wowhead.com/spell=369990))_ — Casting Emerald Blossom or Verdant Embrace reduces the cast time of your next Living Flame by 40%
- **Instinctive Arcana** _(row 5, 2 ranks, [376164](https://www.wowhead.com/spell=376164))_ — Your Magic damage done is increased by 4%  _(ranks: 2/4)_
- **Tip the Scales** _(row 5, [370553](https://www.wowhead.com/spell=370553))_ — Compress time to make your next empowered spell cast instantly at its maximum empower level
- **Attuned to the Dream** _(row 5, 2 ranks, [376930](https://www.wowhead.com/spell=376930))_ — Your healing done and healing received are increased by 2%
- **Protracted Talons** _(row 6, [369909](https://www.wowhead.com/spell=369909))_ — Azure Strike damages 1 additional enemies
- **Inherent Resistance** _(row 6, 2 ranks, [375544](https://www.wowhead.com/spell=375544))_ — Magic damage taken reduced by 2%
- **Draconic Legacy** _(row 6, [376166](https://www.wowhead.com/spell=376166))_ — Your Stamina is increased by 6%
- **Extended Flight** _(row 6, 2 ranks, [375517](https://www.wowhead.com/spell=375517))_ — Hover lasts 4 sec longer  _(ranks: 2000/4000)_
- **Bountiful Bloom** _(row 6, [370886](https://www.wowhead.com/spell=370886))_ — Emerald Blossom heals 2 additional allies
- **Blast Furnace** _(row 7, [375510](https://www.wowhead.com/spell=375510))_ — Fire Breath's damage over time lasts 4 sec longer
- **Exuberance** _(row 7, [375542](https://www.wowhead.com/spell=375542))_ — While above 75% health, your movement speed is increased by 10%
- **Panacea** _(row 7, [387761](https://www.wowhead.com/spell=387761))_ — Emerald Blossom and Verdant Embrace instantly heal you for N when cast
- **Unravel** _(row 8, [1264378](https://www.wowhead.com/spell=1264378))_ — Direct damage from Fire Breath consumes absorb shields from enemies, dealing N additional Spellfrost damage to them
- **Oppressing Roar** _(row 8, [372048](https://www.wowhead.com/spell=372048))_ — Let out a bone-shaking roar at enemies in a cone in front of you, increasing the duration of crowd controls that affect them by 50% in the next 10 sec
- **Lush Growth** _(row 8, 2 ranks, [375561](https://www.wowhead.com/spell=375561))_ — Green spells restore 10% more health  _(ranks: 5/10)_
- **Leaping Flames** _(row 9, [369939](https://www.wowhead.com/spell=369939))_ — Fire Breath causes your next Living Flame to strike 1 additional target per empower level
- **Overawe** _(row 9, [374346](https://www.wowhead.com/spell=374346))_ — Oppressing Roar removes 1 Enrage effect from each enemy, and its cooldown is reduced by 30 sec
- **Aerial Mastery** _(row 9, [365933](https://www.wowhead.com/spell=365933))_ — Hover gains 1 additional charge
- **Time Spiral** _(row 10, [374968](https://www.wowhead.com/spell=374968))_ — Bend time, allowing you and your allies within 40 yds to cast their major movement ability once in the next 10 sec, even if it is on cooldown

### Devastation spec tree — 37 nodes

- **Pyre** _(row 1, [357211](https://www.wowhead.com/spell=357211))_ — Lob a ball of flame, dealing N Fire damage to your target and all enemies within 8 yds
- **Ruby Essence Burst** _(row 2, [376872](https://www.wowhead.com/spell=376872))_ — Your Living Flame has a 20% chance to cause an Essence Burst, making your next Disintegrate or Pyre cost no Essence
- **Azure Essence Burst** _(row 2, [375721](https://www.wowhead.com/spell=375721))_ — Azure Strike has a 15% chance to cause an Essence Burst, making your next Disintegrate or Pyre cost no Essence
- **Lay Waste** _(row 3, [371034](https://www.wowhead.com/spell=371034))_ — Deep Breath's damage is increased by 20%
- **Eternity Surge** _(row 3, [359073](https://www.wowhead.com/spell=359073))_ — Focus your energies to release a salvo of pure magic, dealing $<dmg> Spellfrost damage to an enemy. Damages additional enemies within 25 yds when empowered
- **Volatility** _(row 4, 2 ranks, [369089](https://www.wowhead.com/spell=369089))_ — Pyre has a 30% chance to flare up and explode again on a nearby target  _(ranks: 15/30)_
- **Dragonrage** _(row 4, [375087](https://www.wowhead.com/spell=375087))_ — Erupt with draconic fury and exhale Pyres at 3 enemies within 25 yds
- **Azure Sweep** _(row 4, [1265867](https://www.wowhead.com/spell=1265867))_ — Eternity Surge upgrades your next Azure Strike to Azure Sweep, damaging all nearby enemies and dealing 75% additional damage
- **Arcane Intensity** _(row 4, 2 ranks, [375618](https://www.wowhead.com/spell=375618))_ — Disintegrate and Azure Strike deal 16% more damage  _(ranks: 8/16)_
- **Ruby Embers** _(row 5, [365937](https://www.wowhead.com/spell=365937))_ — Living Flame deals N damage over 12 sec to enemies, or restores N health to allies over 12 sec. Stacks N times
- **Animosity** _(row 5, [375797](https://www.wowhead.com/spell=375797))_ — Casting an empower spell extends the duration of Dragonrage by 5 sec
- **Engulfing Blaze** _(row 6, [370837](https://www.wowhead.com/spell=370837))_ — Living Flame deals 10% increased damage and healing and its cast time is reduced by 0.3 sec
- **Heat Wave** _(row 6, 2 ranks, [375725](https://www.wowhead.com/spell=375725))_ — Fire Breath deals 30% more damage  _(ranks: 15/30)_
- **Honed Aggression** _(row 6, 2 ranks, [371038](https://www.wowhead.com/spell=371038))_ — The critical strike chance of your spells is increased by 4%  _(ranks: 2/4)_
- **Eternity's Span** _(row 6, [375757](https://www.wowhead.com/spell=375757))_ — Eternity Surge hits twice as many targets
- **Event Horizon** _(row 6, [411164](https://www.wowhead.com/spell=411164))_ — Eternity Surge's cooldown is reduced by 3 sec
- **Eye of Infinity** _(row 6, [411165](https://www.wowhead.com/spell=411165))_ — Eternity Surge deals 15% increased damage to your primary target
- **Catalyze** _(row 7, [386283](https://www.wowhead.com/spell=386283))_ — While channeling Disintegrate your Fire Breath on the target deals damage 100% more often
- **Tyranny** _(row 7, [376888](https://www.wowhead.com/spell=376888))_ — During Deep Breath and Dragonrage you gain the maximum benefit of Mastery: Giantkiller regardless of targets' health
- **Charged Blast** _(row 7, [370455](https://www.wowhead.com/spell=370455))_ — Your Blue damage increases the damage of your next Pyre by 2%, stacking N times
- **Shattering Stars** _(row 7, [1265802](https://www.wowhead.com/spell=1265802))_ — Eternity Surge additionally releases a Shattering Star at your target that deals 50% more damage per empower level reached
- **Feed the Flames** _(row 8, [369846](https://www.wowhead.com/spell=369846))_ — After casting -6 Pyres, your next Pyre will explode into a Firestorm
- **Burnout** _(row 8, [375801](https://www.wowhead.com/spell=375801))_ — Fire Breath damage has 16% chance to cause your next Living Flame to be instant cast, stacking N times
- **Onyx Legacy** _(row 8, [386348](https://www.wowhead.com/spell=386348))_ — Deep Breath's cooldown is reduced by 1 min
- **Spellweaver's Dominance** _(row 8, [370845](https://www.wowhead.com/spell=370845))_ — Your damaging critical strikes deal 230% damage instead of the usual 200%
- **Star Salvo** _(row 8, [1265826](https://www.wowhead.com/spell=1265826))_ — Increases Shattering Star damage by 35%
- **Imminent Destruction** _(row 9, [370781](https://www.wowhead.com/spell=370781))_ — Deep Breath reduces the Essence costs of your next 4 Disintegrates and Pyres by 1. Stacks up to N times
- **Font of Magic** _(row 9, [411212](https://www.wowhead.com/spell=411212))_ — Your empower spells' maximum level is increased by 1, and they reach maximum empower level -20% faster
- **Titanic Wrath** _(row 9, [386272](https://www.wowhead.com/spell=386272))_ — Essence Burst increases the damage of affected spells by 15%
- **Azure Celerity** _(row 9, [1219723](https://www.wowhead.com/spell=1219723))_ — Disintegrate deals damage -25% more often, but deals -10% less damage
- **Power Swell** _(row 9, [370839](https://www.wowhead.com/spell=370839))_ — Casting an empower spell increases your Essence regeneration rate by 100% for 4 sec
- **Strafing Run** _(row 10, [1266151](https://www.wowhead.com/spell=1266151))_ — Deep Breath deals 20% reduced damage and can be cast again within 18 sec of being used
- **Scorching Embers** _(row 10, [370819](https://www.wowhead.com/spell=370819))_ — Enemies affected by Fire Breath's damage over time effect take 25% increased damage from your Red spells
- **Causality** _(row 10, [375777](https://www.wowhead.com/spell=375777))_ — Disintegrate reduces the remaining cooldown of your empower spells by 0.5 sec each time it deals damage
- **Scintillation** _(row 10, [370821](https://www.wowhead.com/spell=370821))_ — Disintegrate has a 15% chance each time it deals damage to launch a level 1 Eternity Surge at 40% power
- **Iridescence** _(row 10, [370867](https://www.wowhead.com/spell=370867))_ — Casting an empower spell increases the damage of your next N spells of the same color by 20% within 10 sec
- **Rising Fury** _(row 11, [1271687](https://www.wowhead.com/spell=1271687))_ — While Dragonrage is active you gain Rising Fury every 6 sec, increasing your haste by 4%, stacking up to N times

### Augmentation spec tree — 50 nodes

- **Ebon Might** _(row 1, [395152](https://www.wowhead.com/spell=395152))_ — Increase all damage dealing allies' primary stat by $<amount>% of your own and increase your own damage by 20% for 10 sec
- **Eruption** _(row 2, [395160](https://www.wowhead.com/spell=395160))_ — Cause a violent eruption beneath an enemy's feet, dealing N Volcanic damage split between them and nearby enemies
- **Essence Burst** _(row 2, [396187](https://www.wowhead.com/spell=396187))_ — Your Living Flame has a 20% chance, and your Azure Strike has a 15% chance, to make your next Eruption or Emerald Blossom cost no Essence. Stacks N times
- **Quell** _(row 3, [351338](https://www.wowhead.com/spell=351338))_ — Interrupt an enemy's spellcasting and prevent any spell from that school of magic from being cast for 6 sec
- **Ricocheting Pyroclast** _(row 3, [406659](https://www.wowhead.com/spell=406659))_ — Eruption deals 30% more damage per enemy struck, up to 150%
- **Essence Attunement** _(row 3, [375722](https://www.wowhead.com/spell=375722))_ — Essence Burst stacks 2 times
- **Echoing Strike** _(row 3, [410784](https://www.wowhead.com/spell=410784))_ — Azure Strike deals 15% increased damage and has a 10% chance per target hit to echo, casting again
- **Pupil of Alexstrasza** _(row 3, [407814](https://www.wowhead.com/spell=407814))_ — When cast at an enemy, Living Flame strikes 1 additional enemy for 100% damage
- **Upheaval** _(row 4, [396286](https://www.wowhead.com/spell=396286))_ — Gather earthen power beneath your enemy's feet and send them hurtling upwards, dealing N Volcanic damage to the target and nearby enemies
- **Breath of Eons** _(row 4, [403631](https://www.wowhead.com/spell=403631))_ — Fly to the targeted location, exposing a on enemies in your path for 10 sec and granting Ebon Might for 5 sec
- **Defy Fate** _(row 4, [404195](https://www.wowhead.com/spell=404195))_ — Fatal attacks are diverted into a nearby timeline, preventing the damage, and your death, in this one
- **Ignition Rush** _(row 5, [408775](https://www.wowhead.com/spell=408775))_ — Essence Burst reduces the cast time of Eruption by 40% and increases its damage by 20%
- **Power Nexus** _(row 5, [369908](https://www.wowhead.com/spell=369908))_ — Increases your maximum Essence to $<max>
- **Volcanism** _(row 5, [406904](https://www.wowhead.com/spell=406904))_ — Eruption's Essence cost is reduced by 1
- **Chrono Ward** _(row 5, [409676](https://www.wowhead.com/spell=409676))_ — When allies deal damage with Temporal Wounds, they gain a shield for 100% of the damage dealt. Absorption cannot exceed 30% of your maximum health
- **Perilous Fate** _(row 5, [410253](https://www.wowhead.com/spell=410253))_ — Breath of Eons reduces enemies' movement speed by 70%, and reduces their attack speed by 50%, for 10 sec
- **Bestow Weyrnstone** _(row 5, [408233](https://www.wowhead.com/spell=408233))_ — Conjure a pair of Weyrnstones, one for your target ally and one for yourself. Only one ally may bear your Weyrnstone at a time
- **Timelessness** _(row 5, [412710](https://www.wowhead.com/spell=412710))_ — Enchant an ally to appear out of sync with the normal flow of time, reducing threat they generate by 30% for 3600 sec. Less effective on tank-specialized allies
- **Improved Defy Fate** _(row 5, [1268881](https://www.wowhead.com/spell=1268881))_ — Defy Fate healing increased by 100% and its cooldown is reduced by 1 min
- **Blistering Scales** _(row 6, [360827](https://www.wowhead.com/spell=360827))_ — Protect an ally with explosive dragonscales, increasing their Armor by $<perc>% of your own
- **Draconic Attunements** _(row 6, [403208](https://www.wowhead.com/spell=403208))_ — Learn to attune yourself to the essence of the Black or Bronze Dragonflights:
- **Prescience** _(row 6, [409311](https://www.wowhead.com/spell=409311))_ — Grant an ally the gift of foresight, increasing their critical strike chance by 3% and occasionally copying their damage and healing spells at 15% power for 18 sec
- **Tectonic Locus** _(row 7, [408002](https://www.wowhead.com/spell=408002))_ — Upheaval deals 50% increased damage to the primary target, and launches them higher
- **Unyielding Domain** _(row 7, [412733](https://www.wowhead.com/spell=412733))_ — Upheaval cannot be interrupted, and has an additional 10% chance to critically strike
- **Molten Blood** _(row 7, [410643](https://www.wowhead.com/spell=410643))_ — When cast, Blistering Scales grants the target a shield that absorbs up to $<shield> damage for 30 sec based on their missing health. Lower health targets gain a larger shield
- **Regenerative Chitin** _(row 7, [406907](https://www.wowhead.com/spell=406907))_ — Blistering Scales no longer loses charges and deals 20% more damage
- **Momentum Shift** _(row 7, [408004](https://www.wowhead.com/spell=408004))_ — Consuming Essence Burst grants you 5% Intellect for 6 sec. Stacks up to N times
- **Aspects' Favor** _(row 7, 2 ranks, [407243](https://www.wowhead.com/spell=407243))_ — Obsidian Scales activates Black Attunement, and amplifies it to increase maximum health by $<blacktotal>% for 12 sec  _(ranks: 1/2)_
- **Arcane Reach** _(row 7, [454983](https://www.wowhead.com/spell=454983))_ — The range of your helpful magics is increased by 5 yards
- **Fate Mirror** _(row 7, [412774](https://www.wowhead.com/spell=412774))_ — Prescience grants the ally a chance for their spells and abilities to echo their damage or healing, dealing 15% of the amount again
- **Symbiotic Bloom** _(row 7, 2 ranks, [410685](https://www.wowhead.com/spell=410685))_ — Emerald Blossom increases targets' healing received by 6% for 10 sec  _(ranks: 3/6)_
- **Reactive Hide** _(row 8, [409329](https://www.wowhead.com/spell=409329))_ — Each time Blistering Scales explodes it deals 15% more damage for 12 sec, stacking N times
- **Font of Magic** _(row 8, [408083](https://www.wowhead.com/spell=408083))_ — Your empower spells' maximum level is increased by 1, and they reach maximum empower level -20% faster
- **Hoarded Power** _(row 8, [375796](https://www.wowhead.com/spell=375796))_ — Essence Burst has a 20% chance to not be consumed
- **Motes of Possibility** _(row 8, [409267](https://www.wowhead.com/spell=409267))_ — Eruption has a 25% chance to form a mote of diverted essence near you. Allies who comes in contact with the mote gain a random buff from your arsenal
- **Anachronism** _(row 8, [407869](https://www.wowhead.com/spell=407869))_ — Prescience has a 35% chance to grant Essence Burst
- **Dream of Spring** _(row 8, [414969](https://www.wowhead.com/spell=414969))_ — Emerald Blossom no longer has a cooldown, deals 35% increased healing, and increases the duration of your active Ebon Might effects by 1 sec, but costs 3 Essence
- **Prolong Life** _(row 8, [410687](https://www.wowhead.com/spell=410687))_ — Your effects that extend Ebon Might also extend Symbiotic Bloom
- **Accretion** _(row 9, [407876](https://www.wowhead.com/spell=407876))_ — Eruption reduces the remaining cooldown of Upheaval by 1 sec
- **Imminent Destruction** _(row 9, [459537](https://www.wowhead.com/spell=459537))_ — Breath of Eons reduces the Essence cost of your next 6 Eruptions by 1
- **Time Skip** _(row 9, [404977](https://www.wowhead.com/spell=404977))_ — Surge forward in time, causing your cooldowns to recover 1000% faster for 2 sec
- **Clairvoyant** _(row 9, [1250914](https://www.wowhead.com/spell=1250914))_ — Motes of Possibility may now grant Prescience to allies and have a 10% increased chance to activate
- **Inferno's Blessing** _(row 9, [410261](https://www.wowhead.com/spell=410261))_ — Fire Breath grants the inferno's blessing for 8 sec to you and a nearby ally, giving their damaging attacks and spells a high chance to deal an additional $<dmg> Fire damage
- **Rumbling Earth** _(row 10, [459120](https://www.wowhead.com/spell=459120))_ — Upheaval causes an aftershock at its location, dealing 30% of its damage 2 additional times
- **Plot the Future** _(row 10, [407866](https://www.wowhead.com/spell=407866))_ — Breath of Eons grants you Fury of the Aspects for 15 sec after you land, without causing Exhaustion
- **Interwoven Threads** _(row 10, [412713](https://www.wowhead.com/spell=412713))_ — The cooldowns of your spells are reduced by 10%
- **Tomorrow, Today** _(row 10, [412723](https://www.wowhead.com/spell=412723))_ — Time Skip channels for 1 sec longer
- **Overlord** _(row 10, [410260](https://www.wowhead.com/spell=410260))_ — Breath of Eons casts an Eruption at the first 3 enemies struck. These Eruptions have a 100% chance to create a Mote of Possibility
- **Mighty Inferno** _(row 10, [1291457](https://www.wowhead.com/spell=1291457))_ — Inferno's Blessing's damage is increased by 40%, and your effects that extend Ebon Might also extend Inferno's Blessing
- **Duplicate** _(row 11, [1259173](https://www.wowhead.com/spell=1259173))_ — Breath of Eons summons a version of you from the future to assist you in battle, lasting 20 sec. Your duplicate casts Eruption, Fire Breath, and Upheaval

### Scale Commander hero tree (Devastation & Augmentation) — 18 nodes

- **Mass Eruption** _(row 1, [438587](https://www.wowhead.com/spell=438587))_ — Empower spells cause your next Eruption to strike up to 3 targets. When striking less than 3 targets, Eruption damage is increased by 10% for each missing target
- **Mass Disintegrate** _(row 1, [436335](https://www.wowhead.com/spell=436335))_ — Empower spells cause your next Disintegrate to strike up to 3 targets. When striking fewer than 3 targets, Disintegrate damage is increased by 10% for each missing target
- **Might of the Black Dragonflight** _(row 2, [441705](https://www.wowhead.com/spell=441705))_ — Black spells deal 20% increased damage
- **Bombardments** _(row 2, [434300](https://www.wowhead.com/spell=434300))_ — Mass Disintegrate marks your primary target for destruction for the next 6 sec
- **Onslaught** _(row 2, [441245](https://www.wowhead.com/spell=441245))_ — Entering combat grants a charge of Burnout, causing your next Living Flame to cast instantly
- **Command Squadron** _(row 2, [1260745](https://www.wowhead.com/spell=1260745))_ — While flying during Breath of Eons you are assisted by a squadron of Dracthyr who assault enemies with Pyre, dealing N Fire damage to nearby enemies up to 8 times
- **Melt Armor** _(row 3, [441176](https://www.wowhead.com/spell=441176))_ — Breath of Eons causes enemies to take 20% increased damage from Bombardments and Essence abilities for 12 sec
- **Wingleader** _(row 3, [441206](https://www.wowhead.com/spell=441206))_ — Bombardments reduce the cooldown of **Deep Breath** (Devastation) by 0.5 sec per target struck, up to 1.5 sec — or **Breath of Eons** (Augmentation) by **1.0 sec per target struck, up to 3.0 sec** — *per Bombardment* (effN1/2 = Dev, effN3/4 = Aug). Scales with target density and proc count.
- **Unrelenting Siege** _(row 3, [441246](https://www.wowhead.com/spell=441246))_ — For each second you are in combat, Azure Strike, Living Flame, and Disintegrate deal 1% increased damage, up to 15%
- **Concentrated Power** _(row 3, [1261448](https://www.wowhead.com/spell=1261448))_ — Mass Disintegrate strikes 1 additional targets
- **Hardened Scales** _(row 4, [441180](https://www.wowhead.com/spell=441180))_ — Obsidian Scales reduces damage taken by an additional 10%
- **Menacing Presence** _(row 4, [441181](https://www.wowhead.com/spell=441181))_ — Knocking enemies up or backwards reduces their damage done to you by 15% for 8 sec
- **Diverted Power** _(row 4, [441219](https://www.wowhead.com/spell=441219))_ — Bombardments have a chance to generate Essence Burst
- **Extended Battle** _(row 4, [441212](https://www.wowhead.com/spell=441212))_ — Essence abilities extend Bombardments by 1 sec
- **Nimble Flyer** _(row 4, [441253](https://www.wowhead.com/spell=441253))_ — While Hovering, damage taken from area of effect attacks is reduced by 10%
- **Slipstream** _(row 4, [441257](https://www.wowhead.com/spell=441257))_ — Breath of Eons resets a charge of Hover
- **Refined Essence** _(row 4, [1261452](https://www.wowhead.com/spell=1261452))_ — Essence abilities deal 15% additional damage
- **Maneuverability** _(row 5, [433871](https://www.wowhead.com/spell=433871))_ — Breath of Eons can now be steered in your desired direction

### Flameshaper hero tree (Devastation) — 17 nodes

- **Legacy of the Lifebinder** _(row 1, [1264269](https://www.wowhead.com/spell=1264269))_ — Fire Breath gains an additional charge
- **Shape of Flame** _(row 2, [445074](https://www.wowhead.com/spell=445074))_ — Tail Swipe and Wing Buffet scorch enemies and blind them with ash, causing their next attack within 4 sec to miss
- **Trailblazer** _(row 2, [444849](https://www.wowhead.com/spell=444849))_ — Hover and Deep Breath travel 40% faster, and Hover travels 40% further
- **Ashes in Motion** _(row 2, [1264365](https://www.wowhead.com/spell=1264365))_ — Fire Breath's cooldown is reduced by 5 sec
- **Enkindle** _(row 2, [444016](https://www.wowhead.com/spell=444016))_ — Essence abilities are enhanced with Flame, dealing 20% of healing or damage done as Fire over 8 sec
- **Expanded Lungs** _(row 2, [444845](https://www.wowhead.com/spell=444845))_ — Fire Breath's damage over time is increased by 30%. Dream Breath's heal over time is increased by 30%
- **Essence Well** _(row 2, [1265993](https://www.wowhead.com/spell=1265993))_ — Fire Breath has a 50% chance to generate Essence Burst
- **Conduit of Flame** _(row 3, [444843](https://www.wowhead.com/spell=444843))_ — Critical strike chance against targets above 50% health increased by 15%
- **Burning Adrenaline** _(row 3, [444020](https://www.wowhead.com/spell=444020))_ — Fire Breath reaches its maximum empower level -20% faster
- **Fulminous Roar** _(row 3, [1218447](https://www.wowhead.com/spell=1218447))_ — Fire Breath deals its damage -20% more often
- **Twin Flame** _(row 3, [1265979](https://www.wowhead.com/spell=1265979))_ — Consuming Essence Burst fires a twin flame, striking your target for N Fire damage
- **Titanic Precision** _(row 4, [445625](https://www.wowhead.com/spell=445625))_ — Living Flame and Azure Strike have 1 extra chance to trigger Essence Burst when they critically strike
- **Deep Exhalation** _(row 4, [1264321](https://www.wowhead.com/spell=1264321))_ — Fire Breath's damage over time lasts 4 sec longer
- **Draconic Instincts** _(row 4, [445958](https://www.wowhead.com/spell=445958))_ — Your wounds have a small chance to cauterize, healing you for 30% of damage taken. Occurs more often from attacks that deal high damage
- **Lifecinders** _(row 4, [444322](https://www.wowhead.com/spell=444322))_ — Obsidian Scales also applies to your target or 1 nearby injured allies at 50% value
- **Fire Torrent** _(row 4, [1265992](https://www.wowhead.com/spell=1265992))_ — Twin Flame bounces to up to 2 additional targets
- **Consume Flame** _(row 5, [444088](https://www.wowhead.com/spell=444088))_ — Disintegrate damage consumes 1 sec of Fire Breath from enemies it damages, detonating it for 150% of the amount consumed

### Chronowarden hero tree (Augmentation) — 17 nodes

- **Energy Cycles** _(row 3, [1260568](https://www.wowhead.com/spell=1260568); not in the SimC spell-data dump — sourced from `sc_evoker.cpp` + Wowhead)_ — While **Temporal Burst** is active you gain an Essence Burst every ~6 sec (see mechanics doc §4).

- **Chrono Flame** _(row 1, [431442](https://www.wowhead.com/spell=431442))_ — Living Flame is enhanced with Bronze magic, repeating 15% of the damage or healing you dealt to the target in the last 5 sec as Arcane, up to $<cap2>
- **Warp** _(row 2, [429483](https://www.wowhead.com/spell=429483))_ — Hover now causes you to briefly warp out of existence and appear at your destination. Hover's cooldown is also reduced by 5 sec
- **Temporal Burst** _(row 2, [431695](https://www.wowhead.com/spell=431695))_ — Tip the Scales overloads you with temporal energy, increasing your haste, movement speed, and cooldown recovery rate by N%, decreasing over 30 sec
- **Chronoboon** _(row 2, [1260484](https://www.wowhead.com/spell=1260484))_ — Tip the Scales' cooldown is reduced by 30 sec
- **Reverberations** _(row 2, [431615](https://www.wowhead.com/spell=431615))_ — Verdant Embrace heals for an additional 60% over 8 sec
- **Motes of Acceleration** _(row 3, [432008](https://www.wowhead.com/spell=432008))_ — Warp leaves a trail of Motes of Acceleration. Allies who come in contact with a mote gain 20% increased movement speed for 30 sec
- **Temporality** _(row 3, [431873](https://www.wowhead.com/spell=431873))_ — Warp reduces damage taken by 20%, starting high and reducing over 3 sec
- **Nozdormu Adept** _(row 3, [431715](https://www.wowhead.com/spell=431715))_ — Temporal Anomaly mana cost reduced by 15% and cooldown reduced by 4 sec
- **Chronal Dynamo** _(row 3, [1291522](https://www.wowhead.com/spell=1291522))_ — Living Flame's cast time is reduced by 0.2 sec, and it deals 50% increased damage or healing when it is a non-instant cast
- **Primacy** _(row 3, [431657](https://www.wowhead.com/spell=431657))_ — For each healing over time effect from Verdant Embrace, gain 3% haste, up to 9%
- **Double-time** _(row 4, [431874](https://www.wowhead.com/spell=431874))_ — When Dream Breath or Fire Breath critically strike, their duration is extended by 2 sec, up to a maximum of 12 sec
- **Time Convergence** _(row 4, [431984](https://www.wowhead.com/spell=431984))_ — Non-defensive abilities with a 45 second or longer cooldown grant 5% Intellect for 15 sec
- **Instability Matrix** _(row 4, [431484](https://www.wowhead.com/spell=431484))_ — Each time you cast an empower spell, unstable time magic reduces its cooldown by up to 6 sec
- **Overclock** _(row 4, [1260647](https://www.wowhead.com/spell=1260647))_ — Chrono Flames' maximum damage or healing is increased by 40%, up to $<cap> Arcane
- **Golden Opportunity** _(row 4, [432004](https://www.wowhead.com/spell=432004))_ — Echo is 10% more effective
- **Afterimage** _(row 5, [431875](https://www.wowhead.com/spell=431875))_ — Empower spells send up to 3 Chrono Flames to your targets

---

## Build-string reference (current SimC defaults)
`talents=` strings from the SimC `midnight` MID1 profiles (in this folder):
- **Devastation — Scale Commander** (`MID1_Evoker_Devastation_SC.simc`):
  `CsbBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAzMDMDzgBmZGjZaYmpZMWmxMzMz8AzMzAmxMGzMLzMDMwYwCsMGN2GQmBBbYGMzghB`
- **Devastation — Flameshaper** (`MID1_Evoker_Devastation_FS.simc`):
  `CsbBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgZmZwMDGMgBjZamZmJjxyMzMzwMzMzAmxMzYmZbmZwMwMmB2ALgZYCsFsMMAmZGG`
- **Augmentation:** SimC ships **no** pre-built Aug profile (APL only). Use live
  build pages: [Wowhead Aug Midnight S1](https://www.wowhead.com/guide/classes/evoker/augmentation/midnight-season-1),
  [Murlok Aug SC M+](https://murlok.io/evoker/augmentation/scalecommander/m+),
  [Archon Aug M+](https://www.archon.gg/wow/builds/augmentation/evoker/mythic-plus/talents/high-keys/all-dungeons/this-week).

## Sources
- SimC `midnight`: [`SpellDataDump/evoker.txt`](https://github.com/simulationcraft/simc/blob/midnight/SpellDataDump/evoker.txt) (tooltips + effect values), [`sc_evoker.cpp`](https://github.com/simulationcraft/simc/blob/midnight/engine/class_modules/sc_evoker.cpp) (classification).
- Per-talent live numbers: Wowhead spell links inline.
- Narrative + meta: `EVOKER_MIDNIGHT_MECHANICS.md`.
