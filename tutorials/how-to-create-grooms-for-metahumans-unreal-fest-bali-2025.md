---
title: How to Create Grooms for MetaHumans | Unreal Fest Bali 2025
source: YouTube
url: https://www.youtube.com/watch?v=WqWpwVaewEU
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["metahuman", "rigging", "advanced"]
extraction_status: complete
frames_dir: tutorials/frames/how-to-create-grooms-for-metahumans-unreal-fest-bali-2025/
frame_count: 4
---

# How to Create Grooms for MetaHumans | Unreal Fest Bali 2025

**Source:** [YouTube](https://www.youtube.com/watch?v=WqWpwVaewEU)
**Author:** Unreal Engine
**Duration:** 30m38s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hi, thank you. Thank you for joining me today. I'm Hugo Lignac, and I'm part of the group team at Epic Games, focusing on both hairstyle design and the tools that enable high fidelity and hair creation for our metayumes. The main thing is tough. It combines artistic direction with technical precision, and it's a very demanding aspect of digital human creation. Today I will share how the metayume and groom tools were developed to address these challenges as we aim to help creators deliver production quality results with efficiency and creative flexibility. So first of all, let's just take a step back and look at the technical foundations of grooming. At the core of every groom is a guide driven system. These guides define the flow, the shape, the volume of the hair, forming the basis for interpolated strands that make up the final groom to be rendered. From there we use a procedural node system to apply modifiers and attributes, operations like clumping, noise curls, which are essential for adding natural variation and realism. This approach is at the heart of strand-based grooming, for example for complex and believable hair styles. Understanding the method is one thing, but puttin...

**Frame:** tutorials\frames\how-to-create-grooms-for-metahumans-unreal-fest-bali-2025\frame_000.jpg


---

## Structured Notes

### Core Technique
Strand-based MetaHuman groom creation workflow — guide-driven system, procedural node modifiers (clumping, noise, curl), and achieving production-quality hair using the MetaHuman Creator + Groom tools.

### Summary
30-minute Unreal Fest Bali 2025 session by Hugo Lignac (Epic Groom Team) on creating production-quality grooms for MetaHumans. Covers the foundational guide-driven system, procedural node graph for applying clumping/noise/curl modifiers, the artistic vs. technical balance in hair design, and how MetaHuman Creator's groom presets work under the hood. Targets studios aiming for film/linear quality hair within UE5.

### Key Steps
1. Start from **MetaHuman Creator** groom presets as a base (download via MetaHuman Plugin)
2. Open the groom asset → inspect the **Guide Strands** (low-density splines defining flow and volume)
3. In the **Groom Editor → Nodes**, add procedural modifiers in order:
   - `Clump` → groups nearby strands into natural clusters; set clump radius and per-clump noise
   - `Noise / Curl` → adds randomization and natural variation along strand length
   - `Cut` → trims strand tips to desired length and shape
4. Adjust `Strand Count` (rendered strands, not guides) — film quality: 100K–300K; realtime: 20K–60K
5. Set up **Groom Binding** to bind groom to the MetaHuman's head skeletal mesh
6. In UE: assign groom to the `Groom Component` on the MetaHuman BP's head component
7. Configure `LOD Settings` → reduce strand count at distance; use `Strands → Meshes` conversion for extreme LOD
8. Test with Lumen and Path Tracing — groom renders correctly in both; Path Tracing gives most accurate self-shadowing

### UE Systems / Blueprints / Settings
`Guide Strands` → low-density splines; define hair flow and volume basis for interpolated final strands
`Clump Modifier` → groups strands naturally; most impactful modifier for believability
`Noise / Curl Modifier` → adds randomization along length
`Strand Count` → rendered strands (not guides); balance quality vs. performance
`Groom Binding Asset` → required link between groom guides and character head skeletal mesh
`Groom Component` (MetaHuman BP → Head) → where groom is attached for rendering
LOD: `Strands → Meshes` conversion for distant LOD levels

### Difficulty
Advanced

### UE Version
UE5

### Tags
metahuman, rigging, advanced

---

## Related Entries
- `tutorials/advanced-groom-dataflow-setup-in-ue-57-unreal-fest-stockholm-2025.md` — Groom Dataflow for physics/deformation
- `references/metahuman-reference.md` — MetaHuman setup and components