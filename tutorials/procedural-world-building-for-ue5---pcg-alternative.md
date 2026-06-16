---
title: PROCEDURAL WORLD BUILDING FOR UE5 - PCG ALTERNATIVE
source: YouTube
url: https://www.youtube.com/watch?v=KsgW-19y4ts
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-world-building-for-ue5---pcg-alternative/
frame_count: 10
---

# PROCEDURAL WORLD BUILDING FOR UE5 - PCG ALTERNATIVE

**Source:** [YouTube](https://www.youtube.com/watch?v=KsgW-19y4ts)
**Author:** Polygonflow Dash
**Duration:** 29m24s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hello and welcome. Have you ever opened an under scene and thought, uh, this needs a lot more details?  In this video we'll take a look at the dash plugin for under 5. These tools let you build  environments fully procedurally, just like with the native PCG plugin, but these tools are designed  to be very easy to use, so that you can quickly bring your environments to life, without  dealing with all the notes and complexity of PCG. And if you stick around till the end, I'll show you  some clever tips to speed up your workflow and get the most out of dash. So let's get started.

**Frame:** tutorials\frames\procedural-world-building-for-ue5---pcg-alternative\frame_000.jpg

### Surface Scatter [0:35]
**Transcript:** Let's start with the simplest and most popular tool, the Surface Skiather.  I've opened up a first scene in Unreal, with nothing just a basic terrain plane, nothing too fancy.  From the dash toolbar, I open the content browser,  and from here I can find and use my already downloaded quicksomegascancessets.  Including these nice oiled grass models.  Using dash is super straightforward. I just grab the asset, hold down Ctrl,  and drag and drop it onto the terrain. And I choose Scatter on Selection.  Grassclamps are instantly scattered across the selected surface.  The toolspanel shows up, giving us access to how the scatter settings. If you don't  see it or accidentally close it, no worries. Just go back to the dash toolbar, click edit,  and the toolspanel will open up again. And if you click the list button in the top left corner,  you will see a list of all the active dash tools in the scene. So now, under density,  we can control how densely the assets are scattered. Below that, we can also tweak the scale of  the instances. Let's pump up the density a bit and turn this into nice, grassy field.  Now let's take a quick look at basic masking, starting with the noise mask.  I can con...

**Frame:** tutorials\frames\procedural-world-building-for-ue5---pcg-alternative\frame_001.jpg

### Path Scatter [7:04]
**Transcript:** I'm in a new scene now and I've bought in a mega-scancliffe asset. I want to scatter this clip along  a path to create a kind of rocky shoreline. From dash toolbar, I open the path scatter under the  scatter section. In the tool panel that pops up, we have two main sections, curves and scatter.  I add my cliff as set to the scatter section, but right now there's no curve in the scene.  So let's throw one. I got to create curve tools, draw curve.  Here I can define the spacing between curve points and choose how smooth I want the curve to be.  Once I'm happy, I hit stop and I add the curve to my path scatter. The cliffs show up along the path.  And let's hide the original cliff.  As usual, I can tweak the density to control harmony as the passes appear and I can change the density mode.  For example, right now I'm using the mode that places one cliff per curve point.  You can also specify an exact number of instances to scatter, regardless of the curve length.  Try different modes to see what fits your needs.  Another super useful option is to adjust the pivot offset or the path smills, which controls how  your assets align to the curve and how smoothly they follow its direction.  W...

**Frame:** tutorials\frames\procedural-world-building-for-ue5---pcg-alternative\frame_002.jpg

### Grid Scatter [13:35]
**Transcript:** stone fence ruins using a few mega-scans assets. The grid scatter is great for when you want to lay  out assets in an even structured pattern. I will start by dragging a rock model from the  content browser into the scene. Then under the scatter section of the dash toolbar, I select the  grid scatter tool. I set the rock as both the origin of the grid and the object I want to scatter.  And as you can see, a bunch of instances appear around the original mesh.  I take the scale a bit and set the distribution mode to 3D, so I can stack instances along the Z  axis too. At first nothing seems to appear above, and that's because the high division value is  set to 0. Once I increase it, we'll start getting vertical layers of the rocks.  After a bit of experimentation, I'm happy with the overall pile of rocks.  So now since the grid scatter duplicates in both positive and negative directions from the pivot  point, I scroll down to the feature masking section and enable the option to remove instances  below the origin on the Z axis. Here's also where I refine the remove mask,  and I will use this combination with the proximity mask to carve out the chunk of the stone pile.  From the dash to...

**Frame:** tutorials\frames\procedural-world-building-for-ue5---pcg-alternative\frame_003.jpg

### Radial Scatter [17:08]
**Transcript:** our familiar rock model. From the scatter menu, I select radial scatter, and in the tool's model,  I add the model. Instances appear arranged in a circle pattern. From here, we have tons of  possibilities. I can control the number of instances, the radius, the start angle, or even create a  spiral staircase effect by taking the height parameter. I'd like to create a tower. To do that,  I need to duplicate the concentric rings, which I can do in the concentric section.  I want these extra rings to stack up parts instead of spreading outward.  So I increase the ring height, and set both the minimum and maximum concentric distance to zero.  Add a little adjustment to the overall height, and some fine tuning of the ring offsets.  I will add a few more rings to flesh out the structure, and keep adjusting it until I'm happy with the  tower. But I'm not limited to circles. I can also switch to a random square shape,  using the shaping section in a tool's panel.  And by playing with the scale settings, I can get some interesting results.  I will also apply a bit of random rotation to break up the uniformity.  The color of my tower feels a bit off compared to the environment. Luckily, with ...

**Frame:** tutorials\frames\procedural-world-building-for-ue5---pcg-alternative\frame_004.jpg

### Decal Scatter [22:40]
**Transcript:** use scatter decals across surfaces with ease. I have some dulled up decals from the quickslaunch  bridge plugin that I can use through the dash content browser. I select a couple of them and  with control held down, I drag and drop them onto the surface where I want them scattered.  From the pop-up, I choose scatter here.  I adjust the scale of the scatter decals and tweak the seed value until I get the distribution I like.  I can also define the total number of decals I want in the surface and even adjust the depth.  Just like with the other tools, masking and rotation controls are also available in the decals  scatter tool. You can also access decals scattered directly from the dash toolbar like any other  scatter tool. I will now create another scatter setup. This time, I'm using an existing decal from  my scene. I add the ground surface to the surface section and the goes decal to the decal section.

**Frame:** tutorials\frames\procedural-world-building-for-ue5---pcg-alternative\frame_005.jpg

### Reference & Compound Tool [24:09]
**Transcript:** Now let's take a look at a couple of incredibly useful features, starting with the reference tool  and the compound tool. In every scene, you can have a reference tool. Think of it as a centralized  storage for any properties you want to share between multiple tools, so they all stay in sync.  Let's start with a simple example. I will drag in our familiar rock model and set up a grid  scatter using it. Let's say I want to control the width, depth and the height parameters together,  while still having the flexibility to tweak them individually. I go to a little like a next  the width and choose convert reference. I will name this reference spacing.  So now I can assign the same spacing reference to other sliders. All three parameters are now  linked to the same reference, which means I can adjust them globally via the reference tool,  but also individually through their own sliders.  The reference tool appears in the tools panel, like any other tool, and from there I can easily  manage or rename the references I've created. Now let's move on to the compound tool. Think of  this as an empty container where you can collect and expose only the parameters you care about  from various t...

**Frame:** tutorials\frames\procedural-world-building-for-ue5---pcg-alternative\frame_006.jpg

### Merge Action [26:53]
**Transcript:** mesh from a selection of multiple actors. For example, if you've made a stone ruin and scattered  some foliage on it, you can use the merge actors to combine them into one mesh. I will select both the  ruin and the foliage scatter on top of it. In the dash toolbar, I type merge and select merge  actors. This process might take a few seconds depending on how complex your selection is. The newly  merge static mesh appears in the content browser and I can drag it straight into the scene. This is a  great way to create modular assets, helping you build your scenes faster and keep everything more  manageable. Finally, I want to say a few words about tool presets. Every tool in dash

**Frame:** tutorials\frames\procedural-world-building-for-ue5---pcg-alternative\frame_007.jpg

### Tool Presets [27:35]
**Transcript:** can have its properties saved as a preset, making it super easy to reuse your favorite setups  or even share them with others. Let me show you a simple example. I've used the grid scatter tool  to create a stone pillar. It's fully procedural and adjustable. From the toolspanel, I'd  click this icon and choose create preset. Let's say I want to create another pillar with the same  grid scatter settings. I select my mesh, edit to a new grid scatter tool,  and then click the preset icon in the toolspanel. From there, I simply select the preset I saved  earlier and there it is, another pillar instantly set up.

**Frame:** tutorials\frames\procedural-world-building-for-ue5---pcg-alternative\frame_008.jpg

### Outro [28:35]
**Transcript:** And so that wraps up the video. We've covered a lot from scattering, masking, references, material  tweaks and presets to even merging assets into a final mesh. If you enjoyed this overview,  don't forget to like, subscribe and most importantly, give dash a try.  It's a powerful toolset that makes working in Unreal not just faster, but more fun.  Thanks for watching and see you in the next one.

**Frame:** tutorials\frames\procedural-world-building-for-ue5---pcg-alternative\frame_009.jpg


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
