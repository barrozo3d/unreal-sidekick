---
title: How to Re-Create The Walking Dead in Unreal Engine 5 - Dash Workflow
source: YouTube
url: https://www.youtube.com/watch?v=5aTwhjR5JJE
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-re-create-the-walking-dead-in-unreal-engine-5---dash-workflow/
frame_count: 8
---

# How to Re-Create The Walking Dead in Unreal Engine 5 - Dash Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=5aTwhjR5JJE)
**Author:** Polygonflow Dash
**Duration:** 8m26s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction [0:00]
**Transcript:** Hey everyone, welcome to another video here at Polygonflow.  My name is Galen, and today I'll be showing you a few of the ways that I use Dash to  help build out my interpretation of the iconic hospital scene from the Walking Dead pilot  episode.  Dash saved me a ton of time in scattering assets, decals, and breathing life into this  environment.  In this video, we'll be looking at a number of scattering techniques, decals, cable placement,  and more.

**Frame:** tutorials\frames\how-to-re-create-the-walking-dead-in-unreal-engine-5---dash-workflow\frame_000.jpg

### Assets Used [0:38]
**Transcript:** The Decagon hospital set is where I source the majority of the assets for this build,  and the models they provide are some of the highest quality pieces on the marketplace.  We've put a link in the description below to get the exact set if you want to see  them for yourself.  Alright, and with all that out of the way, let's get started.  Let's start by looking at some of the Blood Spatter in the Patient Room.

**Frame:** tutorials\frames\how-to-re-create-the-walking-dead-in-unreal-engine-5---dash-workflow\frame_001.jpg

### Blood Splatter (Decal Scatter) [1:00]
**Transcript:** I source the few unique Blood Spatter decals from Bridge to help build out a gruesome scene  in one of the rooms just doors away from where Rick wakes up in the hospital.  There's a brief shot in that sequence where you can see some blood in the hallway, so  I decided to build on that idea for this room.  I knew I wanted a fair amount of blood in here, and hand placement here would have been  pretty tedious.  So to start, I'll draw out a basic plane and match the basic footprint of this room.  The reason that I did it this way is because I want the decals to be localized to just  this section of the environment and not the entire ground plane.  Next, let's type decal scatter into the bar.  And I'll load this plane in as my surface input.  There are a number of ways that you could do this using masking in dash, but I elected  simply to use this plane as a guide and hide it at runtime to get the desired effect.  Now let's load in a few of the decals here and see how it looks.  Out of the box, we're already getting a pretty nice effect.  Since I've loaded in a handful of decals, the breakup is starting to look pretty natural  as I increase the density.  Effecting the min and max scale...

**Frame:** tutorials\frames\how-to-re-create-the-walking-dead-in-unreal-engine-5---dash-workflow\frame_002.jpg

### Creating the Ceiling (Grid Scatter) [2:37]
**Transcript:** Alright, let's take a look at the ceiling next.  I really liked how in the initial reference, there were lots of ceiling tiles missing  above and broken up on the floor below.  I started out by finding the material that I liked for the ceiling and modified it slightly  to fit better inside of this world.  I then used the modeling tools to help create a simple box, unwrapped that model to the  texture, and added in a slight amount of noise using the displacement features.  I made three different variations here, just to add a little bit of additional variation  from tile to tile.  The wood scatter allowed me to easily place the ceiling components and add in variation  from piece to piece.  As you can see, I needed to spend a little bit of time sorting out exactly what the scale  values needed to be, and how far I needed the pattern to actually extend, but in just  a few seconds we had our ceiling.  And before all of that, I'd roughed in some loose fitting structural metal components  that I wanted to expose randomly throughout the hallway.  Random remove was the perfect way to implement this, so I played with that slider and seeding  until I got the look that I was going for.  The l...

**Frame:** tutorials\frames\how-to-re-create-the-walking-dead-in-unreal-engine-5---dash-workflow\frame_003.jpg

### Broken Ceiling Tiles (Physics Tool) [4:39]
**Transcript:** Okay, let's take a look at how I employed physics in this scene.  Let's stay with the tiles here for the next example.  From the reference, I inferred that there are tiles that fell from the ceiling, and crumbled  under duress and time.  As such, I wanted to take my existing tile meshes, and crumbled them up to match that type  of duress.  My friend Jacob Koidel has made an excellent video about the fracture system in the modeling  tools, and so I employed a similar technique to break up the tiles and prep them for physics.  And the link to that video is in the description below.  After assigning simple convex collision to the individual pieces, I loaded up the physics  tool.  Essentially, I wanted to mimic the dropping of the tile pieces onto everything below.  As such, it's important to verify that you have proper collisions set up for everything  that you are simulating, but also everything that your dynamic pieces are set to come  in contact with.  After selecting this grouping, all I needed to do was click Dynamic, and then start to  see the end result.  And we can do this for ceiling tiles, hospital clutter, and the like until we get a decent

**Frame:** tutorials\frames\how-to-re-create-the-walking-dead-in-unreal-engine-5---dash-workflow\frame_004.jpg

### Pill Bottle Piles (Physics Tool) [5:42]
**Transcript:** amount of debris.  And I also used physics to create a few piles of pill bottles in the patient room, duplicating  my selection a few times resulted in a pretty neat effect.

**Frame:** tutorials\frames\how-to-re-create-the-walking-dead-in-unreal-engine-5---dash-workflow\frame_005.jpg

### Broken Cables (Quick Pipe) [5:54]
**Transcript:** Alright, let's talk about cables.  Cables are present all over this environment, and Dash helped me to accomplish this in  no time.  And there are several different types of cable implementations that I used here, so let's  take a look at those.  The first is drawing cables over a complicated static mesh.  This toppled supply cart has a lot of intricacy that seemed like a really fun way to use the  tool.  And I wanted the end result to look like the cable had gotten tangled up in the object,  so I started drawing.  You need to start with the curve tool, and this will create the skeleton for our cable.  It's important to pay attention to the minimum spacing setting when drawing, as you need  to identify how many control points you really need in order to achieve the look that you  are going for.  If you have too many points, it will become really difficult to make edits.  So err on the side of fewer, as you can always smooth the actual mesh out with the cable  tool later.  After we are happy with the initial curve, we now need to move towards creating a mesh  around the spline.  Quick pipe allows us to flag the curve that we drew as the main control arm for that piping.  From there,...

**Frame:** tutorials\frames\how-to-re-create-the-walking-dead-in-unreal-engine-5---dash-workflow\frame_006.jpg

### Hanging Cables (Cable Tool) [7:26]
**Transcript:** I also use the cable tool to create a few one off hanging cables from the ceiling structure.  And I cheated a little bit in this example by placing assets up in the ceiling that I  knew I wanted the wires to hang from.  And this gives me a lot more granular control over where the wires are connected.  And some really important settings that I leverage here are connection rate and cut rate  to add variation in the bundles of wires.  In and max gravity adjustments, we're also super helpful in adding multiple elevations  to the clusters.  Add in some noise on top of that, and the cables really added a nice level of breakup  to the scene.  Okay, well I hope you found this video useful.  I really enjoyed building this environment, and I hope you'll tune in to our next video.  Thanks for watching, and we'll see you next time.

**Frame:** tutorials\frames\how-to-re-create-the-walking-dead-in-unreal-engine-5---dash-workflow\frame_007.jpg


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
