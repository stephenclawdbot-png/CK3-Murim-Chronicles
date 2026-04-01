# CK3 Murim Chronicles

> **A total conversion mod bringing the world of Murim (martial arts cultivation) to Crusader Kings 3**

[![Version](https://img.shields.io/badge/version-0.9.2--alpha-blue)]()
[![CK3](https://img.shields.io/badge/CK3-1.12+-green)]()
[![Files](https://img.shields.io/badge/mod%20files-67-orange)]()
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
| **Continuous** | Deep Expansion | Ongoing | ACTIVE |
| **Total** | | **67 files** | **100% COMPLETE + EXPANDING** |

> **v0.9.2 Milestone: Decision & Legacy Deep Expansion.** Massively expanded martial decisions from 9 basic to 21 full-featured decisions (4.8KB->37.2KB, 7.7x) across 6 categories: Cultivation Path, Alchemy & Pills, Techniques, Body Tempering, Social/Jianghu, and Heavenly Tribulation. All decisions have proper PDX syntax, AI weights, exists=yes safety guards, and interconnected variable tracking. Dynasty legacies rewritten from 3 broken tracks to 6 complete legacy tracks with 5 levels each (30 total unlocks, 4.8KB->22.7KB, 4.7x): Azure Sword, Blood Moon Demonic, Iron Body, Celestial Qi, Shadow Arts, and Pill Master Alchemy. Total mod content now exceeds 1.1MB of PDX script.

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
- **Dynasty Legacies**: 6 complete legacy tracks with 5 levels each (30 total unlocks):
  - *Azure Sword Legacy* -- Sword Dao mastery from Foundation to Transcendence
  - *Blood Moon Demonic Legacy* -- Dark cultivation path from Demonic Seed to Asura Ascension
  - *Iron Body Legacy* -- Body tempering from Iron Skin to Diamond Body Perfection
  - *Celestial Qi Legacy* -- Heavenly qi mastery from Qi Sense to Mandate of Heaven
  - *Shadow Arts Legacy* -- Stealth/assassination mastery from Shadow Step to Void Shadow Sovereign
  - *Pill Master Alchemy Legacy* -- Alchemy mastery from Herb Gathering to Immortality Pill
- **Artifacts**: Legendary weapons, technique scrolls, and qi treasures
- **Land Setup**: Asia-specific Murim geographic configuration
- **Schemes**: 15+ cultivation-themed schemes (steal techniques, sabotage cultivation, poison qi, 33,486 bytes)
- **Events**: Cultivation story events, region interactions, combat encounters
- **Character Interactions**: 8 right-click interactions (spar, take disciple, request teaching, death match, steal technique, qi transfer healing, declare sect rivalry, offer protection)

### Phase 2 -- Grind Loop Systems (Complete)
- **Script Values**: Cultivation, Jianghu, Sect, Celestial, Combat, Ranking, and Grind calculation values (90,000+ bytes of formulas)
- **Grind Effects**: Cultivation progress, breakthrough calculations, and reward distribution
- **Grind Triggers**: 40+ triggers across 8 sections for cultivation gates, combat checks, and sect requirements
- **Grind Modifiers**: 55+ character modifiers across 9 sections for cultivation states, duel aftermath, sect activities
- **Opinion Modifiers**: 100+ opinion modifiers across 10 sections for duels, master-disciple bonds, sect relations
- **Grind Events**: Two tiers of grind events (basic + advanced) for cultivation loops
- **Martial Decisions**: 21 full-featured decisions across 6 categories:
  - *Cultivation Path* -- Abandon Mortal Coil, Seclude for Cultivation, Awaken Dormant Potential
  - *Sect Leadership* -- Challenge Sect Master, Found Martial Sect, Recruit Close Disciple
  - *Alchemy & Pills* -- Refine Cultivation Pill, Establish Pill Furnace
  - *Techniques* -- Comprehend Advanced Technique, Study Enemy Technique
  - *Body Tempering* -- Open Meridians, Body Tempering Ritual
  - *Social/Jianghu* -- Host Grand Tournament, Declare Bounty, Recruit Wandering Expert, Seek Ancient Ruins, Activate Bloodline, Establish Trading Post
  - *Dark Path* -- Enter Demon Path, Purge Demonic Qi
  - *Ultimate* -- Challenge Heavenly Tribulation (20% transcendence, 20% death)
- **Additional Decisions**: 70+ cultivation decisions, jianghu decisions, sect decisions, technique decisions (128,000+ bytes)
- **On-Actions**: Yearly cultivation ticks, monthly AI decisions, technique learning hooks

### Phase 3 -- Advanced Mechanics (Complete)
- **Celestial Events**: Heavenly phenomena, tribulations, celestial alignment (29,804 bytes)
- **Celestial Effects**: 25+ effects across 10 systems (Five Elements, Yin-Yang, Meridians, Mandate of Heaven, 31,723 bytes)
- **Breakthrough Events**: 39,230 bytes of multi-stage cultivation breakthrough chains
- **Combat Events**: 26,755 bytes of martial combat with real consequences
- **Duel System**: Basic + Advanced duels (38,608 bytes combined) with incapable, craven, wounded, trauma outcomes
- **Imperial Cultivator Events**: 27,976 bytes of court cultivation politics
- **Artifact Events**: 32,268 bytes of legendary weapon discoveries and technique scroll events
- **Combat Trauma System**: Full PTSD/trauma system with modifiers and traits (22,581 bytes combined)
- **Penalty System**: Cultivation failure consequences with effects and modifiers (20,847 bytes combined)

### Phase 4 -- Wuxia Underground (Complete)
- **Jianghu Events**: 82,032 bytes -- the largest single event file, covering underground martial world
- **Jianghu Interactions**: 41,082 bytes of right-click Jianghu character interactions
- **Jianghu Decisions**: 30,618 bytes of underground world decisions
- **Jianghu Effects**: 18,815 bytes of Jianghu scripted effects
- **Jianghu Triggers**: 24,545 bytes of Jianghu condition checks
- **Jianghu On-Actions**: 16,329 bytes of underground event hooks
- **Jianghu Values**: 12,302 bytes of underground economy calculations
- **Sect Events**: 18,140 bytes of sect politics and internal power struggles
- **Sect Decisions**: 47,627 bytes of sect management and politics

### Advanced Systems (Continuous Expansion)
- **Top 50 Martial Ranking System**: Hidden rank scores for all martial artists, public Top 50 leaderboard, death cascading, player notifications (58,000+ bytes across values/effects/triggers/events/on-actions/localization)
- **AI Autonomy System**: 42,387 bytes of AI-driven cultivation, dueling, and sect management with 7 AI duel types, quarterly tournaments, revenge chains
- **AI Decision System**: 11,405 bytes of AI cultivation decision-making
- **Technique System**: On-actions (29,462 bytes), events (12,349 bytes), triggers (10,887 bytes), decisions (10,643 bytes)
- **Interaction Events**: 40,871 bytes of event chains for all 8 character interactions
- **AI War Behavior**: 12,190 bytes of Murim-flavored AI aggression patterns
- **Localization**: 6 English localization files (106,000+ bytes) covering all systems

---

## File Structure

```
CK3-Murim-Chronicles/
|-- README.md
|-- descriptor.mod / murim.mod
|-- common/
|   |-- ai_war_behavior/murim_ai_aggression.txt
|   |-- artifacts/00_martial_artifacts.txt
|   |-- character_interactions/
|   |   |-- murim_character_interactions.txt (21,386b - 8 interactions)
|   |   |-- murim_jianghu_interactions.txt (41,082b)
|   |-- character_modifiers/
|   |   |-- murim_combat_trauma_modifiers.txt (12,715b)
|   |   |-- murim_grind_modifiers.txt (11,301b - 55+ modifiers)
|   |   |-- murim_penalty_modifiers.txt (8,673b)
|   |-- cultures/01_martial_cultures.txt
|   |-- decisions/
|   |   |-- 00_martial_decisions.txt (37,158b - 21 decisions)
|   |   |-- murim_cultivation_decisions.txt (39,561b)
|   |   |-- murim_jianghu_decisions.txt (30,618b)
|   |   |-- murim_sect_decisions.txt (47,627b)
|   |   |-- murim_technique_decisions.txt (10,643b)
|   |-- dynasty_legacies/
|   |   |-- 01_martial_legacies.txt (22,696b - 6 tracks, 30 unlocks)
|   |   |-- 02_bloodline_inheritance.txt (5,211b)
|   |-- governments/celestial_governments.txt (17,865b - 8 types)
|   |-- lands/00_asia_murim_setup.txt (13,293b)
|   |-- on_actions/
|   |   |-- murim_ai_autonomy_on_actions.txt (42,387b)
|   |   |-- murim_ai_decision_on_actions.txt (11,405b)
|   |   |-- murim_jianghu_on_actions.txt (16,329b)
|   |   |-- murim_on_actions.txt (29,857b)
|   |   |-- murim_ranking_on_actions.txt (13,157b)
|   |   |-- murim_technique_on_actions.txt (29,462b)
|   |-- opinion_modifiers/murim_grind_opinions.txt (8,442b - 100+ opinions)
|   |-- religions/01_martial_religions.txt (12,771b)
|   |-- schemes/murim_schemes.txt (33,486b)
|   |-- script_values/ (7 files, 89,201b total)
|   |-- scripted_effects/ (6 files, 103,103b total)
|   |-- scripted_triggers/ (5 files, 67,311b total)
|   |-- traits/ (6 files, 82,320b total)
|-- events/ (16 files, 487,000+ bytes total)
|   |-- murim_cultivation_events.txt (72,010b - largest cultivation file)
|   |-- murim_jianghu_events.txt (82,032b - largest overall event file)
|   |-- murim_interaction_events.txt (40,871b)
|   |-- murim_breakthrough_events.txt (39,230b)
|   |-- murim_artifact_events.txt (32,268b)
|   |-- murim_celestial_events.txt (29,804b)
|   |-- murim_imperial_cultivator_events.txt (27,976b)
|   |-- murim_combat_events.txt (26,755b)
|   |-- murim_duel_events.txt (20,614b)
|   |-- murim_grind_advanced_events.txt (20,629b)
|   |-- murim_sect_events.txt (18,140b)
|   |-- murim_duel_advanced_events.txt (17,994b)
|   |-- murim_ranking_events.txt (16,745b)
|   |-- murim_technique_events.txt (12,349b)
|   |-- murim_grind_events.txt (12,296b)
|   |-- 00_cultivation_story.txt (9,558b)
|   |-- 00_region_interactions.txt (6,173b)
|-- localization/english/ (6 files, 106,612b total)
```

---

## Total Content Summary

| Category | Files | Bytes | Key Metric |
|----------|-------|-------|------------|
| Decisions | 5 | 165,607 | 91+ decisions |
| Events | 16 | 487,000+ | 200+ event chains |
| On-Actions | 6 | 142,597 | 50+ hooks |
| Script Values | 7 | 89,201 | 500+ formulas |
| Scripted Effects | 6 | 103,103 | 100+ effects |
| Scripted Triggers | 5 | 67,311 | 80+ triggers |
| Traits | 6 | 82,320 | 90+ traits |
| Interactions | 2 | 62,468 | 8+ interactions |
| Schemes | 1 | 33,486 | 15+ schemes |
| Legacies | 2 | 27,907 | 30 dynasty unlocks |
| Other | 11 | ~100,000 | Govts, cultures, etc. |
| **TOTAL** | **67** | **~1.1MB** | **Full Murim world** |

---

## Installation

1. Clone or download this repository
2. Copy the `CK3-Murim-Chronicles` folder to your CK3 mod directory:
   - **Windows**: `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\`
   - **Linux**: `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
   - **macOS**: `~/Documents/Paradox Interactive/Crusader Kings III/mod/`
3. Copy `murim.mod` to the same mod directory
4. Enable "Murim Chronicles" in the CK3 launcher

---

## Changelog

### v0.9.2-alpha (2026-04-01)
- **Martial Decisions Deep Expansion**: 9 -> 21 decisions (4.8KB -> 37.2KB, 7.7x increase)
  - Added: Open Meridians, Body Tempering Ritual, Establish Pill Furnace, Study Enemy Technique, Host Grand Tournament, Declare Jianghu Bounty, Recruit Wandering Expert, Seek Ancient Ruins, Activate Bloodline Power, Awaken Dormant Potential, Establish Trading Post, Purge Demonic Qi
  - All decisions have proper AI weights, exists=yes safety checks, variable tracking
- **Dynasty Legacy Complete Rewrite**: 3 broken tracks -> 6 proper tracks with 5 levels each (30 unlocks)
  - New tracks: Azure Sword, Blood Moon Demonic, Iron Body, Celestial Qi, Shadow Arts, Pill Master Alchemy
  - Fixed all syntax errors from previous version (invalid `stage_age`, broken `add Martial_Prowess`)

### v0.9.1-alpha (2026-04-01)
- Government & Trait Deep Expansion
- 3 -> 8 government types, 11 -> 45+ mixed martial traits

### v0.9.0-alpha (2026-04-01)
- Foundation Hardening Pass: opinions (18.5x), modifiers (9.2x), triggers (4.2x)
- Character Interactions: 3 -> 8 interactions, full event chains
- AI Duel System: 7 duel types, quarterly tournaments, revenge chains

### v0.8.0-alpha (2026-03-31)
- Phase 4 Jianghu Underground complete
- Ranking system with Top 50 leaderboard
- AI autonomy deep expansion

### v0.7.0-alpha (2026-03-31)
- Phase 3 Advanced Mechanics complete
- Celestial system, breakthrough events, combat trauma

### Pre-v0.7.0
- Phases 1-2 foundation and grind loop systems

---

## Design Philosophy

1. **Interconnected Systems**: Every system references and feeds into others. Cultivation affects dueling, dueling affects ranking, ranking affects sect politics, sect politics affects cultivation access.

2. **AI Parity**: AI characters walk the same cultivation path as the player. They challenge each other to duels, pursue breakthroughs, compete for rankings, and form master-disciple bonds.

3. **Real Consequences**: Duels can result in death, incapacitation, craven traits, PTSD, and permanent cultivation damage. Failed breakthroughs cause qi deviation. Heavenly tribulations have a 20% death chance.

4. **Safety First**: All events use `exists = yes` checks before referencing variables/traits. Graceful degradation ensures no crashes from missing data. All files are interrupt-safe.

5. **Scale**: 1.1MB+ of PDX script, 200+ event chains, 90+ decisions, 90+ traits, 30 dynasty unlocks, 8 government types, 100+ opinion modifiers -- a complete Murim world.

---

## License

MIT License - See LICENSE file for details.
