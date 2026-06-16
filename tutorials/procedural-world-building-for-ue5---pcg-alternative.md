---
title: PROCEDURAL WORLD BUILDING FOR UE5 - PCG ALTERNATIVE
source: YouTube
url: https://www.youtube.com/watch?v=KsgW-19y4ts
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.7
ue_version: "UE 5.x"
tags: [dash-1.7, environment, scatter, path-scatter, grid-scatter, radial-scatter, decals, property-references, compound-tool, tool-presets, procedural, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/procedural-world-building-for-ue5---pcg-alternative/
frame_count: 10
---

# PROCEDURAL WORLD BUILDING FOR UE5 - PCG ALTERNATIVE

**Source:** [YouTube](https://www.youtube.com/watch?v=KsgW-19y4ts)
**Author:** Polygonflow Dash
**Duration:** 29m24s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted — see ingested file...]

---

## Structured Notes

### Core Technique
29-minute comprehensive overview of all Dash procedural scatter tools as a node-free PCG alternative — Surface Scatter (density/scale/masking/noise), Path Scatter (density modes/pivot/parallel curves), Grid Scatter (3D/height division/remove below origin/proximity), Radial Scatter (radius/height/concentric rings/spiral/square mode), Decal Scatter, Reference Tool (shared properties), Compound Tool (grouped tool parameters), Merge Actors, Tool Presets.

### Summary
28-minute beginner-to-intermediate PCG alternative overview. Covers all major Dash scatter tools: (1) Surface Scatter — Ctrl+drag → Scatter on Selection; density; scale; Noise Mask (pattern/frequency/invert); Proximity Mask (distance/falloff; curve as mask); Color Texture Mask. (2) Path Scatter — type `create curve`/`draw curve` for spline; add to Path Scatter; density modes (per-point or exact count); pivot offset/path smoothness; parallel curves. (3) Grid Scatter — 3D distribution mode (X/Y/Z stacking); Height Division for Z layers; remove-below-origin; Proximity Mask carving; Random Remove; Random Spin + Jitter; stone fence ruin example. (4) Radial Scatter — radius/start angle/height/concentric rings; ring height for Z stacking; min/max concentric distance = tower by stacking rings; square shaping mode; scale variation. (5) Decal Scatter — multi-select + Ctrl+drag → Scatter Here; depth control; masking; rotation. (6) Reference Tool — Convert value to Reference → name it → assign same reference to other tool parameters → one Reference Tool slider controls all linked values. (7) Compound Tool — drag scatter tools into Compound → exposes only desired parameter controls in one panel; share compound presets. (8) Merge Actors — type `merge` → combines multiple static meshes + scatter instances into single mesh → appears in CB → drag to scene for reuse. (9) Tool Presets — save scatter config as preset → apply to new scatter tools; share with teams.

### Key Steps
1. **Surface Scatter** — open CB → Ctrl+drag asset → Scatter on Selection; density/scale sliders; Noise Mask (pattern/frequency/invert for exclusion zones); Proximity Mask (select curve or mesh → distance falloff); Color Texture Mask (choose UE texture as mask)
2. **Path Scatter** — Create Curve tool → draw spline with point spacing set; OR Draw Curve tool; add spline to Path Scatter curves section + assets to scatter; density mode (per-point/exact count); pivot offset; path smoothness; parallel curves option
3. **Grid Scatter — 3D** — Grid Scatter → Distribution Mode=3D → Height Division=N for Z layers; remove-below-origin option in Feature Masking; combine with Proximity Mask to carve shape; scale variation + Random Spin + Rotation Jitter for natural look; Random Remove for gaps
4. **Radial Scatter** — Radial Scatter → add mesh → adjust radius/start angle/height; Concentric section: duplicate rings → min/max concentric distance=0 + ring height = stack vertically (tower); square shaping mode in Shaping section; scale variation + random rotation
5. **Decal Scatter** — Shift+click decals in CB → Ctrl+drag → Scatter Here; depth control; masking; rotation; OR add from Dash toolbar scatter section; can target existing scene decal as input
6. **Reference Tool** — in any tool parameter → click ✦ icon → Convert Reference → name it (e.g. "spacing"); assign same reference to other parameters in same or different tools → Reference Tool in Tools Panel controls all linked values simultaneously; per-reference individual sliders still available
7. **Compound Tool** — drag multiple scatter tools into Compound container in Tools Panel → Compound exposes only the parameters you choose; one control panel for multi-tool setups; save as compound preset for reuse
8. **Merge Actors** — select multiple actors + scatter instances → type `merge` in Dash bar → Merge Actors → result appears in CB → drag to scene; great for reusable modular pieces
9. **Tool Presets** — in tool panel: click preset icon → Create Preset (name it) → apply preset icon on new tool → select saved preset → instant same-configuration tool

### UE Systems / Blueprints / Settings
- **Surface Scatter masking types** — Noise (procedural pattern), Proximity (object/spline distance), Color Texture (UE texture as mask) — all stackable
- **Path Scatter density modes** — Per-Point (one per spline point) vs Exact Count (fixed total instances regardless of curve length)
- **Grid Scatter 3D** — Distribution Mode=3D; Height Division=N (N layers in Z); Remove Below Origin in Feature Masking (eliminates downward half of grid)
- **Radial Scatter concentric rings** — Concentric Distance=0 + Ring Height=N → stack rings vertically (tower); Concentric Distance>0 → expand rings outward; multiple ring duplicates for tower levels
- **Radial Scatter shaping** — Shaping section: Circle (default) or Square → square mode for urban block/column patterns
- **Reference Tool** — Convert any slider to Reference via ✦ → link multiple parameters → global control + individual fine-tune; visible in Tools Panel list
- **Compound Tool** — empty container; drag tools into it; expose only desired params; create preset for team sharing
- **Merge Actors** — type `merge` → select actors + scatter → one static mesh in CB; ideal for frequently-used modular elements
- **Tool Presets** — save scatter configuration (all params) → apply preset → identical setup in seconds; available per tool + compound level

### Difficulty
Beginner / Intermediate

### UE Version
UE 5.x (Dash 1.7)

### Tags
`#dash-1.7` `#environment` `#scatter` `#path-scatter` `#grid-scatter` `#radial-scatter` `#decals` `#property-references` `#compound-tool` `#tool-presets` `#procedural` `#beginner` `#intermediate`

---

## Related Entries
- [[creating-a-massive-procedural-game-world-in-ue5-with-dash]] — Property References + Curve Masking production workflow (1.7)
- [[dash-170---massive-ue5-world-building-tool]] — 1.7 release overview with Reference Tool + Compound + Presets
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Surface Scatter masking deep-dive (1.4)
- [[path-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Path Scatter beginner guide (1.4)
- [[no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial]] — Galen canyon with Path Scatter + Grid Scatter 3D (1.4)
