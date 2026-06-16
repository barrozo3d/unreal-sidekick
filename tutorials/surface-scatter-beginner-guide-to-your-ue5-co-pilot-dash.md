---
title: Surface Scatter: Beginner Guide to Your UE5 Co-Pilot, DASH
source: YouTube
url: https://www.youtube.com/watch?v=D4IPvlypNkg
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash/
frame_count: 7
---

# Surface Scatter: Beginner Guide to Your UE5 Co-Pilot, DASH

**Source:** [YouTube](https://www.youtube.com/watch?v=D4IPvlypNkg)
**Author:** Polygonflow Dash
**Duration:** 8m55s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro & Surface Scatter Basics [0:00]
**Transcript:** Greetings, I'm Jonathan, Polygon Flows Community Director for Dash, our next Gen Unreal Engine  plugin that makes creating environments like these super easy.  In this video I'll be covering one of our most powerful tools, Surface Scatter, which  has been significantly improved in Dash 1.4.  Let's start by opening Dash, then type Scatter to bring up the Surface Scatter tool.  It's a very complex tool, so expanding the tool window is a good idea to work with it.  There's multiple ways of initiating a Scatter command, either by selecting existing meshes  or by using the Dash content browser and holding Control as you drag the asset into the  environment.  From there you can adjust the number of object instances using Density, and adjust the  maximum and minimum scale values too.  Plus it's possible to sort scaling by a variety of factors to customize your scattered assets.  I'll cover fall off soon, but it's got a dependency that will have to enable later  in the video before its effects will be visible, so I'll come back to this one.  Noise scale can be used to create subtle variation in the scattered assets that prevents  uniformity.  It's perfect for grass, so we'll go ahead and l...

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_000.jpg

### Feature Masking [1:39]
**Transcript:** Feature masking has terrain masking options.  Let's start with angle mask, which constrains the scattered assets up to a specific angle  on the terrain.  Anything higher than this value will not render.  Some height masking uses the relative Z data of the mesh to determine instance placement  while maximum height does the opposite.  These values are determined by the height of the mesh being used to mask.  You can use max and min height masking together, too, to create different effects.  Add mask infills the scattered mesh regardless of existing scatter settings, while remove  mask does the exact opposite to thin out the scatter no matter what the settings are.  For this next part, I'm going to use Unreal to create a simple box object which I'll  use to demonstrate raycast mesh masking.  This was a feature request from the community for scenes like a post-apocalyptic environment,  where you'd find broken down automobiles that would have grass growing directly underneath  them, or perhaps having large rocks with broken stones and pebbles collecting in the shadows  underneath.  It works with any mesh you can throw at it, and it's quite versatile and updates quickly,

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_001.jpg

### Rotation Properties & Scale Properties [2:51]
**Transcript:** too.  Uniform angle rotates all scatter meshes in the same direction, but you'll have to uncheck  randomize angles for it to function.  XY and Z rotation jitter will create randomized rotation of each asset in the scatter field giving  you ultimate control over how each asset will look.  Enable use custom scale to get fine precision over the scale of each asset that gets placed  in the environment, not only the Z scale but the X and Y scale, too.  This can allow you to create much more realistic scattering that takes into account the variation  inherent to natural objects like plants.  In some situations, it might make more sense to use standard minimum, maximum scaling,  but I find custom scale provides a very realistic look in many use cases.

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_002.jpg

### Proximity & Object Masking [3:41]
**Transcript:** Proximity is a tool that allows you to set what scatters based on physical proximity  to an object in the environment.  It can work with any mesh, including a basic Unreal sphere like this.  Proximity distance determines how far the object's influence extends beyond it to prevent  or enable scattering.  Invert proximity is the opposite.  Scatter will only spawn based on the proximity to the object being used.  Scatter determines how closely the scattered meshes adhere to the object used as a proximity  detector.  You can scatter assets using a curve, too.  Type draw into dash and then select draw curve, then draw out your preferred shape.  In this case, a spiral works well to demonstrate how the curve tool will play off the proximity  tool.  You can adjust the curve sampling to fine tune how well the curve blanks out meshes that  are surrounding it.  Object masking is a more precise version of proximity masking.  In this case, I'll use a Megascans asset to mask out the grass.  Because it's so precise, object masking only works if the mesh is physically near the  mesh that scatter assets are being placed upon.  Like proximity masking, you can invert this as well.  Select keep inside...

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_003.jpg

### Vertex Color Masking [5:19]
**Transcript:** For vertex color masking, I've applied a basic red vertex color material to show dash  applying these colors in real time.  I'll set some basic red colors on the environment since this is not a tutorial on vertex coloring  itself.  With the vertex colors applied, I've typed show all tools to bring up the active dash  tool menu and re-select its surface scatter, then apply the original material from the  dash content browser, which is on my third monitor.  After that, I've enabled the red channel and vertex color masking, making the scatter  meshes adhere to the existing vertex colors.  Vertex coloring threshold determines how strong the vertex color masking is, which is useful  for fine tuning the color mask that you've created.  There's different blending modes that you can work with which will help further dial  in the mask that you want for your environment.  You can even adjust the vertex colors using dash and then make any adjustment in surface  scatter to have it automatically update.  The workflow is non-destructive and lets you iterate on any infinite amount of vertex  color masks that you'd like to use in the engine.

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_004.jpg

### Texture Masking & Falloff [6:19]
**Transcript:** Texture masking allows you to load any texture from the Unreal Engine content browser as a  mask.  You've got several options here including color threshold, which controls the intensity  of the texture map.  To texture tiling and texture inversion too, a simple caution stripe texture can be used  to create rows of grass, so imagine what else you can do using texture masking.  Border distance, spread, and scale are all key factors to helping break up the edges of  your scatter fields.  Adjust each of these settings and you'll create natural break up along the border of  the scatter mask.  This toolset creates a broken up edge along the mask, which will help vary the scatter effect  in a more natural way that looks much less programmatic.  Now let's cover fall off that tool that I mentioned in the beginning of the video.  We're going to need some masking to show it off so I've adjusted the break up of the  scatter to demonstrate.  Fall off creates a transition and scale from the tip of the mask to the center of it, allowing  for a more natural appearance to the scattered assets.  It works even better with individual meshes instead of clumps of assets, so the scaling  is applied per ...

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_005.jpg

### Surface Scatter Applied [7:55]
**Transcript:** Here's one of the scenes in the beginning of the video.  This took me two hours to make.  Most of that was handplacing the assets that you see here, there are all that remains  after hiding the surface scatter instances.  Pretty crazy huh?  What are the ways that I like to work is using cubes with the transparent material as a  bounding box for scattering using object masking.  This allows me to specify where exactly I want the scattered assets to appear and let's  me drag the cube around to hand place them in real time.  This is a technique that I used extensively with this scene, including with the trees  in the background.  It gave me the freedom to specify exactly where I wanted randomize scattered trees to appear  without having to worry about them being placed too far forward.  Thanks for watching and let us know what you think in the comments.  See you guys next time.

**Frame:** tutorials\frames\surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash\frame_006.jpg


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
