---
title: Creating a Blend Material in Unreal Engine 5 Just Got Easier
source: YouTube
url: https://www.youtube.com/watch?v=MoAk8c1ek7A
author: Polygonflow Dash
ingested: 2026-06-23
ue_version: "UE5"
tags: [dash, materials, blend-material, nanite-tessellation, road-tool, megascans, snow, wetness, environment, layered-materials, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/creating-a-blend-material-in-unreal-engine-5-just-got-easier/
frame_count: 9
---

# Creating a Blend Material in Unreal Engine 5 Just Got Easier

**Source:** [YouTube](https://www.youtube.com/watch?v=MoAk8c1ek7A)
**Author:** Polygonflow Dash
**Duration:** 8m54s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hello, today I'm going to show you how to customize mega-scan's materials to make them look wet,  rainy and snowy.  We will create a road mesh using the Dash Road tool, and see how easily we can create  a detailed surface on it.  The idea behind all the tools and dashes to make it easier to build words in Unreal  Engine 5 and let you stay in the creative flow throughout the full process.

**Frame:** tutorials\frames\creating-a-blend-material-in-unreal-engine-5-just-got-easier\frame_000.jpg

### Creating a Road [0:25]
**Transcript:** I have prepared a quick environment using the Surface Scatter Tool in Dash.  We first need a road, let's quickly create one.  I click on the Create button and select the Draw Curves option from the Curves tools.  And I draw it freehand on the surface.  Then I locate the road tool in the Dash toolbar.  I add my Curves to the Curves section and set the roads with.  As you can see, wherever I move my Curve, the road follows it.  This is also true for individual points.  Let's tidy up the area around the road.  I have prepared a masking reference in advance.  I specified proximity mask and follow settings as references.  Multiple actors can share the same settings, allowing me to modify them simultaneously.  If you are curious about the details, you can find another video linked in the description.  For I explain this feature in depth, I access the reference tool by clicking on the tool selection icon.  All my scatterings were now shared the same object, distance and follow settings.  I click the Pin icon so the tool panel stays open when I click on the road.  Then I add it as an object.  I set the distance.  The road is currently quite low poly, but I can adjust this in the shape or finding section by modifying the resolution and smoothness.  Now that we have a proper road, let's add a Megas Conroad material.  If you have already one from Bridge, you can simply search for it in the Dash Content Browser and drag and drop it onto the road.  It's important to note that currently Dash only supports material customization for Megas skins or polyhaving materials.  Now that I have applied the road material, I need to adjust the UV mapping so that it looks good.  Returning to the road tool, in the Geometry settings, I can adjust the road's UV scale.  Now I got my base road ready.  It's non-destructive, meaning I can reshape it however I like, and the environment dynamically reacts to it.  I scattered some trees across the terrain to cast nice shadows onto the asphalt.

**Frame:** tutorials\frames\creating-a-blend-material-in-unreal-engine-5-just-got-easier\frame_001.jpg

### Basic Material Customization [3:04]
**Transcript:** We don't have to stop at just basic material.  Let's open the material editor where you can find a lot of options for customizing the road.  Beyond color settings, you can add layers like dirt, rain or snow.  For example, I can select the snow option and with just a few parameter adjustments, I get the snowy surface.  There are plenty of settings here to experiment with.  But we can achieve an even more detailed result by using Dash Blend Material tool and enabling the night desolation.

**Frame:** tutorials\frames\creating-a-blend-material-in-unreal-engine-5-just-got-easier\frame_002.jpg

### Creating a Blend Material [3:45]
**Transcript:** Let's add higher subdivisions to the road so we can utilize the night desolation.  In the road tool geometry settings, I increase the subdivision value.  Then I switch to wireframe mode to better see what's happening.  Next we need to bake the road to convert it into a night mesh.  Unfortunately, this process will cause the road to lose its non-destructive properties.  So it's a good idea to create a backup if you think you might want to edit it later.  I click on this icon to convert my actor into a static mesh.  After that, I type the night into the dash toolbar, select it and enable it.  Then I enable the night desolation as well.  Next I choose three mega-scan materials from the dash asset library and while holding Ctrl, I drag and drop them onto the road mesh.  I select apply blend material.  Then I choose edit blend material from the tool spinal and adjust the tiling if needed.  I can mix the three materials however I like and tweak a bunch of settings individually for each layer.  I can mix the three materials however I like and tweak a bunch of settings individually for each layer.  This includes adjusting wetness and desolation.  I can also add extra layers like snow to the material and find you in them further.

**Frame:** tutorials\frames\creating-a-blend-material-in-unreal-engine-5-just-got-easier\frame_003.jpg

### Snow Layer [5:45]
**Transcript:** Speaking of snow again, I've made a scene to fit the look.

**Frame:** tutorials\frames\creating-a-blend-material-in-unreal-engine-5-just-got-easier\frame_004.jpg

### Snow on Objects [6:08]
**Transcript:** Here I will show you how easily I can add snow layer to mega-scan models.  I drag and drop a model into the scene.  In the tool spinal, I select the edit material option and just like with the roadness earlier, I can adjust the surface to make it snowy, wet or dirty.  We can also create rainy surfaces for assets.  Setting allows to control how wet the surface appears, how much rain falls on it and more.

**Frame:** tutorials\frames\creating-a-blend-material-in-unreal-engine-5-just-got-easier\frame_005.jpg

### Rain and Wetness [6:47]
**Transcript:** With the blend material tool, we can add detail and interest to surfaces in just minutes, as shown here in this small forest clearing.

**Frame:** tutorials\frames\creating-a-blend-material-in-unreal-engine-5-just-got-easier\frame_006.jpg

### Nanite Tesselation [7:15]
**Transcript:** The tool is now ready to be used to create a new layer.  And that's just a quick overview of our material editing tools.  The tool is demonstrated in this video are just a few of many available in-dash, all designed to make building environments in Unreal Engine easier and faster.

**Frame:** tutorials\frames\creating-a-blend-material-in-unreal-engine-5-just-got-easier\frame_007.jpg

### Outro [8:09]
**Transcript:** If you would like to try them all for free, you can do so for 30 days using the link in the description.  Thank you for watching, see you in the next one.

**Frame:** tutorials\frames\creating-a-blend-material-in-unreal-engine-5-just-got-easier\frame_008.jpg


---

## Structured Notes

### Core Technique
Dash workflow for Megascans material customization: basic layer editing (dirt/rain/snow) in material editor, then advanced Blend Material mode using Nanite Tessellation to mix up to 3 Megascans materials per mesh with per-layer wetness, displacement, and snow controls.

### Summary
Polygonflow Dash tutorial showing how to go beyond basic material application to create detailed, layered surfaces on a procedural road mesh. Covers Dash Road Tool setup (Draw Curves → road spline; UV mapping; resolution/smoothness), applying Megascans materials via Dash Content Browser, basic layer editing (snow/rain/wetness parameters), and the full Blend Material workflow: increase subdivisions → bake to static mesh → enable Nanite + Nanite Tessellation → Ctrl-drag 3 materials → Apply Blend Material → edit per-layer in tool panel. Also shows applying weather layers to Megascans prop models. Note: Dash material customization only supports Megascans and Polyhaven materials.

### Key Steps
1. **Road creation:** Dash → Create → Draw Curves (freehand on terrain); Road Tool → add curve to Curves section; set road width; Environment: select all scatter tools → Proximity Mask with road as reference; click reference tool icon to share mask settings across multiple scatter actors
2. **Material application:** search Dash Content Browser → drag Megascans material onto road; Road Tool → Geometry settings → UV Scale adjustment
3. **Basic material layers:** select asset → open material editor → enable snow/rain/dirt presets; adjust parameters per layer
4. **Blend Material workflow (advanced):**
   - Road Tool → Geometry → increase Subdivision value
   - Wireframe mode to visualize tessellation
   - Click actor-to-static-mesh icon (bakes road, loses non-destructive; backup first)
   - Dashbar → "nanite" → enable Nanite; enable Nanite Tessellation
   - Hold Ctrl → drag 3 Megascans materials from Dash asset library onto mesh → "Apply Blend Material"
   - Dashbar → "Edit Blend Material" → adjust tiling per layer; mix ratios; per-layer wetness, tessellation strength, snow amount
5. **Object material editing:** drag Megascans prop → tool panel → Edit Material → snow/wet/dirty/rain per surface

### UE Systems / Blueprints / Settings
- **Dash Road Tool**: Draw Curves → spline-based road; UV Scale, Resolution, Smoothness in Geometry settings; non-destructive until baked
- **Dash Proximity Mask with References**: share proximity/follow settings across multiple scatter tools via Reference button; update all simultaneously
- **Dash Blend Material**: up to 3 Megascans (or Polyhaven) materials blended on one mesh; requires Nanite + Nanite Tessellation; per-layer: tiling, blend ratio, wetness, displacement, snow/dirt/rain amount
- **Nanite Tessellation**: enables sub-polygon displacement from Megascans height maps; must bake road to static mesh first
- **Limitation**: Dash material editing only works with Megascans or Polyhaven materials (not custom materials)

### Difficulty
Intermediate — blend material step requires baking (irreversible without backup) and Nanite setup

### UE Version
UE5

### Tags
[dash, materials, blend-material, nanite-tessellation, road-tool, megascans, snow, wetness, environment, layered-materials, intermediate]

---

## Related Entries
- create-run-down-environments-in-minutes---dash-ue5.md (Dash environment workflow with decals and scatter)
- create-realistic-scatter-using-merge-actors-with-dash.md (Dash scatter and merge)
- creating-a-massive-procedural-game-world-in-ue5-with-dash.md (large-scale Dash world building)
