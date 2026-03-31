# The Murim Chronicles — CK3 Mod

**All Under Heaven: The Way of the Martial Sage**

A Crusader Kings 3 mod that layers a complete wuxia/xianxia martial arts system onto the vanilla game map. Noble houses cultivate internal energy, master divine techniques, and wage war for control of the Murim — the martial world beneath heaven.

> **Design Philosophy:** Same map, same countries, new mechanics. Every vanilla title, province, and character remains intact. Murim Chronicles adds cultivation, sects, and jianghu systems as an overlay — not a total conversion of geography or political boundaries.

---

## Table of Contents

- [Features](#features)
- [Variable System](#variable-system)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Compatibility](#compatibility)
- [Known Issues](#known-issues)
- [Roadmap](#roadmap)
- [Credits](#credits)

---

## Features

### Cultivation System
Characters progress through a 7-tier cultivation ladder with XP-based advancement:

| Realm | Trait Key | Prowess | Health | Lifespan | Special |
|-------|-----------|---------|--------|----------|---------|
| Qi Refinement | `murim_outer_qi` | +2 | +0.5 | — | Can learn techniques |
| Foundation | `murim_qi_gathering` | +5 | +1 | — | Martial +2 |
| Core Formation | `murim_foundation` | +10 | +2 | — | Dread +5 |
| Nascent Soul | `murim_golden_core` | +20 | +4 | +50 | Dread +15 |
| Void | `murim_nascent_soul` | +40 | +8 | +100 | Culture opinion +20 |
| Great Vehicle | `murim_spirit_severing` | +80 | +15 | +200 | Enemy attrition |
| Heavenly Tribulation | `murim_heavenly_tribulation` | +150 | +30 | +500 | Immortal |

- **XP Gain** scales with learning, cultivation traits, meditation, body tempering, and era modifiers
- **Breakthrough Checks** — monthly rolls gated by XP thresholds, trait bonuses, and qi deviation risk
- **Qi Deviation** — failed breakthroughs can cripple or kill; risk increases at higher realms
- **Dual-Path Tension** — practicing both orthodox and demonic cultivation multiplies deviation risk
- **Meridian System** — flow efficiency affects XP rate and technique power
- **Era Modifiers** — Golden Ages boost cultivation speed; Decline Eras punish it
- **Body Constitution** — rare birth traits (Pure Yang Body, Pure Yin Body, Heavenly Spirit Body) grant qi capacity and cultivation bonuses

### Trait System
Eight distinct trait groups with 28 individual traits across martial disciplines:

| Group | Traits | Focus |
|-------|--------|-------|
| Cultivation Realm | 7 tiers | Core power progression |
| Sword Aptitude | 5 tiers (Seed → Immortal) | Sword mastery + knight effectiveness |
| Body Cultivation | 4 tiers (Iron Skin → Golden Body) | Durability + health + enemy attrition |
| Demonic Aptitude | 3 tiers | Prowess + intrigue at stress cost |
| Alchemy | 3 tiers | Learning + health + development |
| Genius/Crippled | 3 special | Heaven-Defying Genius, Crippled Meridian, Secret Manual Holder |
| Body Constitution | 3 rare | Pure Yang, Pure Yin, Heavenly Spirit Body |
| Mixed Martial | 7 hybrid + 4 seasonal | Multi-stat combinations + celestial alignment |

All trait keys use the `murim_` prefix convention for consistency with script values.

### Jianghu Standing
A 0–100 reputation system governing a character's place in the martial world:

- **Standing Gains** from winning duels, hosting tournaments, defending the weak, generous sect donations
- **Standing Losses** from dishonorable kills, breaking oaths, associating with demonic cultivators
- **Wulin Alliance Elections** — high-standing characters compete for Alliance Leader; weighted by standing, cultivation rank, sect power, and renown
- **Face Mechanics** — losing face triggers opinion penalties; restoring face requires public acts
- **Righteous Crusade** — at standing 80+, characters can call the jianghu to war against demonic threats
- **Wandering Hero** reputation track for unaffiliated cultivators

### Sect System
Sects are landless hidden titles with their own power dynamics:

- **Composite Power Score** (0–100) calculated from member count, average cultivation, treasury, and territory
- **Hidden Levy** — sects maintain secret armies; size and quality scale with power score
- **Recruitment Pool** — monthly disciple generation based on sect prestige and local development
- **Sect Master Authority** — internal governance score affecting doctrine enforcement and schism risk
- **Orthodox/Demonic Alignment** — sliding scale from -100 (fully demonic) to +100 (fully orthodox)
- **Internal Challenges** — disciples can challenge masters for leadership via formal duels
- **Treasury** — income from tithes, alchemy sales, spirit stone mines; expenses for training, equipment, formations

### Combat & Techniques
CK3's prowess system extended with cultivation-based amplifiers:

- **6 Combat Styles:** Iron Fist, Flowing Water, Shadow Step, Mountain Stance, Thousand Cuts, Void Palm — each scaling off different stats
- **Technique Tiers:** Minor (qi cost 5) → Major (15) → Ultimate (35) → Forbidden (40), each with mastery requirements
- **Weapon Affinity** — 7 weapon types (sword, saber, spear, fist, palm, whip, hidden weapons) with 0–10 mastery granting up to +15 prowess
- **Duel System** — effective prowess = base prowess + cultivation bonus + technique + weapon affinity + combat style + qi reserves; rank gap of 3+ tiers grants overwhelming advantage
- **Qi Reserves** — 0–100 scale; max capacity scales with cultivation rank; Golden Core+ gets 1.5x multiplier
- **Sparring XP** — training with higher-ranked opponents yields bonus cultivation XP; sect training grounds add further bonuses
- **Martial Manuals** — artifact study grants monthly cultivation XP; 3 quality tiers with increasing study time

### Celestial Integration
Hooks into All Under Heaven's imperial systems:

- **60-Year Celestial Cycle** — Azure Dragon (0–15), Vermilion Bird (16–30), White Tiger (31–45), Black Tortoise (46–59) phases rotate orthodox/unorthodox favor
- **Orthodox Mandate Aura** — orthodox cultivation strengthens the Mandate of Heaven
- **Demonic Mandate Drain** — demonic cultivation erodes imperial legitimacy
- **Ministry Infiltration** — sects can infiltrate the Six Ministries; detection risk scales with infiltration depth
- **Imperial Examinations (Martial Track)** — cultivators compete in state-sponsored martial exams
- **Shadow Emperor** — a hidden demonic cultivator can secretly control the throne
- **Celestial Registry** — tracks all cultivators known to the imperial court
- **Dynastic Cycle** — era transitions (Golden Age, Stability, Decline, Collapse) affect all cultivation and sect mechanics

### Three Martial Paths
Every character and sect follows one of three philosophical alignments:

1. **Orthodox Sects** (Righteous Dao) — public techniques, ancestor worship, Mandate alignment
2. **Demonic Cults** (Heretical Dao) — forbidden arts, blood sacrifice, shadow governance
3. **Unaffiliated Wanderers** (Free Dao) — mixed heritage, unique fusions, no sect loyalty

### Three Government Types
Custom government structures for the martial world:

| Government | Holdings | Key Modifiers | Flavor |
|-----------|----------|---------------|--------|
| Orthodox Sect | Castle, City, Church | +prestige, +piety, +domain, +vassal limit, -dread | Structured hierarchy, righteous reputation |
| Unorthodox Sect | Castle, City | +intrigue, +martial, +prowess, +dread, -tyranny | Fear-based rule, demonic cultivation bonuses |
| Free Cultivator | Castle, City, Church | +prowess, +health, -stress, small domain/vassal | Personal freedom, solo cultivation focus |

### Martial Houses
Every dynasty possesses a namesake technique:

- **House Character** determines martial path (sword, palm, fist, internal, movement)
- **Martial Soul** manifestation: Azure Dragon, White Tiger, Vermilion Bird, Black Tortoise, Qilin, Phoenix
- **Dynasty Legacies** — 100+ martial legacies passed through bloodlines
- **Technique Inheritance** — secret manuals passed from master to heir

### Territory — The Murim
Vanilla map regions gain cultivation overlays across 4 concentric zones:

| Zone | Duchies | Cultivation Speed | Special |
|------|---------|------------------|---------|
| **Heartland** (Zhongyuan) | Kaifeng, Luoyang, Xiangyang, Nanjing, Hangzhou, Chengdu, Jiankang, Yangzhou | +25% | Sect influence +20%, highest martial density |
| **Outer Marches** | Taiyuan, Datong, Youzhou, Qingzhou, Dengzhou, Changsha, Fuzhou, Guangzhou, Lanzhou, Liangzhou | +10% | Herb discovery +20% |
| **Frontier** | Liaoyang, Shangjing, Xining, Lhasa, Thang Long, Dali, Kaesong, Pyongyang | -5% | Ancient ruins +30%, herb discovery +35% |
| **Wilderness** | Karakorum, Ordu-Baliq, Kashgar, Khotan, Kucha, Pagan | -15% | Spirit beasts +40%, ancient ruins +50% |

**5 Isolated Cultivation Zones** with unique modifiers:
- Wudang Mountain Retreat (d_xiangyang) — +40% internal cultivation
- Shaolin Temple Grounds (d_luoyang) — +40% body tempering
- Emei Peak Sanctuary (d_chengdu) — +35% sword cultivation
- Kunlun Forbidden Peaks (d_xining) — +50% cultivation speed (with qi deviation risk)
- Dongting Lake Depths (d_changsha) — +40% water techniques

**8 Sect Headquarters** across orthodox, demonic, and independent factions.

### 14 Playable Cultures
Organized by alignment across 4 culture groups:

**Orthodox:** Azure Dragon Sect, White Tiger Palace, Vermilion Bird Clan, Black Tortoise School
**Demonic:** Blood Moon Cult, Bone Demon Sect, Yin-Yang Cult
**Wanderers:** Wandering Blades, Mountain Hermits, Eastern Pirates
**Regional/Beast Clans:** White Tiger Clan (Mongol heritage), Azure Dragon Tribe (Korean), Vermilion Bird Nest (Vietnamese), Black Tortoise Clan (Tibetan)

### 4 Religions with 11 Faiths
- **Divine Martial Sect** — Orthodox Righteous Dao (3 faiths: Orthodox Way, Scholarly Path, Ascetic Way)
- **Demonic Cultivation Sect** — Heretical Dao (3 faiths: Blood Path, Bone Demon Way, Yin-Yang Path)
- **Unbound Martial Way** — Free Dao (2 faiths: Wandering Sword, Hermit Path)
- **Beast Path Cultivation** — Primal beast spirits (2 faiths: Wolf Spirit Path, Dragon Beast Path)

Each religion has custom virtues/sins, holy sites mapped to real CK3 provinces, and holy order names.

### Decisions & Interactions
Three major decision files covering cultivation, jianghu, and sect gameplay:

- **Cultivation Decisions** — meditation retreats, breakthrough attempts, body tempering, pill refinement, technique practice
- **Jianghu Decisions** — duel challenges, tournament hosting, alliance petitions, face recovery, bounty placement
- **Sect Decisions** — sect founding, disciple recruitment, treasury management, alignment shifts, sect wars

### Schemes
Custom schemes for the martial world: assassination via poison techniques, sect infiltration, technique theft, disciple poaching, and demonic corruption.

### Events
Over 200KB of scripted events across 6 event files:

- **Cultivation Events** (72KB) — breakthrough attempts, qi deviation, meditation visions, realm advancement
- **Jianghu Events** (82KB) — duels, tournaments, alliance politics, wandering encounters, face mechanics
- **Celestial Events** (30KB) — mandate shifts, ministry infiltration, imperial examinations, dynasty cycle transitions
- **Combat Events** (27KB) — technique duels, sparring outcomes, weapon mastery, near-death breakthroughs
- **Cultivation Story** (10KB) — narrative cultivation journey events
- **Region Interactions** (6KB) — zone-specific encounters and region flavor

### AI Behavior
Custom AI war behavior with aggression modifiers based on cultivation rank, sect alignment, and territorial zone.

### On-Actions
Comprehensive on_action hooks (30KB) wiring the variable system to game events: monthly cultivation pulse, birth trait assignment, death cleanup, sect master succession, breakthrough triggers, and more.

---

## Variable System

The mod uses an extensive scripted variable system (6 files, ~90KB) to track all mechanical state:

| File | Scope | What It Tracks |
|------|-------|---------------|
| `murim_cultivation_values.txt` | Character | XP, rank thresholds, breakthrough odds, qi deviation, era scaling, meridian flow |
| `murim_jianghu_values.txt` | Character | Standing, duel honor, face, Wulin election weights, wandering hero rep |
| `murim_celestial_values.txt` | Realm | Mandate aura, ministry infiltration, exam scores, Shadow Emperor, dynastic cycle |
| `murim_sect_values.txt` | Sect (Title) | Power score, levy, recruitment, authority, treasury, alignment |
| `murim_combat_values.txt` | Character | Prowess modifiers, combat styles, qi reserves, technique mastery, weapon affinity |
| `murim_variable_init.txt` | Effect | Character init, sect master init, monthly update loop, death cleanup |

### Initialization Flow
1. Character receives `murim_initiated` flag → `murim_init_character_variables` fires
2. All cultivation, combat, standing, and qi variables set to safe defaults
3. Sect masters get additional authority, treasury, and alignment variables
4. Monthly pulse updates XP, standing decay, qi recovery, face, alignment drift, and treasury
5. Breakthrough and tempering checks run on the monthly cycle
6. Death triggers `murim_cleanup_dead_character` to release variable memory

---

## File Structure

```
CK3-Murim-Chronicles/
├── .gitattributes
├── README.md
├── descriptor.mod
├── murim.mod
│
├── common/
│   ├── ai_war_behavior/
│   │   └── murim_ai_aggression.txt
│   ├── artifacts/
│   │   └── 00_martial_artifacts.txt
│   ├── cultures/
│   │   └── 01_martial_cultures.txt
│   ├── decisions/
│   │   ├── 00_martial_decisions.txt
│   │   ├── murim_cultivation_decisions.txt
│   │   ├── murim_jianghu_decisions.txt
│   │   └── murim_sect_decisions.txt
│   ├── dynasty_legacies/
│   │   ├── 01_martial_legacies.txt
│   │   └── 02_bloodline_inheritance.txt
│   ├── governments/
│   │   └── celestial_governments.txt
│   ├── lands/
│   │   └── 00_asia_murim_setup.txt
│   ├── on_actions/
│   │   └── murim_on_actions.txt
│   ├── religions/
│   │   └── 01_martial_religions.txt
│   ├── schemes/
│   │   └── murim_schemes.txt
│   ├── script_values/
│   │   ├── murim_celestial_values.txt
│   │   ├── murim_combat_values.txt
│   │   ├── murim_cultivation_values.txt
│   │   ├── murim_jianghu_values.txt
│   │   └── murim_sect_values.txt
│   ├── scripted_effects/
│   │   ├── 00_celestial_effects.txt
│   │   └── murim_variable_init.txt
│   └── traits/
│       ├── 01_martial_traits.txt
│       └── 02_mixed_martial_traits.txt
│
├── events/
│   ├── 00_cultivation_story.txt
│   ├── 00_region_interactions.txt
│   ├── murim_celestial_events.txt
│   ├── murim_combat_events.txt
│   ├── murim_cultivation_events.txt
│   └── murim_jianghu_events.txt
│
└── localization/
    └── english/
        └── murim_l_english.yml
```

**29 content files** across **17 directories** — approximately **500KB** of mod content.

---

## Installation

1. Download ZIP or clone the repository
2. Extract to `Documents/Paradox Interactive/Crusader Kings III/mod/`
3. Ensure the folder is named `murim` (must match `murim.mod` path)
4. Enable "The Murim Chronicles" in the CK3 launcher
5. Start a new game — cultivation mechanics activate automatically for characters in the mod's culture/religion scope

**Note:** Not compatible with Ironman mode (custom scripted mechanics).

---

## Compatibility

| Requirement | Status |
|------------|--------|
| CK3 Version | 1.18.x (All Under Heaven patch) |
| All Under Heaven DLC | Recommended but not required (celestial features need it) |
| Vanilla Map | Uses the unmodified vanilla map — no new provinces or title changes |
| Vanilla Countries | All vanilla realms, titles, and characters remain intact |
| Ironman | Not compatible (custom script values and effects) |
| Multiplayer | Untested — all players must have identical mod version |
| Other Mods | Compatible with cosmetic mods; may conflict with mods that overwrite cultures, religions, or governments |

### What This Mod Does NOT Change
- No new map provinces or terrain
- No removed or renamed vanilla titles
- No changes to vanilla character history
- No overwritten vanilla cultures (adds new ones alongside)
- No overwritten vanilla religions (adds new ones alongside)

---

## Known Issues

### Resolved (v0.3.0)
All critical syntax bugs from the initial release have been fixed:

- ~~Fictional province keys~~ — All land setup uses real vanilla CK3 duchy title keys
- ~~Culture file syntax errors~~ — Proper newlines and valid CK3 culture format
- ~~Non-standard government properties~~ — Rewritten with valid government_type syntax
- ~~Invalid religion syntax~~ — Proper religion/faith/doctrine hierarchy
- ~~Culture type fields~~ — Uses traditions instead of invalid type properties
- ~~Land setup block names~~ — Uses proper CK3-compatible region/modifier patterns
- ~~.mod version mismatch~~ — Both murim.mod and descriptor.mod target 1.18.*
- ~~Missing descriptor.mod~~ — Added
- ~~Empty icon references~~ — Religions use named icon keys
- ~~Trait naming mismatch~~ — All traits now use `murim_` prefix, aligned with combat script values

### Remaining

1. **No Custom GFX** — No `.gfx` files, GUI elements, or portrait modifiers. Traits and religions display default or missing icons in-game. Planned for Phase 4.

2. **Localization Coverage** — Single localization file (~11KB). Many trait descriptions, event texts, and tooltip strings may display raw keys until localization is expanded.

3. **Holy Site Validation** — Religion holy sites reference CK3 province keys (luoyang, kaifeng, etc.) that need verification against the exact vanilla title database for the 1.18 map.

---

## Roadmap

### Phase 1 — Syntax Fixes ✓ Complete
- [x] Fix all culture file newline/syntax errors
- [x] Remap fictional province IDs to vanilla CK3 title keys
- [x] Rewrite government types using valid CK3 government format
- [x] Rewrite religion definitions using proper religion/faith/doctrine hierarchy
- [x] Add `descriptor.mod` file
- [x] Fix culture `type` fields → use traditions instead
- [x] Align trait names with `murim_` prefix convention

### Phase 2 — Core Mechanics (Current Priority)
- [ ] Wire script values to on_actions (monthly pulse, birth, death)
- [ ] Implement cultivation breakthrough event chain
- [ ] Implement qi deviation event chain
- [ ] Create sect creation/joining decisions
- [ ] Build duel challenge interaction

### Phase 3 — Content
- [ ] 200+ cultivation story events
- [ ] Wulin Alliance election event chain
- [ ] Imperial martial examination events
- [ ] Shadow Emperor conspiracy chain
- [ ] Sect war casus belli

### Phase 4 — Polish
- [ ] Custom GFX for traits, religions, and artifacts
- [ ] GUI overlay for cultivation status
- [ ] Portrait modifiers for cultivation realms
- [ ] Sound effects for breakthroughs and techniques
- [ ] Steam Workshop publication

---

## Mod Scale

- **29 content files** across 17 directories
- **~500KB** of mod content
- **~90KB** in script values alone (6 variable system files)
- **~230KB** in events (6 event files)
- **~120KB** in decisions and schemes (4 files)
- **14 cultures**, **4 religions** (11 faiths), **3 government types**
- **7 cultivation realms** with full XP/breakthrough/deviation mechanics
- **28 martial traits** across 8 trait groups + 11 mixed/seasonal traits
- **6 combat styles** with technique trees
- **7 weapon types** with affinity mastery
- Fully compatible with vanilla CK3 map and All Under Heaven

---

## Credits

- **Engine:** Paradox Interactive — Crusader Kings 3
- **DLC Integration:** All Under Heaven (Paradox Interactive)
- **Inspiration:** Wuxia/Xianxia literature, Korean manhwa, Chinese cultivation novels
- **Created:** 2026
