#!/usr/bin/env python3
"""CK3 Murim Chronicles - Comprehensive Mod Audit Script
Checks for all known crash and dead-end causes."""

import re, os, glob, collections, sys

MOD_ROOT = '/home/user/CK3-Murim-Chronicles'
issues = []

def add_issue(severity, category, msg):
    issues.append((severity, category, msg))

# ============================================================
# 1. BRACKET BALANCE
# ============================================================
for f in sorted(glob.glob(f'{MOD_ROOT}/common/**/*.txt', recursive=True) +
                glob.glob(f'{MOD_ROOT}/events/*.txt')):
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    opens = content.count('{')
    closes = content.count('}')
    if opens != closes:
        add_issue('CRASH', 'brackets', f'{os.path.relpath(f, MOD_ROOT)}: {{ {opens} }} {closes} (diff {opens-closes})')

# ============================================================
# 2. MISSING TRAITS
# ============================================================
defined_traits = set()
for f in glob.glob(f'{MOD_ROOT}/common/traits/*.txt'):
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    depth = 0
    for line in content.split('\n'):
        stripped = line.strip()
        if depth == 0:
            m = re.match(r'^([a-z_][a-z0-9_]*)\s*=\s*\{', stripped)
            if m:
                defined_traits.add(m.group(1))
        depth += stripped.count('{') - stripped.count('}')

referenced_traits = set()
for f in glob.glob(f'{MOD_ROOT}/events/*.txt') + glob.glob(f'{MOD_ROOT}/common/**/*.txt', recursive=True):
    if '/traits/' in f:
        continue
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    for m in re.finditer(r'(?:add_trait|has_trait|remove_trait)\s*=\s*([a-z_]\w+)', content):
        referenced_traits.add(m.group(1))

vanilla_traits = {
    'brave','craven','wounded_1','wounded_2','wounded_3','diplomat','strategist',
    'whole_of_body','athletic','strong','giant','shrewd','temperate','patient',
    'diligent','ambitious','humble','zealous','cynical','just','arbitrary',
    'wrathful','calm','paranoid','trusting','shy','gregarious','content','lazy',
    'gluttonous','lustful','chaste','greedy','generous','deceitful','honest',
    'compassionate','sadistic','callous','stubborn','fickle','arrogant',
    'forgiving','vengeful','charming','haughty','martial_artist',
    'beauty_good_1','beauty_good_2','beauty_good_3',
    'beauty_bad_1','beauty_bad_2','beauty_bad_3',
    'intellect_good_1','intellect_good_2','intellect_good_3',
    'intellect_bad_1','intellect_bad_2','intellect_bad_3',
    'physique_good_1','physique_good_2','physique_good_3',
    'physique_bad_1','physique_bad_2','physique_bad_3',
    'education_martial_1','education_martial_2','education_martial_3','education_martial_4',
    'education_stewardship_1','education_stewardship_2','education_stewardship_3','education_stewardship_4',
    'education_intrigue_1','education_intrigue_2','education_intrigue_3','education_intrigue_4',
    'education_diplomacy_1','education_diplomacy_2','education_diplomacy_3','education_diplomacy_4',
    'education_learning_1','education_learning_2','education_learning_3','education_learning_4',
    'blademaster_1','blademaster_2','blademaster_3',
    'reveler_1','reveler_2','reveler_3','hunter_1','hunter_2','hunter_3',
    'mystic_1','mystic_2','mystic_3',
    'lifestyle_herbalist','lifestyle_physician','lifestyle_mystic',
    'lifestyle_hunter','lifestyle_reveler','lifestyle_blademaster',
    'berserker','gallant','torturer','seducer','schemer',
    'theologian','scholar','architect','administrator','avaricious','august',
    'celibate','deviant','sodomite','dwarf','scaly','clubfooted',
    'hunchbacked','lisping','stuttering','one_eyed','one_legged',
    'disfigured','blind','maimed','infirm','ill','pneumonic','leper',
    'lover','soulmate','rival','nemesis','friend','best_friend',
    'witch','herbalist','possessed','lunatic','drunkard',
    'hashishiyah','raider','varangian','warrior','shieldmaiden',
    'poet','peasant_leader','recluse','irritable','depressed_1',
    'flagellant','profligate','improvident','contrite','comfort_eater',
    'inappetetic','pureblood','fecund','albino','spindly','weak','dull',
    'slow','ugly','scarred','wounded','brutally_scarred',
    'adventurer','beautiful','curious','excommunicated','frail','genius',
    'imbecile','incapable','intelligent','kinslayer_1','kinslayer_2',
    'kinslayer_3','murderer','mystic','pilgrim','quick','robust','rowdy','wanderer',
}

