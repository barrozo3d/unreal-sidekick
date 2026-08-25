---
title: DASH 1.7.0 - MASSIVE UE5 WORLD BUILDING TOOL
source: YouTube
url: https://www.youtube.com/watch?v=B6T_VQQK6OU
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.7
ue_version: "UE 5.4"
tags: [dash-1.7, release-notes, vines, blend-material, property-references, ies-lights, fog-cards, landscape-masking, tool-presets, volume-scatter, beginner]
extraction_status: complete
frames_dir: tutorials/frames/dash-170---massive-ue5-world-building-tool/
frame_count: 17
---

# DASH 1.7.0 - MASSIVE UE5 WORLD BUILDING TOOL

**Source:** [YouTube](https://www.youtube.com/watch?v=B6T_VQQK6OU)
**Author:** Polygonflow Dash
**Duration:** 5m41s | 17 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted for brevity — see file as ingested...]

---

## Structured Notes

### Core Technique
Dash 1.7 release overview by Adnan — 15 new features including Vines Tool, GPT-4o asset tagging, Property References, IES library, Image-to-Grading, Fog Cards 2.0, Blend Material (3-surface auto-blend), Landscape Layer Masking, Instance Color Variation 2.0, Volume Scatter, Batch Edit Tags, Curve Masking (Keep Inside), Border Masking, Mesh Borders to Curve extraction, Tool Presets, improved scene saving, and Export as Zip.

### Summary
6-minute release video covering all Dash 1.7 features. Key additions: Vines Tool (auto-generates vines from Megascans leaf atlases); GPT-4o tagging (state-of-the-art accuracy, no training data use); Property References (one value drives multiple tool parameters with per-reference weights); IES library in Content Browser; Image-to-Grading (drag image → extract color grade → apply to camera); Fog Cards 2.0 (better in static and motion); Blend Material (3-surface drag onto mesh → auto-blend by height map, noise, vertex color); Landscape Layer Masking (pass layer name to scatter tool); Instance Color Variation 2.0 (randomize hue/sat/brightness per scatter instance); Volume Scatter (scatter inside mesh volume); Batch Edit Tags; Curve Masking with Keep Inside; Border Masking; Mesh Borders to Curve; Tool Presets (save scatter setups for reuse); simplified scene saving (single actor + dictionary); Export Assets as Zip.

### Key Steps
1. **Vines Tool** — Ctrl+drag Megascans leaf atlas onto mesh → Create Vines; OR draw curve → Draw Vines; full control over vine/leaf params
2. **GPT-4o Tagging** — AI tagging now uses GPT-4o for improved accuracy; content not used for model training
3. **Property References** — in any tool's parameter, convert a value to a Reference; reference the same value in other tools; each reference has its own weight for unique offsets
4. **IES Library** — browse photometric profiles from Content Browser; drag to place light with real-world emission shape
5. **Image-to-Grading** — drag image file onto Dash toolbar → extracts color grading from image → applies to active Dash camera
6. **Fog Cards 2.0** — improved rendering in static frames and motion; parameters: density, brightness, speed
7. **Blend Material** — Ctrl+drag 3 surface materials onto a mesh → Apply Blend Material; layers blend by height map + noise + vertex color; full per-layer control
8. **Landscape Layer Masking** — Surface Scatter → pass layer name of a landscape paint layer → scatter restricts to that layer
9. **Instance Color Variation 2.0** — per-instance random Hue, Saturation, Brightness offsets on scatter instances
10. **Volume Scatter** — scatter inside any mesh volume; use cases: bird flock, asteroids, environmental particles
11. **Curve Masking (Keep Inside)** — draw curve area → set as Object Mask → enable Keep Inside checkbox
12. **Border Masking** — custom geometry defines border → scatter clips at mesh boundary
13. **Mesh Borders to Curve** — extract border curve from any mesh
14. **Tool Presets** — save scatter setup (all parameters) → reuse in other scatter tools, scenes, or projects
15. **Export as Zip** — select UE asset → export with all dependencies as a zip for sharing

### UE Systems / Blueprints / Settings
- **Vine Tool** — available in Dash 1.7; Megascans leaf atlas → Create Vines or Draw Vines; full leaf/branch parameter control
- **GPT-4o Tagging** — upgrade over prior AI tagging; state-of-the-art accuracy; no training data use
- **Property References** — convert value → Reference in any tool; link same reference across tools; per-reference weight multiplier
- **IES Library (Content Browser)** — new in 1.7; IES library tab in Dash Content Browser; drag-to-place lights
- **Image-to-Grading** — drag image onto Dash toolbar → auto color grade extraction for active camera (Dash 1.7)
- **Fog Cards 2.0** — improved volumetric fog cards; density, brightness, speed parameters
- **Blend Material** — Ctrl+drag 3 materials → Apply; blending: height map + noise + vertex color; per-layer: tiling, wetness, displacement
- **Landscape Layer Masking** — type layer paint name in Surface Scatter → scatter only on that painted region
- **Instance Color Variation 2.0** — random hue/sat/brightness per scattered instance; valuable for dense foliage uniqueness
- **Volume Scatter** — scatter inside mesh volume bounds
- **Border Masking** — scatter clips at custom mesh border geometry
- **Tool Presets** — save full scatter configuration → recall in any tool; scope: global or project
- **Export as Zip** — select any UE asset → context menu → exports with all texture/mesh dependencies as zip

### Difficulty
Beginner

### UE Version
UE 5.4 (Dash 1.7)

### Tags
`#dash-1.7` `#release-notes` `#vines` `#blend-material` `#property-references` `#ies-lights` `#fog-cards` `#landscape-masking` `#tool-presets` `#volume-scatter` `#beginner`

---

## Captured Frames

<!-- Timestamps RECOVERED 2026-08-25 by recover_moments.py, not chosen.
     ingest.py before c4decae picked blind-era moments deterministically;
     re-derived from the source's own chapter/duration metadata and
     accepted only because the count matched frame_count exactly.
     These are blind-era moments: legible and citable now, but not
     content-anchored. Re-selecting them is still a human call. -->

- [0:05] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_000.jpg
- [0:42] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_001.jpg
- [0:59] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_002.jpg
- [1:27] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_003.jpg
- [1:42] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_004.jpg
- [1:56] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_005.jpg
- [2:12] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_006.jpg
- [2:39] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_007.jpg
- [2:53] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_008.jpg
- [3:12] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_009.jpg
- [3:27] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_010.jpg
- [3:42] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_011.jpg
- [3:58] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_012.jpg
- [4:11] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_013.jpg
- [4:19] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_014.jpg
- [4:39] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_015.jpg
- [4:52] tutorials/frames/dash-170---massive-ue5-world-building-tool/frame_016.jpg

## Related Entries
- [[creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial]] — Dash 1.7 Vines + Image-to-Grading used in production
- [[creating-a-massive-procedural-game-world-in-ue5-with-dash]] — Property References + Curve Masking used in production
- [[creating-a-blend-material-in-unreal-engine-5-just-got-easier]] — Blend Material dedicated tutorial
- [[how-to-create-vines-procedurally-in-unreal-engine-5]] — Vine Tool dedicated tutorial
- [[dash-110---procedural-scatter-presets-in-ue5]] — Tool Presets evolved into Compound Presets in 1.10
