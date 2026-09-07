---
title: Full UE5 Forest Cabin Tutorial - Procedural Tools & More!
source: YouTube
url: https://www.youtube.com/watch?v=VQMHQR4sQCo
author: Polygonflow Dash
ingested: 2026-09-07
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/full-ue5-forest-cabin-tutorial---procedural-tools-more/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# Full UE5 Forest Cabin Tutorial - Procedural Tools & More!

**Source:** [YouTube](https://www.youtube.com/watch?v=VQMHQR4sQCo)
**Author:** Polygonflow Dash
**Duration:** 29m41s | 12 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py full-ue5-forest-cabin-tutorial---procedural-tools-more <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, today we will see how we can make this scene in Unreal Engine using Dash.
[0:07] We will start by doing some vertex painting on our terrain, then scatter grass and trees,
[0:19] followed by vines,
[0:24] and IVs.
[0:27] We will finish with the lighting paths to embellish our scene.


### Terrain [0:37]
**Transcript (timestamped):**
[0:37] Let's start by typing terrain in the Dash toolbar. Select Create Terrain, your newly created terrain will appear in the viewport, alongside the Tools panel.
[0:48] I would like to hide the horizon line from eye level, curved value allows you to achieve that.
[0:56] UV scale will increase the tiling of the texture.
[1:01] Let's now apply a material on our terrain. I open the content browser and select the materials I would like to use.
[1:08] While holding down Ctrl, drag and drop them on your terrain and select Apply Blend Material.
[1:14] Now that we have a material applied, let's increase the tiling to make it look more natural.
[1:19] While your terrain is selected, go to the Tools panel, click on the Edit menu and select Edit Blend Material.
[1:27] I will scroll down to Global Tiling and change its value to 2.8.
[1:36] Now, if you zoom out, you will see how the tiling is repetitive. To solve that, I'll scroll down to Tiling Control and check Enable Breakup Tiling.
[1:45] We now get a nicer result.


### Curves & Road [1:52]
**Transcript (timestamped):**
[1:53] Let's move to the next step and create some deformation for the road on our terrain.
[1:58] In the Dash toolbar, type Draw and select Draw Curve, then draw a path on the terrain.
[2:05] You can adjust the distance value in order to reduce the points on the curve.
[2:15] In the Terrain Tools, under Curve deformation, I will add the curve and adjust some values like Width and Falloff to get a good result.
[2:27] Next, I'm going to place one curve that forms the path toward the cabin and another to level the terrain under the cabin.
[2:38] I would like to show you how you can manage the curves used to deform our terrain.
[2:46] In the Terrain Tool, under Curve deformation, click on Edit Table.
[2:52] A pop-up menu will open. You can click on the plus icon to add a new item.
[2:57] Make sure your curve is selected. Then click on the plus icon under Curve in order to add the curve to your item.
[3:05] You can adjust the Width to your liking and the position as well as the rotation of the curve.
[3:18] Let's add a second curve. While selected, click on the plus icon to add another item to the table.
[3:26] Then click on the plus icon under Curve to add an object.
[3:29] Adjust the Width to your liking. I found 11 was a value that matched what I was going for.
[3:42] While your curve is selected, you can also click on each point in order to manually adjust its position.
[3:59] Let's create a road on the road path. In the Dashbar, type Road and select Road tool.
[4:06] Make sure the curve is selected. In the Tools panel, click on the plus button under the Curves properties.
[4:15] The road will appear on the curve. Adjust some values like Width and Inside height to your liking.
[4:20] You can also apply any material you like. I decided to go for this nice Pine American Road material from the Megascans library. It gives it a really nice look.
[4:33] After I'm done with the road, I import the cabin from the Fisherman cabin asset pack that I downloaded from Fab.
[4:41] This cabin would be our main focal point.
[4:43] The set dressing is really nice. You can see all the details they put in.


### Vertex Painting [4:48]
**Transcript (timestamped):**
[4:51] To get rid of the shadow artifact, you can use the console command r.raytracing.normalbias with a value of 5.
[5:00] Because the path cannot be this uniform, let's vertex paint a different material on it.
[5:05] Switch to Modeling mode. Select your terrain and press the big icon.
[5:11] Then go to Attribute, Paint Vertex Colors and change a couple of values like Brush Size and Strength.
[5:18] And select only the R channel. Change the paint color to black.
[5:26] Then you can paint on the terrain and refine all the small areas.
[5:35] Let's now scatter some grass on the terrain. Select the grass from the Content Browser while holding CTRL, drop it in the scene and choose Scatter here.


### Scattering [5:45]
**Transcript (timestamped):**
[5:58] Adjust the density and other values to your liking.
[6:00] I also decided to change my lighting to make it match the mood I'm going for.
[6:10] Our grass is now scattered on the entire terrain. However, I would like it to be excluded from some areas like the road, cabin and main path.
[6:21] We can achieve that by selecting our curve and adding it to the proximity mask of the scattered grass.
[6:27] Click on the plus button of the Object property and adjust the width and falloff.
[6:40] We can apply the same process to the road and cabin.
[6:50] I would like to remove the grass from this area. It will be a secondary focal point.
[6:55] Let's draw a circle using our draw curve and add it to the object mask and play with the parameters to get a good result.
[7:12] Next, let's scatter some trees in the scene. In the Content Browser, I select the trees I would like to use. It's always good to have some variety.
[7:21] It will make your forest feel nice and natural.
[7:32] Once scattered, I reduce the density to a value of 0.2.
[7:36] Afterward, I have to clear the trees from all the paths using the same proximity mask method as before.
[7:54] Let's hide the forest to have a better view of the scene. I would like to also have some trees behind the cabin.
[8:01] For that, let's draw a curve and use path scatter on it to scatter some trees.
[8:07] I select my curve, hold CTRL and drag and drop them from the Content Browser and then choose scatter on selection.
[8:17] You can see that right now they look quite uniform. By adding some jitter, it will make them look more interesting.
[8:31] You will notice some trees are overlapping with the cabin. Let's clear them by adding them to the proximity table.
[9:02] I also cleared the tree from the secondary focal point. I would like to add a little bit of vertex painting to this area.
[9:13] We will have a fire pit right there, so grass cannot grow in that place.
[9:19] Let's also create a path leading from the house to the fire pit.
[9:24] Because this area will be a focal point, let's place a tree over there. I decided to do it manually.
[9:36] That way, I can rotate and scale it the way I want without it affecting the scattered trees.
[9:43] I noticed the grass was quite sparse. I decided to increase the density. Now it looks more lush and nice looking.
[9:53] Let's add a new asset. Select the Decogon library and type track in the search bar. Select the rusty old one.
[10:02] I would like it to feel like it's been sitting there for a long time and some plants grew on it.
[10:07] I decided to use the version that doesn't have doors anymore. It gives it the feeling that some scrappers stole them alongside some other parts.
[10:19] Let's also clear the grass around it.
[10:38] For the main path, you can see that right now it looks too artificial. Let's add some grass and weeds along that path.
[10:54] Now it looks better.
[11:07] You will notice that there are no trees on the left and the right. We can still see the sky.
[11:14] Thanks to this system being procedural, you can select the point of the curve just to move them or extrude them.
[11:23] The trees will grow where you moved the points.
[11:27] When we bring back the forest, now we have a nice looking scene.
[11:31] You will notice that right now we have trees and grass. We don't have plants that are in between the size.
[11:43] So I decided to add some bushes in order to break that. Have some large, medium and small.
[11:51] You can add the bushes to the grass scatter by selecting the grass and going into the edit table of the scatter and adding a new element.
[12:01] Then you select your grass or your bushes and add them.
[12:08] Of course you have to play with the density. I decided to reduce the density to 0.1.
[12:14] Now it looks much nicer with a nice variety.
[12:21] One more thing that I would like to have is a path, a clear path from the cabin to the fireplace or the fire pit area.
[12:31] Now we can go to the fountain browser, go to Polyhaven and find a nice fireplace or fire pit.
[12:38] Place it where we would like it to be.
[12:41] Now we can go to the fountain browser, go to Polyhaven and find a nice fireplace or fire pit.


### Fireplace [12:44]
**Transcript (timestamped):**
[12:47] In our case, we would like it to be right in the middle of this soil area.
[12:55] I would like to also have some wood inside the fire pit. Later on we will also add a fire.
[13:02] I decided to add a fire pit.
[13:05] I decided to add a fire pit.
[13:08] I would like to also have some wood inside the fire pit. Later on we will also add a fire.
[13:16] I decided to use physics paint in order to place the wood inside the fire pit.
[13:21] Now let's now add the fire.
[13:25] I have a couple of assets or blueprints here that use fire.
[13:30] The blueprint are mostly comprised of Niagara particles and some textures.
[13:52] When working on a scene like this, composition is really important.
[13:57] That's why you will sometimes see me move around trees, rotate them or the truck for instance.
[14:04] I had to play a lot around with it in order to get a nice composition.
[14:10] Let's scatter some grass and weeds on the roof.
[14:21] In an overgrown environment, we can find some vines and plants hanging from the roofs.


### Vines [14:28]
**Transcript (timestamped):**
[14:35] Let's add that to our cabin.
[14:38] Open the content browser, then go to the Quixel library and select the broom creeper.
[14:45] Drag and drop it on your curve, select scatter on selection.
[14:50] You will see that they are scattered however their position is not correct.
[14:55] By disabling the use asset rotation scale, they will be in the correct rotation.
[15:00] Let's now create some vines on our truck.
[15:08] Open the content browser, select your atlases, drag and drop them on your truck and choose create vines on selection.
[15:17] The vines will be created.
[15:19] You can tweak some values like growth instance, growth size and seed in order to get the result you're after.
[15:49] Let's add some additional assets next to our fire pit.
[16:03] You will notice that these assets don't blend well with our terrain.


### RVT Blending [16:04]
**Transcript (timestamped):**
[16:10] Select the terrain and run the RVT command.
[16:18] Enable virtual texture on your scattered assets.
[16:24] Select the assets, go to the tools panel, click on the edit menu, then select edit material.
[16:30] Scroll down to enable virtual texture and check the box.
[16:35] Now our assets blend really well.
[16:40] Let's add some more vines.
[16:47] Now we're taking full advantage of the content browser in order to place the assets that we would like them.
[17:17] And our direct our scene.
[17:34] Now that area looks more natural.
[17:37] We can also have some assets next to the tree or right under the tree.
[17:43] At first I wanted to use this one.
[17:46] Then I realized that it doesn't match well.
[17:49] However, it can be placed right next to the tree and we can use another asset instead.
[18:01] We also enable RVT on this one just to make it blend with the scene.
[18:14] One more thing that I would like to do is have some vines growing along the tree.
[18:20] Right now the tree looks nice, however it can be a little bit more interesting.
[18:27] One of the important values here is mainly the seed.
[18:32] By playing with the seed I can get a lot of different variations.
[18:49] Now the result looks quite nice.
[18:58] I bring back the forest and we can see the composition.


### Lighting [19:01]
**Transcript (timestamped):**
[19:03] Now one of the important parts of any scene is lighting.
[19:09] I start by adding that small fire torch and then I call the lighting.
[19:14] I add first these spotlights.
[19:20] They are round a lot with the intensity and the unit as well as the attenuation radius and the volumetric scatter.
[19:45] Let's also put the light on the window up there.
[19:52] That way it will be visible from the outside.
[20:15] Next is the fire pit.
[20:19] I would like it to be quite bright, that way it will influence the vegetation surrounding it.
[20:27] Now I can adjust the volumetric on that window.
[20:58] We can also add some rocks on our main path in order to make it more interesting.
[21:05] By enabling RVT on the rocks it will give them the feeling of having moss.
[21:27] Next let's go to the dash bar and click on create.


### Fog [21:42]
**Transcript (timestamped):**
[21:48] Then select create fog card.
[21:51] A fog card will appear in the scene.
[21:53] You can move it around and scale it to your liking.
[22:03] By playing around with the cloud density and cloud brightness and color tint you will be able to change the color and its density to your liking.
[22:23] Let's place a couple of them in our scene in order to push back some of the trees and create some nice fogging behind the cabin.
[22:53] Depending on the value of your exponential height fog it is important to play with the cloud brightness in order for your color to be visible in your scene.
[23:04] The higher the brightness the more visible your colors will be.


### Camera Setup [24:22]
**Transcript (timestamped):**
[24:23] Next we can create a camera and add it in our scene.
[24:28] In the dash bar type camera and select create camera.
[24:35] Go to the tools panel, click on the edit menu and select edit camera.
[24:41] Now you will be able to edit your camera and see the result directly in the viewport.
[24:46] I like to play around with the focal length.
[24:48] Usually 24 gives a nice result and a good squeeze factor to make it feel cinematic as that's what we are going for.
[25:01] We can also add some post processing effects like grading presets.
[25:07] I like to go for bright sunny day.
[25:09] It looks really nice and some effects like film grain, vignette and sharpen.
[25:18] I notice that the cabin is facing too much towards the path.


### Final Tweaks [25:28]
**Transcript (timestamped):**
[25:36] It could look slightly more towards the left and we will see the side of the cabin and the light coming out of the window.
[25:44] I decided to rotate the cabin and this is the new composition that we get.
[25:52] Of course with the rotation we also need to adjust the roof.
[25:57] You will see that the grass is now a little bit offset to adjust that.
[26:02] Now we can place a rectangular light on the main path.
[26:15] It will bring in a little bit more warmth to the scene overall.
[26:25] It will also highlight the path.
[27:02] I also decided to reduce the start and distance of my exponential height bog.
[27:10] I also decided to reduce the start and distance of my exponential height bog.
[27:20] I noticed that the highlight on the tree is not strong enough which is why I decided to add another yellow light and place it right next to the trunk.
[27:35] It created a stronger highlight on that tree.
[27:43] There can be another fog separating the fire and the trees.
[27:51] This area right here was quite dark.
[27:57] I decided to add a rectangular light in order to make it more visible, especially at a distance.
[28:04] I decided to add a rectangular light to the tree.
[28:10] I decided to add a rectangular light in order to make it more visible, especially at a distance.
[28:21] Now it looks more natural.
[28:31] Last but not least, let's place some falling leaves in our scene.
[28:38] In the dash bar go to create then create falling leaves.
[28:43] You will see it appear in the scene. Select it and move it around to where you would like the leaves to be falling.
[28:52] I decided to place it next to the fire pit, of course above ground, that way it will feel like the leaves are falling down.
[29:00] I also increased the radius, the spawn radius to a value of 500 and put maximum leaf spawn rate.
[29:12] I hope you guys liked this video and I hope you will be able to implement some of the things you learned throughout this video in your own project.
[29:28] Leave a like and subscribe if you would like to see more.
[29:32] Thanks for watching.



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
