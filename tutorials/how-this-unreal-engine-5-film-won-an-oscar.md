---
title: How this Unreal Engine 5 film won an Oscar
source: YouTube
url: https://www.youtube.com/watch?v=eOQM1Tbyw0Y
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [cinematics, rendering, pipeline, beginner]
extraction_status: complete
frames_dir: tutorials/frames/how-this-unreal-engine-5-film-won-an-oscar/
frame_count: 4
---

# How this Unreal Engine 5 film won an Oscar

**Source:** [YouTube](https://www.youtube.com/watch?v=eOQM1Tbyw0Y)
**Author:** Josh Toonen
**Duration:** 19m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Did you know last year the Oscar for best animated short film went to Wars Over? And it was rendered entirely in Unreal Engine 5? Well, today I want to break this down and show you the filmmaking and visual effect secrets that are hidden in plain sight that you can use to make your own animations and live action short films. I think this is one of the best examples of show don't tell. There's almost no dialogue at all in this entire film, but the colors, the characters, and the poses of each character tell the story. This was written and directed by the talented Dave Mullins. A 20 year Pixar Animation Veteran, and animated by What It Effects, creating a deceptively simple story with beautiful animation. But the reality is, simplicity is never simple. It's hard work. I spent the last 10 years working on visual effects on movies like Star Wars, Rise of Skywalker, and Across the Spider-Verse. And the best way to learn and train your creative eye is to break down movies frame by frame and deconstruct them to understand how they did it. So rather than do this myself, let's do it together and take a look at Wars Over. We use Unreal Engine as the primary ecosystem for the short, structuri...

**Frame:** tutorials\frames\how-this-unreal-engine-5-film-won-an-oscar\frame_000.jpg


---

## Structured Notes

### Core Technique
Conceptual breakdown of "Wars Over," an Oscar-winning short film made entirely in Unreal Engine 5, examining the production pipeline and creative decisions that enabled a Hollywood-quality result from a small team.

### Summary
Josh Toonen reviews the key creative and technical decisions behind the Academy Award-winning UE5 short film "Wars Over," demonstrating that photorealistic filmmaking is achievable without a large studio. The video is primarily inspirational and conceptual rather than a step-by-step tutorial, discussing how UE5's real-time rendering eliminated traditional rendering bottlenecks. Viewers gain an understanding of what a complete UE5 film pipeline looks like at an award-winning level.

### Key Steps
1. Understand the production pipeline: concept → previz in UE5 → animation → lighting → rendering — all within a single UE5 project.
2. Leverage UE5's real-time rendering to iterate on lighting and camera angles instantly rather than waiting for offline renders.
3. Use Lumen for global illumination and Nanite for high-detail environment geometry without manual LOD management.
4. Treat UE5 as a complete film production studio: design, animate, light, and render all in one application.
5. Study the film's visual language — tight compositions, motivated lighting, and restrained VFX all contribute to the Oscar-quality result.

### UE Systems / Blueprints / Settings
- **Lumen**: Real-time global illumination enabling cinematic lighting quality
- **Nanite**: Virtualized geometry for photorealistic environment detail
- **Movie Render Queue**: High-quality final frame rendering pipeline
- **Sequencer**: Timeline-based animation and camera management

### Difficulty
Beginner

### UE Version
UE 5.x

### Tags
cinematics, rendering, pipeline, beginner

---

## Related Entries
- [[how-i-made-a-godzilla-cinematic-in-unreal-engine-5]] — practical full-pipeline breakdown of a UE5 cinematic short
- [[the-future-of-filmmaking-in-unreal-5-virtual-production]] — related overview of UE5 as a production platform
