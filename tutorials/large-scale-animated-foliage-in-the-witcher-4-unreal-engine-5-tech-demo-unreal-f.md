---
title: Large Scale Animated Foliage in The Witcher 4 Unreal Engine 5 Tech Demo | Unreal Fest Stockholm 2025
source: YouTube
url: https://www.youtube.com/watch?v=EdNkm0ezP0o
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE 5.7"
tags: ["nanite", "pcg", "rendering", "pipeline", "advanced", "ue5-7"]
extraction_status: complete
frames_dir: tutorials/frames/large-scale-animated-foliage-in-the-witcher-4-unreal-engine-5-tech-demo-unreal-f/
frame_count: 4
---

# Large Scale Animated Foliage in The Witcher 4 Unreal Engine 5 Tech Demo | Unreal Fest Stockholm 2025

**Source:** [YouTube](https://www.youtube.com/watch?v=EdNkm0ezP0o)
**Author:** Unreal Engine
**Duration:** 37m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** All right, good afternoon, everybody. I hope you're having a good Unreal Fest so far. My name is Kevin, and together with Tyce and Vignesh from CD Projekt, we will take you behind the scenes on the topic of large-scale animated foliage, specifically in the context of the Witcher 4 Unreal Gen 5 tech demo. This is the demo we showcased at Unreal Fest Orlando just a few months ago. So the story arc of today's session is us telling you about the difficulties of rendering foliage to early experiments, leading into solutions, and finally talk about how this collaboration and demo culminates in engine features for you guys to try out in 5.7. So before we kick things off, here's a brief snippet from the demo just to set the tone. It is running on a base PS5 at 60 FPS with all the bells and whistles that UE5 has to offer. So a bit of a spoiler for those who haven't seen it. This is kind of the middle section of the demo where we go on rails and we just kind of fly through, look at all the awesome foliage and vegetation tech that we built. And in case you haven't seen it, it's online. You can see it in its full glory. And as we move up here, we're going to catch up with our protagonists and ...

**Frame:** tutorials\frames\large-scale-animated-foliage-in-the-witcher-4-unreal-engine-5-tech-demo-unreal-f\frame_000.jpg


---

## Structured Notes

### Core Technique
Large-scale animated foliage techniques from the Witcher 4 UE5 tech demo — vertex animation shaders, Nanite foliage with wind, PCG procedural placement, and performance optimization for console (PS5 @ 60fps).

### Summary
Unreal Fest Stockholm 2025 talk by Kevin (Epic) with CD Projekt's Tyce and Vignesh on the Witcher 4 UE5 tech demo foliage pipeline. Covers early experiments, the final solution combining Nanite foliage with a custom vertex animation shader for wind, PCG procedural placement of dense vegetation, and the engine features shipped in UE 5.7 as a result of this collaboration. Running at PS5 60fps with full Lumen/Nanite/TSR.

### Key Steps
1. **Nanite Foliage**: enable Nanite on Static Mesh foliage assets for unlimited polygon count without impostor LODs
2. **Wind animation with Nanite**: use **World Position Offset (WPO)** material with vertex animation shader — Nanite now supports WPO deformation (enabled per-asset, has performance cost)
3. **PCG placement**: use PCG Graph to scatter foliage based on terrain masks, slope, biome rules — replace manual painting
4. Set PCG density parameters driven by distance from camera for streaming LOD behavior
5. **Foliage physics blending**: blend between physics simulation (near) and vertex animation (far) using distance fade
6. **Wind direction system**: global wind parameter collection drives all foliage WPO shaders from one central control
7. Performance: profile `Stat GPU` → vegetation WPO cost; tune WPO `Maximum World Position Offset Displacement` per foliage type
8. Shipped UE 5.7 feature: Nanite WPO improvements specifically from this demo

### UE Systems / Blueprints / Settings
`Nanite → Enable WPO` (per Static Mesh) → Nanite-compatible vertex animation for wind deformation
`World Position Offset (WPO)` material → drives wind sway; controlled by global wind parameter collection
`PCG Graph` → procedural placement of foliage using terrain masks, slope, biome rules
`Stat GPU` → profile WPO vertex animation performance cost
`MPC_Wind` (Material Parameter Collection) → centralized wind direction/speed for all foliage shaders
New in UE 5.7: Nanite WPO enhancements from Witcher 4 collaboration

### Difficulty
Advanced

### UE Version
UE 5.7

### Tags
nanite, pcg, rendering, pipeline, advanced, ue5-7

---

## Related Entries
- `references/rendering-pipeline.md` — Nanite and Lumen reference
- `references/materials-shaders.md` — WPO material expressions