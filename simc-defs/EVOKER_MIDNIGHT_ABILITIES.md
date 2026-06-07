# Evoker active-ability reference — WoW *Midnight* S1 (12.0.5, ~June 2026)

Precise active-ability stats for the two DPS Evoker specs, extracted from
SimulationCraft `midnight` `SpellDataDump/evoker.txt` and value-resolved
(companion to `EVOKER_MIDNIGHT_TALENTS.md` and `EVOKER_MIDNIGHT_MECHANICS.md`).

## How to read
- Stat line: **spell type · school · cast/channel/empower/instant · resource ·
  cooldown · charges · duration · range · max targets**. `Coeff` = spell-power
  coefficient per effect (`SP×k`) and chain-target count — the relative
  power knob the sim uses.
- **`N`** = a value not in the static dump (spell-power-scaled damage, or a
  max-stack count). Click the spell-id → Wowhead for live numbers.
- **Empower** spells (Fire Breath, Eternity Surge, Upheaval) charge to ranks
  1–4 (`GCD 0.5s`, hold-to-empower); higher rank = more targets/damage.
- Notable Midnight change captured below: **Shattering Star is no longer a
  separate button** — it's the passive **Shattering Stars** talent, fired by
  Eternity Surge.

---
## Abilities

### Shared / class

- **Living Flame** _(id 361469)_ — Magic · Fire · cast 2s · 25yd.  
  Send a flickering flame towards your target, healing an ally for N or dealing N Fire damage to an enemy
- **Azure Strike** _(id 362969)_ — Magic · Spellfrost · instant · 25yd. Coeff: e2 SP×1.63.  
  Project intense energy onto 2 enemies, dealing N Spellfrost damage to them
- **Deep Breath** _(id 357210)_ — Magic · Firestorm · instant · CD 1s · 1 charge/120s · dur 6s · 15 - 50yd.  
  Take in a deep breath and fly to the targeted location, spewing molten cinders dealing N Volcanic damage to enemies in your path
- **Hover** _(id 358267)_ — None · Physical · instant · CD 1s · 1 charge/35s · dur 6s.  
  Launch yourself and gain 30% increased movement speed for N sec
- **Tip the Scales** _(id 370553)_ — Magic · Arcane · instant · CD 120s.  
  Compress time to make your next empowered spell cast instantly at its maximum empower level
- **Quell** _(id 351338)_ — Ranged · Physical · instant · CD 20s · dur 6s · 25yd.  
  Interrupt an enemy's spellcasting and prevent any spell from that school of magic from being cast for 6 sec

### Devastation

- **Disintegrate** _(id 356995)_ — Magic · Spellfrost · channel 3s · 3 Essence · 25yd. Coeff: e1 SP×1.59.  
  Tear into an enemy with a blast of blue magic, inflicting N Spellfrost damage over 3 sec, and slowing their movement speed by 50% for 3 sec
- **Pyre** _(id 357211)_ — Magic · Fire · instant · 3 Essence · 25yd.  
  Lob a ball of flame, dealing N Fire damage to your target and all enemies within 8 yds
- **Fire Breath (empower)** _(id 357208)_ — None · Fire · channel 2.5s · 1 charge/30s.  
  Inhale, stoking your inner flame. Release to exhale, burning enemies in a cone in front of you for N Fire damage, reduced beyond 5 targets
- **Eternity Surge (empower)** _(id 359073)_ — None · Spellfrost · channel 2.5s · CD 30s · 25yd.  
  Focus your energies to release a salvo of pure magic, dealing N Spellfrost damage to an enemy. Damages additional enemies within 25 yds when empowered
- **Dragonrage** _(id 375087)_ — None · Physical · instant · CD 120s · dur 18s.  
  Erupt with draconic fury and exhale Pyres at 3 enemies within 25 yds
- **Shattering Star (Shattering Stars talent)** _(id 1265804)_ — Magic · Spellfrost · instant · 25yd. Coeff: e1 SP×1.74.  
  Exhale a bolt of concentrated power from your mouth at the target for N Spellfrost damage
- **Azure Sweep** _(id 1265867)_ — None · Spellfrost · instant.  
  Eternity Surge upgrades your next Azure Strike to Azure Sweep, damaging all nearby enemies and dealing 75% additional damage

### Augmentation

- **Eruption** _(id 395160)_ — Magic · Firestorm · cast 2.5s · 3 Essence · 25yd. Coeff: e1 SP×2.8.  
  Cause a violent eruption beneath an enemy's feet, dealing N Volcanic damage split between them and nearby enemies
- **Upheaval (empower)** _(id 396286)_ — None · Firestorm · channel 2.5s · CD 40s · 25yd.  
  Gather earthen power beneath your enemy's feet and send them hurtling upwards, dealing N Volcanic damage to the target and nearby enemies
- **Ebon Might** _(id 395152)_ — Magic · Firestorm · cast 1.5s · CD 30s · dur 10s · max 30 tgts.  
  Increase all damage dealing allies' primary stat by N% of your own and increase your own damage by 20% for 10 sec
- **Prescience** _(id 409311)_ — Magic · Arcane · instant · 2 charge/12s · 25yd · max 1 tgts.  
  Grant an ally the gift of foresight, increasing their critical strike chance by 3% and occasionally copying their damage and healing spells at 15% power for 18 sec
- **Breath of Eons** _(id 403631)_ — None · Arcane · instant · CD 120s · dur 6s · 15 - 50yd.  
  Fly to the targeted location, exposing a on enemies in your path for 10 sec and granting Ebon Might for 5 sec
- **Blistering Scales** _(id 360827)_ — Magic · Firestorm · instant · CD 30s · dur 3600s · 25yd · max 1 tgts.  
  Protect an ally with explosive dragonscales, increasing their Armor by N% of your own

### Scale Commander mechanics

- **Mass Disintegrate (buff)** _(id 436336)_ — None · Arcane · instant · dur 15s.  
  Empower spells cause your next Disintegrate to strike up to 3 targets. When striking fewer than 3 targets, Disintegrate damage is increased by 10% for each missing target
- **Mass Eruption (buff)** _(id 438588)_ — None · Firestorm · instant · dur 15s.  
  Empower spells cause your next Eruption to strike up to 3 targets. When striking less than 3 targets, Eruption damage is increased by 10% for each missing target
- **Bombardments (debuff)** _(id 434473)_ — None · Firestorm · instant · dur 6s · 100yd.  
  Mass Disintegrate marks your primary target for destruction for the next 6 sec
- **Bombardments (damage)** _(id 434481)_ — Magic · Firestorm · instant · 100yd. Coeff: e1 SP×4.75.  
  Mass Disintegrate marks your primary target for destruction for the next 6 sec
- **Melt Armor (debuff)** _(id 441172)_ — Magic · Firestorm · instant · dur 12s · 100yd. Coeff: e1 SP×1.  
  Deep Breath (Dev) / Breath of Eons (Aug) applies Melt Armor: enemies take 20% increased damage from your Disintegrate, Pyre and Bombardments (Essence abilities) for 12 sec (effect #2).
