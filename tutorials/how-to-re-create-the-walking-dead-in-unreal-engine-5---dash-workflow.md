---
title: How to Re-Create The Walking Dead in Unreal Engine 5 - Dash Workflow
source: YouTube
url: https://www.youtube.com/watch?v=5aTwhjR5JJE
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.4
ue_version: "UE 5.x"
tags: [dash-1.4, environment, scatter, decals, grid-scatter, physics, cable-tool, horror, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-to-re-create-the-walking-dead-in-unreal-engine-5---dash-workflow/
frame_count: 8
---

# How to Re-Create The Walking Dead in Unreal Engine 5 - Dash Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=5aTwhjR5JJE)
**Author:** Polygonflow Dash
**Duration:** 8m26s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted — see ingested file...]

---

## Structured Notes

### Core Technique
Galen from Polygonflow recreates the Walking Dead hospital scene in UE5 using Dash — Decal Scatter on plane guide mesh for localized blood, Grid Scatter for ceiling tiles (exposed structural metal via Random Remove), Physics Tool for broken ceiling tiles (fracture system → simple convex collision → Dynamic mode) and pill bottle piles, Quick Pipe Tool for tangled cables on props, Cable Tool for hanging wires from ceiling.

### Summary
8.5-minute Walking Dead hospital environment breakdown by Galen. Workflow: Dekogon hospital set from Marketplace → Decal Scatter (Megascans blood decals on hidden plane guide mesh for localized room coverage; density + min/max scale; rotation) → Grid Scatter for ceiling tiles (3 tile variations; Random Remove for structural metal exposure; scale + pattern extent) → Physics Tool (fracture ceiling tiles in UE5 modeling tools → simple convex collision → Physics Tool Dynamic mode for tile dropping simulation; pill bottle piles via duplicate + physics) → Quick Pipe for tangled cable on supply cart (draw curve first, note minimum spacing, Quick Pipe selects curve as control arm; radius/segments settings) → Cable Tool for hanging wires (ceiling anchor assets placed first, Connection Rate + Cut Rate for bundle variation, Min/Max Gravity for elevation variation, Noise for breakup).

### Key Steps
1. **Decal Scatter — Blood Room** — draw plane to match room footprint → Decal Scatter → assign plane as surface input → load blood decals → increase density → adjust min/max scale + rotation for natural breakup; plane hidden at runtime (not visible in render)
2. **Grid Scatter — Ceiling Tiles** — create 3 tile mesh variations with slight noise displacement → Grid Scatter → assign all 3 as input → adjust scale to match ceiling grid + pattern extent → Random Remove Mask for exposed structural metal; Metal structural pieces placed under Random Remove'd gaps
3. **Physics — Broken Ceiling Tiles** — open Fracture system in UE5 Modeling Tools (external tutorial for fracture technique) → assign simple convex collision → Physics Tool: select tile pieces → Dynamic mode → tiles drop and settle; repeat for hospital clutter
4. **Physics — Pill Bottle Piles** — place pill bottles → select all → Duplicate → Physics start → creates natural pile; repeat 2-3x for density
5. **Quick Pipe — Tangled Cable** — draw curve over/through supply cart geometry → minimize control points (fewer is better; smooth later) → Quick Pipe: flag curve as control arm → set radius and segments; edit curve shape → cable wraps tangled through cart
6. **Cable Tool — Hanging Wires** — place hidden anchor assets in ceiling structure at desired connection points → Cable Tool: connect anchors → Connection Rate + Cut Rate for bundle variation → Min/Max Gravity for elevation variation → add Noise for organic breakup

### UE Systems / Blueprints / Settings
- **Decal Scatter (plane guide)** — use hidden plane to localize decal area rather than masking; set plane as surface → decals only scatter on that footprint; plane hidden at runtime
- **Grid Scatter (Random Remove Mask)** — Random Remove slider + Seed → removes instances at random creating gaps; useful for exposing underlying structures without manual placement
- **UE5 Fracture (Modeling Tools)** — external fracture workflow → assign simple convex collision to each fragment; required before Physics Tool simulation
- **Physics Tool (Dynamic mode)** — select fractured pieces → Dynamic → simulate drop onto existing collision; Stop when settled → becomes static; Reset only resets selected objects
- **Quick Pipe** — draw curve (fewer control points = easier editing); Quick Pipe → flag curve as control arm → set radius/sides/length parameters; can smooth later in Cable Tool settings
- **Cable Tool** — Connection Rate (strands per anchor pair) + Cut Rate (strand termination variation) + Min/Max Gravity (elevation spread) + Noise (organic breakup); uses hidden anchor meshes for granular control

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.4)

### Tags
`#dash-1.4` `#environment` `#scatter` `#decals` `#grid-scatter` `#physics` `#cable-tool` `#horror` `#intermediate`

---

## Related Entries
- [[environment-breakdown-underground-horror-in-ue5]] — Josh Powers horror workflow; Scatter Mesh Cards + decals
- [[new-physics-tool-for-unreal-engine-5]] — Physics Tool detailed intro (Josh Powers)
- [[how-to-scatter-decals-in-ue5---world-building-plugin]] — Decal Scatter dedicated tutorial
- [[how-to-create-procedural-cables-in-ue5---world-building-plugin]] — Cable Tool dedicated tutorial
