---
title: How to create a training environment in Unreal Engine 5 - Dash Workflow
source: YouTube
url: https://www.youtube.com/watch?v=rBcGl_ScDKs
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.6
ue_version: "UE 5.x"
tags: [dash-1.6, environment, terrain, scatter, path-scatter, cable-tool, grid-scatter, decals, materials, cross-project, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow/
frame_count: 10
---

# How to create a training environment in Unreal Engine 5 - Dash Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=rBcGl_ScDKs)
**Author:** Polygonflow Dash
**Duration:** 14m1s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted — see ingested file...]

---

## Structured Notes

### Core Technique
Jonathan (Community Director) builds a MOUT (Military Operations in Urban Terrain) training site environment — Terrain Tool (noise + convert to static mesh for performance), Road Tool (drawn curve + terrain conforming + border/sink settings), Surface Scatter with Object Masking to exclude road, Path Scatter for sandbags and weeds along curves, Cable Tool for utility pole wires, Grid Scatter for tire obstacle course, Decal Scatter for building weathering, Material Editor for color correction, cross-project asset import.

### Summary
14-minute MOUT training site environment built by Jonathan. Full Dash workflow: type `terrain` → noise terrain → adjust UV density + noise height → convert to static mesh → drag Megascans material from CB → Material Edit (normal/contrast/brightness/saturation) → Road Tool (type `draw curve` → type `road` → assign curve → density/width + terrain conforming + border sink) → Material Edit desaturate concrete → Surface Scatter grass/clover/tall grass (Ctrl+drag, Object Mask = road, proximity masking) → Surface Scatter rocks along road → Path Scatter sandbags along curve (Z direction override + width for dual-row + Random Remove Mask + seed) → Path Scatter weeds along multiple curves → Cable Tool for utility pole wires (hidden sphere anchors on insulators → connect one by one) → Grid Scatter tires obstacle course (grid origin = tire, input mesh = tire, scale/rotation/height) → Decal Scatter on buildings (select all decals → select buildings → max count + height limit + depth limit) → Material Editor for custom concrete color → cross-project fence asset (tagged in separate Dash project → available in current project).

### Key Steps
1. **Terrain** — type `terrain` → adjust: UV density, noise height → Convert to Static Mesh (Dash command) → drag Megascans material → Material Edit: normal intensity, contrast, brightness, saturation
2. **Road** — type `draw` → draw curve → type `road` → assign curve → density (0.9), width (road width), border sink (sharp road edge), sink (height above ground) → add terrain to Road Tool for conforming → adjust UVs → Material Edit to desaturate concrete blue tint
3. **Surface Scatter — Grass + Cover** — Ctrl+drag grass clumps → Object Mask = road mesh (disappears from roadway) → scatter clover + tall grass with same masking; density/scale variation
4. **Surface Scatter — Rocks** — Surface Scatter rocks along roadway edges for visual breakup; similar Ctrl+drag + mask
5. **Path Scatter — Sandbags** — place sandbag mesh → draw curve alongside road → type `path scatter` → add curve + sandbag → Z Direction Override (orient all upright) → Width = dual row (both sides of curve) → Random Remove Mask + Seed (natural gaps)
6. **Path Scatter — Weeds** — draw multiple curves approximating weed zones → Ctrl+drag weeds → Path Scatter on selected curves; adjust density/rotation/width
7. **Cable Tool — Utility Poles** — place hidden spheres on insulator positions of each pole → type `cable` → connect sphere anchors one by one for power lines; adjust gravity + segment thickness
8. **Grid Scatter — Tires** — place one tire → open Grid Scatter → tire = grid origin AND input mesh → adjust scale/rotation/height until satisfied; much faster than manual placement
9. **Decal Scatter — Building Weathering** — select all damage decals → Decal Scatter → add buildings as surfaces → limit by height (decals stay at lower zone) + depth (no stretching) → adjust max count for all buildings equally
10. **Cross-Project Assets** — fence asset from separate tagged Dash project → Preferences → Search External Projects → fence available in current Dash Content Browser; drag to place
11. **Material Editor** — precise color control on concrete materials (road + building); adjust dirt tint for soil realism

### UE Systems / Blueprints / Settings
- **Terrain → Static Mesh conversion** — type `convert terrain` or use Dash command; improves runtime performance significantly vs dynamic terrain
- **Road Tool** — type `road`; Density=0.9, Width=road width, Border Sink=sharp edge, Sink=rise above ground; add terrain to Road Tool for auto-conforming; UV Scale
- **Object Masking** — select road mesh → enable in scatter → grass/rocks disappear from roadway; real-time calculation
- **Path Scatter — Z Direction Override** — orients all instances along scatter global Z (useful for poles, upright objects); Width param = scatter band width (useful for dual-row sandbag wall)
- **Random Remove Mask** — random controlled thinning of scatter instances; Seed for variation
- **Cable Tool anchors** — hidden spheres placed on insulator positions → Cable Tool connects between them; Connection Rate + Cut Rate for wire bundle variation; Min/Max Gravity for elevation variation; Noise for breakup
- **Grid Scatter** — type `grid scatter`; Grid Origin = reference mesh; Input Mesh = mesh to scatter; auto-tiles in grid pattern; scale/rotation/height controls; much faster than manual for repeating elements (tires, bollards)
- **Decal Scatter** — all decals loaded → select buildings → max count distributes equally; Height Limit confines to lower building zones; Depth Limit prevents stretching
- **Cross-Project Access** — Dash 1.6+; Preferences → Search for External Projects → tagged assets available globally

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.6)

### Tags
`#dash-1.6` `#environment` `#terrain` `#scatter` `#path-scatter` `#cable-tool` `#grid-scatter` `#decals` `#materials` `#cross-project` `#intermediate`

---

## Captured Frames

<!-- Timestamps RECOVERED 2026-08-25 by recover_moments.py, not chosen.
     ingest.py before c4decae picked blind-era moments deterministically;
     re-derived from the source's own chapter/duration metadata and
     accepted only because the count matched frame_count exactly.
     These are blind-era moments: legible and citable now, but not
     content-anchored. Re-selecting them is still a human call. -->

- [0:05] tutorials/frames/how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow/frame_000.jpg
- [1:19] tutorials/frames/how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow/frame_001.jpg
- [2:18] tutorials/frames/how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow/frame_002.jpg
- [3:51] tutorials/frames/how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow/frame_003.jpg
- [7:02] tutorials/frames/how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow/frame_004.jpg
- [8:26] tutorials/frames/how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow/frame_005.jpg
- [10:34] tutorials/frames/how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow/frame_006.jpg
- [11:16] tutorials/frames/how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow/frame_007.jpg
- [12:12] tutorials/frames/how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow/frame_008.jpg
- [12:42] tutorials/frames/how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow/frame_009.jpg

## Related Entries
- [[centralized-content-browser-for-ue5---free-plugin]] — Cross-project asset access (1.6 feature)
- [[beginner-guide-to-road-tool-in-ue5-co-pilot-dash]] — Road Tool basics (1.3)
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Surface Scatter masking detail
- [[path-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Path Scatter beginner guide (1.4)
- [[how-to-scatter-decals-in-ue5---world-building-plugin]] — Decal scatter dedicated tutorial
