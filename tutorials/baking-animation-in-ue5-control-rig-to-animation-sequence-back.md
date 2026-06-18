---
title: Baking Animation in UE5: Control Rig to Animation Sequence & Back!
source: YouTube
url: https://www.youtube.com/watch?v=mDEliLixziU
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["animation", "control-rig", "sequencer", "pipeline", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/baking-animation-in-ue5-control-rig-to-animation-sequence-back/
frame_count: 4
---

# Baking Animation in UE5: Control Rig to Animation Sequence & Back!

**Source:** [YouTube](https://www.youtube.com/watch?v=mDEliLixziU)
**Author:** Unreal Engine
**Duration:** 14m8s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey there, welcome back. My name is Sir, and in these videos, we're going to take a look at working with animation data inside of Unreal Engine. And we're going to do that using the new ACOM animation sample project, which you can download on Fab today if you want to follow along. Now, if you're just joining us, this is the second set of videos in the series. In the previous class, we looked at the project overall, got a sense of levels, level sequences, things like that. But in these videos, like I said, we're going to look specifically at working with animation data. And in this video, we're going to talk specifically about animation sequences and live control rigs and the differences between working with each of those options. So here I am in the production. I am looking at the full sequence here. We got our characters running around. And I'm currently loaded into the full master level with this entire environment that I can fly around and check everything out. But for the purposes of these videos, I'm actually going to leave, hit control, and go to a basic level where there's pretty much nothing going on. Now, I can still load that same animation sequence right here with the fu...

**Frame:** tutorials\frames\baking-animation-in-ue5-control-rig-to-animation-sequence-back\frame_000.jpg


---

## Structured Notes

### Core Technique
Animation baking round-trip in UE5 — converting a live Control Rig in Sequencer to a baked Animation Sequence and back, understanding when each form is appropriate.

### Summary
Explains the difference between animating with a live Control Rig (interactive, editable) vs. a baked Animation Sequence (performant, portable) in Sequencer. Covers the bake workflow (Control Rig → Animation Sequence via right-click Bake To Animation Sequence), the reverse (re-link an Animation Sequence back to a Control Rig for editing), and production tradeoffs. Part of the ACOM Animation Sample tutorial series.

### Key Steps
1. Animate character using a live **Control Rig** sub-sequence in Sequencer
2. To bake: right-click the Control Rig track → **Bake To Animation Sequence** → choose output path and frame range
3. A new `.uasset` Animation Sequence is created; the Control Rig track is replaced (or kept)
4. Baked animation is portable and performant — use for crowd sims, AnimToTexture, MRQ renders
5. To re-edit: right-click the Animation Sequence track → **Link To Control Rig** → choose your rig
6. A live Control Rig layer is added on top of the baked sequence for additive editing
7. Re-bake after edits to update the base animation asset
8. **Rule of thumb:** keep live Control Rig during production; bake for delivery/export

### UE Systems / Blueprints / Settings
`Bake To Animation Sequence` (right-click Control Rig track) → creates portable .uasset from live rig
`Link To Control Rig` (right-click Anim Sequence track) → re-attach rig for editing
`Control Rig Sub-Sequence` → live, editable; heavier viewport cost
`Animation Sequence` → baked, fast, portable; used for AnimToTexture, crowd instancing
Frame range and bone filter selectable at bake time

### Difficulty
Intermediate

### UE Version
UE5

### Tags
animation, control-rig, sequencer, pipeline, intermediate

---

## Related Entries
- `references/control-rig-animation.md` — Control Rig full reference
- `tutorials/non-destructive-animation-in-ue5-layered-control-rigs-explained.md` — layer rigs for non-destructive edits
- `references/sequencer-cinematics.md` — Sequencer pipeline