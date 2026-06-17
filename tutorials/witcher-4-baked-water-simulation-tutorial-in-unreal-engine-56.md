---
title: Witcher 4 Baked Water Simulation Tutorial in Unreal Engine 5.6
source: YouTube
url: https://www.youtube.com/watch?v=akHCbIECFX8
author: Aziel Arts
ingested: 2026-06-17
ue_version: "5.6"
tags: [water, simulation, baked-simulation, river, buoyancy, water-advanced, environment, physics, ue5-6]
extraction_status: complete
frames_dir: tutorials/frames/witcher-4-baked-water-simulation-tutorial-in-unreal-engine-56/
frame_count: 4
---

# Witcher 4 Baked Water Simulation Tutorial in Unreal Engine 5.6

**Source:** [YouTube](https://www.youtube.com/watch?v=akHCbIECFX8)
**Author:** Aziel Arts
**Duration:** 22m34s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** What's up in this tutorial we are gonna cover how to set up a baked river simulation in Unreal Engine 5 It takes advantage of Unreal Engine's built-in water and shallow-body simulation system, but now gives us the ability to actually bake that simulation into a super efficient but really good looking simulation Play Black of a river and we're still able to maintain Things floating on the river or making ripples as we walk through it with a character It's really great new feature that's built into Unreal Engine and I'm gonna show you how to set it up Let's get into it and the plugins we need to enable here are of course the water plug-in Which contains the water bodies that we're gonna be the basis for this so raver bodies Lake bodies ocean bodies then we're gonna turn on buoyancy Which is a plugin that lets us have things float on the water with buoyancy and then we're gonna also need to turn on Water advanced and this is where those actual shallow-body Simulations that we're gonna be baking are set up once we've enabled all those plugins I'm gonna go ahead and hit restart now and when we successfully restart you should get this message log pop-up Which is basically telling us that...

**Frame:** tutorials\frames\witcher-4-baked-water-simulation-tutorial-in-unreal-engine-56\frame_000.jpg


---

## Structured Notes

### Core Technique
Baked river/water simulation in UE5.6 using the Water + Water Advanced + Buoyancy plugins — bakes a shallow-body fluid sim into an efficient looping playback while preserving buoyancy for floating objects and ripple interaction for characters.

### Summary
Aziel Arts demonstrates UE5.6's new baked water simulation system, inspired by Witcher 4's river visuals. The workflow uses UE's built-in Water plugin (water bodies: river, lake, ocean), the Water Advanced plugin (which provides the shallow-body simulation to bake), and the Buoyancy plugin (for floating objects). The simulation is baked into efficient playback — high fidelity at low runtime cost — while still supporting dynamic interactions: objects float correctly and characters create ripples when wading through the water.

### Key Steps
1. **Enable plugins**: Plugins menu → enable **Water** (river/lake/ocean water bodies), **Buoyancy** (floating object physics), **Water Advanced** (shallow-body simulation system) → Restart
2. After restart, a message log pop-up confirms Water Advanced is active
3. Add a **Water Body River** (or lake/ocean) actor to the scene from the Water plugin
4. Use the **Water Advanced** shallow-body simulation to run and then bake the fluid simulation
5. Baked simulation produces an efficient looped playback of the river
6. **Buoyancy** continues to work on baked water — place buoyant actors on the river and they float correctly
7. Characters walking through the baked river still generate surface ripples (interaction layer preserved post-bake)

### UE Systems / Blueprints / Settings
- **Water plugin** — Water Body River / Lake / Ocean actors; foundation for all water in UE
- **Water Advanced plugin** — shallow-body fluid simulation; provides the sim to bake
- **Buoyancy plugin** — physics simulation for objects floating on water surface; compatible with baked water
- **Baked simulation** — bakes live fluid sim to efficient looping animation while keeping interactive layers (buoyancy, ripples)

### Difficulty
Intermediate

### UE Version
5.6

### Tags
water, simulation, baked-simulation, river, buoyancy, water-advanced, water-plugin, environment, physics, shallow-water, ue5-6

---

## Related Entries
- Polygonflow Dash environment tutorials (water tool, terrain tool)
- UE Basics documentation (environment, landscapes)
