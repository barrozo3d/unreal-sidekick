---
title: GETTING STARTED WITH DASH - EASY WORLD BUILDING IN UE5
source: YouTube
url: https://www.youtube.com/watch?v=RA3yGbCvxIU
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/getting-started-with-dash---easy-world-building-in-ue5/
frame_count: 19
---

# GETTING STARTED WITH DASH - EASY WORLD BUILDING IN UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=RA3yGbCvxIU)
**Author:** Polygonflow Dash
**Duration:** 23m24s | 19 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hello, I'm Tamash from Polygonflow. I'd like to introduce you to the new features and changes in  Dash 1.8 through a couple of scenes. We will quickly create a procedure for a std at the  test or street corner and show how to easily blend and customize 3 Megascans materials.  So let's go!

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_000.jpg

### New UI [0:17]
**Transcript:** Let's get started with the new Dash UI bar. It has been completely revamped in Dash 1.8.  The most important tools are now instantly accessible from the menus.  This makes it easier to find and use the major tools as well as the smaller utility actions  available in Dash. But if you prefer the other search method, you can still use that too.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_001.jpg

### AI Assistant [0:39]
**Transcript:** Another cool new feature of Dash 1.8 is our new AI assistant. We have integrated  ChatGPT4 with our new documentation into Dash. So you can ask it questions in time.  Since the AI might not always have all the answers, you can access or updated documentation  anytime by clicking here.  Also, feel free to reach out to us on Discord if you get stuck. We will respond to your questions  as soon as we can. I have an idea of a scene I want to create and I've gathered some reference  images for it. I'd like to make a road passing through a forest. Let's ask the AI how it would  create the scene. Simply drag the image into the window and describe what you want to achieve.  The more detailed our description is, the more accurate responses we will get.  And here's the answer. So it suggests we first create a terrain and use the road tool to create  a path on it. After that, we should scatter vegetation across the terrain. As you can see,  it outlined a complete workflow for us. But let's not rush ahead.  I click and create in the Dash toolbar, then select the create terrain mesh under the comment section.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_002.jpg

### Terrain Tool [1:50]
**Transcript:** The new toolspanel pops up. In the future, I can easily switch between my active tools by clicking here.  And by the way, you can always open the toolspanel by clicking the edit icon up here in Dash.  I set up my desired parameters like scale and turbulence.  And I'm happy with my terrain. Let's see what the AI system recommends for the next step.  By clicking on the history, I can review my previous searches.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_003.jpg

### Road Tool [2:35]
**Transcript:** I should continue with my road, which requires a curve. I ask how to create it and hear the answer.  It's located under create curve tools.  Here we can just settings such as mode and spacing between the points we draw. Let's route that curve.  I can easily modify my point density later by holding down Ctrl and the middle mouse button,  then dragging the mouse left or right. Let's create the road. This can also be found under the curve tools  section. Click on create routes. After selecting my curve, I click on the plus button.  Here I can adjust the desired width as well as resolution and smoothness.  Currently, my road doesn't perfectly align to my terrain. I can fix this in the geometry setting section.  Under projection mask, I can choose where my road should be projected onto. But before selecting a  different mesh, I click on this spin icon to lock the current tool so that the road tool remains  open in the toolspanel. Then I select my terrain and click on the plus icon. After that, I also check the  full mesh option. I've created the base road mesh. My reference image shows that the markings are  located on the edges of the road. And I can address this with a simple method. ...

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_004.jpg

### Image Board [4:20]
**Transcript:** introduce dashes new feature to you. I click on board on the dash tool bar. This brings up the board  where I can drag my reference images. It's similar to Milano Tor Purif, but integrated directly  within the engine. The boards can be saved and will remain in the foreground throughout.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_005.jpg

### Road Markings [4:45]
**Transcript:** In order to have the road markings be easily adjustable, I will use the road tool again to create them  instead of using a road texture. I can save this setup as a preset by clicking on this icon.  This way, if I create a new road mesh along my curve, I can apply the saved settings to it.  I select my curve again and create a new road. After that, I apply the saved preset.  To better see what I'm doing, I need to add the material to my road.  By clicking on the content icon, I will open the dash content browser that lets you use the  free polyhave library, the free isle library, and also easily use your downloaded Megascans assets.  I choose the Megascans material and drop it on the road. I then reduce the width of my road.  Next, I will align the top mesh with the bottom one.  My reference image shows that the markings are located at the edges of the road,  and I can solve this for the simple method. Let's move the lines to the edges of the road.  I can do this with the path with section of the road tool panel. I simply set the number  out to duplicates, and I set how far a part they should be. If I want, I can also keep the center line.  This can be saved as a preset as well.  I ...

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_006.jpg

