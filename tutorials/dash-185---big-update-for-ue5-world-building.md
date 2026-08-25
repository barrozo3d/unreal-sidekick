---
title: DASH 1.8.5 - BIG UPDATE FOR UE5 WORLD BUILDING
source: YouTube
url: https://www.youtube.com/watch?v=lHZwUtS6hyE
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.8
ue_version: "UE 5.x"
tags: [dash-1.8, release-notes, fab, ai-assistant, terrain, scatter, materials, beginner]
extraction_status: complete
frames_dir: tutorials/frames/dash-185---big-update-for-ue5-world-building/
frame_count: 9
---

# DASH 1.8.5 - BIG UPDATE FOR UE5 WORLD BUILDING

**Source:** [YouTube](https://www.youtube.com/watch?v=lHZwUtS6hyE)
**Author:** Polygonflow Dash
**Duration:** 8m6s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted — see ingested file...]

---

## Structured Notes

### Core Technique
Dash 1.8.5 release overview by Tomáš — major additions: Fab plugin support in Content Browser, revamped AI assistant (named SOFI), terrain deformation via curves + experimental height map, Incremental Spin (discrete rotation values), Data Tables (layered properties for scatter/terrain), Proximity Width (strip masking without managing multiple masks), Texture Repetition Breakup (enable breakup tiling in Material Edit and Blend Material tools).

### Summary
8-minute release video covering Dash 1.8.5. Key additions: (1) Fab Integration — assets downloaded from the Fab plugin now appear in a dedicated Fab tab in Dash Content Browser; supports Megascans, FBX, and GLTF; asset tags auto-imported; Material Edit and Blend Material tools work on Fab Megascans assets. (2) AI Assistant (SOFI) — more accurate, generates action buttons to call tools directly, links to documentation, supports multi-turn conversations, accepts image uploads. (3) Terrain Deformation — deform terrain mesh with curves (Falloff + Tapering); add via + button in Curve Properties; experimental height map support. (4) Incremental Spin — scatter rotation restricted to specific discrete values (e.g. 0° and 90°), ordered or randomized. (5) Data Tables — stack multiple layers of density, proximity, landscape masking, or terrain curves; click Edit Table → + to add layers. (6) Proximity Width — single control to create a strip of scatter without needing multiple proximity masks or references. (7) Texture Repetition Breakup — enable in Material Edit or Blend Material to eliminate tiling repetition; first iteration.

### Key Steps
1. **Fab Integration** — download asset via Fab plugin → it appears in Dash Content Browser → Fab tab; supports Megascans, FBX, GLTF; search via keyword tags; Material Edit + Blend Material work on Fab Megascans; scatter/physics from fab-assets same as any other asset
2. **AI Assistant (SOFI)** — open from Dash toolbar; type question → get workflow outline with action buttons for each tool; upload image → SOFI suggests workflow for that scene; supports multi-turn conversation
3. **Terrain Deformation with Curves** — place terrain + a curve; in terrain tool → Curve Properties → + to assign curve; reshape curve to deform terrain; multiple curves supported on one mesh
4. **Height Map Support (Experimental)** — select height map in UE Content Browser → + icon in terrain tool → assigns to terrain → adjust Intensity → creates realistic canyon/mountain shapes
5. **Incremental Spin** — in any scatter tool → Rotation tab → Incremental Spin → enter comma-separated values (e.g. 0, 90) → each instance gets one of those values; enable Sorting for ordered sequence
6. **Data Tables** — in any scatter/terrain tool → Edit Table → + to add a layer → configure second density/proximity/etc. → repeat for unlimited stacking; available in: Surface Scatter density, Proximity Masking, Landscape Layer Masking, Noise Masking, Terrain Curves
7. **Proximity Width** — in surface/path/decal/grid scatter → Proximity Width parameter → creates a band of scatter along a proximity line without managing extra masks
8. **Texture Repetition Breakup** — in Material Edit or Blend Material tool → enable "Enable Breakup Tiling" → repetition disappears; adjust breakup parameters as needed

### UE Systems / Blueprints / Settings
- **Fab Integration** — Dash 1.8.5+; assets from Fab plugin → auto-appear in Dash Content Browser Fab tab; tag search available immediately; Material Edit/Blend tools work on Fab Megascans
- **AI Assistant SOFI** — replaces v1.8 AI assistant; more accurate; generates direct action buttons (click → runs tool); documentation links; image upload support; multi-turn conversation
- **Terrain Deformation** — Curve Properties → + button → assign spline; Falloff + Tapering per curve; multiple curves per terrain mesh; experimental Height Map support via + icon in terrain tool
- **Incremental Spin** — discrete rotation values (e.g. 0, 90, 180) randomly assigned to each instance; Sorting=ON for sequential assignment
- **Data Tables** — experimental; layered properties for density/proximity/landscape masking/noise/terrain curves; Edit Table → + → configure each layer
- **Proximity Width** — single strip control in surface/path/decal/grid scatter; replaces need for stacked proximity masks when making scatter bands
- **Texture Repetition Breakup** — in Material Edit + Blend Material → Enable Breakup Tiling; adjustable parameters; v1.8.5 first iteration

### Difficulty
Beginner

### UE Version
UE 5.x (Dash 1.8.5)

### Tags
`#dash-1.8` `#release-notes` `#fab` `#ai-assistant` `#terrain` `#scatter` `#materials` `#beginner`

---

## Captured Frames

<!-- Timestamps RECOVERED 2026-08-25 by recover_moments.py, not chosen.
     ingest.py before c4decae picked blind-era moments deterministically;
     re-derived from the source's own chapter/duration metadata and
     accepted only because the count matched frame_count exactly.
     These are blind-era moments: legible and citable now, but not
     content-anchored. Re-selecting them is still a human call. -->

- [0:05] tutorials/frames/dash-185---big-update-for-ue5-world-building/frame_000.jpg
- [0:31] tutorials/frames/dash-185---big-update-for-ue5-world-building/frame_001.jpg
- [2:42] tutorials/frames/dash-185---big-update-for-ue5-world-building/frame_002.jpg
- [4:25] tutorials/frames/dash-185---big-update-for-ue5-world-building/frame_003.jpg
- [5:36] tutorials/frames/dash-185---big-update-for-ue5-world-building/frame_004.jpg
- [6:07] tutorials/frames/dash-185---big-update-for-ue5-world-building/frame_005.jpg
- [6:47] tutorials/frames/dash-185---big-update-for-ue5-world-building/frame_006.jpg
- [7:07] tutorials/frames/dash-185---big-update-for-ue5-world-building/frame_007.jpg
- [7:36] tutorials/frames/dash-185---big-update-for-ue5-world-building/frame_008.jpg

## Related Entries
- [[getting-started-with-dash---easy-world-building-in-ue5]] — Dash 1.8 comprehensive tutorial (same version series)
- [[creating-a-blend-material-in-unreal-engine-5-just-got-easier]] — Blend Material tool detail
- [[auto-tag-sort-1000-ue5-assetsmonth-with-this-free-content-browser]] — AI tagging in Project Library
- [[best-free-unreal-engine-5-asset-management-plugin-in-2025]] — Fab tab overview in 1.9
