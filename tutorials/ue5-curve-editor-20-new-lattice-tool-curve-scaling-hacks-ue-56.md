---
title: UE5 Curve Editor 2.0 New Lattice Tool & Curve Scaling HACKS (UE 5.6)
source: YouTube
url: https://www.youtube.com/watch?v=VD_cfVvMs6Y
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE 5.6"
tags: ["animation", "sequencer", "intermediate", "ue5-6"]
extraction_status: complete
frames_dir: tutorials/frames/ue5-curve-editor-20-new-lattice-tool-curve-scaling-hacks-ue-56/
frame_count: 4
---

# UE5 Curve Editor 2.0 New Lattice Tool & Curve Scaling HACKS (UE 5.6)

**Source:** [YouTube](https://www.youtube.com/watch?v=VD_cfVvMs6Y)
**Author:** Unreal Engine
**Duration:** 16m40s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome back, my name is Sir, and in these videos, I'm going to walk you through some of the different animation tools we have available to us in Unreal Engine. We're going to be using the ACOM Animation Sample project to dive into some files. And if we're going to remind her that if you're just joining us, this is technically the third set of videos in this series, so if you want to get a little bit more introductory stuff, be sure to check out the videos that have come before. Now, let's go ahead and dive in to Unreal Engine. In this video, I'm going to walk you through some of the different features and tools we have inside of Unreal's Curve Editor to adjust our splines while we're animating, including some of the shiny new features that were introduced in 5.6. So right now, I'm in shot 10. That is inside the episode folder intro beta shot 10 here, and this is the level sequence that I'm in. So here we've got the character beta, brush it a teeth, hang it out, and eventually, being notified that there are some robots breaking into the compound. Now, in this particular shot, I am actually looking at the Control Rig sub-sequence. I've talked about this in some previous videos, but ...

**Frame:** tutorials\frames\ue5-curve-editor-20-new-lattice-tool-curve-scaling-hacks-ue-56\frame_000.jpg


---

## Structured Notes

### Core Technique
Curve Editor 2.0 features in UE 5.6 — Lattice Tool for multi-key region manipulation and Curve Scaling hacks for non-uniform timing adjustment across multiple curves simultaneously.

### Summary
Tutorial on the Curve Editor enhancements in UE 5.6, particularly the new Lattice Tool which lets you draw a bounding region around multiple keys and warp them together (compress timing, add easing, reshape arcs non-destructively). Also covers curve scaling shortcuts for scaling value ranges and timing widths of selected key groups.

### Key Steps
1. In Animation Mode, open the **Curve Editor** (bottom panel or `Ctrl+Alt+C`)
2. Select a control rig sub-sequence to display its curves
3. **Lattice Tool** (new 5.6): click the lattice icon in the Curve Editor toolbar
4. Draw a selection box around the keys you want to shape; a lattice cage appears
5. Drag lattice handles to warp the timing/value of all enclosed keys simultaneously
6. **Curve Scaling**: select keys across multiple curves → use `Ctrl+drag` on the time axis to scale timing
7. Use `Alt+drag` on the value axis to scale the value range of selected keys
8. **Buffer Curves**: see `tutorials/ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks.md` for save/recall

### UE Systems / Blueprints / Settings
`Curve Editor` (Animation Mode → bottom panel) → direct spline editing for all rig controls
`Lattice Tool` (5.6+) → multi-key region warp; draw box, drag handles to reshape
`Curve Scaling` → `Ctrl+drag` time axis (scale timing); `Alt+drag` value axis (scale values)
`Control Rig Sub-Sequence` → access for per-curve key data
`ACOM Animation Sample Project` → demo project used in tutorial

### Difficulty
Intermediate

### UE Version
UE 5.6

### Tags
animation, sequencer, intermediate, ue5-6

---

## Related Entries
- `tutorials/ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks.md` — Buffer Curves and Smart Snap
- `references/control-rig-animation.md` — Control Rig reference