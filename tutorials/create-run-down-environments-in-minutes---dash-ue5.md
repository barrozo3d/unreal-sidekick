---
title: Create Run-down Environments in Minutes - Dash & UE5
source: YouTube
url: https://www.youtube.com/watch?v=NNBDLTPsktc
author: Polygonflow Dash
ingested: 2026-06-23
ue_version: "UE5"
tags: [dash, scatter, environment, post-process, color-grading, decals, mesh-cards, proximity-mask, interior-design, foliage, beginner]
extraction_status: complete
frames_dir: tutorials/frames/create-run-down-environments-in-minutes---dash-ue5/
frame_count: 5
---

# Create Run-down Environments in Minutes - Dash & UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=NNBDLTPsktc)
**Author:** Polygonflow Dash
**Duration:** 6m12s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey there, Josh Powers from Polygon Flow.  Not long ago, I walked you through an environment inspired by the groundbreaking game last of  us.  So today I thought I'd give you another angle through an interior scene inspired by  the same franchise.  This tutorial will go over how an environment can go from a rough out state to highly polished  with dash, the world building tool for Unreal Engine.  And if you don't already have dash, you can go to polygonflow.io and download it using  the full feature free trial.  With that said, let's jump into it.  Alright, so what I have here is the foundation of my scene.  I've created the interior geometry using Moto, but this can be done in the 3D application  of your choice.  As you can notice, the base scene is quite simple.  The standard floor, walls, and ceiling.  And then we have a few props from Megascans, as well as a few custom made assets.  I've also grabbed this suitcase model from Sketchfab to follow more closely with the  concept.  As always, you can find a link to any Sketchfab asset in the description below.  So with that out of the way, let's get to detailing with dash.

**Frame:** tutorials\frames\create-run-down-environments-in-minutes---dash-ue5\frame_000.jpg

### Scatter Grass [1:18]
**Transcript:** First, I wanted to scatter some grass in the corners of the room.  To do this with dash is quite trivial.  We find the right asset in the content browser, drag it onto the viewport, and hold control  to scatter it.  I'll adjust a few parameters on the scatter, but before I really dial those details in,  I want to make sure the grass is locked to these two corners.  I can quickly do this by first selecting the grass, then a few of the props in the corners.  Then I can click on this proximity icon right here.  With this, I can adjust the proximity distance of my grass to quickly expand the coverage  away from these assets.  Then using one of my favorite settings, I can bump up the falloff on the grass, which  gives us a really smooth transition of scale as a scatter reaches its borders.  This makes things feel so much more natural and organic.  Here's a quick tip.  If you drop in a small static mesh that fits your scene, you can then add the mesh to the  proximity mask by going into the grass scatters main property panel.  And with the mesh selected, you can just add it.  Now the grass will extend out to the mesh, and you can easily move it around and scatter  will update in real time.  This will help you really fine tune the look of your proximity masking in no time.

**Frame:** tutorials\frames\create-run-down-environments-in-minutes---dash-ue5\frame_001.jpg

### Scatter Leaves [2:37]
**Transcript:** I wanted to place a bunch of leaves in the scene, and while Megascans does have some leaf  cluster meshes, they don't always play well due to their high frequency.  To fix this, I'll select my floor mesh, then write, create and scatter mesh cards in  my dash prompt bar.  Then I'll select the create cards action.  This will prompt me to pick an opacity map of my leaves, and once we do that, it'll convert  that opacity map to actual mesh cards for each leaf in this case, and then scatter them  all over the ground.  As always, tweaking the results is a fun part.  We can change their density, play with the breakup parameters to have more realistic clustering  and so on.  I'll now go back to the content browser, and just start scattering more objects on the  ground to really start filling out the scene.  The key is to add enough detail that really sells the scene, but not so much that it becomes  too noisy, making it difficult for the viewer's eye to find a place to rest.  We also have this wall outside the window.  Since the scene is more focused on the interior, I didn't spend too much time out there, but  I did scatter some ivy along the wall, as well as add a few decals to further give the  appearance that this area has been decaying over years of neglect.  Back in the interior, the next step is to really leverage the decals to break up tiling  elements of our textures, as well as add more detail to the scene.  This is always such a fun part, as you can make any seemingly generic surface truly  stand out, and thanks to dashes and to-it-of-you-eye, the material floating bars allow us to  edit the decals really quickly in order to make them blend nicely with the background  they're sitting on.

**Frame:** tutorials\frames\create-run-down-environments-in-minutes---dash-ue5\frame_002.jpg

