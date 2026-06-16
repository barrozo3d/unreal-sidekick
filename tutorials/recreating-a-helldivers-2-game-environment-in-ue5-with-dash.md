---
title: Recreating a Helldivers 2 Game Environment in UE5 with Dash
source: YouTube
url: https://www.youtube.com/watch?v=plpGMR46HnE
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/recreating-a-helldivers-2-game-environment-in-ue5-with-dash/
frame_count: 17
---

# Recreating a Helldivers 2 Game Environment in UE5 with Dash

**Source:** [YouTube](https://www.youtube.com/watch?v=plpGMR46HnE)
**Author:** Polygonflow Dash
**Duration:** 22m56s | 17 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction [0:00]
**Transcript:** I'm going to create this had-ever-stue inspired environment in Unreal Engine 5.  I really enjoyed this game and I was inspired by the planned ocean to create this scene.  The game already looks amazing, especially as it was put together in the Stingray game  engine.  My name is Tamash, I work for Dash.  It is a world-building assistant for Unreal.  In this video I'm gonna show you my favorite tools.  I will demonstrate how to create a playable level with our easy-to-use procedural tools,  and without having to learn complex notes or scripts.  You can get a full feature, free trial on our website if you want to follow along.  After all this, there's nothing left but to dive in.  Create a new project and I select the third person template.  Now I create a new level and empty one.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_000.jpg

### Procedural Terrain [0:48]
**Transcript:** Next I click on the Dash icon, which brings up the Dash toolbar.  I type in the word terrain and click on the Create Terrain option.  Dash creates a terrain for us.  I set the scale and play around with the values.  I'm gonna drop in the material that I downloaded from the Megascan library.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_001.jpg

### Procedural Cliffs [1:08]
**Transcript:** Next I'm gonna use the Dash Curve tool and I'm gonna scatter some cliffs on it.  I type in the word Curve into the Dash toolbar and select the Curve tool option.  I set the minimum spacing to 60, then I click on the Start drawing button.  I draw the line on the ground.  As you can see, I can adjust the points of the Curve individually.  I have downloaded the cliff mesh.  Holding down Control, I drag it under the Curve and select scatter on selection.  Here I can adjust the test to rotate them 180 degrees on the Z axis, so the mountains face  inward.  I can drag the curve points anywhere and the scattered objects will follow.  I want to place smaller cliffs in front of the larger ones, so I do the same method again.  I will adjust the materials a bit, isolate the mountains and click on the Edit Material icon  on the Dash toolbar.  I give the McGreener tint and lower the saturation and brightness.  And then I also set the roughness to 0.2.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_002.jpg

### AI Tagging Assets [2:15]
**Transcript:** In the next step, I will show you the Dash AI taking system.  I tap Stag assets in my project, so I can easily search for them based on the tributes,  not just names.  I can already see two projects here, where I have completed the AI taking.  The advantage of this is that it's not necessary to migrate assets between projects.  They are accessible in a new project with the help of Dash.  And this project, I'll be using models from the Mission Terminerova Kitbush pack, which  you can get for free.  You can find the link in the description.  I also use some assets from the Science Level 3 pack.  As you can see, there are currently zero assets tagged.  I select the folders I want to tag and click on the Compute button to start the process.  This might take a while, so go and make a coffee or watch another Dash tutorial on our channel.  The asset icons have appeared in the Dash library.  Now I can search for properties.  If I type in the word Storage, it will show as a stack width storage, like this container.  I can also manually add text.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_003.jpg

### Placing Initial Assets [3:32]
**Transcript:** I select a few assets from the library and drag them into the scene.  I will set up an outpost here.  I can rotate and scale the assets with hotkeys.  Here you can see the combinations.  I want to place a few containers on these platforms.  I can simply do this by dragging them in and defining to stack a few.  I can do it manually by duplicating the items.  But here I want the largest stack of containers.  This is where I will use the grid scatter tool.  I type Grid into the Dash toolbar and select the grid scatter tool.  For both the grid origin and instance mesh, I use this model.  I add just a values here.  I can set the pivot point to the center by typing pivot and center into the Dash toolbar.  Next let's place some larger rocks into the scene.  I drag and drop a few larger assets I downloaded from the Megascans library and roughly position  them into the scene.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_004.jpg

### Scattering and Masking Assets [4:44]
**Transcript:** The next step is to scatter medium sized rocks across the area.  I select the terrain and while holding down Ctrl, I drag in the rock model and click on  the scatter on selection.  The surface scatter window pops up where I can set the parameters like size and density.  And now I'm going to draw a curve here along which I will mask out some rocks.  Setting the minimum spacing to 60, I click on the sole drawing and draw it roughly here.  You can edit and move this curve later.  Just drag it and the scattered objects attached to it will follow.  I select the rocks and in the edit window I scroll down to the proximity masking section.  Here I add my curve as an object.  I click on invert and enter a number for distance.  Now the rocks are scattered along the curve.  I actually want to have a path along the curve with no rocks.  In proximity mask 2, I add the curve again, set a distance and you can see a nicely masked  path appeared.  Wherever I move the curve points, the scattered objects will follow.  Now I select these few meshes and add them to the proximity mask 3 which will mask out  the rocks around them.  I will scatter another model across the ground.  I will use the noise mas...

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_005.jpg

### Physics Asset Placement [10:08]
**Transcript:** Now let me show you the dash physics tool.  I will scatter these two assets.  I type physics into the dash toolbar and select the physics tool.  A new bar pops up.  Let's make sure that the assets are set to dynamic and click on play to start the simulation.  Another great function of the physics tool is the paint function.  I selected this rubble pack from the Metascance library.  Holding down control, I drag them into the scene and click on place overlapped.  I place each version of the rubble pack into the scene.  I select all of them and click on paint to scatter them around the scene.  With shift plus the middle mouse button, I can adjust the brush size and by holding down control,  shift in the left mouse button, I can adjust the scattering density.  Now I simply scatter some rubble in a few places.  This building looks quite clean.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_006.jpg

### Scattering Decals [11:35]
**Transcript:** I will select some decals from the library by holding now shift.  And by holding down control, I will drag them onto the building.  Dash will scatter the decals on the selected surface.  I can adjust the scene randomly.  I will increase the scale.  Sometimes a few decals end up in the wrong place.  I can delete those.  I drag a few more decals manually onto the building.  Let's deal with the black flickering.  Simply enter this command.  And for lusher foliage, type in this.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_007.jpg

### Baking the Scatters [12:39]
**Transcript:** To create advantage of dashes that elements created with it are non-destructive,  you can adjust them anytime.  These scattered instances can be converted into individual meshes, allowing single object editing.  I think I'm generally satisfied with the layout, but in some places I like to delete or move a few objects.  For example, I want to bake these medium sized rocks.  I type bake into the dash toolbar and select the bake instances option.  I add the selected rocks with the plus button.  Dash has generated the individual objects from me, retaining the original scatter setup,  which we can hide or delete.  Now I can adjust the rocks individually.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_008.jpg

### Converting to Foliage Paint [13:22]
**Transcript:** I can do the same with grass.  I type foliage into the toolbar and select convert instances to foliage.  This way we get grass that we can edit with the classic foliage editor.  Now I will clean out some places.  I drop in a few more props around the outpost to make the area more lived in.  I will also scatter some decals here.  I bake the surrounding clips too.  I delete some of them.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_009.jpg

### Adjusting Materials [14:18]
**Transcript:** Next I will adjust the colors of the rocks.  I set the hue to 0.1 to get the greenish shade.  I decrease the saturation and brightness.  I do the same for the other rocks.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_010.jpg

### Atlases & Procedural Vines [14:33]
**Transcript:** Now let's talk about the dash wine tool.  It's available in the dash version 1.7.  I simply select the netless from the dash library.  You can make these available into dash library by downloading them in the standalone quick slow bridge app.  And by setting the download folder here.  I select the rock and by holding down control, I drag the addless onto the rock.  I choose the create wines on selection option.  And there we go.  I can set its parameters as a like.  I'll make it a bit longer.  I can set the scale of the leaves here.  For the material, I simply drag a 3 bar material onto the branches.  Creating a nighttime scene in Unreal isn't an easy task.  But they are plenty of tutorials on YouTube on this topic.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_011.jpg

### Adjusting the Lighting (UDS) [15:30]
**Transcript:** We can save a lot of time by using the ultra dynamic skyplug in,  instead of messing around with the built in lighting tools.  I have deleted all my light sources.  And I drag the ultra dynamic sky blue printed to the scene.  And now or seen is lit up again.  I set the time to midnight.  I set the night brightness to, let's say, 3.  For the exposure, I take in the instant exposure adjustment.  And I will enable while you're my trick folk also.  Now the scene is coming together.  I will brighten up this building a bit to make it more visible.  I will drag a rectangle to the top.  I will drag a rectangular light in.  It's important to turn off volume at risk scattering,  so the light source doesn't show up in the fog.  Tosel set the indirect lighting to 0.  Once we're done with this,  I scatter a few light balls that I modeled in Blender,  basically just a cylinder with two materials.  I add some flying particles to the scene.  I type in particle into the dash toolbar and select it.  I will also add some paddles.  I simply type water into the dash toolbar,  and it will generate the plane with the water material on it.  I will also drop in some smoke blueprints.  You can also find a l...

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_012.jpg

### Helldivers Characters [18:04]
**Transcript:** I find a very good helldiver and a bi-titan model  on the helldivers archive discord server.  Since these are Blender projects with Blender materials,  I bake a new texture for them,  which I will be using in Unreal.  I also animated the titan a bit,  which I exported to Unreal.  You can also find a link to the server down below.  I drop the titan into the scene.  It will be needed for the cinematic slater.  Now I drag a post process for you into the scene.  I set it to Unbound.  I play around with the values.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_013.jpg

### Playable Character [19:11]
**Transcript:** A center plays the player character with a helldiver model.  Met as plans tutorial to the great job of explaining the steps.  The link to the tutorial can be found below.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_014.jpg

### Adding and Adjusting Cameras [19:28]
**Transcript:** Now I want to create a few cinematic shots for the scene.  I will create a dash camera.  And I will set the aspect ratio.  I can adjust post processing and the color grading here as well.  Blume, FumeGrain, Fringe, and so on.  If I don't have a specific idea of what grade the shot should have,  I can choose a preset.  I choose this one.  We can also select an image from our computer and drag it into the dash toolbar.  The selected camera's color grade will take on the color properties of the image.  This is also a new dash 1.7 feature.  But let's stick with the pale greenish blue setting.  I will create another camera and I will set up another angle.  Here I just set the light beam to the background.  Here I just set the light beam to the background.  For the cinematic shots, I also add a few dash fog cards.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_015.jpg

### Adding Fog Cards [21:44]
**Transcript:** I type in fog and select it. I can easily adjust it.  I want a very faint fog just enough to be visible.  Under that, the scene is pretty much done.  I hope you find this video useful.  I had a lot of fun putting it together.  If you like this video, consider joining our Discord server or subscribe to our YouTube channel.  Thanks for watching and see you in the next one.

**Frame:** tutorials\frames\recreating-a-helldivers-2-game-environment-in-ue5-with-dash\frame_016.jpg


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
