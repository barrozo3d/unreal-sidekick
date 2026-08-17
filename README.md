# Unreal Sidekick

An expert consultant skill for Unreal Engine cinematics, real-time VFX, and visual effects that also builds its own knowledge base by ingesting tutorials, and can optionally drive a real, running Unreal Editor session over MCP.

## What it does

Ask it Unreal Engine questions and it answers from a growing library of ingested tutorials plus Epic documentation, plus a hand-written reference knowledge base covering Sequencer/cinematics, Niagara VFX, Lumen/Nanite/rendering, Materials, Blueprints, the Python API, Chaos physics, MetaHuman, Control Rig, MetaSounds, nDisplay/ICVFX, and color/DaVinci pipeline handoff. It's tuned for a solo cinematic/narrative filmmaker's workflow (MetaHuman + mocap + Sequencer + Movie Render Graph), not general gameplay programming. It can also write Blueprint/HLSL/Python/Niagara code, and — optionally — execute commands directly in a running Unreal Editor via a Remote Control MCP server (spawn actors, run console commands, take viewport screenshots).

## Quick start

```powershell
git clone https://github.com/barrozo3d/unreal-sidekick.git "$HOME\.claude\skills\unreal-sidekick"
cd "$HOME\.claude\skills\unreal-sidekick"
.\setup.ps1
```

Then just ask Claude Code an Unreal Engine question — it reads `SKILL.md` automatically. Full setup and troubleshooting details live in `SETUP.md`.

## The Ingest Pipeline, in full detail

This is the part of the skill you'd actually touch to extend it: give it a video, an article, or any source of technical knowledge and the skill will trigger the steps to extract, read, organize, cross-reference and push it.

```
                         ┌─ YouTube tutorial ──────►  select_frames.py (Step 2) ─┐
ingest.py (Step 1,       │                                                       ├─►  Claude Code (Step 3: notes)  ─►  validate.py
routes by URL shape)  ───┤                                                       │
                         └─ Epic docs / community ──►  (no frames — skip Step 2) ─┘
```

Epic *community* pages (`dev.epicgames.com/community/...`) auto-resolve to their embedded YouTube video and then rejoin the YouTube path (frame capture applies). Epic *documentation* pages (`dev.epicgames.com/documentation/...`) never have frames — they go straight from Step 1 to Step 3.

### `ingest.py` — Step 1: data collection (no API calls)

