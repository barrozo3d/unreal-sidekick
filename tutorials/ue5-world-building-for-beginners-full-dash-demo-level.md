---
title: UE5 World Building for Beginners - Full Dash Demo Level
source: YouTube
url: https://www.youtube.com/watch?v=PLACEHOLDER
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.9
ue_version: "UE 5.x"
tags: [dash-1.9, scatter, surface-scatter, path-scatter, grid-scatter, radial-scatter, physics, cable, mesh-pattern, quick-pipe, road-tool, vine, rvt, blend-material, fog-cards, water, falling-leaves, beginner]
extraction_status: complete
frames_dir: tutorials/frames/ue5-world-building-for-beginners-full-dash-demo-level/
frame_count: 19
---

# UE5 World Building for Beginners - Full Dash Demo Level

**Source:** YouTube
**Author:** Polygonflow Dash
**Duration:** ~23m | 19 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted — see ingested file...]

---

## Structured Notes

### Core Technique
Tomáš walks through every tool in the Dash demo level — a comprehensive beginner reference covering Physics Paint, all 5 scatter types, Cable Tool, Mesh Pattern (with ABO library), Quick Pipe, Road Tool (with scatter ring), Advanced Water, Vine Tool (3 methods), RVT blending, Blend Material, Fog Cards, Falling Leaves, Decal Scatter, Rainfall and Snowfall tools — all in the context of a single downloadable demo scene.

### Summary
23-minute beginner tour of the Dash demo level (downloadable). Tool-by-tool walkthrough: Physics Paint → bottles pile; Path Scatter (draw curve → Ctrl+drag → scatter on selected, parallel with for dual rows); Surface Scatter + Proximity Mask; Grid Scatter; Radial Scatter (circular + concentric rings); Merge Actors; Cable Tool; Mesh Pattern (presets + custom, ABO library); Quick Pipe; Road Tool (curve → road + scatter ring via Proximity Mask using road mesh as object + width; Path Scatter on same curve with parallel option); Advanced Water (search → water volume; color + waves + underwater caustics + blurriness); Vine Tool (3 methods: open from toolbar + atlas from Quixel Bridge); RVT (enable virtual textures + run RVT action + enable blend in Material Edit); Blend Material (3 textures + puddles/rain/snow layers); Fog Cards; Falling Leaves; Decal Scatter; Rainfall (dripping droplets + ripples in Material Edit; Blend Material B layer = puddles, T layer = rain); Snowfall (displacement via Nanite + snow in Material Edit).

