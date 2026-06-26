---
title: Creating a Massive Procedural Game World in UE5 with Dash
source: YouTube
url: https://www.youtube.com/watch?v=GLOQdCQonOg
author: Polygonflow Dash
ingested: 2026-06-23
ue_version: "UE5"
tags: [dash, procedural, landscape, scatter, biomes, performance, nanite, foliage, proximity-mask, height-mask, spline, world-building, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/creating-a-massive-procedural-game-world-in-ue5-with-dash/
frame_count: 6
---

# Creating a Massive Procedural Game World in UE5 with Dash

**Source:** [YouTube](https://www.youtube.com/watch?v=GLOQdCQonOg)
**Author:** Polygonflow Dash
**Duration:** 12m45s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hello, I'm Tamash from Polygonflow.  Today I want to test how my PC performs when I push the dash scatter tool quite hard and  I also see how suitable dash is for covering very large scenes quickly.  By the end of the video, you will know everything you need to create a playable, diverse procedural  word in just minutes.  So let's get started.

**Frame:** tutorials\frames\creating-a-massive-procedural-game-world-in-ue5-with-dash\frame_000.jpg

### Stress Testing [0:20]
**Transcript:** First, I'm starting with an empty scene.  The only things here are landscape, water plane and ultra dynamic sky.  So here I can open the dash bar.  To start, let's scatter a few assets using the surface scatter tool.  Here in the scatter section, I can add assets to the tool.  Of course, I could just drag assets in from the content drawer, select them and add them  to start scattering.  But there's a much better workflow.  So I go to the content browser.  Here, dash gives me quick access to multiple content libraries.  For now, I'll switch to the project library where I can access assets from my own project  and also assign search text to them after computing.  If you want a full guide on the content browser, check the video in the description.  Let's start with something simple and see how the scene performs.  Let's scatter some rocks across the landscape.  I hold control and drag them in.  Next scatter here, and instantly I get rocks scattered on my large landscape.  Even at higher densities, the FPS stays relatively stable.  Now let's push it further.  I erase the density and also increase the max count.  The scene is still holding up fairly well.  If I enable Nanite on these rocks by selecting them and then running the Nanite command in  the Dashbar, the performance improves even more.  Nanite is great at handling large numbers of high polystatic measures, and rocks are the  perfect use case for it.  So rocks are clearly another big problem.  But now let's move on to something heavier.  I will scatter a few bushes the same way.  Right away you can see the bigger performance hit.  The FPS drops more compared to rocks.  The main reason is foliage complexity.  Bushes usually have lots of leaf cards with masked materials that creates overdraw, meaning  many pixels get rendered multiple times.  That's much more expensive for the GPU.  If I enable Nanite on the bushes, we do gain some performance back, but foliage is still  generally heavier than solid measures.  Nanite helps, but it doesn't completely remove the cost of transparency and overdraw.  And now let's push it even further.  I will add more Nanite rocks again and mix them with foliage, grass, bushes and trees  together.  Even with a large covered area, the scenes tastes surprisingly stable.  And remember, dash is scattering instances which is highly optimized in Unreal.  Scenes built with dash are fully compatible with standard Unreal workflows.  When someone without dash can open this project, because dash is just 3 mining native Unreal  tools not replacing them.

**Frame:** tutorials\frames\creating-a-massive-procedural-game-world-in-ue5-with-dash\frame_001.jpg

### Environment Building [3:42]
**Transcript:** Now I will delete everything and show how quickly we can build a nice looking procedure  or a word.  Let's start with the trees.  I scatter a few and use feature masking so they don't appear in the water, on the shore,  or on mountain tops.  With the minimum and maximum height masks, I can control exactly where the scattering happens  vertically.  Using a noise mask, I can create natural looking clearings.  And with surface line in the rotation settings, I can keep the trees upright.  Let's repeat the same for bushes and grass.  I can't even link the masks together using references so that one way you can control  multiple scatters.  On the trees, I set up earlier, I scroll down to the feature masking section, open the  options and convert values into references.  I can then reference these in other scatters.  Then I can fine tune each one with weight values, for example allowing bushes near the shore,  by keeping the trees farther away.  And if I add my tools to the compound tool, I can edit several scatters at once.  I scatter some rocks.  They overlap with the bushes and trees, but that's very proximity masking hubs.  I select the bushes, pin the tools so it doesn't switch, and choose the scatter rocks  as a proximity mask.  By adjusting the distance, I clear the vegetation around rocks.  I can save this as a reference and reuse it for trees too.  Now let's divide the word into biomes.  First I create a small path.  Using the draw curve tool in the create menu, I draw a curve across the landscape.  This curve can act as a proximity mask.  Our main proximity object slot is already occupied, but luckily in the proximity table section,  you can add as many as it says we want.  Then I drag wooden fences onto the curve and scatter them along the spline.  Using parallel width, I double it and form both sides of the road.  And with the projection set to the landscape, the fence follows the terrain.  We can even use the fence itself as a proximity mask, for example, to make certain flowers  grow only near it.

**Frame:** tutorials\frames\creating-a-massive-procedural-game-world-in-ue5-with-dash\frame_002.jpg

### Biome Optimization [9:38]
**Transcript:** Right now we can see from the FPS counter that we are using a lot of resources.  The main reason for that is that I have scattered a lot of assets over a full landscape,  but in many games and art environments, it makes sense to only have this much detail  in smaller sections or biomes.  And for that I got a really good trick for you.  If you use the draw curve tool again, to draw one or several areas on your landscape,  you can then set these to the object mask of your surface caters.  And it will keep inside and optimize for curves.  This will make sure your scatters only remain inside these curve areas and with really  good performance.  And another bonus of using this mask compared to other masks is that you will be able to  have really thick density, perfect for grass or foliage.  And you can of course also combine this with other masks within your curve area to get  the details just right.

**Frame:** tutorials\frames\creating-a-massive-procedural-game-world-in-ue5-with-dash\frame_003.jpg

### Freezing Tools [11:00]
**Transcript:** If you need to move these areas or make other large changes to the landscape, the editor's  performance can take a hit when you have this many procedural scatters.  If this is the case, you can select your landscape and run the freeze command in dash.  This will freeze all the tools connected to your landscape so you can make your changes  without the dash tools updating.  Then when you are done, select your landscape again, run the unfreeze command and you will  see the dash tools update to your changes.

**Frame:** tutorials\frames\creating-a-massive-procedural-game-world-in-ue5-with-dash\frame_004.jpg

### Outro [11:43]
**Transcript:** So now you have seen some of the limits and strengths of dash.  My PC is pretty beefy, but you only need a decent PC to use dash on large landscapes.  But keep in mind that the performance depends a lot on the landscape size and your density  values.  If you mainly use dash to create biomes or detailing parts of your environment, most  PCs that run UE5 will work just fine with dash and you will be able to capture the main  value and benefit of dash procedural tools.  Dash makes your building faster, more visual and more flexible, perfect for prototyping and  even production level scenes.  Make sure to give the free trial a spin if you are interested.  Thank you for watching and see you in the next one.

**Frame:** tutorials\frames\creating-a-massive-procedural-game-world-in-ue5-with-dash\frame_005.jpg


---

## Structured Notes

### Core Technique
Large-scale procedural world building with Dash: Surface Scatter + Nanite for performance, Feature Masking (height/noise/surface align) for biome control, shared References across multiple scatters, Proximity Tables for inter-scatter clearance, Curve Object Mask for biome zones, and Freeze/Unfreeze for safe large-scale edits.

### Summary
Polygonflow's Tamash stress-tests Dash on a large UE5 landscape and walks through building a diverse procedural world from scratch. Key performance insight: rocks (solid mesh + Nanite = cheap), bushes/foliage (transparent leaf cards = overdraw even with Nanite = expensive). World building technique: Feature Masking (height range, noise clearings, surface align), Reference system to link masks across scatter tools, Compound Tool for editing all at once, Proximity Table for inter-scatter spacing, Draw Curve as both road/path AND biome zone object mask, and spline-scatter for fences. Biome optimization tip: use Draw Curve enclosed area as Object Mask for very high-density grass scatter with good performance. Freeze command disconnects all Dash tools from landscape for safe edits.

### Key Steps
1. **Quick scatter test:** hold Ctrl + drag asset from Content Browser (or Dash Content Library) onto landscape → instant surface scatter; enable Nanite via Dashbar for performance
2. **Performance hierarchy:** solid meshes (rocks) = cheapest; foliage with transparent cards (bushes, grass) = most expensive due to overdraw; Nanite helps solid meshes most
3. **Feature Masking (trees):**
   - Height Mask: min/max height → keeps trees off mountain tops and below shoreline
   - Noise Mask: random clearings (natural look)
   - Rotation → Surface Align: keeps trees vertical on sloped terrain
4. **Shared mask References:**
   - Trees scatter → Feature Masking section → convert mask values to References
   - Other scatter tools (bushes, grass) → reference the same objects
   - Individual Weight values per scatter (e.g., bushes weight=1 near shore, trees weight=0)
5. **Compound Tool:** add scatter tools to Compound → edit all selected scatters simultaneously
6. **Proximity Table:** select one scatter (bushes) → Pin tool → choose rocks scatter as proximity mask → adjust distance to clear vegetation around rocks → save as reference, reuse for trees
7. **Road/path with fence:**
   - Draw Curve tool → Create menu → draw path across landscape
   - Proximity Table: add curve as additional proximity mask (main slot already in use)
   - Drag fence assets onto curve → spline scatter along path; Parallel Width to duplicate both sides; Projection=Landscape for terrain following
   - Use fence scatter itself as proximity mask for flowers nearby
8. **Biome zones (optimization):**
   - Draw Curve tool → draw enclosed area polygon on landscape
   - Surface Scatter → Object Mask → assign the drawn curve
   - Scatter is confined to that area only → very high density grass/foliage possible with good performance
   - Combine with other masks (height/noise) inside biome area
9. **Freeze/Unfreeze:** select landscape → Dashbar "freeze" → all connected Dash tools stop updating (safe for large landscpe edits); "unfreeze" to recompute

### UE Systems / Blueprints / Settings
- **Dash Surface Scatter**: hold Ctrl + drag = instant scatter; density, max count controls; uses UE instanced static meshes (native, no Dash dependency at runtime)
- **Feature Masking**: Height Mask (vertical range), Noise Mask (organic clearings), Surface Align (upright on slopes)
- **Reference System**: convert scatter mask values to shared References; Weight multiplier per scatter that shares the reference
- **Proximity Table**: multiple proximity objects (beyond main proximity slot); inter-scatter clearance zones
- **Compound Tool**: group multiple scatter tools for simultaneous editing
- **Draw Curve as Object Mask**: enclosed curve area = high-performance biome zone; optimal for dense foliage/grass
- **Spline Scatter**: drag assets onto curve → scatter along spline path; Parallel Width for double-sided; Projection type
- **Freeze/Unfreeze**: disconnects Dash from landscape for safe edits; recomputes on unfreeze
- **Nanite performance notes**: solid opaque meshes benefit greatly; transparent/masked foliage still causes overdraw regardless of Nanite

### Difficulty
Intermediate — many systems but each one is prompt-bar driven

### UE Version
UE5

### Tags
[dash, procedural, landscape, scatter, biomes, performance, nanite, foliage, proximity-mask, height-mask, spline, world-building, intermediate]

---

## Related Entries
- create-realistic-scatter-using-merge-actors-with-dash.md (Dash scatter + merge actors)
- create-run-down-environments-in-minutes---dash-ue5.md (Dash interior environment)
- creating-a-blend-material-in-unreal-engine-5-just-got-easier.md (Dash materials workflow)