missing_traits = referenced_traits - defined_traits - vanilla_traits
for t in sorted(missing_traits):
    add_issue('CRASH', 'missing_trait', t)

# ============================================================
# 3. INVALID SYNTAX: has_culture_group
# ============================================================
for f in glob.glob(f'{MOD_ROOT}/**/*.txt', recursive=True):
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    for m in re.finditer(r'has_culture_group', content):
        line_num = content[:m.start()].count('\n') + 1
        add_issue('CRASH', 'has_culture_group', f'{os.path.relpath(f, MOD_ROOT)}:{line_num}')

# ============================================================
# 4. INVALID ON_ACTION HOOKS
# ============================================================
valid_hooks = {
    'on_yearly_pulse','on_five_year_pulse','on_quarterly_pulse',
    'on_quarterly_character_pulse','on_monthly_pulse',
    'on_death','on_game_start','on_game_start_after_lobby',
    'on_title_gained','on_title_lost','on_war_started','on_war_ended','on_war_won',
    'on_battle_end','on_birth','on_birthday','on_coming_of_age',
    'on_marriage','on_join_court','on_imprisonment','on_release_from_prison',
    'on_alliance_added','on_alliance_broken',
    'on_combat_end_winner','on_combat_end_loser',
    'on_faith_change','on_culture_change',
    'on_activity_pulse','on_duel_completion',
    'on_county_occupied','on_siege_completion',
    'on_character_death','on_birth_child',
}

for f in glob.glob(f'{MOD_ROOT}/common/on_actions/*.txt'):
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    depth = 0
    for i, line in enumerate(content.split('\n'), 1):
        stripped = line.strip()
        if depth == 0:
            m = re.match(r'^(on_\w+)\s*=\s*\{', stripped)
            if m:
                hook = m.group(1)
                if hook not in valid_hooks and not hook.startswith('on_murim'):
                    add_issue('CRASH', 'invalid_hook', f'{os.path.basename(f)}:{i}: {hook}')
        depth += stripped.count('{') - stripped.count('}')

# ============================================================
# 5. MISSING EVENTS (dead ends)
# ============================================================
defined_events = set()
for f in glob.glob(f'{MOD_ROOT}/events/*.txt'):
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    for m in re.finditer(r'^\s*(murim_\w+\.\d+)\s*=\s*\{', content, re.MULTILINE):
        defined_events.add(m.group(1))

missing_events = collections.defaultdict(list)
for f in sorted(glob.glob(f'{MOD_ROOT}/**/*.txt', recursive=True)):
    if '/events/' not in f and '/common/' not in f:
        continue
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    for m in re.finditer(r'(?:trigger_event|id)\s*=\s*(murim_\w+\.\d+)', content):
        eid = m.group(1)
        if eid not in defined_events:
            line_num = content[:m.start()].count('\n') + 1
            missing_events[eid].append(f'{os.path.relpath(f, MOD_ROOT)}:{line_num}')

for eid in sorted(missing_events):
    refs = len(missing_events[eid])
    add_issue('DEAD_END', 'missing_event', f'{eid} ({refs} refs)')

# ============================================================
# 6. MISSING SCRIPTED EFFECTS
# ============================================================
defined_effects = set()
for f in glob.glob(f'{MOD_ROOT}/common/scripted_effects/*.txt'):
    with open(f, 'r', errors='replace') as fh:
        for line in fh:
            m = re.match(r'^(\w+)\s*=\s*\{', line)
            if m:
                defined_effects.add(m.group(1))

for f in glob.glob(f'{MOD_ROOT}/events/*.txt') + glob.glob(f'{MOD_ROOT}/common/on_actions/*.txt'):
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    for m in re.finditer(r'\b(murim_\w*effect\w*)\s*=\s*(yes|\{)', content):
        name = m.group(1)
        if name not in defined_effects:
            line_num = content[:m.start()].count('\n') + 1
            add_issue('DEAD_END', 'missing_effect', f'{name} at {os.path.relpath(f, MOD_ROOT)}:{line_num}')

