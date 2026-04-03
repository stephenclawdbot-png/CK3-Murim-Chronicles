# CK3 Murim Chronicles

> **A total conversion mod bringing the world of Murim (martial arts cultivation) to Crusader Kings 3**

[![Version](https://img.shields.io/badge/version-1.1.0--beta-blue)]()
[![CK3](https://img.shields.io/badge/CK3-1.18.2+-green)]()
[![Files](https://img.shields.io/badge/mod%20files-200+-orange)]()
[![License](https://img.shields.io/badge/license-MIT-lightgrey)]()
[![Phase](https://img.shields.io/badge/all%20phases-COMPLETE-brightgreen)]()

---

## Overview

**Murim Chronicles** transforms CK3 into a Wuxia/Xianxia cultivation world set in historical East Asia. Characters cultivate qi, practice martial techniques, join sects, duel rivals, undergo heavenly tribulations, and navigate the shadowy politics of the Jianghu -- the underground martial world that operates as a shadow layer behind vanilla CK3 politics.

The martial world exists **behind** vanilla -- it never overrides vanilla mechanics. Your vanilla court, wars, marriages, and politics continue as normal, while the martial world operates as a parallel layer of intrigue and power.

---

## Current Status

| Phase | Description | Status |
|-------|-------------|--------|
| **Phase 1** | Core Foundation (traits, sects, cultivation) | COMPLETE |
| **Phase 2** | Grind Loop Systems (training, modifiers) | COMPLETE |
| **Phase 3** | Advanced Mechanics (duels, rankings, celestial) | COMPLETE |
| **Phase 4** | Wuxia Underground (jianghu, black market) | COMPLETE |
| **Expansion** | Deep content (200+ event files, 9 sects) | COMPLETE |
| **Migration** | Global martial artist migration system | COMPLETE |
| **Performance** | Optimized for smooth gameplay | COMPLETE |
| **Definitions** | Zero missing traits/modifiers/opinions/events | COMPLETE |
| **Stability** | 10-loop automated audit, zero crash issues | COMPLETE |

---

## v1.1.0 Changelog (Latest)

### Global Martial Artist Migration System (NEW)
- **8 new migration events** bringing the martial world beyond China/Korea:
  - **Foreign masters hear rumors** of China's ranking system and journey east
  - **Arrival events** for foreign fighters entering the martial world
  - **Tournament challengers** from abroad enter competitions
  - **Wandering masters** appear at foreign courts
  - **AI auto-migration** ensures foreign masters actively seek China's rankings
- Foreign masters arrive with unique fusion martial arts modifiers

### Expanded Geographical Seeding
- **Three-tier seeding density**:
  - **Tier A (51%)**: China, Korea -- dense martial artist population
  - **Tier B (30%)**: Japan, Mongolia, Tibet, SE Asia, Jurchen, Tungusic -- moderate presence
  - **Global (0.5-2%)**: Rest of the world via foreign master spawns and talent discovery
- All regions use `culture = { has_cultural_pillar = heritage_X }` (CK3-correct syntax)

### Gender Equality
- **All `gender_female_chance` set to 50%** across every `create_character` block
- Martial artists can be male or female equally

### All 5 Skills Matter
- **Stewardship, Martial, Intrigue, Diplomacy** now factor into martial artist selection alongside Prowess
- Entry path triggers expanded to recognize non-combat talent
- Weighted selection in all 4 seeding tiers (basic/intermediate/advanced/elite)

### Comprehensive Crash Fixes
- **447 missing trait definitions** added across 3 trait files (1,213 total traits defined)
- **1,303 character memory types** defined (was 16 -- 1,287 were missing)
- **64 invalid `has_culture_group`** calls replaced with CK3-correct `has_cultural_pillar`
- **Invalid on_action hooks** fixed: `on_title_gain` -> `on_title_gained`, `on_ten_year_pulse` -> `on_five_year_pulse`, `on_bi_yearly_pulse` -> `on_yearly_pulse`
- **`increase_wounds_effect`** defined (80 calls, was undefined)
- **66 missing scripted trigger** stubs added
- **Namespace collision** (`murim_global`) resolved
- **Missing `beggar_sect_elder` trait** created (fixed dead seeding code)
- **Cultivation variables** (`murim_cultivation_rank`, `murim_cultivation_xp`, `murim_clan_rank`) added to ALL seeding tiers -- entire progression system was previously disconnected

### Dead-End Event Chain Fixes
- **110 stub events** created for all referenced-but-undefined event IDs
- Every decision, event chain, and scripted effect now reaches a valid event
- Themed content with appropriate rewards (cultivation XP, prestige, gold, etc.)
- Full localization for all 110 stub events

### Stability Verification
- **10-loop automated audit** confirms zero issues:
  - 0 bracket mismatches
  - 0 missing traits
  - 0 missing events
  - 0 missing effects/triggers
  - 0 missing memory types
  - 0 missing opinion/character modifiers
  - 0 invalid syntax
  - 0 duplicate event IDs or trait names
  - All localization files have UTF-8 BOM
- Automated audit script included (`audit_mod.py`) for future validation

---

## Gameplay Systems

### Cultivation & Progression
- **7 Cultivation Realms**: Outer Qi -> Qi Gathering -> Foundation -> Golden Core -> Nascent Soul -> Spirit Severing -> Heavenly Tribulation
- **XP-based progression**: Train, meditate, duel, and study to accumulate cultivation XP
- **Breakthrough events**: Attempt realm advancement with risk of qi deviation (catastrophic failure)
- **Cultivation variables**: `murim_cultivation_rank`, `murim_cultivation_xp`, `murim_clan_rank` track your progression
- **All 5 skills contribute**: Prowess (combat), Martial (strategy), Stewardship (resource management), Intrigue (shadow arts), Diplomacy (sect politics)

### 9 Martial Sects

**Orthodox (Righteous Path):**
| Sect | Specialty | Style |
|------|-----------|-------|
| Mount Hua | Sword arts, righteousness | Elegant swordsmanship |
| Shaolin | Buddhist martial arts, iron body | Monk combat and meditation |
| Wudang | Taoist cultivation, internal arts | Flowing defensive techniques |
| Beggar Sect | Information network, Dog Beating Staff | Street-level intelligence |
| Iron Fist Gate | Pure physical power | Crushing force techniques |
| Tang Clan | Hidden weapons, poisons | Assassination and alchemy |

**Unorthodox (Demonic Path):**
| Sect | Specialty | Style |
|------|-----------|-------|
| Heavenly Demon | Forbidden techniques, domination | Overwhelming dark power |
| Poison Flower Palace | Toxins, seduction, beauty | Poisonous and alluring arts |
| Phantom Blade | Assassination, stealth | Shadow killing techniques |

### Sect Ranks & Clan System
- **6 Ranks**: Outer Disciple -> Associate -> Inner Disciple -> Elder -> Vice Leader -> Leader
- **Clan rank enforcement**: Titled rulers get minimum rank matching their political power
- **Sect politics**: Internal power struggles, elder councils, succession crises
- **Custom clan creation**: Found your own martial clan

### Top 50 Ranking System
- **Dynamic rankings** updated periodically based on prowess, cultivation, and achievements
- **Ranking duels**: Challenge those above you, defend your position
- **Foreign challengers**: Masters from across the world seek to enter the Top 50
- **Prestige and reputation** tied to ranking position

### Duel & Combat System
- **Honor duels**: Formal challenges with witnesses and consequences
- **Death matches**: Lethal combat for dire situations
- **Tournament system**: Young Dragon Tournament (under-30) and Grand Tournament (all ages)
- **Ambush and revenge**: Surprise attacks and vendetta chains
- **Combat trauma**: Wounds, psychological scars, and recovery

### Romance & Relationships
- **Dual cultivation**: Train together with a romantic partner for mutual benefit
- **Forbidden love**: Cross-faction romance with sect consequences
- **Soulmate bonds**: Deep connections that transcend sect boundaries
- **Marriage duels**: Fight for the right to marry
- **Mentor-disciple romance**: Complex relationships with power dynamics

### Jianghu (Underground Martial World)
- **Shadow brokers**: Information dealers operating behind the scenes
- **Black market**: Trade forbidden techniques, rare herbs, and stolen artifacts
- **Protection rackets**: Control territory through martial force
- **Assassination contracts**: Hire killers or become one
- **Faction wars**: Orthodox vs. Unorthodox grand conflicts

### Great Calamity System
- **Cyclical catastrophes** that shake the entire martial world
- **Phase-based progression**: Warning signs -> Escalation -> Crisis -> Aftermath
- **World-altering consequences**: Sect destruction, mass casualties, power vacuums
- **Survivor benefits**: Those who endure gain unique traits and memories

### Court Connection (Shadow Layer)
- **Martial advisors** at court: Recruit martial artists as informal counselors
- **Sect audiences**: Sect leaders approach kings and emperors for political alliance
- **Imperial tournaments**: Host competitions to attract martial talent
- **Shadow behind the throne**: Discover martial influence manipulating your court
- **Non-martial rulers** can learn about the martial world

### AI Participation
- **Full AI autonomy**: NPCs cultivate, duel, join sects, and challenge for leadership
- **AI migration**: Foreign masters actively journey east seeking glory
- **Sect competition**: AI martial leaders challenge each other for dominance
- **Court influence**: AI martial leaders seek positions of power at court

---

## Mod Statistics

| Category | Count |
|----------|-------|
| Events | 2,085 |
| Traits | 1,213 |
| Character Modifiers | 3,867 |
| Scripted Effects | 274 |
| Scripted Triggers | 598 |
| Character Memory Types | 1,303 |
| Localization Keys | 4,331 |

---

## Installation

1. Download or clone this repository
2. Copy the `CK3-Murim-Chronicles` folder to your CK3 mod directory:
   - **Windows**: `%USERPROFILE%/Documents/Paradox Interactive/Crusader Kings III/mod/`
   - **Linux**: `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
   - **macOS**: `~/Documents/Paradox Interactive/Crusader Kings III/mod/`
3. Copy `murim.mod` to the `mod/` directory
4. Launch CK3 and enable "Murim Chronicles" in the mod launcher

---

## Validation

Run the included audit script to verify mod integrity:

```bash
python3 audit_mod.py
```

This checks: bracket balance, missing traits/events/effects/triggers, invalid syntax, duplicate IDs, localization BOMs, and more. A clean run shows `ALL CLEAR - No issues found!`

---

## License

MIT License -- free to use, modify, and distribute.
