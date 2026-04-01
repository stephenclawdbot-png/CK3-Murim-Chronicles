# CK3 Murim Chronicles

> **A total conversion mod bringing the world of Murim (martial arts cultivation) to Crusader Kings 3**

[![Version](https://img.shields.io/badge/version-0.6.0--alpha-blue)]()
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

> **Milestone: All four development phases are now complete with 50 mod files totaling 850,000+ bytes of PDX script.**

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
- **AI Autonomy On-Actions**: Massive AI behavior system (42,387 bytes) including:
  - Monthly cultivation pulse (meditation, body tempering, qi circulation, forbidden study, technique practice)
  - **7 AI Duel Types**: Honor duels, death matches, sect ranking fights, ambush attacks, revenge duels, master vs disciple sparring, breakthrough challenge duels
  - AI challenges the PLAYER directly (30% monthly chance if player has cultivation traits)
  - Quarterly tournament system with sect-hosted background tournaments
  - AI-vs-AI background duels with court notifications to player
  - Personality-weighted decision making (brave/ambitious = aggressive, craven/content = avoidant, intrigue = ambush, honor = formal)
  - Revenge duel chains cascading 3+ events deep (family revenge, sect vengeance, demonic sect attraction)
  - Death cascading effects: duel deaths trigger family revenge arcs, sect vengeance hunts, and demonic investigation
  - Yearly AI breakthrough progression through ALL cultivation ranks
  - AI sect joining, betrayal, and closed cultivation cycles
  - Combat experience hooks (battle winners/losers gain cultivation progress)

### Phase 3 -- Advanced Mechanics (Complete)
- **Cultivation Decisions**: 30+ decisions for realm advancement, meditation, qi refinement (39,561 bytes)
- **Sect Decisions**: 40+ decisions for sect management, recruitment, territory control (47,627 bytes)
- **Technique Decisions**: Practice, master, and innovate martial techniques (10,643 bytes)
- **Condition Triggers**: Comprehensive triggers for cultivation checks, breakthrough readiness, sect eligibility (10,823 bytes)
- **Breakthrough Events**: 40+ events covering Qi Condensation through Nascent Soul breakthroughs, qi deviation, heavenly tribulation, golden/perfect core formation (39,230 bytes)
- **Sect Events**: Sect wars, internal politics, disciple trials, elder councils (18,140 bytes)
- **Duel Events**: Formal challenges, technique showcases, death matches, tournament brackets (20,614 bytes)
- **Technique Events**: Technique discovery, mastery progression, innovation (12,349 bytes)
- **Cultivation Events**: 72,010 bytes of cultivation lifecycle events

### Phase 4 -- Wuxia Underground / Jianghu (Complete)
- **Jianghu Decisions**: 30+ decisions for underground operations, shadow broker networks, puppet governor system (30,618 bytes)
- **Jianghu Events**: 82,032 bytes covering assassination contracts, spy networks, trade route control, imperial exam rigging, underground economy
- **Jianghu Traits**: 35 traits across underground roles, jianghu reputation, imperial-jianghu bridge, sect politics, economic underground (20,606 bytes)
- **Jianghu Triggers**: 60+ scripted triggers across 12 categories: core jianghu status, shadow broker, sect politics, assassination, spy networks, trade routes, hidden cultivator warfare, imperial exam rigging, puppet governors, cross-system integration (24,545 bytes)
- **Jianghu Effects**: Scripted effects for underground operations, shadow networks, political manipulation (18,815 bytes)
- **Jianghu On-Actions**: Automated underground world events and responses (16,329 bytes)
- **Jianghu Interactions**: 41,082 bytes of underground character interactions
- **Jianghu Values**: Script values for underground economy, reputation, and influence calculations (12,302 bytes)
- **Jianghu Localization**: 24,978 bytes of English localization for all underground systems

---

## Complete File Reference

### Core Files
| File | Size | Description |
|------|------|-------------|
| `descriptor.mod` | 187b | Mod descriptor |
| `murim.mod` | 205b | Launcher mod file |
| `README.md` | ~13KB | This file |

### Traits (`common/traits/`)
| File | Size | Description |
|------|------|-------------|
| `01_martial_traits.txt` | 6,874b | Core martial cultivation traits |
| `02_mixed_martial_traits.txt` | 3,972b | Hybrid martial arts traits |
| `03_prowess_technique_traits.txt` | 13,234b | Technique mastery traits |
| `04_grind_loop_traits.txt` | 9,455b | Training and grinding traits |
| `05_jianghu_underground_traits.txt` | 20,606b | Underground world traits |

### Script Values (`common/script_values/`)
| File | Size | Description |
|------|------|-------------|
| `murim_cultivation_values.txt` | 16,229b | Cultivation formula values |
| `murim_combat_values.txt` | 16,178b | Combat calculation values |
| `murim_celestial_values.txt` | 14,802b | Celestial realm values |
| `murim_sect_values.txt` | 12,561b | Sect management values |
| `murim_grind_values.txt` | 9,133b | Grind loop values |
| `murim_jianghu_values.txt` | 12,302b | Underground economy values |

### Scripted Effects (`common/scripted_effects/`)
| File | Size | Description |
|------|------|-------------|
| `00_celestial_effects.txt` | 3,211b | Celestial realm effects |
| `murim_variable_init.txt` | 18,516b | Variable initialization |
| `murim_penalty_effects.txt` | 12,174b | Penalty and punishment effects |
| `murim_grind_effects.txt` | 9,069b | Grind loop effects |
| `murim_jianghu_effects.txt` | 18,815b | Underground operation effects |

### Scripted Triggers (`common/scripted_triggers/`)
| File | Size | Description |
|------|------|-------------|
| `murim_condition_triggers.txt` | 10,823b | Cultivation condition checks |
| `murim_grind_triggers.txt` | 3,041b | Grind eligibility triggers |
| `murim_technique_triggers.txt` | 10,887b | Technique requirement triggers |
| `murim_jianghu_triggers.txt` | 24,545b | Underground system triggers |

### Decisions (`common/decisions/`)
| File | Size | Description |
|------|------|-------------|
| `00_martial_decisions.txt` | 4,806b | Core martial decisions |
| `murim_cultivation_decisions.txt` | 39,561b | Cultivation path decisions |
| `murim_sect_decisions.txt` | 47,627b | Sect management decisions |
| `murim_technique_decisions.txt` | 10,643b | Technique decisions |
| `murim_jianghu_decisions.txt` | 30,618b | Underground decisions |

### On-Actions (`common/on_actions/`)
| File | Size | Description |
|------|------|-------------|
| `murim_on_actions.txt` | 29,857b | Core cultivation on-actions |
| `murim_technique_on_actions.txt` | 4,365b | Technique learning hooks |
| `murim_ai_decision_on_actions.txt` | 11,405b | AI decision-making |
| `murim_ai_autonomy_on_actions.txt` | 42,387b | **AI autonomy + 7 duel types + tournaments** |
| `murim_jianghu_on_actions.txt` | 16,329b | Underground on-actions |

### Events (`events/`)
| File | Size | Description |
|------|------|-------------|
| `00_cultivation_story.txt` | 9,558b | Cultivation story events |
| `00_region_interactions.txt` | 6,173b | Region-specific interactions |
| `murim_cultivation_events.txt` | 72,010b | Cultivation lifecycle events |
| `murim_breakthrough_events.txt` | 39,230b | Breakthrough and tribulation events |
| `murim_combat_events.txt` | 26,755b | Combat encounter events |
| `murim_celestial_events.txt` | 29,804b | Celestial realm events |
| `murim_duel_events.txt` | 20,614b | Duel and tournament events |
| `murim_grind_events.txt` | 12,296b | Training grind events |
| `murim_sect_events.txt` | 18,140b | Sect politics events |
| `murim_technique_events.txt` | 12,349b | Technique mastery events |
| `murim_interaction_events.txt` | 11,435b | Interaction response events |
| `murim_imperial_cultivator_events.txt` | 27,976b | Imperial court cultivator events |
| `murim_jianghu_events.txt` | 82,032b | Underground world events |

### Other Files
| File | Size | Description |
|------|------|-------------|
| `common/governments/celestial_governments.txt` | 3,710b | Sect government type |
| `common/cultures/01_martial_cultures.txt` | 8,339b | Martial cultures |
| `common/religions/01_martial_religions.txt` | 12,771b | Cultivation religions |
| `common/dynasty_legacies/01_martial_legacies.txt` | 4,848b | Martial legacies |
| `common/dynasty_legacies/02_bloodline_inheritance.txt` | 5,211b | Bloodline system |
| `common/artifacts/00_martial_artifacts.txt` | 7,698b | Martial artifacts |
| `common/lands/00_asia_murim_setup.txt` | 13,293b | Geographic setup |
| `common/schemes/murim_schemes.txt` | 33,486b | Cultivation schemes |
| `common/ai_war_behavior/murim_ai_aggression.txt` | 12,190b | AI war behavior |
| `common/character_interactions/murim_character_interactions.txt` | 11,393b | Core interactions |
| `common/character_interactions/murim_jianghu_interactions.txt` | 41,082b | Underground interactions |
| `common/character_modifiers/murim_grind_modifiers.txt` | 1,225b | Grind modifiers |
| `common/character_modifiers/murim_penalty_modifiers.txt` | 8,673b | Penalty modifiers |
| `common/opinion_modifiers/murim_grind_opinions.txt` | 457b | Grind opinions |

### Localization (`localization/english/`)
| File | Size | Description |
|------|------|-------------|
| `murim_l_english.yml` | 10,764b | Core English localization |
| `murim_grind_l_english.yml` | 18,493b | Grind system localization |
| `murim_techniques_l_english.yml` | 15,386b | Technique localization |
| `murim_jianghu_l_english.yml` | 24,978b | Underground localization |

---

## Installation

1. Download or clone this repository
2. Copy the entire folder to your CK3 mod directory:
   - **Windows**: `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\`
   - **macOS**: `~/Documents/Paradox Interactive/Crusader Kings III/mod/`
   - **Linux**: `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
3. Enable "Murim Chronicles" in the CK3 launcher
4. Start a new game (recommended) or load an existing save

## Compatibility

- **CK3 Version**: 1.12+ required
- **DLC**: No DLC required; enhanced with Royal Court, Tours & Tournaments
- **Save Compatible**: New features are additive; existing saves should work but a new game is recommended for the full experience
- **Mod Conflicts**: May conflict with mods that modify `on_actions`, trait definitions, or government types extensively

---

## Changelog

### v0.6.0-alpha (2026-04-01)
- **MASSIVE AI Duel System Expansion**: Rewrote `murim_ai_autonomy_on_actions.txt` from 6,624 bytes to 42,387 bytes (6.4x expansion)
- Added 7 autonomous AI duel types: honor duels, death matches, sect ranking fights, ambush attacks, revenge duels, master vs disciple sparring, breakthrough challenge duels
- AI now challenges the PLAYER directly (~30% monthly chance if player has cultivation traits/prowess)
- Quarterly tournament system with sect-hosted background tournaments
- All AI-vs-AI duels generate court notifications so player sees the martial world in action
- Personality-weighted duel decisions (brave = aggressive, craven = avoidant, intrigue = ambush, honor = formal)
- Revenge duel chains cascade 3+ events deep (family revenge -> sect vengeance -> demonic investigation)
- Death cascading: duel kills trigger family revenge arcs, sect vengeance hunts, demonic sect attraction
- On-death hooks for revenge chain propagation across dynasties
- Combat experience hooks: battle winners/losers gain cultivation progress
- Yearly AI breakthrough progression through ALL cultivation ranks with personality weighting
- AI sect joining, betrayal cycles, and closed cultivation seclusion
- All triggers include `exists = yes` checks for load safety and graceful degradation

### v0.5.0-alpha (2026-04-01)
- **Phase 4 COMPLETE**: All 9 Jianghu Underground files implemented
- Full Wuxia underground system: shadow brokers, assassination contracts, spy networks
- Imperial exam rigging, puppet governor system, trade route control
- 35 new Jianghu traits across 5 categories
- 60+ scripted triggers for underground mechanics
- 82,032 bytes of Jianghu events
- 41,082 bytes of underground character interactions
- 24,978 bytes of English localization

### v0.4.0-alpha (2026-03-31)
- **Phase 3 COMPLETE**: All 9 advanced mechanics files
- 40+ breakthrough events with qi deviation and heavenly tribulation
- Sect management with 47,627 bytes of decisions
- Technique mastery system

### v0.3.0-alpha (2026-03-31)
- **Phase 2 COMPLETE**: All 11 grind loop system files
- AI autonomous cultivation and decision making
- Script values for all calculation systems

### v0.2.0-alpha (2026-03-31)
- **Phase 1 COMPLETE**: Core foundation with 15 files
- Basic cultivation, traits, cultures, religions, governments

---

## Roadmap

### Phase 5 (Planned)
- [ ] Visual effects and custom GUI for cultivation status
- [ ] Music and sound effects for cultivation events
- [ ] Map markers for sect territories and sacred grounds
- [ ] Custom 3D models for martial artifacts
- [ ] Extended localization (Chinese, Korean, Japanese)
- [ ] Steam Workshop integration

### Continuous Improvement (Ongoing)
- [x] Load safety: all files interrupt-safe with fallback defaults
- [x] AI cultivator parity: AI walks the same cultivation path as player
- [x] Frequent AI duels: 7 duel types firing commonly with court notifications
- [ ] Interconnected event chains: minimum 3-deep cause-and-effect cascades
- [ ] 500+ unique character interactions across all files
- [ ] Full localization coverage for all new systems

---

## Contributing

This mod is under active automated development. Contributions welcome via pull requests.

## License

MIT License -- see LICENSE file for details.