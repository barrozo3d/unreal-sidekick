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

# Re-collect a tutorial/doc-hub that was already fully extracted (overwrites Structured Notes)
python ingest.py "<url>" --force
```

`ingest.py` refuses to overwrite a tutorial or doc-hub `.md` whose frontmatter already has `extraction_status: complete`, to protect hand-written Structured Notes from being wiped by an accidental re-ingest. Pass `--force` only when you intend to discard the existing extraction and will re-run the extraction pass afterward.
