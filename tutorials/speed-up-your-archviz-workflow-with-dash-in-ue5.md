---
title: Speed Up Your Archviz Workflow with Dash in UE5
source: YouTube
url: https://www.youtube.com/watch?v=cC0l3yZMt3M
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/speed-up-your-archviz-workflow-with-dash-in-ue5/
frame_count: 16
---

# Speed Up Your Archviz Workflow with Dash in UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=cC0l3yZMt3M)
**Author:** Polygonflow Dash
**Duration:** 14m47s | 16 section(s)

---

## Raw Data (for Claude Code extraction)


### <Untitled Chapter 1> [0:00]
**Transcript:** Hello and welcome!  In this video I'm going to show you how to use Dash and its features in Unreal, creating  a realistic in their scene.  I will cover the benefits of the new Poly Heaven integration, how to use Physics Tool,  Edit Materials and more.  I'm Tomasz Nod, S3D Artist from Budapest Hungary, and I'm going to be a guide in this video,  so let's jump in.  I made a kitchen model in Blender without any complex interior.  It only includes a few main furniture pieces such as cabinets, a counter and a bar stool.  Let's drag and drop the models into the scene.  As you can see, the objects have no material.  The scene also lacks lighting.  I will easily fix this by illuminating the space with an HDRI image, which I will simply

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_000.jpg

### Lighting the Scene with Free Poly Haven HDRI [0:50]
**Transcript:** drag from Dash into the scene.  I click on the Dash icon, which brings up the toolbar.  Here I click on the browser icon.  Assets from Poly Heaven are now integrated into Dash, so you can easily drop assets into  the scene without the need of downloading them separately from the Poly Heaven website.  If you're not familiar with Poly Heaven, it's a publicly founded asset library featuring  textures, HDRIs and 3D models all available for free, suitable for every purpose.  As you may have already noticed, your download and mega scan assets are also here.  Let's look for an HDRI, an autumn landscape will be perfect for this scene.  I can choose the resolution I like and simply drag it into the scene.  We have now created an HDRI backdrop.  It was that easy.  I can adjust its intensity and transfer mid-design wish.  Let's add a post process volume to the scene.  I set it to Unbound and adjust the exposure as well.  I've created a simple glass material too.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_001.jpg

### Creating a Glass Material [2:17]
**Transcript:** Here you can see how it looks.  Let's make a prefab and drop it into the scene.  Maybe I tweaked the exposure a bit more.  Now let's focus on the materials.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_002.jpg

### Adding Materials from Megascans [2:42]
**Transcript:** I open dash again and I will drag a wooden throw material into the scene that I downloaded  from the Megascans library.  I adjust a few parameters like saturation, roughness and brightness.  I will repeat the same process for each object.  And a little tweak on the exposure.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_003.jpg

### Adding a Light Source [3:40]
**Transcript:** I'm creating a simple light source above the scene.  I will create a cube, scale it and place it under the cabinet.  It will receive an emissive material.  This is how the room looks now with the bathroom.  Let's set up a camera.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_004.jpg

### Using DASH to set up a Camera [4:05]
**Transcript:** I type camera into the dash toolbar and I select the create camera option.  I set it settings like exposure, sensor, focal length and also just camera's location.  I'm currently setting it with this angle.  It's time to fill the space with more smaller objects.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_005.jpg

### Adding Props with DASH Physics Tool [4:31]
**Transcript:** I want a bunch of fruits on the counter, preferably in orange tones, which I think will go  nice with the green tiles.  I drag in an orange.  I use the dash physics tool which will be very useful for this scene.  I type physics into the toolbar and select the physics tool.  With the orange selected, I click on the complex button, set the asset to dynamic and start  the simulation.  I duplicate a few fruits on the top of each other.  This can be repeated as many times as needed until I'm satisfied with my little pile.  I continue populating the space with more vegetabus and fruits, utilizing the physics tool  to make the fruits naturally fall into the counter.  I sprinkle in some knots as well.  I can also manually adjust the composition.  I drag in the point light to make the fruit pipe out a little more.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_006.jpg

### Adding Additional Lights [6:37]
**Transcript:** Currently, I'm not overly concerned about how my lights behave outside the camera view.  I throw in a few more objects, taking advantage of the polyhave and model library.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_007.jpg

### Adding Free Poly Haven Assets with DASH [7:26]
**Transcript:** I place a rectangular light in the scene, simulating an overhead light above the counter.  Much better.  This is how our image looks currently.  I tweak the composition a bit more until I'm completely satisfied.  The current camera view is done, it's time to create another one.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_008.jpg

### Adding Multiple Camera Views [9:23]
**Transcript:** The space feels a bit empty, so I'm bringing in a few models to make it look more lived

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_009.jpg

### Adding Pots and Plants [9:50]
**Transcript:** in.  I'm starting with some larger potted plants.  For this particular model, I've simply deleting the original plant and replacing it with  a little more.  Let's add some decals to break up the space a bit more.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_010.jpg

### Adding Megascans Decals using DASH [10:58]
**Transcript:** I'm also obtaining these from the Megascans library.  Using dash makes it much easier to handle decals.  And a few books can also find a place here.  Let's move on to the camera post processing.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_011.jpg

### Adjusting Camera Post Processing with the DASH Camera Editor [12:02]
**Transcript:** I can set the post process effects in the dash camera editor.  I can easily set up bloom, fringe, temperature and other effects.  Let's set up a level sequence.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_012.jpg

### Creating a Camera Sequence [12:20]
**Transcript:** I create a new sequence and give it a name.  I drop in the camera I want to render.  After that, I create a short animation and set the frame rate to 25 FPS.  I set the keys to linear to achieve a consistent motion.  I've also created a third camera view with a larger focal length.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_013.jpg

### Time to Render using Path Tracer [13:01]
**Transcript:** It's sent to render.  But before I do that, let's set up the path tracer in the post process volume.  The most crucial step is to disable the denoiser since we can't fine tune it.  In addition, these are the settings I've used.  I open the movie render queue.  I select the sequence I want to render, then clear everything in the settings.  What I need is anti aliasing, path tracer, a excel extension and game overrides for the  best image quality.  I set the resolution in 4K and set the folder where the render images should go.  Before I forget, I check the override anti aliasing option and set the sample count as well.  One solid is done, it's time to start the render.  And once again, here's the final result.  I reduce some noise in the Vintage Resolve and add the layer of dust, but that's it.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_014.jpg

### Final Result [14:10]
**Transcript:** As you saw, we've done from a set of basic objects, the photorealistic interior scene  with the half of dash.  Hope you find some inspiration in this video and if you like dash, join this card server  where you can share your creations and get fresh information about future updates.  Take care, bye bye.

**Frame:** tutorials\frames\speed-up-your-archviz-workflow-with-dash-in-ue5\frame_015.jpg


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
