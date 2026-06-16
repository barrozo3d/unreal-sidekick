---
title: Recreating a Helldivers 2 Game Environment in UE5 with Dash
source: YouTube
url: https://www.youtube.com/watch?v=plpGMR46HnE
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.7
ue_version: "UE 5.x"
tags: [dash-1.7, game-environments, terrain, scatter, surface-scatter, path-scatter, grid-scatter, physics, vine, fog-cards, image-to-grading, uds, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/recreating-a-helldivers-2-game-environment-in-ue5-with-dash/
frame_count: 17
---

# Recreating a Helldivers 2 Game Environment in UE5 with Dash

**Source:** [YouTube](https://www.youtube.com/watch?v=plpGMR46HnE)
**Author:** Polygonflow Dash
**Duration:** 22m56s | 17 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted — see ingested file...]

---

## Structured Notes

### Core Technique
Tomáš builds a playable Helldivers 2-inspired UE5 level using the full Dash 1.7 toolkit — Terrain, Curve+Path Scatter for cliffs, AI Tagging for custom asset packs, Grid Scatter for stacked containers, triple Proximity Mask on Surface Scatter for road exclusion, Physics Paint for rubble, Bake + Convert to Foliage, Vine Tool (1.7), UDS night scene, Image-to-Grading (1.7), Fog Cards, and particle/water one-liners.

### Summary
22-minute full environment breakdown of a Helldivers 2 fan scene in UE5 using the third-person template for a playable level. Workflow: Terrain + Megascans material → Curve tool for cliff splines (Path Scatter inward-facing) → AI Tagging (Mission Terminova Kitbash + Science Level 3) → manual prop placement + Grid Scatter for container stacks (pivot type `pivot center`) → triple Proximity Mask Surface Scatter for road edge rocks (curve as path cutout) → Physics Drop + Physics Paint (Ctrl+Shift+LMB = density, Shift+MMB = brush size) for rubble → Decal Scatter on buildings → Bake Instances → Convert to Foliage → Material Adjustment (hue/saturation) → Vine Tool (1.7, with Quixel Bridge atlases) → UDS (night, brightness 3, instant exposure) → particle (type `particle`) + water (type `water`) → Helldivers + Bile Titan (Blender-baked texture + animation) → Dash Camera (post-processing + color grading presets + Image-to-Grading = new 1.7 feature) → Fog Cards → MRQ render.

### Key Steps
1. **Terrain** — type `terrain` → Create Terrain; scale; Megascans material
2. **Cliff Splines** — type `curve` → min spacing 60 → draw → Ctrl+drag cliff mesh → Scatter on Selection → rotate 180° Z = face inward; repeat for front layer; Edit Material = green tint, lower saturation/brightness, roughness 0.2
3. **AI Tagging** — select folders → Compute; search by concept (storage, container, etc.); can add manual text tags
4. **Grid Scatter (containers)** — type `grid` → Grid Scatter; same mesh as grid origin + instance mesh; type `pivot` → pivot center for correct stacking
5. **Triple Proximity Mask (road rocks)** — Ctrl+drag rock onto terrain → Surface Scatter; draw a path curve → ProxMask 1: curve + Invert = rocks along road; ProxMask 2: curve = clear path strip; ProxMask 3: nearby static meshes = rocks clear around buildings
6. **Noise Mask** — apply noise mask to grass/vegetation scatter for organic breakup
7. **Physics Tool** — type `physics` → select rubble packs; Set Dynamic → Play = auto-scatter; Paint mode: Shift+MMB = brush size, LMB = paint, Ctrl+Shift+LMB = density
8. **Decal Scatter** — Shift+select multiple decals from library → Ctrl+drag onto building surface → Scatter on Selection; delete stray decals; run 2 console commands for foliage culling + vegetation lushness
9. **Bake Instances** — type `bake` → Bake Instances → add selected rocks with + → generates individual objects (keeps scatter hidden)
10. **Convert to Foliage** — type `foliage` → Convert Instances to Foliage → edit with classic foliage editor for cleanup
11. **Vine Tool (1.7)** — select Quixel Bridge atlas → Ctrl+drag onto rock → Create Vines on Selection; adjust length, leaf scale, branch material
12. **UDS Night** — delete all lights → drag Ultra Dynamic Sky Blueprint → set time = midnight, night brightness = 3, instant exposure, volumetric fog; rectangular light on building (disable volumetric scattering, indirect=0); particle type `particle`; water type `water`
13. **Image-to-Grading (1.7)** — in camera settings, drag any image to Dash toolbar → camera color grade takes on that image's properties; or pick from presets
14. **Fog Cards** — type `fog` → add; adjust density for subtle atmospheric depth

### UE Systems / Blueprints / Settings
- **Proximity Mask (triple)** — ProxMask 1: curve + Invert = band of rocks along road; ProxMask 2: same curve + distance = clear center strip; ProxMask 3: static meshes = clear zone around buildings
- **Physics Paint density** — Ctrl+Shift+LMB to adjust density on the fly while painting
- **Console commands for foliage** — two commands to fix culling + lusher foliage (not specified verbally but demonstrated)
- **Vine Tool (1.7)** — select atlas from Quixel Bridge tab in Dash CB → Ctrl+drag onto surface → Create Vines on Selection; set vine length, leaf scale, branch material
- **Image-to-Grading (1.7)** — drag any desktop image onto Dash toolbar while camera selected → applies that image's color properties as grade; also works with presets
- **Fog Cards** — type `fog` → animated card with density/scale controls
- **Helldivers character import** — Blender project → bake new UE texture in Blender → export FBX + animation → import to UE5
- **Playable Helldivers character** — via Metahumans tutorial method (external)

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.7)

### Tags
`#dash-1.7` `#game-environments` `#terrain` `#scatter` `#surface-scatter` `#path-scatter` `#grid-scatter` `#physics` `#vine` `#fog-cards` `#image-to-grading` `#uds` `#intermediate`

---

## Related Entries
- [[creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial]] — companion Helldivers 2 tutorial by Tomáš (1.7); similar pipeline, different angle
- [[dash-170---massive-ue5-world-building-tool]] — Dash 1.7 feature overview including Image-to-Grading + Vine Tool
- [[creating-a-massive-procedural-game-world-in-ue5-with-dash]] — similar Tomáš game-world pipeline (1.7)
- [[how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow]] — triple proximity masking for road + building exclusion (1.6)
