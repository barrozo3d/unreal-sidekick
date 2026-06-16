---
title: Realistic Architecture Environment in UE5 - Dash Workflow
source: YouTube
url: https://www.youtube.com/watch?v=_9b_dabCpVE
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/realistic-architecture-environment-in-ue5---dash-workflow/
frame_count: 16
---

# Realistic Architecture Environment in UE5 - Dash Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=_9b_dabCpVE)
**Author:** Polygonflow Dash
**Duration:** 15m26s | 16 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction [0:00]
**Transcript:** Hello and welcome! In this video I'm going to show you how to use the Ashlandits features  to create an outdoor scene for aquids. I will cover the benefits of the new AI taking system,  how to use the scattering tools, edit materials and more. I'm Thomas Schneider and I'm going to be  your guide in this video. So let's go! First I got our some images for inspirational purposes  based on my ideas. I would like to create a modern house integrated with some older ruins in the  middle of a grasslandscape. I'm starting a new project and a new empty level. I open to

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_000.jpg

### Dash Content Library and Adding an HDRI [0:35]
**Transcript:** Dash Toolbar and click on the browse content library icon. Here I can find my download in  mega-scancer sets, other content from PolyAven and also my own assets but I'll talk more about  it a bit later. From PolyAven HDR library I select an HDR ID that I like, I have some favorites,  I choose one from those, I set the resolution and drag it into the scene. Now our space is  lit up. I create a simple house model with some placeholders that I will import into the project.  You can find it in the video description. I set the lighting by rotating the HDR ID.  I add a directional light into the scene and set its rotation to align with the HDR  sun. I drag in a post process for you. I set it to a mount and adjust the exposure.  In the Dash Toolbar I type in camera to create one. I roughly set up my composition

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_001.jpg

### Creating a Camera [1:54]
**Transcript:** and I adjust it a little. For this scene I downloaded a few assets from the epic market place  such as the rural Australian pack and the back yard packs 1 and 2. I've imported the downloaded

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_002.jpg

### AI Tagging Asset Packs [2:16]
**Transcript:** asset packs into the project. I can search for the asset I want to use but I need to know the name  of the asset or I can do some filtering by type for example I'm looking for aesthetic  mesh or material. This is where the new AI taking system comes in. This creates tags for the assets.  So I can search also for properties not just names. I click on the AI tagging button  which brings up the content browser. Dash the text all of the assets in my project. I click on  the compute button to start the process. This may take a few minutes.  All my assets are available, organized and ready to be easily dropped into the scene.  So let's search for some trees or I can search only for the red assets  or grain.  Also I can combine tags so let's search for chairs and the color orange.  Is that simple?  My next step is to create the grassland. I downloaded some vegetation from the Vegas cons library.

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_003.jpg

### Creating the ground [3:45]
**Transcript:** I quickly delete the placeholder  and use dash to generate the terrain. I adjust the parameters to my liking.  For this scene I generate the simple flat terrain.  I drop in the grass texture from the dash library and set the UV scale.  It's time to start applying materials to the building. For the windows I simply drag in the

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_004.jpg

### Adding Materials to the Building [4:30]
**Transcript:** glass material from the starter content. By default the glass should look quite bad.  If you want you can set the translucency to rate-raised for a better look.  I downloaded some 3D scans from the Megascans library as well. I want to generate some

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_005.jpg

### Creating Stone Walls with Grid Scatter [5:00]
**Transcript:** old crumbling stone walls to surround the modern building and drag this rock into the scene.  In the dash toolbar I type in scatter and I'm going to use the grid scatter for now.  After selecting my rock I click on the plus sign beside the instance mesh and also beside  the grid origin panel. Now I scattered my rock. I quickly set the parameters  and click on the random spin option for a more natural look.  And voila we have our stone wall.  Later on I scattered some plans on it which should break the repetition more effectively.  Now I duplicated a few times.  In most of my images we have overgrown vegetation so I placed the rock model next to the wall  and I'm going to scatter some bushes on it later.  A drop in the rock I used for the wall into the scene along with two other rocks.

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_006.jpg

