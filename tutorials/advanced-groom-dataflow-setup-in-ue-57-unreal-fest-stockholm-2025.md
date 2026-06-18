---
title: Advanced Groom Dataflow Setup in UE 5.7 | Unreal Fest Stockholm 2025
source: YouTube
url: https://www.youtube.com/watch?v=cER2jT8oxKY
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE 5.7"
tags: ["metahuman", "rigging", "advanced", "ue5-7"]
extraction_status: complete
frames_dir: tutorials/frames/advanced-groom-dataflow-setup-in-ue-57-unreal-fest-stockholm-2025/
frame_count: 4
---

# Advanced Groom Dataflow Setup in UE 5.7 | Unreal Fest Stockholm 2025

**Source:** [YouTube](https://www.youtube.com/watch?v=cER2jT8oxKY)
**Author:** Unreal Engine
**Duration:** 31m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hi, everyone. My name is Michael Fro and I'm working at Epic as a Senior Physics Engineer. So today I'm going to present you the new advanced group that the flow setup that has been introduced in UE57. So, the agenda for today. So we are going through the motivation behind this initiative, why we decided to change a bit how the group was set up. Then I introduced briefly the data for framework. So for people who are not aware of or never used of, it would be like a really simple introduction, really brief one. So now we go through the group integration, the deformation pipeline, and we're finished by like a simple example to show off all of that connection. So, group has been around for quite some time. There's been I think released like five or six years ago. And if a lot of things are evolved since then, the way you were set up in things didn't really change. So you were just doing all your work and all your setup in the most application that could be Maya or Denis. And just after that, you are importing your group and after you are able to modify it a bit inside engine and you are using it. But the way you are really set up in things didn't really change. So we wanted to improve...

**Frame:** tutorials\frames\advanced-groom-dataflow-setup-in-ue-57-unreal-fest-stockholm-2025\frame_000.jpg


---

## Structured Notes

### Core Technique
Groom Dataflow framework (UE 5.7) — a node-based procedural system for setting up, deforming, and customizing grooms (hair/fur) inside Unreal Engine, replacing the static import-only pipeline.

### Summary
Unreal Fest Stockholm 2025 talk by Michael Fro (Epic Physics Engineer) on the new Groom Dataflow framework in UE 5.7. The old pipeline required all groom setup in DCC (Maya/Houdini) then static import. Dataflow brings a node-based procedural graph inside UE for modifying guides, adding procedural deformations (wind, physics simulation), and blending groom behaviors — without going back to DCC. Covers motivation, Dataflow framework basics, groom integration nodes, and a practical example.

### Key Steps
1. Import your base groom asset as before (USD/Alembic .abc); this is still the starting point
2. Open the groom asset → find the new **Dataflow** tab in the groom editor (UE 5.7+)
3. The Dataflow graph uses nodes to modify the imported groom procedurally
4. Add **Guide Deformation** nodes for dynamic modifications (physics simulation, wind response)
5. Connect groom guides through `Groom Physics` node for real-time strand simulation
6. Add **Blend Shape** nodes to mix between styled and simulated states (e.g. 70% style / 30% physics)
7. The Dataflow graph is re-evaluated at runtime — no baking needed for simulation
8. Use **Groom Binding** asset to bind groom to skeletal mesh (required for character movement)
9. Preview in the groom editor with live physics: adjust stiffness, damping, collision radius

### UE Systems / Blueprints / Settings
`Groom Asset → Dataflow Tab` (UE 5.7+) → node-based procedural groom modification inside engine
`Guide Deformation Node` → applies physical simulation/wind deformation to guides
`Groom Physics Node` → real-time strand simulation parameters (stiffness, damping)
`Blend Shape Node` → mix styled groom with simulated state
`Groom Binding Asset` → binds groom guides to skeletal mesh bones for character animation
Import format: USD Alembic (.abc) from Maya/Houdini still required as base groom

### Difficulty
Advanced

### UE Version
UE 5.7

### Tags
metahuman, rigging, advanced, ue5-7

---

## Related Entries
- `tutorials/how-to-create-grooms-for-metahumans-unreal-fest-bali-2025.md` — strand-based groom creation for MetaHumans
- `references/metahuman-reference.md` — MetaHuman hair and groom setup