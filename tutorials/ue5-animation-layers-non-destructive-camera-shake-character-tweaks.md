---
title: UE5 Animation Layers: Non-Destructive Camera Shake & Character Tweaks
source: YouTube
url: https://www.youtube.com/watch?v=NDrc3ap2ZAA
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["animation", "sequencer", "cinematics", "camera", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/ue5-animation-layers-non-destructive-camera-shake-character-tweaks/
frame_count: 4
---

# UE5 Animation Layers: Non-Destructive Camera Shake & Character Tweaks

**Source:** [YouTube](https://www.youtube.com/watch?v=NDrc3ap2ZAA)
**Author:** Unreal Engine
**Duration:** 15m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Punditalk Animation Layers, a super handy workflow that I see a lot of games animators use, but I often see feature film animators really not use all that much. Not sure why, so let's check it out. So here I am in Shot 55. This is the one where he made a rips down this door, goes and runs, and we get this awesome little slow motion moment. Now, we're gonna talk about two uses of animation layers in this video. One is for characters and one is for cameras, and that's what we're starting right now. This animation actually has camera shake. It has a bunch of great camera animation that we can dive a little bit deeper into. In Shot 55, down towards the bottom, we have the camera itself, but we also have the camera rig. So if I leave the camera view, I'll come over here, and I'll show you what's going on. So here is our camera, right there, camera actor, and we also have the camera rig skeletal mesh, which is sort of its own asset to be able to control the camera. Now, the camera rig itself, if we twirl this down, has a space for animation sequences, which we don't actually have anything on, and then we have the camera control rig, which is the controls, right? These are the actual grab...

**Frame:** tutorials\frames\ue5-animation-layers-non-destructive-camera-shake-character-tweaks\frame_000.jpg


---

## Structured Notes

### Core Technique
Sequencer Animation Layers — adding non-destructive additive animation tracks on top of existing character or camera rig animation without altering the base performance.

### Summary
Covers UE5's Animation Layers in Sequencer for both characters and camera rigs. Demonstrates adding a camera shake layer on top of a Control Rig camera animation without touching the original keyframe data — layers blend additively and can be weighted/muted independently. Same workflow applies to characters for secondary motion, LOD adjustments, and micro-corrections.

### Key Steps
1. In Sequencer, find the character or camera Control Rig sub-sequence
2. Click **+ Track → Animation Layer** to add a new layer above the base animation
3. The new layer is empty and additive by default — it adds on top without replacing
4. Animate the layer's controls (e.g. camera position jitter, shoulder sway)
5. Adjust the **Layer Weight** in the track header (0 = off, 1 = full)
6. Key the Layer Weight to fade layers in/out per shot
7. **Camera Shake** use case: add a camera layer → animate small random translation/rotation offsets → result blends with the main camera move
8. **Character micro-correction** use case: add a layer → fix a specific joint overlap without re-animating the full performance
9. Layers can be muted/soloed in the track header for comparison

### UE Systems / Blueprints / Settings
`Animation Layer Track` (Sequencer) → additive non-destructive animation on top of base sequence
`Layer Weight` → 0–1 keyable blend; mute/solo in track header
`Camera Rig` in Sequencer → skeletal mesh camera rig with its own Control Rig + animation layer
Works on both character Control Rig and camera rig sub-sequences

### Difficulty
Intermediate

### UE Version
UE5

### Tags
animation, sequencer, cinematics, camera, intermediate

---

## Related Entries
- `references/sequencer-cinematics.md` — Sequencer track types
- `references/control-rig-animation.md` — Control Rig additive layers
- `tutorials/non-destructive-animation-in-ue5-layered-control-rigs-explained.md` — layered control rigs