# ============================================================
# 7. MISSING SCRIPTED TRIGGERS
# ============================================================
defined_triggers = set()
for f in glob.glob(f'{MOD_ROOT}/common/scripted_triggers/*.txt'):
    with open(f, 'r', errors='replace') as fh:
        for line in fh:
            m = re.match(r'^(\w+)\s*=\s*\{', line)
            if m:
                defined_triggers.add(m.group(1))

for f in glob.glob(f'{MOD_ROOT}/events/*.txt') + glob.glob(f'{MOD_ROOT}/common/**/*.txt', recursive=True):
    if '/scripted_triggers/' in f:
        continue
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    for m in re.finditer(r'\b(murim_\w*trigger\w*)\s*=\s*(yes|no)', content):
        name = m.group(1)
        if name not in defined_triggers:
            line_num = content[:m.start()].count('\n') + 1
            add_issue('DEAD_END', 'missing_trigger', f'{name} at {os.path.relpath(f, MOD_ROOT)}:{line_num}')

# ============================================================
# 8. BOM CHECK
# ============================================================
for f in glob.glob(f'{MOD_ROOT}/localization/**/*.yml', recursive=True):
    with open(f, 'rb') as fh:
        first3 = fh.read(3)
    if first3 != b'\xef\xbb\xbf':
        add_issue('CRASH', 'missing_bom', os.path.relpath(f, MOD_ROOT))

# ============================================================
# 9. DUPLICATE EVENT IDS
# ============================================================
all_event_ids = collections.defaultdict(list)
for f in glob.glob(f'{MOD_ROOT}/events/*.txt'):
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    for m in re.finditer(r'^\s*(\w+\.\d+)\s*=\s*\{', content, re.MULTILINE):
        all_event_ids[m.group(1)].append(os.path.basename(f))

for eid, files in sorted(all_event_ids.items()):
    if len(files) > 1:
        add_issue('CRASH', 'duplicate_event', f'{eid}: {files}')

# ============================================================
# 10. MISSING CHARACTER MEMORY TYPES
# ============================================================
defined_memories = set()
mem_dir = f'{MOD_ROOT}/common/character_memory_types'
if os.path.isdir(mem_dir):
    for f in glob.glob(f'{mem_dir}/*.txt'):
        with open(f, 'r', errors='replace') as fh:
            for line in fh:
                m = re.match(r'^(\w+)\s*=\s*\{', line)
                if m:
                    defined_memories.add(m.group(1))

for f in glob.glob(f'{MOD_ROOT}/events/*.txt'):
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    for m in re.finditer(r'create_character_memory\s*=\s*\{[^}]*type\s*=\s*(\w+)', content):
        mem_type = m.group(1)
        if mem_type not in defined_memories:
            add_issue('CRASH', 'missing_memory_type', mem_type)

# ============================================================
# 11. DUPLICATE TRAIT NAMES
# ============================================================
trait_name_files = collections.defaultdict(list)
for f in glob.glob(f'{MOD_ROOT}/common/traits/*.txt'):
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    depth = 0
    for line in content.split('\n'):
        stripped = line.strip()
        if depth == 0:
            m = re.match(r'^([a-z_][a-z0-9_]*)\s*=\s*\{', stripped)
            if m:
                trait_name_files[m.group(1)].append(os.path.basename(f))
        depth += stripped.count('{') - stripped.count('}')

for name, files in sorted(trait_name_files.items()):
    if len(files) > 1:
        add_issue('CRASH', 'duplicate_trait', f'{name}: {files}')

# ============================================================
# 12. MISSING OPINION MODIFIERS
# ============================================================
defined_opinions = set()
for f in glob.glob(f'{MOD_ROOT}/common/opinion_modifiers/*.txt'):
    with open(f, 'r', errors='replace') as fh:
        for line in fh:
            m = re.match(r'^(\w+)\s*=\s*\{', line)
            if m:
                defined_opinions.add(m.group(1))

for f in glob.glob(f'{MOD_ROOT}/events/*.txt') + glob.glob(f'{MOD_ROOT}/common/**/*.txt', recursive=True):
    if '/opinion_modifiers/' in f:
        continue
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    for m in re.finditer(r'(?:modifier|opinion)\s*=\s*(murim_\w+)', content):
        name = m.group(1)
        if name not in defined_opinions and '_opinion' in name:
            add_issue('DEAD_END', 'missing_opinion', name)

