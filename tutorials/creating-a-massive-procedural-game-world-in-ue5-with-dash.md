---
title: Creating a Massive Procedural Game World in UE5 with Dash
source: YouTube
url: https://www.youtube.com/watch?v=GLOQdCQonOg
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.7
ue_version: "UE 5.x"
tags: [dash-1.7, landscape, scatter, feature-masking, proximity-masking, references, curve-masking, compound-tool, freeze, performance, intermediate]
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
**Transcript:** First, I'm starting with an empty scene.  The only things here are landscape, water plane and ultra dynamic sky.  Let's scatter a few assets using the surface scatter tool.  Here in the scatter section, I can add assets to the tool.  Of course, I could just drag assets in from the content drawer, select them and add them  to start scattering.  But there's a much better workflow.  So I go to the content browser.  Here, dash gives me quick access to multiple content libraries.  For now, I'll switch to the project library where I can access assets from my own project  and also assign search text to them after computing.  If you want a full guide on the content browser, check the video in the description.  Let's start with something simple and see how the scene performs.  Let's scatter some rocks across the landscape.  I hold control and drag them in.  Next scatter here and instantly I get rocks scattered on my large landscape.  Even at higher densities, the FPS stays relatively stable.  Now let's push it further.  I will raise the density and also increase the max count.  The scene is still holding up fairly well.  If I enable Nanite on thes...

**Frame:** tutorials\frames\creating-a-massive-procedural-game-world-in-ue5-with-dash\frame_001.jpg

### Environment Building [3:42]
**Transcript:** Now I will delete everything and show how quickly we can build a nice looking procedure  of Earth.  Let's start with the trees.  As get a few and use feature masking so they don't appear in the water, on the shore or  on mountain tops.  With the minimum and maximum height masks, I can control exactly where the scattering happens  vertically.  Using a noise mask, I can create natural looking clearings.  And with surface line in the rotation settings, I can keep the trees upright.  Let's repeat the same for bushes and grass.  I can't even link the masks together using references so that one way you can control  multiple scatters.  On the trees I set up earlier, I scroll down to the feature masking section, open the  options and convert values into references.  I can then reference these in other scatters.  Then I can fine tune each one with weight values.  For example, allowing bushes near the shore while keeping the trees farther away.  And if I add my tools to the compound tool, I can edit several scatters at once.  Next I scatter some rocks.  They overlap with the bushes and trees, but that's very proximity masking hubs.  I select the bushes, pin the tools so it doesn't switch and...

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
Large-scale landscape biome building in Dash 1.7 — Feature Masking (height + angle), Property References to share mask values across multiple scatter instances with per-reference weights, Curve Masking for biome containment, Compound Tool for multi-scatter editing, and Freeze/Unfreeze commands for editor performance during large landscape changes.

### Summary
13-minute tutorial by Tomáš testing Dash scatter performance on a large landscape and building a complete procedural world (landscape + water + UDS). First segment stress-tests scatter density + Nanite performance. Second segment builds trees/bushes/grass using Feature Masking (height min/max for no shoreline/mountain-top placement), Noise Mask for clearings, Property References to link masks across scatter tools with individual weight offsets, Compound Tool for bulk editing, and Proximity Masking between asset types. Third segment introduces Curve Masking (draw curve → set as Object Mask → check Keep Inside) as the key biome optimization: dense foliage only inside drawn curve areas with significantly better performance than full-landscape scatter.

### Key Steps
1. **Start scene** — empty level + landscape + water plane + Ultra Dynamic Sky
2. **Surface Scatter on landscape** — Ctrl+drag assets → Scatter on Selection; test with increasing density + max count; enable Nanite for performance headroom
3. **Feature Masking (trees)** — Height Min/Max = exclude shoreline and mountaintops; Noise Mask = natural clearings; Rotation → Surface Align = trees stay upright
4. **Repeat for bushes/grass** — same Feature Masking approach per asset type
5. **Property References** — on trees scatter: Feature Masking section → convert values to References; in other scatter tools: reference the same values with per-tool weight offsets (e.g. bushes allowed slightly closer to shore than trees)
6. **Compound Tool** — add multiple scatter tools → edit all simultaneously in one UI
7. **Proximity Masking (rocks vs foliage)** — select bushes → pin panel → add bushes to rocks' Proximity Mask → rocks excluded from bush areas
8. **Biome Curve Masking** — Draw Curve tool → draw curve area on landscape → set curve as Object Mask in scatter → check Keep Inside; scatter now limited to curve bounds with much better FPS than full-landscape scatter
9. **Combine masks inside biome** — add Feature + Noise masks within the curve area for organic detailing
10. **Freeze/Unfreeze** — select landscape → Dash command `freeze` → all tools pause updating → make landscape changes → `unfreeze` → tools update to new landscape state

### UE Systems / Blueprints / Settings
- **Feature Masking** — Height Min/Max (vertical clamp), Angle (slope exclusion for flat-only placement), Raycast (exclude inside mesh bounds)
- **Noise Mask** — breaks up scatter density with procedural noise; creates clearings and natural variation
- **Surface Align (Rotation)** — keeps scattered assets upright regardless of terrain slope
- **Property References** — convert any mask value to a Reference; reference it in other scatter tools; each reference has its own weight multiplier for fine tuning
- **Compound Tool** — groups multiple scatter tools into one editable unit; any changes apply to all tools in the group
- **Curve Masking (Keep Inside)** — draw curve → set as Object Mask → enable Keep Inside; scatter restricted to curve-enclosed area; dramatically better FPS vs full-landscape scatter for dense foliage biomes
- **Freeze / Unfreeze commands** — type `freeze` or `unfreeze` in Dash prompt with landscape selected; pauses/resumes all tool updates for editor performance during large edits

### Difficulty
Intermediate

### UE Version
UE 5.x (Dash 1.7)

### Tags
`#dash-1.7` `#landscape` `#scatter` `#feature-masking` `#proximity-masking` `#references` `#curve-masking` `#compound-tool` `#freeze` `#performance` `#intermediate`

---

## Related Entries
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Feature Masking + Proximity Mask full reference
- [[dash-170---massive-ue5-world-building-tool]] — 1.7 release notes (Property References, Curve Masking, Landscape Layer Masking introduced)
- [[procedural-world-building-for-ue5---pcg-alternative]] — alternative procedural landscape approach
- [[beginner-terrain-tool-tutorial-for-ue5]] — Dash terrain basics
