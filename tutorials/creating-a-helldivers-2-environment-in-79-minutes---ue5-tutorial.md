---
title: Creating a Helldivers 2 Environment in 79 minutes - UE5 Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=kJhqc5_6usc
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial/
frame_count: 22
---

# Creating a Helldivers 2 Environment in 79 minutes - UE5 Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=kJhqc5_6usc)
**Author:** Polygonflow Dash
**Duration:** 80m12s | 22 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction [0:00]
**Transcript:** I'm going to create this had-ever-stue inspired environment in Unreal Engine 5.  I really enjoyed this game and I was inspired by the planned ocean to create this scene.  The game already looks amazing, especially as it was put together in the Stingray game engine.  My name is Tamash, I work for Dash.  It is a world-building assistant for Unreal.  In this video, I'm going to show you my favorite tools.  I will demonstrate how to create a playable level with our easy-to-use procedural tools  and without having to learn complex notes or scripts.  This video is a long step-by-step breakdown tutorial that you can follow along if you want.  We have also posted a shorter version of the video.  You can find the link in the description.  You can get a full feature, free trial on our website if you want to follow along.  After all this, there's nothing left but to dive in.  I create a new project and I select the third person template.  I name my project and press create.  Now I create a new level and empty one.  Under the window tab, I click on the environment light mixer and add these components into the scene.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_000.jpg

### Procedural Terrain [1:30]
**Transcript:** Next, I click on the dash icon, which brings up the dash toolbar.  I type in the word terrain and click on the create terrain option.  This creates a terrain for us.  I set the scale and play around with the values.  Well, something like this.  I'm going to drop in the material that I downloaded from the Megascan library.  And I set the UV scale to 10.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_001.jpg

### Procedural Cliffs [2:30]
**Transcript:** Next, I'm going to use the dash curve tool and I'm going to scatter some cliffs on it.  I type in the word curve and select the curve tool option.  I set the minimum spacing to 60.  Then I click on the start drawing button.  I draw the line on the ground.  As you can see, I can adjust the points of the curve individually.  I have downloaded the cliff mesh.  It's from the Megascan standard pack.  Holding down control, I drag it under the curve and select scatter on selection.  Here, I can adjust the test, D and rotate them 180 degrees on the Z axis,  so the mountains face inward.  I can drag the curve points anywhere and the scattered objects will follow.  I want to place smaller cliffs in front of the larger ones, so I do the same method again.  And I will draw the curve here.  At minus bottom, straight down the curve,  Francisco Straight Multiply,  A few adjustments and there we go.  I will adjust the materials a bit, isolate the mountains and click on the edit material icon  on the dashboard bar.  I give the magrenair tint and lower the saturation and brightness.  And I also set the roughness to 0.4.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_002.jpg

### AI Tagging Assets [6:08]
**Transcript:** In the next step, I will show you the dash AI tagging system.  It helps to take assets in my project, so I can easily search for them based on tributes,  not just names.  I can already see two projects here where I have completed the AI tagging.  The advantage of this is that it's not necessary to migrate assets between projects.  They are accessible in a new project with the help of dash.  And this project I'll be using models on the Mission Terminera Vakitbush pack, which  you can get for free.  You can find the link in the description.  I also use some assets from the Science Laboratory pack.  As you can see, there are currently zero assets tagged.  I select the folders I want to tag and click on the Compute button to start the process.  This might take a while, so go and make a coffee or watch another dash tutorial on our  channel.  The asset icons have appeared in the dash library.  Now I can search for properties.  If I type in the word storage, it will show as a tag width storage.  Like this container, I can also manually add text.  Let's see what happens if I search for a color.  Yep, my blue color dashed appear.  I can also combine text like blue fences.  And I can select ...

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_003.jpg

### Placing Initial Assets [8:10]
**Transcript:** Now I will start setting up the area.  I select the few assets from the library and drag them into the scene.  I will set up an outpost here.  I can rotate and scale the assets with hotkeys.  Here you can see the combinations.  Let's drop in a few platforms.  I want to place a few containers on these platforms.  And if I need to stack a few, I can do it manually by duplicating the items.  But here I want the largest stack of containers.  This is where I will use the grid scatter tool.  Maybe I select the smaller model here.  Let's try that one.  I type grid into the dash toolbar and select the grid scatter tool.  For both the grid origin and instance mesh, I use this model.  I can set the pivot point to the center by typing pivot and center into the dash toolbar.  Next, let's place some larger rocks into the scene.  I drag and drop a few larger assets.  I download them from the Megascans library and droply position them into the scene.  And I add a few smaller rocks as well to make the composition more interesting.  The next step is to scatter medium sized rocks across the area.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_004.jpg

