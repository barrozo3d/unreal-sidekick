---
title: Create Run-down Environments in Minutes - Dash & UE5
source: YouTube
url: https://www.youtube.com/watch?v=NNBDLTPsktc
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-early
ue_version: "UE 5.x"
tags: [dash-early, environment, scatter, proximity-masking, decals, mesh-cards, post-process, color-grading, beginner]
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
**Transcript:** First, I wanted to scatter some grass in the corners of the room.  To do this with dash is quite trivial.  We find the right asset in the content browser, drag it onto the viewport, and hold control  to scatter it.  I'll adjust a few parameters on the scatter, but before I really dial those details in,  I want to make sure the grass is locked to these two corners.  I can quickly do this by first selecting the grass, then a few of the props in the corners.  Then I can click on this proximity icon right here.  With this, I can adjust the proximity distance of my grass to quickly expand the coverage  away from these assets.  Then using one of my favorite settings, I can bump up the falloff on the grass, which  gives us a really smooth transition of scale as a scatter reaches its borders.  This makes things feel so much more natural and organic.  Here's a quick tip.  If you drop in a small static mesh that fits your scene, you can then add the mesh to the  proximity mask by going into the grass scatters main property panel.  And with the mesh selected, you can just add it.  Now the grass will extend out to the mesh, and you can easily move it around and scatter  will update in real tim...

**Frame:** tutorials\frames\create-run-down-environments-in-minutes---dash-ue5\frame_001.jpg

### Scatter Leaves [2:37]
**Transcript:** I wanted to place a bunch of leaves in the scene, and while Megascans does have some leaf  cluster meshes, they don't always play well due to their high frequency.  To fix this, I'll select my floor mesh, then write, create and scatter mesh cards in  my dash prompt bar.  Then I'll select the create cards action.  This will prompt me to pick an opacity map of my leaves, and once we do that, it'll convert  that opacity map to actual mesh cards for each leaf in this case, and then scatter them  all over the ground.  As always, tweaking the results is a fun part.  We can change their density, play with the breakup parameters to have more realistic clustering  and so on.  I'll now go back to the content browser, and just start scattering more objects on the  ground to really start filling out the scene.  The key is to add enough detail that really sells the scene, but not so much that it becomes  too noisy, making it difficult for the viewer's eye to find a place to rest.  We also have this wall outside the window.  Since the scene is more focused on the interior, I didn't spend too much time out there, but  I did scatter some ivy along the wall, as well as add a few decals to further g...

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
Post-apocalyptic interior detailing pass using Dash — corner-locked grass scatter with Proximity Mask + Falloff, Megascans leaf Mesh Cards from opacity map, decal scatter, ivy wall scatter, and named color-grade LUT presets from Dash's grading library.

### Summary
6-minute tutorial by Josh Powers polishing a Last of Us–inspired interior from blockout to final render using Dash. Key techniques: corner-locked grass via Proximity Mask on prop actors with Falloff for organic border fade; Mesh Cards generated from a Megascans leaf opacity map for natural leaf clustering; scatter of more props and decals; ivy on exterior wall; Dash Camera with post-process panel (DOF, vignette, chromatic aberration, sharpness console var exposed in UI); and named LUT presets from Dash's color grading library (`type: last of us` or `cycle grading` to step through all presets).

### Key Steps
1. **Corner grass** — Ctrl+drag grass asset → Scatter; select grass + corner props → click Proximity icon; adjust Distance to expand coverage toward props; increase Falloff for smooth organic border fade
2. **Moveable proximity guide mesh** — drop small static mesh → add to grass scatter's Proximity Mask → scatter updates live as guide mesh moves
3. **Leaf Mesh Cards** — select floor mesh → type `create scatter mesh cards` in Dash prompt → Create Cards → pick Megascans leaf opacity map → Dash generates one mesh card per leaf → scatters over floor; tune density + breakup
4. **Fill scatter** — add more Megascans debris, objects from Content Browser; scatter to fill visual interest without excessive noise
5. **Ivy + decals** — scatter ivy on exterior wall; add grunge/crack decals to surfaces
6. **Camera + post-process** — type `new camera` → move to composition → click post-process icon → tune DOF, vignette, chromatic aberration, sharpness
7. **Color grade** — type `last of us color grading` to apply named preset; OR type `cycle grading` to step through all presets (Blade Runner, Children of Men, traditional, etc.)

### UE Systems / Blueprints / Settings
- **Proximity Mask → Distance** — expands scatter coverage toward masked actors (not away from them); use Invert for exclusion
- **Proximity Falloff** — smooth scale fade at scatter boundary; increases organic feel at border edges
- **Create Scatter Mesh Cards** — type `create scatter mesh cards` in Dash prompt; selects floor → picks opacity map → generates individual mesh cards from each leaf in atlas; density + breakup settings
- **Color Grading Library** — type named preset or `cycle grading` to step through all available Dash LUT presets; applied per-camera
- **Camera Sharpness** — normally console-var-only in UE5; exposed as slider in Dash camera post-process panel

### Difficulty
Beginner

### UE Version
UE 5.x (Dash early)

### Tags
`#dash-early` `#environment` `#scatter` `#proximity-masking` `#decals` `#mesh-cards` `#post-process` `#color-grading` `#beginner`

---

## Related Entries
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Proximity Mask + Falloff full reference
- [[introducing-dash-for-unreal-engine-5]] — Mesh Cards from opacity atlas (first introduction)
- [[beginner-guide-to-ue5-co-pilot-dash-camera-settings]] — Camera Tool + LUT color grading
- [[how-to-scatter-decals-in-ue5---world-building-plugin]] — Decal scatter reference
