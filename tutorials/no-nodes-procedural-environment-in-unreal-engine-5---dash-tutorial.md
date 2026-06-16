---
title: No Nodes Procedural Environment in Unreal Engine 5 - Dash Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=6U2jbJmqs4k
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial/
frame_count: 11
---

# No Nodes Procedural Environment in Unreal Engine 5 - Dash Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=6U2jbJmqs4k)
**Author:** Polygonflow Dash
**Duration:** 8m24s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction [0:00]
**Transcript:** Hey everyone, welcome to another video here at Polygonflow. My name is Gaelin, and in  today's video we'll be covering how I made this canyon scene in Unreal using Dash.  The approach to this environment is simple, in that we will be anchoring all the rules  of the scene to two spline actors. Every adjustment that I make to the individual points  along the spline will affect all of the actors on one side of the canyon, making the  scene highly customizable by a dash. Let's start by looking at all of the actors we

**Frame:** tutorials\frames\no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial\frame_000.jpg

### Assets Used [0:37]
**Transcript:** will employ for this environment. I have several scanned cliff pieces here that will serve  as the main elements of the canyon walls here to start. Just a quick note to say here  that I employed the modeling tools to cap off the back faces of these pieces before  I got started. Next, I have some ground elements to break up the terrain. I'll be doing  two passes with these pieces, one that will be closer to the canyon walls with larger  physical features and the next with higher frequency details falling off from the previous  set. I'll also be adding in an amount of foliage that will fall with similar logic,  where the actors will mostly hug the canyon walls. With all that out of the way, let's

**Frame:** tutorials\frames\no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial\frame_001.jpg

### Drawing the Canyon Shape [1:18]
**Transcript:** start. Let's start by creating the main shapes for the canyon walls. The spline tool  and dash is highly versatile and gives you a good amount of settings to play with as  you draw over terrain or existing static meshes. One setting I'll be adjusting here at  the outset is the spacing between spline points. With the canyon wall mesh being pretty  large, I want the spacing between points to be larger than the default setting here in  dash. If the spacing is too close together, it will be difficult to make large scale  adjustments later on. Now that I've drawn out the basic shape for what I want the walls  to conform to, let's pair up the logic for the spline with Pathscatter. Pathscatter essentially

**Frame:** tutorials\frames\no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial\frame_002.jpg

### Creating the Canyon Base [1:55]
**Transcript:** just gives you a curve as a projection method and has a ton of features that we can affect  in order to get the look that we are going for. Let's begin by adding in the curve we drew  as the main control arm for the tool. After selecting here in the viewport, I'll set  the plus button here in the Pathscatter window to pair it. Next, let's select all the  wall components and add them to the scatter tab. And just like that, you can see all the  assets begin to populate along the path. The first adjustment I'll make here is the scale  of the assets. We want to add in an amount of variation from asset to asset, but not so  much to where anything sticks out. Next, we can start to affect the density. At this stage,  it might be worth revisiting the minimax settings that we changed earlier to see how everything  looks in concert. Obviously, we don't want any gaps along the path, but we also don't  want too many meshes in our penetrating, so I'll likely make adjustments to this as I  go. Another unique feature in Pathscatter is the ability to add parallel curves in the  settings without drawing out new splines altogether. I won't be employing that feature  here in this example as I want to...

**Frame:** tutorials\frames\no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial\frame_003.jpg

### Scattering on the Ground [3:25]
**Transcript:** We'll still be using the spline we initially drew out to help inform where the assets  get placed, but not to the Pathscatter this time. To be clear, you could still use Pathscatter  if you wanted to generate a similar effect with slightly different settings, but I chose  to use the surface scatter for this use case. Let's start by loading in the necessary  assets. We'll also start loading in the surface input here at the top. In my case, I generated  a procedural terrain mesh using dash and used a simple sand material across the entire  surface. Next, let's load in some of the larger ground scatter elements here at the top  of the window. As you can see, by default, it scatters across the entire terrain. Dash

