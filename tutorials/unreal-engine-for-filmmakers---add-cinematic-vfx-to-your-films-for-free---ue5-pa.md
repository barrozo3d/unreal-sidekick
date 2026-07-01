---
title: Unreal Engine for Filmmakers - Add Cinematic VFX to your Films for FREE - UE5 [PART 1]
source: YouTube
url: https://www.youtube.com/watch?v=Yl_VJqmll-E
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 5.x"
tags: [niagara, vfx, simulation, particles, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-for-filmmakers---add-cinematic-vfx-to-your-films-for-free---ue5-pa/
frame_count: 8
---

# Unreal Engine for Filmmakers - Add Cinematic vfx to your Films for FREE - UE5 [PART 1]

**Source:** [YouTube](https://www.youtube.com/watch?v=Yl_VJqmll-E)
**Author:** Boundless Entertainment
**Duration:** 13m8s | 8 section(s)

---

## Structured Notes

### Core Technique
Introduction to Niagara Fluid Simulations in UE5: enable the Niagara Fluids plugin, create a Grid 3D Gas system from the "Simple Particle Source" template, configure voxel resolution, and enable mesh collision with actor tags.

### Summary
13-minute introduction to UE5's Niagara Fluid Simulation system for filmmakers. Niagara Fluids is a separate plugin (beta) that adds volumetric gas and liquid simulation — physics-based, not a particle sprite system. Key templates: 2D gas, 2D liquid, 3D gas, 3D liquid. Tutorial uses "Grid 3D Gas Simple Particle Source" for smoke/fire effects. Core concepts: voxel resolution controls quality vs. performance (Resolution Max Axis = 250 is good, 350 starts to lag); collision with objects in the scene requires manually adding an actor tag (not automatic for performance reasons); the simulation architecture has two layers: particle source emitter (emission origin) + gas controls emitter (physics simulation).

### Key Steps
1. **Enable Niagara Fluids plugin** — Edit > Plugins > search "Niagara" > find "Niagara Fluids" (Fluid Simulation Toolkit) > enable > OK (beta warning) > Restart Now; wait for shader compilation
2. **Create Niagara System** — Content Drawer > right-click in a folder > FX > Niagara System > New System from Template > Next; choose from: 2D gas sim, 2D liquid, 3D gas, 3D liquid options; select "Grid 3D Gas Simple Particle Source" > name it NS_Fire (or similar) > wait for shader compile
3. **Place in scene** — drag NS_Fire from Content Drawer into viewport; system appears with simulation volume in scene
4. **Increase voxel resolution** — select Niagara actor in scene > Details > find Resolution Max Axis > default ~100 = blocky/low quality; set 250 for good quality, 350 for high (slows editor); can leave low for viewport and increase for render-only via scalability settings
5. **Enable object collision** — by default no objects collide with the sim (prevents crashes); to enable collision for a specific mesh: select the mesh > Details > search "Tags" > Actor Tags > add tag "Fluid" (or the tag specified in your Niagara template); simulation will now respond to that mesh
6. **Verify collision in Niagara** — double-click NS asset > select emitter layer > Emitter Summary > Simulation > Static Mesh = ON (if having collision issues)
7. **Understand architecture** — double-click NS > two emitters: (a) Particle Source Emitter = emits particles that act as fluid source; (b) Gas Controls Emitter = applies physics forces + simulates fluid behavior; solo each to understand their roles

### UE Systems / Parameters
- **Niagara Fluids plugin** — Edit > Plugins; separate from base Niagara; required for Grid 3D Gas, Grid 3D Liquid templates; beta in UE5
- **Grid 3D Gas** — voxel-based volumetric gas simulation; fire, smoke, explosions; interacts with tagged objects in scene; resolution controlled by Resolution Max Axis
- **Resolution Max Axis** — number of voxels along the longest simulation axis; ~100 = fast/blocky; 250 = good quality; 350+ = slow; affects both viewport and render unless scalability is configured
- **Actor Tags** — Details > Actor Tags; add "Fluid" tag (or template-specified tag) to static meshes to enable collision with the Niagara fluid sim
- **Particle Source Emitter** — emits particles that seed the fluid simulation; controls emission origin, rate, velocity; feeds into Gas Controls Emitter
- **Gas Controls Emitter** — receives particle data from source emitter; applies physics (buoyancy, vorticity, dissipation, gravity); produces the visible fluid simulation

### Difficulty
Intermediate

### UE Version
UE 5.x (Niagara Fluids — early UE5 era, beta plugin)

### Tags
`#niagara` `#vfx` `#simulation` `#particles` `#intermediate`

---

## Related Entries
- [[unreal-engine-for-filmmakers---cinematic-vfx-for-free---ue5-part-2]] — Part 2 (parameter tweaking + lighting)
- [[unreal-engine-for-filmmakers---incredible-realtime-particle-simulations-for-free]] — companion particle simulations tutorial
- [[how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way]] — another simulation rendering workflow
