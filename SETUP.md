# Unreal Sidekick — Setup

## For Claude: New Machine Setup Protocol

When the user says "set up this skill" or "new machine":

1. Check Python: `python --version` (need 3.9+)
2. Check yt-dlp: `python -m yt_dlp --version`
3. Check Whisper: `python -c "import whisper; print('ok')" 2>&1`
4. Check ffmpeg: `ffmpeg -version`
5. Check git: `git -C %USERPROFILE%/.claude/skills/unreal-sidekick status`
6. Check GitHub remote: `git -C %USERPROFILE%/.claude/skills/unreal-sidekick remote -v`
7. For anything missing: run `setup.ps1`

---

## Manual Setup (new machine)

### 1. Clone the repo
```powershell
git clone https://github.com/barrozo3d/unreal-sidekick %USERPROFILE%/.claude/skills/unreal-sidekick
```

### 2. Install dependencies
```powershell
cd %USERPROFILE%/.claude/skills/unreal-sidekick
pip install -r requirements.txt
```

### 3. Install ffmpeg (for frame extraction)
```powershell
winget install ffmpeg
# or: choco install ffmpeg
```

### 4. Verify
```powershell
python ingest.py --help
```

---

## YouTube Bot Detection Fix

As of 2026-08, `ingest.py` automatically passes `--extractor-args youtube:player_client=android` whenever `cookies.txt` isn't present, since YouTube's default `web_safari` client started throwing HTTP 429 + "Sign in to confirm you're not a bot" on many videos. No setup needed — built into `_ytdlp_cmd()`.

If a video still fails under the android client (rare — mainly age-restricted/region-locked videos):

1. Install "Get cookies.txt LOCALLY" Chrome/Edge extension
2. Go to youtube.com while logged in
3. Export cookies → save as `cookies.txt` in the skill directory
4. Re-run ingest — it picks up cookies.txt automatically (and drops the android-client arg)

---

## UE Remote Control MCP Server (Mode 4)

Enables Claude to execute commands directly in an open Unreal Editor via MCP. Two options — choose based on your needs.

### Option A: runreal/unreal-mcp (Recommended — no custom plugin needed)

**Requires:** Node.js 18+ and UE Python Remote Execution

**One-time UE setup:**
1. `Edit → Plugins → search "Python Editor Script Plugin" → Enable → Restart`
2. `Edit → Project Settings → Plugins → Python → Enable Remote Execution ✓`
3. Set Remote Execution Multicast Group IP: `239.0.0.1` (default is fine)

**Claude Code config** — add to `%USERPROFILE%\.config\claude-desktop\mcp.json`:
```json
{
  "mcpServers": {
    "unreal": {
      "command": "npx",
      "args": ["-y", "@runreal/unreal-mcp"]
    }
  }
}
```

**Available tools:** list/search/export assets, execute Python in editor, create/update/delete actors, viewport screenshots, console commands, project and map info.

**Verify:** With UE open, say "unreal: take a viewport screenshot" in Claude Code.

---

### Option B: chongdashu/unreal-mcp (More features — Blueprint graph editing)

**Requires:** Visual Studio 2022, UE C++ project

**One-time setup:**
```powershell
git clone https://github.com/chongdashu/unreal-mcp
```
1. Copy `MCPGameProject/Plugins/UnrealMCP` → your project's `Plugins/` folder
2. Right-click `.uproject` → Generate Visual Studio project files
3. Build: `Development Editor` configuration
4. In UE: `Edit → Plugins → search "UnrealMCP" → Enable → Restart`
5. Start server: `uv --directory <path/to/unreal-mcp/Python> run unreal_mcp_server.py`

**Claude Code config:**
```json
{
  "mcpServers": {
    "unrealMCP": {
      "command": "uv",
      "args": ["--directory", "<path/to/unreal-mcp/Python>", "run", "unreal_mcp_server.py"]
    }
  }
}
```

**Available tools:** Create/delete/transform actors, query actor properties, create Blueprint classes, add components, configure physics, add event/function nodes, connect Blueprint graph pins, compile Blueprints, spawn actors.

