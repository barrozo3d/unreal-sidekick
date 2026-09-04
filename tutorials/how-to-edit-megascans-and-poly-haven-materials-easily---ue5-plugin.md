---
title: How to Edit Megascans and Poly Haven Materials Easily - UE5 Plugin
source: YouTube
url: https://www.youtube.com/watch?v=7NKl90gt0w0
author: Polygonflow Dash
ingested: 2026-06-23
ue_version: "UE5"
tags: [materials, megascans, polyhaven, polygonflow-dash, plugin, displacement, nanite, environment, texturing]
extraction_status: complete
frames_dir: tutorials/frames/how-to-edit-megascans-and-poly-haven-materials-easily---ue5-plugin/
frame_count: 9
---

# How to Edit Megascans and Poly Haven Materials Easily - UE5 Plugin

**Source:** [YouTube](https://www.youtube.com/watch?v=7NKl90gt0w0)
**Author:** Polygonflow Dash
**Duration:** 7m6s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro & Getting a Material [0:00]
**Transcript:** Greetings, I'm Jonathan, Pauling on flow's community director for Dash, our next Gen Unreal Engine plugin.  In this video I'll be covering our material editing tool, which has been significantly improved in Dash 1.4.  So let's start by opening Dash.  Open the content browser and then navigate to an existing material you'd like to work with, then drag and drop it into the environment.

**Frame:** tutorials\frames\how-to-edit-megascans-and-poly-haven-materials-easily---ue5-plugin\frame_000.jpg

### Opening the Material Edit tool [0:23]
**Transcript:** With the terrain selected, the Dash panel has an art palette icon that you'll select to open the material editor.  Before we proceed, it is important to note that the new material editor system only works with Megascans and Polyhave and Assets at the moment.  Future builds of Dash should allow you to work with any asset that you own in the system.  Expand the window and you'll see a whole suite of tools to work with.

**Frame:** tutorials\frames\how-to-edit-megascans-and-poly-haven-materials-easily---ue5-plugin\frame_001.jpg

### Adjusting Basic Material Settings [0:46]
**Transcript:** With the material editor you can adjust the Albedo Hue, the Albedo Saturation, the Albedo Brightness and Contrast.  You can also adjust the roughness of the material in addition to changing the Normal Maps Intensity via a slider.  You can also adjust the texture tiling from the material editor too.

**Frame:** tutorials\frames\how-to-edit-megascans-and-poly-haven-materials-easily---ue5-plugin\frame_002.jpg

### Displacement [1:08]
**Transcript:** Before displacement can be used, you need to select the mesh that you want to displace, then type Nanite and Dash and select the Command, Actor Switch Nanite to enable Nanite and Displacement for that mesh.  Then you can begin to play with the Displacement values.  Adjusting these values can cause shadow artifacts on the mesh, which can usually be fixed by slightly moving the mesh in the world.  Unrealth 5's Nanite system works great with real-time displacement and allows you to create much more interesting worlds using Dash.  You can use the Material Editor with Megascans or Polyhave and Objects as well.  And if you're the tinkering type, you can apply one of the material instances to one of your custom objects that you've imported into Unreal.  Replace textures and get Dash's Material Editor to work with those too.  If you don't like these settings or you just want to work with default settings again, you can use the Material Editor Options menu to reset all the values to default.  Working with Dash is fully procedural, so you can adjust anything on the fly without worrying about it.

**Frame:** tutorials\frames\how-to-edit-megascans-and-poly-haven-materials-easily---ue5-plugin\frame_003.jpg

### Adding & Adjusting Dirt Layer [2:13]
**Transcript:** In the latest versions of Dash, you can now break up textures by adding dirt to the material.  This has its own set of parameters that we can adjust to fine tune the material that we're using, from the intensity of the dirt, to the Albedo Hue,  overall dirt color saturation, brightness, and tiling too.  This allows you to customize the materials that you're working with, and in the future, even more options will be available here to improve the procedural texturing.  Let's use the Content Browser to drag some additional assets into the scene.  Dash now has a pretty robust snow system too.

**Frame:** tutorials\frames\how-to-edit-megascans-and-poly-haven-materials-easily---ue5-plugin\frame_004.jpg

### Adding & Adjusting Snow Layer [2:50]
**Transcript:** You can enable snow texturing by opening the snow rollout and clicking Enable Snow, which allows you to adjust the sharpness of the textured snow.  The angular slopes, the snow, will collect on.  The reflectivity of the snow by adjusting its roughness.  The chunkiness of the snow by adjusting the normal map and the tiling of the snow texture.  As with dirt, even more options will be available with the snow system as it continues to be improved and refined.  You can also use the snow and dirt systems with the rest of the material editor so you can change the surface properties of the object to make snow more visible.  Some assets are too bright for snow and dirt to show up well, so you can fix this by adjusting the material brightness and contrast, then play around with the coverage of the snow on the object.  Now that the snow is much easier to see.  Remember earlier when I said that Dash is fully procedural?

**Frame:** tutorials\frames\how-to-edit-megascans-and-poly-haven-materials-easily---ue5-plugin\frame_005.jpg

### Snow and Procedural Terrain [3:45]
**Transcript:** Let's try out the snow system on a Dash terrain by giving it a decent amount of subdivisions and surface variation for the snow system to work.  Once I'm happy with the terrain, I can add the grass texture from earlier and enable snow on it.  Then I can play with the settings and see what I get.  You can also adjust the terrain itself and the material will auto-populate the changes based on the surface topology of the terrain.  Pretty neat, right?  Having this fully procedural workflow and Unreal Engine makes creating environments super easy.  Now let's move on to water.  Type water in Dash and select Create Water to automatically create a plane with a pre-applied Dash Water Material.

**Frame:** tutorials\frames\how-to-edit-megascans-and-poly-haven-materials-easily---ue5-plugin\frame_006.jpg

### Adjusting Water Material [4:38]
**Transcript:** The plane Dash creates isn't big enough for my scene, so I'm going to rescale it to make it fit the environment that I've built.  For a plane this is a very simple way to create a plane with a pre-applied Dash Water Material.  For a plane this large without modified UVs, the default tiling range needs to be adjusted.  Sliding the tiling value around will change the values up to a point, but for anything higher than 100 you need to manually type in values to extend the sliding range.  I'll type in a large value and then adjust it until I'm happy with it.  The depth of the water determines how murky the water appears from a distance.  The depth of the water determines how murky the water appears from a distance.  The higher up the water plane is above an object, the murky or the object will appear as the depth value is increased.  Distortion uses the normal map to create the optical illusion of waves breaking up the refracted object under the water.  The stronger the value is, the more visible the refraction becomes.  Underlying hue and saturation changes the color of the objects and terrain below the water surface.  Both of these sliders work in concert to produce a subtle but noticeable color absorption pattern, which can resemble real-world oceans or something completely different entirely.  You can also change the intensity of the waves in the surface of the water by adjusting the normal slider.  You can also use the normal hue and saturation sliders to get a wildly different water effect or dial in the tropical green that I'm looking for here.

**Frame:** tutorials\frames\how-to-edit-megascans-and-poly-haven-materials-easily---ue5-plugin\frame_007.jpg

### Using the Water Material [6:20]
**Transcript:** Water isn't just for larger environments either.  You can place a plane within a crate to have a bucket of water to work with.  And if you adjust the material parameters, you can make it into a bucket of blood or perhaps radioactive sludge.  The only limit is your imagination.  Thanks for watching another tutorial on how to work with Polygonflow-dash.  This was Jonathan Polygonflow's Community Director and let us know what you think of the comments.  We'll see you next time.

**Frame:** tutorials\frames\how-to-edit-megascans-and-poly-haven-materials-easily---ue5-plugin\frame_008.jpg


---

## Structured Notes

### Core Technique
Polygonflow Dash 1.4 plugin material editor: non-destructive real-time material adjustment for Megascans and Poly Haven assets in UE5. Covers Albedo, roughness, normal, tiling, Nanite displacement, procedural dirt and snow layers, and a built-in water material system. Fully procedural — all changes update live.

### Summary
7-minute tutorial by Polygonflow showing how to use the Dash 1.4 plugin's material editor to modify Megascans and Poly Haven materials without touching the material graph. The editor exposes Albedo hue/saturation/brightness/contrast, roughness, normal intensity, texture tiling, Nanite-driven displacement, procedural dirt and snow layers (each with their own controls), and a water material creator (tiling, depth, distortion, wave normals). All edits are non-destructive and live-updating. Currently limited to Megascans and Poly Haven assets, with broader asset support planned.

### Key Steps
1. **Open material editor** — select a mesh placed in scene, click the art palette icon in the Dash panel
2. **Albedo** — adjust Hue, Saturation, Brightness, Contrast sliders
3. **Roughness / Normal** — adjust roughness slider and Normal Map Intensity slider
4. **Tiling** — adjust texture tiling from the material editor
5. **Nanite displacement** — select mesh → type "Nanite" in Dash → run "Actor Switch Nanite" command to enable Nanite + displacement → then adjust displacement values (fix shadow artifacts by slightly moving mesh in world)
6. **Dirt layer** — enable in material editor; set intensity, Albedo Hue, saturation, brightness, tiling
7. **Snow layer** — open Snow rollout → Enable Snow → adjust sharpness, angular slope (where snow collects), roughness (reflectivity), normal map chunkiness, tiling; combine with base material brightness/contrast if snow isn't visible
8. **Water** — type "water" in Dash → "Create Water" → plane with Dash Water Material auto-created; resize plane; adjust: tiling (>100 requires manual value entry), depth (murkiness), distortion (wave refraction), underlying hue/saturation, wave normal intensity/hue/saturation
9. **Reset** — Material Editor Options → reset all values to default

### UE Systems / Blueprints / Settings
- **Polygonflow Dash plugin** — third-party UE5 plugin; v1.4 introduces improved material editor; compatible with Megascans and Poly Haven assets (custom asset support planned)
- **Dash panel** — main plugin UI; art palette icon opens material editor; search field for commands like "Actor Switch Nanite" and "Create Water"
- **Actor Switch Nanite command** — Dash command; enables Nanite + displacement on selected mesh (prerequisite for displacement in material editor)
- **Displacement shadow artifacts** — fix: slightly translate the mesh in world coordinates after enabling displacement
- **Dirt layer** — procedural dirt overlay; parameters: intensity, Albedo Hue, saturation, brightness, tiling
- **Snow layer** — procedural snow overlay; parameters: sharpness, angular slope coverage, roughness (shininess), normal map intensity (chunk size), tiling; use "Enable Snow" button to toggle
- **Dash Water Material** — pre-built water material applied to plane via "Create Water" command; parameters: tiling (manual entry required for >100), depth, distortion, underlying hue/saturation, wave normal intensity/hue/saturation
- **Material Editor Options** — menu within editor; "Reset to Default" option restores all sliders
- **Procedural workflow** — all Dash edits are non-destructive; can be adjusted at any time without breaking the material

### Difficulty
Beginner. No material graph knowledge required. Plugin abstracts all material editing into simple sliders.

### UE Version
UE5

### Tags
materials, megascans, poly-haven, polygonflow-dash, plugin, displacement, nanite, environment, texturing

---

## Related Entries
- `how-to-create-cinematic-environments-in-unreal-engine-5.md` — environment building techniques that complement material workflows
- `i-textured-the-entire-environment-using-a-single-texture.md` — contrasting manual single-texture approach vs plugin-assisted material editing
- `introduction-to-substrate-materials-unreal-engine-57.md` — advanced UE5 material system (Substrate) for deeper material customization
