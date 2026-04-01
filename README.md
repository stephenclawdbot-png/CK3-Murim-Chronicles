# CK3 Murim Chronicles

> **A total conversion mod bringing the world of Murim (martial arts cultivation) to Crusader Kings 3**

[![Version](https://img.shields.io/badge/version-0.5.0--alpha-blue)]()
[![CK3](https://img.shields.io/badge/CK3-1.12+-green)]()
[![Files](https://img.shields.io/badge/mod%20files-50-orange)]()
[![License](https://img.shields.io/badge/license-MIT-lightgrey)]()
[![Phase](https://img.shields.io/badge/phases%201--4-COMPLETE-brightgreen)]()

---

## Overview

**Murim Chronicles** transforms CK3 into a Wuxia/Xianxia cultivation world set in historical East Asia. Characters cultivate qi, practice martial techniques, join sects, duel rivals, undergo heavenly tribulations, and navigate the shadowy politics of the Jianghu -- the underground martial world that secretly controls the imperial court.

This mod integrates deeply with CK3's vanilla systems: council positions, wars, marriages, imprisonments, title grants, and vassal management are all influenced by the hidden cultivation world.

---

## Current Status

| Phase | Description | Files | Status |
|-------|-------------|-------|--------|
| **Phase 1** | Core Foundation | 15/15 | COMPLETE |
| **Phase 2** | Grind Loop Systems | 11/11 | COMPLETE |
| **Phase 3** | Advanced Mechanics | 9/9 | COMPLETE |
| **Phase 4** | Wuxia Underground | 9/9 | COMPLETE |
| **Total** | | **50 files** | **100% COMPLETE** |

> **Milestone: All four development phases are now complete with 50 mod files totaling 800,000+ bytes of PDX script.**

---

## Implemented Systems

### Phase 1 -- Core Foundation (Complete)
- **Cultivation System**: Qi Condensation through Nascent Soul realms with variable-based progression
- **Martial Traits**: 50+ traits including prowess techniques, mixed martial arts, and cultivation markers
- **Sect Government**: Celestial government type for martial sects with unique succession
- **Martial Cultures**: Murim-specific cultural traditions and pillars
- **Martial Religions**: Dao cultivation paths as religious frameworks
- **Dynasty Legacies**: Bloodline inheritance and martial legacy tracks
- **Artifacts**: Legendary weapons, technique scrolls, and qi treasures
- **Land Setup**: Asia-specific Murim geographic configuration
- **Schemes**: 15+ cultivation-themed schemes (steal techniques, sabotage cultivation, poison qi, 33,486 bytes)
- **Events**: Cultivation story events, region interactions, combat encounters
- **Character Interactions**: Core martial world interactions (challenge, teach, spar)

### Phase 2 -- Grind Loop Systems (Complete)
- **Script Values**: Cultivation, Jianghu, Sect, Celestial, Combat, and Grind calculation values (80,000+ bytes of formulas)
- **Grind Effects**: Automated cultivation grinding with diminishing returns
- **Grind Triggers**: Conditional checks for grind eligibility and progression
- **Grind Modifiers**: Character modifiers for active cultivation states
- **Grind Opinions**: Opinion modifiers for sect relationships during training
- **Technique On-Actions**: Automated technique learning and mastery events
- **AI Decision On-Actions**: AI-driven cultivation choices based on personality
- **AI Autonomy On-Actions**: NPC autonomous sect joining, technique practice, dueling

### Phase 3 -- Advanced Mechanics (Complete)
- **Cultivation Decisions**: 30+ decisions for realm advancement, meditation, qi refinement (39,561 bytes)
- **Sect Decisions**: 40+ decisions for sect management, recruitment, territory control (47,627 bytes)
- **Technique Decisions**: Practice, master, and innovate martial techniques (10,643 bytes)
- **Condition Triggers**: Comprehensive triggers for cultivation checks, breakthrough readiness, sect eligibility (10,823 bytes)
- **Breakthrough Events**: 40+ events covering Qi Condensation through Nascent Soul breakthroughs, qi deviation, heavenly tribulation, golden/perfect core formation (39,230 bytes)
- **Sect Events**: Sect wars, internal politics, disciple trials, elder councils (18,140 bytes)
- **Duel Events**: Formal martial duels, tournament brackets, death matches, honor challenges (20,614 bytes)
- **Penalty Effects**: Qi deviation cascades, meridian damage, cultivation crippling (12,174 bytes)
- **Penalty Modifiers**: Debuff modifiers for failed breakthroughs, combat injuries, sect punishments (8,673 bytes)

### Phase 4 -- Wuxia Underground Integration (Complete)
- **Jianghu Decisions**: 30+ underground decisions -- shadow broker operations, sect espionage, assassination contracts, trade route manipulation (30,618 bytes)
- **Jianghu Events**: 80+ events covering the entire underground martial world -- sect power plays, imperial court infiltration, hidden master encounters, jianghu faction wars, betrayal cascades, shadow economy (82,032 bytes)
- **Jianghu Underground Traits**: 35 traits across 5 categories -- underground roles, jianghu reputation, imperial-jianghu bridge, sect politics, economic underground (20,606 bytes)
- **Jianghu Triggers**: 60+ scripted triggers across 12 sections -- core jianghu status, shadow broker, sect politics, assassination contracts, spy networks, trade route control, hidden cultivator warfare, imperial exam rigging, puppet governor system, cross-system integration, underground economy, jianghu event conditions (24,545 bytes)
- **Jianghu Effects**: Scripted effects for underground operations -- shadow network expansion, puppet governor installation, trade route seizure, assassination execution, spy cell management (18,815 bytes)
- **Jianghu On-Actions**: Automated underground events -- periodic jianghu power shifts, shadow broker rotations, imperial infiltration cycles, sect espionage triggers, trade war escalations (16,329 bytes)
- **Jianghu Interactions**: Full character interactions for the underground world -- recruit spy, bribe official, challenge shadow broker, negotiate trade routes, issue assassination contracts with complete is_shown/is_valid/on_accept/on_decline/ai_accept blocks (41,082 bytes)
- **Imperial Cultivator Events**: Events bridging the imperial court and cultivation world -- hidden cultivators tipping wars, secret masters advising emperors, cultivation politics in the forbidden city (27,976 bytes)
- **Jianghu Script Values**: Calculation values for underground power, shadow influence, trade control, spy network strength (12,302 bytes)

---

## Key Features

### Cultivation Progression
Characters progress through **6 major realms**: Mortal -> Qi Condensation -> Foundation Establishment -> Core Formation -> Nascent Soul -> Soul Transformation. Each realm has sub-stages with variable-tracked progression. Breakthroughs require specific conditions and risk qi deviation.

### Wuxia Underground (Jianghu)
The hidden martial world operates beneath the imperial court:
- **Sects rig imperial examinations** to place cultivators in government
- **Shadow brokers install puppet governors** across provinces
- **Hidden cultivators secretly tip wars** by supporting one side with martial power
- **Jianghu factions control trade routes** and extract tribute from merchants
- **Assassination contracts** can be issued through the underground network
- **Spy networks** infiltrate rival sects and imperial institutions

### AI Integration
NPCs autonomously:
- Cultivate qi and advance realms based on personality traits
- Join sects aligned with their ethics and ambitions
- Challenge rivals to duels when honor demands
- Participate in jianghu underground operations
- React to breakthroughs, betrayals, and sect politics

### Vanilla CK3 Integration
- Prowess bonuses scale with cultivation realm
- Martial techniques modify combat outcomes
- Sect membership affects vassal opinion
- Cultivation realm influences succession strength
- Underground influence affects council positions
- Shadow networks modify intrigue and diplomacy

---

## Installation

### Requirements
- Crusader Kings 3 version **1.12** or later
- No DLC required (compatible with all DLCs)

### Manual Installation
1. Download or clone this repository
2. Copy the entire mod folder to your CK3 mod directory:
   - **Windows**: `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\`
   - **macOS**: `~/Documents/Paradox Interactive/Crusader Kings III/mod/`
   - **Linux**: `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
3. Copy `murim.mod` to the mod directory root
4. Enable "Murim Chronicles" in the CK3 launcher

### Steam Workshop
*Coming soon after beta release.*

---

## Compatibility

| Mod | Compatible | Notes |
|-----|-----------|-------|
| Vanilla CK3 | Yes | Designed for vanilla + all DLCs |
| Community Flavor Pack | Likely | No known conflicts |
| More Game Rules | Likely | No known conflicts |
| Total Conversion Mods | No | Overrides core systems |

### Known Limitations
- Best experienced with East Asian ruler starts
- Some events reference China-specific geography
- Localization is English-only in current version

---

## File Reference

### Core Files (Phase 1)
| File | Path | Size |
|------|------|------|
| Martial Decisions | common/decisions/00_martial_decisions.txt | 4,806 |
| Martial Traits | common/traits/01_martial_traits.txt | 6,874 |
| Mixed Martial Traits | common/traits/02_mixed_martial_traits.txt | 3,972 |
| Prowess Techniques | common/traits/03_prowess_technique_traits.txt | 13,234 |
| Martial Cultures | common/cultures/01_martial_cultures.txt | 8,339 |
| Martial Religions | common/religions/01_martial_religions.txt | 12,771 |
| Martial Legacies | common/dynasty_legacies/01_martial_legacies.txt | 4,848 |
| Bloodline Inheritance | common/dynasty_legacies/02_bloodline_inheritance.txt | 5,211 |
| Martial Artifacts | common/artifacts/00_martial_artifacts.txt | 7,698 |
| Celestial Governments | common/governments/celestial_governments.txt | 3,710 |
| Asia Murim Setup | common/lands/00_asia_murim_setup.txt | 13,293 |
| Celestial Effects | common/scripted_effects/00_celestial_effects.txt | 3,211 |
| Variable Init | common/scripted_effects/murim_variable_init.txt | 18,516 |
| Character Interactions | common/character_interactions/murim_character_interactions.txt | 11,393 |
| Schemes | common/schemes/murim_schemes.txt | 33,486 |

### Events
| File | Path | Size |
|------|------|------|
| Cultivation Story | events/00_cultivation_story.txt | 9,558 |
| Region Interactions | events/00_region_interactions.txt | 6,173 |
| Cultivation Events | events/murim_cultivation_events.txt | 72,010 |
| Celestial Events | events/murim_celestial_events.txt | 29,804 |
| Combat Events | events/murim_combat_events.txt | 26,755 |
| Grind Events | events/murim_grind_events.txt | 12,296 |
| Interaction Events | events/murim_interaction_events.txt | 11,435 |
| Technique Events | events/murim_technique_events.txt | 12,349 |
| Breakthrough Events | events/murim_breakthrough_events.txt | 39,230 |
| Sect Events | events/murim_sect_events.txt | 18,140 |
| Duel Events | events/murim_duel_events.txt | 20,614 |
| Jianghu Events | events/murim_jianghu_events.txt | 82,032 |
| Imperial Cultivator | events/murim_imperial_cultivator_events.txt | 27,976 |

### Localization
| File | Path | Size |
|------|------|------|
| Core Localization | localization/english/murim_l_english.yml | 10,764 |
| Grind Localization | localization/english/murim_grind_l_english.yml | 18,493 |
| Techniques Localization | localization/english/murim_techniques_l_english.yml | 15,386 |

---

## Roadmap

### Completed
- [x] Phase 1: Core Foundation (15 files)
- [x] Phase 2: Grind Loop Systems (11 files)
- [x] Phase 3: Advanced Mechanics (9 files)
- [x] Phase 4: Wuxia Underground Integration (9 files)

### Planned
- [ ] Phase 5: Localization Expansion (Jianghu, decisions, breakthrough loc keys)
- [ ] Phase 6: GUI/Interface (custom windows for cultivation status, sect management)
- [ ] Phase 7: Balance Pass and Playtesting
- [ ] Phase 8: Steam Workshop Release

---

## Contributing

This mod is under active development. Contributions welcome:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with a clear description

### Coding Standards
- Follow CK3 PDX script conventions
- Use `murim_` prefix for all custom identifiers
- Include comments for complex logic blocks
- Test with CK3 error log before submitting

---

## License

MIT License -- see LICENSE file for details.

---

*Built with determination and qi. The Jianghu remembers.*
