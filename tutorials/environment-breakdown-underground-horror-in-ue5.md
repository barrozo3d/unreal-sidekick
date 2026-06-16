---
title: Environment Breakdown: Underground Horror in UE5
source: YouTube
url: https://www.youtube.com/watch?v=zxVE6uyBEHs
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/environment-breakdown-underground-horror-in-ue5/
frame_count: 9
---

# Environment Breakdown: Underground Horror in UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=zxVE6uyBEHs)
**Author:** Polygonflow Dash
**Duration:** 8m33s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Horror Hallway Scene [0:00]
**Transcript:** 😘  Hey, Josh Powers with Polygon Flow, and today we're going to break down how I created

**Frame:** tutorials\frames\environment-breakdown-underground-horror-in-ue5\frame_000.jpg

### Modular Asset Design & Layout [0:30]
**Transcript:** this environment in Unreal 5 with the help of Dash, your co-pilot to world building.  So let's dive into this one.  Because the scene is exclusively man-made, I decided to create modular assets that I can  snap together to lay out my scene.  These assets are modeled on the grid so I can use the grid snapping in the editor to  quickly assemble my environment.  There are numerous ways you could go about building a scene like this, but I feel like  the speed and flexibility of using modular assets, at least as a starting point, is a  terrific way to build out your scene.  I also created an Atlas texture using Substance Painter that it was able to not only leverage  for my wall and ceiling pieces, but also some of the secondary props in the scene.  This texture can be done manually, or by using Hot Spot Texture plugins that have become  more popular recently in games like Half Life Alex and The Last of Us.  This allows me to create endless variations of different wall and ceiling panels using  just one texture set.  Alright, with the base layout of my scene finished, I need to start blocking out my lighting.

**Frame:** tutorials\frames\environment-breakdown-underground-horror-in-ue5\frame_001.jpg

### Light Blockout [1:38]
**Transcript:** I had several references for the kind of lighting I wanted in this scene, so I'll start  by adding a wrecked light since the lighting source assets will follow this kind of lighting  very closely.  Once I'm happy with that, I'm going to use Dash's content library to drag in one of these  Megascans props.  And then I'm going to tweak the lighting position a little bit so that the light source itself  doesn't impact the prop.  Because the Megascans asset doesn't come with the fluorescent tubes we need, I'll use the  Dash Prompt Bar to create a cylinder asset, and then I'll scale it into the right size  to mimic the light tubes we want for these particular props.  Once that's feeling good, I'm going to drag on a simple material with an emissive.  Because of Lumen, this will also brighten up the interior of the prop to truly look  like the fluorescent tubes are giving off light.  We'll come back later and really finesse the bulbs, but for now they look good so we'll  just go ahead and add this ominous red light at the end of the hallway and then move  on to propping out the scene.

**Frame:** tutorials\frames\environment-breakdown-underground-horror-in-ue5\frame_002.jpg

### Dash Asset Placement [2:45]
**Transcript:** For most of the props, I'm able to place assets from the Megascans library through Dash's  content library.  This dynamic approach to placing assets makes my job a whole lot faster and if I'm being  honest more enjoyable.  Using the hotkeys when placing assets makes it a completely effortless job and my mind  remains in the focused creative zone.  I don't have to think about what access I'm on to quickly move, rotate and scale.  Instead I just imagine where I want the asset, what position it should be in, and then  I can quickly move on to the next asset.  It seems like a trivial improvement at first glance, but it's incredible what kind of  impact it's had on my experience as an environment artist, and I never want to go back to the  old way of asset placement.  I also utilize Dash's physics tool to help me scatter some of the more chaotic elements  of the scene.  Not only does this tool save me a tremendous amount of time over hand placing each asset,  but it also gives end results that are much more natural and organic looking.  Plus, let's admit it, it's really fun too.

**Frame:** tutorials\frames\environment-breakdown-underground-horror-in-ue5\frame_003.jpg

