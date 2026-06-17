---
title: Unreal Engine for Filmmakers - Cinematic VFX for FREE - UE5 [PART 2]
source: YouTube
url: https://www.youtube.com/watch?v=5zJktaYwK-I
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 5.x"
tags: [niagara, vfx, simulation, rendering, lighting, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-for-filmmakers---cinematic-vfx-for-free---ue5-part-2/
frame_count: 5
---

# Unreal Engine for Filmmakers - Cinematic VFX for FREE - UE5 [PART 2]

**Source:** [YouTube](https://www.youtube.com/watch?v=5zJktaYwK-I)
**Author:** Boundless Entertainment
**Duration:** 19m24s | 5 section(s)

---

## Structured Notes

### Core Technique
Niagara Fluid Simulation Part 2: detailed parameter tweaking in the Emitter Summary panel + manual lighting assignment workaround. Focuses on vorticity, smoke/fire density balance, world space size scaling, and assigning scene directional lights to the Niagara actor for correct illumination.

### Summary
19-minute deep-dive continuing from Part 1. After setting up a Grid 3D Gas fluid sim (Part 1), this video covers how to tune the look: open Emitter Summary (click emitter in Niagara editor > Emitter Summary tab); vorticity confinement increases turbulence/detail in the sim; density controlled in the particle source emitter's "Set Fluid Source Attributes" module — density=1 for dense smoke, density=0 for fire-only; fire/smoke ratio controllable independently. Scaling: World Space Size parameter resizes the sim volume in world space. Lighting problem: Niagara fluid sims don't automatically receive scene lighting — must manually assign directional lights in the Niagara actor's Directional Light slots (supports 2 directional lights; assign to scene light actor via dropdown). Light color and intensity match from scene but don't account for shadow occlusion, so simulation lit from a shadow may still appear lit — accept as a limitation.

### Key Steps
1. **Open Emitter Summary** — select Niagara actor > double-click NS asset > click emitter layer > Emitter Summary tab; organized into tabs: Simulation, Render, Debug, Scalability
2. **Verify static mesh collision** — Emitter Summary > Simulation > static mesh = ON; this allows the simulation to interact with tagged collision objects
3. **Vorticity confinement** — Emitter Summary > Simulation > Vorticity Confinement = increase for more turbulence/detail, decrease for cleaner calmer simulation
4. **Smoke/fire density** — particle source emitter > Set Fluid Source Attributes > Density: 1 = dense smoke; 0 = fire only; 0.2 = light smoke + fire (default-ish)
5. **Scale the simulation** — Niagara actor details > World Space Size: increases/decreases the physical size of the fluid volume in the scene
6. **Lighting** — select Niagara actor > details > find Directional Light 1, Directional Light 2 > click dropdown > type "directional light" > assign your scene's directional light; note: only 2 directional light slots; no point/spot support; shadow occlusion is not computed

### UE Systems / Parameters
- **Emitter Summary** — organized panel of key Niagara fluid parameters; alternative to navigating full Niagara stack; most fluid look controls live here
- **Set Fluid Source Attributes module** — lives in the particle source emitter; controls: Density (smoke amount), fire intensity, velocity scale; must be present for gas controls emitter to receive fluid-source data
- **Vorticity Confinement** — Niagara parameter that adds swirling detail to the gas simulation; higher = more turbulent
- **World Space Size** — scales the simulation volume; use this instead of actor transform scale for correct sim scaling
- **Directional Light slots** — Niagara actor detail panel; 2 slots for directional lights only; assign to get approximate directional illumination on the sim; no Lumen or point light support

### Difficulty
Intermediate

### UE Version
UE 5.x (UE5 era — Niagara Fluids plugin required)

### Tags
`#niagara` `#vfx` `#simulation` `#rendering` `#lighting` `#intermediate`

---

## Related Entries
- [[unreal-engine-for-filmmakers---add-cinematic-vfx-to-your-films-for-free---ue5-pa]] — Part 1 (setup and basics)
- [[unreal-engine-for-filmmakers---incredible-realtime-particle-simulations-for-free]] — particle simulations companion
- [[unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic]] — scene lighting for same workflow context
