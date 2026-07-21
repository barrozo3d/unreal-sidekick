---
title: Unreal Engine & Dash Medieval Environment Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=_SKfQJ5pAAc
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.7
ue_version: "UE 5.x"
tags: [dash-1.7, game-environments, scatter, grid-scatter, path-scatter, physics, cable, fog-cards, cross-project, presets, uds, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-dash-medieval-environment-tutorial/
frame_count: 12
---

# Unreal Engine & Dash Medieval Environment Tutorial

**Source:** YouTube
**Author:** Polygonflow Dash
**Duration:** ~12m | 12 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted — see ingested file...]

---

## Structured Notes

### Core Technique
Tomáš builds a medieval Russian-inspired environment for the Veldraham art challenge using Dash 1.7 — Grid Scatter for modular tower assembly (saved as preset), cross-project asset access, Physics Drop + Physics Paint for props in containers, path spline scatter for icicles (multiple curves on same scatter), Cable Tool for rooftop hanging cables, animated Fog Cards, Easy Snow plugin for snow layer, and UDS for atmospheric lighting.

### Summary
12-minute breakdown (not step-by-step tutorial) showing how Tomáš built a medieval snowy village environment for Lurter Studio's Veldraham art challenge. Assets: Cosmos Rocket plugin (Russian Village + Wicking Village packs) + free Cosmos assets. Workflow: Grid Scatter for main tower + structures (preset saves config) → reference images via Dashboard drag → water plane + Blender bridge → UDS for lighting → AI tag + cross-project access (Dash CB shows Fab, Polyhaven, Quixel alongside tagged project assets) → Physics Drop (objects into bucket) + Physics Paint (planks between barrels) → scatter foliage with proximity masking (multiple assets in same proximity mask, per-asset masking distance) → draw spline → Path Scatter icicles (multiple curves on same scatter) → Cable Tool (rooftop hanging cables; gravity + count) → Fog Cards (animated) → Easy Snow plugin → final render.

### Key Steps
1. **Grid Scatter — modular structure** — Grid Scatter for tower blocks (general shape first, details later); save as preset for reuse
2. **Dashboard reference images** — drag desktop images into Dash Dashboard panel for in-engine reference; good for dual-monitor-free setups
3. **Cross-project asset access (1.6+)** — compute/AI tag assets in one project → available in all projects via Dash CB; no manual folder migration
4. **Physics Drop** — Ctrl+drag assets into scene → "place overlapped" → select → Physics Drop; objects fall into containers naturally; duplicate with Physics still active
5. **Physics Paint** — Physics Paint brush mode; paint planks between barrels for natural placement
6. **Proximity Mask (foliage, multiple assets)** — include multiple scatter assets in same scatter; each asset gets its own masking distance in the proximity mask table
7. **Path Scatter (icicles, multiple curves)** — draw one or more curves; assign multiple curves to same Path Scatter; icicles follow all curves simultaneously; extended curve points followed automatically
8. **Bake Instances** — bake scattered instances → modify individually (delete/reposition)
9. **Cable Tool** — connect rooftop structures; gravity + count settings for hanging cables
10. **Fog Cards** — animated fog cards for atmosphere
11. **Snowfall (Easy Snow plugin)** — external Easy Snow plugin for snow accumulation on surfaces

### UE Systems / Blueprints / Settings
- **Grid Scatter preset** — save current Grid Scatter config as named preset → apply instantly to any new Grid Scatter (same configuration: spacing, rotation, mesh)
- **Dashboard image import** — drag image file from desktop into Dash Dashboard panel; stays in engine; good substitute for external reference viewers
- **Cross-project CB (1.6+)** — Dash CB shows: Fab + Polyhaven + Quixel + Project Assets (tagged across ALL projects); no migration needed
- **Proximity mask table — multiple assets** — open same surface scatter → multiple scatter meshes → proximity mask table → each row = one asset → individual distance control per asset
- **Multiple curves on Path Scatter** — Path Scatter can have multiple curves assigned simultaneously; all contribute to scatter distribution; extended curves auto-followed when scatter updates
- **Cosmos Rocket** — third-party plugin (Lurter Studio); installs as UE plugin → browse + download assets inside engine → free assets available; drag to scene
- **Easy Snow plugin** — external plugin for snow accumulation; used when Dash Snowfall tool not sufficient or project predates Dash 1.9

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.7 — Tool Presets, cross-project, no Mesh Pattern/ABO/Blend Material)

### Tags
`#dash-1.7` `#game-environments` `#scatter` `#grid-scatter` `#path-scatter` `#physics` `#cable` `#fog-cards` `#cross-project` `#presets` `#uds` `#intermediate`

---

## Related Entries
- [[creating-a-massive-procedural-game-world-in-ue5-with-dash]] — Tomáš game world pipeline with Property References + Compound Tool (1.7)
- [[dash-170---massive-ue5-world-building-tool]] — Dash 1.7 feature overview
- [[how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow]] — Jonathan MOUT training site; Road Tool + multi-scatter (1.6)
- [[recreating-a-helldivers-2-game-environment-in-ue5-with-dash]] — full Dash 1.7 playable level (same era)
