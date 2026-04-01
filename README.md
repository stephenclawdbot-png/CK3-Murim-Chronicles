# CK3 Murim Chronicles

> **A total conversion mod bringing the world of Murim (martial arts cultivation) to Crusader Kings 3**

[![Version](https://img.shields.io/badge/version-0.7.0--alpha-blue)]()
[![CK3](https://img.shields.io/badge/CK3-1.12+-green)]()
[![Files](https://img.shields.io/badge/mod%20files-53-orange)]()
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
| **Total** | | **53 files** | **100% COMPLETE** |

> **v0.7.0 Milestone: Expanded character interaction system from 3 to 8 right-click interactions with full event chains. Interaction events file expanded from 11KB to 41KB. Total mod content exceeds 900KB of PDX script.**

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
- **Character Interactions**: 8 right-click interactions (see below)

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
  - Death cascading effects: when ranked fighter dies, revenge hooks propagate, family members gain vengeance modifiers
  - Combat experience integration: AI fighters track wins/losses, develop trauma or confidence

### Phase 3 -- Advanced Mechanics (Complete)
- **Character Interactions (21,386 bytes)**: 8 right-click interactions:
  1. **Spar** -- Friendly combat training with xp gain and wound risk
  2. **Take Disciple** -- Accept a student with technique inheritance chance
  3. **Request Teaching** -- Seek knowledge from stronger cultivators
  4. **Challenge to Death Match** -- Lethal duel with real death/incapacitation/qi deviation outcomes. Declining causes craven trait and prestige loss. Full prowess+cultivation duel system with critical wins/losses
  5. **Steal Technique** -- Hostile espionage (subtle or forced). Intrigue-based infiltration with discovery risk, rival creation, and sect war escalation. Can learn iron_body, shadow_step, celestial_palm, and more
  6. **Qi Transfer Healing** -- Sacrifice own qi to heal wounded/ill allies. Gentle (safe) or forceful (risky) modes. Healer risks qi deviation; patient gets wounds/deviations cured
  7. **Declare Sect Rivalry** -- Formalize hostile sect relations. Triggers ongoing raid/assassination/diplomacy event chains. Courtier opinion cascading. 5-year cooldown
  8. **Offer Protection** -- Bodyguard contract with monthly payment. Random assassination attempts to defend against. Builds loyalty and generates gold
- **Interaction Events (40,871 bytes)**: Full event chains for all 8 interactions including:
  - Death Match chain (1001-1005): 4-outcome duel with critical/normal win/loss, spectator reactions, decline shame gossip
  - Steal Technique chain (2001-2010): Subtle theft with intrigue checks, bribery option, discovery consequences, forced confrontation, intimidation
  - Qi Transfer Healing (3001): Gentle vs forceful healing with qi deviation risk
  - Sect Rivalry chain (4001, 4010): Declaration response, ongoing raids/assassinations/peace negotiations
  - Protection Contract (5001): Monthly patrol with assassin attack events
- **Combat Events**: Martial duels with prowess-based outcome weighting
- **Duel Events**: Formal duels with combat trauma consequences (20,614 bytes)
- **Celestial Events**: Heavenly tribulations, divine breakthroughs (29,804 bytes)
- **Technique Events**: Martial art discovery and mastery chains (12,349 bytes)

### Phase 4 -- Wuxia Underground (Complete)
- **Jianghu Decisions**: Shadow broker operations, assassination contracts, spy networks (30,618 bytes)
- **Jianghu Events**: 82,032 bytes of underground martial world storylines
- **Underground Traits**: 35 Jianghu traits across 5 categories (20,606 bytes)
- **Jianghu Triggers**: 60+ scripted triggers for underground status checks (24,545 bytes)
- **Jianghu Effects**: Scripted effects for shadow operations (18,815 bytes)
- **Jianghu On-Actions**: Automated underground world events (16,329 bytes)
- **Jianghu Interactions**: 41,082 bytes of underground character interactions
- **Jianghu Values**: Script values for underground economy calculations (12,302 bytes)
- **Jianghu Localization**: Full English localization for underground content (24,978 bytes)

### Martial Ranking System (Complete)
- **Top 50 Martial Artist Rankings**: Hidden rank score = prowess + cultivation weight + technique count + duel wins - losses
- **Ranking Values**: Score calculations and weight formulas (7,996 bytes)
- **Ranking Effects**: Recalculate, add/remove from rankings on death (12,806 bytes)
- **Ranking Triggers**: is_ranked_martial_artist, is_top_50, is_hidden_ranked (8,277 bytes)
- **Ranking On-Actions**: Automated ranking updates and death processing (13,157 bytes)
- **Ranking Events**: Notifications for entering/leaving top 50, champion dethroned (16,745 bytes)
- **Ranking Localization**: Full English localization for ranking UI (14,922 bytes)

---

## File Reference

### Common (Script Logic)
| Path | Size | Description |
|------|------|-------------|
| `common/ai_war_behavior/murim_ai_aggression.txt` | 12,190 | AI war behavior for martial sects |
| `common/artifacts/00_martial_artifacts.txt` | 7,698 | Legendary weapons and qi treasures |
| `common/character_interactions/murim_character_interactions.txt` | 21,386 | 8 right-click interactions |
| `common/character_interactions/murim_jianghu_interactions.txt` | 41,082 | Underground interactions |
| `common/character_modifiers/murim_combat_trauma_modifiers.txt` | 12,715 | Combat trauma modifier effects |
| `common/character_modifiers/murim_grind_modifiers.txt` | 1,225 | Cultivation grind modifiers |
| `common/character_modifiers/murim_penalty_modifiers.txt` | 8,673 | Penalty and debuff modifiers |
| `common/cultures/01_martial_cultures.txt` | 8,339 | Murim cultural traditions |
| `common/decisions/00_martial_decisions.txt` | 4,806 | Base martial decisions |
| `common/decisions/murim_cultivation_decisions.txt` | 39,561 | Cultivation advancement decisions |
| `common/decisions/murim_jianghu_decisions.txt` | 30,618 | Underground operation decisions |
| `common/decisions/murim_sect_decisions.txt` | 47,627 | Sect management decisions |
| `common/decisions/murim_technique_decisions.txt` | 10,643 | Technique learning decisions |
| `common/dynasty_legacies/01_martial_legacies.txt` | 4,848 | Martial dynasty legacies |
| `common/dynasty_legacies/02_bloodline_inheritance.txt` | 5,211 | Bloodline power inheritance |
| `common/governments/celestial_governments.txt` | 3,710 | Sect government types |
| `common/lands/00_asia_murim_setup.txt` | 13,293 | Geographic setup |
| `common/on_actions/murim_ai_autonomy_on_actions.txt` | 42,387 | AI duel/cultivation autonomy |
| `common/on_actions/murim_ai_decision_on_actions.txt` | 11,405 | AI decision triggers |
| `common/on_actions/murim_jianghu_on_actions.txt` | 16,329 | Underground on-actions |
| `common/on_actions/murim_on_actions.txt` | 29,857 | Core cultivation on-actions |
| `common/on_actions/murim_ranking_on_actions.txt` | 13,157 | Ranking system on-actions |
| `common/on_actions/murim_technique_on_actions.txt` | 4,365 | Technique on-actions |
| `common/opinion_modifiers/murim_grind_opinions.txt` | 457 | Grind opinion modifiers |
| `common/religions/01_martial_religions.txt` | 12,771 | Dao cultivation religions |
| `common/schemes/murim_schemes.txt` | 33,486 | Cultivation schemes |
| `common/script_values/murim_celestial_values.txt` | 14,802 | Celestial calculation values |
| `common/script_values/murim_combat_values.txt` | 16,178 | Combat formula values |
| `common/script_values/murim_cultivation_values.txt` | 16,229 | Cultivation progression values |
| `common/script_values/murim_grind_values.txt` | 9,133 | Grind loop values |
| `common/script_values/murim_jianghu_values.txt` | 12,302 | Underground economy values |
| `common/script_values/murim_ranking_values.txt` | 7,996 | Ranking score formulas |
| `common/script_values/murim_sect_values.txt` | 12,561 | Sect management values |
| `common/scripted_effects/00_celestial_effects.txt` | 3,211 | Celestial breakthrough effects |
| `common/scripted_effects/murim_grind_effects.txt` | 9,069 | Grind loop effects |
| `common/scripted_effects/murim_jianghu_effects.txt` | 18,815 | Underground effects |
| `common/scripted_effects/murim_penalty_effects.txt` | 12,174 | Penalty/punishment effects |
| `common/scripted_effects/murim_ranking_effects.txt` | 12,806 | Ranking calculation effects |
| `common/scripted_effects/murim_variable_init.txt` | 18,516 | Variable initialization |
| `common/scripted_triggers/murim_condition_triggers.txt` | 10,823 | Conditional check triggers |
| `common/scripted_triggers/murim_grind_triggers.txt` | 3,041 | Grind eligibility triggers |
| `common/scripted_triggers/murim_jianghu_triggers.txt` | 24,545 | Underground condition triggers |
| `common/scripted_triggers/murim_ranking_triggers.txt` | 8,277 | Ranking status triggers |
| `common/scripted_triggers/murim_technique_triggers.txt` | 10,887 | Technique eligibility triggers |
| `common/traits/01_martial_traits.txt` | 6,874 | Core martial traits |
| `common/traits/02_mixed_martial_traits.txt` | 3,972 | Mixed martial arts traits |
| `common/traits/03_prowess_technique_traits.txt` | 13,234 | Prowess technique traits |
| `common/traits/04_grind_loop_traits.txt` | 9,455 | Grind progression traits |
| `common/traits/05_jianghu_underground_traits.txt` | 20,606 | Underground world traits |
| `common/traits/06_combat_trauma_traits.txt` | 9,866 | Combat trauma traits |

### Events
| Path | Size | Description |
|------|------|-------------|
| `events/00_cultivation_story.txt` | 9,558 | Cultivation narrative events |
| `events/00_region_interactions.txt` | 6,173 | Regional interaction events |
| `events/murim_breakthrough_events.txt` | 39,230 | Cultivation breakthrough chains |
| `events/murim_celestial_events.txt` | 29,804 | Heavenly tribulation events |
| `events/murim_combat_events.txt` | 26,755 | Combat encounter events |
| `events/murim_cultivation_events.txt` | 72,010 | Core cultivation events |
| `events/murim_duel_events.txt` | 20,614 | Formal duel events |
| `events/murim_grind_events.txt` | 12,296 | Grind loop events |
| `events/murim_imperial_cultivator_events.txt` | 27,976 | Imperial court cultivator events |
| `events/murim_interaction_events.txt` | 40,871 | Character interaction event chains |
| `events/murim_jianghu_events.txt` | 82,032 | Underground storyline events |
| `events/murim_ranking_events.txt` | 16,745 | Ranking notification events |
| `events/murim_sect_events.txt` | 18,140 | Sect management events |
| `events/murim_technique_events.txt` | 12,349 | Technique discovery events |

### Localization
| Path | Size | Description |
|------|------|-------------|
| `localization/english/murim_grind_l_english.yml` | 18,493 | Grind system localization |
| `localization/english/murim_jianghu_l_english.yml` | 24,978 | Underground localization |
| `localization/english/murim_l_english.yml` | 10,764 | Core system localization |
| `localization/english/murim_ranking_l_english.yml` | 14,922 | Ranking system localization |
| `localization/english/murim_techniques_l_english.yml` | 15,386 | Technique localization |

### Mod Configuration
| Path | Size | Description |
|------|------|-------------|
| `descriptor.mod` | 187 | Mod descriptor |
| `murim.mod` | 205 | CK3 mod registration |
| `.gitattributes` | 45 | Git configuration |

---

## Installation

1. Clone or download this repository
2. Copy the `CK3-Murim-Chronicles` folder to your CK3 mod directory:
   - **Windows**: `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\`
   - **Linux**: `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
   - **macOS**: `~/Documents/Paradox Interactive/Crusader Kings III/mod/`
3. Copy `murim.mod` to the mod directory root
4. Enable "Murim Chronicles" in the CK3 launcher

---

## Compatibility

- **CK3 Version**: 1.12+ recommended
- **DLC**: No DLC required; Royal Court enhances artifact interactions
- **Save Compatible**: New games recommended for full experience
- **Other Mods**: May conflict with mods that modify traits, governments, or on_actions extensively

---

## Changelog

### v0.7.0-alpha (2026-04-01)
- **Character Interactions Expansion**: Grew from 3 to 8 right-click interactions (11KB to 21KB)
  - Added: Challenge to Death Match, Steal Technique, Qi Transfer Healing, Declare Sect Rivalry, Offer Protection
  - All interactions have full AI logic, trait-weighted decisions, and cross-system integration
- **Interaction Events Overhaul**: Expanded from 11KB to 41KB (3.6x increase)
  - Death Match chain with 4-outcome duel, spectator reactions, shame gossip
  - Steal Technique chain with intrigue/bribery paths, discovery consequences
  - Qi Transfer Healing with gentle/forceful modes and qi deviation risk
  - Sect Rivalry chain with raids, assassinations, peace negotiations
  - Protection Contract with monthly patrol and assassin attack events

### v0.6.0-alpha (2026-04-01)
- **AI Duel System**: 7 AI duel types with personality-weighted decisions (42,387 bytes)
- AI challenges player directly (30% monthly). Quarterly tournaments. Revenge chains 3+ deep
- README updated with comprehensive system documentation

### v0.5.0-alpha (2026-04-01)
- All Phase 2, 3, and 4 target files confirmed complete (29/29)
- Martial Ranking System fully operational
- Total repo content exceeds 850KB of PDX script

---

## Roadmap

### Phase 5 (Planned)
- [ ] Localization expansion for all new interaction events
- [ ] GUI/interface files for cultivation HUD
- [ ] Sound effects and music integration
- [ ] Custom map modes for sect territories
- [ ] Balance pass across all cultivation values
- [ ] Multiplayer testing and compatibility

---

## Contributing

This mod is being developed via automated build loops. To contribute:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with valid CK3 PDX script
4. Ensure all `exists = yes` safety checks are present

---

## License

MIT License -- See LICENSE file for details.
