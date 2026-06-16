---
title: How to Create a Cinematic Archviz Render with UE5 & Dash
source: YouTube
url: https://www.youtube.com/watch?v=HL8NDvv1G44
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-create-a-cinematic-archviz-render-with-ue5-dash/
frame_count: 8
---

# How to Create a Cinematic Archviz Render with UE5 & Dash

**Source:** [YouTube](https://www.youtube.com/watch?v=HL8NDvv1G44)
**Author:** Polygonflow Dash
**Duration:** 13m17s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hello, I'm Tamash from Polygonflow.  In this video I will show you how I created the scene for the 3DMOS.org renovation challenge  using Dash inside Unreal Engine 5.  I will also help you to get started with the challenge and show you how you can build  your own scene in just a few days using the free Dash Trail.  For the final result, I will render the scene using Path Tracer for a more realistic look.

**Frame:** tutorials\frames\how-to-create-a-cinematic-archviz-render-with-ue5-dash\frame_000.jpg

### The House [0:23]
**Transcript:** So let's get started.  Let's start on the 3DMOS.org website.  We can download the house model and find all the information you need for the challenge.  You just have to fill out the application from first.  I have unpacked the model and textures and now I'm here in Blender.  I already have a vision for how I want to renovate this house so I quickly put together  a mood board and frame ref.  So the idea is to extend the rustic house with the modern section surrounded by an English  Thai garden with lush vegetation.  I'm also going to heavily rebuild the side building and add the rustic stone wall around  the scene covered with climbing plants.  Let's start with the renovation.  First I will remove everything I want to need.  This process took the longest.  I modeled the side building so now it's time to export everything to Unreal Engine.  I'm exporting it as an FBX and in the geometry section I set smoothing the face.  Inside Unreal I will import the house into a new folder.  I don't need collisions in this project.  I can simply drag and drop the static meshes into the scene.  As you can see I kept original textures but I would like to replace them with better  materials.  This is...

**Frame:** tutorials\frames\how-to-create-a-cinematic-archviz-render-with-ue5-dash\frame_001.jpg

### The Environment [4:53]
**Transcript:** Next let's check out the Surface Ketter tool.  I'm going to scatter a small gravel mesh across the ground to create a gravel surface.  While holding Ctrl, I drag the mesh into the scene and click scatter on selection.  Then I adjust the scale and density.  I don't want to cover the entire surface, only the area around the terrace.  To achieve this, I will add the terrace to the proximity mask and invert the distance  value.  Next up is the Stonewall.  I will build this using mesh scattered along another curve.  For the climbing vegetation, I can download some foliage and bring them into the scene.  I hold Ctrl and choose Placing Red.  Then I can select a few and add them as scatter objects inside the Surface Ketter setup  to break up the vegetation a bit, I can use the noise mask.  And to reduce the repetition in the wall itself, I can bake the scatter so I can manually  tweak the individual wall pieces.  I also want some climbing vegetation on the building.  For this I will use the wine tool.  I can add a few wall pieces as a surface and use a simple cube mesh as the origin.  For the leaves, I can reuse some IVSs from before.  And now let's work on the background.  I'm simply goin...

**Frame:** tutorials\frames\how-to-create-a-cinematic-archviz-render-with-ue5-dash\frame_002.jpg

### Camera Composition [9:52]
**Transcript:** want even visible in the finer render.

**Frame:** tutorials\frames\how-to-create-a-cinematic-archviz-render-with-ue5-dash\frame_003.jpg

### The Interior [10:12]
**Transcript:** And for the interior decoration, you can find some amazing free assets directly inside  the content browser.  I already have some furniture pieces from the Amazon Berk library and I will use them  to furnish the side building.  Of course the materials on these assets are also very easy to customize.

**Frame:** tutorials\frames\how-to-create-a-cinematic-archviz-render-with-ue5-dash\frame_004.jpg

### Lightning & HDRI [10:52]
**Transcript:** The scene is almost finished.  All the smithing is an HDRI background.  I will drag the light studio blueprint into the scene.  If you can't find it, you can edit manually with the add button.  After that, in the outliner I can select every lighting related actor except the directional  light and delete them.  Inside the light studio I can enable use HDRI and select an HDRI file.  I downloaded from polyhaven as the HDRI cube map.  I will also uncheck use sunlight, use atmosphere and use fog if needed.  Then in skylight 1 I will change the source type to cube map and assign the same HDRI file  to the background trees.  We can also increase the cube map resolution for sharper reflections.  Finally I can tweak the directional light a bit.  Now let's see how the scene looks in past racing mode.  Looking nice.  I will finish the scene with a few extra details like small grass patches growing near the  walls, some teacals and a few decorative props.

**Frame:** tutorials\frames\how-to-create-a-cinematic-archviz-render-with-ue5-dash\frame_005.jpg

### Rendering [12:15]
**Transcript:** So I can bring the camera into level sequence and add a bit of movement.  After that I can render everything using the movie render cube.  Here are my render settings.  A little bit of color grading and vedon.

**Frame:** tutorials\frames\how-to-create-a-cinematic-archviz-render-with-ue5-dash\frame_006.jpg

### Outro [12:35]
**Transcript:** And that's it for this renovation scene.  I hope this gave you some ideas for your own challenge entry and also showed how much  faster environment creation can be with dash inside Unreal Engine 5.  I managed to build this scene in just 5 work days and most of the time went into planning  and modeling.  You still have a lot of time left to create your own entry, so good luck and have fun  building.  Thank you for watching and see you in the next one.

**Frame:** tutorials\frames\how-to-create-a-cinematic-archviz-render-with-ue5-dash\frame_007.jpg


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
