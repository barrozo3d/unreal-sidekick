---
title: No Nodes Procedural Environment in Unreal Engine 5 - Dash Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=6U2jbJmqs4k
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.4
ue_version: "UE 5.x"
tags: [dash-1.4, environment, scatter, path-scatter, grid-scatter, physics, spline, canyon, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial/
frame_count: 11
---

# No Nodes Procedural Environment in Unreal Engine 5 - Dash Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=6U2jbJmqs4k)
**Author:** Polygonflow Dash
**Duration:** 8m24s | 11 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted — see ingested file...]

---

## Structured Notes

### Core Technique
Galen builds a spline-driven canyon environment in Dash without any node graphs — all scatter tools anchor to the same spline actors so every spline point adjustment instantly updates walls, ground scatter, and foliage. Path Scatter for canyon walls, Surface Scatter with spline proximity masking for ground elements, Grid Scatter 3D for rockslide simulation via Physics Tool.

### Summary
8.5-minute canyon environment tutorial by Galen. Core concept: two spline actors as master control arms; every Dash tool anchors to them — adjust spline points → all walls/ground scatter/foliage update in sync. Workflow: Draw Spline (adjust point spacing for large cliff assets) → Path Scatter cliff meshes along spline (density mode: per-point OR exact count; parallel curves option; pivot offset for alignment) → Terrain Tool for ground (simple flat + sand material) → Surface Scatter large ground rocks with proximity mask ON spline (invert + distance falloff + noise breakup) → second pass smaller detail rocks + foliage using same method → second canyon wall spline → Grid Scatter 3D for boulder pile above canyon (height division for Z stacking; Random Remove + remove-below-origin; scale variation + random spin + rotation jitter) → Physics Tool rockslide simulation (Dynamic mode → Set Static) → same method shown on tropical scene as alternate use case.

### Key Steps
1. **Draw Spline** — type `draw curve` or use Spline tool → adjust point spacing (larger for bigger assets) → draw canyon wall shape → stop drawing
2. **Path Scatter — Canyon Walls** — type `path scatter` → add cliff meshes to scatter tab → add drawn spline → adjust density (per-point mode: one cliff per spline point; exact count mode: fixed total instances) → scale variation (small amount for natural feel, not too much) → pivot offset (align base of cliff to curve) → parallel curves option (adds second parallel line without new spline)
3. **Terrain + Ground** — type `terrain` → adjust to simple flat + Dash terrain tool params → drag sand material from CB
4. **Surface Scatter — Ground Cover (proximity to spline)** — Ctrl+drag ground rocks → Scatter on Selection → Proximity Mask: select spline → + → Invert ON → Distance slider = falloff from spline (ground elements hug walls) → add noise mask for natural edge breakup; repeat for second higher-frequency detail pass + foliage
5. **Second Canyon Wall** — same methods with second independent spline for opposite wall
6. **Grid Scatter 3D — Boulder Pile** — source boulder meshes → Grid Scatter → load to instance meshes → Scale variation (wide range for natural rocks) → Distribution Mode = 3D → Height Division = increase for vertical Z stacking → Random Remove for gaps → Feature Masking → Remove Below Origin (Z axis) → limit scatter to above canvas → adjust seed; Random Spin + Rotation Jitter for variation
7. **Physics Rockslide** — Physics Tool → Set Dynamic on grid → Start → boulders fall into canyon → Stop when settled → Set Static; repeat with different seed for variation

### UE Systems / Blueprints / Settings
- **Path Scatter — density modes** — Per-Point mode (one instance per spline point; spacing controlled by point spacing); Exact Count mode (fixed total instances regardless of curve length); toggle in tool panel
- **Path Scatter — Parallel Curves** — option to add second parallel row without drawing new spline; offset from original
- **Path Scatter — Pivot Offset** — controls how assets align to curve direction and offset from curve; critical for cliff pieces to sit correctly
- **Surface Scatter — Spline Proximity Mask** — add spline actor to Proximity Mask → Invert = scatter concentrates near spline; Distance = radius; Noise = soft edge breakup
- **Grid Scatter — 3D Distribution Mode** — scatter in X, Y, and Z; Height Division parameter = how many layers in Z; Distribution starts at 0 in Z → increase Height Division to stack upward
- **Grid Scatter — Remove Below Origin (Z)** — Feature Masking section → option to remove instances below origin on Z axis; useful for grid extending downward
- **Grid Scatter — Proximity Mask** — combine with Remove Below Origin to carve custom chunk shapes from boulder pile
- **Random Spin + Rotation Jitter** — in Grid Scatter: Random Spin = random per-instance rotation; Jitter = rotation variation range; essential for natural rock scatters

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.4)

### Tags
`#dash-1.4` `#environment` `#scatter` `#path-scatter` `#grid-scatter` `#physics` `#spline` `#canyon` `#procedural` `#intermediate`

---

## Related Entries
- [[path-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Path Scatter beginner guide (1.4)
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Surface Scatter masking (1.4)
- [[new-physics-tool-for-unreal-engine-5]] — Physics Tool intro (Josh Powers)
- [[how-to-re-create-the-walking-dead-in-unreal-engine-5---dash-workflow]] — Grid Scatter with Random Remove (Galen)
