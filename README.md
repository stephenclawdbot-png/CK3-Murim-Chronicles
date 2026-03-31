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
- [Known Issues & Bugs](#known-issues--bugs)
- [Roadmap](#roadmap)
- [Credits](#credits)

---

## Features

### Cultivation System
Characters progress through a full cultivation ladder with XP-based advancement:

| Realm | XP Threshold | Lifespan Bonus | Prowess Bonus |
|-------|-------------|----------------|---------------|
| Qi Refinement | 0 | +0 | +2 |
| Foundation | 100 | +5 | +5 |
| Core Formation | 250 | +15 | +10 |
| Nascent Soul | 500 | +30 | +18 |
| Void Tribulation | 1000 | +50 | +30 |
| Great Vehicle | 2500 | +100 | +50 |
| Heavenly Tribulation | 5000 | +200 | +80 |

- **XP Gain** scales with learning, cultivation traits, meditation, body tempering, and era modifiers
- **Breakthrough Checks** — monthly rolls gated by XP thresholds, trait bonuses, and qi deviation risk
- **Qi Deviation** — failed breakthroughs can cripple or kill; risk increases at higher realms
- **Dual-Path Tension** — practicing both orthodox and demonic cultivation multiplies deviation risk
- **Meridian System** — flow efficiency affects XP rate and technique power
- **Era Modifiers** — Golden Ages boost cultivation speed; Decline Eras punish it

### Jianghu Standing
A 0-100 reputation system governing a character's place in the martial world:

- **Standing Gains** from winning duels, hosting tournaments, defending the weak, generous sect donations
- **Standing Losses** from dishonorable kills, breaking oaths, associating with demonic cultivators
- **Wulin Alliance Elections** — high-standing characters compete for Alliance Leader; weighted by standing, cultivation rank, sect power, and renown
- **Face Mechanics** — losing face triggers opinion penalties; restoring face requires public acts
- **Righteous Crusade** — at standing 80+, characters can call the jianghu to war against demonic threats
- **Wandering Hero** reputation track for unaffiliated cultivators

### Sect System
Sects are landless hidden titles with their own power dynamics:

- **Composite Power Score** (0-100) calculated from member count, average cultivation, treasury, and territory
- **Hidden Levy** — sects maintain secret armies; size and quality scale with power score
- **Recruitment Pool** — monthly disciple generation based on sect prestige and local development
- **Sect Master Authority** — internal governance score affecting doctrine enforcement and schism risk
- **Orthodox/Demonic Alignment** — sliding scale from -100 (fully demonic) to +100 (fully orthodox)
- **Internal Challenges** — disciples can challenge masters for leadership via formal duels
- **Treasury** — income from tithes, alchemy sales, spirit stone mines; expenses for training, equipment, formations

### Combat & Techniques
CK3's prowess system extended with cultivation-based amplifiers:

- **6 Combat Styles:** Sword, Saber, Fist, Palm, Internal, Movement — each with unique bonuses
- **Technique Tiers:** Minor → Major → Ultimate → Forbidden, each with qi costs and mastery requirements
- **Weapon Affinity** — characters develop bonds with specific weapons over time
- **Duel System** — cultivation rank gap directly modifies duel outcomes; a Core Formation cultivator dominates Qi Refinement
- **Qi Reserves** — combat techniques drain qi; overuse causes exhaustion penalties
- **Sparring XP** — training with higher-ranked opponents yields bonus cultivation XP

### Celestial Integration
Hooks into All Under Heaven's imperial systems:

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

### Martial Houses
Every dynasty possesses a namesake technique:

- **House Character** determines martial path (sword, palm, fist, internal, movement)
- **Martial Soul** manifestation: Azure Dragon, White Tiger, Vermilion Bird, Black Tortoise, Qilin, Phoenix
- **Dynasty Legacies** — 100+ martial legacies passed through bloodlines
- **Technique Inheritance** — secret manuals passed from master to heir

### Territory — The Murim
Vanilla map regions gain cultivation overlays:

- **Central Plains** (China heartland) — Orthodox sect capitals, ancestral temples, highest martial density
- **Outer Marches** (Korea, Japan, Southern China) — Mixed sects, blade tournaments, duel culture
- **Frontier** (Manchuria, Vietnam, Tibet) — Beast clans, mountain hermits, moderate development
- **Wilderness** (Steppes, Siberia, SE Asia) — Demonic cults, forbidden grounds, sparse but powerful cultivators
- **Isolated Zones** (Kunlun, Penglai) — Immortal hermit enclaves, immune to war

### 14 Playable Cultures
Organized by alignment:

**Orthodox:** Azure Dragon Sect, White Tiger Palace, Vermilion Bird Clan, Black Tortoise School
**Demonic:** Blood Moon Cult, Bone Demon Sect, Yin-Yang Cult
**Wanderers:** Wandering Blades, Mountain Hermits, Eastern Pirates
**Beast Clans:** White Tiger Clan, Azure Dragon Tribe, Vermilion Bird Nest, Black Tortoise Clan

### 4 Religions
- **Divine Martial Sect** — Orthodox Righteous Dao with ancestor worship and holy sites
- **Demonic Cultivation Sect** — Heretical Dao with blood sacrifice and necromancy doctrines
- **Unbound Martial Way** — Free Dao for wanderers, hermits, and pirates
- **Beast Path Cultivation** — Primal beast spirit worship with six animal faiths

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
├── murim.mod                              # Mod descriptor
├── README.md
├── common/
│   ├── artifacts/
│   │   └── 00_martial_artifacts.txt       # Sect treasures, ancient weapons, manuals
│   ├── cultures/
│   │   └── 01_martial_cultures.txt        # 14 martial cultures with traditions
│   ├── decisions/
│   │   └── 00_martial_decisions.txt       # Cultivation, sect, and duel decisions
│   ├── dynasty_legacies/
│   │   ├── 01_martial_legacies.txt        # Martial dynasty legacy trees
│   │   └── 02_bloodline_inheritance.txt   # Bloodline technique inheritance
│   ├── governments/
│   │   └── celestial_governments.txt      # Orthodox, Unorthodox, Sect governments
│   ├── lands/
│   │   └── 00_asia_murim_setup.txt        # Region development tiers & sect HQs
│   ├── religions/
│   │   └── 01_martial_religions.txt       # 4 martial religions with doctrines
│   ├── script_values/
│   │   ├── murim_cultivation_values.txt   # Cultivation XP, breakthroughs, qi deviation
│   │   ├── murim_jianghu_values.txt       # Jianghu standing, duels, Wulin Alliance
│   │   ├── murim_celestial_values.txt     # Mandate, ministries, examinations
│   │   ├── murim_sect_values.txt          # Sect power, levy, treasury, alignment
│   │   └── murim_combat_values.txt        # Prowess, techniques, combat styles
│   ├── scripted_effects/
│   │   ├── 00_celestial_effects.txt       # Celestial event effects
│   │   └── murim_variable_init.txt        # Variable init, monthly update, cleanup
│   └── traits/
│       ├── 01_martial_traits.txt          # Cultivation realm traits, martial talents
│       └── 02_mixed_martial_traits.txt    # Hybrid path traits, cursed states
├── events/
│   ├── 00_cultivation_story.txt           # Cultivation narrative events
│   └── 00_region_interactions.txt         # Region-based encounter events
└── localization/
    └── english/
        └── murim_l_english.yml            # All English localization strings
```

**22 files** across **15 directories** — approximately **165KB** of mod content.

---

## Installation

1. Download ZIP or clone the repository
2. Extract to `Documents/Paradox Interactive/Crusader Kings III/mod/`
3. Ensure the folder is named `CK3-MURIM-MOD` (must match `murim.mod` path)
4. Enable "The Murim Chronicles" in the CK3 launcher
5. Start a new game — cultivation mechanics activate automatically for characters in the mod's culture/religion scope

**Note:** Not compatible with Ironman mode (custom scripted mechanics).

---

## Compatibility

| Requirement | Status |
|------------|--------|
| CK3 Version | 1.18.x (All Under Heaven patch) |
| All Under Heaven DLC | Recommended but not required (celestial features need it) |
| Vanilla Map | ✓ Uses the unmodified vanilla map — no new provinces or title changes |
| Vanilla Countries | ✓ All vanilla realms, titles, and characters remain intact |
| Ironman | ✗ Not compatible (custom script values and effects) |
| Multiplayer | Untested — all players must have identical mod version |
| Other Mods | Compatible with cosmetic mods; may conflict with mods that overwrite cultures, religions, or governments |

### What This Mod Does NOT Change
- No new map provinces or terrain
- No removed or renamed vanilla titles
- No changes to vanilla character history
- No overwritten vanilla cultures (adds new ones alongside)
- No overwritten vanilla religions (adds new ones alongside)

---

## Known Issues & Bugs

### Critical (Will Cause Errors)

1. **Fictional Province Keys in Land Setup**
   `00_asia_murim_setup.txt` references non-existent province IDs (`c_kunlun_mountains`, `c_penglai_island`, `province_siberia`, `province_burma_jungle`). These must be mapped to real vanilla CK3 title keys (e.g., `c_kunlun_mountains` → a real county in western China like `c_yutian`).

2. **Culture File Syntax Errors**
   `01_martial_cultures.txt` has missing newlines before `culture = {` blocks — lines like `# Orthodox Central Sectsculture = {` will fail to parse. Each `culture = {` must be on its own line.

3. **Non-Standard Government Properties**
   `celestial_governments.txt` uses properties that don't exist in CK3's government system (`can_call_crusade`, `can_have_demonic_vassals`, `can_raid`). Needs rewrite using valid `government_type` format with `valid_holdings`, `can_get_government`, etc.

4. **Invalid Religion Syntax**
   `01_martial_religions.txt` uses `can_sacrifice`, `can_grant_concessions`, and `custom_faiths` blocks that aren't valid CK3 religion definition syntax. Needs proper `religion` → `faith` → `doctrine` hierarchy.

### Moderate

5. **Culture Type Fields**
   `type = nomadic` and `type = seafaring` in culture definitions are not valid CK3 culture properties. Use appropriate `traditions` instead.

6. **Land Setup Block Names**
   `province_development_tier_1`, `development_tier_2`, etc. are not native CK3 constructs. The land setup file needs to use proper CK3 modding syntax (scripted effects, on_actions, or history files).

7. **`.mod` File Version Mismatch**
   `murim.mod` says `supported_version="1.18.0"` while the old README claimed "1.12.x". Now corrected in this README to 1.18.x.

### Minor

8. **Missing `descriptor.mod`**
   CK3 mods typically need both `<modname>.mod` (in the mod folder root) and a `descriptor.mod` inside the mod directory. Only `murim.mod` exists.

9. **Empty Icon References**
   Religion definitions have `icon = ""` — these will show blank icons in-game. Need valid icon paths or GFX references.

10. **No `.gfx` or GUI Files**
    No custom graphics, interface elements, or portrait modifiers. Traits and religions will display default or missing icons.

---

## Roadmap

### Phase 1 — Syntax Fixes (Current Priority)
- [ ] Fix all culture file newline/syntax errors
- [ ] Remap fictional province IDs to vanilla CK3 title keys
- [ ] Rewrite government types using valid CK3 government format
- [ ] Rewrite religion definitions using proper religion/faith/doctrine hierarchy
- [ ] Add `descriptor.mod` file
- [ ] Fix culture `type` fields → use traditions instead

### Phase 2 — Core Mechanics
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

- **22 files** across 15 directories
- **~165KB** of mod content
- **~90KB** in script values alone (6 variable system files)
- **14 cultures**, **4 religions**, **3 government types**
- **7 cultivation realms** with full XP/breakthrough/deviation mechanics
- **6 combat styles** with technique trees
- Fully compatible with vanilla CK3 map and All Under Heaven

---

## Credits

- **Engine:** Paradox Interactive — Crusader Kings 3
- **DLC Integration:** All Under Heaven (Paradox Interactive)
- **Inspiration:** Wuxia/Xianxia literature, Korean manhwa, Chinese cultivation novels
- **Created:** 2026
