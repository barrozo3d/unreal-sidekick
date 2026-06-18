---
title: Stylized Animation Control Rig Characters in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=WMKvwVIuFS4
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["animation", "control-rig", "rigging", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/stylized-animation-control-rig-characters-in-unreal-engine-5/
frame_count: 4
---

# Stylized Animation Control Rig Characters in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=WMKvwVIuFS4)
**Author:** Unreal Engine
**Duration:** 13m23s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Now at this point, we've gone over the file and the project is a whole. We've gone over the world, the level itself. We've gone through the sub sequences and seen how to mess with level sequences, adjust shots independently, and adjust the camera rigs. Also, very importantly, we've seen how to make different viewport layouts. So we can actually see our camera and our workspace in a perspective window at the same time. In this video, we're going to focus on the characters. We're going to kind of break free of the regular cinematic that we've been looking at, because we're going to spend more time in here. But now we want to look specifically at our characters. Let's take a look at beta. So what I'm going to do is I'm actually just going to close out of my sequencer. And in fact, we don't even need to stay in this level. We can if we want to, I'll go ahead and switch this back to a perspective full view. We could just drop beta here into the world, or we can do this control end in just a basic level. Both work. I'll show you each. To take a look at our character, I'm going to just control space bar, jump back to content, assets, characters, and we'll look at the beta character. Now h...

**Frame:** tutorials\frames\stylized-animation-control-rig-characters-in-unreal-engine-5\frame_000.jpg


---

## Structured Notes

### Core Technique
Exploring and animating a Control Rig character (non-MetaHuman) in UE5 — opening the character asset, inspecting the Modular Control Rig setup, and beginning keyframe animation in Animation Mode.

### Summary
Third video in the ACOM Animation Hub series. Focuses on the character Beta from the ACOM sample — a stylized non-MetaHuman robot character with a full Modular Control Rig. Shows how to open a character's Control Rig via the Content Browser, inspect IK/FK controls, switch to Animation Mode in Sequencer, and start posing/keyframing. Discusses FK vs IK tradeoffs for stylized characters.

### Key Steps
1. Find the character asset in the Content Browser: `Assets/Characters/[CharacterName]`
2. Double-click to open the **Skeletal Mesh** editor → inspect the rig hierarchy
3. Drag the character into a **Level Sequence** in Sequencer
4. On the character track, click **+ Sub-Sequence → Control Rig** to add an animation sub-sequence
5. Select **Modular Control Rig** (or the character's specific full-body rig)
6. Enter **Animation Mode** (Sequencer toolbar) to enable interactive posing
7. Select controls in the viewport or the **Anim Outliner** panel
8. Use `G` key to toggle between FK (rotate-only) and IK (position-based) control modes
9. Set keys with `S` (all controls) or `Ctrl+S` (selected controls only)

### UE Systems / Blueprints / Settings
`Content Browser → Assets/Characters` → character skeletal mesh location
`Modular Control Rig` → pre-built IK/FK module library; drag controls in viewport
`Anim Outliner` (Animation Mode) → hierarchical list of all rig controls
`G key` → FK/IK toggle for limb controls
`S` → set keys for all visible controls; `Ctrl+S` → selected only
`Animation Mode` (Sequencer toolbar) → activates posing tools

### Difficulty
Intermediate

### UE Version
UE5

### Tags
animation, control-rig, rigging, intermediate

---

## Related Entries
- `references/control-rig-animation.md` — Modular Control Rig and IK reference
- `tutorials/baking-animation-in-ue5-control-rig-to-animation-sequence-back.md` — baking the finished animation