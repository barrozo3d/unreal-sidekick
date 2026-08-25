---
title: Creating a Helldivers 2 Environment in 79 minutes - UE5 Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=kJhqc5_6usc
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.7
ue_version: "UE 5.x"
tags: [dash-1.7, game-environment, terrain, scatter, vines, fog-cards, image-to-grading, ai-tagging, physics, bake, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/
frame_count: 22
---

# Creating a Helldivers 2 Environment in 79 minutes - UE5 Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=kJhqc5_6usc)
**Author:** Polygonflow Dash
**Duration:** 80m12s | 22 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted for brevity — see file as ingested...]

---

## Structured Notes

### Core Technique
Full Dash 1.7 game environment pipeline by Tomáš — terrain, scatter-on-curve cliff placement, Grid Scatter, AI tagging, Physics Drop + Paint, Bake Instances, Convert to Foliage, Vine Tool (1.7 feature), nighttime lighting via Ultra Dynamic Sky, Image-to-Grading (1.7 feature), Fog Cards, and cinematic cameras with LUT presets.

### Summary
80-minute step-by-step Helldivers 2–inspired playable environment tutorial. Tomáš builds from a new UE5 project: terrain, scatter-on-curve cliffs (large + small, rotated 180° for inward facing), AI tagging for cross-project asset search, Grid Scatter for container stacks with pivot-center fix, Proximity Masking for organic path creation (dual-mask technique: mask 1 invert for clearance zone + mask 2 for path width), Physics Drop + Paint for debris/rubble, Decal Scatter, Bake Instances, Convert Scatter to Foliage Paint, Vine Tool (Dash 1.7 — Megascans leaves + bark material), nighttime lighting (UDS shortcut vs manual Directional+PPV+Fog approach), PPV exposure, volumetric fog, Fog Cards, image-to-grading (drag image onto Dash bar = extract color grade for camera), and cinematic multi-camera setup.

### Key Steps
1. **Project + level setup** — Third person template; new empty level; Window → Environment Light Mixer → add components
2. **Terrain** — type `terrain` → Create Terrain; adjust scale + noise; drag Megascans material; set UV Scale = 10
3. **Scatter on Curve (cliffs)** — type `curve` → Draw Curve (min spacing 60); Ctrl+drag cliff mesh → Scatter on Selection; adjust density; rotate 180° on Z (inward facing); repeat with smaller cliffs on second curve
4. **Edit Material (cliffs)** — isolate cliffs → Edit Material icon → greenish hue tint, lower saturation/brightness, roughness = 0.4
5. **AI Tagging + cross-project** — Content Browser → Project Library → select folders → Compute; search `storage`, `blue fences`; manual tag editing; access assets from other projects without migration
6. **Outpost layout** — drag assets from library; R/E hotkeys for rotate/scale; Grid Scatter for container stacks; type `pivot center` to fix pivot
7. **Rock + path proximity masking** — Surface Scatter rocks on terrain; Draw Curve as path guide; Proximity Mask 1 = curve + Invert + distance (clearance zone); Proximity Mask 2 = same curve + distance (path width)
8. **Physics Drop + Paint** — type `physics` → Physics Tool; Start → duplicate → compose; Paint function for rubble (Shift+MMB = brush size, Ctrl+Shift+LMB = density)
9. **Decal Scatter** — Shift-select decals → Ctrl+drag onto building → scatter; adjust scale/density; hide duplicates in wrong places
10. **Bake Instances** — type `bake` → Bake Instances → add rocks with + → generates individual editable meshes; retain original scatter for backup
11. **Convert to Foliage** — type `foliage` → Convert Instances to Foliage; use native foliage editor for cleanup painting
12. **Vine Tool (Dash 1.7)** — select rock → Ctrl+drag Megascans leaf atlas → Create Vines on Selection; set length, leaf scale; drag bark material onto branches
13. **Lighting (UDS approach)** — delete all manual lights; drag Ultra Dynamic Sky blueprint; set Time = midnight; Night Brightness = 3; Instant Exposure Adjustment; enable volumetric fog; rect light for building fill (disable Volumetric Scattering + Indirect Lighting = 0); Cloud Coverage = 0 (fixes cloud+fog z-fighting)
14. **Image-to-Grading (Dash 1.7)** — drag reference image onto Dash toolbar → camera color grade auto-extracted from image; also supports named presets
15. **Fog Cards** — type `fog` → select Fog Card; adjust density, brightness
16. **Cinematic cameras** — multiple Dash cameras; aspect ratio, DOF, post-process, color grade presets

