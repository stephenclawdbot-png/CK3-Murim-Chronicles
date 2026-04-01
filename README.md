# The Murim Chronicles -- CK3 Mod

**All Under Heaven: The Way of the Martial Sage**

A Crusader Kings 3 mod that layers a complete wuxia/xianxia martial arts system onto the vanilla game map. Noble houses cultivate internal energy, master divine techniques, and wage war for control of the Murim -- the martial world beneath heaven.

> **Design Philosophy:** Same map, same countries, new mechanics. Every vanilla title, province, and character remains intact. Murim Chronicles adds cultivation, sects, and jianghu systems as an overlay -- not a total conversion of geography or political boundaries.

**Current Version:** 0.4.0-alpha | **Files:** 43 | **Status:** Active Development (Phase 3 in progress, Phase 4 started)

---

## Table of Contents

- [Features](#features)
- [Breakthrough System](#breakthrough-system)
- [Variable System](#variable-system)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Compatibility](#compatibility)
- [Known Issues](#known-issues)
- [Roadmap](#roadmap)
- [Credits](#credits)

---

## Features

### Cultivation System
Characters progress through a 7-tier cultivation ladder with XP-based advancement:

| Realm | Trait Key | Prowess | Health | Lifespan | Special |
|-------|-----------|---------|--------|----------|---------|
| Qi Refinement | `murim_outer_qi` | +2 | +0.5 | -- | Can learn techniques |
| Foundation | `murim_qi_gathering` | +5 | +1 | -- | Martial +2 |
| Core Formation | `murim_foundation` | +10 | +2 | -- | Dread +5 |
| Nascent Soul | `murim_golden_core` | +20 | +4 | +50 | Dread +15 |
| Void | `murim_nascent_soul` | +40 | +8 | +100 | Culture opinion +20 |
| Great Vehicle | `murim_spirit_severing` | +80 | +15 | +200 | Enemy attrition |
| Heavenly Tribulation | `murim_heavenly_tribulation` | +150 | +30 | +500 | Immortal |

- **XP Gain** scales with learning, cultivation traits, meditation, body tempering, and era modifiers
- **Breakthrough Checks** -- monthly rolls gated by XP thresholds, trait bonuses, and qi deviation risk
- **Qi Deviation** -- failed breakthroughs can cripple or kill; risk increases at higher realms
- **Dual-Path Tension** -- practicing both orthodox and demonic cultivation multiplies deviation risk
- **Meridian System** -- flow efficiency affects XP rate and technique power
- **Era Modifiers** -- Golden Ages boost cultivation speed; Decline Eras punish it
- **Body Constitution** -- rare birth traits (Pure Yang Body, Pure Yin Body, Heavenly Spirit Body) grant qi capacity and cultivation bonuses

### Breakthrough System (NEW)
A comprehensive 40+ event chain system governing cultivation stage advancement:

| Stage Transition | Qi Required | Key Mechanics |
|-----------------|-------------|---------------|
| Qi Condensation (1->2) | 50 qi | Focused meditation, forceful compression, or master-guided paths |
| Foundation Establishment (2->3) | 150 qi | Body tempering, spiritual root purification, sect resource support |
| Core Formation (3->4) | 300 qi | Golden core vs perfect core outcomes, dual cultivation option |
| Nascent Soul (4->5) | 500 qi | Soul separation, heavenly tribulation path, age requirement 25+ |
| Soul Transformation (5->6) | 800 qi | Nine-fold tribulation, sect formation ritual, age requirement 35+ |

**Breakthrough Features:**
- **Multiple Paths** -- each stage offers 3-4 distinct breakthrough methods with different risk/reward profiles
- **Perfect Core (Rare)** -- patient cultivators can achieve a perfect golden core with 2x qi bonus and decade-long buffs
- **Tribulation-Forged Soul** -- surviving heavenly tribulation during nascent soul yields the strongest variant
- **Failure Cascade** -- minor (qi deviation) -> moderate (meridian damage) -> severe (cracked core) -> catastrophic (cultivation crippled)
- **Forbidden Restoration** -- crippled cultivators can seek demonic techniques to restore cultivation at great cost
- **Heavenly Tribulation Events** -- lightning tribulation and nine-thunder tribulation for Stage 4+ cultivators
- **Bottleneck System** -- stuck cultivators can meditate, travel, or fight stronger opponents for inspiration
- **Rival Interference** -- enemies can attack during vulnerable breakthrough states; allies or sect formations provide protection
- **Master-Guided Breakthroughs** -- mentors improve success rates and can share secret techniques
- **Environmental Bonuses** -- spiritual nexus discovery, cultivation chambers, ancestral inheritance from deceased cultivator parents
- **Sect Formation Rituals** -- high-ranked sect members participate in group empowerment ceremonies

### Trait System
Eight distinct trait groups with 28+ individual traits across martial disciplines:

| Group | Traits | Focus |
|-------|--------|-------|
| Cultivation Realm | 7 tiers | Core power progression |
| Sword Aptitude | 5 tiers (Seed -> Immortal) | Sword mastery + knight effectiveness |
| Body Cultivation | 4 tiers (Iron Skin -> Golden Body) | Durability + health + enemy attrition |
| Demonic Aptitude | 3 tiers | Prowess + intrigue at stress cost |
| Alchemy | 3 tiers | Learning + health + development |
| Genius/Crippled | 3 special | Heaven-Defying Genius, Crippled Meridian, Secret Manual Holder |
| Body Constitution | 3 rare | Pure Yang, Pure Yin, Heavenly Spirit Body |
| Mixed Martial | 7 hybrid + 4 seasonal | Multi-stat combinations + celestial alignment |
| Grind Loop | 5+ training | Active cultivation, meditation, body tempering states |

All trait keys use the `murim_` prefix convention for consistency with script values.

### Jianghu Standing
A 0-100 reputation system governing a character's place in the martial world:

- **Standing Gains** from winning duels, hosting tournaments, defending the weak, generous sect donations
- **Standing Losses** from dishonorable kills, breaking oaths, associating with demonic cultivators
- **Wulin Alliance Elections** -- high-standing characters compete for Alliance Leader; weighted by standing, cultivation rank, sect power, and renown
- **Face Mechanics** -- losing face triggers opinion penalties; restoring face requires public acts
- **Righteous Crusade** -- at standing 80+, characters can call the jianghu to war against demonic threats
- **Wandering Hero** reputation track for unaffiliated cultivators

### Sect System
Sects are landless hidden titles with their own power dynamics:

- **Sect Ranks** (Outer Disciple -> Inner Disciple -> Core Disciple -> Elder -> Sect Leader)
- **Sect Types** -- Sword Sects, Alchemy Sects, Demonic Sects, Buddhist Sects, Scholarly Sects
- **Sect Wars** -- sects can declare war on each other independent of feudal politics
- **Resource System** -- sects accumulate spirit stones, technique scrolls, and medicinal herbs
- **Sect Decisions** -- 47,000+ bytes of decisions including establishing sects, hosting tournaments, issuing edicts, and managing disciples

### Jianghu Underground (Phase 4 - In Progress)
The wuxia world operates in the shadows beneath the imperial court:

- **Shadow Networks** -- cultivators secretly influence who gets titles, passes examinations, wins battles, and controls trade routes
- **Underground Decisions** -- Form Underground Sect, Declare Wulin Alliance, Launch Imperial Crackdown, Establish Shadow Court, Rig Imperial Examinations, Open Black Market, Commission Assassination, Seek Imperial Patronage
- **Jianghu Events** -- 82,000+ bytes covering underground tournaments, sect wars spilling into imperial politics, spy exposure at court, assassination attempts on the emperor, forbidden technique auctions, imperial crackdowns, wulin alliance summits, trade route disputes, black market raids

### Technique System
60+ martial techniques organized by style:

- **Sword Techniques** -- Falling Leaves, Seven Stars, Void Slash, Heaven-Splitting Strike
- **Body Techniques** -- Iron Shirt, Diamond Body, Phoenix Rebirth
- **Internal Techniques** -- Qi Tsunami, Dragon's Breath, Celestial Circulation
- **Forbidden Techniques** -- Soul Devourer, Blood Sacrifice, Corpse Manipulation
- Each technique has learning requirements, mastery progression, and combat applications

### Combat & Duel System
- **Formal Duels** governed by jianghu rules with seconds and stakes
- **Ambush Mechanics** for dishonorable assassinations
- **Tournament Events** -- realm-wide competitions with prestige and standing rewards
- **Army Buff System** -- high-realm cultivators provide attrition, toughness, and pursuit bonuses to their armies

### Celestial System
- **Celestial governments** with immortal ruler mechanics
- **Celestial events** -- 29,000+ bytes of heavenly phenomena, divine interventions, and spiritual realm interactions
- **Script values** for celestial calculations and power scaling

### Scheme System
- **33,000+ bytes** of martial schemes including assassination, qi theft, technique stealing, sect infiltration, and political manipulation
- Deep integration with CK3's intrigue system

### AI Autonomy
NPCs intelligently engage with martial systems:

- **Personality-driven cultivation** -- ambitious characters push harder; content ones meditate
- **AI war behavior** -- cultivator-commanders apply unique army strategies based on their cultivation realm and technique mastery
- **Sect AI** -- NPC sect leaders recruit, promote, and expel members based on loyalty and skill
- **Autonomous on-actions** -- 3 separate on_action files totaling 40,000+ bytes driving AI behavior

---

## Variable System

All persistent data uses CK3 character/dynasty variables:

| Variable | Type | Range | Description |
|----------|------|-------|-------------|
| `murim_cultivation_stage` | int | 0-6 | Current cultivation realm |
| `murim_qi_reserve` | int | 0-999 | Stored qi energy for breakthroughs |
| `murim_core_quality` | int | 0-3 | Golden core quality (0=none, 3=perfect) |
| `murim_tribulation_survivor` | int | 0-1 | Survived heavenly tribulation flag |
| `murim_sect_id` | int | 1-99 | Current sect membership |
| `murim_sect_rank` | int | 0-5 | Rank within sect hierarchy |
| `murim_jianghu_standing` | int | 0-100 | Reputation in the martial world |
| `murim_technique_mastery` | int | 0-100 | Current technique proficiency |
| `murim_meridian_flow` | int | 0-100 | Meridian efficiency |
| `murim_body_tempering` | int | 0-50 | Physical cultivation progress |
| `murim_combat_xp` | int | 0-999 | Martial combat experience |

---

## File Structure

```
CK3-Murim-Chronicles/
|-- descriptor.mod
|-- murim.mod
|-- README.md
|
|-- common/
|   |-- ai_war_behavior/
|   |   |-- murim_ai_aggression.txt              # AI army tactics for cultivators
|   |
|   |-- artifacts/
|   |   |-- 00_martial_artifacts.txt              # Legendary weapons & items
|   |
|   |-- character_interactions/
|   |   |-- murim_character_interactions.txt       # Core martial interactions
|   |
|   |-- character_modifiers/
|   |   |-- murim_grind_modifiers.txt             # Training loop modifiers
|   |
|   |-- cultures/
|   |   |-- 01_martial_cultures.txt               # Martial-focused cultures
|   |
|   |-- decisions/
|   |   |-- 00_martial_decisions.txt              # Base martial decisions
|   |   |-- murim_cultivation_decisions.txt       # 39KB cultivation decisions
|   |   |-- murim_jianghu_decisions.txt           # 30KB underground decisions [P4]
|   |   |-- murim_sect_decisions.txt              # 47KB sect management
|   |   |-- murim_technique_decisions.txt         # Technique learning decisions
|   |
|   |-- dynasty_legacies/
|   |   |-- 01_martial_legacies.txt               # Martial dynasty tracks
|   |   |-- 02_bloodline_inheritance.txt          # Cultivation bloodlines
|   |
|   |-- governments/
|   |   |-- celestial_governments.txt             # Immortal ruler government
|   |
|   |-- lands/
|   |   |-- 00_asia_murim_setup.txt               # Geographic setup
|   |
|   |-- on_actions/
|   |   |-- murim_on_actions.txt                  # 29KB core on-actions
|   |   |-- murim_ai_autonomy_on_actions.txt      # AI cultivation behavior
|   |   |-- murim_technique_on_actions.txt         # Technique learning triggers
|   |
|   |-- opinion_modifiers/
|   |   |-- murim_grind_opinions.txt              # Training-related opinions
|   |
|   |-- religions/
|   |   |-- 01_martial_religions.txt              # Cultivation-focused faiths
|   |
|   |-- schemes/
|   |   |-- murim_schemes.txt                     # 33KB martial schemes
|   |
|   |-- script_values/
|   |   |-- murim_cultivation_values.txt          # Cultivation scaling values
|   |   |-- murim_combat_values.txt               # Combat calculation values
|   |   |-- murim_celestial_values.txt            # Celestial power values
|   |   |-- murim_jianghu_values.txt              # Jianghu reputation values
|   |   |-- murim_sect_values.txt                 # Sect power values
|   |   |-- murim_grind_values.txt                # Training loop values
|   |
|   |-- scripted_effects/
|   |   |-- 00_celestial_effects.txt              # Celestial realm effects
|   |   |-- murim_grind_effects.txt               # Training loop effects
|   |   |-- murim_variable_init.txt               # 18KB variable initialization
|   |
|   |-- scripted_triggers/
|   |   |-- murim_grind_triggers.txt              # Training condition checks
|   |   |-- murim_technique_triggers.txt          # Technique requirement checks
|   |   |-- murim_condition_triggers.txt          # 10KB cultivation conditions
|   |
|   |-- traits/
|   |   |-- 01_martial_traits.txt                 # Core cultivation traits
|   |   |-- 02_mixed_martial_traits.txt           # Hybrid martial traits
|   |   |-- 03_prowess_technique_traits.txt       # Technique mastery traits
|   |   |-- 04_grind_loop_traits.txt              # Training state traits
|   |
|-- events/
|   |-- 00_cultivation_story.txt                  # Story event chains
|   |-- 00_region_interactions.txt                # Region-based encounters
|   |-- murim_cultivation_events.txt              # 72KB cultivation events
|   |-- murim_celestial_events.txt                # 29KB celestial events
|   |-- murim_combat_events.txt                   # 26KB combat events
|   |-- murim_grind_events.txt                    # Training loop events
|   |-- murim_interaction_events.txt              # Interaction result events
|   |-- murim_technique_events.txt                # Technique learning events
|   |-- murim_jianghu_events.txt                  # 82KB underground events [P4]
|   |-- murim_breakthrough_events.txt             # 39KB breakthrough events [P3] (NEW)
|   |
|-- localization/
|   |-- english/
|       |-- murim_l_english.yml                   # Core localization
|       |-- murim_grind_l_english.yml             # Training loop strings
|       |-- murim_techniques_l_english.yml        # Technique name strings
```

**Total: 43 script files** | ~630KB+ of PDX script

---

## Installation

1. Download or clone this repository
2. Copy the `CK3-Murim-Chronicles` folder to your CK3 mod directory:
   - **Windows:** `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\`
   - **macOS:** `~/Documents/Paradox Interactive/Crusader Kings III/mod/`
   - **Linux:** `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
3. Ensure both `murim.mod` and `descriptor.mod` are present
4. Launch CK3 and enable "The Murim Chronicles" in the mod launcher
5. Start a new game (recommended) or load an existing save

---

## Compatibility

- **CK3 Version:** 1.12+ (Royal Court and later)
- **DLC Requirements:** None (base game compatible)
- **DLC Enhanced:** Royal Court (artifacts), Tours & Tournaments (duels), Roads to Power (schemes)
- **Mod Conflicts:** May conflict with mods that heavily modify:
  - Trait files (overlapping trait keys)
  - On-action files (event trigger conflicts)
  - Government types (if using celestial governments)
- **Save Compatible:** Adding mid-save is supported; removing mid-save may cause variable errors
- **Map:** Uses vanilla map -- compatible with most visual/UI mods

---

## Known Issues

- Some localization strings are placeholder pending full Phase 3/4 completion
- Breakthrough event balance is still being tuned (qi costs and success rates)
- AI may occasionally spam cultivation decisions if trait checks are too lenient
- Celestial government succession may conflict with some vanilla succession laws
- Phase 4 jianghu underground system is partially implemented

---

## Roadmap

### Phase 1 -- Core Framework (COMPLETE)
- [x] Cultivation traits and realm progression
- [x] Basic sect system
- [x] Martial artifacts
- [x] Cultures, religions, dynasty legacies
- [x] Core event chains (cultivation, combat, celestial)
- [x] Variable initialization system
- [x] Geographic setup
- [x] Localization (core + techniques)

### Phase 2 -- Grind Loop & Combat (COMPLETE)
- [x] Script values (cultivation, combat, celestial, jianghu, sect, grind)
- [x] Scripted triggers (grind, technique)
- [x] Scripted effects (grind, celestial)
- [x] Training loop events, modifiers, opinions, traits
- [x] AI war behavior for cultivators
- [x] Technique on-actions and events

### Phase 3 -- Advanced Systems (IN PROGRESS - 5/9 files)
- [x] Cultivation decisions (39KB comprehensive system)
- [x] Sect decisions (47KB sect management)
- [x] Technique decisions
- [x] Condition triggers (10KB cultivation state checks)
- [x] Breakthrough events (39KB stage advancement system) **NEW**
- [ ] Sect events
- [ ] Duel events
- [ ] Penalty effects
- [ ] Penalty modifiers

### Phase 4 -- Wuxia Underground (IN PROGRESS - 2/9 files)
- [x] Jianghu decisions (30KB shadow politics)
- [x] Jianghu events (82KB underground world)
- [ ] Jianghu underground traits (30+ shadow world traits)
- [ ] Jianghu scripted triggers
- [ ] Jianghu scripted effects
- [ ] Jianghu character interactions (25+ unique interactions)
- [ ] Jianghu on-actions (AI underground autonomy)
- [ ] Imperial cultivator events
- [ ] Jianghu localization

### Phase 5 -- Polish & Balance (PLANNED)
- [ ] Full localization pass for all systems
- [ ] Balance tuning for breakthrough rates
- [ ] Performance optimization
- [ ] Comprehensive playtesting
- [ ] Steam Workshop release

---

## Credits

**The Murim Chronicles** is built with automated development assistance. All game mechanics are designed to integrate seamlessly with Crusader Kings 3's existing systems.

- **Game Engine:** Crusader Kings 3 by Paradox Interactive
- **Inspiration:** Wuxia/Xianxia literary tradition -- Jin Yong, Er Gen, I Eat Tomatoes
- **Development:** Automated build pipeline with manual design oversight

---

*"The Dao that can be told is not the eternal Dao. The name that can be named is not the eternal name." -- Laozi*

*"In the martial world, only the strong define what is right." -- Murim Proverb*
