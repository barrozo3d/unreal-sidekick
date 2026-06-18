---
title: Level Management: Sub-Levels, Spawnables, Possessibles in UE5
source: YouTube
url: https://www.youtube.com/watch?v=yOcgYMcxr3Q
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["sequencer", "cinematics", "narrative", "pipeline", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/level-management-sub-levels-spawnables-possessibles-in-ue5/
frame_count: 4
---

# Level Management: Sub-Levels, Spawnables, Possessibles in UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=yOcgYMcxr3Q)
**Author:** Unreal Engine
**Duration:** 15m48s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** All right, now in this video, we're gonna go ahead and explore the level itself and we're gonna update that and see how it interacts with the level sequences in the actual cinematic project. So right off the bat, moving around our level, we can see that there's a bunch of different assets. I wanna give a few helpful pointers for working with a level like this. One thing that's worth mentioning is the way that this level is constructed. If I go to window levels, which might actually be open by default for you already, but in the top right corner, I have this levels window panel. And you can see that there's a whole bunch of sub-levels all being referenced inside of our main world here. Now, you'll probably figure this out by playing with it, but if I take, for example, the gym lights and turn them off, you'll see that it actually disables the lighting for this room. However, if I take something like the warehouse lights and turn them off, you won't notice a difference because the warehouse is back through this door here. To put it in that off, you'll see that the lighting changes a bit. It's still pretty dark, but you get the idea. And so what we have is a folder full of lighting an...

**Frame:** tutorials\frames\level-management-sub-levels-spawnables-possessibles-in-ue5\frame_000.jpg


---

## Structured Notes

### Core Technique
Level organization for cinematic productions — Sub-Levels in the Levels panel for modular asset/lighting management, and Spawnables vs. Possessibles in Sequencer for actor lifecycle control.

### Summary
First video in the ACOM Animation Hub series (world/level overview). Covers the Levels panel (Window > Levels) and using Sub-Levels to isolate lighting, geometry, and assets per zone — toggle entire level chunks on/off. Then explains Sequencer's Spawnables (spawned by Sequencer; exist only during playback; portable between levels) vs. Possessibles (already in level; Sequencer takes control; level-specific). Critical distinction for cinematic production flexibility.

### Key Steps
1. Open **Window → Levels** to see the sub-level hierarchy for the persistent world
2. Each sub-level contains isolated content (lighting, environment geometry, props) — toggle visibility/loading per sub-level
3. To control sub-levels from Sequencer: add a **Level Visibility Track** → reference specific sub-levels by name
4. **Spawnables**: in Sequencer, click the actor's track header `+` → `Convert to Spawnable` → now the actor is managed by Sequencer (spawns/despawns with the sequence)
5. **Possessibles**: default mode — Sequencer takes control of an actor that already exists in the level
6. Use **Spawnables** for characters/cameras that move between shots or sequences (portable)
7. Use **Possessibles** for environment actors that are permanently placed in the level
8. **Level Streaming Volumes** or Blueprint can auto-load/unload sub-levels based on player/camera position

### UE Systems / Blueprints / Settings
`Window → Levels` panel → sub-level manager; toggle load/visibility per sub-level
`Level Visibility Track` (Sequencer) → load/unload sub-levels at specific frames
`Spawnable` (Sequencer) → actor created and destroyed by Sequencer; portable; green 'S' icon
`Possessible` (Sequencer) → pre-placed level actor; Sequencer controls properties only; yellow 'P' icon
`World Composition` / `World Partition` → alternative streaming for open-world projects

### Difficulty
Intermediate

### UE Version
UE5

### Tags
sequencer, cinematics, narrative, pipeline, intermediate

---

## Related Entries
- `references/narrative-blueprints.md` — level streaming and Blueprint-triggered cinematics
- `references/sequencer-cinematics.md` — Sequencer track types and sub-sequences
- `tutorials/advanced-ue5-cinematic-workflow-camera-rigs-custom-viewports.md` — sub-sequences structure