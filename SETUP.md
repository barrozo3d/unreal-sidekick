# Unreal Sidekick — Setup

## For Claude: New Machine Setup Protocol

When the user says "set up this skill" or "new machine":

1. Check Python: `python --version` (need 3.9+)
2. Check yt-dlp: `python -m yt_dlp --version`
3. Check Whisper: `python -c "import whisper; print('ok')" 2>&1`
4. Check ffmpeg: `ffmpeg -version`
5. Check git: `git -C C:/Users/KABUM/.claude/skills/unreal-sidekick status`
6. Check GitHub remote: `git -C C:/Users/KABUM/.claude/skills/unreal-sidekick remote -v`
7. For anything missing: run `setup.ps1`

---

## Manual Setup (new machine)

### 1. Clone the repo
```powershell
git clone https://github.com/barrozo3d/unreal-sidekick C:/Users/KABUM/.claude/skills/unreal-sidekick
```

### 2. Install dependencies
```powershell
cd C:/Users/KABUM/.claude/skills/unreal-sidekick
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

If you get 429 / "Sign in to confirm" errors:

1. Install "Get cookies.txt LOCALLY" Chrome/Edge extension
2. Go to youtube.com while logged in
3. Export cookies → save as `cookies.txt` in the skill directory
4. Re-run ingest — it picks up cookies.txt automatically

---

## Ingest Commands

```powershell
# YouTube tutorial
python ingest.py "https://www.youtube.com/watch?v=..."

# Epic documentation section (crawls 2 levels deep)
python ingest.py "https://dev.epicgames.com/documentation/unreal-engine/..."

# Epic documentation — shallow crawl (1 level only)
python ingest.py "https://dev.epicgames.com/documentation/unreal-engine/..." --doc-depth 1

# Epic community talk (auto-resolves to YouTube)
python ingest.py "https://dev.epicgames.com/community/learning/..."

# Epic community — override if wrong YouTube video found
python ingest.py "https://dev.epicgames.com/community/..." --youtube-url "https://youtu.be/CORRECT_ID"

# YouTube — skip video download (text-only extraction)
python ingest.py "https://www.youtube.com/watch?v=..." --skip-video
```
