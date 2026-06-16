---
title: Unreal Engine & Dash Medieval Environment Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=_SKfQJ5pAAc
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-dash-medieval-environment-tutorial/
frame_count: 12
---

# Unreal Engine & Dash Medieval Environment Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=_SKfQJ5pAAc)
**Author:** Polygonflow Dash
**Duration:** 11m49s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hello, I'm Tamash from Polygonflow.  In this video I'm going to show you how I made this scene in Unreal Engine.  I will try to showcase the workflow I use here at Polygonflow, so this won't really  be a step-step tutorial.  This scene is an example of how I can approach environment building for the Veldraham's art  challenge by Lurter Studio.  I will be using several of their assets and speeding up my process with the dash of Art  Building plugin.  From layout to lighting, we will go through the key steps.  Stick around until the end to catch tricks that will speed up your workflow and bring your  environments to life faster.  So let's jump in.

**Frame:** tutorials\frames\unreal-engine-dash-medieval-environment-tutorial\frame_000.jpg

### Art Challenge [0:37]
**Transcript:** I'm starting here on the Lurter Studio's website.  The goal is to create a stunning environment using either Max Middle Encos concept art  or your own.  I choose the city of Nogrot as my starting point.  To access the Cosmos assets library in Unreal, I installed the Rocket plugin for UE5.  For this scene, I use two main asset packs, the medieval Russian Village pack and the  Wicking Village pack, along with a few extra assets from the Cosmos library.  It's also worth mentioning if you apply to the challenge, you get two full asset packs  completely free, ready to use in your scenes right away.  To help me build the scene more efficiently, I will also use the dash plugin, a Veldraham  setting tool for Unreal Engine.  Since I want to create this environment as quickly as possible, dash will be a huge  half through other process.  Now we are here in Unreal Engine.

**Frame:** tutorials\frames\unreal-engine-dash-medieval-environment-tutorial\frame_001.jpg

### Cosmos Rocket [1:37]
**Transcript:** I've downloaded the necessary asset packs and opened up the overview scene from the Russian  Village pack.  I've also installed the Cosmos Rocket plugin, which allows me to access Cosmos assets  directly inside the engine, including a lot of free ones.  It's super straightforward.  I just select the asset I want, choose the game engine and quality and download it.  Or just simply drag and drop the minted scene.

**Frame:** tutorials\frames\unreal-engine-dash-medieval-environment-tutorial\frame_002.jpg

### Main Structure [2:21]
**Transcript:** Let's begin with the main tower.  To make it faster, I'm using the dash grid scatter tool.  This way I don't have to place each piece manually one by one.  I set up the tool and then I can save it as a preset for later use.  I'm not focusing on the details yet.  It's enough to get the general shape and structure down at this stage.  I'm also creating this blank structure preset.  And I'm also using the same method for this improvised structure.  Again, I'm not worried about the details right now.  I want to move quickly and block out the main volumes of the scene.  If you don't have two monitors and still want to view reference images inside the engine,  you can use the dashboard feature.  You can drag images directly into it.  I'm adding my inspiration image from my desktop.  My goal isn't to recreate the image exactly.  I'm mainly following the core composition and the overall theme.  Next, I will start shaping the environment around my scene.  I've added a water plane to the scene and I also modeled a simple bridge in Blender.  After that, I started looking for a potential camera angle.  For lighting, I'm using the Ultra Dynamic Sky plugin, which lets me quickly set up the

**Frame:** tutorials\frames\unreal-engine-dash-medieval-environment-tutorial\frame_003.jpg

### Lightning [4:25]
**Transcript:** overall lighting and atmosphere.  One of the best features of Dash is that I can access my assets across all my projects.

**Frame:** tutorials\frames\unreal-engine-dash-medieval-environment-tutorial\frame_004.jpg

### Dash's Content Browser [4:54]
**Transcript:** No need to manually copy asset folders from one project to another.  All I have to do is open a project, compute and take my assets in the Dash Content Browser,  and from done on, they will be available in any other project.  We actually have a full tutorial on this.  You can find the link in the description.  So, in the Dash Content Browser, you will see your tech desits alongside Fab, Polyhaven,  and Quick Solicites.  If you want to learn more about the Content Browser itself, we've got a tutorial on that too.  Awesome link below.

**Frame:** tutorials\frames\unreal-engine-dash-medieval-environment-tutorial\frame_005.jpg

### Detailing the Scene [5:40]
**Transcript:** Once my assets are tagged, I can easily scatter them using Dash or drop them using Physics tools.  Scatter can also be controlled with splines.  I go ahead and create one using Dash.  Then, with proximity masking, I can control my scatter desits with spline.  I'm using the grid scatter to create a loading platform on the ground.  These scattered instances can be baked at any time, which lets you modify them individually if needed.  Now, I'm dragging in a few Cosmos assets into the scene.  For adding more details to the environment, the Physics tools of Dash are super helpful.  For example, I'm throwing a few assets into this bucket and duplicating them using the Physics drop.

**Frame:** tutorials\frames\unreal-engine-dash-medieval-environment-tutorial\frame_006.jpg

### Physics Tools [7:38]
**Transcript:** Another great tool is the Physics Paint, which lets me scatter planks between barrels in a very natural way.  I can also scatter foliage with Dash and then mask it as needed.

**Frame:** tutorials\frames\unreal-engine-dash-medieval-environment-tutorial\frame_007.jpg

### Foliage Scattering [8:08]
**Transcript:** Using masking tables, I can include multiple assets in the same proximity mess setup and tweak each one's masking distance individually.  To add snow on top of the assets, I'm using the Easy Snow plugin.  Now, I want to add some hanging icicles along the roof edges.  So, I will draw a curve and use some icicle assets I found in a Cosmos pack to scatter them along it.  You can add multiple curves to the same scatter and even extended curves will be followed automatically while the scatter nashes.  The main structures are done just a few more details to go.  First, I will create some hanging cables between the rooftops.

**Frame:** tutorials\frames\unreal-engine-dash-medieval-environment-tutorial\frame_008.jpg

### Cable Tool [9:47]
**Transcript:** For this, I'm using the Dash cable tool.  You can easily connect two or more assets with cables and adjust their gravity and count.  I'm also adding a few more detail assets.  These were all found in the Cosmos rocket library.  I'm placing a few fault planes using Dash.

**Frame:** tutorials\frames\unreal-engine-dash-medieval-environment-tutorial\frame_009.jpg

### Fog Cards [10:38]
**Transcript:** These are animated fog cards playing a bring atmosphere to the scene.

**Frame:** tutorials\frames\unreal-engine-dash-medieval-environment-tutorial\frame_010.jpg

### Outro [11:01]
**Transcript:** And that's the last step.  And now, here's the final render of the scene.  I hope this gave you a good overview for the Well Drums art challenge.  If you would like to learn more about Dash or see future updates and behind the scenes breakdowns, feel free to like, subscribe and check out the links in the description.  Thanks for watching and see you in the next one.  Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-dash-medieval-environment-tutorial\frame_011.jpg


---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### UE Systems / Blueprints / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### UE Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Entries
[PENDING EXTRACTION]
