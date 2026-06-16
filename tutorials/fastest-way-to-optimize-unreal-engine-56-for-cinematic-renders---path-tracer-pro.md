---
title: FASTEST Way to Optimize Unreal Engine 5.6 for Cinematic Renders - Path Tracer Pro
source: YouTube
url: https://www.youtube.com/watch?v=BCWThDhzImI
author: Boundless Entertainment
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro/
frame_count: 11
---

# FASTEST Way to Optimize Unreal Engine 5.6 for Cinematic Renders - Path Tracer Pro

**Source:** [YouTube](https://www.youtube.com/watch?v=BCWThDhzImI)
**Author:** Boundless Entertainment
**Duration:** 10m39s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


### <Untitled Chapter 1> [0:00]
**Transcript:** What's going on guys, Sam here for Boundless Entertainment and I have a couple of exciting  announcements for you guys today.  First, we've just launched the new Unreal Engine for Filmmakers course.  This course is brand new and fully updated in Unreal Engine 5.2 with over 25 hours of  content.  The course is designed to take you from beginner to pro in just 10 days using industry  standard techniques, so you're ready to work in any professional setting.  It covers everything from planning and blocking out your scene to building complex scenes  in Unreal Engine, advanced lighting, character animation, creating dynamic fluid and gas  simulations, compositing live action footage with your CGI scene inside of Unreal Engine,  and rendering your scene at maximum quality for cinematic results.  We already have over 6,000 students enrolled on the site, including artists from industrial

**Frame:** tutorials\frames\fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro\frame_000.jpg

### ILM, LUCASFILM, BLIZZARD [0:50]
**Transcript:** light magic, Lucasfilm, and also Blizzard Entertainment who is using this exact course to train  artists in creating cinematics in Unreal Engine.  The other exciting announcement and main topic of this video is the release of our first plugin,  Path Tracer Pro.  Path Tracer Pro is an absolute must-have plugin for Unreal Engine 5.2.  It allows you to optimize Nanite meshes for use with the Path Tracer or Ray Tracer shadows

**Frame:** tutorials\frames\fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro\frame_001.jpg

### OPTIMIZE NANITE MESHES FOR USE WITH PATH TRACER OR RAY TRACED SHADOWS [1:11]
**Transcript:** in any Unreal Engine scene with just two clicks, saving you from hours of tedious  work modifying individual meshes manually.  Now if you don't really know what I'm talking about here, I'm going to get into that in a  minute when we jump into Unreal Engine, but first it's important to understand why you  should be using Unreal Engine's Path Tracer and Ray Tracer shadows in the first place.

**Frame:** tutorials\frames\fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro\frame_002.jpg

### WHY SHOULD I USE THE PATH TRACER & RAY TRACED SHADOWS? [1:31]
**Transcript:** The Path Tracer is Unreal Engine's physically accurate lighting model, which brute force

**Frame:** tutorials\frames\fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro\frame_003.jpg

### PATH TRACER - UE'S PHYSICALLY ACCURATE LIGHTING MODEL [1:37]
**Transcript:** calculates the balanced and indirect lighting in your scene, providing the most realistic  and accurate lighting results possible.  As the Path Tracer spares little expense in achieving the highest fidelity image, it's  what we call an offline renderer, meaning it can't render images in real time like

**Frame:** tutorials\frames\fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro\frame_004.jpg

### OFFLINE RENDERER [1:55]
**Transcript:** Lumen does.  This makes it pretty much useless for interactive purposes like gaming or VR, but that doesn't  matter for creating films, visual effects, game cinematics, archviz, or any other linear  content.  And it allows us to take advantage of the Path Tracer to achieve a higher quality result  than what's possible with Lumen.  Ray Tracer shadows, on the other hand, produce far more realistic shadows and lighting in

**Frame:** tutorials\frames\fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro\frame_005.jpg

### NON RAY TRACED SHADOWS [2:21]
**Transcript:** real time scenes, and they're the best option for rendering shadows in the lit mode, which  is to say with Lumen.  So neither of these options work out of the box with Nanite meshes and require a tedious

**Frame:** tutorials\frames\fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro\frame_006.jpg

### DEFAULT RAY TRACED SHADOWS [2:30]
**Transcript:** process of modifying each individual Nanite mesh in order to be compatible with Ray Tracer  shadows and Path Tracing mode.  The Path Tracer Pro plugin streamlines this process for you, allowing you to optimize  the Nanite meshes in your scene for use with the Path Tracer and Ray Tracer shadows with  just two clicks, allowing you to achieve the most realistic lighting possible with ease  and saving you hours of time in the process.  So let's jump into Unreal Engine and get into a bit more detail about how and why this  plugin works.  So to really explain what this plugin does, let me show you the original process that  we had to do in order to optimize our scene for Path Tracing.  So I'll show you what happens if I switch into Path Tracing mode here.  You can see that suddenly we have a huge reduction in the detail quality of these meshes.  So actually if I go over to this mesh, for example, it's really obvious.  So if I go into lit mode, you can see we have a ton of detail, we have these little  rocks that are sitting on top of the surface here.  Now if I go into Path Tracing mode, suddenly all that detail is completely gone and we're  left with this jagged, poorly rendered rock.  ...

**Frame:** tutorials\frames\fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro\frame_007.jpg

### Nanite is not compatible with some features, including Path Tracing & Ray Traced shadows. [4:58]
**Transcript:** inside of Unreal.  Specifically, it's not compatible with the Path Tracer.  And so when you switch to Path Tracing Mode, you lose all of that detail that has been  imported with your Nanite meshes.  Because Unreal isn't utilizing Nanite in order to render these things because it can't.  It's not compatible with the Path Tracer.  It's also not compatible with Ray Tracer's shadows.  And if you've ever noticed, you get some kind of weird funky artifacts on your geometry

**Frame:** tutorials\frames\fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro\frame_008.jpg

### Nanite with Ray Traced Shadows [5:22]
**Transcript:** sometimes when you're using Ray Tracer's shadows in your scene.

**Frame:** tutorials\frames\fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro\frame_009.jpg

### Nanite without Ray Traced Shadows [5:28]
**Transcript:** So how can we fix this problem?  So I want to show you the way that we used to fix this and I want to show you the way  that we can fix this now with the Path Tracer Pro plugin.  So if we click on this mesh and we double click on the static mesh down here, if we look,  now we can see that we have the full level of detail because we're in Lit Mode in this  preview window.  What we would have to do in the past is go down here and change this setting called Fallback  Relative Error down to zero.  And then we'd have to click Apply Changes.  And then we have to wait for it to actually load the mesh and apply those changes.  Now, that loaded very quickly for me, but this is not the case when you are first doing  this process.  So I already had changed the Fallback Relative Error in my project.  So it was already preloaded and it allowed it to make this conversion very quickly.  However, it normally takes between 30 and 45 seconds for me on this computer, which is  very good machine and runs unreal extremely well.  This takes about 30 to 40 seconds for it to actually load when you make that change.  And you can't do anything in the editor while it's loading.  You have to click Apply Chang...

**Frame:** tutorials\frames\fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro\frame_010.jpg


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
