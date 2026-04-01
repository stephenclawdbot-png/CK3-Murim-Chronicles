# CK3 Murim Chronicles

> **A total conversion mod bringing the world of Murim (martial arts cultivation) to Crusader Kings 3**

[![Version](https://img.shields.io/badge/version-0.9.0--alpha-blue)]()
[![CK3](https://img.shields.io/badge/CK3-1.12+-green)]()
[![Files](https://img.shields.io/badge/mod%20files-56-orange)]()
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
| **Total** | | **56 files** | **100% COMPLETE** |

> **v0.9.0 Milestone: Deep Systems Expansion -- massively expanded Celestial Effects (3KB->31KB, 9.9x) with Five Elements, Yin-Yang Balance, Meridian System, Heavenly Tribulation, and Astral Projection. Expanded Technique On-Actions (4KB->29KB, 6.7x) with inheritance, marriage exchange, degradation, AI sparring, and 15 on_action hooks. Total mod content now exceeds 1MB of PDX script.**

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
- **Technique On-Actions**: 15 on_action hooks (29,462 bytes) including:
  - Yearly technique unlock pulse (Tier 1/2/3 with mastery deepening)
  - Coming-of-age prodigy check with family aptitude inheritance
  - Duel victory breakthrough + combat insight for both winner and loser
  - War victory enlightenment + battlefield technique insight
  - Death technique inheritance (disciple priority, children fallback, legacy manual creation)
  - Marriage technique exchange + dual cultivation technique unlock
  - Monthly practice pulse with Dedicated/Virtuoso/Living Legend milestones
  - Technique degradation from inactivity + aging decline (resisted by high cultivators)
  - AI sparring system (quarterly, court-based, mutual benefit)
  - Secret technique theft on court visits
  - Master-disciple teaching pulse with surpass-master mechanic
  - Tournament technique showcase for courtiers
  - Meditation breakthrough (boosted by Yin-Yang balance and meridians)
  - Near-death enlightenment (classic murim trope)
  - Sect technique library access on title gain
- **AI Decision On-Actions**: AI-driven cultivation choices based on personality
- **AI Autonomy On-Actions**: Massive AI behavior system (42,387 bytes) including:
  - Monthly cultivation pulse for all eligible AI characters
  - 7 AI duel types: honor duels, death matches, sect ranking fights, ambush attacks, revenge duels, master vs disciple sparring, breakthrough challenge duels
  - AI challenges player directly (~30% monthly chance)
  - Quarterly tournament system
  - Revenge chains that cascade 3+ events deep
  - Death cascading hooks for sect succession
  - Combat experience integration with personality-weighted decisions

### Phase 3 -- Advanced Mechanics (Complete)
- **Celestial Effects**: Comprehensive celestial mechanics system (31,723 bytes) with 25+ scripted effects across 10 sections:
  - Celestial Alignment & Beast Cycle (60-year Sexagenary cycle, 4 beasts)
  - Celestial Beast Blessings (Azure Dragon, Vermilion Bird, White Tiger, Black Tortoise)
  - Five Elements System (Wood/Fire/Earth/Metal/Water with generation and destruction cycles)
  - Elemental Mastery progression (Minor Attunement -> Major Attunement -> Transcendence)
  - Yin-Yang Balance (-100 to +100 scale, meditation restoration, deviation warnings)
  - Meridian System (20 channels: 12 primary + 8 extraordinary, milestone rewards)
  - Mandate of Heaven (Empire-tier, vassal acknowledgment, challenge mechanics)
  - Heavenly Tribulation (9-stage player event chain, AI auto-resolve, death risk)
  - Celestial Qi Absorption (element-aligned bonus, conflict penalty)
  - Astral Projection (high-cultivator meditation ability)
  - Yearly Celestial Maintenance (master orchestrator for all subsystems)
  - Celestial Combat Effects (resonance/harmony/dissonance bonuses)
  - Heavenly Punishment (oathbreaker/demonic cultivator consequences)
- **Breakthrough Events**: 39,230 bytes of cultivation breakthrough chains
- **Duel Advanced Events**: 17,994 bytes of advanced duel mechanics
- **Combat Events**: 26,755 bytes of martial combat encounters
- **Imperial Cultivator Events**: 27,976 bytes of court politics meets cultivation
- **Celestial Events**: 29,804 bytes of celestial phenomena and tribulations
- **Penalty Systems**: Cultivation penalties, qi deviation, and consequences (12,174 bytes effects + 8,673 bytes modifiers)
- **Condition Triggers**: 10,823 bytes of prerequisite checks
- **Variable Initialization**: 18,516 bytes of safe variable bootstrapping

### Phase 4 -- Wuxia Underground (Complete)
- **Jianghu Decisions**: 30,618 bytes of underground martial world choices
- **Jianghu Events**: 82,032 bytes (largest file) of underground storylines
- **Jianghu Traits**: 20,606 bytes of underground character archetypes
- **Jianghu Triggers**: 24,545 bytes of underground conditional logic
- **Jianghu Effects**: 18,815 bytes of underground mechanical effects
- **Jianghu On-Actions**: 16,329 bytes of automated underground behaviors
- **Jianghu Interactions**: 41,082 bytes of underground character interactions
- **Jianghu Values**: 12,302 bytes of underground calculation formulas
- **Combat Trauma Modifiers**: 12,715 bytes of PTSD, injury, and recovery mechanics

### Ranking System (Complete)
- **Ranking Values**: Hidden rank score calculation (7,996 bytes)
- **Ranking Effects**: Recalculate, add/remove from rankings (12,806 bytes)
- **Ranking Triggers**: is_ranked, is_top_50, is_hidden_ranked (8,277 bytes)
- **Ranking Events**: Top 50 notifications, champion dethroned, death removal (16,745 bytes)
- **Ranking On-Actions**: Automated ranking updates (13,157 bytes)

---

## File Reference

| Directory | Files | Total Size |
|-----------|-------|------------|
| common/traits/ | 6 | ~64KB |
| common/decisions/ | 4 | ~133KB |
| common/script_values/ | 7 | ~89KB |
| common/scripted_effects/ | 6 | ~104KB |
| common/scripted_triggers/ | 5 | ~67KB |
| common/on_actions/ | 6 | ~127KB |
| common/character_interactions/ | 2 | ~62KB |
| common/character_modifiers/ | 3 | ~33KB |
| common/opinion_modifiers/ | 1 | ~8KB |
| common/schemes/ | 1 | ~33KB |
| common/ai_war_behavior/ | 1 | ~12KB |
| common/artifacts/ | 1 | ~8KB |
| common/cultures/ | 1 | ~8KB |
| common/dynasty_legacies/ | 2 | ~10KB |
| common/governments/ | 1 | ~4KB |
| common/lands/ | 1 | ~13KB |
| common/religions/ | 1 | ~13KB |
| events/ | 14 | ~435KB |
| localization/english/ | 6 | ~106KB |
| **TOTAL** | **56 mod files** | **~1,050KB+** |

---

## Installation

1. Clone or download this repository
2. Copy the mod folder to your CK3 mod directory:
   - **Windows**: `%USERPROFILE%/Documents/Paradox Interactive/Crusader Kings III/mod/`
   - **Linux**: `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
   - **macOS**: `~/Documents/Paradox Interactive/Crusader Kings III/mod/`
3. Copy `murim.mod` to the same mod directory
4. Enable "Murim Chronicles" in the CK3 launcher

---

## Compatibility

- **CK3 Version**: 1.12+ (Wandering Nobles and later)
- **DLC Required**: None (base game compatible)
- **DLC Recommended**: Royal Court (for artifact integration), Tours & Tournaments (for duel enhancements)
- **Save Compatible**: New game recommended for full experience

---

## Changelog

### v0.9.0-alpha (2026-04-01)
- **Celestial Effects Overhaul**: 3,211 -> 31,723 bytes (9.9x expansion)
  - Added Five Elements system with generation/destruction cycles
  - Added Yin-Yang Balance system (-100 to +100 scale)
  - Added Meridian System (20 channels with milestone rewards)
  - Added Heavenly Tribulation (9-stage event chain with death risk)
  - Added Celestial Qi Absorption and Astral Projection
  - Added Heavenly Punishment for oathbreakers
  - All effects now use exists=yes safety checks
- **Technique On-Actions Overhaul**: 4,365 -> 29,462 bytes (6.7x expansion)
  - Added death technique inheritance (disciple/children/legacy manual)
  - Added marriage technique exchange + dual cultivation
  - Added monthly practice pulse with 3 milestone tiers
  - Added technique degradation from inactivity
  - Added AI quarterly sparring system
  - Added secret technique theft on court visits
  - Added master-disciple teaching with surpass-master mechanic
  - Added near-death enlightenment
  - Added sect library access

### v0.8.0-alpha (2026-04-01)
- Foundation Hardening Pass: expanded weakest 3 files
- Opinion modifiers: 7 -> 100+ (18.5x increase)
- Character modifiers: 9 -> 55+ (9.2x increase)
- Grind triggers: 12 -> 40+ (4.2x increase)

### v0.7.0-alpha (2026-04-01)
- Character Interactions expanded to 8 types (21,386 bytes)
- Interaction Events expanded to 40,871 bytes with full event chains
- Death Match, Steal Technique, Qi Transfer, Sect Rivalry, Protection events

### v0.6.0-alpha (2026-04-01)
- AI Duel System massively expanded (42,387 bytes)
- 7 AI duel types with personality-weighted decisions
- AI challenges player directly (~30% monthly)
- Quarterly tournament system
- Revenge chains cascade 3+ events deep

### v0.5.0-alpha (2026-03-31)
- All Phase 2/3/4 files complete (29/29 target files)
- Total repository: 50+ mod files
- README comprehensive overhaul

---

## Roadmap

- [ ] **Phase 5**: Localization expansion (Chinese, Korean, Japanese)
- [ ] **Phase 5**: GUI/interface custom windows for cultivation status
- [ ] **Phase 5**: Custom map markers for sect headquarters
- [ ] **Phase 5**: Music and sound effects for cultivation events
- [ ] **Phase 6**: Multiplayer balancing and testing
- [ ] **Phase 6**: Steam Workshop publication

---

## Contributing

This project is under active automated development. Feel free to open issues for bugs or feature requests.

---

## License

MIT License - See LICENSE for details.