### Dropping Stones with the Physics Tool [6:38]
**Transcript:** I will scatter them using the physics tool of dash. I type physics to the dash toolbar  and this brings up the physics bar. I select rocks and set them to dynamic.  I set every other object that I don't want the rocks to fall through to static.  With the rocks selected I click on paint. By pressing them both to shift and the middle mouse  button I can adjust the brush size and then by clicking the left mouse button I can paint some rocks.  I can adjust the position of the rocks by holding down the middle mouse button.

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_007.jpg

### Creating a Path [7:25]
**Transcript:** Let's create a path. In the dash toolbar I select the curve tool.  I set the minimum spacing between points to 50 then after pressing the start drawing button  I draw a curve freely by hand. I can also adjust the curve points individually.  I drag a mega scone model into the scene. I'm going to scatter it along the curve.  I make some quick adjustments to the material.  In the dash toolbar I select the path scatter option.  With the model selected I click on the plus sign, text the scatter and after selecting the curve  I press the plus sign next to the curves or you can just drag and drop it on the curve  that works either. I can adjust some of the parameters to my liking.  Now we have a road. I will scatter some rocks along it.

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_008.jpg

### Scatter along the Path [8:19]
**Transcript:** I select my terrain. In the content browser I select the desired elements then by holding down  control I drag them over my terrain. I click on the scatter on selection option.  I would like to scatter the rocks to appear only along the edge of the road.  To achieve this I click on the proximity mask 1, select the road and click on the plus sign.  The rocks disappear from the road. Now I click on invert and adjust the distance parameter.  After that I click on the proximity mask 2. I select my curve in the center of the road  and click on the plus sign. I adjust the distance parameter to mask out the rocks that we don't need.  I also adjust the density of the rocks.  I want to scatter another rock model in the same way. I apply the same method.  After that I scatter some vegetation along the road as well.  And in just a few minutes we managed to create a nice little road.

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_009.jpg

### Scattering Grass and Adjusting Proximity [9:51]
**Transcript:** Next I select some plants that I always scatter on the terrain creating a lush grassland.  Holding down control I scatter the plants and with the help of proximity masking I can select  where grass should not appear, such as on the road and under the building.  Let's see how the scene looks now with the path tracer.  As you can see, our vegetation is not visible in the background. I can fix this with two simple console

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_010.jpg

### Fixing Culling and LODs [10:31]
**Transcript:** comments. For now I will hide my grass.  I scatter some rocks around to fill up the space a bit.  Now I want to add some trees in the background.

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_011.jpg

### Scattering Trees on a Plane [11:00]
**Transcript:** In the dash prawn bar I type in plain, which generates a simple plain in the scene.  I scale it up and place it behind the building.  I always scatter some trees from the australian as I pack onto this plain.  Now I can easily move the trees around using the plain.  I will add a few more trees to the composition.  I will use the same method as the one I used to make.

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_012.jpg

### Scattering Foliage on the Stones [12:05]
**Transcript:** It's time to scatter some vegetation on the rock walls using the well-known method.  I want the bushes to only appear at the top of the wall.  I can achieve this with a height mask tool.  I will duplicate this for the other side as well.  And I repeat the process for the other walls too.  Let's add some bushes to the large rock as well.  Here a bit denser.  The vegetation completely covers this rock.  And I also want to place some plants in between the rocks.  I found the sky a bit boring, so I experimented with a few other HDRIs.  This one, with its nice blue sky and fluffy clouds, looks much better.  Let's draw in some props from the assets library and search for them with text.

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_013.jpg

### Adding Assets from the Content Library [13:31]
**Transcript:** I will also add some decals to our building, making it more interesting.  I will scatter some bushes on this rocky ground model to break up the grassland and make the ground more diverse.  I generated a mesh in blender with holes in it, which I will use to simulate the sunlight filter ring through the clouds.

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_014.jpg

### Color Grading & Final Result [14:44]
**Transcript:** Finally, I apply some color grading.  And after some adjustments, use my final result.  So that's it.  I hope you found some useful information in this video.  And if you like Dash, consider joining the Discord server,  where you can share your artwork and get fresh information about future updates. Take care, bye bye.

**Frame:** tutorials\frames\realistic-architecture-environment-in-ue5---dash-workflow\frame_015.jpg


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
