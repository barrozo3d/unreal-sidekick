---
title: Introducing Dash for Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=NVSEN3ND6VU
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/introducing-dash-for-unreal-engine-5/
frame_count: 9
---

# Introducing Dash for Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=NVSEN3ND6VU)
**Author:** Polygonflow Dash
**Duration:** 12m1s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Dash Overview [0:00]
**Transcript:** Hey everyone, Josh Powers here from Polygonflow, and today I'm thrilled to announce Dash,  a novel approach to world building in the Unreal Engine.  With this video, I hope to show you just how exceptional Dash is at streamlining your creative  process with no loss of creative control.  So sit tight and let's get into it.  Okay, with the Unreal Editor open, the Dash icon should be right up here, and then if you click  on it, a prompt bar will show up.  Our goal for Dash is to remove literally any complex interaction you have to do with  your 3D software.  And as such, you'll see me throughout the tutorial working exclusively in full screen  mode, with nothing but the Unreal Engine 5 viewport supercharged with Dash's incredible  versatility.  So let's hit F11 and go into full screen and then jump right into it.  You can think of this prompt bar as a comprehensive set of solutions for world building.  Typing keywords in here will show all relevant tools and actions, and the same drop down menu  here can also be opened by double clicking on the logo itself.  The menu on the left is where you can check for updates, open up the documentation, and  much, much more.  There's lots of other...

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_000.jpg

### Dash Prompting [1:21]
**Transcript:** art.  First let's create some terrain.  You can type create a terrain or just terrain into the prompt bar.  You'll notice the terrain action being the first suggestion.  An action will typically have its title in bold and its context sensitive, meaning it'll  operate based on your prompt and sometimes you're seeing content.  Tools, however, don't have their text in bold and will just open up a small panel through  which the tools work.  You can press the up and down arrows to cycle between suggestions, select them with your  mouse, or just hit enter, which will bring up the first tool being suggested.  As you can see, Dash created a terrain mesh for us and also opened a floating panel through  which we can now adjust.  If I close the panel, then select the terrain again, Dash will automatically show this icon,  which suggests that whatever act drive selected in the Unreal Editor has an editable tool  attached to it.  This is available for a couple of other behaviors as well and we'll be going through those  later in this tutorial.  Let's go ahead and click on the icon and adjust our terrain settings.  Next we want to give the terrain a material and this is where the content library...

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_001.jpg

### Water Creation [3:27]
**Transcript:** To do this let's write create a plane in the Dash prompt bar, pick the primitive action  and a plane should be created in the center of our view.  Next let's write apply water and a water material will be applied to it.  I'll go ahead and scale my plane to properly cover the terrain and now we're ready to move  on.  With our terrain set up let's start placing some objects in the scene.  You can drag and drop them from the content library and an interactive object placement  allows you to neatly drag the object around all while lining it to the underlying surface.  You can hold control to scale it, shift to rotate it and even control shift to sync it  below the surface which is extremely common to do when world building.  The panel over here shows you all the hotkeys you can use with this context based placement  tool and you can quit the context at any point by hitting escape and to collapse the hot  key panel just double click on it.  Just to recap we've been able to create a ground adjusted settings, give it a material, add  some water and now place an object all without ever interacting with unreal's clotted workflow  and we haven't even scratched the surface of what Dash can do...

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_002.jpg

### Surface Scatter Intro [4:50]
**Transcript:** Before we start detailing our scene let's go ahead and type new camera to create a new  camera.  Then I'll pick a view I feel comfortable with and do some very brief tweaks to my field  of view, sharpen and other basic effects to get a good base.  I'll also pick my lighting setup either by typing cycle lighting to see all the possible  lighting setups or just write a specific word to pick a preferred one.  With that out of the way let's start adding more detail.  Scattering is one of Dash's main strengths and its simplicity is truly unparalleled.  Just drag and ask it from the content library to your viewport and hold control when you  drop it.  This will give you a couple of scatter options.  Let's just go with scatter here.  Like with the terrain a floating panel shows up and with it everything we need to get a  good base.  As you can see I'm getting really good results within seconds.  I recommend you play with all the values but fall off and break up are among my favorites  as they allow you to get some truly phenomenal results in new time.  As a small tip the sliders usually make fairly minute changes.  However by holding control you can increase the rate of change and with sh...

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_003.jpg

