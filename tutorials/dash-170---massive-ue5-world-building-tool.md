---
title: DASH 1.7.0 - MASSIVE UE5 WORLD BUILDING TOOL
source: YouTube
url: https://www.youtube.com/watch?v=B6T_VQQK6OU
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/dash-170---massive-ue5-world-building-tool/
frame_count: 17
---

# DASH 1.7.0 - MASSIVE UE5 WORLD BUILDING TOOL

**Source:** [YouTube](https://www.youtube.com/watch?v=B6T_VQQK6OU)
**Author:** Polygonflow Dash
**Duration:** 5m41s | 17 section(s)

---

## Raw Data (for Claude Code extraction)


### Vines Tool [0:00]
**Transcript:** Hi there, Adnan here from Polygonflow. We've been hard at work on Dash 1.7, a major upgrade  that brings you UE 5.4 support, new tools, world building improvements and much more.  Let's look at each feature step by step. First we've got the Vines tool. You can create  Vines from scratch or in this case leverage the leaves from the Megascans library to automatically  create Vines out of them. As with all things Dash, the workflow couldn't be simpler and you  still have full control over every aspect of your Vines and leaves. Next we've revamped

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_000.jpg

### GPT4o Asset Tagging [0:37]
**Transcript:** our asset tagging to leverage GPT-40. This gives you state of the art accuracy and your  content is never used for training either. As we work towards Dash 2.0, making content  easier to find and place is a major goal for us.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_001.jpg

### Property References [0:54]
**Transcript:** Another major feature in this release is property references. In this demo, I wanted to have  one value control the width of the road, the grass scattered nearby and everything else.  Each referenced property has its own weight, giving you full control and unique offsets  at the same time. This workflow is ideal for complex scenes because it keeps everything  as simple as it can be.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_002.jpg

### IES Library Support [1:22]
**Transcript:** For those in arc fees, we've also implemented an IES library straight inside the Dash  content browser. As you can see, the workflow is as easy as it gets.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_003.jpg

### Image to Grading [1:37]
**Transcript:** Another simple yet useful feature is the new image to grading. Drag and drop an image  onto the Dash bar and we'll extract its color grading then apply it to the Dash camera  in your scene.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_004.jpg

### Fog Cards 2.0 [1:51]
**Transcript:** Next, we've revamped our fog cards to make them look better, whether in static or in motion.  As with everything in Dash, you can always just select and adjust every single parameter  from the density to the brightness to the speed and everything else.  One feature I'm particularly excited about is the new blend material. By just dragging

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_005.jpg

### Blend Material [2:07]
**Transcript:** dropping three surfaces from the content browser onto a surface in your scene, it instantly  creates a highly customizable material that blends each layer based on height map data,  noise and vertex color. We've given you a granular control over every single aspect of  each layer.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_006.jpg

### Landscape Layer Masking [2:34]
**Transcript:** Next, you've all been requesting the ability to mask your scattered object by the landscape  layer and we've given you just that in this update. Pass the name of a specific layer  to the tool surface scatter and that'll do it.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_007.jpg

### Instance Color Variation 2.0 [2:48]
**Transcript:** Another feature that we've cleaned up in 1.7 is instance color variation. As the name  says, it gives you the ability to randomize your scattered objects' properties like the  hue, saturation and brightness, which is invaluable for highly detailed yet unique word building.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_008.jpg

### Volume Scatter [3:07]
**Transcript:** Volume scatter is a small but incredibly useful tool that can be used to create flock of birds  as turrets around a planet or really anything that you want to put inside some mesh.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_009.jpg

### Batch Edit Tags [3:22]
**Transcript:** Back to tagging, you now have the ability to batch edit tags on multiple assets at once.  I personally use this to mark assets when I'm about to use them in a project and will  further refine this workflow to make it more accessible.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_010.jpg

### Curve Masking [3:37]
**Transcript:** When scattering on large surfaces, you sometimes want to keep objects strictly inside a curve.  Well, that's super easy with this update. Just pass the curve as an object mask, make  sure you have the keep inside checkbox checked and that's about it.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_011.jpg

### Border Masking [3:53]
**Transcript:** Border masking is another scattering feature I'm really excited about. You can create custom  geometry and ensure that your scattered object can be clipped off the borders effortlessly.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_012.jpg

### Mesh Borders to Curve [4:06]
**Transcript:** Making of mesh borders, you also have the ability to extract curves from mesh borders.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_013.jpg

### Tool Presets [4:14]
**Transcript:** Tool presets are another major features in dash 1.7. You could create a really cool  scatter setup for example and reuse it in as many other scattered tools or even scenes  or projects as you want.  Back to the basics, we've made scenes saving much simpler in this update. All your data

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_014.jpg

### Saving Improvements [4:34]
**Transcript:** now resides in a simple actor and the data structure is a simple dictionary that's easy  to read and modify.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_015.jpg

### Export Assets [4:47]
**Transcript:** To close this video, this small but crucial feature allows you to select any asset in your  UE content browser and export it with all its dependencies as a zip file.  And that's about it. As you can see, dash is becoming more and more what we always wanted  it to be, an ecosystem of solutions for anyone creating worlds in Unreal Engine. Whether  that translates to better scatter masking or the ability to blend materials or even just  zip assets and share them with others, we're slowly adding every piece of the puzzle  to make sure that you can create worlds that you feel proud of.  I hope you've enjoyed this video and I can't wait to tell you more about what we've been  working on on Dash 2.0. Until then, let's have fun with this update and I'll see you  around.

**Frame:** tutorials\frames\dash-170---massive-ue5-world-building-tool\frame_016.jpg


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
