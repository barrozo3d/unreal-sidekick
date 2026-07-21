---
title: Working Fully Procedurally in Unreal Engine 5 - Custom Asset Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=rdXL5PtsGnY
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.8
ue_version: "UE 5.x"
tags: [dash-1.8, procedural, path-scatter, quick-pipe, cable, surface-scatter, proximity-mask, splines, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/working-fully-procedurally-in-unreal-engine-5---custom-asset-tutorial/
frame_count: 9
---

# Working Fully Procedurally in Unreal Engine 5 - Custom Asset Tutorial

**Source:** YouTube
**Author:** Polygonflow Dash
**Duration:** ~6m | 9 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted - see ingested file...]

---

## Structured Notes

### Core Technique
Tomáš builds a fully procedural rope bridge from a single spline using Dash 1.8: Path Scatter for planks (1-per-point + parallel rows) with proximity mask preventing post intersection, Quick Pipe for bridge ropes (same curve + parallel), Cable Tool in Curve Mode for handrail ropes, Surface Scatter with Height Mask on posts for climbing vines, and Path Scatter for hanging vines with Remove Mask - all anchored to one curve so moving any point updates the entire bridge.

### Summary
6-minute fully-procedural bridge tutorial: draw one spline → Path Scatter planks (rotation + density + 1-per-point exact mode; parallel with = dual rows; pin icon = keep tools panel open; proximity mask = wooden posts prevent plank intersection) → Quick Pipe for rope deck (same curve + parallel with for both side ropes; rope material drag-on) → Cable Tool Curve Mode (select curve, handrail ropes; height + gravity; parallel with; material) → Surface Scatter on posts (Feature Masking → Height Mask = plants only on lower zone) → Surface Scatter on cube with proximity mask inverted (vegetation follows posts) → Path Scatter hanging vines (Remove Mask + post as proximity mask; Alt+click = add curve points). Everything stays linked to the original curve.

### Key Steps
1. **Draw curve** - curve tool; min spacing; place between two reference cubes
2. **Path Scatter (planks)** - select curve → Ctrl+drag plank meshes from Fab/Quixel → scatter on selection → Path Scatter created; set rotation; density = 1 per point (exact); Tools panel stays open via pin icon
3. **Parallel rows** - in Path Scatter Parallel With settings → adjust distance → planks double to two rows
4. **Proximity mask (planks/posts)** - select planks Path Scatter; add posts as proximity mask → planks avoid post positions; no intersection
5. **Quick Pipe (bridge ropes)** - open Quick Pipe from Tools; add same curve; adjust radius; Parallel With = create second rope on other side; drag rope material onto pipe
6. **Cable Tool Curve Mode** - open Cable Tool; Curve Mode → select same curve; adjust height (raise above plank level) and gravity; Parallel With = second handrail; apply rope material
7. **Surface Scatter on posts (plants)** - select English Ivy assets; open Surface Scatter from toolbar; add posts as surface; density + scale; Feature Masking → Masking Height = only lower portion of post
8. **Surface Scatter on cube (vegetation around posts)** - Ctrl+drag vegetation onto cube → scatter here; set posts as proximity mask → invert = vegetation follows posts wherever they are on the cube
9. **Path Scatter (hanging vines)** - Path Scatter on same curve; Remove Mask = use posts as proximity mask → vines hang between posts; Alt+click curve to add points

### UE Systems / Blueprints / Settings
- **Path Scatter - 1 per point mode** - density = 1 in per-point mode places exactly one object per curve point; use for poles/pillars spaced evenly
- **Pin icon (Tools panel)** - prevents panel from switching when clicking other objects; essential when adding proximity objects from the viewport
- **Quick Pipe Parallel With** - duplicates the pipe geometry at an offset; used here to create two side ropes from one curve
- **Cable Tool Curve Mode** - alternative to object-to-object: Cable follows a drawn curve directly; combine with Parallel With for handrails
- **Feature Masking Height** - in Surface Scatter Feature Masking section; min/max height threshold restricts scatter to a vertical zone; used here for lower half of posts
- **Proximity mask inverted (cube)** - scatter on large plane/cube; proximity mask = posts + invert; result: scatter density peaks around each post, creating vegetation clusters that follow the posts
- **Remove Mask + proximity** - in Path Scatter, Remove Mask with posts as proximity object removes scatter near posts; creates natural gaps for hanging vines between posts
- **Alt+click curve** - adds new point to existing Dash curve; scatter updates immediately

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.8 - Fab mentioned in CB alongside Quixel)

### Tags
`#dash-1.8` `#procedural` `#path-scatter` `#quick-pipe` `#cable` `#surface-scatter` `#proximity-mask` `#splines` `#intermediate`

---

## Related Entries
- [[no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial]] - Galen spline-driven canyon; Grid Scatter 3D + Path Scatter on shared spline (1.4)
- [[how-to-re-create-the-walking-dead-in-unreal-engine-5---dash-workflow]] - Cable Tool connection/cut rate + Quick Pipe (1.4)
- [[how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow]] - Cable Tool utility poles with hidden sphere anchors (1.6)
- [[procedural-world-building-for-ue5---pcg-alternative]] - all scatter tools overview including Path Scatter density modes (1.7)
