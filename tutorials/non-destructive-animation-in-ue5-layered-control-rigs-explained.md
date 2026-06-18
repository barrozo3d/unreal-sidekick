---
title: NON-DESTRUCTIVE Animation in UE5! Layered Control Rigs Explained
source: YouTube
url: https://www.youtube.com/watch?v=A8U_8iPc5hA
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["animation", "control-rig", "sequencer", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/non-destructive-animation-in-ue5-layered-control-rigs-explained/
frame_count: 4
---

# NON-DESTRUCTIVE Animation in UE5! Layered Control Rigs Explained

**Source:** [YouTube](https://www.youtube.com/watch?v=A8U_8iPc5hA)
**Author:** Unreal Engine
**Duration:** 9m29s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** In this video, I'm going to show you how to make non-destructive changes on top of pre-existing animation instead of Unreal Engine. And there's several ways to do this, but in this particular case, I'm going to show you how to use layer control rigs to get the job done. And as a quick reminder, I do have an animation YouTube channel if you want to go even deeper into these topics, as well as my own courses where I teach animation in Unreal Engine super, super in-depth. So with that, let's jump in. Here we are in our sample project. I'm currently looking at Shot 52, which has all these robots firing these fun little laser weapons. Now, to get here, I am just in the episodes in Trebeta, and it is right here, Shot 52. I'm in this level sequence. I'm currently just in a blank environment, just so I think it's cool to be able to see exactly what's in this particular shot. And so if I hit play, this is what we've got with our characters. Now, just as quick heads up, these fun little laser blasts are actually not 3D elements. If I leave the camera view and go find my camera, I can look really closely here, and you'll see that the laser blasts are actually 2D hand drawn animations on a lit...

**Frame:** tutorials\frames\non-destructive-animation-in-ue5-layered-control-rigs-explained\frame_000.jpg


---

## Structured Notes

### Core Technique
Layer Control Rigs in Sequencer — adding a live Modular Control Rig on top of a baked Animation Sequence to make non-destructive corrections and additive adjustments.

### Summary
Shows how to add a secondary Control Rig layer in Sequencer on top of an existing baked animation. The layer rig evaluates additively — you can tweak wrist rotation, fix foot sliding, or add secondary motion without touching the source animation data. Also notes a 2D sprite laser blast technique: hand-drawn 2D animation on a billboard lit mesh actor.

### Key Steps
1. In Sequencer, find the character's Animation Sequence track (baked mocap or keyframed)
2. Click **+ Track** on the Skeletal Mesh track → **Control Rig** → choose **Modular Control Rig** or a full body rig
3. The new Control Rig track evaluates ON TOP of the animation sequence additively
4. In the Control Rig track, scrub to the correction frame → move/rotate the desired control
5. Keys written to the Layer Control Rig track only; original Animation Sequence untouched
6. **Weight** the control rig layer (0–1) in the track header to blend the correction in
7. To remove: mute or delete the Control Rig layer track — original animation restored instantly
8. Use for: foot IK correction, wrist orientation fix, secondary bone override, stylistic exaggeration

### UE Systems / Blueprints / Settings
`Layer Control Rig Track` (Sequencer → + Track → Control Rig) → additive rig on top of baked animation
`Modular Control Rig` → full body rig; use a partial/hand rig for targeted corrections
`Track Weight` (0–1) → blend layer contribution
`Animation Sequence` (base track) → untouched; layer sits above in evaluation stack
`2D Sprite / Lit Translucent Billboard` → technique for hand-drawn laser/VFX overlays on 3D scene

### Difficulty
Intermediate

### UE Version
UE5

### Tags
animation, control-rig, sequencer, intermediate

---

## Related Entries
- `references/control-rig-animation.md` — full Control Rig reference
- `tutorials/ue5-animation-layers-non-destructive-camera-shake-character-tweaks.md` — animation layers on camera rigs
- `tutorials/baking-animation-in-ue5-control-rig-to-animation-sequence-back.md` — baking round-trip