### Scattering and Masking Assets [13:30]
**Transcript:** I suck the terrain and while holding down control, I drag in the rock model and click on  the scatter on selection.  I can also sync them a bit more into the ground.  And I can adjust to see the bit.  And now I'm going to draw a curve here along which I will mask out some rocks.  I click on the solid drawing and draw it roughly here.  You can edit and move this curve later.  Just drag it and the scattered objects attached to it will follow.  I select rocks and in the edit window I scroll down to the proximity masking section.  Here I add my curve as an object.  I click on invert and enter a number for distance.  I actually want to have a path along the curve with no rocks.  In proximity mask 2, I add the curve again, set a distance and you can see a nicely masked  path appeared.  Wherever I move the curve points, the scattered objects will follow.  Now, I select these few meshes and add them to the proximity mask 3 which will mask  the curve.  I will scatter another model across the ground.  And I will set its parameters the same way.  I will use the noise masking tool here to set how frequently they should be scattered.  I will also use the proximity mask here.  Now, I will scatte...

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_005.jpg

### Physics Asset Placement [32:20]
**Transcript:** I will scatter these two assets.  I drag them into the sea.  I type physics into the dash toolbar and select the physics tool.  A new bar pops up.  Let's make sure that the assets are set to dynamic.  And click on play to start the simulation.  And I can duplicate them a few times.  I think this looks great.  I will stop the simulation.  Another great function of the physics tool is the paint function.  I selected this rubble pack from the Megascans library.  Holding down control, I drag them into the scene and click on place overlap.  I place each version of the rubble pack into the scene.  I select all of them and click on paint to scatter them around the scene.  With Shift plus the middle mouse button, I can adjust the brush size.  And by holding down control, shift in the left mouse button.  I can adjust the scattering density.  Now I simply scatter some rubble in a few places.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_006.jpg

### Scattering Decals [35:10]
**Transcript:** This building looks quite clean.  I will select some decals from the library by holding now shift.  And by holding down control, I will drag them onto the building.  Dash will scatter the decals on the selected surface.  I can adjust the scene randomly.  I will increase the scale.  Sometimes a few decals end up in the wrong place.  I can delete those.  I drag a few more decals manually onto the building.  I can adjust the scattering density.  I can adjust the scattering density.  I can adjust the scattering density.  I can adjust the scattering density.  Let's deal with the black flickering.  Simply enter this command.  And for lesser foliage, type in this.  To create advantage of Dash is that elements created with it are non-destructive.  You can adjust them anytime.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_007.jpg

### Baking the Scatters [38:30]
**Transcript:** These scattered instances can be converted into individual meshes, allowing single object editing.  I think I'm generally satisfied with the layout.  But in some places, I like to delete or move a few objects.  For example, I want to bake these medium sized rocks.  I type bake into the Dash toolbar and select the bake instances option.  I add the selected rocks with the plus button.  Dash has generated the individual objects for me, retaining the original scatter setup,  which we can hide or delete.  Now I can adjust the rocks individually.  I also bake these rocks as well.  I can do the same with grass.  I type foliage into the toolbar and select convert instances to foliage.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_008.jpg

### Converting to Foliage Paint [39:50]
**Transcript:** This way we get grass that we can edit with the classic foliage editor.  Here you can see all the grass types I scattered.  Now I will clean out some places.  I can apply some paste as shown in my description.  Now I will add clouds to the scenery and Angie.  Now I am designing a tilescape, so I will use this for coloring.  I drop in a few more props around the outpost to make the area more lived in.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_009.jpg

### Adding More Assets [42:08]
**Transcript:** And I can arrange the rocks a bit.  I will also scatter some decals here.  I will also scatter some decals here.  I have also placed a larger rock into the background and scatter a few gravel models around it to blend it better into the environment.  I bake the surrounding clips too. I delete some of them.  I will tidy up this area a bit.  Next I will adjust the colors of the rocks.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_010.jpg

### Adjusting Materials [47:35]
**Transcript:** I set the hue to 0.1 to get the greenish shade. I decrease the saturation and the brightness.  I do the same for the other rocks.   Now let's talk about this.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_011.jpg

### Atlases & Procedural Vines [49:25]
**Transcript:** Now let's talk about the Dash Wine tool. It's available in the Dash version 1.7. I simply  select the Nettles from the Dash Library. You can make these available into Dash Library  by downloading them in the standalone Wixel Bridge app. And by setting the download folder  here. I select the rock and while holding tank control, I drag the Atlas onto the rock.  I choose the Create Wines on Selection option. And there we go. I can set its parameters  as I like. I'll make it a bit longer. I can set the scale of the leaves here. For the  material, I simply drag a 3-barque material onto the branches. Creating a nighttime

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_012.jpg

