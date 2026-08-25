---
title: How to Create a Cinematic Archviz Render with UE5 & Dash
source: YouTube
url: https://www.youtube.com/watch?v=HL8NDvv1G44
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.9
ue_version: "UE 5.x"
tags: [dash-1.9, archviz, scatter, vines, path-tracing, amazon-abo, materials, lighting, hdri, mrq, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-to-create-a-cinematic-archviz-render-with-ue5-dash/
frame_count: 8
---

# How to Create a Cinematic Archviz Render with UE5 & Dash

**Source:** [YouTube](https://www.youtube.com/watch?v=HL8NDvv1G44)
**Author:** Polygonflow Dash
**Duration:** 13m17s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted — see ingested file...]

---

## Structured Notes

### Core Technique
Tomáš walks through a 3DMOS renovation challenge archviz scene built in UE5 + Dash — Blender modeling/export → UE5 import → Surface Scatter gravel (proximity masked to terrace area) + Curve-based stone wall scatter → Vine Tool for climbing vegetation → ABO library furniture for interior → HDRI lighting via Light Studio Blueprint → Path Tracer render via MRQ → color grade.

### Summary
13-minute archviz production workflow for a rustic-meets-modern renovation scene. Pipeline: Blender modeling (side building + FBX export: Geometry → Smoothing=Face) → UE5 import (no collision) → replace original textures with Megascans materials via Dash → Surface Scatter gravel (Ctrl+drag → Scatter on Selection, proximity mask on terrace + invert distance) → stone wall using scatter along curve + bake for manual tweaks → Vine Tool for climbing vegetation (wall pieces as surface + cube as origin + IVY leaf atlases) → background trees as low-res geo barely visible → Amazon Berkeley Objects furniture for side building interior → material edit on ABO assets → Light Studio Blueprint (enable HDRI → select Polyhaven HDRI as cubemap; uncheck sunlight/atmosphere/fog; Skylight 1 → Cube Map source → same HDRI; increase cubemap resolution for reflections) → tweak directional light → final details (grass near walls, decals, props) → MRQ render (camera in Level Sequence, Path Tracing mode) → color grade + vignette.

### Key Steps
1. **Blender export** — FBX export: Geometry section → Smoothing = Face (critical for UE5 normal import)
2. **UE5 import** — import FBX to new folder; disable collision; drag static meshes to scene; replace textures with Megascans via Dash Content Library
3. **Surface Scatter Gravel** — search for gravel mesh in Dash CB → Ctrl+drag onto ground → Scatter on Selection → adjust scale and density → add terrace mesh to Proximity Mask → invert distance value → scatter excluded from terrace (gravel only outside)
4. **Stone Wall** — scatter stone mesh along a curve; use Noise Mask for natural variation; Bake scatter to static mesh → manual tweaks on individual pieces
5. **Vine Tool** — assign multiple wall mesh pieces as surface → simple cube as origin mesh → use Vine Tool → assign IVY leaf atlases from previous scatter reuse
6. **Background Trees** — Ctrl+drag trees → place quickly as background fill; barely visible in render
7. **ABO Interior Furniture** — open Dash CB → ABO tab → browse furniture → drag to place; material edit for color/surface matching
8. **HDRI Lighting (Light Studio Blueprint)** — drag Light Studio Blueprint from content drawer → in Outliner: select all lighting actors except Directional Light → delete → open Light Studio details → enable Use HDRI → select Polyhaven HDRI file as HDRI Cubemap → uncheck Use Sunlight, Use Atmosphere, Use Fog if needed → Skylight 1: Source Type = Cube Map → assign same HDRI; increase Cubemap Resolution for sharper reflections → tweak Directional Light intensity
9. **Final Details** — Surface Scatter small grass patches near walls; decals for surface interest; decorative props
10. **Path Tracer Render** — add camera to Level Sequence → MRQ → Path Tracing tab → render → color grade + vignette in post

### UE Systems / Blueprints / Settings
- **FBX Export from Blender** — Geometry → Smoothing=Face for correct normals in UE5
- **Surface Scatter (proximity inversion)** — Ctrl+drag → Scatter on Selection → Proximity Mask: assign terrace mesh → Invert Distance = ON → scatter avoids terrace surface
- **Scatter Bake** — type `bake` in Dash bar → converts scatter instances to editable static meshes for manual adjustment; non-destructive backup retained
- **Vine Tool** — assign multiple wall pieces as surface; cube as origin; Vine Tool creates climbing vines; attach leaf atlas for leaves
- **Light Studio Blueprint** — drag from Dash or UE content drawer; enable Use HDRI → assign Polyhaven HDRI cubemap; disable Sunlight/Atmosphere/Fog; Skylight → Cube Map → same HDRI; increase resolution for reflections
- **Path Tracer (MRQ)** — camera in Level Sequence → MRQ → Path Tracing output; Tomáš renders for realistic archviz look

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.9+)

### Tags
`#dash-1.9` `#archviz` `#scatter` `#vines` `#path-tracing` `#amazon-abo` `#materials` `#lighting` `#hdri` `#mrq` `#intermediate`

---

## Captured Frames

<!-- Timestamps RECOVERED 2026-08-25 by recover_moments.py, not chosen.
     ingest.py before c4decae picked blind-era moments deterministically;
     re-derived from the source's own chapter/duration metadata and
     accepted only because the count matched frame_count exactly.
     These are blind-era moments: legible and citable now, but not
     content-anchored. Re-selecting them is still a human call. -->

- [0:05] tutorials/frames/how-to-create-a-cinematic-archviz-render-with-ue5-dash/frame_000.jpg
- [0:28] tutorials/frames/how-to-create-a-cinematic-archviz-render-with-ue5-dash/frame_001.jpg
- [4:58] tutorials/frames/how-to-create-a-cinematic-archviz-render-with-ue5-dash/frame_002.jpg
- [9:57] tutorials/frames/how-to-create-a-cinematic-archviz-render-with-ue5-dash/frame_003.jpg
- [10:17] tutorials/frames/how-to-create-a-cinematic-archviz-render-with-ue5-dash/frame_004.jpg
- [10:57] tutorials/frames/how-to-create-a-cinematic-archviz-render-with-ue5-dash/frame_005.jpg
- [12:20] tutorials/frames/how-to-create-a-cinematic-archviz-render-with-ue5-dash/frame_006.jpg
- [12:40] tutorials/frames/how-to-create-a-cinematic-archviz-render-with-ue5-dash/frame_007.jpg

## Related Entries
- [[architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial]] — Archviz workflow with Cable Tool string lights (Dash 1.6)
- [[how-to-create-vines-procedurally-in-unreal-engine-5]] — Vine Tool dedicated tutorial
- [[dash-192---new-ue5-tools-amazon-3d-library-integration]] — ABO Library introduction (1.9.2)
- [[realistic-architecture-environment-in-ue5---dash-workflow]] — Related archviz workflow tutorial