### Procedural Scattering [7:38]
**Transcript:** alongside the road, following the workflow outlined by the AI assistant.  I have downloaded a few plants I'd like to use. I select them from my content browser,  and by holding down control, I drag and drop them onto the terrain. I click on scatter here.  In the tool panel, I can adjust parameters such as density or the scale of plants.  The next step is to mask out the plants from the road. For this, I scroll down in the tool panel,  to proximity masking. I will select the road as the object, but before doing that, I click on the  pen icon to keep the current surface scatter tool panel open. I don't select the road, and adjust the  distance. I want the scatter plants to appear only near the road, not across the entire terrain.  So I invert the distance parameter and increase it approximately to the range where I want the  plants to spread. Then in proximity mask 2, I select the road again and remove the plants from the  road itself. I can save the proximity mask value as a reference, which can be applied to multiple  scattered actors, allowing me to control several scattered objects together, and save time.  I select the distance parameter, and by clicking on the icon next to it, ...

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_007.jpg

### Camera Tool [11:10]
**Transcript:** to compose my scene. I simply type camera into the dash toolbar and select the create camera  option. In the tool panel, I can adjust the aspect ratio, apply color grading, and use post-process  FX to replicate the look of my reference image. I need to adjust the trees a bit more.  If I want, I can choose the grading preset and tweak it accordingly to my needs.  Another cool feature of the camera tool is that I can either drag an image or use the dash image  port to extract the grading from an existing image onto my dash camera.  Two more things are missing from the image, the leaves alongside the road, and the fog in the  background. I've got a lot of leaves models from the Macaskan's library. I select them and  drag them over my curve. I choose the scatter here option, and dash automatically scatters the leaves  alongside the curve. I adjust the parameters to my liking and under parallel with. I use the  distance parameter to duplicate the leaves and spread them out along both sides of the road.  Next, I type a fog and search for the create fog card option.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_008.jpg

### Fog Card [12:40]
**Transcript:** I can freely adjust the scale, wind and other attributes.  After a bit of fine tuning, I first roll this complete.  As you can see, within a few minutes, we've blurred the foundation of the first road  and it's completely procedural. Whenever I move the curve points, the road and the forest follow seamlessly.  I made a few adjustments in the end, as you can see, I easily change the color grade and the  camera settings with dash. I have prepared the street corner scene. In this part of the video,

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_009.jpg

### Place Tools [13:32]
**Transcript:** I introduce the dash tools in the place menu and show how to quickly add a lot of detail to  the scene. Let's take a look at the select tools. These can significantly speed up your workflow.  I will select this trashcan, and by clicking on the select nearby, dash will automatically select  the surrounding assets. Toften happens that after a long rendering, I noticed that an asset is not  aligned correctly with the ground and it's floating in the air. The project below option solves  this issue by aligning the selected assets to the ground. If you want to randomize the placement  of our asset, the random swap tool can help us. From this menu, I can easily adjust the pivot  point of each asset.  We can also randomize the parameters of the assets, such as their scale and orientation.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_010.jpg

### Transform Tools [14:27]
**Transcript:** Now, I want to quickly fill this scene with content and details. I have downloaded an asset pack

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_011.jpg

### AI Asset Tagging [14:34]
**Transcript:** from the app market place. These assets are not yet available in the dash content browser,  but I can easily fix this by using the dash AI tagging system. I select the current project option.  Here I find the location of the asset pack. I select the folder that I want to import. I can choose  whether I want AI tags for the assets or not. I check the box to enable AI tagging and click on  the compute button. As I mentioned in the first part of the video, the dash AI tagging system  signs tags to the assets, making it easy for me to search through them. Once the tagging process  is complete, I can right click on the asset to see its properties. I can see that this asset has  a lot of tags now. Dash recognizes asset based on its appearance. I can also add my own tags to the  assets if I feel some importance tags are missing or if I want to categorize together some assets  under one tag. Additionally, I can search for assets with a similar look and properties. Let's  search for something using a keyboard. I type in the word container as it starts to show up,  but I can also search for color.  Or even combine tags. I search for a few bottles and show you how to fill up the trash cans wi...

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_012.jpg

