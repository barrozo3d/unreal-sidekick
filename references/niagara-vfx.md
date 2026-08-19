---
class: topic-reference
verified: partial
sources:
  - tutorials/  (corroboration audit, batch B4 -- see note)
last_verified: 2026-08-19
version_basis: "unknown"
# Origin: model memory. Audited 2026-08-19 (batch B4) -- no fabricated names
# found. Parameters/API symbols remain unverified. Tutorial beats reference.
---
> ## Audit note — batch B4, 2026-08-19
>
> No fabricated names found. Flags are Niagara module and data-interface names (`Color Over Life`, `Grid2D Collection`, `Gas Solver`) plus settings; corpus covers Niagara (56 files) at workflow level only.
>
> **Method and its ceiling.** Every term this file asserts was checked against the
> skill's 362 ingested tutorials with `audit_references.py`. That corpus is built
> from spoken narration, so it corroborates what presenters **say** — node and
> tool names — and structurally cannot corroborate what they only **show or
> type**: parameter names, default values, console variables, API symbols.
> **Corroboration finds fabricated names, not wrong values.** Treat parameters and
> code identifiers in this file as unverified until checked against Epic's docs.
>
> Across all of `unreal-sidekick`, the audit found **no fabricated node names**.
> Full detail: `houdini-wand/PROMO_ENTRY_CLEANUP_PLAN.md` (workstream B).

# Niagara VFX — Reference

Niagara is Unreal Engine's primary VFX system (UE 4.20+). It replaced Cascade.

## Core Architecture

```
Niagara System
└── Emitter(s)
    ├── Emitter Update (runs once per frame per emitter)
    ├── Particle Spawn (runs once per particle birth)
    └── Particle Update (runs once per particle per frame)
        └── Renderer(s)
```

## Emitter Types

| Type | When to use |
|------|-------------|
| **GPU Sim** | Large particle counts (10k+), GPU-heavy effects |
| **CPU Sim** | Particle logic that reads back to CPU, collision with complex geometry |
| **Mesh Particles** | Instanced static meshes as particles (debris, rocks) |
| **Ribbon** | Trails, lightning, streaks — connects particles in sequence |
| **Sprite** | Camera-facing billboards — default particle type |
| **Light** | Particles that emit dynamic light |
| **Decal** | Particles that project decals onto surfaces |

## Key Modules by Stage

### Emitter Update
- `Spawn Rate` — particles/second
- `Spawn Burst Instantaneous` — one-time spawn count
- `Emitter Lifetime` — loop/duration control

### Particle Spawn
- `Initialize Particle` — set initial Position, Velocity, Color, Size, Lifetime
- `Add Velocity` — initial velocity vector
- `Sphere Location` — spawn in sphere volume
- `Skeletal Mesh Location` — spawn from mesh surface/bones

### Particle Update
- `Gravity Force` — apply gravity
- `Drag` — velocity damping
- `Curl Noise Force` — turbulent/fluid-like motion
- `Vortex Force` — rotational force
- `Point Attraction Force` — attract toward a point
- `Color Over Life` — gradient color by normalized age
- `Scale Sprite Size Over Life` — size curve by normalized age
- `Collision` — particle collision with scene geometry

## GPU Simulation Notes
- Max particles per emitter: ~1M practical (GPU memory limited)
- Can't read back to CPU per-particle (no Blueprint access to individual particles)
- Use `Niagara Data Interface` for communication with Blueprints
- GPU sims require `Shader Model 5+`

## Fluid Simulation (Niagara Fluids)
- Plugin: `Niagara Fluids` (must enable in Project Settings > Plugins)
- Uses Grid2D/Grid3D data interfaces for fluid grids
- `Gas Solver` — smoke/fire simulation
- `Shallow Water Solver` — 2D water surface
- Requires Compute Shaders — GPU only

## Data Interfaces
| Interface | Use |
|-----------|-----|
| `Skeletal Mesh` | Sample mesh surface, bones, sockets |
| `Static Mesh` | Sample static mesh surface/vertices |
| `Spline` | Follow or sample from a spline |
| `Texture Sample` | Read texture data into particles |
| `Blueprint Generated` | Two-way communication with Blueprints |
| `Audio` | Drive particles from audio spectrum |
| `Grid2D Collection` | Fluid grid (2D) |
| `Grid3D Collection` | Fluid grid (3D) |

## Common Cinematic VFX Setups

### Dust Mote / Atmospheric Particles
- CPU emitter, Sprite renderer
- Spawn Rate: low (10-50)
- `Sphere Location` radius matching shot scale
- Curl Noise Force for gentle drift
- Alpha fade on Color Over Life

### Impact / Hit Effect
- GPU emitter, Sprite + Mesh renderers combined
- `Spawn Burst Instantaneous` — one frame burst
- `Add Velocity in Cone` for directional spray
- Short lifetime (0.3-1s), fast color fade

### Fire / Smoke (Real-time)
- Use `Niagara Fluids` Gas Solver if performance allows
- Or: multiple sprite emitters layered (fire core, outer flame, smoke)
- Rendered in separate passes and composited if needed for MRQ

## Movie Render Queue Integration
- Niagara can be controlled via Sequencer tracks
- `Niagara System Lifecycle Track` in Sequencer manages sim lifecycle
- For offline renders: use `High-Quality Rendering` mode (allows slower GPU sim)
- Warm-up frames: set `Engine Warm Up Count` in MRQ render settings
