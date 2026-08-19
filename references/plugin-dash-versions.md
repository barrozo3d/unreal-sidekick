---
class: topic-reference
verified: no
sources:
  - https://docs.polygonflow.io
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# Polygonflow Dash — Version History & Compatibility Reference

**Plugin:** Dash (World Building & Asset Management for UE5)
**Developer:** Polygonflow
**Store:** Fab.com + free tier (Dash Advanced Asset Manager)
**Docs:** https://docs.polygonflow.io
**Platform:** Windows only (all versions)
**UE Compatibility:** UE5+ (specific version notes per release below)

---

## Version Compatibility Matrix

| Dash Version | UE Min | UE Max (known) | Notes |
|---|---|---|---|
| 1.7.0 | UE 5.x | UE 5.3 | First version with Vines Tool + Blend Material |
| 1.8.0 | UE 5.x | UE 5.4 | UI overhaul; UE 5.5 preview support added |
| 1.8.5 | UE 5.x | UE 5.5 | FAB support added; Data Tables experimental |
| 1.9.0 | UE 5.x | UE 5.5 | Free Content Browser released |
| 1.9.1 | UE 5.x | **UE 5.6** | Hotfix adding UE 5.6 support |
| 1.9.2 | UE 5.x | UE 5.6 | New tools + Amazon 3D Library integration |
| 1.9.3 | UE 5.x | UE 5.6 | New Asset Marketplace |
| 1.10.0 | UE 5.x | UE 5.6 | Preset system; requires 5.4+ for Tiling Y fix |
| 1.11.0 | UE 5.x | UE 5.6+ | Drawable presets; 50+ built-in presets |
| 1.12.0 | UE 5.x | **UE 5.8** | Vine/Cable/Grid Scatter scatter-integration; Camera Tool V2; new Vertical Stack tool; Debounce execution mode |

> **Compatibility rule:** Always check the Dash version shown in a tutorial against this table. Features from 1.8+ (Data Tables, FAB support) won't exist in older installs. Preset system (save/share setups) requires 1.10+. Drawable viewport presets require 1.11+.

---

## Release Notes

### Dash 1.12.0
**Theme:** "Improved UE5 world building tools" — deeper scatter integration + performance

**New Features:**
- **UE 5.8 support** — early support, may have bugs; report issues upstream
- **Vine Tool + Scattered Surfaces** — assign a scatter as an additional surface; vines grow naturally onto scattered meshes
- **Cable Tool Scatter Mode** — cables now generate between scattered objects (scatter as input); UI cleaned up, irrelevant controls auto-hide per mode
- **Grid Scatter Projection** — 2D grid scatters can now conform/project onto uneven terrain while keeping grid structure
- **Placement Tools** — new one-click **Placing Grid** and **Placing Circle** actions to auto-organize selected meshes
- **Camera Tool V2** — unlocks native CineCameraActor focus controls in-panel; all Dash camera settings (custom + native) now Sequencer-animatable
- **Vertical Stack Tool (new)** — auto-generates bottom/middle/top prop stacks with jitter/random removal/offset controls
- **Debounce Execution Mode (new)** — alternative to default Runtime mode; waits ~100ms (adjustable in preferences) after edits stop before updating, for better performance in heavy scenes
- **Scatter Table Dropdown** — expand a multi-mesh slot to inspect/select/remove individual meshes without a full rebuild
- **Window Persistence** — Dash tool windows remember size/position across sessions

---

### Dash 1.11.0 (Released ~May 2026)
**Theme:** "Drawable presets, new presets and a faster, more flexible Content Browser"

**New Features:**
- **Drawable Presets** — hold `Ctrl + Drag` to draw presets directly in viewport; works for surface scatter, curve-based tools (Path Scatter, Cable Tool, Quick Pipe, Road Tool), and compound presets
- **18 new built-in presets** (total: 50+ presets); covers fences, forests, pathways
- **Instant Asset Access** — new compute option adds project assets without waiting for thumbnail rendering (uses default UE thumbnails instead)
- **Content Browser Filters** — quick filter by asset type (materials, meshes, blueprints) integrated into search bar

**Bug Fixes:**
- Fixed fullscreen crash in Play Mode with Tools Panel open
- Fixed Quixel and Poly Haven material resolution application
- Fixed Content Browser preference shortcuts
- Fixed custom tool name truncation
- Improved FAB texture clarity at angles

---

### Dash 1.10.0 (Released ~March 2026)
**Theme:** "Build it once. Use it everywhere"

**New Features:**
- **Preset System** — save any Dash setup (tool settings + input meshes) as a reusable preset; browse and drag-and-drop from Preset Library in Content Browser
- **30+ built-in presets** — single-tool to advanced Compound setups; designed as practical starting points and instructional examples
- **Redesigned Compounds** — connect multiple Dash tools and control from single interface; expose only essential parameters

**Tool Enhancements:**
- Physics Paint: added Min/Max Scale controls for variable natural asset sizing
- Path Scatter: Actor support (Decals + Blueprints, experimental), "Every Other Offset" for footprint decals, rotation/scale inheritance from source meshes

**Bug Fixes:**
- Fixed Tiling Y property compatibility with **UE 5.4+**
- Fixed Quick Pipe tool renaming
- Fixed proximity mask inversion persistence
- Fixed billboard/corrupt mesh issues with FAB assets

---