**Use Option B if:** you need Claude to build Blueprints graphically (add nodes, wire pins).  
**Use Option A if:** you want to execute Python scripts and manage assets with minimal setup.

---

## Ingest Commands

The pipeline is two scripts, run in sequence — frame capture is a deliberate,
content-aware step done by Claude Code, not something either script guesses
at. Step 1 never downloads video or extracts frames anymore; it only collects
transcript/metadata (or crawled doc text) and pushes a pending stub.

```powershell
# Step 1 — YouTube tutorial (transcript only, no video/frames yet)
python ingest.py "https://www.youtube.com/watch?v=..."

# Step 1 — Epic documentation section (crawls 2 levels deep, no frames needed)
python ingest.py "https://dev.epicgames.com/documentation/unreal-engine/..."

# Step 1 — Epic documentation — shallow crawl (1 level only)
python ingest.py "https://dev.epicgames.com/documentation/unreal-engine/..." --doc-depth 1

# Step 1 — Epic community talk (auto-resolves to YouTube)
python ingest.py "https://dev.epicgames.com/community/learning/..."

# Step 1 — Epic community — override if wrong YouTube video found
python ingest.py "https://dev.epicgames.com/community/..." --youtube-url "https://youtu.be/CORRECT_ID"

# Step 1 — YouTube — mark as permanently frame-less (text-only extraction, skips Step 2 entirely)
python ingest.py "https://www.youtube.com/watch?v=..." --skip-video

# Step 1 — Re-collect a tutorial/doc-hub that was already fully extracted (overwrites Structured Notes)
python ingest.py "<url>" --force

# Step 2 — YouTube tutorials only: after reading the timestamped transcript, capture the chosen moments
python select_frames.py <slug> <ts1> <ts2> ...   seconds or mm:ss, e.g. 10 60 4:20 8:05
python select_frames.py <slug> ... --force       re-capture even if frame_status: complete
```

`ingest.py` refuses to overwrite a tutorial or doc-hub `.md` whose frontmatter already has `extraction_status: complete`, to protect hand-written Structured Notes from being wiped by an accidental re-ingest. Pass `--force` only when you intend to discard the existing extraction and will re-run the extraction pass afterward. `select_frames.py` has the same guard on `frame_status: complete`. Epic documentation pages have no video/frames at all — skip Step 2 for those and go straight to extraction.

## Frame capture height (`INGEST_FRAME_HEIGHT`)

Frames are captured at **720p** in this skill (viewport/result-led content more often than parameter-pane-led), set by
`DEFAULT_FRAME_HEIGHT` at the top of `ingest.py`. The value is per-skill on
purpose: `download_video_low()` itself is drift-gated across all five skills, so
its source stays identical while only the constant changes.

Raise or lower it for a single run without editing anything:

```
# PowerShell
$env:INGEST_FRAME_HEIGHT = "1080"; python ingest.py <url>
# bash
INGEST_FRAME_HEIGHT=1080 python ingest.py <url>
```

Why it matters: frames are how a claim gets checked against what was actually on
screen, and text that cannot be read cannot settle anything. Frames below **480p**
count as blind-era and `reground_frames.py` treats them as needing re-capture.
Raise this when a tutorial is a UI-heavy screencast and lower it only if disk or
bandwidth genuinely bites — the cap exists for download cost, not quality.

> This variable existed for weeks before being documented here, and so defaulted
> to 720p everywhere by accident. Per the Setup Sync Rule at the top of this
> file, a new environment variable must be added here in the same change.

## Note: captured frames are local-only

`tutorials/frames/` is gitignored — frame images never sync to GitHub. On a fresh
clone, `frame_status: complete` in a tutorial's frontmatter refers to frames that
existed on the machine that ingested it; the durable knowledge is the extracted
Structured Notes, not the images. If you need the stills again on this machine,
re-capture them with:

```
python select_frames.py <slug> <ts1> <ts2> ... --force
```

(timestamps are listed in the tutorial file's "Captured Frames" section).
