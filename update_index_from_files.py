"""
Reads all tutorial files with extraction_status: complete
and updates any PENDING INDEX.md entries from the file content.
"""
import os, re

INDEX_PATH = 'tutorials/INDEX.md'

def read_file(path):
    return open(path, 'r', encoding='utf-8-sig').read()

def extract_section(content, section_name):
    """Extract text under a ## Section Name heading, up to the next ## heading."""
    pattern = rf'### {re.escape(section_name)}\s*\n(.*?)(?=\n###|\Z)'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        return m.group(1).strip()
    return None

def get_tags_from_frontmatter(content):
    m = re.search(r'^tags:\s*\[([^\]]*)\]', content, re.MULTILINE)
    if m:
        raw = m.group(1)
        tags = [t.strip().strip('"').strip("'") for t in raw.split(',') if t.strip()]
        return ', '.join(tags)
    return None

def get_ue_version_from_frontmatter(content):
    m = re.search(r'^ue_version:\s*["\']?([^"\'\n]+)["\']?', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return None

idx_content = read_file(INDEX_PATH)

# Find all INDEX entries that are PENDING
# Split by ### entries
sections = re.split(r'(?=^### )', idx_content, flags=re.MULTILINE)

updates_made = 0
new_sections = []

for section in sections:
    if '[PENDING EXTRACTION]' not in section:
        new_sections.append(section)
        continue

    # Find the file path in this section
    file_match = re.search(r'\*\*File:\*\* (tutorials/[^\s\n]+\.md)', section)
    if not file_match:
        new_sections.append(section)
        continue

    fpath = file_match.group(1)
    if not os.path.exists(fpath):
        print(f"  FILE NOT FOUND: {fpath}")
        new_sections.append(section)
        continue

    tut_content = read_file(fpath)

    # Check if extraction is complete
    status_m = re.search(r'extraction_status:\s*(\w+)', tut_content)
    if not status_m or status_m.group(1) != 'complete':
        print(f"  STILL PENDING IN FILE: {fpath}")
        new_sections.append(section)
        continue

    # Extract summary, tags, UE version
    summary = extract_section(tut_content, 'Summary')
    if not summary:
        print(f"  NO SUMMARY FOUND: {fpath}")
        new_sections.append(section)
        continue

    # Collapse multi-line summary to single line
    summary_single = ' '.join(summary.splitlines()).strip()
    # Truncate very long summaries for INDEX
    if len(summary_single) > 400:
        summary_single = summary_single[:397] + '...'

    # Get tags from frontmatter
    tags = get_tags_from_frontmatter(tut_content)

    # Get UE version from frontmatter
    ue_version = get_ue_version_from_frontmatter(tut_content)

    # Get difficulty from structured notes
    difficulty = extract_section(tut_content, 'Difficulty')

    # Get actual UE version from Structured Notes (more precise than frontmatter)
    ue_version_notes = extract_section(tut_content, 'UE Version')
    if ue_version_notes and ue_version_notes != '[PENDING EXTRACTION]':
        ue_version = ue_version_notes.strip()

    # Build updated section
    new_section = section

    # Replace [PENDING EXTRACTION] in Summary
    new_section = re.sub(
        r'(\*\*Summary:\*\*) \[PENDING EXTRACTION\]',
        f'\\1 {summary_single}',
        new_section
    )

    # Replace [PENDING] in Tags
    if tags:
        new_section = re.sub(
            r'(\*\*Tags:\*\*) \[PENDING\]',
            f'\\1 {tags}',
            new_section
        )

    # Replace [PENDING] in UE Version
    if ue_version:
        new_section = re.sub(
            r'(\*\*UE Version:\*\*) \[PENDING\]',
            f'\\1 {ue_version}',
            new_section
        )

    if new_section != section:
        title = section.split('\n')[0].strip()
        print(f"  Updated: {title}")
        updates_made += 1

    new_sections.append(new_section)

# Write updated INDEX.md
new_idx = ''.join(new_sections)
with open(INDEX_PATH, 'w', encoding='utf-8-sig', newline='\r\n') as f:
    f.write(new_idx)

print(f"\nDone. {updates_made} INDEX entries updated.")

# Verify
idx2 = open(INDEX_PATH, 'r', encoding='utf-8-sig').read()
remaining = idx2.count('[PENDING EXTRACTION]')
print(f"Remaining [PENDING EXTRACTION] in INDEX.md: {remaining}")
