---
title: Advanced UE5 Cinematic Workflow: Camera Rigs & Custom Viewports
source: YouTube
url: https://www.youtube.com/watch?v=E7C1xbpEA_Q
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["sequencer", "cinematics", "camera", "pipeline", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/advanced-ue5-cinematic-workflow-camera-rigs-custom-viewports/
frame_count: 4
---

# Advanced UE5 Cinematic Workflow: Camera Rigs & Custom Viewports

**Source:** [YouTube](https://www.youtube.com/watch?v=E7C1xbpEA_Q)
**Author:** Unreal Engine
**Duration:** 12m56s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** In this video, we are going to dive into sub sequences, the camera setups with the camera rig, and we're going to mess with the viewport layout a little bit so we can get comfortable changing how we look at all the data on screen. So here I am inside of my regular sequence, right? I'm in the main level sequence that contains the whole cinematic project that editing all that stuff. Now it's important to understand that this level sequence, this asset right here, it's a level sequence, it's a timeline. It's a place to put data, be able to animate it, and be able to use a timeline to evaluate it. But inside of it, we have these shot tracks and inside these shot tracks are shots, right? But each of these shots is just another level sequence. Level sequences within level sequences within level sequences, we end up calling them sub sequences when they're nested in there. But functionally, there is not like an actual difference or type of asset that a sub sequence needs to be. They're all just level sequences. We just call them sub sequences, because it's shorter, easier to say. It tells you more about what their purpose is. Because if I double click on this shot, or actually before I dou...

**Frame:** tutorials\frames\advanced-ue5-cinematic-workflow-camera-rigs-custom-viewports\frame_000.jpg


---

## Structured Notes

### Core Technique
Advanced Sequencer cinematic workflow — sub-sequences structure, camera rig skeletal mesh + Control Rig setup, and custom multi-panel viewport layouts for simultaneous camera + perspective editing.

### Summary
Second video in the ACOM Animation Hub series. Covers the master Level Sequence → sub-sequences hierarchy (all are just Level Sequences; naming is organizational), setting up a Camera Rig Skeletal Mesh with its own Control Rig track for physically-driven camera moves, and configuring custom viewport layouts (e.g. 2-panel: camera view left, perspective right) for efficient animation editing.

### Key Steps
1. In Sequencer, inspect the master Level Sequence → Shot Track → each shot is a sub-sequence Level Sequence
2. Double-click a shot to enter it; `breadcrumb` path shown at top of Sequencer
3. Inside a shot, find the **Camera Rig** skeletal mesh track — it's a separate Skeletal Mesh Actor
4. The Camera Rig has its own **Control Rig sub-sequence** for animating the camera physically
5. The actual **Cine Camera Actor** is a child of the Camera Rig — inherits its transform
6. To set up custom viewport: `Viewport → Layout` dropdown → choose a split layout (2×1, 1+2, etc.)
7. In one viewport: press `G` → Pilot the Camera for the camera POV
8. In the other: keep as Perspective for working around the scene
9. Lock the camera viewport to a specific shot camera using the camera selector dropdown

### UE Systems / Blueprints / Settings
`Shot Track` (master Level Sequence) → contains sub-sequences as individual shots
`Sub-sequence` → just a Level Sequence nested inside another; same asset type
`Camera Rig Skeletal Mesh` → physically-simulated camera crane/dolly; driven by Control Rig
`Cine Camera Actor` → parented to Camera Rig; inherits physical motion
`Viewport → Layout` → split into multiple panels; one camera view + one perspective
`Breadcrumb Trail` (Sequencer top bar) → shows nesting depth; click to navigate up

### Difficulty
Intermediate

### UE Version
UE5

### Tags
sequencer, cinematics, camera, pipeline, intermediate

---

## Related Entries
- `references/sequencer-cinematics.md` — Sequencer structure and camera workflow
- `tutorials/level-management-sub-levels-spawnables-possessibles-in-ue5.md` — level organization for cinematics