### Adjusting the Lighting (UE) [50:18]
**Transcript:** scene in Unreal isn't an easy task. But there are plenty of tutorials on YouTube on this topic.  Unfortunately, it's not straightforward to create nighttime lighting in Unreal with  the basic tools. But I'll show you where to start. First, you need to enable the  Engine content. You can do it here. I can search for the Skyspear Blueprint, which I'll  drag it to the scene. I lower the Sun, and decrease the intensity of the directional  light. Let's say to 1. We can add a slightly bluish tint to the directional light. I set the  indirect lighting to 6. Rotate a bit. Now I will add the process process for him to the scene.  And I set it to Unbound. I adjust exposure.  And let's set up the fog, too. Check the volume metric fog.  Set the scatter distribution to 0.4. Now, and the extension scale to 6.2. You can adjust the fog  settings as you like.  We can also adjust brightness of the stars.  There's still a lot we can tweak. Maybe I can improve it with the color grid. A bit darker blue.  So we have created a let's say okay night lighting, but I will show you a simpler solution.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_013.jpg

### Adjusting the Lighting (UDS) [53:20]
**Transcript:** To do this, I first delete all my light sources and the process for you.  We can save a lot of time by using the Ultra Dynamic Skype plugin instead of messing around with  the built-in lighting tools. I drag the Ultra Dynamic Skype blueprint into the scene.  And now, or scene is lit up again, I set the time to midnight. I set the night brightness to,  let's say, 3. For the exposure, I take in the instant exposure adjustment.  And I will enable the volume metric fog also.  I'm just messing around with settings until I'm happy with the result.  Now, the scene is coming together.  I will brighten up this building a bit to make it more visible. I will drag a rectangular light in.  I set the intensity a bit lower.  And the source panel a bit larger.  It's important to turn off volume metric scattering so the light source doesn't show up in the fog.  That was also set the indirect lighting to 0.  Let's test the scene.  The clouds behave strangely behind the fog so I set the cloud coverage to 0.  I scatter a few lightposts that I modeled in Blender, basically just a cylinder of two materials.  I add some flying particles to the scene, I type in particle into the dash toolbar and select it...

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_014.jpg

### Adding Floating Particles [57:40]
**Transcript:** I will also add some paddles, a simply type water into the dash toolbar and it will generate the

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_015.jpg

### Adding More Props [59:00]
**Transcript:** plane with the water material on it.  I will also drop in some small blue prints.  You can also find a link for this down below.  And here I scatter a few blood stained eclos in some places.  And I can adjust the color to  area with sky surfaceGeumert,  And I'm going to scatter these yellow mushrooms near some larger rocks.  I don't need that many variations.  I will keep to.  And I will use proximity masking again.  This area here is quite empty, so I will scatter some barrels here.  Some decals also.  Find a very good helldiver and bi-titan model on the helldivers archive this court server.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_016.jpg

### Helldivers Characters [65:50]
**Transcript:** Since these are blender projects with blender materials, I bake a new texture for them which I will be using in Unreal.  I also animated the titan a bit, which I exported to Unreal. You can also find a link to the server down below.  I dropped the titan into the scene. It will be needed for the cinematic slater.  Now I'd record post process for you into the scene.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_017.jpg

### Adjusting PPV [66:32]
**Transcript:** I set it to Ambound, a play around with the values.  And now let's test the scene again.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_018.jpg

### Playable Helldivers Character [68:28]
**Transcript:** A stentere plays the player character with their helldiver model.  Matt asplans tutorial does a great job of explaining the steps. The link to the tutorial can be found below.  I'm pretty satisfied how the scene turned out.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_019.jpg

### Adding and Adjusting Cameras [68:49]
**Transcript:** Now I want to create a few cinematic shots for the scene. I will create a dash camera.  And I will set the aspect ratio.  Now I try to set up a good composition.  I can adjust post processing and the color grading here as well.  Blume, film grain, fringe and so on.  If I don't have a specific idea of what grade the shot should have, I can choose a preset.  I choose this one.  We can also select an image from our computer and drag it into the dash toolbar.  The selected camera's color grade will take on the color properties of the image. This is also a new dash 1.7 feature.  But let's stick with the pale and greenish blue setting.  I will create another camera and I will set up another angle.  I will set up another angle.  I will set up another angle.  I will set up another angle.  I will set up another angle.  I will set up another angle.  I will set up another angle.  I will set up another angle.  I will set up another angle.  I will set up another angle.  Maybe this shot needs a few more rocks.  I will set up another angle.  I will set up another angle.  I will set up another angle.  I will set up another angle.  I will set up another angle.  I will set up another angle.  I will ...

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_020.jpg

### Adding Fog Cards [78:13]
**Transcript:** I type in fog and select it.  I can easily adjust it.  I want a very faint fog, just enough to be visible.  I will set up another angle.  I will set up another angle.  I will set up another angle.  And with that, the scene is pretty much done.  I hope you find this video useful.  I had a lot of fun putting it together.  If you like this video, consider joining our Discord server or subscribe to our YouTube channel.  Thanks for watching and see you in the next one.

**Frame:** tutorials\frames\creating-a-helldivers-2-environment-in-79-minutes---ue5-tutorial\frame_021.jpg


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
