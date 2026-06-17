import glob, sys, io, re, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

index_path = 'tutorials/INDEX.md'
raw = open(index_path, 'rb').read()
content = raw.decode('utf-8-sig')

already_done = set()

updated = 0
not_found = []

for fpath in sorted(glob.glob('tutorials/*.md')):
    tut = open(fpath, encoding='utf-8', errors='ignore').read()
    if 'Dean Yurke' not in tut and 'deanyurke' not in fpath:
        continue
    if 'extraction_status: complete' not in tut:
        continue

    slug = os.path.basename(fpath).replace('.md', '')
    if slug in already_done:
        continue

    title = ''
    ue_ver = ''
    tags_raw = ''

    for line in tut.split('\n'):
        if line.startswith('title:'):
            title = line[6:].strip()
        if line.startswith('ue_version:'):
            ue_ver = line[11:].strip().strip('"')
        if line.startswith('tags:'):
            tags_raw = line[5:].strip()

    m = re.search(r'### Summary\n(.+?)(?=\n###|\n---)', tut, re.DOTALL)
    summary = m.group(1).strip()[:200] if m else ''

    tags_list = re.findall(r'[\w\-]+', tags_raw)
    tags_str = ' '.join('`#' + t + '`' for t in tags_list[:10])

    old_pat = '- **UE Version:** [PENDING]\r\n- **Tags:** [PENDING]\r\n- **Summary:** [PENDING EXTRACTION]\r\n- **File:** tutorials/' + slug + '.md'
    new_pat = '- **UE Version:** ' + ue_ver + '\r\n- **Tags:** ' + tags_str + '\r\n- **Summary:** ' + summary + '\r\n- **File:** tutorials/' + slug + '.md'

    if old_pat in content:
        content = content.replace(old_pat, new_pat, 1)
        updated += 1
        print('Updated: ' + title[:65])
    else:
        not_found.append(slug)
        print('NOT FOUND: ' + slug)

print('\nTotal updated: ' + str(updated))
if not_found:
    print('Not found: ' + str(len(not_found)))

open(index_path, 'wb').write(('﻿' + content).encode('utf-8'))
print('INDEX.md saved.')
