---
title: unreal-engine-5-4-release-notes
source: Epic Documentation
url: https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-4-release-notes
ingested: 2026-06-12
ue_version: "UE 5.4"
tags: [release-notes, motion-design, pcg, rendering, animation, niagara, nanite, lumen, ue5-4]
extraction_status: complete
page_count: 1
---

# unreal-engine-5-4-release-notes

**Source:** [Epic Documentation](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-4-release-notes)
**Pages crawled:** 1
**Ingested:** 2026-06-12

---

## Raw Documentation Content


### unreal-engine-5-4-release-notes
**URL:** https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-4-release-notes

Table of Contents


---

## Structured Notes

### Core Topics
Motion Design, PCG improvements, Nanite tessellation & displacement, Lumen improvements, Modular Control Rig (Experimental), Neural Rendering, Procedural Animation Tools, Texture Graph (Experimental), Temporal Super Resolution improvements, Substrate (Experimental), Movie Render Graph (Early Access)

### Summary
UE 5.4 focused on cinematic and motion design tooling. Motion Design module became a first-class citizen in the editor. PCG gained vector fields, hierarchical generation, and runtime update support. Nanite got displacement and tessellation for organic surfaces. Movie Render Graph entered Early Access as a node-based replacement for MRQ. Modular Control Rig launched as Experimental.

*Note: The crawler captured only the hub table of contents for this page. Notes below are synthesized from release knowledge.*

### Key Features Added in UE 5.4

**Animation:**
- **Modular Control Rig (Experimental)**: Node-based, module-driven rigging system; reusable modules per body part; new foundation for non-destructive rigging
- **Motion Matching improvements**: State machine integration; distance matching; trajectory prediction improvements
- **IK Rig & Retargeting**: Improved full-body IK solve; faster retargeting workflow
- **Skeletal Editor (Beta)**: In-editor weight painting; mesh editing

**Rendering:**
- **Nanite Displacement & Tessellation (Experimental)**: Micro-polygon displacement in Nanite; organic surfaces without baking
- **Substrate Materials**: Continued development; more node types; better editor feedback
- **Lumen**: Improved GI accuracy at distance; better indoor performance
- **TSR (Temporal Super Resolution)**: Improved ghost reduction; sharper output at lower base resolution
- **Path Tracer**: Improved volumetric rendering, sky atmosphere support

**Procedural / PCG:**
- **PCG v2 enhancements**: Vector fields, dynamic pins, hierarchical generation subgraphs, runtime PCG updates, improved debugging

**Cinematic:**
- **Movie Render Graph (Early Access)**: Node-based rendering pipeline replacing the linear MRQ queue; conditional branching, custom pass graphs
- **Sequencer**: Shot-level color grading; improved in-viewport Sequencer control

**Motion Design:**
- **Motion Design module**: First-class status; keyframeable cloners (grid, linear, circle, random); effectors; procedural motion patterns; Rundown graph

**World Building:**
- **World Partition**: HLOD improvements; better Level Instance workflows; streaming improvements for large maps

### UE Version
UE 5.4 (2024)

### Tags
release-notes, motion-design, pcg, rendering, animation, niagara, nanite, lumen, ue5-4

---

## Related Entries
- `tutorials/procedural-content-generation-framework-in-unreal-engine.md` — PCG system in depth
- `tutorials/animating-characters-and-objects-in-unreal-engine.md` — Sequencer, MRQ details
- `tutorials/designing-visuals-rendering-and-graphics-with-unreal-engine.md` — Nanite, Lumen, Path Tracer
- `references/version-tracker.md` — All UE version comparison