### Dash 1.9.3
**New:** Asset Marketplace directly inside Dash

---

### Dash 1.9.2
**New:** New UE5 tools + Amazon 3D Library integration

---

### Dash 1.9.1 (Hotfix)
**Critical:** Added **UE 5.6 support**

---

### Dash 1.9.0
**Theme:** Content Browser goes free; major asset management overhaul

**New Features:**
- **Free Content Browser** — Megascans, FAB, Poly Haven, IES assets; browseable, searchable, drag-and-drop across all UE5 projects (no paid subscription needed)
- **Collection System** — organize assets into private or shared team collections
- **Semantic / AI Search** — finds conceptually similar items; fuzzy matching; boolean operators (+ and -)
- **Advanced Water Shader** — waves, underwater effects, rain-on-water simulation
- **Falling Leaves system** — forest/park/urban scenes
- **Runtime Virtual Texture (RVT)** workflow support
- Blueprint support in Content Browser (browseable + searchable mesh BPs)
- Multi-asset picker: `Ctrl+Drop` for selecting variations
- Quick Asset Search mini-browser accessible from Dash bar
- Materials AI tagging enabled by default (opt-out available)

**Important:** Must uninstall previous Dash version before upgrading to 1.9.

---

### Dash 1.8.5 (Official)
**Theme:** FAB integration + Sophon AI + Data Tables

**New Features:**
- **FAB Support** — assets downloaded via FAB plugin appear in Dash Content Browser; supports Megascans, FBX, GLT (Material Edit + Blend Material work with Megascans only, not other FAB formats yet)
- **Data Tables (Experimental)** — layering system for stacking multiple effects; supports Proximity Masking, Landscape Layer Masking, Noise Masks, Terrain Curves
- **Sophon AI Assistant** (revamped from 1.8) — improved accuracy, direct tool suggestions, better docs links, extended conversations
- **Terrain Deformation Enhancements** — curve-based deformation with falloff + tapering; experimental height map support
- **Proximity Width** — strip of objects without multiple masks
- **Texture Repetition Breakup** — "Enable BreakUp Tiling" in Material Edit + Blend Material
- **Incremental Spin** — ordered rotation (e.g. "0 90") for scatter objects
- **Simplified Baking** — one-click convert instances to static meshes

**Breaking Change:** Surface Scatter Density now operates in Global Mode exclusively; density values typically exceed 1 now.

**Bug Fixes:**
- Physics tools no longer affected by UE volumes/regions
- Physics Paint controls work consistently after engine restart
- Tool names aligned with Outliner nomenclature

---

### Dash 1.8.0
**Theme:** UI overhaul + path tools redesign + AI documentation

**New Features:**
- **Revamped UI** — split into distinct menus; recent actions + favorites tracking
- **Tools Panel** — unified panel; pin, detach, rename, scroll active tools
- **Path-Based Tools redesign** — Road Tool, Quick Pipe, Decal Scatter, Path Scatter completely redesigned; noise for terrain variation; path width controls
- **Blend Material** — rain and snow effects; improved blending
- **Surface Scatter** — pivot mode options; directional masking (sunlight-based); scale influence controls
- **Dash Board Tool (Beta)** — reference image organization (Miro/PureRef-style) inside UE5
- **Compound Tool** — manage complex multi-tool setups
- **AI Tagging** — doubled quotas; custom OpenAI API key support; improved quality
- UE 5.5 preview support

---

### Dash 1.7.0
**Theme:** Vines + AI tagging + IES + Color Grading

**New Features:**
- **Vines Creation Tool** — auto-generates vines on selected surfaces; drag-and-drop Megascans atlas textures for auto-conversion to mesh cards
- **AI Tagging (GPT-4o)** — replaces open-source models; monthly caps: 800 (students) / 2,000 (professionals) / 10,000 (studios); user data NOT retained for training
- **Reference Properties** — unified system replacing variables; control properties across multiple Dash tools simultaneously
- **IES Profiles Library** — direct access to ieslibrary.com profiles inside Dash
- **Image to Grading** — drag-and-drop color grading from local images or URLs
- **Fog Cards 2.0** — improved lighting + animation controls
- **Blend Material tool** — multi-surface composition
- **Landscape Layer Masking** for Surface Scatter
- **Volume Scatter** — fill objects with other objects
- Performance: curve masking 10× faster

**Workflow Change:** Save file structure moved to level data for collaborative workflows (team-friendly)

---

## How to Cross-Reference Tutorials

When extracting a Dash tutorial:
1. Identify which Dash version is shown (look for version badge in UI, title, or transcript)
2. Note the UE version used
3. Flag any features that were introduced in a later version (e.g. a tutorial showing Presets needs 1.10+)
4. Add compatibility warning if the feature shown was changed/fixed in a later version

**Key compatibility flags to add in extraction:**
- `dash-1.7+` — Vines, IES Library, Blend Material
- `dash-1.8+` — Data Tables (experimental), Sophon AI, FAB support
- `dash-1.9+` — Free Content Browser, Advanced Water Shader, AI Search
- `dash-1.10+` — Preset System (save/share setups)
- `dash-1.11+` — Drawable Presets (Ctrl+Drag in viewport)
- `dash-1.12+` — Vine/Cable Tool scattered-surface integration, Grid Scatter projection, Camera Tool V2 (native focus + Sequencer), Vertical Stack Tool, Debounce execution mode
