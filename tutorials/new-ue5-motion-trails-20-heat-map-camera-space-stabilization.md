---
title: NEW UE5 Motion Trails 2.0: Heat Map & Camera Space Stabilization
source: YouTube
url: https://www.youtube.com/watch?v=erHPJ8eoXyY
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE 5.6"
tags: ["animation", "sequencer", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/new-ue5-motion-trails-20-heat-map-camera-space-stabilization/
frame_count: 4
---

# NEW UE5 Motion Trails 2.0: Heat Map & Camera Space Stabilization

**Source:** [YouTube](https://www.youtube.com/watch?v=erHPJ8eoXyY)
**Author:** Unreal Engine
**Duration:** 9m43s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey there, welcome back for some more Unreal Animation training. I'm Sir Wade and we're going to take a look at the ACOM Animation Sample Project one last time for a few more videos. This is the fourth series in case you're watching all of them. And we're going to dive into the technical animation tools this time around. In this particular video, we're going to start off with the new Motion Trails that we're introduced in Unreal Engine 5.6, which are very powerful. In case you're just joining us, this is technically the fourth set of videos in this series. And so if you're looking for something to kind of ease in, catch up on some of the others and come on back. But here we are in the Sample Project. I am in Shot 50, which is this awesome shot where he breaks through the door. We've got Gamma jumping through the little gap that gets created and Beta is forced and open the doors. We're going to cover the constraints and other stuff in some later videos, but for now, let's focus on the Motion Trails using Gamma. So here he comes, hopping through the little gap in the door. Let's go ahead and leave our camera behind and we can see him pop on through. There he goes. So I'm going to com...

**Frame:** tutorials\frames\new-ue5-motion-trails-20-heat-map-camera-space-stabilization\frame_000.jpg


---

## Structured Notes

### Core Technique
Motion Trails 2.0 (introduced UE 5.6) — Heat Map visualization and Camera Space Stabilization modes for evaluating animation arc quality and viewport stability.

### Summary
Official UE tutorial on the new Motion Trails system added in 5.6. Covers the Heat Map mode which color-codes trail speed (useful for spotting pops/holds), and Camera Space Stabilization which keeps trails relative to the camera for cleaner arc evaluation even on moving cameras. Part of the ACOM Animation Sample project tutorial series.

### Key Steps
1. With a character/control selected in Sequencer, open **Motion Trails**: `Viewport → Show → Advanced → Motion Trails`
2. Select the controls to visualize (IK hands, feet, head) and enable Motion Trails for them
3. Switch to **Heat Map mode** in the Motion Trails settings panel — trail colors indicate speed (cool = slow, hot = fast)
4. Use Heat Map to spot timing issues: sudden color jumps = pops; extended cool regions = unintended holds
5. Enable **Camera Space Stabilization** — trails are now evaluated relative to the active camera rather than world space
6. Camera Space mode makes arc evaluation meaningful even on camera-moving shots
7. Adjust keyframes based on Heat Map feedback; re-evaluate trail to verify fix

### UE Systems / Blueprints / Settings
`Motion Trails` (Viewport Show flags) → visualize bone/control arcs over time
`Heat Map Mode` → color-codes trail by velocity; cold=slow, hot=fast; use to spot pops/holds
`Camera Space Stabilization` → evaluates trails relative to camera (5.6+), improves arc review on moving shots
`ACOM Animation Sample Project` (Fab) → reference project for this tutorial series

### Difficulty
Intermediate

### UE Version
UE 5.6

### Tags
animation, sequencer, intermediate, ue5-6

---

## Related Entries
- `references/control-rig-animation.md` — Control Rig animation tools
- `references/sequencer-cinematics.md` — Sequencer workflow