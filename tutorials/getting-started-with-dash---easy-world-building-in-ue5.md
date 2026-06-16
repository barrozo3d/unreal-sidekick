---
title: GETTING STARTED WITH DASH - EASY WORLD BUILDING IN UE5
source: YouTube
url: https://www.youtube.com/watch?v=RA3yGbCvxIU
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.8
ue_version: "UE 5.x"
tags: [dash-1.8, terrain, road-tool, scatter, proximity-masking, ai-tagging, blend-material, physics-tools, world-building, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/getting-started-with-dash---easy-world-building-in-ue5/
frame_count: 19
---

# GETTING STARTED WITH DASH - EASY WORLD BUILDING IN UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=RA3yGbCvxIU)
**Author:** Polygonflow Dash
**Duration:** 23m24s | 19 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hello, I'm Tamash from Polygonflow. I'd like to introduce you to the new features and changes in Dash 1.8 through a couple of scenes. We will quickly create a procedural road through a street corner and show how to easily blend and customize 3 Megascans materials. So let's go!

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_000.jpg

### New UI [0:17]
**Transcript:** Let's get started with the new Dash UI bar. It has been completely revamped in Dash 1.8. The most important tools are now instantly accessible from the menus. This makes it easier to find and use the major tools as well as the smaller utility actions available in Dash. But if you prefer the other search method, you can still use that too.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_001.jpg

### AI Assistant [0:39]
**Transcript:** Another cool new feature of Dash 1.8 is our new AI assistant. We have integrated ChatGPT4 with our new documentation into Dash. So you can ask it questions any time. I have an idea of a scene I want to create and I've gathered some reference images for it. I'd like to make a road passing through a forest. Let's ask the AI how it would create the scene. Simply drag the image into the window and describe what you want to achieve. The more detailed our description is, the more accurate responses we will get. And here's the answer. So it suggests we first create a terrain and use the road tool to create a path on it. After that, we should scatter vegetation across the terrain. I click Create in the Dash toolbar, then select the create terrain mesh.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_002.jpg

### Terrain Tool [1:50]
**Transcript:** The new tools panel pops up. In the future, I can easily switch between my active tools by clicking here. And by the way, you can always open the tools panel by clicking the edit icon up here in Dash. I set up my desired parameters like scale and turbulence. And I'm happy with my terrain. Let's see what the AI system recommends for the next step. By clicking on the history, I can review my previous searches.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_003.jpg

### Road Tool [2:35]
**Transcript:** I should continue with my road, which requires a curve. It's located under create curve tools. Here I can set settings such as mode and spacing between the points I draw. I can easily modify my point density later by holding down Ctrl and the middle mouse button, then dragging the mouse left or right. Let's create the road. Click on create road. After selecting my curve, I click on the plus button. Here I can adjust the desired width as well as resolution and smoothness. Currently, my road doesn't perfectly align to my terrain. I can fix this in the geometry setting section. Under projection mask, I can choose where my road should be projected onto. But before selecting a different mesh, I click on this pin icon to lock the current tool so that the road tool remains open in the tools panel. Then I select my terrain and click on the plus icon. After that, I also check the full mesh option.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_004.jpg

### Image Board [4:20]
**Transcript:** I'd like to introduce Dash's new Image Board feature. I click on Board on the Dash toolbar. This brings up the board where I can drag my reference images. It's similar to PureRef, but integrated directly within the engine. The boards can be saved and will remain in the foreground throughout.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_005.jpg

### Road Markings [4:45]
**Transcript:** In order to have the road markings be easily adjustable, I will use the road tool again to create them instead of using a road texture. I can save this setup as a preset by clicking on this icon. This way, if I create a new road mesh along my curve, I can apply the saved settings to it. I select my curve again and create a new road. After that, I apply the saved preset. I open the Dash content browser and choose a Megascans material and drop it on the road. I then reduce the width. I can move the line markings to the edges of the road using the Path Width section of the road tool panel. I set the number of duplicates and set how far apart they should be. This can be saved as a preset as well.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_006.jpg

### Procedural Scattering [7:38]
**Transcript:** I have downloaded a few plants I'd like to use. I select them from my content browser, and by holding down control, I drag and drop them onto the terrain. I click on scatter here. In the tool panel, I can adjust parameters such as density or the scale of plants. The next step is to mask out the plants from the road. For this, I scroll down in the tool panel to proximity masking. I will select the road as the object, but before doing that, I click on the pen icon to keep the current surface scatter tool panel open. I select the road, and adjust the distance. I want the scatter plants to appear only near the road, not across the entire terrain. So I invert the distance parameter and increase it approximately to the range where I want the plants to spread. Then in proximity mask 2, I select the road again and remove the plants from the road itself. I can save the proximity mask value as a reference, which can be applied to multiple scattered actors, allowing me to control several scattered objects together.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_007.jpg

### Camera Tool [11:10]
**Transcript:** I simply type camera into the Dash toolbar and select the create camera option. In the tool panel, I can adjust the aspect ratio, apply color grading, and use post-process FX. Another cool feature of the camera tool is that I can either drag an image or use the Dash image port to extract the grading from an existing image onto my Dash camera. Two more things are missing from the image: the leaves alongside the road, and the fog in the background. I select some leaves models from Megascans, drag them over my curve, choose the scatter here option, and Dash automatically scatters the leaves alongside the curve. I adjust the parameters to my liking and under parallel width, I use the distance parameter to duplicate the leaves and spread them out along both sides of the road. Next, I type fog and search for the create fog card option.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_008.jpg

### Fog Card [12:40]
**Transcript:** I can freely adjust the scale, wind and other attributes. After a bit of fine tuning, the first scene is complete. As you can see, within a few minutes, we've built the foundation of the forest road and it's completely procedural. Whenever I move the curve points, the road and the forest follow seamlessly.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_009.jpg

### Place Tools [13:32]
**Transcript:** I introduce the Dash tools in the place menu and show how to quickly add a lot of detail to the scene. Let's take a look at the select tools. I will select this trashcan, and by clicking on the select nearby, Dash will automatically select the surrounding assets. The project below option solves the floating asset issue by aligning the selected assets to the ground. If you want to randomize the placement of an asset, the random swap tool can help us. From this menu, I can easily adjust the pivot point of each asset. We can also randomize the parameters of the assets, such as their scale and orientation.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_010.jpg

### Transform Tools [14:27]
**Transcript:** Now I want to quickly fill this scene with content and details. I have downloaded an asset pack from the marketplace.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_011.jpg

### AI Asset Tagging [14:34]
**Transcript:** These assets are not yet available in the Dash content browser, but I can easily fix this by using the Dash AI tagging system. I select the current project option. Here I find the location of the asset pack. I select the folder that I want to import. I can choose whether I want AI tags for the assets or not. I check the box to enable AI tagging and click on the Compute button. The Dash AI tagging system assigns tags to the assets, making it easy for me to search through them. Once the tagging process is complete, I can right click on the asset to see its properties. I can see that this asset has a lot of tags now. Dash recognizes assets based on their appearance. I can also add my own tags to the assets. Additionally, I can search for assets with a similar look and properties.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_012.jpg

### Physics Tools [15:45]
**Transcript:** I select a few bottles and drag and drop them into one of the bins. Under the previously used place menu, I select the physics drop command. The selected assets fall into the bin, then I duplicate them until they start spilling over the top. I want to quickly fill my scene with large piles of rubble and trash. The AI suggests using the physics paint tool. I can find it under the place menu. I choose some assets from the content browser and drag them into my scene by holding down control. I select physics paint. By holding down shift, ctrl, and the middle mouse button, I can adjust the size of my brush. I paint a few piles of rubble.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_013.jpg

### Decal Scatter [17:28]
**Transcript:** While holding down control, I drag decals into the scene and choose scatter here. In the tools panel, I can set how many decals I want and how densely they should be scattered. In the third part of the video, I will showcase the material blend tool of Dash. I create a terrain from the create menu with high subdivision for Nanite displacement. I bake it into a static object and enable Nanite support. I download some materials from the Megascans library.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_014.jpg

### Blend Material [18:55]
**Transcript:** I select three materials, and by holding down control, I drop them onto the terrain. I choose the apply blend material option. I click on the edit button, then select edit blend material. First, I'm going to set the global tiling. I can adjust which material I want to be in the foreground. I will create a muddy terrain with some puddles. I tweak the wetness and displacement a bit. Here, I can adjust the snow.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_015.jpg

### Snow & Rain Layer [19:34]
**Transcript:** And I can imitate rain drops on the terrain. I want the mood of an early winter morning, where the melted snow and mud have frozen. As you can see, I can make a very detailed blend. I think this ground is a perfect base for a medieval scene.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_016.jpg

### Building an Environment [20:07]
**Transcript:** I'm using a few assets from the Medieval game environment pack downloaded from the Epic Marketplace. I start with setting up the camera. Under the create menu, I select create camera, and set the aspect ratio and focal length. Next, I draw a curve and scatter Megascans gravel assets on the terrain. I use the curve in the proximity masking section to create a two-lane gravel path. I bring a wooden post into the scene and from the scatter menu, select path scatter. In the curve section, I add the path curve, select the wooden post for scatter, arrange into rows, play with density and random rotation. I scatter some foliage around the buildings, add snow on top of objects in the material tool panel, scatter Megascans trees in the background, add some cliffs and rocks. For final details, I use the physics tools from the place menu.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_017.jpg

### Outro [22:24]
**Transcript:** And there you have it. We have covered the biggest new features in Dash 1.8: the new Dash UI bar, revamped documentation, the new AI assistant, the Image Board. I demonstrated how you can easily access the frequently used world building tools such as the road tool, the physics tools, and how to use the Dash blend material tool to create more detailed environments. Thank you for watching. See you in the next one.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_018.jpg


---

## Structured Notes

### Core Technique
Dash 1.8 comprehensive workflow: revamped UI toolbar, AI assistant (ChatGPT4 with drag-image support), road tool with terrain projection + road marking presets, dual proximity masking (invert + exclude), Image Board, physics drop/paint, AI asset tagging, decal scatter, and Blend Material tool with wetness/snow/displacement layers.

### Summary
23-minute getting-started tutorial for Dash 1.8 by Tamash. Covers three scenes: (1) procedural road-through-forest — terrain, road tool with curve + projection mask + road markings as duplicate road mesh, scatter with dual proximity masks (near-road only + exclude from road surface); (2) street-corner detail pass — Select Nearby, Project Below, Random Swap, physics drop (bins) + physics paint (rubble piles), AI asset tagging, decal scatter; (3) blend material demo — three Megascans layers with global tiling, wetness, displacement, snow/rain. New 1.8 features: revamped top-menu UI bar, AI assistant (ChatGPT4 + image drag), Image Board (in-editor PureRef-style pinboard), camera image-based color grade extraction.

### Key Steps
1. **New UI bar (1.8)** — most-used tools in top menu buttons; search still available; tool panel tabs for active tools.
2. **AI assistant** — drag reference image into AI window + describe scene → get step-by-step workflow suggestion; history button for past searches.
3. **Terrain** — Create menu → Create Terrain Mesh → set scale, turbulence.
4. **Road Tool** — Create Curve Tools → draw curve (Ctrl+MMB drag = point density) → Create Road → select curve → set width, resolution, smoothness → Geometry → Projection Mask → pin icon to lock tool → select terrain → Full Mesh checkbox.
5. **Road markings (separate road mesh)** — create second road mesh on same curve → apply Megascans material → reduce width → Path Width section → set duplicates + spread → save as preset.
6. **Dual proximity mask** — scatter plants → Proximity Masking section → pen icon to lock scatter panel → select road, set distance, Invert (appear only near road) → Proximity Mask 2 → road again, remove from road surface → save mask as shared reference.
7. **Camera with image-based grade** — Create Camera → adjust aspect ratio, focal length → drag reference image into camera tool → extract color grading automatically.
8. **Fog card** — type `fog` → Create Fog Card → adjust scale, wind.
9. **Place Tools** — Select Nearby, Project Below (float fix), Random Swap, pivot adjust, randomize scale/orientation.
10. **Physics Drop** — Place menu → Physics Drop; Physics Paint — select assets + Ctrl drag → Physics Paint; brush size = Shift+Ctrl+MMB.
11. **AI asset tagging** — Content Browser → current project → select folder → enable AI tagging → Compute; search by tag, color, or visual similarity.
12. **Blend Material** — select 3 Megascans materials + Ctrl drag onto terrain → Apply Blend Material → Edit → global tiling, foreground layer, wetness, displacement, snow, rain drops layers.

### UE Systems / Blueprints / Settings
- **Dash 1.8 UI bar** — top menus replace search-first UX; tool panel with tabs; pin icon locks tool open
- **AI Assistant (1.8)** — ChatGPT4 integrated; drag image + text → workflow steps; history button
- **Image Board (1.8)** — in-editor PureRef-style reference board; saved; stays foreground
- **Road Tool** — curve-based road mesh; projection mask snaps to terrain; Full Mesh checkbox; width/resolution/smoothness; Path Width for markings offset; preset save/load
- **Proximity Masking** — distance threshold per object; Invert flag; pen/pin icon locks tool; save as shared reference (controls multiple scatters together)
- **Physics Drop** — falls assets to ground with physics; Physics Paint = brush-based; Shift+Ctrl+MMB = brush size
- **Blend Material tool** — up to 3 Megascans layers; global tiling; layer order; wetness, displacement, snow, rain per layer; requires Nanite enabled on mesh for displacement

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.8)

### Tags
`#dash-1.8` `#terrain` `#road-tool` `#scatter` `#proximity-masking` `#ai-tagging` `#blend-material` `#physics-tools` `#world-building` `#intermediate`

---

## Related Entries
- [[introducing-dash-for-unreal-engine-5]] — original intro with early surface scatter + prompt bar
- [[dash-110---procedural-scatter-presets-in-ue5]] — Dash 1.10 preset system
- [[dash-111---unreal-engine-world-building-just-got-easier]] — Dash 1.11 content browser improvements
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — dedicated scatter guide
- [[path-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — dedicated path scatter guide
