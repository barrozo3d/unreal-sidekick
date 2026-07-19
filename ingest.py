"""
ingest.py — Data collection for unreal-sidekick skill (Step 1 of 2)

NO API CALLS. Collects everything and saves to disk for Claude Code extraction.

Pipeline — YouTube tutorial (Step 1 — this script):
  1. yt-dlp metadata + chapter parsing
  2. Whisper transcription (falls back to yt-dlp captions), per-sentence
     timestamps preserved even inside chapters
  3. Transcript segmented by chapters (or one "Full Content" section)
  4. Save raw .md to tutorials/<slug>.md (frame_status: pending-selection)
  5. Update INDEX.md with pending stub
  6. git commit + push

No video is downloaded and no frames are extracted here — frame timestamps
need judgment (which moment actually shows the technique), not a blind
percentage split, so that's deferred to select_frames.py (Step 2), run by
Claude Code after reading the timestamped transcript. See select_frames.py's
docstring for that step. Frames land in tutorials/frames/<slug>/ (local only,
not committed to git) once selected.

Pipeline — Epic documentation page (dev.epicgames.com/documentation):
  1. Detect hub page
  2. BFS crawl up to --doc-depth levels (default 2)
  3. Extract clean text per page
  4. Assemble into one structured .md file
  5. Update INDEX.md with pending stub
  6. git commit + push

Pipeline — Epic community page (dev.epicgames.com/community):
  1. Detect community URL → auto-resolve to YouTube via search
  2. Proceed as YouTube tutorial

Usage:
  python ingest.py <youtube-url>
  python ingest.py <youtube-url> --whisper-model small
  python ingest.py <youtube-url> --skip-video
  python ingest.py <epic-doc-hub-url>
  python ingest.py <epic-doc-hub-url> --doc-depth 1
  python ingest.py <epic-community-url>
  python ingest.py <epic-community-url> --youtube-url https://youtu.be/CORRECT_ID
"""

import sys, os, re, json, subprocess, tempfile, shutil, argparse, time
from datetime import datetime
from pathlib import Path

# Ensure stdout handles Unicode on Windows (cp1252 default breaks non-ASCII titles)
# and flushes per line — block-buffered prints otherwise arrive after subprocess
# (git/yt-dlp) output when both are captured, scrambling the step order in logs.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)

# ── Configuration ─────────────────────────────────────────────────────────────

SKILL_DIR     = Path(__file__).parent
TUTORIALS_DIR = SKILL_DIR / "tutorials"
FRAMES_DIR    = TUTORIALS_DIR / "frames"
INDEX_FILE    = TUTORIALS_DIR / "INDEX.md"
def _default_whisper_model():
    """small on GPU (better accuracy, still fast), base on CPU (speed matters more)."""
    try:
        import torch
        if torch.cuda.is_available():
            return "small"
    except Exception:
        pass
    return "base"

DEFAULT_WHISPER = _default_whisper_model()
EPIC_DOC_BASE    = "https://dev.epicgames.com/documentation/unreal-engine/"
EPIC_DOC_HOST    = "dev.epicgames.com"
CRAWL_DELAY      = 0.4   # seconds between requests (be polite)

# ── Utilities ─────────────────────────────────────────────────────────────────

def slugify(text):
    s = text.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    return s.strip("-")[:80]

def _ytdlp_cmd():
    """Return yt-dlp invocation, using cookies.txt if present for YouTube bot bypass.

    YouTube bot detection requires authentication. To fix 429/sign-in errors:
    1. Install browser extension: 'Get cookies.txt LOCALLY' (Chrome/Edge/Firefox)
    2. Go to youtube.com while logged in
    3. Click the extension -> Export -> save as cookies.txt in this skill directory
    4. Re-run ingest.py — it will pick up cookies.txt automatically
    """
    base = ["yt-dlp"] if shutil.which("yt-dlp") else [sys.executable, "-m", "yt_dlp"]
    cookies_file = SKILL_DIR / "cookies.txt"
    if cookies_file.exists():
        return base + ["--cookies", str(cookies_file), "--remote-components", "ejs:github"]
    return base

