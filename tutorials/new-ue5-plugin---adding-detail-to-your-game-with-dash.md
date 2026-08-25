---
title: New UE5 Plugin - Adding Detail to Your Game with DASH
source: YouTube
url: https://www.youtube.com/watch?v=UO2ehs5OjEw
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.4
ue_version: "UE 5.x"
tags: [dash-1.4, game-environment, scatter, decals, physics, cable-tool, polyhaven, foliage, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/new-ue5-plugin---adding-detail-to-your-game-with-dash/
frame_count: 10
---

# New UE5 Plugin - Adding Detail to Your Game with DASH

**Source:** [YouTube](https://www.youtube.com/watch?v=UO2ehs5OjEw)
**Author:** Polygonflow Dash
**Duration:** 8m58s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted — see ingested file...]

---

## Structured Notes

### Core Technique
Josh Powers adds detail to a dystopian game environment — Megascans + Polyhaven props via Dash Content Library (Polyhaven integration "brand new"), Decal Scatter (multi-select + Ctrl+drag), Surface Scatter weeds with Proximity Mask (tree base), Convert Instances to Foliage (type `foliage` → manual foliage mode editing for edges), Physics Tool (trash bags → duplicate for piles), Cable Tool (static mesh anchors → type `cable` → connection rate/gravity/duplicates).

### Summary
9-minute game environment detailing tutorial by Josh Powers. Workflow: dystopian base scene with modular Megascans/custom pieces → Dash CB Megascans tab for props placement (drag+drop + hotkeys) → switch to Polyhaven tab (brand new feature: instantly access Polyhaven models/textures/HDRIs; auto-download on drag; resolution tabs on hover) → Shift+click multiple decals → Ctrl+drag → Scatter Here: Decal Scatter (min/max scale; similar decal sizes per scatter recommended) → Ctrl+drag weeds → Surface Scatter with Proximity Mask (select tree + add to proximity list → invert → adjust distance for growing-from-base effect) → type `foliage` → Convert Instances to Foliage (non-undoable; enables foliage mode brush for manual edge cleanup) → trash bags → Set Dynamic → Start → Duplicate for pile effect → Cable Tool (select anchor box meshes → type `cable` → add to object list → radius/duplicates/min-max gravity/connection rate → crowded cable bundle look).

### Key Steps
1. **Megascans Prop Placement** — Dash CB → Megascans tab → drag+drop → placement hotkeys (LMB=move, Ctrl+LMB=scale, Shift+LMB=rotate)
2. **Polyhaven Integration** — CB → click arrow → Polyhaven tab → drag asset → auto-download if needed → hover thumbnail = resolution tabs (choose resolution before download)
3. **Decal Scatter** — Shift+click multiple decals in CB → Ctrl+drag into scene → Scatter Here → adjust min/max scale (use similar-scale decals per scatter for consistency); OR single decal drag-and-drop = placement mode
4. **Surface Scatter with Proximity Mask** — Ctrl+drag weeds → Surface Scatter → Proximity Mask: select tree → add to proximity list → Invert → adjust distance → weeds grow outward from tree base; add other objects to proximity list for more coverage
5. **Convert Instances to Foliage** — type `foliage` in Dash prompt bar → Convert Instances to Foliage (non-undoable; commit only when satisfied) → now in Foliage Mode: brush add/remove for manual edge shaping
6. **Physics Tool — Trash Piles** — select trash bags → Physics Tool → Set Dynamic → Start (bags drop) → Duplicate selected → repeat for layered pile; random natural appearance
7. **Cable Tool** — place simple box meshes as anchor points on ceiling/walls → select all anchors → type `cable` → Cable Tool → add to object list → cables auto-generate between meshes → Adjust: radius, duplicates (strands per connection), min/max gravity, connection rate (extra connection points between cables for crowded look)

### UE Systems / Blueprints / Settings
- **Polyhaven integration** — "brand new feature" at time of recording; hover thumbnail = resolution tabs (1K/2K/4K); auto-PBR on drag; models/textures/HDRIs
- **Decal Scatter multi-select** — Shift+click assets in CB → Ctrl+drag → Scatter Here popup → full scatter settings; tip: use same-scale decals per scatter for consistent min/max scaling
- **Proximity Mask (invert)** — Proximity Mask field: add object(s) → Invert = exclude near object becomes include near object → Distance slider = radius of effect
- **Convert Instances to Foliage** — type `foliage` → non-undoable warning → confirms scatter → FoliageType created → editable in Foliage Mode with add/remove brushes; ideal for final edge detailing after scatter
- **Physics Tool (duplicate)** — Set Dynamic → Start → Duplicate (creates second batch above → re-simulates → natural stacking); repeatable for deep piles
- **Cable Tool** — static mesh anchors + type `cable` → object list; Radius (thickness), Duplicates (strands per pair), Min/Max Gravity (elevation spread), Connection Rate (extra mid-connection points for crowded look)

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.4)

### Tags
`#dash-1.4` `#game-environment` `#scatter` `#decals` `#physics` `#cable-tool` `#polyhaven` `#foliage` `#intermediate`

---

## Captured Frames

<!-- Timestamps RECOVERED 2026-08-25 by recover_moments.py, not chosen.
     ingest.py before c4decae picked blind-era moments deterministically;
     re-derived from the source's own chapter/duration metadata and
     accepted only because the count matched frame_count exactly.
     These are blind-era moments: legible and citable now, but not
     content-anchored. Re-selecting them is still a human call. -->

- [0:05] tutorials/frames/new-ue5-plugin---adding-detail-to-your-game-with-dash/frame_000.jpg
- [0:20] tutorials/frames/new-ue5-plugin---adding-detail-to-your-game-with-dash/frame_001.jpg
- [0:40] tutorials/frames/new-ue5-plugin---adding-detail-to-your-game-with-dash/frame_002.jpg
- [1:25] tutorials/frames/new-ue5-plugin---adding-detail-to-your-game-with-dash/frame_003.jpg
- [2:24] tutorials/frames/new-ue5-plugin---adding-detail-to-your-game-with-dash/frame_004.jpg
- [3:59] tutorials/frames/new-ue5-plugin---adding-detail-to-your-game-with-dash/frame_005.jpg
- [4:59] tutorials/frames/new-ue5-plugin---adding-detail-to-your-game-with-dash/frame_006.jpg
- [6:05] tutorials/frames/new-ue5-plugin---adding-detail-to-your-game-with-dash/frame_007.jpg
- [6:55] tutorials/frames/new-ue5-plugin---adding-detail-to-your-game-with-dash/frame_008.jpg
- [8:13] tutorials/frames/new-ue5-plugin---adding-detail-to-your-game-with-dash/frame_009.jpg

## Related Entries
- [[new-ue5-plugin---easy-environment-creation]] — Josh Powers earlier environment tutorial
- [[how-to-scatter-decals-in-ue5---world-building-plugin]] — Decal scatter dedicated tutorial (1.4)
- [[how-to-create-procedural-cables-in-ue5---world-building-plugin]] — Cable Tool dedicated tutorial (1.4)
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Surface Scatter masking deep-dive (1.4)
- [[new-physics-tool-for-unreal-engine-5]] — Physics Tool dedicated intro