### Key Steps
1. **Physics Paint** — select assets in scene → place menu → Physics Paint; or Ctrl+drag from CB → place overlapped → Physics Paint; gravity + simulation
2. **Path Scatter** — draw curve → Ctrl+drag asset while holding → scatter on selected; adjust settings; one per point = exact density; parallel with = dual rows
3. **Surface Scatter + Proximity Mask** — Ctrl+drag → scatter on selected; scroll to Proximity Mask; assign object → distance + width; invert toggle
4. **Grid Scatter** — scatter menu → Grid Scatter; assign origin actor + scatter objects; adjust width/depth/height; proximity mask to remove sections
5. **Radial Scatter** — scatter menu → Radial Scatter; assign scatter object + optional origin actor; count + radius + concentric rings; Surface Scatter trees on top of Radial Scatter output (Ctrl+drag → scatter on selected)
6. **Merge Actors** — select scatter outputs → Merge Actor action in search bar → reusable static mesh
7. **Cable Tool** — create menu → Cable Tool; assign objects; radius + duplicates + gravity
8. **Mesh Pattern** — open Mesh Pattern; assign surface; pick from included presets OR add custom pattern objects; scale/padding/noise; ABO library for high-quality free assets (e.g. couch → material edit from active tools list)
9. **Quick Pipe** — open Quick Pipe from tools; assign any curve; set radius + parallel with
10. **Road Tool** — draw curve → open Road Tool → assign curve → road appears; adjust width + material; Surface Scatter on floor → Proximity Mask: road mesh as object = clear road zone + distance/width; Path Scatter on same curve with parallel option = vegetation along road edges
11. **Advanced Water** — search `water` or create menu → place water volume; Tools panel = water color + waves + underwater caustics/blurriness; reopen by selecting water actor in Tools panel
12. **Vine Tool** — Method 1: open from toolbar → assign surface + origin actor (default leaf); Method 2: draw vine curve; Method 3: Quixel atlases → Ctrl+drag onto surface → Create Vines on Selection
13. **RVT** — enable virtual textures in Project Settings; select supported asset + surface (Megascans from Fab + UE Landscape/Dash Terrain/plane without Nanite); run RVT action in search bar → RVT volumes created; select rock → Material Edit → virtual texture effect enable + slope slider
14. **Blend Material** — CB → select 3 supported textures → Ctrl+drag onto surface → Create Blend Material; select surface → Material Edit in active tools list → puddles/rain/snow layer options
15. **Fog Card** — create menu or search → add fog card actor; customize in Tools panel
16. **Falling Leaves** — create menu or search → place actor; control from Tools panel
17. **Decal Scatter** — scatter menu or drag from CB → Ctrl+drag onto surface → scatter on surface
18. **Rainfall** — create menu or search; Material Edit of supported rock = dripping droplets + ripples; Blend Material B layer = puddles, T layer = rain
19. **Snowfall** — create menu or search; Material Edit = snow + displacement (requires Nanite on mesh); run Nanite action in search bar
20. **Procedural mesh → static mesh** — all Dash procedural meshes (Pipe/Cable/Road/Pattern) use custom Dash actors → convert to static mesh before shipping (big button in tool panel or Bake Mesh action); non-reversible

### UE Systems / Blueprints / Settings
- **Mesh Pattern — ABO** — Amazon Berkeley Objects library in Dash CB (free high-quality assets); search couch → drag + drop; open Material Edit from active tools list to adjust textures
- **Road Tool + scatter ring** — Proximity Mask: road mesh as proximity object + distance = clear road; width setting = how far scatter extends outward from road edge
- **RVT slope setting** — Material Edit → virtual texture → slope parameter controls where surface texture blends onto rock (0 = no sand, higher = more coverage on slopes)
- **Blend Material layers** — 3 textures blend together on surface; B-layer = puddles; T-layer = rain; adjust intensity in Material Edit
- **Snowfall displacement** — requires Nanite enabled on mesh (run Nanite action) for displacement to work correctly
- **Pin icon in Tools panel** — prevents accidentally switching which tool is shown when clicking other objects; critical when working with proximity masks on one tool while clicking proxy objects
- **Procedural mesh conversion** — Bake Mesh action or big button in each tool; non-reversible; do AFTER all adjustments are finalized

### Difficulty
Beginner

### UE Version
UE 5.x (Dash 1.9 — Mesh Pattern, ABO, Rainfall/Snowfall, Advanced Water, Falling Leaves present)

### Tags
`#dash-1.9` `#scatter` `#surface-scatter` `#path-scatter` `#grid-scatter` `#radial-scatter` `#physics` `#cable` `#mesh-pattern` `#quick-pipe` `#road-tool` `#vine` `#rvt` `#blend-material` `#fog-cards` `#water` `#falling-leaves` `#beginner`

---

## Related Entries
- [[dash-192---new-ue5-tools-amazon-3d-library-integration]] — Mesh Pattern deep-dive + ABO library (1.9)
- [[dash-19---managing-assets-in-ue5-just-got-a-lot-easier]] — Advanced Water, Falling Leaves, RVT, Collections (1.9)
- [[procedural-world-building-for-ue5---pcg-alternative]] — all scatter tools overview with Radial Scatter details (1.7)
- [[how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow]] — Road Tool + proximity masking in depth (1.6)
- [[working-fully-procedurally-in-unreal-engine-5---custom-asset-tutorial]] — Quick Pipe + Cable Tool Curve Mode + Path Scatter bridge (1.8)
