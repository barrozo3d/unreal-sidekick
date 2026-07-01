---
title: Unreal Engine 5 Compositing Tutorial - Composite Any Scene Fully Inside of UE5
source: YouTube
url: https://www.youtube.com/watch?v=OvvtTYB46b8
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 5.x"
tags: [compositing, camera-tracking, image-plate, vfx, sequencer, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-5-compositing-tutorial---composite-any-scene-fully-inside-of-ue5/
frame_count: 4
---

# Unreal Engine 5 Compositing Tutorial - Composite Any Scene Fully Inside of UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=OvvtTYB46b8)
**Author:** Boundless Entertainment
**Duration:** 6m53s | 1 section(s)

---

## Structured Notes

### Core Technique
Pre-Genesis compositing workflow: 3D track footage in After Effects → export camera → import into UE5 → rotoscope subject in AE → export as alpha image sequence → load as Image Plate in UE5 → build CG scene around the live-action plate for an in-engine composite.

### Summary
7-minute tutorial on compositing live-action footage entirely inside UE5 without leaving the engine (except for camera-tracking and roto). Pre-Genesis era technique. Workflow: shoot footage → 3D track in After Effects (or similar) → export camera data → import camera into UE5 as a tracked camera → in AE, remove the background around the actor (rotoscope) → export the isolated actor as an image sequence with alpha channel → import into UE5 as an Image Plate in Sequencer → the actor plate plays back on a 2D plane in the 3D scene → build the CG environment around it in UE5 using the plate as reference → render the full composite in MRQ. Note: This technique is superseded by Genesis (see 3d-tracking-natively-in-unreal-engine tutorial) which handles camera-tracking natively in UE5.

### Key Steps
1. **Shoot footage** — record video of actor/subject with tracking markers if needed (textured surfaces, dots)
2. **3D track in AE** — After Effects > 3D Camera Tracker effect on footage clip; AE analyzes motion and reconstructs 3D camera; adjust solver until stable; place null at ground plane
3. **Export camera** — from AE 3D tracker: right-click > Create Camera; then use the AE-to-UE exporter (or FBX export from 3D tracking software) to export camera position/rotation data as FBX or CSV
4. **Import camera into UE5** — File > Import FBX > import as camera into a Level Sequence; camera now matches the tracked real-world motion frame-for-frame
5. **Rotoscope in AE** — in AE: isolate actor from background; use Roto Brush + refine edge + mask path; output = actor over transparent background
6. **Export as image sequence with alpha** — AE > Render Queue or Media Encoder > output EXR or PNG sequence with alpha channel; one frame per image
7. **Import as Image Plate in UE5** — place an Image Plate Actor in scene; assign the exported image sequence; Image Plate plays back the footage frame-synced to Sequencer
8. **Build scene** — use the Image Plate as visual reference; build UE5 environment (lighting, geometry, props) to match the footage lighting and perspective
9. **Render** — MRQ > render composite; UE5 outputs Image Plate + CG environment merged; final composite ready or bring EXR into AE/Resolve for final grade

### UE Systems
- **Image Plate Actor** — UE5 actor that displays a 2D image sequence in 3D space; synced to Sequencer timeline; used as compositing layer for live-action footage
- **Tracked Camera (FBX import)** — import FBX camera animation into Level Sequence; camera follows the 3D track from AE/3DE exactly
- **Level Sequence** — Sequencer > New Level Sequence; contains camera + Image Plate + CG actors + lights; drives the composite render
- **After Effects 3D Camera Tracker** — AE's built-in motion track effect; 3D reconstructs scene from 2D footage; export camera as null+camera rig

### Difficulty
Intermediate

### UE Version
UE 5.x (pre-Genesis era)

### Tags
`#compositing` `#camera-tracking` `#image-plate` `#vfx` `#sequencer` `#intermediate`

---

## Related Entries
- [[3d-tracking-natively-in-unreal-engine---full-tutorial]] — Genesis: automated camera-tracking natively in UE (supersedes this workflow)
- [[unreal-engine-for-filmmakers---add-cinematic-vfx-to-your-films-for-free---ue5-pa]] — beginner compositing series Part 1
- [[unreal-engine-for-filmmakers---cinematic-vfx-for-free---ue5-part-2]] — beginner compositing Part 2
- [[unreal-engine-compositing-tutorial---unreal-engine-for-filmmakers-course-link-in]] — compositing tutorial with course link