def check_prerequisites():
    missing = []
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "--version"],
                       capture_output=True)
    if r.returncode != 0:
        missing.append("yt-dlp (pip install yt-dlp)")
    if missing:
        print("Missing prerequisites:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)
    has_ffmpeg  = bool(shutil.which("ffmpeg"))
    has_whisper = False
    try:
        import whisper
        has_whisper = True
    except ImportError:
        pass
    return has_ffmpeg, has_whisper

# ── YouTube: Metadata ──────────────────────────────────────────────────────────

def get_info(url):
    r = subprocess.run(
        _ytdlp_cmd() + ["--dump-json", "--no-playlist", url],
        capture_output=True, text=True, timeout=60, check=True
    )
    return json.loads(r.stdout)

# ── YouTube: Transcript ────────────────────────────────────────────────────────

WHISPER_VOCAB_HINT = ("Unreal Engine, UE5, Nanite, Lumen, Niagara, MetaHuman, Sequencer, Movie Render Queue, Movie Render Graph, Blueprint, Control Rig, Chaos, Substrate, MegaLights, Landscape, World Partition, PCG, RVT, LOD, Fab")

def _load_whisper_model(model_name):
    """First use of a model downloads its weights, and tqdm floods captured
    output with hundreds of progress-bar lines on stderr. Print one notice
    instead; replay the captured stderr only if loading actually fails."""
    import io, contextlib, whisper
    cache_dir = Path(os.getenv("XDG_CACHE_HOME", str(Path.home() / ".cache"))) / "whisper"
    if not (cache_dir / f"{model_name}.pt").exists():
        print(f"      Whisper model '{model_name}' not cached yet - downloading weights (one-time)...")
    captured = io.StringIO()
    try:
        with contextlib.redirect_stderr(captured):
            return whisper.load_model(model_name)
    except Exception:
        sys.stderr.write(captured.getvalue())
        raise

def whisper_transcribe(audio_path, model_name):
    model = _load_whisper_model(model_name)
    # initial_prompt biases decoding toward this skill's vocabulary — without it
    # Whisper mis-hears domain terms (e.g. "COPs" -> "cups", "Houdini" -> "Odini").
    return model.transcribe(str(audio_path), initial_prompt=WHISPER_VOCAB_HINT)

def download_audio(url, tmp):
    out = str(tmp / "audio.%(ext)s")
    cmd = _ytdlp_cmd() + ["-x", "--audio-format", "mp3", "--audio-quality", "0",
         "--no-playlist", "-o", out, url]
    # YouTube throttling makes one-off download failures common; a single retry
    # usually recovers and preserves the timestamped Whisper transcript instead
    # of degrading to the timestamp-less captions fallback.
    for attempt in (1, 2):
        try:
            subprocess.run(cmd, capture_output=True, timeout=300, check=True)
            break
        except subprocess.CalledProcessError:
            if attempt == 2:
                raise
            print("      Audio download failed - retrying once...")
    for f in tmp.iterdir():
        if f.suffix in (".mp3", ".m4a", ".ogg", ".webm"):
            return f
    raise FileNotFoundError("Audio file not found after download")

def ytdlp_captions(url, tmp):
    subprocess.run(
        _ytdlp_cmd() + ["--write-auto-subs", "--sub-lang", "en",
         "--sub-format", "vtt", "--skip-download", "--no-playlist",
         "-o", str(tmp / "%(id)s"), url],
        capture_output=True, timeout=120
    )
    for f in tmp.glob("*.vtt"):
        raw = f.read_text(encoding="utf-8", errors="ignore")
        lines = []
        for line in raw.splitlines():
            if "-->" in line or line.startswith("WEBVTT") or line.strip().isdigit():
                continue
            clean = re.sub(r"<[^>]+>", "", line).strip()
            if clean and (not lines or clean != lines[-1]):
                lines.append(clean)
        f.unlink()
        return " ".join(lines)
    return ""

def segment_by_chapters(transcript, chapters):
    """
    Bucket the Whisper transcript into sections (by official chapters, or one
    "Full Content" section if none exist). Each section keeps both a joined
    `text` blob (for the completeness/hallucination safeguards) and a
    per-sentence `segments` list of (start_seconds, text) tuples — the fine
    timestamps are what let Step 2 pick content-anchored frame moments instead
    of trusting chapter boundaries blindly.
    """
    segs = transcript.get("segments", [])
    if not chapters:
        all_segs = [(s.get("start", 0), s["text"].strip()) for s in segs]
        return [{"title": "Full Content", "start": 0,
                 "text": transcript.get("text", "").strip(),
                 "segments": all_segs}]
    result = []
    for i, ch in enumerate(chapters):
        t0 = ch.get("start_time", 0)
        t1 = chapters[i+1].get("start_time", float("inf")) if i+1 < len(chapters) else float("inf")
        in_range = [s for s in segs if t0 <= s.get("start", 0) < t1]
        text = " ".join(s["text"].strip() for s in in_range).strip()
        seg_list = [(s.get("start", 0), s["text"].strip()) for s in in_range]
        result.append({"title": ch.get("title", f"Chapter {i+1}"), "start": t0,
                        "text": text, "segments": seg_list})
    return result

# ── YouTube: Frame extraction ──────────────────────────────────────────────────

def download_video_low(url, tmp):
    out = str(tmp / "video.%(ext)s")
    subprocess.run(
        _ytdlp_cmd() + ["-f", "worst[ext=mp4]/worst", "--no-playlist", "-o", out, url],
        capture_output=True, timeout=600, check=True
    )
    for f in tmp.iterdir():
        if f.suffix in (".mp4", ".webm", ".mkv"):
            return f
    raise FileNotFoundError("Video not found after download")

def extract_frames(video_path, timestamps, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    frames = []
    for i, ts in enumerate(timestamps):
        dst = out_dir / f"frame_{i:03d}.jpg"
        subprocess.run(
            ["ffmpeg", "-ss", str(max(ts, 0)), "-i", str(video_path),
             "-frames:v", "1", "-q:v", "2", str(dst), "-y"],
            capture_output=True
        )
        if dst.exists():
            frames.append(dst)
    return frames

# ── Ingest safeguards ─────────────────────────────────────────────────────────

_STOP_WORDS = {
    'the','a','an','and','or','in','of','to','is','it','i','we','you','this',
    'that','for','are','on','at','be','by','with','have','was','as','from',
    'so','if','but','not','do','my','me','he','she','they','up','out','just',
    'can','all','now','will','our','when','their','what','about','here','one',
    'been','some','get','which','there','has','had','his','her','its','them',
    'then','than','also','into','more','would','could','should','very','like',
}

def _detect_hallucination(text):
    """Content word repeated >= 8x in last 50 words → probable ASR loop."""
    import collections
    lines = [l for l in text.splitlines()
             if not re.search(r'frame_\d+\.(jpg|png)|tutorials[/\\]frames', l, re.I)]
    words = re.findall(r'\b[a-z]+\b', ' '.join(lines).lower())
    if not words:
        return False, '', 0
    tail = [w for w in words[-50:] if w not in _STOP_WORDS]
    if not tail:
        return False, '', 0
    top_word, top_count = collections.Counter(tail).most_common(1)[0]
    return top_count >= 8, top_word, top_count

def run_safeguards(ch_transcripts):
    """
    Run all Step-1 ingest quality checks (transcript completeness + ASR hallucination).
    Returns (warnings, critical) — critical items mark extraction_status: needs-review.

    Frame-count validation is NOT done here: ingest.py no longer downloads video or
    extracts frames (deferred to select_frames.py, Step 2), so there's nothing to check
    yet at this point. See select_frames.py's own safeguard checks + append_safeguard_note()
    for the frame-capture-time equivalent.
    """
    warnings, critical = [], []
    total_chars = sum(len(ch.get('text', '')) for ch in ch_transcripts)

    # 1. Chapter transcript coverage
    for ch in ch_transcripts:
        text = ch.get('text', '').strip()
        name = ch.get('title', '?')
        if not text:
            critical.append(f"Empty transcript in chapter '{name}'")
        elif len(text) < 50:
            warnings.append(f"Very short transcript ({len(text)} chars) in '{name}'")

    # 2. Total transcript completeness
    if total_chars < 500:
        critical.append(
            f"Total transcript only {total_chars} chars (min 500). "
            "Captions unavailable or audio silent — extraction will be poor."
        )
    elif total_chars < 1200:
        warnings.append(
            f"Thin transcript: {total_chars} chars. "
            "Notes may be shallow — consider --whisper-model small."
        )

    # 3. ASR hallucination detection (per chapter)
    for ch in ch_transcripts:
        text = ch.get('text', '')
        if len(text) > 200:
            hallu, word, count = _detect_hallucination(text)
            if hallu:
                critical.append(
                    f"ASR hallucination in '{ch.get('title', '?')}': "
                    f"'{word}' x{count} in last 50 content words. "
                    "Review and truncate the affected section before extracting."
                )

    return warnings, critical

def _print_safeguard_report(warnings, critical):
    if not warnings and not critical:
        print("[SAFEGUARD] All checks passed")
        return
    print("[SAFEGUARD] Quality issues found:")
    for w in warnings:
        print(f"      WARNING  : {w}")
    for c in critical:
        print(f"      CRITICAL : {c}")
    if critical:
        print("      => extraction_status set to 'needs-review'")

def build_safeguard_section(warnings, critical):
    """
    Render the WARNING/CRITICAL findings as a markdown section. Returns "" if both
    lists are empty (clean ingests get no extra section — matches the console
    behavior of only speaking up when something's actually wrong).

    Persisting this into the .md file (not just printing to console) is what makes
    a `needs-review` flag auditable later — otherwise the *reason* a tutorial got
    flagged only ever existed in whatever terminal happened to be open at ingest time.
    """
    if not warnings and not critical:
        return ""
    lines = [
        "\n## Ingest Safeguard Report\n",
        "_Auto-generated at ingest/frame-capture time — explains why "
        "`extraction_status` may be `needs-review`. Safe to delete once reviewed._\n",
    ]
    for c in critical:
        lines.append(f"- **CRITICAL:** {c}")
    for w in warnings:
        lines.append(f"- WARNING: {w}")
    lines.append("\n---\n")
    return "\n".join(lines)

def append_safeguard_note(content, note, level="WARNING"):
    """
    Insert one more finding into an existing '## Ingest Safeguard Report' section,
    or create that section if this is the first finding for the file (e.g. Step 1's
    transcript checks were clean but Step 2's frame-capture check in select_frames.py
    found a problem). Shared by both ingest.py and select_frames.py so all quality-check
    reasoning ends up in one place inside the file, regardless of which step found it.
    """
    line = f"- **{level}:** {note}" if level == "CRITICAL" else f"- {level}: {note}"
    m = re.search(r"\n## Ingest Safeguard Report\n.*?\n---\n", content, re.DOTALL)
    if m:
        insertion_point = content.rindex("\n---\n", m.start(), m.end())
        return content[:insertion_point] + line + "\n" + content[insertion_point:]
    header = "## Raw Data (for Claude Code extraction)\n"
    idx = content.index(header) + len(header)
    section = (
        "\n## Ingest Safeguard Report\n\n"
        "_Auto-generated at ingest/frame-capture time — explains why "
        "`extraction_status` may be `needs-review`. Safe to delete once reviewed._\n\n"
        f"{line}\n\n---\n"
    )
    return content[:idx] + section + content[idx:]

# ── Epic documentation crawler ─────────────────────────────────────────────────

def fetch_page_text(url):
    """Fetch an Epic documentation page and return (title, sub_links, clean_text)."""
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return None, [], f"[Fetch error: {e}]"

    # Extract title
    tm = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    raw_title = tm.group(1).strip() if tm else url.split("/")[-1]
    title = raw_title.split(" | ")[0].strip()

    # Extract sub-page links — absolute and relative, all Epic doc path prefixes
    EPIC_BASE = "https://dev.epicgames.com"
    DOC_PAT   = r"(?:en-us/)?(?:unreal-engine|metahuman)"
    abs_links = re.findall(
        rf'href="(https://dev\.epicgames\.com/documentation/{DOC_PAT}/[^"?#]+)"',
        html
    )
    rel_links = re.findall(
        rf'href="(/documentation/{DOC_PAT}/[^"?#]+)"',
        html
    )
    all_links = abs_links + [EPIC_BASE + l for l in rel_links]
    sub_links = list(dict.fromkeys(l for l in all_links if l.rstrip("/") != url.rstrip("/")))

    # Extract readable text
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    html = re.sub(r"<style[^>]*>.*?</style>",  "", html, flags=re.DOTALL)
    html = re.sub(r"<nav[^>]*>.*?</nav>",       "", html, flags=re.DOTALL)
    html = re.sub(r"<header[^>]*>.*?</header>", "", html, flags=re.DOTALL)
    html = re.sub(r"<footer[^>]*>.*?</footer>", "", html, flags=re.DOTALL)
    html = re.sub(r"<[^>]+>", " ", html)
    html = re.sub(r"&nbsp;", " ", html)
    html = re.sub(r"&[a-z]+;", "", html)
    text = re.sub(r"\s+", " ", html).strip()

    # Trim to reasonable size (docs pages can be long)
    if len(text) > 12000:
        text = text[:12000] + "... [truncated]"

    return title, sub_links, text


def crawl_epic_docs(hub_url, max_depth=2):
    """
    BFS crawl of an Epic documentation hub page and its linked sub-pages.
    Returns list of (title, url, content) tuples in crawl order.
    """
    from collections import deque

    visited  = set()
    results  = []
    queue    = deque([(hub_url, 0)])

    while queue:
        url, depth = queue.popleft()
        clean_url = url.rstrip("/")
        if clean_url in visited or depth > max_depth:
            continue
        visited.add(clean_url)

        print(f"      [{len(results)+1}] depth={depth}  {url.split('/')[-1]}")
        title, sub_links, text = fetch_page_text(url)
        if title:
            results.append((title, url, text))

        if depth < max_depth:
            for link in sub_links:
                if link.rstrip("/") not in visited:
                    queue.append((link, depth + 1))

        time.sleep(CRAWL_DELAY)

    return results


def build_doc_md(hub_url, pages, slug):
    """Assemble crawled documentation pages into a single structured markdown file."""
    today = datetime.now().strftime("%Y-%m-%d")
    hub_title = pages[0][0] if pages else slug

    sections = ""
    for i, (title, url, content) in enumerate(pages):
        sections += f"\n### {title}\n"
        sections += f"**URL:** {url}\n\n"
        sections += f"{content}\n"

    return f"""---
title: {hub_title}
source: Epic Documentation
url: {hub_url}
ingested: {today}
ue_version: "[PENDING]"
tags: []
extraction_status: pending
page_count: {len(pages)}
---

# {hub_title}

**Source:** [Epic Documentation]({hub_url})
**Pages crawled:** {len(pages)}
**Ingested:** {today}

---

## Raw Documentation Content

{sections}

---

## Structured Notes

### Core Topics
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Concepts & Systems
[PENDING EXTRACTION]

### UE Systems / Settings / Code
[PENDING EXTRACTION]

### UE Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Entries
[PENDING EXTRACTION]
"""


def update_index_doc_pending(hub_url, hub_title, slug, filename, page_count):
    entry = f"""

### {hub_title}
- **Source:** Epic Documentation
- **URL:** {hub_url}
- **Pages:** {page_count}
- **UE Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/{filename}
"""
    content = INDEX_FILE.read_text(encoding="utf-8")
    if f"tutorials/{filename}" in content or hub_url in content:
        print(f"      INDEX.md already has an entry for {filename} — skipping (re-ingest will refresh the .md file but not duplicate the index)")
        return
    placeholder = "*(Empty — add your first entry by saying"
    if placeholder in content:
        content = re.sub(r"\*\(Empty[^)]+\)\*", entry.strip(), content)
    elif "\n---\n\n## Tag Reference" in content:
        content = content.replace("\n---\n\n## Tag Reference",
                                  f"{entry}\n---\n\n## Tag Reference")
    else:
        idx = content.rfind("\n---")
        content = content[:idx] + entry + content[idx:] if idx != -1 else content + entry
    INDEX_FILE.write_text(content, encoding="utf-8")

# ── YouTube: Build raw .md ─────────────────────────────────────────────────────

def build_raw_md(info, ch_transcripts, slug, frame_status="pending-selection",
                  sg_warnings=None, sg_critical=None):
    title    = info.get("title", "Unknown")
    url      = info.get("webpage_url", "")
    author   = info.get("uploader", "Unknown")
    today    = datetime.now().strftime("%Y-%m-%d")
    duration = info.get("duration", 0)
    dur_str  = f"{int(duration)//60}m{int(duration)%60}s" if duration else "unknown"

    # Chapter breakdown with per-sentence timestamped transcript.
    # No frames yet at this point — frame capture is Step 2 (content-aware,
    # see select_frames.py), not blind-timestamped here in Step 1.
    chapters_section = ""
    for ch in ch_transcripts:
        t_fmt = f"{int(ch.get('start',0))//60}:{int(ch.get('start',0))%60:02d}"
        chapters_section += f"\n### {ch['title']} [{t_fmt}]\n"
        segs = ch.get('segments') or []
        if segs:
            chapters_section += "**Transcript (timestamped):**\n"
            for t, txt in segs:
                if not txt:
                    continue
                mm, ss = int(t) // 60, int(t) % 60
                chapters_section += f"[{mm}:{ss:02d}] {txt}\n"
            chapters_section += "\n"
        elif ch.get("text"):
            chapters_section += f"**Transcript:** {ch['text']}\n\n"

    if frame_status == "skipped":
        frame_note = "Frame capture was skipped for this ingest (--skip-video). Text-only extraction."
    else:
        frame_note = (
            f"Frames are not captured yet. Read the timestamped transcript below, pick moments\n"
            f"that actually show a technique/result worth a still (not blind percentages —\n"
            f"even within a named chapter, verify the real moment against its timestamps), then run:\n"
            f"  python select_frames.py {slug} <ts1> <ts2> ...\n"
            f"(seconds or mm:ss). This appends a \"Captured Frames\" section and updates the\n"
            f"frontmatter before you write the Structured Notes below."
        )

    safeguard_section = build_safeguard_section(sg_warnings or [], sg_critical or [])

    return f"""---
title: {title}
source: YouTube
url: {url}
author: {author}
ingested: {today}
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/{slug}/
frame_count: 0
frame_status: {frame_status}
---

# {title}

**Source:** [YouTube]({url})
**Author:** {author}
**Duration:** {dur_str} | {len(ch_transcripts)} section(s)

---

## Raw Data (for Claude Code extraction)
{safeguard_section}
{frame_note}

{chapters_section}

---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### UE Systems / Blueprints / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### UE Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Entries
[PENDING EXTRACTION]
"""

def update_index_pending(info, slug, filename):
    title  = info.get("title", "Unknown")
    url    = info.get("webpage_url", "")
    author = info.get("uploader", "Unknown")
    entry = f"""

### {title}
- **Source:** YouTube
- **URL:** {url}
- **Author:** {author}
- **UE Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/{filename}
"""
    content = INDEX_FILE.read_text(encoding="utf-8")
    if f"tutorials/{filename}" in content or (url and url in content):
        print(f"      INDEX.md already has an entry for {filename} — skipping (re-ingest will refresh the .md file but not duplicate the index)")
        return
    placeholder = "*(Empty — add your first entry by saying"
    if placeholder in content:
        content = re.sub(r"\*\(Empty[^)]+\)\*", entry.strip(), content)
    elif "\n---\n\n## Tag Reference" in content:
        content = content.replace("\n---\n\n## Tag Reference",
                                  f"{entry}\n---\n\n## Tag Reference")
    else:
        idx = content.rfind("\n---")
        content = content[:idx] + entry + content[idx:] if idx != -1 else content + entry
    INDEX_FILE.write_text(content, encoding="utf-8")

# ── Epic community URL resolver ────────────────────────────────────────────────

def resolve_epic_community_url(url):
    """
    Epic community pages embed YouTube videos but block yt-dlp (Cloudflare + CSRF).
    Extract the slug, search YouTube for the first match, verify title+channel.

    WARNING: Search can return the wrong video. Verify the output box before continuing.
    If wrong, re-run with the correct YouTube URL or use --youtube-url.
    """
    from urllib.parse import urlparse
    path = urlparse(url).path.rstrip("/")
    segments = [s for s in path.split("/") if s]
    slug = segments[-1] if segments else ""
    if len(slug) < 10 and len(segments) >= 2:
        slug = segments[-2]
    search_terms = slug.replace("-", " ").strip()
    print(f"      Epic community URL detected.")
    print(f"      Searching YouTube for: {search_terms}")

    result = subprocess.run(
        [sys.executable, "-m", "yt_dlp",
         f"ytsearch1:{search_terms}",
         "--print", "%(id)s|||%(title)s|||%(uploader)s|||%(duration_string)s",
         "--skip-download", "--no-playlist", "--quiet"],
        capture_output=True, text=True
    )
    if result.returncode == 0 and result.stdout.strip():
        line   = result.stdout.strip().split("\n")[0]
        parts  = line.split("|||")
        vid_id = parts[0] if len(parts) > 0 else ""
        title  = parts[1] if len(parts) > 1 else "Unknown"
        chan   = parts[2] if len(parts) > 2 else "Unknown"
        dur    = parts[3] if len(parts) > 3 else "?"
        yt_url = f"https://www.youtube.com/watch?v={vid_id}"
        print(f"")
        print(f"      ┌─ EPIC COMMUNITY → YOUTUBE ────────────────────────────┐")
        print(f"      │ Title   : {title[:54]}")
        print(f"      │ Channel : {chan[:54]}")
        print(f"      │ Duration: {dur}")
        print(f"      │ URL     : {yt_url}")
        print(f"      └───────────────────────────────────────────────────────┘")
        print(f"      ⚠  Verify this is correct. Ctrl+C to cancel.")
        print(f"         Or re-run with: --youtube-url https://youtu.be/CORRECT_ID")
        print(f"")
        return yt_url
    raise RuntimeError(
        f"Could not find YouTube match. Search: '{search_terms}'\n"
        f"Pass the YouTube URL directly instead."
    )

# ── Main ───────────────────────────────────────────────────────────────────────

def find_duplicate_by_video_id(video_id, exclude_name):
    """Return the tutorial file that already references this YouTube video ID, if any.

    Slug/URL checks miss re-ingests where the uploader changed the title (new slug,
    new URL text) — the 11-char video ID is the stable identity, so search for it.
    """
    if not video_id:
        return None
    needle = f"v={video_id}"
    for f in TUTORIALS_DIR.glob("*.md"):
        if f.name in ("INDEX.md", exclude_name):
            continue
        try:
            if needle in f.read_text(encoding="utf-8", errors="ignore"):
                return f
        except OSError:
            continue
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Unreal Sidekick data collection (Step 1 of 2)"
    )
    parser.add_argument("url")
    parser.add_argument("--whisper-model", default=DEFAULT_WHISPER,
                        choices=["tiny", "base", "small", "medium", "large"])
    parser.add_argument("--skip-video", action="store_true",
                        help="Skip video download and frame extraction (YouTube)")
    parser.add_argument("--youtube-url", default=None,
                        help="Override Epic community URL auto-resolution with a known YouTube URL")
    parser.add_argument("--doc-depth", type=int, default=2,
                        choices=[0, 1, 2, 3],
                        help="Crawl depth for Epic documentation pages (default: 2)")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite an existing tutorial file even if extraction_status: complete")
    args = parser.parse_args()

    # ── Route: Epic documentation hub ────────────────────────────────────────
    is_epic_doc = (EPIC_DOC_HOST in args.url and
                   any(p in args.url for p in (
                       "/documentation/unreal-engine/",
                       "/documentation/en-us/unreal-engine/",
                       "/documentation/metahuman/",
                       "/documentation/en-us/metahuman/",
                   )))

    # ── Route: Epic community page → YouTube ─────────────────────────────────
    is_epic_community = (EPIC_DOC_HOST in args.url and "/community/" in args.url)

    if is_epic_community:
        if args.youtube_url:
            print("      Epic community URL detected — using provided YouTube override.")
            args.url = args.youtube_url
        else:
            args.url = resolve_epic_community_url(args.url)
        is_epic_doc = False

    if is_epic_doc:
        # ── Documentation crawl pipeline ─────────────────────────────────────
        print(f"[1/4] Detected Epic documentation hub.")
        print(f"      Crawling up to depth={args.doc_depth}...")
        pages = crawl_epic_docs(args.url, max_depth=args.doc_depth)
        if not pages:
            print("ERROR: No pages retrieved. Check the URL and try again.")
            sys.exit(1)

        hub_title = pages[0][0]
        slug      = slugify(hub_title)
        out_md    = TUTORIALS_DIR / f"{slug}.md"

        if out_md.exists() and not args.force and "extraction_status: complete" in out_md.read_text(encoding="utf-8"):
            print(f"      {out_md.name} is already fully extracted — refusing to overwrite.")
            print(f"      Pass --force to re-collect anyway (this will wipe the existing Structured Notes).")
            return

        print(f"\n[2/4] Crawled {len(pages)} pages. Assembling markdown...")

        md = build_doc_md(args.url, pages, slug)
        out_md.write_text(md, encoding="utf-8")
        print(f"[3/4] Updating INDEX.md...")
        update_index_doc_pending(args.url, hub_title, slug, out_md.name, len(pages))

        print(f"[4/4] Committing to GitHub...")
        os.chdir(SKILL_DIR)
        subprocess.run(["git", "add",
                        str(out_md.relative_to(SKILL_DIR)),
                        str(INDEX_FILE.relative_to(SKILL_DIR))], check=True)
        subprocess.run(["git", "commit", "-m", f"collect: {hub_title} ({len(pages)} pages)"],
                       check=True)
        subprocess.run(["git", "push"], check=True)

        print(f"\n{'='*60}")
        print(f"  Collection complete. Claude Code: run extraction now.")
        print(f"  Documentation file: tutorials/{out_md.name}")
        print(f"  Pages collected: {len(pages)}")
        print(f"{'='*60}\n")
        return

    # ── YouTube tutorial pipeline ─────────────────────────────────────────────
    has_ffmpeg, has_whisper = check_prerequisites()
    is_yt = "youtube.com" in args.url or "youtu.be" in args.url
    tmp   = Path(tempfile.mkdtemp())

    try:
        print("[1/4] Fetching metadata...")
        info = get_info(args.url) if is_yt else fetch_article(args.url)

        title    = info.get("title", "Unknown")
        chapters = info.get("chapters") or []
        duration = info.get("duration", 0)
        print(f"      {title}")
        print(f"      {len(chapters)} chapter(s), {int(duration//60)}m{int(duration)%60}s")

        slug      = slugify(title)
        out_md    = TUTORIALS_DIR / f"{slug}.md"

        if is_yt and not args.force:
            dup = find_duplicate_by_video_id(info.get("id", ""), out_md.name)
            if dup:
                print(f"      This video is already in the library under a different title:")
                print(f"        {dup.name}")
                print(f"      Skipping (same YouTube video ID). Pass --force to ingest anyway.")
                return

        if out_md.exists() and not args.force and "extraction_status: complete" in out_md.read_text(encoding="utf-8"):
            print(f"      {out_md.name} is already fully extracted — refusing to overwrite.")
            print(f"      Pass --force to re-collect anyway (this will wipe the existing Structured Notes).")
            return

        print(f"[2/4] Downloading audio + transcribing with Whisper ({args.whisper_model})...")
        ch_transcripts = []
        used_captions_fallback = False
        if is_yt:
            if has_whisper:
                try:
                    audio = download_audio(args.url, tmp)
                    transcript = whisper_transcribe(audio, args.whisper_model)
                    ch_transcripts = segment_by_chapters(transcript, chapters)
                    print(f"      {len(transcript.get('segments',[]))} segments -> {len(ch_transcripts)} sections")
                except Exception as e:
                    print(f"      Whisper failed ({e}), using yt-dlp captions")
                    used_captions_fallback = True
                    text = ytdlp_captions(args.url, tmp)
                    ch_transcripts = [{"title": "Full Content", "start": 0, "text": text, "segments": []}]
            else:
                print("      Whisper not installed — using yt-dlp captions")
                used_captions_fallback = True
                text = ytdlp_captions(args.url, tmp)
                ch_transcripts = [{"title": "Full Content", "start": 0, "text": text, "segments": []}]
        else:
            print("      Article — using page text")
            ch_transcripts = [{"title": "Full Content", "start": 0,
                               "text": info.get("description", ""), "segments": []}]

        # Frame capture is deferred to Step 2 (select_frames.py), driven by Claude
        # reading the timestamped transcript below — content-aware beats blind
        # percentage timestamps, and picking *which* moments matter needs judgment
        # this script deliberately doesn't have (no API calls made here).
        can_have_frames = is_yt and not args.skip_video and has_ffmpeg
        frame_status = "pending-selection" if can_have_frames else "skipped"
        if not can_have_frames:
            reason = "article" if not is_yt else ("--skip-video" if args.skip_video else "ffmpeg not found")
            print(f"[3/4] Frame capture skipped ({reason})")
        else:
            print("[3/4] Frame capture deferred to Step 2 (content-aware selection via select_frames.py)")

        # Safeguard checks — transcript completeness/hallucination only; frame-count
        # validation now happens in select_frames.py once real timestamps are chosen.
        sg_warnings, sg_critical = run_safeguards(ch_transcripts)
        if used_captions_fallback:
            sg_warnings.append('Transcript came from the yt-dlp captions fallback - NO per-sentence timestamps. Content-anchored frame selection (select_frames.py) will have to estimate moments; consider re-running ingest.py to retry Whisper before extracting.')
        _print_safeguard_report(sg_warnings, sg_critical)

        print("[4/4] Writing raw tutorial file...")
        md = build_raw_md(info, ch_transcripts, slug, frame_status, sg_warnings, sg_critical)
        if sg_critical:
            md = md.replace("extraction_status: pending", "extraction_status: needs-review", 1)
        out_md.write_text(md, encoding="utf-8")
        update_index_pending(info, slug, out_md.name)

        print("      Committing raw data to GitHub...")
        os.chdir(SKILL_DIR)
        subprocess.run(["git", "add",
                        str(out_md.relative_to(SKILL_DIR)),
                        str(INDEX_FILE.relative_to(SKILL_DIR))], check=True)
        subprocess.run(["git", "commit", "-m", f"collect: {title}"], check=True)
        subprocess.run(["git", "push"], check=True)

        print(f"\n{'='*60}")
        print(f"  Collection complete. Claude Code: run extraction now.")
        print(f"  Tutorial file: tutorials/{out_md.name}")
        if can_have_frames:
            print(f"  Next: read the timestamped transcript, then run")
            print(f"        python select_frames.py {slug} <ts1> <ts2> ...")
            print(f"        before writing Structured Notes.")
        else:
            print(f"  Frames:        none (text-only extraction)")
        print(f"{'='*60}\n")

    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def fetch_article(url):
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    html = re.sub(r"<style[^>]*>.*?</style>",  "", html, flags=re.DOTALL)
    html = re.sub(r"<[^>]+>", " ", html)
    html = re.sub(r"&[a-z]+;", " ", html)
    text = re.sub(r"\s+", " ", html).strip()
    tm   = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    title = tm.group(1).strip() if tm else url
    from urllib.parse import urlparse
    return {"title": title, "uploader": urlparse(url).netloc,
            "description": text[:8000], "duration": 0,
            "webpage_url": url, "chapters": []}


if __name__ == "__main__":
    main()
