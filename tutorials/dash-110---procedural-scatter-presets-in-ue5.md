---
title: DASH 1.10 - PROCEDURAL SCATTER PRESETS IN UE5
source: YouTube
url: https://www.youtube.com/watch?v=EN6X-d6DIb0
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/dash-110---procedural-scatter-presets-in-ue5/
frame_count: 9
---

# DASH 1.10 - PROCEDURAL SCATTER PRESETS IN UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=EN6X-d6DIb0)
**Author:** Polygonflow Dash
**Duration:** 10m7s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hello, I'm Thomas from Polygonflow.  Today I'm excited to show you the latest updated dash, the worldbuilding plugin for Unreal  Engine 5.  This update brings a complete overhaul of our preset system, making dash even easier to  use, more flexible and significantly more powerful.  In addition to that, we've added several new features and improvements across the plugin.  So let's jump in.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_000.jpg

### Presets [0:24]
**Transcript:** Alright, let's start by creating a simple cleaf preset for a canyon using PathSkatter.  First, I use the draw curve tool to define the shape of my canyon.  Then I go to the content browser, find my preferred cleaf asset, and while my curve is selected,  I drag it into the level by holding Ctrl to see the drop options.  From there, I choose geterons selected to automatically create the pathskatter on my curve.  Now I can tweak a few settings such as density and scale.  Once I'm happy with the result, I can create a preset using the preset icon in the tool  spinal.  I will give it a name, some text, and the thumbnail, then I choose global scope and save it.  With global scope, I can access the preset in any of my projects.  Now let's open a new empty level and try it out.  In the new level, I open PathSkatter from the dashboard.  When I click the preset icon, I can see my newly created canyon preset.  And with a single click, it's recreated exactly as before.  And I just hide the scatter reference mesh.  And as you can see, everything remains fully procedural, so I can continue adjusting any  of the settings just like before.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_001.jpg

### Compound Presets [1:50]
**Transcript:** And now let's expand this simple cleaf preset into something more advanced, an overgrown  canyon using the updated compound and reference systems.  So first, I scatter some rocks under the cliffs using the same spline as before.  A few tweaks to make it look better.  And next I will scatter some foliage onto the cliffs using surface scatter.  I select the cliffs, hold Ctrl and drag in a few foliage assets and choose scatter  on selected.  Then I adjust the settings like density, height, mask, and scale to get a natural distribution.  Let's add some foliage variation.  Next I want some rocks on the ground.  So I will select the plane beneath my cliffs and scatter some assets onto it.  To remove rocks underneath the cliffs, I can use a proximity mask.  I pin the ground scatter tool to keep it open.  Select the cliffs and assign them as proximity objects.  Then I tweak the distance and width to control exactly where the rocks appear around the cliff  formations.  Now the setup looks good.  Let's organize everything using the compound and reference systems.  I click a property, choose create compound tool, and name it overgrown canyon.  Then I add the key properties for each tool to th...

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_002.jpg

### Physics Paint Scales [5:10]
**Transcript:** A new feature I want to show you today is an improvement to the physics paint.  You can now control object scaling using the min and max scale range.  While in physics paint mode, I can simply adjust these values to introduce natural size  variations as I paint.  This is small addition, but it gives you more control and more organic results when painting  assets into your scene.  And after that, I just drop in the dash water plane and the scene is done.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_003.jpg

### Preset Library [6:13]
**Transcript:** To make managing and using presets even easier, we've added a dedicated preset library inside  the content browser.  Here you can browse, search, and quickly access to all your dash presets in one place.  For example, here is my overgrown canyon preset from before.  On the last side, you can find folder structure where presets are organized into different  categories, including project and global presets.  If you save a preset with global scope, it becomes available across all your unrelanging  projects.  Just keep in mind that the assets used in the preset need to exist at the same location  in the other project for everything to work correctly.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_004.jpg

### Built-in Presets [6:51]
**Transcript:** To happy cast started with the new preset system and with dash in general, we've included  a bunch of presets in dash 1.10.  All of them are free to use, explore, and customize.  Some are simple single tool presets, while others are more advanced compound setups that  demonstrate how different tools can work together.  All built in presets use free to use assets from Quaternius, so if you like what you see,  you can check out the full library as well.  In our presets, these assets act as placeholders.  So once you place a preset into your level, you can easily replace the assigned meshes with  your own assets and adapt everything to your project.  Like this, with this preset, I can easily swap out the assets in the edit table.  Another new feature in dash 1.10 is that the basket on us supports decals and blueprint

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_005.jpg

### Decal Scattering [8:12]
**Transcript:** actors.  For example, I can draw a curve and scatter footsteps decals along it.  Let's change the scatter type to actors.  To make the footsteps look natural, I just set the settings a bit.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_006.jpg

### Blueprint Scattering [8:51]
**Transcript:** Let's try a blueprint.  I place a blueprint in my level.  Select the curve and open path scatter.  I simply switch the scatter type from instances to actors again and add the curve and the blueprint.  And just like that, the blueprint is scattered along this line.  This makes path scatter much more flexible, especially for gameplay elements or more  advanced setups.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_007.jpg

### Outro [9:22]
**Transcript:** And that wraps up dash 1.10.  Using the completely redesigned preset system, built in presets, improved path scatter and  edit control in physics paint, dash is not even easier to use while giving you more  flexibility and power when building words in Unreal Engine 5.  And as always, if you have feedback, ideas for future presets or features you'd like  to see in dash, let us know in the comments.  Thanks for watching and see you in the next one.

**Frame:** tutorials\frames\dash-110---procedural-scatter-presets-in-ue5\frame_008.jpg


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
