---
title: Create Realistic Scatter Using Merge Actors with Dash
source: YouTube
url: https://www.youtube.com/watch?v=P90HaXlYSNE
author: Polygonflow Dash
ingested: 2026-06-23
ue_version: "UE5"
tags: [dash, scatter, merge-actors, physics-simulation, nanite, environment, optimization, props, workflow, beginner]
extraction_status: complete
frames_dir: tutorials/frames/create-realistic-scatter-using-merge-actors-with-dash/
frame_count: 6
---

# Create Realistic Scatter Using Merge Actors with Dash

**Source:** [YouTube](https://www.youtube.com/watch?v=P90HaXlYSNE)
**Author:** Polygonflow Dash
**Duration:** 6m31s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, Josh Powers with Polygon Flow.  And in today's video, I want to highlight a new feature in Dash 1.3 called Merge Actors.  I use this along with a few other new tools in the latest release to help me create this  World War I battle scene.  So let's jump in and get right to it.

**Frame:** tutorials\frames\create-realistic-scatter-using-merge-actors-with-dash\frame_000.jpg

### Scene Overview [0:27]
**Transcript:** So here I have the base scene using some Megascans along with some custom models I made.  I also grabbed a few fantastic and free models off Sketchfab to add a lot more content to  this scene.  As always, links will be provided below for the assets I used.  The scene you'll notice is feeling a little bare.  The ground in particular is really flat and uninteresting.  It doesn't tell the story of the chaos and devastation after an intense battle between  two heavily armed forces, especially given the destruction we see on the building in  the tank.  Now I could use some Megascans or Sketchfab assets to scatter around, and I do plan to  supplement the scene with some of those.  But I want to show you how you can leverage Merge Actors in the Physics tool to create  some more custom made assets to scatter around your scene.  And to do this, I'm going to go ahead and jump into a fresh scene.

**Frame:** tutorials\frames\create-realistic-scatter-using-merge-actors-with-dash\frame_001.jpg

### Bricks [1:23]
**Transcript:** Here in this new scene, you'll see that I have a few burnt bricks placed around.  This is one of the many bricks you can find in the Megascans library, but this one I think  feels pretty good for the scene.  So I'm going to go ahead and select the bricks, and then I'm going to open the Physics  tool from the prompt bar.  For now, I'm going to hit start and the tool automatically make all the selected assets  dynamic objects and drop them down to the plane.  From here, what I like to do is duplicate these objects a few times using the duplicate  button.  After I've done this three to five times, I'll hit the select button, which selects  the duplicated objects, and then I'll hit duplicate another timer too, which gives  us a lot of duplicates to work with.  Sometimes especially when using one mesh with unique characteristics, you'll notice some  of the bricks really make it obvious or just duplicates.  And while it's better to use multiple assets for something like this to add a bit of variety,  one trick you can do is hold down control and hit the reset button up here.  This will put the duplicates back to where they originally spawned, and as such, a lot  of the assets are inside one another.  Now when I hit start, the bricks give us a bit of an explosion effect as they push away  from each other.  This is a great way to really get each brick to land a little differently, which will  help reduce that obvious repeating pattern the bricks were showing before.  And if you aren't 100% satisfied with the results, just hit reset and start again to keep  trying until you have something you like.  Okay, I'm happy with how this pile looks, but the problem is, each brick is its own actor,  and the more actors you have in your scene, the more taxing it's going to be on your performance.  So now what I can do is select the brick assets, and then go up to the prompt bar and type  merge actors.  This will take all the assets and create a single static mesh.  Now we have dozens of bricks in this pile, but it's only one static mesh actor.  Now I can just type NANI into the prompt bar, and select actor switch NANI, which will  enable NANI for this mesh, further optimizing it.  Depending on the scene you've created, you're probably going to want multiple variations  of the asset you're creating.  Just like we wanted to avoid obvious repetition in the brick pile itself, we don't want every  scattered instance to be the same pile, just at different rotations.  So creating a few variants of piles, perhaps even introducing some additional assets, will  really help add a lot of variety to the scatter.  Back in my scene, I can now drag my newly created meshes out onto my terrain, and then with  them selected, type surface scatter in the prompt bar.  And I'll go ahead and add them to the scatter set, then I just need to select my terrain,  and add that to the surface set of the scatter.  Now everything is set up just like any normal scatter, except you're able to scatter tens  of thousands of bricks and significantly fewer actors.

**Frame:** tutorials\frames\create-realistic-scatter-using-merge-actors-with-dash\frame_002.jpg

### Pivots [4:39]
**Transcript:** If you've brought in GLTF assets from Sketchfab, you might notice that some of the assets  will come in with multiple static meshes, even though they're only part of one object.  So here for instance, I have a small dirt pile that I want to use, but it came in as  six different meshes.  And you'll also notice that when I drag it in, it's way up here, very far away from the  pivot point.  So let's first address the multiple meshes.  Just like before, with my mesh selected, I'll just type merge actors, and then boom, it's  a single static mesh.  Now to address the issue of the pivot being so far away, Dash 1.3 has a new feature that  lets you adjust your pivots in the blink of an eye.  If we type pivot in the prompt bar, we'll see this pivot option, and it tells you a few  different ways that you can work with this.  Center, top, and bottom.  So in this case, we're just going to type pivot bottom, and it's going to center and  place the pivot at the bottom most spot of the meshes bounty box, which will make it so  much easier to work with when placing the asset around our scene.

**Frame:** tutorials\frames\create-realistic-scatter-using-merge-actors-with-dash\frame_003.jpg

### Summary [5:50]
**Transcript:** These new tools are such a time saver, and will help you really optimize your scene to  avoid hundreds of thousands of actors piling up in your environment.  And there are perfect complement to the already powerful and fun to use physics tool.

**Frame:** tutorials\frames\create-realistic-scatter-using-merge-actors-with-dash\frame_004.jpg

### Outro [6:05]
**Transcript:** And these tools are just a few of the great new features in this latest release of Dash,  and we're only scratching the surface of what's to come.  Be sure to join our Discord channel to post your work in the art channel, and let us  know what kind of features you'd like us to consider and feature updates for Dash.  We look forward to seeing what you create.  Thanks for watching, and we'll see you in the next one.

**Frame:** tutorials\frames\create-realistic-scatter-using-merge-actors-with-dash\frame_005.jpg


---

## Structured Notes

### Core Technique
Dash 1.3 workflow: Physics tool to scatter and randomize asset piles → Merge Actors to combine into a single static mesh → Nanite enable → Surface Scatter for efficient large-scale distribution. Pivot adjustment for Sketchfab GLTF multi-mesh imports.

### Summary
Short Polygonflow Dash tutorial (6m) showing how to create optimized, non-repetitive scatter assets for environment scenes. Uses Dash's Physics tool to drop and randomize asset piles (including a Ctrl+Reset trick to overlap duplicates before re-simulating for natural variation), then Merge Actors reduces dozens of separate brick actors to one static mesh. Nanite is toggled via Dash prompt bar. Multiple pile variants feed a Surface Scatter setup. Pivot adjustment (center/top/bottom) fixes Sketchfab GLTF assets that arrive with offset pivots or multiple sub-meshes.

### Key Steps
1. Select source assets (e.g., Megascans bricks) → Dash Prompt Bar → "Physics Tool" → Start (auto-makes objects dynamic, drops to plane)
2. Duplicate button 3-5× → select duplicated objects → duplicate again to build quantity
3. Ctrl+Reset: resets duplicates to original spawn origin (causes overlap) → Start again → physics explosion scatters them into natural varied pile
4. Repeat/reset until satisfied with pile appearance
5. Select all brick actors → Prompt Bar → "merge actors" → all selected become a single static mesh actor
6. Prompt Bar → "NANI" → "actor switch NANI" → enables Nanite on merged mesh
7. Create 2-3 variants of piles (different resets/seeds) for scatter variety
8. Drag variants onto terrain → Prompt Bar → "surface scatter" → add variants to Scatter Set, terrain to Surface Set
9. **Sketchfab GLTF fix:** select multi-mesh import → "merge actors" → single mesh; then "pivot bottom" to center pivot at bounding box bottom

### UE Systems / Blueprints / Settings
- **Dash Physics Tool**: makes actors dynamic rigid bodies; drop simulation; Ctrl+Reset overlaps duplicates for re-simulation variety
- **Dash Merge Actors**: combines selected static mesh actors into one static mesh (reduces actor count/draw calls)
- **Dash Nanite toggle**: "actor switch NANI" via prompt bar enables Nanite on merged mesh for LOD optimization
- **Dash Surface Scatter**: scatter tens of thousands of instances with far fewer actors when source is a merged mesh
- **Dash Pivot tool** (1.3): Prompt Bar → "pivot" → options center/top/bottom; "pivot bottom" = bottom of bounding box (essential for Sketchfab imports)
- Sketchfab GLTF assets often import as multiple sub-meshes with offset pivots — Merge Actors + Pivot Bottom fixes both in seconds

### Difficulty
Beginner — all operations via Dash prompt bar with no Blueprint or manual editor work

### UE Version
UE5

### Tags
[dash, scatter, merge-actors, physics-simulation, nanite, environment, optimization, props, workflow, beginner]

---

## Related Entries
- create-run-down-environments-in-minutes---dash-ue5.md (Dash environment workflow)
- creating-a-massive-procedural-game-world-in-ue5-with-dash.md (Dash large-scale scattering)
