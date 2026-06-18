---
title: Introduction to Substrate Materials | Unreal Engine 5.7
source: YouTube
url: https://www.youtube.com/watch?v=d1ncs8M6Lkg
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE 5.7"
tags: ["materials", "shaders", "substrate", "rendering", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/introduction-to-substrate-materials-unreal-engine-57/
frame_count: 4
---

# Introduction to Substrate Materials | Unreal Engine 5.7

**Source:** [YouTube](https://www.youtube.com/watch?v=d1ncs8M6Lkg)
**Author:** Unreal Engine
**Duration:** 8m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay everyone, welcome to a new highlight video. Today we're taking a closer look at substrate, which is enabled by default, starting with Unreal 5.7 and onwards. Substrate introduces a new approach to material rendering and data storage, giving us more flexibility and control over how materials are built and evaluated. With the option to choose between two GBA formats, one focused on state-of-the-art visual fidelity and another optimized for performance. Now let's take a deeper look at what is substrate. Substrate is Unreal's engine next-generation material framework. It lets artists build layered, physically accurate surfaces with far more control than the traditional material system. As we look at the substrate slab node, you can see how the interface is organized into layers of visual behavior. At the top, we have reflectivity driven by F0 and F90. This defines how light responds at glancing and facing angles. Below that is the roughness section, which controls microsurface detail. And further down, we can opt into advanced features like fuzz or glint materials, which introduces tiny sparkling highlights to make that car paint material shine the way it should be. The slab mediu...

**Frame:** tutorials\frames\introduction-to-substrate-materials-unreal-engine-57\frame_000.jpg


---

## Structured Notes

### Core Technique
Introduction to Substrate material framework — enabled by default from UE 5.7; `Substrate Slab` node replaces legacy material shading models for layered, physically-accurate surface rendering.

### Summary
Official Epic overview of Substrate in UE 5.7 (now enabled by default). Covers the Substrate Slab node structure (F0/F90 reflectivity, roughness, fuzz/glint advanced features), two GBuffer format options (high-fidelity vs. performance), and how Substrate gives artists more layering control than the traditional material system.

### Key Steps
1. Substrate is enabled by default in UE 5.7+ — no manual activation needed (check `Project Settings → Rendering → Substrate`)
2. In Material Editor, use the **`Substrate Slab`** node as the primary material expression
3. Configure `F0` (facing reflectivity) and `F90` (glancing angle reflectivity) for PBR accuracy
4. Set `Roughness` input for microsurface detail
5. Enable `Fuzz` layer for velvet/fabric surfaces; enable `Glint` for sparkle (car paint, glitter)
6. Layer multiple Slab nodes using **`Substrate Layer`** blend nodes
7. Choose GBuffer format in `Project Settings → Rendering → Substrate → GBuffer Format`: `8-Byte` (performance) or `16-Byte` (maximum fidelity)
8. Path Tracing is fully supported with Substrate — no special setup needed

### UE Systems / Blueprints / Settings
`Substrate Slab` node — primary material primitive replacing old shading models
`F0 / F90` inputs → physically accurate reflectivity at facing and glancing angles
`Fuzz` input → microfiber/velvet surface layer
`Glint` input → sparkle highlights (car paint, metallic flake)
`Substrate Layer` node → blend/stack multiple Slab layers
`Project Settings → Rendering → Substrate → GBuffer Format` → 8-Byte (perf) or 16-Byte (fidelity)

### Difficulty
Intermediate

### UE Version
UE 5.7

### Tags
materials, shaders, substrate, rendering, intermediate

---

## Related Entries
- `references/materials-shaders.md` — broader material system reference
- `tutorials/everything-you-wanted-to-know-about-substratebut-are-too-afraid-to-ask-unreal-fe.md` — deep dive Unreal Fest talk
- `references/rendering-pipeline.md` — Path Tracing compatibility