### Post Processing [4:34]
**Transcript:** Alright, I'm fairly happy with the results here, so the next step is to type new camera  to create a new camera in our scene.  I'll move it back to the right frame, and then click on this post-process icon.  Here I can tweak the depth of field, vignetting, chromatic aberration, and some other properties.  We've also got this sharpness property, which is only accessible through command lines  in GUI-5, but adds a nice crispness to our shot right off the bat.  And then finally, I'll use dashes color grading library to find the right grading for my  scene.  I can either type the last of us color grading to just apply the grading of the game,  or I can type cycle grading to go through all the available options ranging from blade  runner to children of men, as well as some more traditional grading styles.  In this case, I'll stick with last of us.

**Frame:** tutorials\frames\create-run-down-environments-in-minutes---dash-ue5\frame_003.jpg

### Outro [5:31]
**Transcript:** And this is what the end result looks like.  And remember, this scene was quite basic a few moments ago.  But after very little time with dashes incredibly powerful tools, we were able to create something  that transported you to a post-apocalyptic world.  I hope you've enjoyed the video, and please let us know what you'd like to see next.  Don't forget to download dash and give this workflow a shot.  On our Discord, we've got an active art channel where people share their work and learn  from each other, and we really recommend anyone passionate about world building to join  us there as well.  Thank you so much for watching, and I'll see you next time.

**Frame:** tutorials\frames\create-run-down-environments-in-minutes---dash-ue5\frame_004.jpg


---

## Structured Notes

### Core Technique
Dash-driven interior environment dressing workflow: proximity-masked scatter for organic grass/leaf placement, mesh card generation from opacity maps for Megascans leaf assets, decal layering for texture breakup, and Dash color grading library for cinematic look.

### Summary
Josh Powers (Polygonflow) builds a Last of Us-inspired post-apocalyptic interior from a rough blockout using Dash tools in ~6 minutes. Key techniques: hold-Ctrl scatter for quick placement, Proximity Mask to confine scatter to corners (with falloff for natural border fade), Mesh Cards tool that converts an opacity map into actual scattered 3D mesh cards (solving Megascans leaf high-frequency issues), ivy + decals on exterior, and Dash's post-process panel and color grading library (type LUT name or "cycle grading") for rapid look dev.

### Key Steps
1. **Grass scatter:** find asset in Content Browser → drag into viewport → hold Ctrl to scatter; adjust density, falloff (smooth border scale transition)
2. **Proximity Mask:** select grass scatter + nearby props → click Proximity icon in Dash; adjust Proximity Distance to expand coverage around assets; add a small positioned mesh to property panel proximity mask for real-time fine-tuning
3. **Leaf mesh cards:** select floor mesh → Dash Prompt Bar → "create and scatter mesh cards" → Create Cards action → pick leaf opacity map → Dash generates individual 3D mesh cards for each leaf shape → scatter on floor; tweak density + breakup parameters
4. **General scatter:** drag additional Megascans/Sketchfab assets onto surfaces; balance detail density so viewer's eye finds rest points
5. **Exterior:** scatter ivy on walls; apply decals for decay/weathering (Dash material floating bar for inline edits)
6. **Decals for interiors:** use decals to break tiling textures and add surface detail; Dash floating bar enables fast material edits without opening editor
7. **Camera + Post-Process:** Prompt Bar → "new camera" → reframe; click Post-Process icon → adjust DOF, Vignetting, Chromatic Aberration, Sharpness (note: Sharpness is otherwise CLI-only in UE5)
8. **Color grading:** Prompt Bar → type specific LUT name (e.g., "last of us color grading") to apply preset OR type "cycle grading" to cycle all available grades (Blade Runner, Children of Men, etc.)

### UE Systems / Blueprints / Settings
- **Dash Scatter (hold Ctrl)**: quick scatter of selected content browser asset onto viewport surface
- **Dash Proximity Mask**: constrains scatter to within a set distance of target objects; Falloff=smooth scale transition at scatter border; add mesh as dynamic proximity anchor via property panel
- **Dash Mesh Cards from Opacity Map**: converts 2D leaf opacity map into individual 3D mesh cards scattered on a surface; fixes tiling/normals issues with flat Megascans leaf clusters
- **Dash Post-Process Panel**: DOF, Vignetting, Chromatic Aberration, Sharpness (last one only accessible via Dash or console command in standard UE5)
- **Dash Color Grading Library**: type LUT name or "cycle grading" in prompt bar; includes cinematic and game reference grades

### Difficulty
Beginner — fully Dash prompt-bar driven; no Blueprint or material editor work

### UE Version
UE5

### Tags
[dash, scatter, environment, post-process, color-grading, decals, mesh-cards, proximity-mask, interior-design, foliage, beginner]

---

## Related Entries
- create-realistic-scatter-using-merge-actors-with-dash.md (Dash scatter + Merge Actors workflow)
- creating-a-massive-procedural-game-world-in-ue5-with-dash.md (Dash large-scale world building)