# ============================================================
# 13. MISSING CHARACTER MODIFIERS
# ============================================================
defined_char_mods = set()
for f in glob.glob(f'{MOD_ROOT}/common/character_modifiers/*.txt'):
    with open(f, 'r', errors='replace') as fh:
        for line in fh:
            m = re.match(r'^(\w+)\s*=\s*\{', line)
            if m:
                defined_char_mods.add(m.group(1))

for f in glob.glob(f'{MOD_ROOT}/events/*.txt') + glob.glob(f'{MOD_ROOT}/common/**/*.txt', recursive=True):
    if '/character_modifiers/' in f:
        continue
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    for m in re.finditer(r'has_character_modifier\s*=\s*(murim_\w+)', content):
        name = m.group(1)
        if name not in defined_char_mods:
            add_issue('DEAD_END', 'missing_char_modifier', name)
    for m in re.finditer(r'add_character_modifier\s*=\s*\{[^}]*modifier\s*=\s*(murim_\w+)', content):
        name = m.group(1)
        if name not in defined_char_mods:
            add_issue('CRASH', 'missing_char_modifier_add', name)

# ============================================================
# 14. CREATE_CHARACTER WITHOUT CULTURE/LOCATION
# ============================================================
for f in sorted(glob.glob(f'{MOD_ROOT}/events/*.txt') +
                glob.glob(f'{MOD_ROOT}/common/**/*.txt', recursive=True)):
    with open(f, 'r', errors='replace') as fh:
        content = fh.read()
    if 'create_character' not in content:
        continue
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        if re.search(r'create_character\s*=\s*\{', lines[i]):
            block_start = i
            brace_count = 0
            block_end = None
            for j in range(i, len(lines)):
                brace_count += lines[j].count('{') - lines[j].count('}')
                if brace_count <= 0:
                    block_end = j
                    break
            if block_end is None:
                i += 1
                continue
            block_text = '\n'.join(lines[block_start:block_end+1])
            has_culture = bool(re.search(r'\bculture\s*=', block_text))
            has_location = bool(re.search(r'\blocation\s*=', block_text))
            has_template = bool(re.search(r'\btemplate\s*=', block_text))
            if not has_location:
                add_issue('CRASH', 'create_character_no_location',
                    f'{os.path.relpath(f, MOD_ROOT)}:{block_start+1}')
            if not has_culture and not has_template:
                add_issue('CRASH', 'create_character_no_culture',
                    f'{os.path.relpath(f, MOD_ROOT)}:{block_start+1}')
            i = block_end + 1
        else:
            i += 1

# ============================================================
# REPORT
# ============================================================
crash_issues = [i for i in issues if i[0] == 'CRASH']
dead_end_issues = [i for i in issues if i[0] == 'DEAD_END']

# Deduplicate
seen = set()
unique_issues = []
for i in issues:
    key = (i[0], i[1], i[2])
    if key not in seen:
        seen.add(key)
        unique_issues.append(i)

crash_issues = [i for i in unique_issues if i[0] == 'CRASH']
dead_end_issues = [i for i in unique_issues if i[0] == 'DEAD_END']

print(f"{'='*60}")
print(f"AUDIT RESULTS")
print(f"{'='*60}")
print(f"CRASH issues: {len(crash_issues)}")
print(f"DEAD_END issues: {len(dead_end_issues)}")
print(f"{'='*60}")

if crash_issues:
    print("\n--- CRASH ISSUES ---")
    by_cat = collections.defaultdict(list)
    for s, c, m in crash_issues:
        by_cat[c].append(m)
    for cat, msgs in sorted(by_cat.items()):
        print(f"\n[{cat}] ({len(msgs)}):")
        for msg in msgs[:20]:
            print(f"  {msg}")
        if len(msgs) > 20:
            print(f"  ... and {len(msgs)-20} more")

if dead_end_issues:
    print("\n--- DEAD END ISSUES ---")
    by_cat = collections.defaultdict(list)
    for s, c, m in dead_end_issues:
        by_cat[c].append(m)
    for cat, msgs in sorted(by_cat.items()):
        print(f"\n[{cat}] ({len(msgs)}):")
        for msg in msgs[:30]:
            print(f"  {msg}")
        if len(msgs) > 30:
            print(f"  ... and {len(msgs)-30} more")

if not crash_issues and not dead_end_issues:
    print("\nALL CLEAR - No issues found!")

sys.exit(1 if crash_issues else 0)
