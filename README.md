# CK3 Murim Chronicles

> **A total conversion mod bringing the world of Murim (martial arts cultivation) to Crusader Kings 3**

[![Version](https://img.shields.io/badge/version-0.9.1--alpha-blue)]()
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

> **v0.9.1 Milestone: Government & Trait Deep Expansion.** Expanded government types from 3 to 8 (3.7KB->17.9KB, 4.8x) with Hidden Valley Sect, Murim Alliance, Imperial Cultivation Court, Demonic Cult, and Wandering Sword Pavilion. Expanded mixed martial traits from 11 to 45+ (4KB->22.3KB, 5.6x) across 8 new categories: Dual-Element Fusion, Body Cultivation Stages, Qi Deviation States, Martial Reputation Titles, Bloodline Awakening, and Cross-System Synergy. Total mod content now exceeds 1.05MB of PDX script.

---

## Implemented Systems

### Phase 1 -- Core Foundation (Complete)
- **Cultivation System**: Qi Condensation through Nascent Soul realms with variable-based progression
- **Martial Traits**: 90+ traits including prowess techniques, mixed martial arts, body cultivation stages, qi deviation states, martial reputation titles (Sword Saint, Fist Emperor, Heavenly Demon, etc.), bloodline awakening stages, and cultivation markers
- **Sect Government**: 8 distinct government types:
  - *Orthodox Sect* -- Righteous hierarchy with elder council, virtue-based succession
  - *Unorthodox Sect* -- Fear-based rule with blood oath succession, shadow council
  - *Free Cultivator* -- Independent wanderer with personal freedom, no sect obligations
  - *Hidden Valley Sect* -- Isolationist secret knowledge hoarders, massive learning bonuses
  - *Murim Alliance* -- Coalition of sects with rotating leadership and joint defense
  - *Imperial Cultivation Court* -- State-sponsored cultivation with bureaucratic ranks
  - *Demonic Cult* -- Sacrifice-based dark sect with corruption and rapid power growth
  - *Wandering Sword Pavilion* -- Mercenary-style reputation-driven organization
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
  - Yearly technique unlock pulse (Tier 1/2/3 with mastery)
  - Prodigy discovery system
  - Duel breakthrough revelations
  - War enlightenment epiphanies
  - Death inheritance (master -> disciple technique transfer)
  - Marriage technique exchange between sects
  - Monthly practice pulse with degradation
  - AI sparring and teaching automation
  - Technique theft detection and consequences
  - Forbidden technique temptation system
  - Body tempering synergy
  - Cross-system breakthrough chains

### Phase 3 -- Advanced Mechanics (Complete)
- **Celestial Effects**: 25+ scripted effects across 10 systems (31,723 bytes):
  - Celestial Alignment with seasonal bonuses
  - Five Elements generation and destruction cycles
  - Yin-Yang Balance system (-100 to +100 scale)
  - Meridian System with 20 channels
  - Mandate of Heaven political legitimacy
  - Heavenly Tribulation 9-stage survival
  - Celestial Qi Absorption from environment
  - Astral Projection reconnaissance
  - Yearly Maintenance auto-cultivation
  - Combat Effects and Heavenly Punishment
- **Ranking System**: Top 50 Martial Artist rankings with hidden scores, death cascading, and player notifications
- **Condition Triggers**: Advanced prerequisite checks for all cultivation actions
- **Combat Values**: Detailed duel and battle calculations
- **Penalty System**: Cultivation failure consequences and recovery paths

### Phase 4 -- Wuxia Underground (Complete)
- **Jianghu Events**: 82,032 bytes of underground martial world content
- **Jianghu Interactions**: 41,082 bytes of character interactions (bounty hunting, information trading, underworld politics)
- **Jianghu Triggers**: 24,545 bytes of conditional checks for underground activities
- **Jianghu Effects**: 18,815 bytes of scripted effects for black market, assassination contracts, etc.
- **Jianghu On-Actions**: 16,329 bytes of automated underground world events
- **Jianghu Decisions**: 30,618 bytes of player choices in the shadow world
- **AI Autonomy**: 42,387 bytes of AI behavior -- 7 duel types, monthly player challenges (~30%), quarterly tournaments, revenge chains, personality-weighted decisions
- **AI Decision Making**: 11,405 bytes of AI cultivation path automation
- **Combat Trauma**: Full trauma system with PTSD, battle scars, crippling injuries, and psychological consequences

---

## Key Features

### Trait Categories (90+ unique traits)
| Category | Count | Description |
|----------|-------|-------------|
| Mixed Martial Skills | 7 | Dual-skill combinations (Shadow Blade, Iron Strategist, etc.) |
| Celestial Practitioner | 4 | Seasonal alignment traits |
| Dual-Element Fusion | 6 | Transcendent element combinations (Taiji Master, Primordial Awakened) |
| Body Cultivation | 5 | Progressive stages (Iron Skin -> Vajra Immortal Body) |
| Qi Deviation States | 5 | Cultivation failure consequences with increasing severity |
| Martial Reputation | 8 | Legendary titles (Sword Saint, Fist Emperor, Heavenly Demon, etc.) |
| Bloodline Awakening | 5 | Dynasty-tied ancestral power stages |
| Cross-System Synergy | 5 | Multi-system mastery (Pill-Dao Master, Formation Battle Sage) |
| Prowess Techniques | 13+ | Sword, fist, palm, spear, body technique trees |
| Jianghu Underground | 20+ | Shadow world reputation and role traits |
| Combat Trauma | 9+ | Battle scars, PTSD, crippling injuries |
| Cultivation Markers | 9+ | Qi stages from condensation to void |

### Government Types (8 total)
| Government | Domain | Vassal | Key Bonus |
|------------|--------|--------|-----------|
| Orthodox Sect | 2 | 12 | Learning +3, Piety +0.5/mo |
| Unorthodox Sect | 4 | 6 | Prowess +4, Dread +25 |
| Free Cultivator | 1 | 3 | Health +0.5, XP +10% |
| Hidden Valley | 2 | 5 | Learning +5, XP +20%, Defender +5 |
| Murim Alliance | 3 | 20 | Diplomacy +5, Vassal Opinion +15 |
| Imperial Court | 5 | 15 | Stewardship +3, Tax +15% |
| Demonic Cult | 2 | 4 | Prowess +6, XP +25%, Dread +40 |
| Wandering Sword | 2 | 8 | Prowess +5, Knight Eff. +25% |

---

## Installation

1. Clone or download this repository
2. Copy to your CK3 mod directory:
   - **Windows**: `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\`
   - **Linux**: `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
   - **macOS**: `~/Documents/Paradox Interactive/Crusader Kings III/mod/`
3. Enable "Murim Chronicles" in the CK3 launcher

---

## Changelog

### v0.9.1-alpha (2026-04-01)
- **Government Expansion**: 3 -> 8 government types (3.7KB -> 17.9KB, 4.8x)
  - NEW: Hidden Valley Sect (isolationist, secret knowledge)
  - NEW: Murim Alliance (coalition, rotating leadership)
  - NEW: Imperial Cultivation Court (bureaucratic, state-sponsored)
  - NEW: Demonic Cult (sacrifice, corruption, rapid power)
  - NEW: Wandering Sword Pavilion (mercenary, reputation-driven)
- **Trait Expansion**: 11 -> 45+ mixed martial traits (4KB -> 22.3KB, 5.6x)
  - NEW: Dual-Element Fusion (6 traits)
  - NEW: Body Cultivation Stages (5 progressive stages)
  - NEW: Qi Deviation States (5 severity levels)
  - NEW: Martial Reputation Titles (8 legendary titles)
  - NEW: Bloodline Awakening (5 progressive stages)
  - NEW: Cross-System Synergy (5 polymath traits)

### v0.9.0-alpha (2026-04-01)
- Celestial Effects expanded 9.9x (3KB -> 31KB) with Five Elements, Yin-Yang, Meridian System, Heavenly Tribulation, Astral Projection
- Technique On-Actions expanded 6.7x (4KB -> 29KB) with 15 on_action hooks

### v0.8.0-alpha (2026-04-01)
- Foundation Hardening: opinions 18.5x, modifiers 9.2x, triggers 4.2x expansion
- Character Interactions expanded to 8 types with full event chains
- Interaction Events expanded 3.6x with Death Match, Steal Technique, Qi Transfer, Sect Rivalry, Protection Contract chains

### v0.7.0-alpha (2026-03-31)
- AI Duel System: 7 duel types, monthly player challenges, quarterly tournaments, revenge chains
- 42,387 bytes of AI autonomy scripting

### v0.6.0-alpha and earlier
- Core systems, grind loops, advanced mechanics, jianghu underground

---

## File Structure

```
CK3-Murim-Chronicles/
  common/
    ai_war_behavior/       # AI martial aggression (12KB)
    artifacts/             # Legendary weapons & scrolls (7.7KB)
    character_interactions/ # 8+ right-click interactions (62KB)
    character_modifiers/   # Combat trauma, grind, penalty mods (33KB)
    cultures/              # Martial cultures (8.3KB)
    decisions/             # 5 decision files (133KB)
    dynasty_legacies/      # Bloodline inheritance (10KB)
    governments/           # 8 government types (17.9KB)
    lands/                 # Asia Murim setup (13.3KB)
    on_actions/            # 6 on_action files (142KB)
    opinion_modifiers/     # 100+ opinion mods (8.4KB)
    religions/             # Dao cultivation paths (12.8KB)
    schemes/               # 15+ cultivation schemes (33.5KB)
    script_values/         # 7 value calculation files (89KB)
    scripted_effects/      # 6 effect files (103KB)
    scripted_triggers/     # 5 trigger files (67KB)
    traits/                # 6 trait files (86KB)
  events/                  # 15 event files (453KB)
  localization/english/    # 6 localization files (106KB)
```

---

## Contributing

This mod is under active development. Contributions welcome via pull requests.

## License

MIT License -- see LICENSE file for details.
