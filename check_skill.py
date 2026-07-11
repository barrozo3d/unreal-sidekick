import os, re

print("=== OVERALL SKILL CHECK ===")

# 1. Count total tutorials
idx = open("tutorials/INDEX.md", "r", encoding="utf-8-sig").read()
entries = re.findall(r"^### ", idx, re.MULTILINE)
pending = re.findall(r"\[PENDING EXTRACTION\]", idx)
print(f"Tutorials in INDEX: {len(entries)} total, {len(pending)} pending extraction")

# 2. Check all referenced files in skill file exist
skill = open("SKILL.md", "r", encoding="utf-8").read()
refs_mentioned = re.findall(r"`(references/[^`]+\.md)`", skill)
refs_mentioned += re.findall(r"`(recipes/[^`]+\.md)`", skill)
# Filter out template placeholders (ueXX, X-X patterns used as changelog examples)
refs_mentioned = [r for r in refs_mentioned if 'XX' not in r and 'X-X' not in r]
refs_missing = [r for r in refs_mentioned if not os.path.exists(r)]
print(f"Files mentioned in skill file: {len(refs_mentioned)}, missing: {len(refs_missing)}")
for r in refs_missing:
    print(f"  MISSING: {r}")

# 3. Check for dead links in reference files
ref_files = [f for f in os.listdir("references") if f.endswith(".md")]
cross_refs_broken = []
for rf in ref_files:
    content = open(f"references/{rf}", "r", encoding="utf-8-sig").read()
    file_refs = re.findall(r"`((?:references|recipes|tutorials)/[^`]+\.md)`", content)
    for fr in file_refs:
        if not os.path.exists(fr):
            cross_refs_broken.append((rf, fr))
print(f"Broken cross-refs in reference files: {len(cross_refs_broken)}")
for src, broken in cross_refs_broken:
    print(f"  {src} -> {broken}")

# 4. Check version-tracker is current
vt = open("references/version-tracker.md", "r", encoding="utf-8-sig").read()
# Support both plain and bold-markdown frontmatter: "current_stable: X" or "**current_stable:** X"
stable_match = re.search(r"\*?\*?current_stable:\*?\*?\s*(.+)", vt)
checked_match = re.search(r"\*?\*?last_checked:\*?\*?\s*(.+)", vt)
print(f"Version tracker current_stable: {stable_match.group(1).strip() if stable_match else 'NOT FOUND'}")
print(f"Version tracker last_checked: {checked_match.group(1).strip() if checked_match else 'NOT FOUND'}")

# 5. Check tutorial file/index consistency
all_tutorial_files = set()
for f in os.listdir("tutorials"):
    if f.endswith(".md") and f != "INDEX.md":
        all_tutorial_files.add(f)

referenced = set(re.findall(r"tutorials/([^/\s]+\.md)", idx))
referenced.discard("filename.md")  # template example

orphans = all_tutorial_files - referenced
missing_on_disk = referenced - all_tutorial_files
print(f"Tutorial files: {len(all_tutorial_files)} on disk, {len(referenced)} in INDEX")
print(f"Orphaned files (disk not indexed): {len(orphans)}")
for o in sorted(orphans):
    print(f"  ORPHAN: {o}")
print(f"Missing files (indexed not on disk): {len(missing_on_disk)}")
for m in sorted(missing_on_disk):
    print(f"  MISSING: {m}")

print()
print("=== CHECK COMPLETE ===")
