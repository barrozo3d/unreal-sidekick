---
title: UE5 Curve Editor SECRETS: Buffer Curves & Smart Snap Keyframe Tricks
source: YouTube
url: https://www.youtube.com/watch?v=9g0K4GOACis
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["animation", "sequencer", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks/
frame_count: 4
---

# UE5 Curve Editor SECRETS: Buffer Curves & Smart Snap Keyframe Tricks

**Source:** [YouTube](https://www.youtube.com/watch?v=9g0K4GOACis)
**Author:** Unreal Engine
**Duration:** 14m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome back. In this video, we're going to take a look at some different techniques to work with animation data, specifically when it comes to the curve editor. And we're going to take a look at shot 40. So in our project here, I'm inside of shot number 40 right here. This is the level sequence I've opened and we're taking a look at the characters running down the corridor. Now I'm going to go ahead and just work with the anim work project. I've also muted the baked animation subsequent and I've brought back up the control rig live anim work subsequent because inside of here is the beta character with all of the original keyframe data from the original animator. So with this in mind, there's one other thing I want to do and that is to actually add a camera cuts track into this sequence right here. I don't have an easy way to get in and out of this camera view. And so if I add a camera cut track, because I'm sort of breadcrumbing my way back down into this level sequence, the subsequent here, I am able to access the camera using this camera cut track to get in and out. Now this works even though I don't have a camera in this particular sequence because I'm loaded in through this la...

**Frame:** tutorials\frames\ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks\frame_000.jpg


---

## Structured Notes

### Core Technique
Curve Editor workflow secrets — Buffer Curves (save/restore curve states as comparison reference) and Smart Snap (frame-accurate key placement with intelligent snapping).

### Summary
Reveals two powerful but underused Curve Editor features: Buffer Curves, which lets you save the current state of selected curves as a ghost reference and swap back and forth for A/B comparison; and Smart Snap, which intelligently snaps keys to nearby frames, handles, or curve intersections. Also covers a technique for adding a Camera Cut Track to a sub-sequence for quick camera navigation when editing deeply nested shots.

### Key Steps
1. In the Curve Editor, select the curves/keys you want to save as reference
2. **Buffer Curves**: right-click → **Buffer Curves** (or the Buffer button in toolbar) → curve state saved as ghost
3. After editing, compare by right-click → **Swap Buffer** — toggles between current and saved state
4. Use Buffer Curves for A/B: save a good timing, experiment, swap back if experiment fails
5. **Smart Snap**: enable the snap icon in Curve Editor toolbar → when dragging keys, they snap to nearby frames or curve intersections
6. Smart Snap respects the sequence frame rate; avoids sub-frame keys accidentally
7. **Camera Cut Track trick**: when editing a nested sub-sequence without a camera, add a Camera Cut Track pointing to the parent camera → enables quick camera view toggle inside the sub-sequence

### UE Systems / Blueprints / Settings
`Buffer Curves` (Curve Editor right-click) → save/restore curve state for A/B comparison; Swap Buffer toggles
`Smart Snap` (Curve Editor toolbar) → intelligent key snapping to frames/handles/intersections
`Camera Cut Track` in sub-sequence → enables camera view access when navigating nested sequences
`Curve Editor` → accessible via bottom panel in Animation Mode

### Difficulty
Intermediate

### UE Version
UE5

### Tags
animation, sequencer, intermediate

---

## Related Entries
- `tutorials/ue5-curve-editor-20-new-lattice-tool-curve-scaling-hacks-ue-56.md` — Lattice Tool and curve scaling
- `references/sequencer-cinematics.md` — Sequencer sub-sequence workflow