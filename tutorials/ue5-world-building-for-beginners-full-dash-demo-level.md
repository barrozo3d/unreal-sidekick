---
title: UE5 WORLD BUILDING FOR BEGINNERS – FULL DASH DEMO LEVEL
source: YouTube
url: https://www.youtube.com/watch?v=bxeocONsu1Y
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/ue5-world-building-for-beginners-full-dash-demo-level/
frame_count: 19
---

# UE5 WORLD BUILDING FOR BEGINNERS – FULL DASH DEMO LEVEL

**Source:** [YouTube](https://www.youtube.com/watch?v=bxeocONsu1Y)
**Author:** Polygonflow Dash
**Duration:** 22m55s | 19 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hello, I'm Tomas from Polygonflow and today I'm excited to show you a new Dash demo scene.  You can download this scene yourself to experiment with the pre-made tools and learn the basics of Dash.  You can find the link down below.  In this video we will go through each part of the scene and I will show you how I created it  and how you can customize it further. So let's start with the quick recap.  Dash is a worldbuilding tool for Unreal Engine 5 that contains a lot of features  all designed to make it easier to build environments. Let's start with my favorite one,

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_000.jpg

### Physics [0:32]
**Transcript:** the physics paint. So here we get a pile of bottles which would be very time consuming to place  by hand. Luckily, Dash got a tool that's perfect for placing objects realistically.  To use it, select your preferred assets in the scene and start the physics paint from the  place menu in the Dash toolbar.  But you can open the Dash Content Browser which has integrations with a few asset libraries  such as Fab and then Holes Control and drag and drop your preferred assets and you will see  the physics paint option.  Next, we have the Paths Cutter, one of our scattering tools. This one is based on a spline,

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_001.jpg

### Path Scatter [1:19]
**Transcript:** as you can see here when I move the spline points around. To edit an existing tool like this,  simply click the Add it button, open the Tools panel and then select your scatter output  and it will auto-open in the Tools panel. If it doesn't, make sure you don't get another tool  already pinned in the Tools panel with this little pin icon. And you can also open the  full list of active tools with the button in the top left in the Tools panel.  To recreate this Paths Cutter, let's start with drawing a curve with a draw curve action.  Then select your curve and find your preferred assets in the Dash Content Browser.  Drag and drop one or several assets while holding Control and select scatter and selected.  And now you will see that the Paths Cutter has been created and you can continue to tweak it in  the Tools panel.  If you want another Paths Cutter with another asset, just repeat the same process.

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_002.jpg

### Surface Scatter [2:45]
**Transcript:** Our next tool is our most used one, Surface Cutter. With this you can scatter anything  randomly on any surface, perfect for our natural environments. To create this, you can follow  the same drag under a procedure from the Content Browser as the used with Paths Cutter.  Or you can simply open a new Surface Cutter from the scatter menu or from Search,  and then assign your Surface and your scatter assets.  If you want to use several scatter assets, you can either create several Surface Cutters and  get full control of each or just create one Surface Cutter with several scatter assets.  In the later case, you can control the density of each respective asset from the scatter table.  Surface Cutter has many powerful sayings and masks in order to give you full creative control,

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_003.jpg

### Proximity Mask [3:58]
**Transcript:** but the common one is the proximity mask, which lets you assign objects and then control how the  scattering behaves around those assets. So if I move this object here, you can see that my  footage adjusts as well. To use this mask, simply open your Surface Cutter,  and assign one or several objects as proximity objects,  and then control the distance with and so on. You can also invert it.  Next up, we have Grid Scatter, which lets you scatter objects in a grid-like pattern,

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_004.jpg

### Grid Scatter [4:54]
**Transcript:** perfect for more structure scattering. And of course, you can adjust a lot of settings with  Grid Scatter as well. For example, you can also use proximity mask to remove certain parts of  this rock structure. To recreate this, simply open Grid Scatter from the scatter menu.  Assign your Argin actor and your scatter objects, and then start experimenting with all the  different settings such as width, depth, and height.  Then we also got a tool called Radio Scatter, which rocks very similar to Grid Scatter,

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_005.jpg

### Radial Scatter [5:56]
**Transcript:** but its scatters in a circular pattern instead. And here we have also decided to use Surface  Cutter on this Radio Scatter. To recreate this, open Radio Scatter from the scatter menu,  assign your scatter object, and if you want, also an Argin actor in the position category.  Then start adjusting the settings to get a good look, for example the count, radius,  and the concentric rings.  Then at any point you can select your Radio Scatter output, open the dash content browser,  hold CTRL when drag and drop in one or several assets, and then choose scatter on selected to  get some vegetation on your Radio Scatter.  And here's a good tip for you. If you have created something cool with one or several scatter tools,  you can select all the outputs, and then use the Merge Actor action in the search bar to generate  a reusable static mesh out of these scatters.  Next one is the first of our procedural mesh tools, the Cable Tool. This tool lets you create

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_006.jpg

### Cable Tool [8:19]
**Transcript:** procedural cables between one or several objects, such that when you move the objects,  the cables suggest accordingly. As always, there are tons of settings to adjust the result,  for example the radius, the amount of duplicates, and the gravity.  To recreate this, open the Cable Tool from the create menu or from the search bar,  and then just assign your objects and start customizing.  The next tool, the mesh pattern, is one of our latest tools.

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_007.jpg

### Mesh Pattern [9:13]
**Transcript:** This lets you create procedural, tie-able patterns, for example this floor or this wall.  Here you can adjust important settings such as scale, padding, or noise.  To recreate this, open mesh pattern,  assign your surface object, and then choose among the large list of included presets,  or create your own by adding your own pattern objects.  And here I also wanted to mention another of the supported libraries in the Content Browser,  the Amazon Berkeley Objects. This is a huge collection of high-quality,  regalverts 3D models, all available for free.  So for example, let's search for a couch, and then drag and drop it into the scene.  If you are not happy with the material of NES sets from the supported libraries and  dash content browser, we have made it incredibly easy to adjust it.  Simply select your asset, for example this couch, and then open the active tools list in the tools  panel, and you can open the material editor tool for this selected asset. Here you can adjust a ton  of texture settings very easily. The next procedural mesh we got is the piped tool.

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_008.jpg

### Quick Pipe [10:57]
**Transcript:** This creates a procedural pipe around the curve, so when you move the curve, the pipe adjust  accordingly. To recreate this, you can use any curve, and then assign it with a newly created quick pipe.  10. The most important setting is probably the radius, but of course there are a lot of other  settings as well. For all the dash procedural meshes, it's important to know that they all  use custom dash actor. So before you build your game or share this level to anyone without dash,  you should convert the procedural meshes to static meshes. You can do this either with the  big button in each tool, or by selecting the output and drawing the big mesh action from the search  bar. But remember, this action is non-reversible, so don't do it before you are happy with the results.

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_009.jpg

### Road Tool [12:04]
**Transcript:** Next up, we got the roll tool, which is also a procedural mesh. But here we have also combined it  with the surface cutter and the puffs cutter to get the nice looking combined piece. As all of  these tools are procedural and connected, you can then move the curve used by the roll tool to  adjust the complete piece, or for example adjust the roll width and see everything adjusts accordingly.  To recreate this piece, let's start by creating a curve. Then open the roll tool, and when you assign  the curve, you will see a road has been created along it. Then we can adjust some roll settings  and design a road material.  Then to get the scatter ring around the road, we start off by scattering with surface cutter on the floor.  Then we scroll down to the proximity mask in surface cutter,  make sure the pin icon is enabled to avoid accidentally switching tools,  and then assign the road mesh as a proximity object.  And now we can control how close the scatter comes to the road with the distance setting,  and also how far away the scatter reaches with the width setting.  Then for the puffs cutter, we use the same curve as with the road tool,  and then use the parallel of these settings to...

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_010.jpg

### Advanced Water [14:20]
**Transcript:** dash also includes a few blueprint tools, first up being the advanced water tool.  This is a water volume where you can adjust the water planes color, waves,  but also the underwater properties such as the caustics and blurriness.  To recreate this, simply search for water in the search bar, or find it in the create menu.  Then you can place the water volume anywhere you like, and customize its settings.  If you need to reopen a closed water plane tool, simply add the toolspinal open,  and then select your water plane.  Our next tool is a real fun one. The wine tool lets you create wine branches with scatter

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_011.jpg

### Vine Tool [15:18]
**Transcript:** leaves on any surface, and as it is procedural, you can move the rock or the origin actor,  and everything adjust accordingly. As many other tools, it has lots of customizations,  but the main one is definitely the growth iteration.  To create this, you have three options. The first option being the open wine tool from the  dash toolbar, and then assigning a surface and an origin actor. This method uses or default leaf,  but you can of course assign any mesh in the leaf mesh container.  The second way of creating wines is to use a draw wine section from the dash bar.  Once you are in draw mode, you can draw a curve and have the wines be created along the curve.  Another way to create wines is possible if you have some atlases from Quixel Bridge.  Then you can open the Quixel Odd Library in the dash content browser, and select an atlas  of yours, and drag and drop it onto your surface while holding Ctrl, the CD option,  create wines selected. This way you use the selected atlas and create wines on your surface  instantly. One of the most liked features of our material added tool is the ability to use

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_012.jpg

### RVT [16:45]
**Transcript:** RBT to blend the assets with the surfaces, like here where we have blended a rock with our sand  surface. If I decrease the slope setting, you can see that the sand on my rock decreases.  To use this, there are a few key things to know. First, you have to have virtual textures  enabled in your project. Secondly, it only works with the assets from the supported libraries in the  dash content browser. For example, Megascans from fab, and finally the surface can be either a UE  landscape, a dash terrain, or a plane, but the surface can't have the night enabled. Then when you  have your supported asset placed on your supported surface, you can select both of them and run the  RBT action in a dash search bar, which will create your RBT volumes. Then all you have to do is select  your rock and in a tools panel, open the list of active tools, and then just enable and adjust the  virtual texture effect. On a similar note, we also have a blend material tool in the ash.

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_013.jpg

### Blend Material [17:55]
**Transcript:** With this, you can select three supported textures from the content browser and blend them together.  And this tool also includes layers for puddles, rain, and snow. Recreating this is super easy.  Open the content browser, select three supported textures, and drag and drop them while holding  control to your surface and then choose create blend material. Once created, you can open the  blend material tool by selecting the surface and finding it in the active tools list.  And here we have our folk card tool. This lets you create a nice looking folk card,

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_014.jpg

### Fog Card [18:32]
**Transcript:** which you can then move around and customize to match your environment. Super easy,  but it can give great atmospheric depth to your scene. To edit it, open the tools panel,  and simply select the folk card actor. You can add the folk card tool from the create menu or from search.  On the subject of atmospheric tools, we also got our following leaves tool that lets you create and

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_015.jpg

### Falling Leaves [19:05]
**Transcript:** control an actor that spawns falling leaves. This can also be added from the create menu or from  search and then controlled from the tools panel as always.  And as a small bonus here, we used our decal scatter tool to scatter some relief decals on the  ground. This tool can be found in the scatter menu or be used directly from the content browser.  We got two tools left, the first being or rain tool. It is very similar to the fallen leaves tool,

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_016.jpg

### Rain Fall [19:58]
**Transcript:** but instead of leaves it creates falling rain and is a bit more advanced. And to get a really  nice scene, we also wanted to showcase the rain effect for material edit and blend material tool.  So if you have placed a sported asset like this rock, you can select it and from the active  tools list in the tools panel, you can open the material edit. If you scroll down here,  you will see some extra layers like dirt, snow and rain. In the rain settings, you can add dripping  droplets and ripples.  And if we select the ground surface where I have applied the blend material,  the B layer is for puddles and the T layer is for rain.

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_017.jpg

### Snow Fall [21:09]
**Transcript:** And at last but not least, we got our snow tool. This works just the same as the rain for a tool.  And here we have also added some snow to a rock through the material edit tool.  And the cool thing with the snow is that it uses displacement as you increase the amount of snow.  But of course this only works if you have enabled the night on the rock, which you can do by selecting  the rock and running the night comment into their search bar.  So and that's it for today. I hope you enjoyed seeing me going through a bunch of different  dash tools and don't forget that you can download this demo level, create a free trial and explore  these tools among with the rest of the dash tools for yourself.  If you got any questions, let us know in the comments or in our discord.  And of course don't forget to subscribe to our YouTube channel to see future dash videos.  Thank you and see you in the next one.

**Frame:** tutorials\frames\ue5-world-building-for-beginners-full-dash-demo-level\frame_018.jpg


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
