# CK3 Murim Chronicles

> **A total conversion mod bringing the world of Murim (martial arts cultivation) to Crusader Kings 3**

[![Version](https://img.shields.io/badge/version-0.4.0--alpha-blue)]()
[![CK3](https://img.shields.io/badge/CK3-1.12+-green)]()
[![Files](https://img.shields.io/badge/mod%20files-49-orange)]()
[![License](https://img.shields.io/badge/license-MIT-lightgrey)]()

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
| **Phase 4** | Wuxia Underground | 3/9 | IN PROGRESS |
| **Total** | | **49 files** | **76% complete** |

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
- **Schemes**: 15+ cultivation-themed schemes (steal techniques, sabotage cultivation, poison qi)
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
- **Penalty Modifiers**: Debuff modifiers for failed breakthroughs, damaged cores, suppressed cultivation (8,673 bytes)

### Phase 4 -- Wuxia Underground (In Progress: 3/9 files)
The Wuxia world operates **underground**. The Emperor of China doesn't fully know the extent of cultivator influence. Sects manipulate who gets titles, who passes imperial examinations, who wins battles, and who controls trade -- all through shadow networks.

- **Jianghu Underground Traits** (NEW): 35 traits across 5 categories:
  - *Underground Roles*: Shadow broker, sect spy, imperial informant, black market dealer, hidden master, retired legend, court cultivator (secret), jianghu enforcer
  - *Jianghu Reputation*: Trade route controller, wulin alliance leader, forbidden technique user, qi poisoner, scroll thief, puppet master, examination rigger, tournament host, protection racketeer, smuggler
  - *Imperial-Jianghu Bridge*: Imperial cultivator corps, double agent, cultivator governor, sect-backed general, crackdown survivor, underground railroad operator
  - *Sect Politics*: Sect patriarch, rogue cultivator, sect defector, inner disciple spy, righteous crusader, demonic cultivator
  - *Economic Underground*: Pill refiner, formation master, spirit stone hoarder, intelligence network master, oath breaker

- **Jianghu Decisions** (Complete): Form Underground Sect, Declare Wulin Alliance, Launch Imperial Crackdown, Establish Shadow Court, Control Provincial Appointments, Rig Imperial Examinations, Open Black Market, Commission Assassination, Seek Imperial Patronage (30,618 bytes)

- **Jianghu Events** (Complete): Underground tournament, sect war spilling into imperial politics, spy exposed at court, assassination attempt on emperor, forbidden technique auction, imperial crackdown, wulin alliance summit, trade route dispute, black market raid, secret disciple revealed as prince (82,032 bytes)

#### Phase 4 Remaining (6 files):
- Jianghu Scripted Triggers (underground condition checks)
- Jianghu Scripted Effects (shadow network manipulation)
- Jianghu Character Interactions (25+ underground interactions)
- Jianghu On-Actions (AI underground autonomy)
- Imperial Cultivator Events (emperor vs. cultivator storylines)
- Jianghu Localization (all Phase 4 text strings)

---

## File List (49 files)

<details>
<summary>Click to expand full file list</summary>

```
Root:
  descriptor.mod
  murim.mod
  README.md

common/ai_war_behavior/
  murim_ai_aggression.txt

common/artifacts/
  00_martial_artifacts.txt

common/character_interactions/
  murim_character_interactions.txt

common/character_modifiers/
  murim_grind_modifiers.txt
  murim_penalty_modifiers.txt

common/cultures/
  01_martial_cultures.txt

common/decisions/
  00_martial_decisions.txt
  murim_cultivation_decisions.txt
  murim_jianghu_decisions.txt
  murim_sect_decisions.txt
  murim_technique_decisions.txt

common/dynasty_legacies/
  01_martial_legacies.txt
  02_bloodline_inheritance.txt

common/governments/
  celestial_governments.txt

common/lands/
  00_asia_murim_setup.txt

common/on_actions/
  murim_ai_autonomy_on_actions.txt
  murim_ai_decision_on_actions.txt
  murim_on_actions.txt
  murim_technique_on_actions.txt

common/opinion_modifiers/
  murim_grind_opinions.txt

common/religions/
  01_martial_religions.txt

common/schemes/
  murim_schemes.txt

common/script_values/
  murim_celestial_values.txt
  murim_combat_values.txt
  murim_cultivation_values.txt
  murim_grind_values.txt
  murim_jianghu_values.txt
  murim_sect_values.txt

common/scripted_effects/
  00_celestial_effects.txt
  murim_grind_effects.txt
  murim_penalty_effects.txt
  murim_variable_init.txt

common/scripted_triggers/
  murim_condition_triggers.txt
  murim_grind_triggers.txt
  murim_technique_triggers.txt

common/traits/
  01_martial_traits.txt
  02_mixed_martial_traits.txt
  03_prowess_technique_traits.txt
  04_grind_loop_traits.txt
  05_jianghu_underground_traits.txt

events/
  00_cultivation_story.txt
  00_region_interactions.txt
  murim_breakthrough_events.txt
  murim_celestial_events.txt
  murim_combat_events.txt
  murim_cultivation_events.txt
  murim_duel_events.txt
  murim_grind_events.txt
  murim_interaction_events.txt
  murim_jianghu_events.txt
  murim_sect_events.txt
  murim_technique_events.txt

localization/english/
  murim_grind_l_english.yml
  murim_l_english.yml
  murim_techniques_l_english.yml
```

</details>

---

## Installation

1. Download or clone this repository
2. Copy the entire folder to your CK3 mod directory:
   - **Windows**: `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod\`
   - **Linux**: `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
   - **Mac**: `~/Documents/Paradox Interactive/Crusader Kings III/mod/`
3. Ensure both `murim.mod` and `descriptor.mod` are present
4. Launch CK3 and enable "Murim Chronicles" in the mod launcher
5. Start a new game (save compatibility not guaranteed between versions)

---

## Compatibility

- **CK3 Version**: 1.12+ recommended
- **DLC**: No DLC required. Enhanced experience with Royal Court (artifacts) and Tours & Tournaments (duels)
- **Other Mods**: May conflict with mods that heavily modify traits, governments, or East Asian regions
- **Save Games**: New game recommended when updating between alpha versions

---

## Roadmap

### Completed
- [x] Phase 1: Core cultivation, traits, sects, religions, artifacts, events
- [x] Phase 2: Grind loop systems, script values, AI decision-making
- [x] Phase 3: Advanced decisions, breakthrough events, duels, penalties

### In Progress
- [ ] Phase 4: Wuxia Underground x Vanilla China Integration (3/9 files)
  - [x] Jianghu Underground Traits (35 traits)
  - [x] Jianghu Decisions (9 major decisions)
  - [x] Jianghu Events (10+ event chains)
  - [ ] Jianghu Triggers & Effects
  - [ ] Jianghu Interactions (25+ new interactions)
  - [ ] Jianghu On-Actions (AI underground autonomy)
  - [ ] Imperial Cultivator Events
  - [ ] Phase 4 Localization

### Planned
- [ ] Phase 5: GUI/Interface customization
- [ ] Phase 6: Music and sound effects
- [ ] Phase 7: Custom map overlays for sect territories
- [ ] Phase 8: Multiplayer balancing pass

---

## Design Philosophy

**The Jianghu operates in shadow.** The vanilla CK3 Chinese empire functions normally on the surface -- governors govern, armies march, examinations select officials. But beneath it all, cultivation sects pull strings:

- **Title Assignment**: Sects manipulate who receives imperial appointments
- **Civil Examinations**: Rigged by cultivator influence to place sect allies
- **Battle Outcomes**: Hidden cultivators tip the balance of wars
- **Political Marriages**: Arranged for sect benefit, not just dynasty
- **Trade Routes**: Controlled by underground networks, not just merchants

Every system connects back to CK3's vanilla mechanics. This isn't a separate game bolted on -- it's a shadow layer woven through the existing systems.

---

## Credits

- Built with automated CI/CD pipeline
- CK3 modding documentation: [Paradox Wiki](https://ck3.paradoxwikis.com/)
- Inspired by: Wuxia literature, Korean Murim manhwa, Chinese cultivation novels

---

*Murim Chronicles is an unofficial fan mod and is not affiliated with Paradox Interactive.*
