# Unreal Sidekick

A Claude Code skill: an expert consultant for Unreal Engine cinematics, real-time VFX, and visual effects that also builds its own knowledge base by ingesting tutorials, and can optionally drive a real, running Unreal Editor session over MCP.

## What it does

Ask it Unreal Engine questions and it answers from a growing library of ingested tutorials plus Epic documentation, plus a hand-written reference knowledge base covering Sequencer/cinematics, Niagara VFX, Lumen/Nanite/rendering, Materials, Blueprints, the Python API, Chaos physics, MetaHuman, Control Rig, MetaSounds, nDisplay/ICVFX, and color/DaVinci pipeline handoff. It's tuned for a solo cinematic/narrative filmmaker's workflow (MetaHuman + mocap + Sequencer + Movie Render Graph), not general gameplay programming. It can also write Blueprint/HLSL/Python/Niagara code, and — optionally — execute commands directly in a running Unreal Editor via a Remote Control MCP server (spawn actors, run console commands, take viewport screenshots). Its library currently holds 354 ingested tutorial/documentation files.

## Quick start

```powershell
git clone https://github.com/barrozo3d/unreal-sidekick.git "$HOME\.claude\skills\unreal-sidekick"
cd "$HOME\.claude\skills\unreal-sidekick"
.\setup.ps1
```

Then just ask Claude Code an Unreal Engine question — it reads `SKILL.md` automatically. Full setup and troubleshooting details live in `SETUP.md`.

## How it works

**Consulting.** Every question is answered against `tutorials/INDEX.md` (the ingested-tutorial/documentation library, grepped by keyword/tag rather than read top to bottom) plus `references/*.md` files covering Niagara VFX, Sequencer/cinematics, rendering (Lumen/Nanite/Path Tracing/TSR), materials/shaders, Blueprints, the Python API, Chaos physics, MetaHuman, nDisplay/ICVFX, MetaSounds, Control Rig, color pipeline, narrative Blueprints, lip-sync, plugin version notes, and a version tracker — plus multi-step `recipes/*.md` for full pipeline questions (e.g. Blender-to-UE, MRQ multi-pass EXR, MetaHuman-to-Sequencer-to-MRQ). See `SKILL.md` for the full reference-file map and answer format.

**Growing the library.** Say "ingest this: [URL]" and a three-step pipeline runs:
1. `ingest.py` — for YouTube tutorials, pulls audio and transcribes it with Whisper (per-sentence timestamps preserved); for Epic documentation pages, crawls the hub page and linked sub-pages up to 2 levels deep into one structured file. No video download, no frames yet.
2. `select_frames.py` — Claude reads the timestamped transcript, picks 4-8 moments that actually show a technique worth a still, and this script captures just those frames (YouTube tutorials only; Epic docs skip this step).
3. Claude reads the captured frames and transcript, writes structured notes (technique, steps, settings/code, tags), cross-links related entries, and commits everything to this repo.

`validate.py` is a post-ingest integrity checker (no `[PENDING EXTRACTION]` leftovers, no broken INDEX cross-references, transcripts long enough to be real, no placeholder URLs) — run `python validate.py` after a batch of ingests. It also warns (never fails) if the shared ingest-pipeline internals have drifted from its sibling skills.

**Live connection (optional).** `SKILL.md` documents Mode 4 — executing commands directly in a running Unreal Editor via a Remote Control MCP server. Two options are documented in `SETUP.md` → "UE Remote Control MCP Server": `runreal/unreal-mcp` (recommended, no custom plugin, uses UE's built-in Python Remote Execution) for asset listing/export, Python execution, actor CRUD, and viewport screenshots; or `chongdashu/unreal-mcp` (more setup, requires a C++ plugin and Visual Studio) for graphical Blueprint graph editing. Neither is active by default — Claude checks and tells the user how to set one up if asked to execute something and no MCP server is configured.

## Repo structure

```
SKILL.md                 Main instructions Claude reads (modes, reference map, MCP setup pointers, tag pool)
SETUP.md                  Human + Claude setup guide, incl. UE Remote Control MCP options
README.md                  This file
KNOWLEDGE_GAPS_TODO.md      Tracked gaps in the knowledge base
batch_ingest.py             Bulk-ingest helper
ingest.py                    Step 1 of the ingest pipeline
select_frames.py             Step 2 of the ingest pipeline
validate.py                   Post-ingest integrity checker + sibling-skill drift check
setup.ps1                      New-machine install script
requirements.txt                Python dependencies
recipes/                         Multi-step pipeline guides (6 files: Blender-to-UE, MRQ EXR, MetaHuman-Sequencer-MRQ, Path Tracer/NFOR delivery, Sequencer Python batch render, full cinematics pipeline)
references/                       Hand-written Unreal Engine knowledge base (19 files: Niagara, Sequencer, rendering, materials, Blueprints, Python, Chaos, MetaHuman, nDisplay, MetaSounds, Control Rig, color pipeline, narrative Blueprints, lip-sync, plugin version notes, version tracker, release notes)
tutorials/                         Ingested tutorial/documentation library + INDEX.md (354 files)
```

## Sibling skills

Same ingest/validate/setup architecture as this skill's siblings — `blender-motion`, `houdini-wand`, `nuke-em-all`, and `paint-me-like-your-french-substances` — each covering a different DCC/VFX toolset. `validate.py`'s drift check compares shared pipeline internals across all five and warns (never fails) if a copy has drifted.

## Status

Public personal project, no warranty, not affiliated with or endorsed by Epic Games. 354 tutorials/documentation files ingested as of 2026-08-12.
