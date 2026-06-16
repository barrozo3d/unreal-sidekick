---
title: How to Create Procedural Cables in UE5 - World Building Plugin
source: YouTube
url: https://www.youtube.com/watch?v=uNzCmzeEISU
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.4
ue_version: "UE 5.x"
tags: [dash-1.4, cable-tool, procedural, world-building, environment-art, beginner]
extraction_status: complete
frames_dir: tutorials/frames/how-to-create-procedural-cables-in-ue5---world-building-plugin/
frame_count: 4
---

# How to Create Procedural Cables in UE5 - World Building Plugin

**Source:** [YouTube](https://www.youtube.com/watch?v=uNzCmzeEISU)
**Author:** Polygonflow Dash
**Duration:** 5m49s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Greetings, I'm Jonathan, Polygonflow's Community Director. Today I'm covering the Cable tool, one of many tools available in Polygonflow's Dash, our next Gen Unreal Engine plugin. This is the best way to create wiring and other types of cables in Unreal, and I'll show you how. I have these free utility poles from Polyhaven, and I want to wire them up. I'll use dummy box objects in Unreal to do it. After selecting them in the outliner, I can open the Dash toolbar and then type Cable tool to prompt Dash to select the Cable tool. The Cable tool has three different modes with individual settings per mode. Let's start off with the default mode, Objects. With this mode, we simply add the currently selected objects to the Cable tool and it will auto-populate a set of cables between the dummy objects with default parameters. Let's control those parameters a bit and start by adjusting the divisions option, which reduces or increases the amount of subdivision in each cable. Gradius controls the thickness of the cables. The higher the value, the thicker the end result will be. Gravity min and max both control the droop of the cables and how they're affected by the gravity in the world.

**Frame:** tutorials\frames\how-to-create-procedural-cables-in-ue5---world-building-plugin\frame_000.jpg


---

## Structured Notes

### Core Technique
Dash Cable Tool: three modes (Objects, Curve, Mixed) — select objects or draw curves → cables auto-generate between them with controllable divisions, radius, gravity droop, and material.

### Summary
6-minute Cable Tool tutorial (Dash 1.4 era) by Jonathan. Uses free Polyhaven utility poles + dummy box objects as cable anchor points. Three modes: Objects (select objects → cables auto-populate between them), Curve (draw custom cable paths), Mixed. Key parameters: Divisions (mesh subdivision/smoothness), Gradius/Radius (cable thickness), Gravity Min/Max (cable droop amount). Material applied from Content Library or custom. Practical use case: utility wiring, hanging cables, rope bridges between architecture.

### Key Steps
1. **Place anchor objects** — position meshes or dummy boxes at cable connection points (e.g., tops of utility poles).
2. **Select anchors** — select all anchor objects in outliner or viewport.
3. **Open Cable Tool** — type `cable tool` in Dash prompt bar.
4. **Objects mode (default)** — add selected objects to Cable Tool → cables auto-generate between all selected objects.
5. **Divisions** — adjust for smoother/rounder cable curves vs performance.
6. **Gradius/Radius** — controls cable thickness.
7. **Gravity Min/Max** — controls droop amount (range of gravity influence = variation in sag between cables).
8. **Apply material** — drag material from Content Library onto cables.
9. **Curve mode** — alternative: draw custom curve paths for precise cable routing.

### UE Systems / Blueprints / Settings
- **Cable Tool (Dash)** — three modes: Objects (auto-connect selected), Curve (custom path), Mixed
- **Divisions** — mesh subdivision per cable segment; higher = smoother curves
- **Gradius/Radius** — cable mesh thickness
- **Gravity Min/Max** — sag droop range; min/max creates variation between cables rather than uniform sag
- **Polyhaven** — free 3D assets source (utility poles, etc.)

### Difficulty
Beginner

### UE Version
UE 5.x (Dash 1.4 era)

### Tags
`#dash-1.4` `#cable-tool` `#procedural` `#world-building` `#environment-art` `#beginner`

---

## Related Entries
- [[dash-110---procedural-scatter-presets-in-ue5]] — Dash 1.10 compound presets include Cable Tool in fence/pier setups
- [[how-to-create-vines-procedurally-in-unreal-engine-5]] — similar procedural path-following for organic cables/vines
- [[create-run-down-environments-in-minutes---dash-ue5]] — cables used in run-down urban environment
