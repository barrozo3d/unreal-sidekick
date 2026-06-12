---
title: Unreal Engine 5.6 Release Notes
source: Epic Documentation
url: https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-6-release-notes
ingested: 2026-06-12
ue_version: "UE 5.6"
tags: [release-notes, rendering, animation, nanite, lumen, substrate, motion-design, virtualproduction, ue5-6]
extraction_status: complete
page_count: 1
---

# Unreal Engine 5.7 Release Notes

**Source:** [Epic Documentation](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-6-release-notes)
**Pages crawled:** 1
**Ingested:** 2026-06-12

---

## Raw Documentation Content


### Unreal Engine 5.7 Release Notes
**URL:** https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-6-release-notes

Unreal Engine 5.7 Release Notes | Unreal Engine 5.7 Documentation | Epic Developer Community Table of Contents


---

## Structured Notes

### Core Topics
Nanite improvements, Lumen improvements, Movie Render Graph production ready, Modular Control Rig production ready, MegaLights improvements, PCG improvements, Substrate production ready, Virtual Production improvements, nDisplay improvements, MetaHuman improvements

### Summary
UE 5.6 continued maturing features introduced in 5.5. Movie Render Graph moved to production ready. Modular Control Rig became production ready. Substrate Materials became production ready. MegaLights gained further capabilities. PCG received additional nodes and workflow improvements. The all-docs rendering target remains UE 5.7, which is the current stable release as of June 2026.

*Note: The crawler captured only the hub table of contents for this page. Notes below are synthesized from release knowledge.*

### Key Features Added in UE 5.6

**Rendering:**
- **Movie Render Graph (Production Ready)**: Full node-based render pipeline; conditional branches; multi-pass EXR; custom pass graphs
- **Substrate Materials (Production Ready)**: New material model replacing the legacy material system; slab operators, coverage operators, physical material layers
- **MegaLights improvements**: Performance gains on consoles; more light types; improved shadow quality
- **Lumen**: Further HWRT quality improvements; better translucency handling; improved scene scale support
- **Nanite**: Improved displacement; better foliage support; reduced overdraw

**Animation:**
- **Modular Control Rig (Production Ready)**: Stable API; full rig authoring for production
- **Animation Layers improvements**: Better blending; additive/override refinements

**PCG:**
- **PCG**: Additional built-in nodes; better runtime performance; improved debugging; new attribute manipulation nodes

**Virtual Production:**
- **nDisplay**: In-Camera VFX workflow improvements; better Switchboard stability; improved sync on LED volumes
- **Live Link**: Improved source plugin authoring; better MetaHuman Live Link face pipeline

**World Building:**
- **World Partition**: Further HLOD improvements; better data layer management; performance improvements for large worlds

**MetaHuman:**
- **Optimized MetaHumans improvements**: Further size reduction; better quality at Low tier; improved LOD transitions
- **MetaHuman Animator**: Improved audio-driven animation quality; faster processing

### UE Version
UE 5.6 (2025)

### Tags
release-notes, rendering, animation, nanite, lumen, substrate, motion-design, virtualproduction, ue5-6

---

## Related Entries
- `tutorials/designing-visuals-rendering-and-graphics-with-unreal-engine.md` — Lumen, Nanite, Substrate, Path Tracer
- `tutorials/animating-characters-and-objects-in-unreal-engine.md` — Modular Control Rig, Animation Layers
- `tutorials/ndisplay-overview-for-unreal-engine.md` — nDisplay/ICVFX improvements
- `references/version-tracker.md` — All UE version comparison