### Physics Tools [15:45]
**Transcript:** I select a few and drag and drop them into one of the bins. Under the previously used place menu,  I select the physics drop command. The selected assets fall into the bin, then I duplicate them  until they start spilling over the top. If I move one bottle, it affects the others,  allowing me to arrange them as I like, but maybe I don't need so many bottles.  This should be enough. I select a few bottles and adjust them to create a composition.  Using the physics drop tool, they fall to the ground.  I want to quickly fill my scene with large piles of rubble and trash to add more details.  I asked the AI assistant for a recommendation on how to do this. I type in my question.  The AI suggests using the physics paint tool, so let's go with that. I can find it under the place menu.  When I click on it, dash indicates that no assets are selected for scattering.  I could drop in some assets to the scene, but I will use another method. Here, I choose some assets  from the content browser and drag them into my scene by holding down control. I select physics paint.  By holding down shift, controller, and the middle mouse button, I can adjust the size of my brush.  I paint a few piles of ru...

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_013.jpg

### Decal Scatter [17:28]
**Transcript:** and while holding down control, just drag them into the scene. Then choose scatter here.  In the tools panel, I can set how many decals I want and how densely they should be scattered.  With the tools I have shown so far, we can create detailed scenes extremely quickly,  but in the next part of the video, I demonstrate how to maximize the potential of what dash offers.  In the third part of the video, I will showcase the material blend tool of dash.  I created a terrain from the create menu.  I make sure it has a high subdivision for an night displacement later.  I think I'm satisfied with it, and I click on this icon to bake it into a static object.  I will enable the night support for the mesh.  I will type the night into the search bar and select actor enable the night.  If you need help, you can always get the information into the dash documentation.  For example, I can search here for displacement.  I also activate the test selection in the project by typing it into the search bar.  I downloaded some materials from the Megascan library.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_014.jpg

### Blend Material [18:55]
**Transcript:** I select three materials, and by holding down control, I drop them onto the terrain.  I choose the apply blend material option.  I click on the edit button, then select edit blend material.  First, I'm going to set the global tiling.  I can adjust which material I want to be in the foreground.  I will create a muddy terrain with some puddles.  I tweak the wetness and displacement a bit.  Here, I can adjust the snow.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_015.jpg

### Snow & Rain Layer [19:34]
**Transcript:** And I can imitate rain drops on the terrain.  I want the mood of an early winter morning, where the melt, snow and mud have frozen.  As you can see, I can make a very detailed blend.  I think this ground is a perfect base for a medial scene.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_016.jpg

### Building an Environment [20:07]
**Transcript:** I'm using a few assets from the Medieval game environment pack,  which I downloaded from the epic market place.  And I start to create the environment.  Let's start with setting up the camera.  Under the create menu, I select the create camera, and set the aspect ratio on focal length to my preference.  Next, let's continue with the gravel path.  I draw a curve, and scatter a megascan gravel assets on the terrain.  I use the curve in the proximity masking section and create a two-laying gravel path.  I bring a wooden post into the scene.  Then, from the scatter menu, I select the path scatter option.  In the curve section, I add the path curve, and for the scatter, I select the wooden post.  I arrange the asset into rows.  Then, I play with the density and the random rotation.  I also scatter some foliage around the buildings.  I can also add snow on top of objects in the material tool panel.  I scatter some megascans trees in the background.  I've also done some cliffs and scattered a few rocks.  Now, for the final details.  I can easily choose some assets from the content library.  I use the physics tools from the place menu.  I want to make the scene fogier.  I select the create...

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_017.jpg

### Outro [22:24]
**Transcript:** And there you have it.  We have discovered the biggest new features in dash 1.8.  We export the new dash UI bar or revamped documentation,  the new AI assistant and the dashboard.  I demonstrate it how you can easily access or frequently use the word building tools,  such as the road tool, the physics tools, and how to use the dash blend material tool  to create more detailed environments.  If you enjoyed this video, try out dash for free.  Join us on our Discord server where you can showcase your creations.  Thank you for watching.  See you in the next one.

**Frame:** tutorials\frames\getting-started-with-dash---easy-world-building-in-ue5\frame_018.jpg


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