### Dash Cables & Curves [3:53]
**Transcript:** For the cable strewn about on the ground, I used Dash to quickly draw some curves at  a lower sample rate.  And then with the curve selected, I just wrote 2 pipe in the prompt bar, which will give  the selected curve thickness.  I can then play with some of the settings until I get the results I'm going for, and then  move on.  It's so fast and easy to use.  Between the Megascans and custom props I created, I was able to get the scene most of  the way there.  However, I also took advantage of a few asset packs from the Unreal Marketplace to add  a bit more terror to the scene.  These are some really great assets for your horror project, so if you want to check  them out, we'll link to everything I used from the marketplace in the description.

**Frame:** tutorials\frames\environment-breakdown-underground-horror-in-ue5\frame_004.jpg

### Decal Scattering with Dash [4:39]
**Transcript:** I wanted this scene to scream chaos, and while we've achieved a lot of that with general  prop placement, the floor itself needs some attention still, and I can quickly achieve  this by using Create and Scatter Mesh Cards in the Dash prompt bar.  This lets me choose an Atlas Opacity map from my local drive, and then it'll create  individual mesh cards for each of the elements of the Atlas texture, and then it'll scatter  them around all the assets I had selected.  From there, I can adjust their scatter properties like any other scatter instance until I'm happy  with the results.

**Frame:** tutorials\frames\environment-breakdown-underground-horror-in-ue5\frame_005.jpg

### Rubble Scattering with Dash [5:15]
**Transcript:** To add a bit more detail to the floor, I'll add some small pebbles to simulate general  debris from wear and tear, as well as little things that might come in on the bottom of  boots or equipment over the years of use.  I want to keep this effect somewhat subtle, so I'll make sure the overall scale of this  scatter is quite small, and then I'll also utilize the proximity masking feature to limit  the majority of the scatter to be along the walls and other props along the wall.  Then I'll just re-add some of them back towards the middle of the path just so that it's  not so perfectly limited to the walls.

**Frame:** tutorials\frames\environment-breakdown-underground-horror-in-ue5\frame_006.jpg

### Decal Placement [5:49]
**Transcript:** The horror nature of this scene requires some blood, which was achieved through decals.  Placing these decals with dash makes it a breeze.  I'm quickly able to fill my scene with a myriad of decals through the content library by  simply dragging them into the scene and using dash's dynamic placement tool to move, rotate,  and scale the decals in the scene to really help paint the picture of terror I'm going for.  In addition to the blood, I'm able to add other elements such as cracks and damage on  the ground, as well as some grime and grunge along the walls.  For the puddles in the middle of the hallway, I simply made a duplicate of one of the blood  decal materials and then used the material adjustment tool from the dash prompt bar to  shift the hue, saturation, and brightness, which gives us more of a puddled water look instead  of blood, which saves me the trouble of making a completely new decal.  Alright, we've now reached a polishing phase where we can spend time on the little touches

**Frame:** tutorials\frames\environment-breakdown-underground-horror-in-ue5\frame_007.jpg

### Environmental Storytelling [6:45]
**Transcript:** that'll help add drama and story to our scene.  For example, I have a lot of blood decals on this wall here, but the geometry is the  same as every other panel of this type.  So I'll switch it out with a unique instance of this wall panel that has some dented and  bent up geometry, as well as a dented up normal map too.  I can also apply this dented material to other wall panels along the corridor to help with  the visual interest and break up any repetition.  Even without geometry changes, it does a great job with the glancing light and reflections  coming from the end of the hall.  From here it's just a matter of tweaking some of the materials, adding some additional  atmospheric elements such as some Niagara effects I got from the marketplace, and adding  some various states of conditions to the lights in the scene, including some flickering lights,  some dented ones, as well as some that are fully burnt out.  You can grab these materials from a link in the description below, but in future versions  of Dash will include them natively so that you can quickly add these materials to your  scene.  And there you have it.  With the help of Dash I was able to build this scene in Unreal...

**Frame:** tutorials\frames\environment-breakdown-underground-horror-in-ue5\frame_008.jpg


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