### Constrain Scatter to Paths [6:18]
**Transcript:** We'll write draw curve and dash and literally just draw a curve in our viewport.  Then with our grass and the curve selected an icon will show up in the toolbar allowing  us to mask out the grass with the curve.  As with most things a short concise panel shows up with just the right settings you need.  You can use this masking workflow with any type of object.  Just make sure you first select the asset you want to mask which in our case is the grass.  Then select whatever you want to mask it with.  It could be curves, meshes or even another set of instance objects such as large rocks  scattered throughout the landscape.  And by the way scattering also works on curves and instances.  I can select some instances here then drag and drop some objects from the content library  with control press and also scatter on instances.  But keep in mind that scattering on instances can be quite resource intensive.  Needless to say we've worked to give you state of the art capabilities with zero friction  in the process.  This simplified approach doesn't remove any complexity from your workflow.  As a small side note you can at any point close the panel of the specific scatter set up,  then delete...

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_004.jpg

### Dash Color Grading [8:10]
**Transcript:** post processing work.  Dash has a plethora of color grading presets to offer.  And as with the lighting we can just type cycle grading to cycle through the different  options or even go with specific keywords of famous movies such as the Joker and Children  of Men.  Or more relevant keywords like Warm or Vintage.  Back to my camera settings I'll just tweak a few things a bit and that should do it.  This workflow for me is what makes Dash truly exceptional.  We haven't even touched Unreal Engine's panels or nodes and everything happened through  a prompt bar without ever taking over creative control.  These types of natural scenes are the first set of environments that Dash truly excels  at.  But even with this first release we're already expanding to more man-made environments.

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_005.jpg

### Manmade Environments with Dash [9:06]
**Transcript:** Here we have a new scene I built using the various tools in Dash.  But to really make it shine I can just search for some decals in the content library, drag  and drop them onto the viewport, and then the interactive decal place will give us the  best decal workflow out there.  And even more you can select multiple decals and scatter them as you would scatter regular  meshes.  This makes detailing man-made environments such a fun and inspiring process.  Alright, here I am in another scene and I wanted to scatter the Megascans trees which are

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_006.jpg

### Forest Creation [9:41]
**Transcript:** not available in bridge.  To do this I'll drag and drop them somewhere in the scene, find and open the tool surface  scatter, add the trees to scatter, then a surface to scatter too.  Just like with drag and drop scatter, if we select the trees we just manually scattered  we can select the 3.icon up here and now have the floating bar to adjust our trees.  This method of scattering is now identical to the other, which means we can also mask them  out based on curves or other objects.  We'll be supporting such assets directly in the content library soon, making the process  just as simple as the content library's scatter workflow.  And before we close our scattered adventures, I'll show you one more thing.

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_007.jpg

### Create Leaf Scatter [10:30]
**Transcript:** Megascans comes with thousands of Atlas textures through their website, but they're unfortunately  not available in the bridge plugin.  To remedy this, we can download them locally through the Megascans website or bridge software.  And then back in dash, you can write, create scatter mesh cards or just scatter cards, then  select the action mesh cards.  And it'll open a dialog for you to select the opacity map of your Atlas asset.  And just from that, dash will import all your textures, create mesh cards and materials  with them, then scatter them on whatever object you had selected in your viewport.  Again, there's zero loss of control.  All our scatter parameters are right there to tweak, and with this, you now suddenly  have thousands of assets that can be used to detail environments at record speed.  And that concludes our first introduction video.  We'll be diligently working to give you all the learning material you need to get acquainted  with dash, and I hope to show you many more environment case studies, where we'll just  be creating beautiful worlds at our own pace.  In this age of one click solutions with AI systems and bloated workflows on the other end  of the spectru...

**Frame:** tutorials\frames\introducing-dash-for-unreal-engine-5\frame_008.jpg


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
