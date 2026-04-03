# CK3 Murim Chronicles

> **A total conversion mod bringing the world of Murim (martial arts cultivation) to Crusader Kings 3**

[![Version](https://img.shields.io/badge/version-1.0.0--beta-blue)]()
[![CK3](https://img.shields.io/badge/CK3-1.18.2+-green)]()
[![Files](https://img.shields.io/badge/mod%20files-180+-orange)]()
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
| **Expansion** | Deep content (180+ event files, 9 sects) | COMPLETE |
| **Performance** | Optimized for smooth gameplay | COMPLETE |
| **Definitions** | Zero missing traits/modifiers/opinions | COMPLETE |

---

## v1.0.0 Changelog (Latest)

### Performance Optimization
- **All `every_living_character` converted to `every_ruler`** across 24+ event files and all on_actions -- eliminates expensive full-character-list iteration
- **All monthly pulses converted to quarterly** -- 66% reduction in idle CPU usage
- **XP values tripled** to maintain progression rate at quarterly frequency
- **Expensive `any_living_character` triggers replaced** with cheap flag/prowess checks in AI autonomy
- **Zero monthly pulses during normal gameplay** -- smooth idle performance

### Martial World / Vanilla Court Connection (NEW)
- **8 new events** linking the martial world to vanilla rulers as a shadow layer:
  - **Martial Advisor at Court** -- recruit a martial artist as informal advisor (intelligence, guard training, shadow whispers)
  - **Sect Leader Seeks Audience** -- a sect leader approaches the king/emperor (ally, enforcer, or decline)
  - **Imperial Martial Tournament** -- host a tournament to attract martial talent to your court
  - **Martial World Crisis** -- jianghu violence spills into your realm (military, diplomatic, or isolate)
  - **Shadow Behind the Throne** -- discover martial influence manipulating your court
  - **AI Court Influence** -- AI martial leaders autonomously seek court influence
  - **Martial World Intro** -- non-martial rulers learn about the jianghu for the first time
- Martial world stays **behind** vanilla -- no overrides, just shadow flavor and modifier benefits

### Ruler Rank Enforcement
- **Titled rulers who are martial artists get minimum rank:**
  - Emperor = Vice Leader (rank 5) minimum
  - King/Duke = Elder (rank 4) minimum  
  - Count = Inner Disciple (rank 3) minimum
- Enforced on title gain and yearly catch-all pulse
- A king wouldn't be an outer disciple -- political power earns martial respect

### Entry Path System Fix
- **All 4 entry paths now properly triggered** (previously only path 1 was connected):
  1. **Wanderer Path** -- unlanded characters with prowess discover the martial world
  2. **Ruler Path** -- landed rulers with martial courtiers learn cultivation secretly
  3. **Courtier Path** -- courtiers learn from martial peers at court
  4. **Adventurer Path** -- brave/curious/travelling characters encounter wandering masters
- **AI participates equally** via ai_chance on all options
- Both `martial_artist` trait AND `murim_martial_artist` variable now set on all creation paths for consistent detection

### Combat Safety System
- **All `death = { death_reason = death_battle }` calls** converted to `murim_combat_death_or_injury_effect`
- **Characters under age 16 are protected from death** -- receive severe injury instead (wounded_3 + trauma modifier)
- Consistent across ALL 180+ event files -- no exceptions

### Critical Bug Fixes
- **Fixed `has_trait = murim_martial_artist`** → `murim_is_martial_artist_trigger = yes` across 31 event files + on_actions. The trait was rarely added to characters, causing the entire calamity system and many expansion events to silently fail.
- **Fixed missing `scope:orthodox_leader`** in faction_war_expansion2 event 0007 (would crash CK3)
- **Fixed missing `immediate` block** for scope resolution in faction war events

### Complete Definition Coverage
- **413 trait definitions** added (murim_expansion_traits_patch.txt)
- **2,933 character modifier definitions** added across patch files
- **1,071 opinion modifier definitions** added across patch files  
- **36 county modifier definitions** verified
- **Zero silent failures** -- every `add_trait`, `add_character_modifier`, `add_opinion`, `has_character_modifier`, and `remove_character_modifier` call resolves to a real definition

### AI Sect Competition (NEW)
- **4 events** where AI martial leaders challenge each other and the player:
  - Elder challenges for sect leadership
  - Sect master challenges
  - Usurpation schemes
  - Alliance leader grand challenges
- AI can take your position -- creates dynamic power struggles

### Civilian Casualty System (NEW)
- **3 events** for martial world collateral damage:
  - Street fight collateral
  - Technique misfire
  - Village devastation
- Each has 3 options with different outcomes and AI weights

---

## Implemented Systems

### Core Systems
- **Cultivation System**: 7 realms from Outer Qi to Heavenly Tribulation with XP-based progression
- **9 Martial Sects**: Mount Hua, Shaolin, Wudang, Tang Clan, Beggar Sect, Iron Fist Gate (orthodox) + Heavenly Demon, Poison Flower Palace, Phantom Blade (unorthodox)
- **Sect Ranks**: Outer Disciple → Associate → Inner Disciple → Elder → Vice Leader → Leader
- **90+ Martial Traits**: Prowess techniques, body cultivation, qi deviation states, reputation titles
- **Top 50 Ranking System**: Dynamic martial rankings with yearly updates and ranking duels

### Event Systems (180+ files)
- **Cultivation Events**: Breakthroughs, qi deviation, meditation, body tempering, meridian opening
- **Duel System**: Honor duels, death matches, ranking fights, tournaments, ambush, revenge chains
- **Romance System**: Dual cultivation, forbidden love, soulmate bonds, marriage duels, love triangles
- **Calamity System**: Great Calamity cycles with phase-based progression, world-shaking events
- **Faction Wars**: Orthodox vs Unorthodox conflict chains with AI participation
- **Shadow Politics**: Court manipulation, spy networks, assassination, puppet schemes
- **Daily Life**: 20+ events for everyday martial world encounters
- **Sect-Specific Chains**: Deep event chains for each of the 9 sects
- **Court Connection**: Martial world influence on vanilla rulers (shadow layer)

### Performance
- Zero `every_living_character` calls in gameplay loops
- All pulses quarterly (not monthly) with tripled XP to compensate
- Cheap flag/stat checks replace expensive character iteration in triggers
- `has_variable = murim_martial_artist` gating skips non-martial characters early

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

## Key Features Summary

- **180+ event files** across cultivation, combat, romance, politics, sects, calamities, and court connection
- **2,900+ character modifier definitions** for every martial state and effect
- **1,000+ opinion modifier definitions** for nuanced relationships
- **400+ trait definitions** for martial progression and sect membership
- **9 distinct martial sects** with full event chains and rank systems
- **Full AI autonomy** -- NPCs cultivate, duel, join sects, seek court influence, and challenge for leadership
- **Shadow layer design** -- martial world operates behind vanilla, never overrides it
- **Youth protection** -- characters under 16 cannot die in martial combat
- **Performance optimized** -- quarterly pulses, efficient iteration, cheap trigger checks

---

## License

MIT License -- free to use, modify, and distribute.
