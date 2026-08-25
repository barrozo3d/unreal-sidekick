---
title: Speed Up Your Archviz Workflow with Dash in UE5
source: YouTube
url: https://www.youtube.com/watch?v=cC0l3yZMt3M
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.4
ue_version: "UE 5.x"
tags: [dash-1.4, archviz, polyhaven, physics, camera, materials, decals, path-tracing, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/
frame_count: 16
---

# Speed Up Your Archviz Workflow with Dash in UE5

**Source:** YouTube
**Author:** Polygonflow Dash
**Duration:** ~15m | 16 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted — see ingested file...]

---

## Structured Notes

### Core Technique
Tomáš Nod (external contributor, Budapest) builds a kitchen archviz scene using Dash 1.4's newly integrated Polyhaven HDRI lighting, Material Adjustment for all surfaces, Physics Tool (Complex collision) for natural fruit pile composition, Dash Camera with post-processing controls, Megascans decals, Level Sequence + Movie Render Queue with Path Tracer.

### Summary
14-minute archviz workflow: Blender kitchen model (FBX) → drag to UE5 scene → Polyhaven HDRI drag-to-scene (brand new 1.4 integration; Quixel + Megascans also available) → PPV (Unbound, exposure) → type `camera` → create CineCameraActor + set focal length + composition → Megascans material drag-to-mesh (saturation/roughness/brightness tweaks) → emissive cube as under-counter light → Physics Tool for fruit pile (Complex collision + Set Dynamic + duplicate while simulating) → additional props from Polyhaven model library → Megascans decals via Dash CB → Camera post-processing panel (bloom, fringe, temperature) → Level Sequence camera animation (25 FPS, linear keys) → Path Tracer via PPV → Movie Render Queue (anti-aliasing, path tracer, EXR, game overrides, 4K) → davinci-resolve noise reduction + dust layer.

### Key Steps
1. **HDRI Lighting** — Dash CB → Polyhaven tab → pick HDRI → drag to scene; Quixel + Megascans also in same CB; adjust intensity + rotation
2. **Post Process Volume** — drag PPV → Unbound → adjust exposure
3. **Camera** — type `camera` → Dash creates CineCameraActor; set focal length, sensor, exposure; reposition in viewport
4. **Materials (Megascans)** — open Dash CB → Megascans → drag material onto mesh; adjust saturation, roughness, brightness
5. **Under-counter light (emissive)** — create cube → scale to light strip size → apply emissive material
6. **Physics Tool (fruit piles)** — type `physics` → select fruit mesh → Complex collision → Set Dynamic → Start simulation; duplicate fruits while simulating; repeat until pile composition satisfies; manually adjust position
7. **Decals (Megascans)** — Dash CB → Megascans decals → drag onto surface; adjust scale/rotation via Dash decal controls
8. **Camera Post Processing** — Dash camera settings panel → adjust bloom, fringe, temperature, exposure
9. **Level Sequence** — New Sequence → name → drag in camera → create animation keys → set FPS=25 → set keys Linear for consistent motion; add third camera angle (larger focal length)
10. **Path Tracer + MRQ** — PPV → Path Tracer ON → denoiser OFF; MRQ → select sequence → clear settings → add: anti-aliasing, path tracer, EXR extension, game overrides; set 4K; override AA sample count → Render

### UE Systems / Blueprints / Settings
- **Polyhaven CB (brand new, 1.4)** — HDRI resolution picker → drag to scene; also Polyhaven 3D models available
- **Physics Tool — Complex collision** — select ground mesh → Complex collision option; prevents dynamic objects falling through; critical for props landing on irregular surfaces
- **Level Sequence** — standard UE Level Sequence; set keys to Linear mode for consistent camera speed
- **MRQ (Path Tracer)** — denoiser disabled for Path Tracer (cannot fine-tune); sample count override in AA settings; EXR extension for post work in davinci-resolve
- **davinci-resolve post** — noise reduction + dust layer added externally

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.4 — Polyhaven described as "now integrated")

### Tags
`#dash-1.4` `#archviz` `#polyhaven` `#physics` `#camera` `#materials` `#decals` `#path-tracing` `#intermediate`

---

## Captured Frames

<!-- Timestamps RECOVERED 2026-08-25 by recover_moments.py, not chosen.
     ingest.py before c4decae picked blind-era moments deterministically;
     re-derived from the source's own chapter/duration metadata and
     accepted only because the count matched frame_count exactly.
     These are blind-era moments: legible and citable now, but not
     content-anchored. Re-selecting them is still a human call. -->

- [0:05] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_000.jpg
- [0:55] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_001.jpg
- [2:22] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_002.jpg
- [2:47] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_003.jpg
- [3:45] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_004.jpg
- [4:10] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_005.jpg
- [4:36] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_006.jpg
- [6:42] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_007.jpg
- [7:31] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_008.jpg
- [9:28] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_009.jpg
- [9:55] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_010.jpg
- [11:03] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_011.jpg
- [12:07] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_012.jpg
- [12:25] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_013.jpg
- [13:06] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_014.jpg
- [14:15] tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/frame_015.jpg

## Related Entries
- [[how-to-create-a-cinematic-archviz-render-with-ue5-dash]] — Tomáš cinematic archviz with Path Tracer + ABO (1.9)
- [[realistic-architecture-environment-in-ue5---dash-workflow]] — Thomas Schneider archviz with AI tagging + physics paint (1.5)
- [[architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial]] — archviz overview with Radial Scatter + Cable Tool (1.6)
- [[auto-tag-sort-1000-ue5-assetsmonth-with-this-free-content-browser]] — AI tagging + Polyhaven + IES full CB tutorial (1.5)
