---
title: Beginner Water Tool Tutorial for UE5
source: YouTube
url: https://www.youtube.com/watch?v=oY4pVa6mPYM
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-early
ue_version: "UE 5.x"
tags: [dash-early, water, terrain, world-building, beginner]
extraction_status: complete
frames_dir: tutorials/frames/beginner-water-tool-tutorial-for-ue5/
frame_count: 3
---

# Beginner Water Tool Tutorial for UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=oY4pVa6mPYM)
**Author:** Polygonflow Dash
**Duration:** 1m49s | 3 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hi, I'm Jonathan, Polygonflow's Community Director, and I'm here to showcase our next Gen Plug-in Dash, which is a world-building tool for Unreal Engine, greatly simplifying the process of creating environments. From content browsing to asset scattering, camera setup, color grading, and everything in between, you'll dash right through your next environment. In this video, I'm going to go over how to create a water material in a brand new scene.

**Frame:** tutorials\frames\beginner-water-tool-tutorial-for-ue5\frame_000.jpg

### Getting Started [0:25]
**Transcript:** To get started, click on the Dash icon next to the mode drop-down menu. Then type terrain in the Dash prompt field, and hit enter to open the terrain editor. You can adjust the terrain to your liking here using the various adjustment options in the terrain generator.

**Frame:** tutorials\frames\beginner-water-tool-tutorial-for-ue5\frame_001.jpg

### Using Prompting [0:49]
**Transcript:** Once you're finished with the adjustments, click the bridge icon in Dash to open the content library, then drag a material that you'd like to work with onto the new terrain. Next, we'll use Dash to prompt a new plane by typing plane in the prompt field. Then hit R to access the scale tool, and scale the plane to your preferred size to create geometry for the water material to be applied to. Once you're happy with the water plane's placement, type water in the Dash prompt field, and select set water material. Click on the plane, select the material adjustment properties, and adjust the water to your liking. That's how simple this is. What Dash is doing is taking the process of creating a water material and saving you both time and effort by creating it for you. But if you want to learn how it's built in real time, you can open the material and inspect it. Check in with us next time for more beginner-focused tutorials on how you can work with Dash inside of Unreal Engine.

**Frame:** tutorials\frames\beginner-water-tool-tutorial-for-ue5\frame_002.jpg


---

## Structured Notes

### Core Technique
Dash water plane creation: type `plane` → create flat mesh → scale with R tool → type `water` → Set Water Material applies a pre-built Dash water material; material properties editable inline.

### Summary
1.75-minute beginner water tutorial by Jonathan. Minimal steps: create terrain → apply terrain material from Content Library → type `plane` → scale to cover water area → type `water` → Set Water Material. Material is pre-built by Dash but fully inspectable/editable in material editor. Part of the Jonathan beginner series.

### Key Steps
1. **Open Dash** — icon next to mode dropdown.
2. **Create terrain** — type `terrain` → adjust settings.
3. **Apply terrain material** — B icon → Content Library → drag Megascans material onto terrain.
4. **Create water plane** — type `plane` → hit Enter → plane spawns at scene center.
5. **Scale plane** — press R (scale tool) → scale to desired water area size; move into position.
6. **Set water material** — type `water` → select Set Water Material → Dash applies built-in water material to selected plane.
7. **Adjust water** — click plane → material adjustment properties → tweak parameters.

### UE Systems / Blueprints / Settings
- **Dash water material** — pre-built; applied via `set water material` action; adjustable via material properties panel; full material graph accessible for inspection
- **R key** — scale tool shortcut in UE5 viewport (not Dash-specific)

### Difficulty
Beginner

### UE Version
UE 5.x (Dash early release)

### Tags
`#dash-early` `#water` `#terrain` `#world-building` `#beginner`

---

## Related Entries
- [[beginner-terrain-tool-tutorial-for-ue5]] — terrain parameters (same series)
- [[beginner-content-library-tutorial-for-ue5]] — content library usage (same series)
- [[introducing-dash-for-unreal-engine-5]] — original Dash intro with water plane workflow
- [[new-ue5-plugin---easy-environment-creation]] — water material + roughness adjustment workflow
