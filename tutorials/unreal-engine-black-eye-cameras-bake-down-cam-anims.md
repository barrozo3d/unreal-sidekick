---
title: Unreal Engine Black Eye Cameras: Bake down cam anims
source: YouTube
url: https://www.youtube.com/watch?v=D_CrTaBzEa4
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1.1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, sequencer, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-bake-down-cam-anims/
frame_count: 4
---

# Unreal Engine Black Eye Cameras: Bake down cam anims

**Source:** [YouTube](https://www.youtube.com/watch?v=D_CrTaBzEa4)
**Author:** Black Eye Technologies
**Duration:** 1m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** There's a new version of Black Eye, version 1.1, and one of this powerful new features is Camera Bake. Bake down some camera keyframes for a DCC round trip. Okay, so I made this body cam zombie, just got lots of motion in it. Let's bake it down. Number one, link to a destination camera, add a Desequencer, hit record. So let's make a new camera. And we'll throw it in the scene and we'll rename it to be well organized, and then you drag it down into Sequencer. Now you link the Black Eye camera to this camera. This is basically saying, where do I want to output all of these keyframes? We're gonna help put them onto this guy. Select it, hit bake. That's it. We're now baking down all those camera keyframes onto this new camera actor. And let's open it up. Let's look at all those delicious curves. So this is now a static camera. So if you're gonna render in layers or want to output to DCC to do some more animation work, it's all right there. There it is. So one, two, three, you can go from a procedural camera to a bake camera. Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-bake-down-cam-anims\frame_000.jpg


---

## Structured Notes

### Core Technique
Black Eye v1.1 Camera Bake: link a Black Eye procedural camera to a destination CineCameraActor and record it in Sequencer to produce dense baked keyframes for DCC round-trips or layered rendering.

### Summary
1.5-minute tutorial for the Camera Bake feature introduced in v1.1. Creates a baked, static CineCameraActor with dense keyframes from a Black Eye procedural camera. Use case: you want to export camera animation to Maya/Blender, render in layers, or hand off to a pipeline that expects standard keyframed cameras. Steps: create destination camera → drag to Sequencer → link Black Eye camera to it → hit Bake.

### Key Steps
1. **Create a destination CineCameraActor** — standard UE CineCamera; rename it clearly.
2. **Drag destination camera to Sequencer** — it appears as a new track.
3. **Select the Black Eye camera → Linked Cameras** — in the Black Eye camera details, find the "Linked Cameras" section.
4. **Set the destination camera as the bake target** — pick the CineCamera from the Linked Cameras selector.
5. **Hit Record (Bake)** — Black Eye bakes all procedural motion to dense keyframes on every channel of the destination camera.
6. **Inspect output** — open the baked camera's Sequencer curves. All transforms are now keyframed. The Black Eye camera is no longer needed for playback.

### UE Systems / Blueprints / Settings
- **Camera Bake** — Black Eye v1.1+ feature; found in Black Eye camera Details panel under "Linked Cameras"
- **Linked Cameras** — array on the Black Eye camera; specifies bake destination CineCameraActor
- **Record/Bake button** — triggers the bake pass; outputs dense keyframes
- **CineCameraActor** — standard UE camera; receives baked keyframes; compatible with all DCC exporters

### Difficulty
Beginner

### UE Version
UE 5.x (Black Eye v1.1)

### Tags
`#blackeye-v1` `#camera` `#sequencer` `#beginner`

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:08] tutorials/frames/unreal-engine-black-eye-cameras-bake-down-cam-anims/frame_000.jpg
- [0:25] tutorials/frames/unreal-engine-black-eye-cameras-bake-down-cam-anims/frame_001.jpg
- [0:45] tutorials/frames/unreal-engine-black-eye-cameras-bake-down-cam-anims/frame_002.jpg
- [1:06] tutorials/frames/unreal-engine-black-eye-cameras-bake-down-cam-anims/frame_003.jpg

## Related Entries
- [[unreal-engine-black-eye-cameras-start-here-tutorial]] — Baking Cameras section (same feature, more context)
- [[unreal-engine-black-eye-cameras-version-11-new-features-cross-camera]] — other v1.1 new features
