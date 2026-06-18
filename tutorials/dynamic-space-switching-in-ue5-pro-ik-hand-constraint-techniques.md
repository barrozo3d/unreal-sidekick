---
title: DYNAMIC Space Switching in UE5: Pro IK Hand Constraint Techniques
source: YouTube
url: https://www.youtube.com/watch?v=9AavXj11Iw4
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["animation", "control-rig", "rigging", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/dynamic-space-switching-in-ue5-pro-ik-hand-constraint-techniques/
frame_count: 4
---

# DYNAMIC Space Switching in UE5: Pro IK Hand Constraint Techniques

**Source:** [YouTube](https://www.youtube.com/watch?v=9AavXj11Iw4)
**Author:** Unreal Engine
**Duration:** 6m32s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Well, go back. In this video, we're going to take a look at some of the posing tools available to us, specifically space switching. Now, space switching is something that often rigs have built in, but I'm real has some really cool features to be able to dynamically adjust where different controls are looking for their parent relationships. If you want to have IK hands, switch into different parts of the body to move alongside things or be locked to certain parts of the body. It's very cool. So, we're going to take a look at that full system and I'll show you how it works. So here we are in shot 65. We've got the live rig with beta grabbing this big canister and chucking it once again. So, I'm going to come zoom in on this hand. Now, this hand is currently an IK, right? It's just sitting there. It's not moving the canister. We don't have any constraints active right now. We'll do that in some follow-up videos. But what I want to do is I want to move this IK hand around, or at least I want to maybe move the body with that IK hand in mind. And so, one of the things that is so good about IK hands, as we probably all know, is that it's locked in space, right? That hand is locked and I c...

**Frame:** tutorials\frames\dynamic-space-switching-in-ue5-pro-ik-hand-constraint-techniques\frame_000.jpg


---

## Structured Notes

### Core Technique
Dynamic Space Switching for IK hands in UE5 — changing the IK parent space between body parts (world, root, spine, chest) on a per-key basis directly in the viewport.

### Summary
Demonstrates UE5's built-in space switching system for IK controls in Control Rig. Shows how to switch an IK hand from world-locked to body-relative space mid-animation — essential for contact/holding shots — using the control's space switch property in the Anim Outliner. Covers the difference between world-space IK and body-space IK and when each is appropriate.

### Key Steps
1. In Animation Mode, select an IK hand control in the viewport
2. In the **Anim Outliner**, find the control → look for the `Space` property or right-click → **Switch Space**
3. Available spaces typically include: `World`, `Root`, `Pelvis`, `Spine`, `Chest`, `Parent`
4. Key the current space at the frame before switching (to preserve position)
5. Advance one frame, switch to the new space → key to lock
6. The control will now move with the new parent space from that frame forward
7. **Tip:** when a character grabs an object, switch IK hand space to the object's bone/socket so the hand sticks automatically
8. Combine with Parent Constraints for prop-holding shots

### UE Systems / Blueprints / Settings
`Space Switching` property (IK Control in Control Rig) → parent space selector: World / Root / Pelvis / Spine / Chest
`Anim Outliner` → shows space property per control; key directly here
`IK Hand Control` → stays locked in chosen space; great for contact moments
`FK Hand Control` → body-relative by default; use when hand does not need to stay fixed in world

### Difficulty
Intermediate

### UE Version
UE5

### Tags
animation, control-rig, rigging, intermediate

---

## Related Entries
- `references/control-rig-animation.md` — full IK/FK and Control Rig reference
- `tutorials/ue5-constraints-are-easy-parent-constraint-workflow-for-animators.md` — Parent Constraints for prop attachment