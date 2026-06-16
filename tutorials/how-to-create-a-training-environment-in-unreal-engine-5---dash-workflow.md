---
title: How to create a training environment in Unreal Engine 5 - Dash Workflow
source: YouTube
url: https://www.youtube.com/watch?v=rBcGl_ScDKs
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow/
frame_count: 10
---

# How to create a training environment in Unreal Engine 5 - Dash Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=rBcGl_ScDKs)
**Author:** Polygonflow Dash
**Duration:** 14m1s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction [0:00]
**Transcript:** Greetings. I'm Jonathan. Polygon flows community director for Dash, our next gen Unreal Engine  plugin that makes creating environments like this a total breeze.  Today I'm demonstrating a mount site inspired by reference photos from Camp Shelby in Mississippi.  Mount is an acronym that stands for Military Operations in Urban Terrain. This style of  architecture is found mostly on training sites or airsoft courses, but today we're using  it to demonstrate how effective Dash can be in creating realistic training environments  for real-time simulators using Unreal Engine 5.  I've worked in this industry before, and this level of detail would have taken me a long  time. With Dash, the scene creation time was reduced to hours instead of days, letting  me focus on building the world to look like a one-to-one representation of the real thing  in short order.  The buildings themselves were modeled outside of Unreal Engine. If you'd like to work  with them yourself, you can download them from the link in the description. The driving  force behind this environment is Dash and the speed at which it allows me to create open  worlds. Look at the difference when all of the Dash created assets a...

**Frame:** tutorials\frames\how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow\frame_000.jpg

### Terrain Creation (Terrain Tool) [1:14]
**Transcript:** I'm going to recreate this environment but leave the buildings in place, then work with  Dash to flesh out the world so that you can follow along with me.  Let's start by typing terrain into the Dash prompt bar, then select the terrain tool.  Here's a wide variety of options to work with here. I'm going to adjust the terrain so  that it's large enough to fill the visible world. Other settings that I'll adjust will  change the density of the UVs and the height of the noise in the terrain.  Once I'm happy with the final look, I'll convert the terrain to a static mesh using Dash.  Converting the terrain to a static mesh significantly improves performance.  Open the content browser and drag an appropriate material to form the bedrock of the environment.  Inside the edit material panel, I'll adjust the normal, contrast, brightness,  and saturation of the surface to match the type of soil that I want to use for the world.

**Frame:** tutorials\frames\how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow\frame_001.jpg

### Road Creation (Road Tool) [2:13]
**Transcript:** I'll move on to adding the main roadway that traverses the mount site. I'll type draw and  dash and begin drawing out an adjusting curve until I'm happy with the general shape of the  road path that I'm laying out. Then type road into Dash and select the road tool.  From there, I'll add the curve to the tool so the road appears, then adjust the density so  it's got enough geometry to follow the general shape of the curve and adjust the width to  represent the size of a typical mount village roadway. After I'm happy with how it looks,  I'll add the terrain to the road tool so that the road conforms itself to the shape of the terrain.  Then I'll adjust the border sink so the road has a sharp edge and use the sink option to make  it rise above the ground just a little. Once this is done, I'll adjust the UVs and then find a  material to add to the road that I'll work for demonstrating a quick concrete layout. Then open  the content browser and search for a concrete material from Megascans that will work well here.  With the concrete material on the road, I need to adjust it to get rid of the bluish tint that it  has by default. So I'll desaturate it using Dash's material editor and cha...

**Frame:** tutorials\frames\how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow\frame_002.jpg

### Grass, Weeds, Debris, & Tree Scattering (Surface Scatter) [3:46]
**Transcript:** To make the terrain more realistic, we need grass. In the content browser, I've selected Megascans  grass clumps and held control while dragging them onto the terrain to scatter them quickly  across the ground. After playing with some scale and density settings, the next step is to select  the road mesh and enable object masking so the grass doesn't grow in the roadway.  Object masking takes a moment or two to calculate, and the grass disappears and we're left with a  clean road. To make the grass more interesting, I've scattered clover and tall metal grass as well,  using similar techniques to break up the environment.  Laying down several types of ground cover will help with breaking up repeating mesh elements  and introduce believability to the world, and with dash it doesn't really take much time at all,  and every aspect of the scatter process is procedural and can be changed at any point.  Because dash is procedural, you can select an existing dash created asset and open it at any point  to adjust it how you see fit. The last bit of surface scattering we need to focus on is rocks,  which will make the road far less uniform and way more interesting. I've opened the content  br...

**Frame:** tutorials\frames\how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow\frame_003.jpg

