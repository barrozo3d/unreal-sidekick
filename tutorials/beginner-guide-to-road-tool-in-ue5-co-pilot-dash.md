---
title: Beginner Guide to Road Tool in UE5 Co-Pilot DASH
source: YouTube
url: https://www.youtube.com/watch?v=x6DR-CGi8dE
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.3
ue_version: "UE 5.x"
tags: [dash-1.3, road-tool, curves, terrain-projection, world-building, beginner]
extraction_status: complete
frames_dir: tutorials/frames/beginner-guide-to-road-tool-in-ue5-co-pilot-dash/
frame_count: 4
---

# Beginner Guide to Road Tool in UE5 Co-Pilot DASH

**Source:** [YouTube](https://www.youtube.com/watch?v=x6DR-CGi8dE)
**Author:** Polygonflow Dash
**Duration:** 3m45s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Greetings, I'm Jonathan, Polygonflow's Community Director for Dash, our next Gen plugin for Unreal Engine that makes creating environments a total breeze. In this video, I'll be covering the road tool, the newest addition to Dash 1.3. Let's hop into it and see what this thing is actually capable of.

**Frame:** tutorials\frames\beginner-guide-to-road-tool-in-ue5-co-pilot-dash\frame_000.jpg

### Dash [0:16]
**Transcript:** We'll start by opening Dash and then type terrain into the Dash prompt window. Once the terrain is in place with some moderately large hills to work with, we'll prompt Dash to create a curve and then position the camera above the terrain so it's easier to see what we're doing. Expand the curve tool options and then select start drawing. Draw out your preferred road shape. Once you're finished, hit enter to complete drawing. The curve tool creates conforming line work over the terrain, which is going to come in handy very soon.

**Frame:** tutorials\frames\beginner-guide-to-road-tool-in-ue5-co-pilot-dash\frame_001.jpg

### Road Tool [1:13]
**Transcript:** Next, type road into the Dash prompt bar and hit enter to bring up the road tool. At first glance, it'll look a little bit wonky. That's because it needs to be customized to match the terrain and the curve that you're using to generate the road. Make sure that the curve is selected, then click the plus sign in the curves option to add it to the road tool's calculations. Looking at the road, you'll see the wonkiness that I mentioned earlier. That's okay though. We just need to add more density to the road and increase its width. A density value of 0.9 is a pretty good point to work with, which adds enough polygonal density to the mesh to match the roundness of the curve. Width is pretty self-explanatory, a value of 10 works well here. Increasing smoothness will also help the road affix itself to the drawn curve. Next, select the terrain and click the plus icon next to surface. This will project the road mesh onto the terrain. After that, we'll want to increase the sync value to raise the road above the terrain to avoid intersecting Z-fighting with the terrain.

**Frame:** tutorials\frames\beginner-guide-to-road-tool-in-ue5-co-pilot-dash\frame_002.jpg

### Conclusion [2:33]
**Transcript:** What I really want to show off is how interactive the Dash road tool is. It takes into account every change that you make to your curve or to the terrain mesh the road is being projected on. This allows for endless, non-destructive iteration and lets you focus on being creative with much less worry about having to spend tons of time reworking complex road work that you'd built previously. Because Dash is non-destructive, you can change anything about this environment and simply undo the changes or adjust it how you will. There's no limit to your creativity here. I'm Jonathan and this was another tutorial on using Dash. Thanks for watching.

**Frame:** tutorials\frames\beginner-guide-to-road-tool-in-ue5-co-pilot-dash\frame_003.jpg


---

## Structured Notes

### Core Technique
Dash 1.3 Road Tool: draw a terrain-conforming curve → assign to Road Tool → set density (0.9), width, smoothness → project onto terrain mesh via Surface → raise with Sync value to prevent Z-fighting. Fully non-destructive; updates live when curve or terrain changes.

### Summary
3.75-minute beginner Road Tool introduction (Dash 1.3) by Jonathan. The road tool was a new addition in Dash 1.3. Workflow: terrain → draw curve (conforms to terrain) → type `road` → expand tool → add curve → set density 0.9 (polygon density to follow curve smoothness) + width 10 + smoothness → add terrain to Surface for projection → increase Sync to lift road above terrain. Fully live: editing curve or terrain auto-updates the road. Non-destructive throughout.

### Key Steps
1. **Create terrain** — type `terrain` → adjust size for road scale.
2. **Draw curve** — type `create curve` or `curve` → expand tool → Start Drawing → draw road path → Enter to finish; curve conforms to terrain surface.
3. **Open Road Tool** — type `road` → hit Enter.
4. **Add curve** — select curve → click + icon in Curves section.
5. **Set density** — ~0.9 provides enough poly density to follow curve roundness without artifacts.
6. **Set width** — value of 10 is a good starting point.
7. **Set smoothness** — increases road mesh conformance to drawn curve.
8. **Project onto terrain** — select terrain → click + icon in Surface section → road mesh projects onto terrain.
9. **Sync value** — increase to raise road above terrain surface to prevent Z-fighting.
10. **Apply material** — drag Megascans or own road material from Content Library onto road mesh.
11. **Iterate non-destructively** — edit curve points or terrain at any time; road updates automatically.

### UE Systems / Blueprints / Settings
- **Road Tool (Dash 1.3)** — curve-based procedural road mesh; density, width, smoothness params; Surface projection onto any mesh
- **Density (~0.9)** — polygon subdivision density; needs to be high enough to match curve curvature
- **Width** — road mesh width in UE units
- **Smoothness** — curve adherence strength
- **Surface projection** — select terrain + add to Surface list; road projects onto terrain Z
- **Sync value** — lifts road above terrain to avoid Z-fighting; replaces manual offset
- **Non-destructive** — curve edits and terrain changes propagate to road automatically; no rebake needed

### Difficulty
Beginner

### UE Version
UE 5.x (Dash 1.3)

### Tags
`#dash-1.3` `#road-tool` `#curves` `#terrain-projection` `#world-building` `#beginner`

---

## Related Entries
- [[getting-started-with-dash---easy-world-building-in-ue5]] — Dash 1.8 road tool with road markings, presets, dual proximity mask
- [[beginner-terrain-tool-tutorial-for-ue5]] — terrain creation (same series)
- [[path-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — curve draw tool detail (same curve system)