**Frame:** tutorials\frames\no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial\frame_004.jpg

### Masking the Scatter to the Canyon [4:13]
**Transcript:** has some really simple and effective masking features that we can lean on to anchor the  scatter to the same control arm that we set up with the Pathscatter example. In this  case, I'll be leveraging the proximity mask feature. Let's select our initial spline  and load it into the Objects tab using the plus icon. As you can see, we need to invert  this mask and increase our distance until we get a soft falloff from the spline. We can  supplement this mask with additional noise as well if we wanted to break up any of the  hard lines in the resulting scatter. As I mentioned before, I have another ground scatter  element I'd like to use here with a different frequency of detail that will fill in nicely  with the other pieces that we just laid down. I'll speed through this section, but ultimately  we are using the exact same method in surface scattering while masking for the spline actors.  And once again, we'll use the same method for scattering foliage along the canyon walls.  Alright, now that we have everything connected up to our initial spline, you can see that

**Frame:** tutorials\frames\no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial\frame_005.jpg

### Adjusting the Canyon with the Spline [5:16]
**Transcript:** every adjustment that we make to individual spline points affects all of the actors that  we are using here in the scene. This makes for a highly directable scene in that everything  is linked to our initial spline actor. Creating simple logic like this in Environment Creation  reduces iteration time drastically. As you can see here, I created a second wall for  our canyon employing the exact same methods to have two independent control arms for the  scene. Now, I wanted to employ some of Dash's physics features to create a rock slide at the

**Frame:** tutorials\frames\no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial\frame_006.jpg

### Creating a Grid of Rocks [5:47]
**Transcript:** end of this canyon. There are many ways to accomplish this using Dash, but I wanted to try  something a little different for this scene. To start, I've sourced a few boulder assets  that I think will look pretty good for the rock slide. Next, let's type grid scatter in at  the top of the toolbar. After we load the boulder assets into the instance mesh's section,  we can start to build out a large grid of rocks above the canyon. Obviously, the more pieces here  that you create, the more intense the computation will be on the physics side of things, so be conscious  of what you are loading in. And to be clear, it's worth running the simulation a few times to see  exactly how many actors you'll need for this type of look and just play around with a couple settings  until you dial in the look that you're going for. As you can see, I'm also creating a wide range  scale wise from actors to actor so that it doesn't look like all the same few rocks just scattered around.  I've also checked random spin to on and added in some rotation jitter so that the assets  themselves will have nice variation once they start to collide with each other.  The random remove slider also helps create some ni...

**Frame:** tutorials\frames\no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial\frame_007.jpg

### Rock Slide Physics Simulation [7:12]
**Transcript:** Okay, and now for the fun part, let's open up the physics tool and watch these pieces fall into place.  For more detailed breakdown on the physics tool, here's a link to a previous video where we cover  every aspect that the feature set. Suffice to say that we need to make every one of these rocks  physics ready using Dash and ensure that our collision for everything above and below is set up  properly. One thing that is worth pointing out philosophically is that this exact same method of

**Frame:** tutorials\frames\no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial\frame_008.jpg

### Other Use Cases [7:35]
**Transcript:** world building can apply to a completely different use case. I've paired up this tropical scene  with a single spline and am able to effect change super easily as a result.  Obviously, the computation becomes more taxing depending on the resolution and complexity of the  assets, so keep that in mind as you start to optimize this method for your own personal workflows.

**Frame:** tutorials\frames\no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial\frame_009.jpg

### Final Result [8:03]
**Transcript:** Alright, and just like that, we've made a really simple scene using Dash and a handful of assets.  Thank you so much for tuning in, and I hope you're able to find this video useful. We'll catch you in the next one.

**Frame:** tutorials\frames\no-nodes-procedural-environment-in-unreal-engine-5---dash-tutorial\frame_010.jpg


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