### UE Systems / Blueprints / Settings
- **Scatter on Curve** — select curve → Ctrl+drag mesh; Z Rotation = 180° offset for inward-facing cliffs
- **Grid Scatter** — type `grid`; set grid origin + instance mesh; Count per axis; Pivot Center fix needed first
- **Proximity Mask (dual-mask path technique)** — Mask 1: curve + Invert + Distance = clear zone around path; Mask 2: same curve + smaller Distance = path width; combined = grass-free corridor
- **Bake Instances** — type `bake` → Bake Instances → add scatter with +; creates individual meshes; original scatter kept hidden (non-destructive backup)
- **Convert to Foliage** — type `foliage` → Convert Instances to Foliage; assets become Foliage Tool instances; edit with native foliage paint
- **Vine Tool (1.7)** — Ctrl+drag Megascans leaf atlas onto mesh → Create Vines on Selection; or draw curve → Draw Vines; parameters: length, leaf scale, branch radius; apply material to branches separately
- **Ultra Dynamic Sky (UDS)** — drag BP into scene; Time = midnight; Night Brightness slider; Instant Exposure Adjustment; volumetric fog included; Cloud Coverage = 0 to prevent fog interaction artifacts
- **Rect Light anti-fog** — disable Volumetric Scattering + set Indirect Lighting Intensity = 0 on interior fill lights to prevent fog hotspots
- **Image-to-Grading** — drag image from desktop/Explorer onto Dash toolbar; Dash extracts dominant color grade from image; applies to active camera (Dash 1.7 feature)
- **Fog Cards** — type `fog` in Dash prompt; Fog Card actor with Density, Brightness, Speed parameters

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.7)

### Tags
`#dash-1.7` `#game-environment` `#terrain` `#scatter` `#vines` `#fog-cards` `#image-to-grading` `#ai-tagging` `#physics` `#bake` `#intermediate`

---

## Captured Frames

<!-- Timestamps RECOVERED 2026-08-25 by recover_moments.py, not chosen.
     ingest.py before c4decae picked blind-era moments deterministically;
     re-derived from the source's own chapter/duration metadata and
     accepted only because the count matched frame_count exactly.
     These are blind-era moments: legible and citable now, but not
     content-anchored. Re-selecting them is still a human call. -->

- [0:05] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_000.jpg
- [1:35] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_001.jpg
- [2:35] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_002.jpg
- [6:13] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_003.jpg
- [8:15] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_004.jpg
- [13:35] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_005.jpg
- [32:25] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_006.jpg
- [35:15] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_007.jpg
- [38:35] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_008.jpg
- [39:55] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_009.jpg
- [42:13] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_010.jpg
- [47:40] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_011.jpg
- [49:30] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_012.jpg
- [50:23] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_013.jpg
- [53:25] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_014.jpg
- [57:45] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_015.jpg
- [59:05] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_016.jpg
- [1:05:55] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_017.jpg
- [1:06:37] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_018.jpg
- [1:08:33] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_019.jpg
- [1:08:54] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_020.jpg
- [1:18:18] tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/frame_021.jpg

## Related Entries
- [[dash-170---massive-ue5-world-building-tool]] — Dash 1.7 release notes (Vines + Image-to-Grading feature announcement)
- [[creating-a-massive-procedural-game-world-in-ue5-with-dash]] — large-scale scatter performance + Freeze tool
- [[how-to-create-vines-procedurally-in-unreal-engine-5]] — Vine Tool full reference
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Proximity Mask patterns
- [[recreating-a-helldivers-2-game-environment-in-ue5-with-dash]] — alternative/shorter Helldivers 2 build
