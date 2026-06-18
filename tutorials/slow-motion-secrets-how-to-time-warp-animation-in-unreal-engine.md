---
title: Slow Motion SECRETS! How to Time Warp Animation in Unreal Engine
source: YouTube
url: https://www.youtube.com/watch?v=d-_hv7IXjkM
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["animation", "sequencer", "cinematics", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/slow-motion-secrets-how-to-time-warp-animation-in-unreal-engine/
frame_count: 4
---

# Slow Motion SECRETS! How to Time Warp Animation in Unreal Engine

**Source:** [YouTube](https://www.youtube.com/watch?v=d-_hv7IXjkM)
**Author:** Unreal Engine
**Duration:** 10m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** In this video, I'm going to show you how to do time warp, slow-mo adjustments to the timing of your animation. Now, in this project, we have that happening, but it's not happening with sort of the Unreal Engine tool method. It's happening manually. The animator's manually animated the slow motion, with just slower keyframe data and just general animation timing. But let's say that you had animated something and you realize later, I want this slow motion moment. So what I'll do is I'm actually going to leave this shot and go find another shot where maybe like here we've got these different moments of great impact and fight sequences. So let's add some slow motion to this. But when you shot 60 as our example, he comes in, he uppercuts this dude and does this helicopter spin. Let's try some stuff. We can do one of these punches, we can obviously do the spin, or maybe we'll do this wayam right there. I really like this last punch because it's got all this cool chromatic aberration, effects drawing stuff there. I feel like that'd be sweet. So maybe we'll do that punch in slow motion. Now in this particular case, because we're looking at the full production, right, we have this whole lis...

**Frame:** tutorials\frames\slow-motion-secrets-how-to-time-warp-animation-in-unreal-engine\frame_000.jpg


---

## Structured Notes

### Core Technique
Time-warping animation in Sequencer — using the `Time Warp` track and `Rate Scale` to create non-destructive slow motion moments on existing animation clips.

### Summary
Covers how to add slow-motion to pre-existing animation in Sequencer without re-animating. Demonstrates the Time Warp track on a control rig sub-sequence to retime specific hit/impact moments, and Rate Scale on animation clips for constant slow-down. Includes camera/chromatic aberration integration for stylized slo-mo.

### Key Steps
1. Open the Level Sequence containing the shot; locate the control rig sub-sequence
2. Right-click the animation/control rig track → **Add Time Warp Track**
3. Keyframe the Time Warp value: `1.0` = normal, `0.25` = 25% speed (slow motion)
4. Add easing keys around the slow-mo section to smoothly ramp in and out
5. Alternatively, select an animation clip in Sequencer → right-click → **Edit Section** → adjust `Rate Scale` (0.25 = 4x slower)
6. For camera: add chromatic aberration via Post Process Volume → `Lens → Chromatic Aberration Intensity` keyframed to peak at slo-mo moment
7. Preview in Sequencer (Shift+Space) to verify timing; adjust Time Warp keys as needed

### UE Systems / Blueprints / Settings
`Time Warp Track` (Sequencer) → non-destructive retiming of animation sections
`Rate Scale` (animation clip property) → constant speed multiplier for entire clip
`Post Process Volume → Chromatic Aberration` → slo-mo visual enhancement
`Control Rig Sub-Sequence` → where Time Warp is most commonly applied

### Difficulty
Intermediate

### UE Version
UE5

### Tags
animation, sequencer, cinematics, intermediate

---

## Related Entries
- `references/sequencer-cinematics.md` — Sequencer track types and timeline workflow
- `references/control-rig-animation.md` — Control Rig sub-sequence structure