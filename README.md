# CK3 Murim Chronicles

> **A total conversion mod bringing the world of Murim (martial arts cultivation) to Crusader Kings 3**

[![Version](https://img.shields.io/badge/version-0.9.4--alpha-blue)]()
[![CK3](https://img.shields.io/badge/CK3-1.12+-green)]()
[![Files](https://img.shields.io/badge/mod%20files-70-orange)]()
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
| **Continuous** | Deep Expansion | 26+ | ACTIVE |
| **Total** | | **70 files** | **100% COMPLETE + EXPANDING** |

> **v0.9.4 Milestone: Romance System & Daily Life Expansion.** Added complete romance event system (10 events: dual cultivation proposals, forbidden love across rival sects, soulmate bonds, marriage duels, romantic rivals, sect loyalty vs love dilemmas, kidnapping rescues, cultivation partner betrayal, joint breakthroughs, love triangles). Expanded daily life from 10 to 20 events with advanced encounters (martial scholar, poisoned wine, orphan talent discovery, ancient tomb exploration, bridge guardian challenges, spirit beast hunts, calligraphy martial insights, flood rescue, mysterious night music, retired grandmaster garden). Added comprehensive localization for romance, politics, fate, training, mentor, and daily life events. Total mod content now exceeds 1.4MB of PDX script across 70 files.

---

## Implemented Systems

### Phase 1 -- Core Foundation (Complete)
- **Cultivation System**: Qi Condensation through Nascent Soul realms with variable-based progression
- **Martial Traits**: 90+ traits including prowess techniques, mixed martial arts, body cultivation stages, qi deviation states, martial reputation titles (Sword Saint, Fist Emperor, Heavenly Demon, etc.), bloodline awakening stages, and cultivation markers
- **Sect Government**: 8 distinct government types with unique succession laws and mechanics
- **Martial Cultures**: Murim-specific cultural traditions and pillars
- **Martial Religions**: Dao cultivation paths as religious frameworks
- **Dynasty Legacies**: 6 complete legacy tracks with 5 levels each (30 total unlocks)
- **Bloodline Inheritance**: 12 fully-realized dynasty bloodlines with 3 progression stages each

### Phase 2 -- Grind Loop Systems (Complete)
- **Training Events**: Multi-stage training montages with risk/reward (waterfall meditation, iron body tempering, thousand steps, blindfolded combat, gravity formations)
- **Grind Modifiers**: 80+ modifiers across alchemy, training montage, weapon forging, spirit beast bond, and formation mastery
- **Grind Triggers**: Comprehensive trigger system for all cultivation states
- **Grind Effects**: Scripted effects for cultivation advancement, penalty application, and recovery
- **Grind Values**: Balanced script values for all numerical calculations
- **Opinion Modifiers**: 40+ opinion modifiers for sect relations, master-disciple bonds, and rivalry

### Phase 3 -- Advanced Mechanics (Complete)
- **Duel System**: Honor duels, death matches, ranking fights, tournaments, ambush, revenge chains, master vs disciple, AI-driven challenges
- **Ranking System**: Top 50 martial rankings with yearly updates, ranking duels, hidden talent emergence
- **Ranker Death Events**: World notifications, memorials, hall of legends, power vacuum events, #1 death world-shaking events
- **Celestial Events**: Heavenly tribulations, cosmic alignments, celestial being encounters
- **Combat Trauma**: PTSD-like traits with recovery mechanics, combat flashbacks, and psychological consequences
- **AI Autonomy**: Full AI decision-making for cultivation, dueling, sect management, and technique selection

### Phase 4 -- Wuxia Underground (Complete)
- **Jianghu Events**: 20+ events covering underground tournaments, bounty hunting, mercenary work, black market, poison trade, assassination, information brokering, evil alliance formation
- **Jianghu Interactions**: Challenge to duel, request teaching, offer discipleship, trade techniques, joint cultivation, poison rival, steal technique
- **Jianghu Triggers**: Comprehensive trigger system for underground world states
- **Jianghu Effects**: Scripted effects for all underground operations
- **Jianghu Localization**: Full English localization for all underground content
- **Sect Decisions**: 15+ decisions for sect management, including founding, merging, and dissolving sects

### Continuous Expansion (Active)
- **Romance System** (NEW): 10 interconnected romance events -- dual cultivation, forbidden love across rival sects, soulmate bonds, marriage duels, romantic rivals, sect loyalty vs love, kidnapping rescue, cultivation partner betrayal, joint breakthroughs, love triangles
- **Politics Events**: 10 events -- martial alliance formation, wulin congress, inter-sect diplomacy, marriage alliances, trade negotiations, territory disputes, peace summits, betrayal pacts, war declarations, tribute demands
- **Fate Events**: 10 events -- heavenly tribulation, karmic debt, reincarnation memories, prophecy, chosen one emergence, destiny's fork, ancestral spirit visions, heaven's judgment, cosmic alignment, fate-defying breakthroughs
- **Mentor Events**: 10 events -- finding master, test of character, first lesson, master's dark past, secret technique, master falls ill, final words, legacy, betrayal by fellow disciple, surpassing the master
- **Daily Life Events**: 20 events -- tea house rumors, traveling merchants, street performances, hidden beggars, festivals, wandering masters, night markets, fortune tellers, herb gathering, scholar encounters, poisoned wine, orphan talent, ancient tombs, bridge guardians, spirit beasts, calligraphy insights, floods, mysterious music, retired grandmasters
- **Training Events**: 10 events -- training montage, sparring, waterfall meditation, iron body tempering, thousand steps, blindfolded combat, gravity formation, secret training ground, spirit beast taming, life-and-death training
- **Artifact Events**: 10+ events -- weapon discovery, cursed items, ancient scrolls, alchemy, forging, talismans, treasure hunts, spirit beast cores, formation arrays
- **Technique Events**: Sword arts, palm techniques, body methods, hidden weapon mastery, formation arrays
- **Cultivation Events**: 20+ events -- breakthroughs, qi deviation, meditation, body tempering, meridian opening, foundation, core formation, nascent soul, tribulation
- **Imperial Cultivator Events**: Court cultivation politics, imperial tournament, forbidden city events
- **Mount Hua & Tang Clan**: Faction-specific event chains

---

## File Structure

```
CK3-Murim-Chronicles/
  descriptor.mod
  murim.mod
  README.md
  common/
    ai_war_behavior/
      murim_ai_aggression.txt
    artifacts/
      00_martial_artifacts.txt
    character_interactions/
      murim_character_interactions.txt
      murim_jianghu_interactions.txt
    character_modifiers/
      murim_combat_trauma_modifiers.txt
      murim_grind_modifiers.txt
      murim_penalty_modifiers.txt
    cultures/
      01_martial_cultures.txt
    decisions/
      00_martial_decisions.txt
      murim_cultivation_decisions.txt
      murim_jianghu_decisions.txt
      murim_sect_decisions.txt
      murim_technique_decisions.txt
    dynasty_legacies/
      01_martial_legacies.txt
      02_bloodline_inheritance.txt
    governments/
      celestial_governments.txt
    lands/
      00_asia_murim_setup.txt
    on_actions/
      murim_ai_autonomy_on_actions.txt
      murim_ai_decision_on_actions.txt
      murim_jianghu_on_actions.txt
      murim_on_actions.txt
      murim_ranking_on_actions.txt
      murim_technique_on_actions.txt
    opinion_modifiers/
      murim_grind_opinions.txt
    religions/
      01_martial_religions.txt
    schemes/
      murim_schemes.txt
    script_values/
      murim_celestial_values.txt
      murim_combat_values.txt
      murim_cultivation_values.txt
      murim_grind_values.txt
      murim_injury_chance_values.txt
      murim_jianghu_values.txt
      murim_ranking_values.txt
      murim_sect_values.txt
    scripted_effects/
      00_celestial_effects.txt
      murim_grind_effects.txt
      murim_jianghu_effects.txt
      murim_penalty_effects.txt
      murim_ranking_effects.txt
      murim_variable_init.txt
    scripted_triggers/
      murim_condition_triggers.txt
      murim_grind_triggers.txt
      murim_jianghu_triggers.txt
      murim_ranking_triggers.txt
      murim_technique_triggers.txt
    traits/
      01_martial_traits.txt
      02_mixed_martial_traits.txt
      03_prowess_technique_traits.txt
      04_grind_loop_traits.txt
      05_jianghu_underground_traits.txt
      06_combat_trauma_traits.txt
      murim_global_martial_traits.txt
  events/
    00_cultivation_story.txt
    00_region_interactions.txt
    murim_artifact_events.txt
    murim_breakthrough_events.txt
    murim_celestial_events.txt
    murim_combat_events.txt
    murim_cultivation_events.txt
    murim_daily_life_events.txt
    murim_daily_life_advanced_events.txt
    murim_duel_events.txt
    murim_duel_advanced_events.txt
    murim_fate_events.txt
    murim_global_martial_events.txt
    murim_grind_events.txt
    murim_grind_advanced_events.txt
    murim_imperial_cultivator_events.txt
    murim_interaction_events.txt
    murim_jianghu_events.txt
    murim_mentor_events.txt
    murim_mount_hua_events.txt
    murim_politics_events.txt
    murim_ranker_death_events.txt
    murim_ranking_events.txt
    murim_romance_events.txt
    murim_sect_events.txt
    murim_tang_clan_events.txt
    murim_technique_events.txt
    murim_training_events.txt
  localization/
    english/
      murim_advanced_l_english.yml
      murim_grind_l_english.yml
      murim_jianghu_l_english.yml
      murim_l_english.yml
      murim_ranking_l_english.yml
      murim_romance_l_english.yml
      murim_techniques_l_english.yml
```

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

- **200+ unique events** across cultivation, combat, romance, politics, daily life, and supernatural systems
- **90+ martial arts traits** with interconnected progression
- **80+ character modifiers** for cultivation states, combat effects, and training
- **50+ scripted triggers** for complex condition checking
- **40+ opinion modifiers** for nuanced relationship dynamics
- **8 unique government types** with custom succession laws
- **12 dynasty bloodlines** with 3 progression stages each
- **7 localization files** with full English support
- **Full AI autonomy** -- NPCs cultivate, duel, join sects, and make decisions independently
- **Deep interconnection** -- every system feeds into every other system

---

## License

MIT License -- free to use, modify, and distribute.
