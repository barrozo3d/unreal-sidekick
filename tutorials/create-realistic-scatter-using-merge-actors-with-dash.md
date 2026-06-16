---
title: Create Realistic Scatter Using Merge Actors with Dash
source: YouTube
url: https://www.youtube.com/watch?v=P90HaXlYSNE
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.3
ue_version: "UE 5.x"
tags: [dash-1.3, merge-actors, physics, pivot, scatter, megascans, sketchfab, beginner]
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
**Transcript:** Here in this new scene, you'll see that I have a few burnt bricks placed around.  This is one of the many bricks you can find in the Megascans library, but this one I think  feels pretty good for the scene.  So I'm going to go ahead and select the bricks, and then I'm going to open the Physics  tool from the prompt bar.  For now, I'm going to hit start and the tool automatically make all the selected assets  dynamic objects and drop them down to the plane.  From here, what I like to do is duplicate these objects a few times using the duplicate  button.  After I've done this three to five times, I'll hit the select button, which selects  the duplicated objects, and then I'll hit duplicate another timer too, which gives  us a lot of duplicates to work with.  Sometimes especially when using one mesh with unique characteristics, you'll notice some  of the bricks really make it obvious or just duplicates.  And while it's better to use multiple assets for something like this to add a bit of variety,  one trick you can do is hold down control and hit the reset button up here.  This will put the duplicates back to where they originally spawned, and as such, a lot  of the assets are inside ...

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
Dash 1.3 Merge Actors command (consolidate multi-mesh Sketchfab GLTFs into a single static mesh) combined with Pivot Adjustment (center/top/bottom) and Physics Drop to scatter debris realistically.

### Summary
6-minute tutorial by Josh Powers demonstrating a WWI battle scene enriched with physically-dropped debris. The key new Dash 1.3 features highlighted are: Merge Actors (type `merge actors` in prompt to combine multi-mesh Sketchfab imports into one static mesh) and Pivot Adjustment (type `pivot center/top/bottom` to instantly reposition the pivot to the bounding box). These combine with the Physics Tool to allow physics-accurate placement of varied debris without stacking hundreds of actor instances.

### Key Steps
1. **Select bricks** → type `Physics` in Dash prompt → open Physics Tool → Start (selected assets become dynamic, drop to floor)
2. **Duplicate physics assets** — use Duplicate button in Physics toolbar 3-5 times; then Select button (selects newly duplicated objects) → Duplicate again to multiply
3. **Handle duplicate repetition** — Ctrl+Reset to respawn all duplicates from origin → re-drop for different positions/rotations (assets overlap at spawn and separate on drop)
4. **Merge multi-mesh Sketchfab imports** — select all meshes of a single object → type `merge actors` in Dash prompt → single static mesh result
5. **Fix distant pivot** — type `pivot bottom` in Dash prompt → pivot moves to bottom-center of bounding box; options: `pivot center`, `pivot top`, `pivot bottom`
6. **Drop fixed asset** — now correctly pivoted asset can be physics-dropped and placed precisely in scene

### UE Systems / Blueprints / Settings
- **Merge Actors command** — type `merge actors` in Dash prompt; merges all selected static meshes into one; new in Dash 1.3; solves multi-mesh GLTF imports from Sketchfab
- **Pivot Adjustment commands** — `pivot center`, `pivot top`, `pivot bottom`; repositions pivot to bounding box center/top/bottom instantly; new in Dash 1.3
- **Physics Tool** — Start = all selected assets become dynamic + drop; Reset = reset selected assets; Ctrl+Reset = reset all dynamic assets; Duplicate = duplicate selected; Select = select only the duplicated batch
- **Sketchfab GLTF import quirks** — may import as multiple static meshes; may have pivot far from geometry; both fixed with Merge Actors + Pivot commands

### Difficulty
Beginner

### UE Version
UE 5.x (Dash 1.3)

### Tags
`#dash-1.3` `#merge-actors` `#physics` `#pivot` `#scatter` `#megascans` `#sketchfab` `#beginner`

---

## Related Entries
- [[new-physics-tool-for-unreal-engine-5]] — full Physics Tool explainer (early Dash)
- [[beginner-content-library-tutorial-for-ue5]] — Content Library drag-and-drop + Ctrl+drag physics entry
- [[surface-scatter-beginner-guide-to-your-ue5-co-pilot-dash]] — Surface Scatter for dense coverage; Physics for specific placement