| Function | What it does |
|---|---|
| `slugify(text)` | Turns a title into a filesystem-safe slug (`tutorials/<slug>.md`) — lowercases, strips punctuation, collapses whitespace to hyphens, caps at 80 chars. |
| `_ytdlp_cmd()` | Builds the base yt-dlp command. Defaults to forcing the `android` player client to dodge YouTube's "Sign in to confirm you're not a bot" 429s; switches to `cookies.txt`-based auth automatically if that file exists in the skill directory. |
| `check_prerequisites()` | Verifies `yt-dlp` is importable (hard requirement, exits if missing); detects whether `ffmpeg` and `whisper` are available (soft — pipeline degrades gracefully without them). |
| `get_info(url)` | Runs `yt-dlp --dump-json` and parses title, uploader, duration, chapters, video ID. |
| `WHISPER_VOCAB_HINT` | A domain-vocabulary string (Unreal Engine terms: Nanite, Lumen, Niagara, MetaHuman, Sequencer, Movie Render Graph, Control Rig, Chaos, Substrate, MegaLights, World Partition, PCG, etc.) fed to Whisper as an `initial_prompt` so it transcribes jargon correctly instead of mishearing it. |
| `_load_whisper_model(model_name)` | Loads (and caches) a Whisper model, suppressing the noisy first-download progress bar in favor of one clean notice. |
| `whisper_transcribe(audio_path, model_name)` | Runs Whisper transcription with the vocab hint applied. |
| `download_audio(url, tmp)` | Downloads and extracts audio as mp3 (one automatic retry on YouTube throttling failures). |
| `ytdlp_captions(url, tmp)` | Fallback path when Whisper isn't installed or transcription fails: pulls YouTube's own auto-captions and strips VTT markup down to plain text (no per-sentence timestamps in this path). |
| `segment_by_chapters(transcript, chapters)` | Buckets the transcript into per-chapter sections (or one "Full Content" section if the video has no chapters), preserving a per-sentence `(timestamp, text)` list per section — this is what lets Step 2 pick *content-anchored* frame moments instead of guessing blind percentages. |
| `download_video_low(url, tmp)` | Downloads the lowest-quality video stream available (reused by `select_frames.py` — frame pixels don't need to be high-res). |
| `extract_frames(video_path, timestamps, out_dir)` | Runs `ffmpeg -ss <t> -frames:v 1` per timestamp to grab exact stills. |
| `_detect_hallucination(text)` | ASR-hallucination guard: flags a chapter if one content word repeats ≥8 times in its last 50 words (a classic Whisper infinite-loop symptom). |
| `run_safeguards(ch_transcripts)` | Runs all Step-1 quality checks: per-chapter transcript emptiness/shortness, total-transcript-length thresholds (<500 chars = critical, <1200 = warning), and the hallucination check above. Returns `(warnings, critical)`. |
| `_print_safeguard_report(warnings, critical)` | Prints the warnings/criticals to the console in a fixed `[SAFEGUARD]` format. |
| `build_safeguard_section(warnings, critical)` / `append_safeguard_note(content, note, level)` | Render safeguard findings as a `## Ingest Safeguard Report` markdown block and persist it *inside* the tutorial file — so a `needs-review` flag stays auditable later instead of only ever existing in a terminal that's since closed. Shared by both `ingest.py` and `select_frames.py`. |
| `fetch_page_text(url)` | **Epic docs path.** Fetches one Epic documentation page, strips script/style/nav/header/footer tags, extracts its title and up to 12,000 chars of clean text, and collects every linked sub-page URL under `/documentation/unreal-engine/` or `/documentation/metahuman/`. |
| `crawl_epic_docs(hub_url, max_depth=2)` | **Epic docs path.** BFS crawl of a documentation hub page and its linked sub-pages (default depth 2, 0.4s delay between requests), returning `(title, url, content)` tuples in crawl order. |
| `build_doc_md(hub_url, pages, slug)` | **Epic docs path.** Assembles all crawled pages into one structured `tutorials/<slug>.md` file — frontmatter + a `## Raw Documentation Content` section per page + a `Structured Notes` skeleton of `[PENDING EXTRACTION]` markers. |
| `update_index_doc_pending(hub_url, hub_title, slug, filename, page_count)` | **Epic docs path.** Appends (or refuses to duplicate) a pending stub entry in `tutorials/INDEX.md` for a documentation hub — the doc-path counterpart to `update_index_pending()` below. |
| `resolve_epic_community_url(url)` | **Epic community path.** Epic's community pages embed YouTube videos but block yt-dlp directly (Cloudflare + CSRF) — extracts the page slug, searches YouTube for the best match, prints a verification box (title/channel/duration/URL) for the user to confirm, then hands off to the normal YouTube pipeline. |
| `build_raw_md(info, ch_transcripts, slug, frame_status, sg_warnings, sg_critical)` | **YouTube path.** Assembles `tutorials/<slug>.md`: YAML frontmatter (title/source/url/author/tags/`extraction_status`/`frame_status`) + the chapter-by-chapter timestamped transcript + a `Structured Notes` skeleton of `[PENDING EXTRACTION]` markers for Step 3 to fill in. |
| `update_index_pending(info, slug, filename)` | **YouTube path.** Appends (or refuses to duplicate) a pending stub entry in `tutorials/INDEX.md`. |
| `update_readme_tutorial_count()` | Recomputes the real on-disk tutorial count and rewrites this README's `**N tutorials ingested**` line — runs automatically at the end of every ingest (both paths) so the number never goes stale. |
| `find_duplicate_by_video_id(video_id, exclude_name)` | Dedup guard — searches existing tutorial files for the same 11-char YouTube video ID (catches re-ingests where the uploader renamed the video, which a slug/URL-only check would miss). |
| `fetch_article(url)` | Fallback for a non-YouTube, non-Epic URL passed into the YouTube-pipeline branch: fetches a plain HTML page, strips scripts/styles/tags, and extracts a title + up to 8000 chars of body text for text-only ingestion. |
| `main()` | Routes by URL shape (Epic documentation hub → doc-crawl pipeline; Epic community page → resolve to YouTube then fall through; everything else → YouTube/article pipeline), then within each path: collect → run safeguards → write the `.md` file → update `INDEX.md` and `README.md` → `git add` + `commit` + `push`. Flags: `--whisper-model {tiny,base,small,medium,large}`, `--skip-video` (YouTube only, permanently marks `frame_status: skipped`), `--doc-depth {0,1,2,3}` (Epic docs crawl depth, default 2), `--youtube-url` (override Epic-community auto-resolution), `--force` (overwrite even if `extraction_status: complete`). |

**Run it:** `python ingest.py "<url>"` from this skill's own directory.

### `select_frames.py` — Step 2: content-aware frame capture (YouTube tutorials only)

| Function | What it does |
|---|---|
| `parse_timestamp(raw)` | Accepts plain seconds (`"485"`) or `mm:ss` / `h:mm:ss` (`"8:05"`) — Claude picks these by hand after reading the timestamped transcript, not by blind percentage splits. |
| `read_frontmatter_field(content, key)` / `set_frontmatter_field(content, key, value)` | Regex-based YAML-frontmatter getter/setter used to read `frame_status`/`url` and write back `frame_count`/`frame_status`/`frame_selection`. |
| `main()` | Refuses to run on an Epic Documentation entry (no video/frames apply) or on an already-`complete`/`skipped` file unless `--force`; clears stale frames from a prior capture; downloads the low-quality video via `ingest.download_video_low()`; extracts the requested frames via `ingest.extract_frames()`; appends a `## Captured Frames` section; updates frontmatter. Does **not** commit — that happens together with the Structured Notes in Step 3. |

**Run it:** `python select_frames.py <slug> <ts1> <ts2> ...` (4-8 timestamps is typical) after reading the transcript in `tutorials/<slug>.md`.

### Step 3 — Extraction (done by Claude Code, not a script)

Claude reads each captured frame with the Read tool (YouTube tutorials only — Epic docs skip straight here from Step 1), identifies the viewport/panel/node-graph/Blueprint content shown, fills in every `[PENDING EXTRACTION]` marker in the Structured Notes (Core Technique/Core Topics, Summary, Key Steps, UE Systems/Blueprints/Settings/Code, Difficulty, UE Version, Tags), cross-links related tutorials sharing 2+ tags, updates the matching `INDEX.md` stub, sets `extraction_status: complete`, and commits `tutorials/<slug>.md` + `INDEX.md` together (`git commit -m "extract: [title]"`).

### `validate.py` — post-ingest integrity checker

| Function | What it does |
|---|---|
| `fail(msg)` | Records a failure message and prints it — the single sink every check below reports through. |
| `get_tutorial_files()` | Lists every `tutorials/*.md` file except `INDEX.md`. |
| `parse_index_refs()` | Extracts every `**File:** tutorials/...` reference out of `INDEX.md`. |
| `get_notes_content(content)` | Pulls the `## Structured Notes` section body out of a tutorial file. |
| `is_youtube_source(content)` / `parse_duration_secs(content)` | Read the `source:` frontmatter field and the `**Duration:**` line. |
| `get_transcript_text(content)` | Reconstructs the raw transcript text from the `## Raw Data` section (stripping out any `## Ingest Safeguard Report` box first, since that has its own `---` divider that would otherwise be mistaken for the section boundary). |
| `check_tutorials()` | Checks 1–4 and 8–10: no `[PENDING EXTRACTION]` markers, no `extraction_status: pending`, no `ue_version` PENDING placeholder, no empty `tags: []`, no `PLACEHOLDER` URLs, structured notes ≥200 chars for YouTube sources, and a transcript-length sanity check (≥3 chars/sec of runtime) for videos over 3 minutes. |
| `check_index()` | Checks 5–7: no duplicate `INDEX.md` entries, every disk file is indexed, no `INDEX.md` entry points at a missing file. |
| `check_script_drift()` | Cross-skill check (warn-only, never fails the run): compares this repo's shared helper functions (`slugify`, `download_audio`, `ytdlp_captions`, `segment_by_chapters`, `_detect_hallucination`, `append_safeguard_note`, `find_duplicate_by_video_id`) against the same functions in every sibling skill installed on the same machine, and warns if a copy has drifted — catching an intentional fix in one skill that never got ported to the others. |
| `main()` | Runs all checks, prints a pass/fail summary, exits 1 on any failure. |

**Run it:** `python validate.py` after a batch of ingests, or any time you want to sanity-check the library.

### Extending this pipeline

- **New source type** (e.g. a forum thread, a PDF): follow the `fetch_article()` pattern (plain-text fallback) or the `fetch_page_text()`/`crawl_epic_docs()` pattern (structured multi-page crawl) depending on whether it's a single page or a linked hub; feed the result through `build_raw_md()` or `build_doc_md()`.
- **New quality check**: add a check function inside `check_tutorials()`/`check_index()` in `validate.py`, following the existing `fail(msg)` pattern.
- **New safeguard**: add a check inside `run_safeguards()` in `ingest.py`, appending to `warnings`/`critical` — it'll automatically get persisted via `build_safeguard_section()`/`append_safeguard_note()`.
- **New reference file**: add `references/<topic>.md`, then add it to the table in `SKILL.md` → "Step 2 — Check Reference Files" so Claude knows when to reach for it.
- **New recipe file**: add `recipes/<pipeline-name>.md` for a multi-step, cross-system workflow (not a single-system reference), then add it to the table in `SKILL.md` → "Step 2b — Check Recipes".
- **Live connection to a running Unreal Editor**: see "Live connection" below — no pipeline code changes needed, it's a separate MCP layer.

---

## Every mode this skill supports

| Mode | Trigger phrases | What happens |
|---|---|---|
| **Setup** | "set up this skill", "new machine", "check if installed", "help me install" | Reads `SETUP.md` and follows the "For Claude: New Machine Setup Protocol" checklist (Python/yt-dlp/Whisper/ffmpeg/git/remote checks, runs `setup.ps1` for anything missing). |
| **Mode 1 — Consult / Answer** | "how do I", "what is", "what's the best way to", "explain", "why is", "help me with", "how does X work in Unreal" | Searches `tutorials/INDEX.md` (grepped by keyword/tag) + the 16 `references/*.md` files + `recipes/*.md` for multi-step pipeline questions, answers in the fixed Approach / Step-by-Step / Key Settings / Blueprint-HLSL-Python / Gotchas / Related-Entries format, citing sources. |
| **Mode 2 — Write Code** | "write me a blueprint", "material expression for", "niagara script for", "python script for", "give me the code", "HLSL for" | Writes Blueprint logic (described node-by-node, since there's no text format), Material HLSL (with target Custom Expression node noted), a Niagara module, or a Python editor script — directly. |
| **Mode 3 — Ingest** | "ingest", "learn from", "add this tutorial", "add this doc", "read this" | Runs the pipeline above unprompted through all steps — `ingest.py`, then `select_frames.py` if it's a YouTube tutorial, then Claude's own extraction pass. |
| **Mode 4 — Execute (UE Remote Control MCP)** | "create a", "spawn", "add to scene", "execute in unreal", "run this in UE", "take a viewport screenshot", "list all actors", "open this asset", "run console command" | Drives a real running Unreal Editor via the `unreal` or `unrealMCP` MCP tools (whichever is configured); for complex operations, writes Python and executes it via the Python execution tool; always confirms what changed and offers a viewport screenshot. If no MCP server is configured, tells the user to check `SETUP.md` → "UE Remote Control MCP Server". |

**Auto-Changelog Rule (Version Check):** at the start of every Mode 1 consultation, if `references/version-tracker.md`'s `last_checked` date is over 14 days old, the skill fetches Epic's release notes, checks for a version not yet tracked, and — if found — ingests its release notes into a new `references/release-notes-ueXX.md` and updates the tracker. Skipped if the user is clearly in a hurry.

## Live connection (optional)

`SKILL.md` documents Mode 4 — executing commands directly in a running Unreal Editor via a Remote Control MCP server. Two options, both documented in `SETUP.md` → "UE Remote Control MCP Server":

| Option | Setup | Tools | Notes |
|---|---|---|---|
| `runreal/unreal-mcp` | `npx`-installed Node.js MCP server; one-time UE setup enables the built-in Python Editor Script Plugin + Remote Execution — no custom plugin to build | List/search/export assets, execute Python in editor, create/update/delete actors, viewport screenshots, console commands, project/map info | **Recommended** — least setup, no C++ build required |
| `chongdashu/unreal-mcp` | Requires Visual Studio 2022 + a UE C++ project; clone the repo, copy its `UnrealMCP` plugin into the project, generate VS project files, build in `Development Editor` config, enable the plugin, then run its Python server | Create/delete/transform actors, query actor properties, create Blueprint classes, add components, configure physics, add event/function nodes, connect Blueprint graph pins, compile Blueprints | More setup, but the only option for graphical Blueprint graph editing (adding nodes, wiring pins) |

Neither is active by default. Claude checks and tells the user how to set one up if asked to execute something and no MCP server is configured.

## Repo structure

```
SKILL.md                 Main instructions Claude reads (modes, reference map, MCP setup pointers, tag pool)
SETUP.md                  Human + Claude setup guide, incl. UE Remote Control MCP options
README.md                  This file
CODE_OF_CONDUCT.md          Purpose/ethics statement — knowledge + consultation, not reproduction
KNOWLEDGE_GAPS_TODO.md        Tracked gaps in the knowledge base
batch_ingest.py                 Bulk-ingest helper
ingest.py                        Step 1 of the ingest pipeline (YouTube + Epic docs/community paths)
select_frames.py                  Step 2 of the ingest pipeline (YouTube tutorials only)
validate.py                        Post-ingest integrity checker + sibling-skill drift check
setup.ps1                           New-machine install script
requirements.txt                     Python dependencies
recipes/                              Multi-step pipeline guides (6 files: Blender-to-UE, MRQ EXR, MetaHuman-Sequencer-MRQ, Path Tracer/NFOR delivery, Sequencer Python batch render, full cinematics pipeline)
references/                           Hand-written Unreal Engine knowledge base (19 files: Niagara, Sequencer, rendering, materials, Blueprints, Python, Chaos, MetaHuman, nDisplay, MetaSounds, Control Rig, color pipeline, narrative Blueprints, lip-sync, plugin version notes, version tracker, release notes)
tutorials/                             Ingested tutorial/documentation library + INDEX.md (354 files)
```

## Sibling skills

Same ingest/validate/setup architecture as this skill's siblings — `blender-motion`, `houdini-wand`, `nuke-em-all`, and `paint-me-like-your-french-substances` — each covering a different DCC/VFX toolset. `validate.py`'s drift check compares shared pipeline internals across all five and warns (never fails) if a copy has drifted.

## Status

Public personal project, no warranty, not affiliated with or endorsed by Epic Games. **359 tutorials ingested** (count auto-updates on every `ingest.py` run — do not hand-edit this line).
