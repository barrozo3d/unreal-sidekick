---
title: Unreal Engine 5: Animation Cinematic Production Overview
source: YouTube
url: https://www.youtube.com/watch?v=ywtvn1uncZo
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["animation", "sequencer", "cinematics", "pipeline", "beginner"]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-5-animation-cinematic-production-overview/
frame_count: 4
---

# Unreal Engine 5: Animation Cinematic Production Overview

**Source:** [YouTube](https://www.youtube.com/watch?v=ywtvn1uncZo)
**Author:** Unreal Engine
**Duration:** 11m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hi, my name is Sir. You might know me as Sir Wade if you've ever seen any of my videos before. I have a YouTube channel that covers animation, exploring new workflows and creative technology, and I provide professional industry training from Maya, Blender, and Unreal Engine artist and animators. So if you want to go even deeper than what we're going to cover in these videos, you can find me on my YouTube channel or on my course website. But for now, I'm going to get you started with the animation tools inside of Unreal Engine using the brand new Animation Sample project that just came out. Let's jump in. All right, so when we load up the project, this is what we're looking at. This is our welcome level. We've got a couple of characters hanging out here, and if you want to see them in their idols, we can just hit play up at the top. Now, all of these characters, the cinematic we're going to look at and the entire world that we have to access, these were all developed by Agora Studio. They did a great job with all these assets, and now we have some stylized characters to play with, which is great. We also have a robot who's not pictured here, because this is a place for the good guys...

**Frame:** tutorials\frames\unreal-engine-5-animation-cinematic-production-overview\frame_000.jpg


---

## Structured Notes

### Core Technique
High-level overview of cinematic animation production in UE5 using the ACOM Animation Sample Project — project structure, Level Sequences, sub-sequences, and the animation editing workflow.

### Summary
First video in Sir Wade's UE5 Animation tutorial series using the ACOM (Agora Studio) animation sample project available on FAB. Overview of the full project: welcome level, stylized characters (Beta + Gamma robots), the master Level Sequence structure, how shots are organized as sub-sequences, and what tools will be covered in subsequent videos. Entry point for the entire series.

### Key Steps
1. Download the **ACOM Animation Sample Project** from Fab (free)
2. Open project → `Welcome Level` shows idle characters; hit Play to preview
3. Open **Level Sequences** (Content Browser → Episodes → IntroBeta) to find the main cinematic sequence
4. Inspect the **Master Sequence** → contains a Shot Track with individual shot sub-sequences
5. Open a shot sub-sequence → see character tracks, camera tracks, Control Rig sub-sequences
6. Switch to **Animation Mode** (Sequencer toolbar toggle) to enable interactive posing
7. Character details: stylized robot by Agora Studio; uses Modular Control Rig + UE physics for secondary motion
8. Following videos in series cover: animation data (baking), curve editor, constraints, motion trails, layers

### UE Systems / Blueprints / Settings
`ACOM Animation Sample Project` (Fab, free) → full cinematic production project by Agora Studio
`Master Level Sequence` → contains Shot Track → individual shot sub-sequences
`Animation Mode` (Sequencer toolbar) → enables interactive Control Rig posing
`Modular Control Rig` → character rig used for Beta/Gamma robots
`ACOM Project structure`: Episodes → IntroBeta → master sequence → shot sub-sequences

### Difficulty
Beginner

### UE Version
UE5

### Tags
animation, sequencer, cinematics, pipeline, beginner

---

## Related Entries
- `references/sequencer-cinematics.md` — Sequencer and Level Sequence reference
- `tutorials/advanced-ue5-cinematic-workflow-camera-rigs-custom-viewports.md` — sub-sequences deep dive
- `tutorials/level-management-sub-levels-spawnables-possessibles-in-ue5.md` — level structure