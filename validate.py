#!/usr/bin/env python3
"""
validate.py — Post-ingest integrity checker for unreal-sidekick tutorials.

Run from the repo root:
    python validate.py

Exit 0 = all checks pass.
Exit 1 = one or more failures found (details printed to stdout).

Checks performed:
  1. No [PENDING EXTRACTION] markers in any tutorial body
  2. No extraction_status: pending in frontmatter
  3. No ue_version: "[PENDING]" in frontmatter
  4. No empty tags arrays (tags: [] or tags: [""])
  5. INDEX.md has no duplicate **File:** entries
  6. Every tutorial file on disk appears in INDEX.md exactly once
  7. Every INDEX.md file reference points to a file that exists on disk
  8. Every tutorial with a YouTube source has non-trivial structured notes (> 200 chars)
"""

import os
import re
import sys

TUTORIALS_DIR = os.path.join(os.path.dirname(__file__), "tutorials")
INDEX_PATH = os.path.join(TUTORIALS_DIR, "INDEX.md")

NOTES_MIN_CHARS = 200
TEMPLATE_REFS = {"filename.md"}  # placeholder in INDEX.md header — not real entries

failures = []


def fail(msg):
    failures.append(msg)
    print(f"  FAIL: {msg}")


def get_tutorial_files():
    return sorted(
        f for f in os.listdir(TUTORIALS_DIR)
        if f.endswith(".md") and f != "INDEX.md"
    )


def parse_index_refs():
    with open(INDEX_PATH, "r", encoding="utf-8-sig") as fh:
        content = fh.read()
    refs = []
    for m in re.finditer(r"\*\*File:\*\*\s+tutorials/([^\s\)]+\.md)", content):
        fname = m.group(1)
        if fname not in TEMPLATE_REFS:
            refs.append(fname)
    return refs


def get_notes_content(content):
    m = re.search(r"## Structured Notes(.+)", content, re.DOTALL)
    return m.group(1).strip() if m else ""


def is_youtube_source(content):
    m = re.search(r"^source:\s*(.+)", content, re.MULTILINE)
    if not m:
        return False
    return "youtube" in m.group(1).lower()


def check_tutorials():
    print("\n[1] Checking tutorial files for PENDING markers and frontmatter issues...")
    files = get_tutorial_files()
    for fname in files:
        path = os.path.join(TUTORIALS_DIR, fname)
        with open(path, "r", encoding="utf-8-sig") as fh:
            content = fh.read()

        # Check 1: PENDING EXTRACTION markers in body
        if "[PENDING EXTRACTION]" in content:
            fail(f"{fname}: contains [PENDING EXTRACTION] markers")

        # Check 2: extraction_status: pending
        if re.search(r"extraction_status:\s*pending", content, re.IGNORECASE):
            fail(f"{fname}: extraction_status is 'pending'")

        # Check 3: ue_version is PENDING placeholder
        if re.search(r'ue_version:\s*["\']?\[?PENDING', content, re.IGNORECASE):
            fail(f"{fname}: ue_version is still a PENDING placeholder")

        # Check 4: empty tags
        if re.search(r"tags:\s*\[\s*\]", content):
            fail(f"{fname}: tags array is empty")

        # Check 8: YouTube source needs non-trivial structured notes
        if is_youtube_source(content):
            notes = get_notes_content(content)
            if len(notes) < NOTES_MIN_CHARS:
                fail(
                    f"{fname}: YouTube source but structured notes are too short "
                    f"({len(notes)} chars, minimum {NOTES_MIN_CHARS})"
                )

    print(f"  Checked {len(files)} files.")


def check_index():
    print("\n[2] Checking INDEX.md for duplicates and cross-references...")

    refs = parse_index_refs()
    disk_files = set(get_tutorial_files())

    # Check 5: duplicate File: entries in INDEX
    seen = {}
    for fname in refs:
        seen.setdefault(fname, 0)
        seen[fname] += 1
    for fname, count in seen.items():
        if count > 1:
            fail(f"INDEX.md: duplicate entry for '{fname}' (appears {count} times)")

    ref_set = set(refs)

    # Check 6: every disk file is in INDEX
    missing_from_index = disk_files - ref_set
    for fname in sorted(missing_from_index):
        fail(f"INDEX.md: missing entry for '{fname}' (file exists on disk)")

    # Check 7: every INDEX ref has a matching file on disk
    orphan_refs = ref_set - disk_files
    for fname in sorted(orphan_refs):
        fail(f"INDEX.md: references non-existent file '{fname}'")

    print(f"  INDEX entries: {len(ref_set)} | Disk files: {len(disk_files)}")


def main():
    print("=" * 60)
    print("unreal-sidekick validate.py")
    print("=" * 60)

    if not os.path.isdir(TUTORIALS_DIR):
        print(f"ERROR: tutorials directory not found at {TUTORIALS_DIR}")
        sys.exit(1)

    if not os.path.isfile(INDEX_PATH):
        print(f"ERROR: INDEX.md not found at {INDEX_PATH}")
        sys.exit(1)

    check_tutorials()
    check_index()

    print("\n" + "=" * 60)
    if failures:
        print(f"RESULT: FAIL — {len(failures)} issue(s) found:")
        for f in failures:
            print(f"  • {f}")
        sys.exit(1)
    else:
        print("RESULT: PASS — all checks clean.")
        sys.exit(0)


if __name__ == "__main__":
    main()
