---
title: How to Create the ULTIMATE Previz with Polycam, Metahumans, and Move.AI in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=ova-8EAD8eg
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.x"
tags: [previz, polycam, lidar-scan, metahuman, move-ai, mocap, pre-production, digital-set, short-film, ue5]
extraction_status: complete
frames_dir: tutorials/frames/how-to-create-the-ultimate-previz-with-polycam-metahumans-and-moveai-in-unreal-e/
frame_count: 4
---

# How to Create the ULTIMATE Previz with Polycam, Metahumans, and Move.AI in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=ova-8EAD8eg)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 9m33s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** What if I told you the future of filmmaking isn't just about what happens on set, but what happens inside a video game engine first? Recently, my production company took on a challenging project, a short film about Alzheimer's disease that required complex camera movements, intricate dance sequences, and seamless transitions between memories. But instead of creating a traditional shot list or storyboard, I tried something different. I decided to shoot the entire film before I shot the actual film. Using Unreal Engine, Performance Capture, and a LiDAR scan of our location, I created a complete digital version of our story. Crazy? Maybe. Overkill? I thought so too. But what happened next completely changed how I think about filmmaking? In the next few minutes, I'm going to show you exactly how I turned a real house into a digital set, acted out all the roles myself, and used a video game engine to plan every single shot of our film. More importantly, I'll show you whether this elaborate process actually made our final film better. And the answer might surprise you. Now I'd used Unreal Engine to create more basic pre-visits for a few projects before. Early last year, we shot a differe...

**Frame:** tutorials\frames\how-to-create-the-ultimate-previz-with-polycam-metahumans-and-moveai-in-unreal-e\frame_000.jpg


---

## Structured Notes

### Core Technique
LiDAR scan a real location with Polycam, import the resulting 3D mesh into Unreal Engine as a digital set, then populate it with MetaHumans driven by Move.AI performance capture to previz an entire short film before shooting the real version — covering every shot, camera movement, dance sequence, and transition.

### Summary
Charlie Driscoll's production company uses Unreal Engine 5 as a full previz tool for an Alzheimer's short film requiring complex camera movements, dance sequences, and memory transitions. The real house location is LiDAR scanned with Polycam and imported into UE5 as a digital set. Driscoll acts all roles himself using Move.AI performance capture and MetaHuman Animator, building a complete digital version of the film before principal photography. The video argues this elaborate previz process — which could seem like overkill — actually made the final live-action film substantially better by revealing shot problems, timing issues, and creative solutions impossible to anticipate from a traditional shot list or storyboard.

### Key Steps
1. LiDAR scan real location using Polycam app (smartphone LiDAR); export as 3D mesh.
2. Import Polycam mesh into UE5 as digital set representing the actual shooting location.
3. Act all roles using Move.AI body capture and MetaHuman Animator face capture; retarget animations to MetaHumans.
4. Block out every shot in Sequencer: camera movements, dance sequences, memory transitions.
5. Iterate on edit in Sequencer until complete digital film is locked.
6. Use digital previz as shot list and creative reference for live-action principal photography.
7. Compare digital previz version against final live-action film to validate process.

### UE Systems / Blueprints / Settings
- Polycam (LiDAR scanning app for iOS/Android; mesh export for UE)
- Move.AI body motion capture (multi-cam or single-cam, unspecified in transcript)
- MetaHuman Animator (face capture)
- Level Sequencer (full film blocking: cameras, character animation, transitions)
- MetaHumans (character placeholders for all roles)
- Cine Camera Actor (previz camera work)

### Difficulty
Intermediate

### UE Version
5.x

### Tags
previz, polycam, lidar-scan, metahuman, move-ai, mocap, pre-production, digital-set, short-film, ue5

---

## Related Entries
- `cinematic-motion-capture-with-move-one-and-metahuman-animator---unreal-engine-54.md` — full pipeline tutorial for the mocap and MetaHuman workflow used in this previz
- `how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator.md` — references this video as an example of previz work
- `how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng.md` — earlier pipeline overview of Move.AI + MetaHuman workflow
