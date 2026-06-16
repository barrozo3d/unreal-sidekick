---
title: DASH 1.10 - PROCEDURAL SCATTER PRESETS IN UE5
source: YouTube
url: https://www.youtube.com/watch?v=EN6X-d6DIb0
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.10
ue_version: "UE 5.x"
tags: [dash-1.10, presets, compound-presets, path-scatter, physics-paint, decal-scatter, blueprint-scatter, world-building, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/dash-110---procedural-scatter-presets-in-ue5/
frame_count: 9
---

# DASH 1.10 - PROCEDURAL SCATTER PRESETS IN UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=EN6X-d6DIb0)
**Author:** Polygonflow Dash
**Duration:** 10m7s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hello, I'm Thomas from Polygonflow. Today I'm excited to show you the latest updated Dash, the worldbuilding plugin for Unreal Engine 5. This update brings a complete overhaul of our preset system, making Dash even easier to use, more flexible and significantly more powerful. In addition to that, we've added several new features and improvements across the plugin. So let's jump in.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_000.jpg

### Presets [0:24]
**Transcript:** Alright, let's start by creating a simple cliff preset for a canyon using PathScatter. First, I use the draw curve tool to define the shape of my canyon. Then I go to the content browser, find my preferred cliff asset, and while my curve is selected, I drag it into the level by holding Ctrl to see the drop options. From there, I choose scatter on selected to automatically create the PathScatter on my curve. Now I can tweak a few settings such as density and scale. Once I'm happy with the result, I can create a preset using the preset icon in the tool panel. I will give it a name, some text, and the thumbnail, then I choose global scope and save it. With global scope, I can access the preset in any of my projects. Now let's open a new empty level and try it out. In the new level, I open PathScatter from the dashboard. When I click the preset icon, I can see my newly created canyon preset. And with a single click, it's recreated exactly as before. And as you can see, everything remains fully procedural, so I can continue adjusting any of the settings just like before.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_001.jpg

### Compound Presets [1:50]
**Transcript:** And now let's expand this simple cliff preset into something more advanced, an overgrown canyon using the updated compound and reference systems. So first, I scatter some rocks under the cliffs using the same spline as before. Next I will scatter some foliage onto the cliffs using surface scatter. I select the cliffs, hold Ctrl and drag in a few foliage assets and choose scatter on selected. Then I adjust the settings like density, height, mask, and scale to get a natural distribution. Next I want some rocks on the ground. So I will select the plane beneath my cliffs and scatter some assets onto it. To remove rocks underneath the cliffs, I can use a proximity mask. I pin the ground scatter tool to keep it open. Select the cliffs and assign them as proximity objects. Then I tweak the distance and width to control exactly where the rocks appear around the cliff formations. Now the setup looks good. Let's organize everything using the compound and reference systems. I click a property, choose create compound tool, and name it overgrown canyon. Then I add the key properties for each tool to the compound's edit table.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_002.jpg

### Physics Paint Scales [5:10]
**Transcript:** A new feature I want to show you today is an improvement to the physics paint. You can now control object scaling using the min and max scale range. While in physics paint mode, I can simply adjust these values to introduce natural size variations as I paint. This is a small addition, but it gives you more control and more organic results when painting assets into your scene. And after that, I just drop in the Dash water plane and the scene is done.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_003.jpg

### Preset Library [6:13]
**Transcript:** To make managing and using presets even easier, we've added a dedicated preset library inside the content browser. Here you can browse, search, and quickly access all your Dash presets in one place. For example, here is my overgrown canyon preset from before. On the left side, you can find a folder structure where presets are organized into different categories, including project and global presets. If you save a preset with global scope, it becomes available across all your Unreal Engine projects. Just keep in mind that the assets used in the preset need to exist at the same location in the other project for everything to work correctly.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_004.jpg

### Built-in Presets [6:51]
**Transcript:** To help get started with the new preset system and with Dash in general, we've included a bunch of presets in Dash 1.10. All of them are free to use, explore, and customize. Some are simple single tool presets, while others are more advanced compound setups that demonstrate how different tools can work together. All built-in presets use free-to-use assets from Quaternius, so if you like what you see, you can check out the full library as well. In our presets, these assets act as placeholders. So once you place a preset into your level, you can easily replace the assigned meshes with your own assets and adapt everything to your project. Another new feature in Dash 1.10 is that PathScatter now supports decals and blueprint actors.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_005.jpg

### Decal Scattering [8:12]
**Transcript:** For example, I can draw a curve and scatter footstep decals along it. Let's change the scatter type to actors. To make the footsteps look natural, I just tweak the settings a bit.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_006.jpg

### Blueprint Scattering [8:51]
**Transcript:** Let's try a blueprint. I place a blueprint in my level. Select the curve and open path scatter. I simply switch the scatter type from instances to actors again and add the curve and the blueprint. And just like that, the blueprint is scattered along this line. This makes path scatter much more flexible, especially for gameplay elements or more advanced setups.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_007.jpg

### Outro [9:22]
**Transcript:** And that wraps up Dash 1.10. Using the completely redesigned preset system, built-in presets, improved path scatter and scale control in physics paint, Dash is now even easier to use while giving you more flexibility and power when building worlds in Unreal Engine 5. Thanks for watching and see you in the next one.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_008.jpg


---

## Structured Notes

### Core Technique
Dash 1.10 preset system overhaul: single-tool presets (global/project scope), compound presets (multi-tool setups with editable reference table), dedicated Preset Library in content browser, built-in Quaternius presets, plus PathScatter now supports decals and Blueprint actors, and Physics Paint gained min/max scale control.

### Summary
10-minute Dash 1.10 release video by Thomas. Demonstrates the completely redesigned preset system: create a single-tool PathScatter preset (canyon cliff) → save with global scope → one-click recall in any project; expand into a compound preset (cliff + foliage on cliff + rocks on ground with proximity mask) → name and save with editable reference table for key parameters. New Preset Library browser in Content Browser (project/global categories, built-in Quaternius placeholder presets replaceable with own assets). New: PathScatter supports decals and Blueprint actors (switch type from Instances to Actors). Physics Paint: new min/max scale range for organic size variation while painting.

### Key Steps
1. **Single-tool preset** — draw curve → Ctrl+drag cliff asset → scatter on selected → tweak density/scale → preset icon in tool panel → name + thumbnail + choose Global scope → Save.
2. **Recall preset** — new level → open PathScatter → click preset icon → click canyon preset → recreated fully procedurally.
3. **Compound preset** — build multiple tools on same curve/surface (PathScatter cliffs + surface scatter foliage on cliffs + surface scatter rocks on ground with proximity mask) → compound tool → Create Compound Tool → name → add key properties from each tool to edit table → save as preset.
4. **Preset Library** — Content Browser → Preset Library tab → browse/search; project presets (current project only) vs global presets (all projects); global requires assets at same content path in target project.
5. **Built-in presets** — included in Dash 1.10; free Quaternius placeholder meshes; swap meshes in edit table for own assets.
6. **PathScatter decals** — draw curve → open PathScatter → switch scatter type to Actors → add decal → scatter decals along curve.
7. **PathScatter blueprints** — same workflow: scatter type = Actors → add Blueprint → Blueprint scattered along curve; works for gameplay elements.
8. **Physics Paint scale control (1.10)** — in Physics Paint mode → set min/max scale range → painted assets get randomized scale variation within range.

### UE Systems / Blueprints / Settings
- **Preset (single-tool)** — preset icon in tool panel; name + description + thumbnail; Global scope = available all projects (assets must match content path); Project scope = current project only
- **Preset Library (1.10)** — dedicated tab in Dash Content Browser; browse/search; project/global folder categories
- **Compound Preset** — groups multiple tools into one preset; key parameters exposed in an editable reference table; entire multi-tool setup recreated with one click
- **Built-in Presets (1.10)** — Quaternius free asset placeholders; mesh slots replaceable with own assets via edit table
- **PathScatter Actors mode (1.10)** — switch scatter type from Instances to Actors; supports Decals and Blueprint actors; enables gameplay-element scattering
- **Physics Paint min/max scale (1.10)** — scale range slider in Physics Paint mode; introduces natural size variation while painting

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.10)

### Tags
`#dash-1.10` `#presets` `#compound-presets` `#path-scatter` `#physics-paint` `#decal-scatter` `#blueprint-scatter` `#world-building` `#intermediate`

---

## Related Entries
- [[dash-111---unreal-engine-world-building-just-got-easier]] — Dash 1.11 extends presets with Drawable Presets
- [[path-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — PathScatter fundamentals
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Surface Scatter fundamentals
- [[getting-started-with-dash---easy-world-building-in-ue5]] — Dash 1.8 Physics Paint + road tool
