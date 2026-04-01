# CK3 Murim Chronicles

> **A total conversion mod bringing the world of Murim (martial arts cultivation) to Crusader Kings 3**

[![Version](https://img.shields.io/badge/version-0.8.0--alpha-blue)]()
[![CK3](https://img.shields.io/badge/CK3-1.12+-green)]()
[![Files](https://img.shields.io/badge/mod%20files-55-orange)]()
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
| **Total** | | **55 files** | **100% COMPLETE** |

> **v0.8.0 Milestone: Foundation Hardening Pass -- massively expanded the three weakest files. Opinion modifiers 7->100+ (18.5x), Character modifiers 9->55+ (9.2x), Grind triggers 12->40+ (4.2x). Total mod content now exceeds 950KB of PDX script.**

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
- **Character Interactions**: 8 right-click interactions (spar, take disciple, request teaching, death match, steal technique, qi transfer healing, declare sect rivalry, offer protection)

### Phase 2 -- Grind Loop Systems (Complete)
- **Script Values**: Cultivation, Jianghu, Sect, Celestial, Combat, and Grind calculation values (80,000+ bytes of formulas)
- **Grind Effects**: Automated cultivation grinding with diminishing returns
- **Grind Triggers**: 40+ conditional checks across 8 categories -- cultivation eligibility, duel readiness, technique prerequisites, sect membership, ranking eligibility, jianghu underground, trait safety checks, and cross-system integration (12,779 bytes)
- **Grind Modifiers**: 55+ character modifiers across 9 categories -- cultivation states, duel aftermath, sect activities, technique mastery, ranking tiers, jianghu underground, body tempering, combat trauma, and cross-system integration (11,301 bytes)
- **Grind Opinions**: 100+ opinion modifiers across 10 categories -- duels, cultivation, master-disciple, sects, techniques, ranking, jianghu underground, social dynamics, combat trauma, and cross-system integration (8,442 bytes)
- **Technique On-Actions**: Automated technique learning and mastery events
- **AI Decision On-Actions**: AI-driven cultivation choices based on personality
- **AI Autonomy On-Actions**: Massive AI behavior system (42,387 bytes) including:
  - Monthly cultivation pulse (meditation, body tempering, qi circulation, forbidden study, technique practice)
  - **7 AI Duel Types**: Honor duels, death matches, sect ranking fights, ambush attacks, revenge duels, master vs disciple sparring, breakthrough challenge duels
  - AI challenges the PLAYER directly (30% monthly chance if player has cultivation traits)
  - Quarterly tournament system with sect-hosted background tournaments
  - AI-vs-AI background duels with court notifications to player
  - Personality-weighted decision making (brave/ambitious = aggressive, craven/content = avoidant, intrigue = ambush, honor = formal)
  - Revenge duel chains cascading 3+ events deep
  - Death consequences trigger successor duels
  - Combat experience tracking (variables incremented per duel)

### Phase 3 -- Advanced Mechanics (Complete)
- **Cultivation Decisions**: 39,561 bytes of decisions including advanced breakthroughs, qi circulation, meridian opening
- **Sect Decisions**: 47,627 bytes covering sect founding, management, wars, alliances
- **Technique Decisions**: 10,643 bytes for technique learning, mastery, creation
- **Cultivation Events**: 72,010 bytes of cultivation progression events
- **Breakthrough Events**: 39,230 bytes covering realm transitions and tribulations
- **Celestial Events**: 29,804 bytes of heavenly phenomena and divine encounters
- **Combat Events**: 26,755 bytes of martial combat scenarios
- **Duel Events**: 20,614 bytes of one-on-one duel resolution
- **Condition Triggers**: 10,823 bytes of advanced condition checks
- **Technique Triggers**: 10,887 bytes of technique-specific eligibility checks

### Phase 4 -- Wuxia Underground (Complete)
- **Jianghu Decisions**: 30,618 bytes covering shadow broker operations, underground arena, puppet governors
- **Jianghu Events**: 82,032 bytes (largest file) -- assassination missions, spy networks, trade routes, imperial exam rigging
- **Jianghu Traits**: 20,606 bytes with underground-specific character traits
- **Jianghu Triggers**: 24,545 bytes with 60+ underground condition checks
- **Jianghu Effects**: 18,815 bytes of underground operation scripted effects
- **Jianghu On-Actions**: 16,329 bytes of automated underground world events
- **Jianghu Interactions**: 41,082 bytes of right-click underground interactions
- **Jianghu Values**: 12,302 bytes of underground economy calculations
- **Imperial Cultivator Events**: 27,976 bytes bridging cultivation and imperial politics

### Ranking System (Complete)
- **Ranking Values**: Hidden rank score calculation (prowess + cultivation weight + technique count + duel record)
- **Ranking Effects**: Recalculate ranks, add/remove from rankings, death cleanup
- **Ranking Triggers**: Ranked martial artist checks, top 50 detection, hidden rank verification
- **Ranking Events**: Top 50 notifications, champion dethroned, new entrant, dead fighter removal
- **Ranking On-Actions**: Automated ranking update cycles and AI competition

### Support Systems
- **Combat Trauma**: Modifiers and traits for PTSD, crippling injuries, berserker rage
- **Penalty System**: Effects and modifiers for cultivation failures and forbidden technique costs
- **Variable Initialization**: Comprehensive system to safely initialize all Murim variables
- **Localization**: English localization for grind, jianghu, techniques, and ranking systems (84,543+ bytes across 5 files)

---

## File Reference

| Directory | Files | Total Size |
|-----------|-------|------------|
| `common/traits/` | 6 files | ~64KB |
| `common/decisions/` | 4 files | ~133KB |
| `common/script_values/` | 7 files | ~89KB |
| `common/scripted_effects/` | 6 files | ~75KB |
| `common/scripted_triggers/` | 5 files | ~69KB |
| `common/on_actions/` | 6 files | ~120KB |
| `common/character_interactions/` | 2 files | ~62KB |
| `common/character_modifiers/` | 3 files | ~32KB |
| `common/opinion_modifiers/` | 1 file | ~8KB |
| `common/schemes/` | 1 file | ~33KB |
| `common/artifacts/` | 1 file | ~8KB |
| `common/cultures/` | 1 file | ~8KB |
| `common/religions/` | 1 file | ~13KB |
| `common/governments/` | 1 file | ~4KB |
| `common/dynasty_legacies/` | 2 files | ~10KB |
| `common/lands/` | 1 file | ~13KB |
| `common/ai_war_behavior/` | 1 file | ~12KB |
| `events/` | 13 files | ~414KB |
| `localization/english/` | 5 files | ~85KB |
| **Total** | **55 blob files** | **~950KB+** |

---

## Installation

1. Clone or download this repository
2. Copy the mod folder to your CK3 mod directory:
   - **Windows**: `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\`
   - **macOS**: `~/Documents/Paradox Interactive/Crusader Kings III/mod/`
   - **Linux**: `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
3. Copy `murim.mod` to the mod directory root
4. Enable "Murim Chronicles" in the CK3 launcher

---

## Compatibility

- **CK3 Version**: 1.12+ recommended
- **Save Compatible**: New game recommended for full experience
- **Other Mods**: May conflict with total conversion mods; compatible with most cosmetic/UI mods

---

## Changelog

### v0.8.0-alpha (2026-04-01) -- Foundation Hardening
- **Opinion Modifiers**: Expanded from 7 to 100+ modifiers (457 -> 8,442 bytes, 18.5x increase)
  - 10 sections: duels, cultivation, master-disciple, sects, techniques, ranking, jianghu, social, combat trauma, cross-system
  - Balanced values (-100 to +100 range) with appropriate decay timers
- **Character Modifiers**: Expanded from 9 to 55+ modifiers (1,225 -> 11,301 bytes, 9.2x increase)
  - 9 sections: cultivation states, duel aftermath, sect activities, technique mastery, ranking tiers, jianghu underground, body tempering, combat trauma, cross-system
  - Each modifier affects multiple stats with balanced gameplay impact
- **Grind Triggers**: Expanded from 12 to 40+ triggers (3,041 -> 12,779 bytes, 4.2x increase)
  - 8 sections: cultivation eligibility, duel readiness, technique study, sect membership, ranking eligibility, jianghu underground, trait safety checks, cross-system integration
  - All triggers use exists=yes safety and graceful fallback patterns

### v0.7.0-alpha (2026-04-01) -- Expanded Interactions
- Character interactions expanded from 3 to 8 right-click actions
- Interaction events expanded from 11KB to 41KB with full event chains
- Death Match, Steal Technique, Qi Transfer, Sect Rivalry, Offer Protection interactions added

### v0.6.0-alpha (2026-04-01) -- AI Duel System
- AI autonomy on-actions expanded from 6,624 to 42,387 bytes (6.4x increase)
- 7 AI duel types with personality-weighted decisions
- AI challenges player directly with 30% monthly chance
- Quarterly tournament system
- Revenge duel chains cascading 3+ events deep

### v0.5.0-alpha (2026-04-01) -- Phase 4 Complete
- All 29 Phase 2/3/4 target files completed
- Jianghu underground system fully implemented
- Ranking system with Top 50 martial artist tracking
- Imperial cultivator bridge events

### v0.4.0-alpha (2026-03-31) -- Phase 3 Core
- Advanced cultivation mechanics
- Breakthrough and tribulation event chains
- Comprehensive sect management decisions

### v0.3.0-alpha (2026-03-31) -- Phase 2 Foundation
- Grind loop systems implemented
- AI decision-making framework
- Script values and calculation formulas

---

## Roadmap

- [ ] **Phase 5**: GUI/Interface -- custom windows for cultivation status, sect management, ranking display
- [ ] **Phase 5**: Sound/Music -- cultivation ambience, duel sound effects, breakthrough fanfares  
- [ ] **Phase 5**: Map overlays -- sect territory visualization, qi density heat maps
- [ ] **Phase 6**: Multiplayer balancing and competitive cultivation
- [ ] **Phase 6**: Modular compatibility patches for popular mods
- [ ] **Ongoing**: Expand to 1000+ unique event/interaction variations

---

## License

MIT License -- see LICENSE file for details.

---

*Cultivate your qi. Master your techniques. Dominate the Murim.*
