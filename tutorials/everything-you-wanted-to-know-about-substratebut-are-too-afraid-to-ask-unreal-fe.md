---
title: Everything You Wanted to Know About Substrate(But Are Too Afraid to Ask)| Unreal Fest Stockholm 2025
source: YouTube
url: https://www.youtube.com/watch?v=SqPaL8HS_Lw
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE 5.7"
tags: ["materials", "shaders", "substrate", "rendering", "advanced"]
extraction_status: complete
frames_dir: tutorials/frames/everything-you-wanted-to-know-about-substratebut-are-too-afraid-to-ask-unreal-fe/
frame_count: 4
---

# Everything You Wanted to Know About Substrate(But Are Too Afraid to Ask)| Unreal Fest Stockholm 2025

**Source:** [YouTube](https://www.youtube.com/watch?v=SqPaL8HS_Lw)
**Author:** Unreal Engine
**Duration:** 43m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hi everyone, thank you so much for being here. Welcome to everything you wanted to know about substrate, but we're afraid to ask. I'd like to tell you a little bit about me before we get started. My name's Nathaniel Morgan and I'm a principal technical artist here at Epic Games. I'm one of the product owners for the rendering systems of Unreal Engine and I'm here to talk to you about our new material systems substrate. I want to underscore that I'm here representing the work of the whole substrate team and most especially the main engineers responsible for substrates Sebastian Haleir and Charles de Rousier without whom none of this would be possible. So substrate is now production ready as of Unreal 5.7. I'd like to take some time to explore with you what substrate is, why it represents a fundamental shift in Unreal Engine shading model and how to start using it effectively in your own projects. Whether you're working in games, linear content or CG visualization, substrate gives you more control over surface shading, greater visual fidelity and a more expressive material system without relying on hacky or otherwise brittle shader workarounds. Before we dive in, here's a quick overv...

**Frame:** tutorials\frames\everything-you-wanted-to-know-about-substratebut-are-too-afraid-to-ask-unreal-fe\frame_000.jpg


---

## Structured Notes

### Core Technique
Deep-dive Substrate system talk (Unreal Fest Stockholm 2025) — architecture, GBuffer formats, layering system, path tracing support, migration from legacy shading models, and practical usage patterns for games, linear, and CG-viz.

### Summary
43-minute technical session by Nathaniel Morgan (Principal Technical Artist, Epic) covering everything about Substrate: why it replaces the legacy shading model system, the Slab node architecture, two GBuffer memory formats (8-byte performance vs. 16-byte fidelity), material layering via the operator stack, Substrate's path tracing integration, and migration guides. Production-ready as of UE 5.7 and enabled by default.

### Key Steps
1. Substrate enabled by default in 5.7 — check `Project Settings → Rendering → Substrate → Enable Substrate`
2. Choose **GBuffer Format**: `Substrate 8-Byte` (performance; mobile/console) or `Substrate 16-Byte` (fidelity; PC/linear)
3. Core unit: **Substrate Slab** node → configure F0, F90, Roughness, Diffuse Albedo, Normal
4. Add optional **Fuzz Layer** for cloth/velvet; **Glint** for car paint sparkle; **SSS** for skin
5. Use **Substrate Layer Blend** nodes to stack multiple Slab nodes (by weight or mask)
6. **Thin Film Interference** node → iridescent surfaces (soap bubbles, oil slicks, beetle wings)
7. Legacy material output nodes (`DefaultLit`, `Unlit`, etc.) auto-migrate — existing materials should work
8. Substrate materials work in both rasterization and **Path Tracing** without any special nodes
9. For advanced SSS (subsurface scattering) skin: use the `Subsurface` Slab parameter instead of the legacy SSS shading model

### UE Systems / Blueprints / Settings
`Substrate Slab` node → physically-accurate surface primitive (F0, F90, Roughness, Albedo, Normal, Fuzz, Glint, SSS, Anisotropy)
`Substrate Layer Blend` → stack multiple Slabs with mask or weight
`Thin Film Interference` node → iridescent surface effect
`Project Settings → Rendering → Substrate → GBuffer Format` → 8-Byte (performance) or 16-Byte (fidelity)
Path Tracing → fully compatible; no extra nodes required
Legacy materials → auto-migrate; no manual rework for basic surfaces
Principal engineers: Sebastian Haleir + Charles de Rousier

### Difficulty
Advanced

### UE Version
UE 5.7

### Tags
materials, shaders, substrate, rendering, advanced

---

## Related Entries
- `tutorials/introduction-to-substrate-materials-unreal-engine-57.md` — beginner intro to Substrate
- `references/materials-shaders.md` — full materials reference
- `references/rendering-pipeline.md` — Path Tracing integration