### Sandbag & Weed Placement (Path Scatter) [6:57]
**Transcript:** Megascans library into the world, then creating a gentle curve with a low amount of interpolation  so I can easily adjust the points if needed. Once I'm happy with the curve, I'll type path  into Dash and select path scatter, then add the curve to the tool, and select the sandbags,  and add them as well. The scaling needs to be adjusted to look like a sandbag wall, as does the  density. Path scatter takes the input assets and distributes them along a curve, which is great for  building fences and other physical barriers. One of the really nice aspects of Dash is that  anything that you do is taken into account, so I'm going to adjust the end points of the curve to  clean up the final appearance and make the sandbags stop colliding with the buildings.  Let's add even more detail to bring it to life. I'll draw more curves to lay out where I want  weeds to grow, approximating where they would be most likely to thrive in the world, then I'll find  some weeds in the Megascans library and home control and drag them into the world and scatter them  on the selected paths. The scaling here needs adjusting, as does the density and rotation,  along with a few other settings like the width and...

**Frame:** tutorials\frames\how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow\frame_004.jpg

### Utility Poles & Cables (Path Scatter, Cable Tool) [8:21]
**Transcript:** and held control while dragging the mesh into the world to scatter it on the curve. This automatically  creates a path scatter, which needs some adjustments to make a convincing procedural placement.  I'll adjust the Z direction override to get the poles oriented in the same direction,  then adjust the width so that Dash creates two copies of the poles for each side of the road.  Then adjust the remove mask parameter to randomize where the poles appear,  and adjust the seed parameter until I've got to look that I'm happy with.  You could do this manually with Dash, but you'd also lose a lot of the ability to adjust the  position of the assets based on the location of the curve.  The utility poles need cables added to them, and Dash has a tool for that aptly named the cable  tool. This tool will take a bit of setup. I've placed hidden spheres on top of the ceramic  insulators of each utility pole, so I can connect them one by one to ensure that the power lines  are linear and look realistic. It takes a minute or two, but the end result is solid and true to life.  If you want to push your simulated environments to the next level, Dash brings fidelity and  performance to real world tr...

**Frame:** tutorials\frames\how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow\frame_005.jpg

### Physical Fitness Site (Grid Scatter) [10:29]
**Transcript:** car tire by dragging the tire into the environment, placing it in an open patch of dirt,  then creating a new grid scatter with Dash. Adding the tire to the grid origin and as the input mesh,  you get an instant grid of the tire repeating itself. This can be adjusted with a variety of  different options in grid scatter, including scaling, rotation, height, etc. Until I'm happy with  the final look, which requires a bit of adjustment. But ultimately, significantly less than the amount  of time it would have taken to place these assets manually. Let's showcase how to take these

**Frame:** tutorials\frames\how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow\frame_006.jpg

### Building Weathering (Decal Scatter) [11:11]
**Transcript:** buildings and give them some character with decal scatter. Prompting Dash to open decal scatter,  I'm selecting all of my decals that I want to apply to the buildings, and now I've loaded them  into the tool. I'll cut to the buildings that need detailing and select the first one and add it  to the tool. This automatically applies a larger sort of selected decals to the building, but we  can go further with it by limiting how far the decals will apply based on the height of the building.  And also prevent the decals from creating stretching by adjusting the depth.  Adjusting various other parameters results in a really nice looking random assortment of  battle scars and damage that would accrue over the years that this site existed. We can also add  other buildings to the scatter and change the max count of the decals, so it equally applies  decals to all of the selected buildings. It's a very versatile tool that should open up a lot of  customization for you, like everything in Dash. It's totally procedural too.

**Frame:** tutorials\frames\how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow\frame_007.jpg

### Building Materials (Material Editor) [12:07]
**Transcript:** I was also able to get the precise color that I wanted from my materials using the Dash  Material Editor, which made it very simple to get a quick material change when I needed it.  Similar to what I did earlier with the road by adding dirt, I can also basically change any  aspect of this material inside of Dash entirely procedurally.  Another aspect of Dash is the content browser that lets you load in assets from other

**Frame:** tutorials\frames\how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow\frame_008.jpg

### Unified Content Library [12:37]
**Transcript:** Unreal Engine projects that you've tagged on your machine using Dash. This fence I'm using was  originally designed for a recreation of Deus Ex's Hell's Kitchen, but because I tagged the project  in Dash, I can load the assets into this environment seamlessly. This is a huge time saver, especially  if you've got a lot of additional content outside of your main project that you're working in.  If you'd like the buildings to work with for your own projects, you'll find them in the description  so that you can follow along with this Dash tutorial. I'm Jonathan, Polygon Flows Community Director  for Dash, and I thank you for watching. Be sure to let us know what you think on our discord  server and in the comments section below. If you want to learn more about Dash, also be sure to  check out our library of how-to videos, featuring deep dives in the various aspects of the tools that  Dash offers. See you next time.

**Frame:** tutorials\frames\how-to-create-a-training-environment-in-unreal-engine-5---dash-workflow\frame_009.jpg


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
