---
title: Mastering the UE5 Tweener Tool: Push Pull & Overshoot Animation
source: YouTube
url: https://www.youtube.com/watch?v=oUPOBsCrWwE
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["animation", "sequencer", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/mastering-the-ue5-tweener-tool-push-pull-overshoot-animation/
frame_count: 4
---

# Mastering the UE5 Tweener Tool: Push Pull & Overshoot Animation

**Source:** [YouTube](https://www.youtube.com/watch?v=oUPOBsCrWwE)
**Author:** Unreal Engine
**Duration:** 11m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** In this video, I'm going to walk you through each of the different modes that we have in the tween tool to adjust the keys on your curves and start blending between your different poses. Let's talk about the tween tool. I think a lot of us are familiar with it and how it works in other tools. Let's dive into what Unreal has to offer us. So here I am in shot number, what shot is this? This is shot 65. We've got beta here, grabbing and lifting this big old thing and throwing it. I've extended the shot a little bit so that we have a little more runtime at the end just to sit with the pose. Now, what we're going to do is I'm going to show you how the throw can be modified using the tween tools. With all this motion in mind, I want to just grab the main controls to pilot this animation. So I'm going to go ahead and just grab maybe the body. I don't know if the hips are in use, but I'll grab that too. I'll grab the upper shoulder torso area, grab the neck, grab the head. I'm going to grab the hands. This one is currently using IK, which means I also need the pole vector for the elbow. I'm going to need this hand, which is an FK. So I'll grab the hand, the elbow, the upper arm, and then c...

**Frame:** tutorials\frames\mastering-the-ue5-tweener-tool-push-pull-overshoot-animation\frame_000.jpg


---

## Structured Notes

### Core Technique
Tween Tool in UE5 Animation Mode — Push, Pull, Overshoot, Average, and Ease In/Out modes for non-destructively adjusting timing and pose blending between keyframes.

### Summary
Covers each mode of UE5's Tween Tool for animators: Push (extend toward next key), Pull (snap toward previous key), Overshoot (exaggerate beyond next key), Average (blend to 50% midpoint), and Ease variants. Demonstrated on a throwing animation to add anticipation and follow-through without re-keying. Each mode is accessible in the Animation toolbar.

### Key Steps
1. In Animation Mode, select the controls to tween
2. Scrub the timeline to the frame you want to adjust
3. Open the **Tween Tool** from the Animation toolbar (or `T` shortcut)
4. **Pull mode** (drag left): moves current pose toward the previous key — useful for anticipation
5. **Push mode** (drag right): moves current pose toward the next key — useful for follow-through
6. **Overshoot mode**: moves pose PAST the next key — adds exaggeration/snap to a hit
7. **Average mode**: blends current pose toward the mathematical midpoint between prev/next keys — smooths breakdowns
8. **Ease In / Ease Out**: slides the tangent timing without moving the pose value
9. Drag the Tween slider left/right to the desired amount; release to commit the tweak

### UE Systems / Blueprints / Settings
`Tween Tool` (Animation Mode toolbar) → T shortcut or toolbar icon
Pull → toward previous key; Push → toward next key; Overshoot → past next key
Average → 50% midpoint blend; Ease In/Out → tangent timing adjustment
Works on selected controls only — select fewer controls for targeted tweaks

### Difficulty
Intermediate

### UE Version
UE5

### Tags
animation, sequencer, intermediate

---

## Related Entries
- `references/control-rig-animation.md` — Control Rig animation tools
- `tutorials/ue5-curve-editor-20-new-lattice-tool-curve-scaling-hacks-ue-56.md` — Curve Editor for precision key editing