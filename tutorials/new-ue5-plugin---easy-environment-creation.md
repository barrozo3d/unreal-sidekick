---
title: New UE5 Plugin - Easy Environment Creation
source: YouTube
url: https://www.youtube.com/watch?v=lCicNo8MGNA
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/new-ue5-plugin---easy-environment-creation/
frame_count: 11
---

# New UE5 Plugin - Easy Environment Creation

**Source:** [YouTube](https://www.youtube.com/watch?v=lCicNo8MGNA)
**Author:** Polygonflow Dash
**Duration:** 7m35s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, Josh Powers with Polygonflow.  And today we're going to create a fun lighthearted scene using Megascans and Dash, your co-pilot  to worldbuilding.  So let's get started.

**Frame:** tutorials\frames\new-ue5-plugin---easy-environment-creation\frame_000.jpg

### Scene Setup [0:15]
**Transcript:** So here we are with mostly an empty scene.  All I have is an HDRI skybox and a directional light.  For those unfamiliar, you can place an HDRI skybox by going to the content dropdown,  lights, and HDRI backdrop.  If you don't see HDRI backdrop, make sure that you have it enabled in your plugins menu  by checking this box right here.  Alright, to start I'm going to just quickly make a plane using the Unreal modeling package.  After setting the size and amount of subdivisions for the plane, I'll go ahead and open the  content library and Dash to find a good dirt material to add to it.  For this particular piece, I wanted to have a puddle right in the foreground so I go  to the sculpting tool to start pushing down the vertices in this area.

**Frame:** tutorials\frames\new-ue5-plugin---easy-environment-creation\frame_001.jpg

### Displacement Tool [1:10]
**Transcript:** Once I'm settled on this, I can go to the displacement tool and drag the mask texture  map that imported with this material right onto this slot.  In most cases, Megascans will import with the depth or displacement map for a given  surface in the blue channel of the mask texture.  So by dragging the texture into the slot and changing the channel to blue, I can then  displace the plane to give a more undulated, uneven look to it.

**Frame:** tutorials\frames\new-ue5-plugin---easy-environment-creation\frame_002.jpg

### Water Material [1:40]
**Transcript:** Alright, this looks cool, but I do want to make a few adjustments to the material, which  I can do by selecting the mesh and clicking this edit material button up here on the  Dash prompt bar.  The first thing I want to do is pull the roughness way down so that it gives it a much more  wet appearance.  And I'll sell this further by playing with the brightness, contrast, and saturation  sliders.  After that, I'll just want to add some additional tiling to prevent the texture from looking too  low-res.  Adding a simple water into my scene is super fast using Dash.  I can just type plain to add my water plane, and then after scaling and moving it into  position, I just need to type water and select the set water material, which will apply  the water material to my selected plane.  Then I can just make a few adjustments to the water material, and I'm all set.

**Frame:** tutorials\frames\new-ue5-plugin---easy-environment-creation\frame_003.jpg

### Scatter Tool [2:35]
**Transcript:** With the foundation of my scene ready, it's time to put the scatter tool to work.  As always, I'll grab an asset in the content library and drag it straight onto my scene  while holding control.  And then I'll just select the scatter here option.  As I like to mention, building up my scatters and layers is a great way to quickly get a  realistic look with a scene.  In this case, I'm actually using the same asset multiple times to scatter them at different  scales.  This is a great way to attain that lush feel without needing a plethora of different  assets to fill things out.  That said, we do see a variety of plants in real life, so it's a good idea to break things  up by adding some other foliage assets to the scene to add some more visual interest  throughout.  Just a few weeds, grass plants, and flowers can really do a lot for the framing of this  shot.  Then I can scatter a few extra elements, such as some rocks, pebbles, and some leaves as  a finishing touch for the scattering.

**Frame:** tutorials\frames\new-ue5-plugin---easy-environment-creation\frame_004.jpg

### Placement Tool [3:38]
**Transcript:** For this shot, I really want to have a clear foreground, mid-ground, and background.  So for the far side of the mid-ground, I'll add a log asset to my scene by dragging it  from the content library and using dashed placement tool to position, scale, and rotate this  asset right where I want it to be in my shot.  Using this tool is really great to rapidly position an asset, and it never breaks my flow  as an environment artist.  And I'm happy with its positioning, I'll scatter some vegetation onto it, keeping it  quite small to replicate some moss growth.  Playing with a few of the settings, such as noise break up and ad mask, will give a unique  placement of the asset on the log, helping sell the realism even further.  Alright, let's add the first toy which I'll drag from the content library.  We're starting with the moose, which will be the focal point of the shot.  Using the placement tool, I'll scale up the moose quite a bit so that it's the largest  by far of all the toys in the shot.

**Frame:** tutorials\frames\new-ue5-plugin---easy-environment-creation\frame_005.jpg

### Adding a Camera [4:41]
**Transcript:** And now that we have the moose placed, I'm at a point where I'll add a camera to set  up the composition of the shot.  To do this, I'll simply type new camera in the dash prompt bar, and it'll add a new  cinematic camera to the scene.  Once I have the camera roughly in position, I can go up to this aperture icon on the  dash prompt bar, and open up the camera and post settings menu.  This will let me adjust various camera settings such as my focal length, focal distance, aperture,  etc. to bring the subject into focus while fading the other areas to be more out of focus.

**Frame:** tutorials\frames\new-ue5-plugin---easy-environment-creation\frame_006.jpg

### Adding Toys [5:20]
**Transcript:** Alright, so now I can go ahead and give our moose some friends.  I'll add some various other toys that come with mega scans to add a bit more life to  the shot.  However, for these little guys, I want to keep their scale lower compared to the moose  in order to clearly define that the moose is the focal point of the shot.  So I'll just use the placement tool to quickly add them to the scene.

**Frame:** tutorials\frames\new-ue5-plugin---easy-environment-creation\frame_007.jpg

### Adding Trees [5:43]
**Transcript:** Alright, I'm just about finished with both the mid and foreground areas, but we need  something for the background other than just the HDRI sky.  To do this, I'm going to simply duplicate my mid ground geometry, scale it up, and position  it somewhere behind the log.  From here, I'll just add some of the mega scan trees by manually placing them in the  scene from the content browser.  And with them selected, I can initialize the scatter tool in the dash prompt bar by typing  surface scatter.  From here, it's just a matter of tweaking the settings of my scatter tool, and I'm left  with a nice natural tree background for my shot.

**Frame:** tutorials\frames\new-ue5-plugin---easy-environment-creation\frame_008.jpg

### Adding Shrubs [6:27]
**Transcript:** Then lastly, for my background area, I want to add some shrubs just behind the log to  act as a bit of a separating curtain between the mid ground and background areas.  To limit the shrubs to just this area, I can draw a curve along the spot using the draw  curve tool in dash.  Then I can simply select the shrub, then the curve, and use it as a proximity mask by  clicking this icon right here.  Then lastly, I can fine-tune some more of the camera settings along with the post-processing  to finish up the shot.

**Frame:** tutorials\frames\new-ue5-plugin---easy-environment-creation\frame_009.jpg

### Outro [7:06]
**Transcript:** And there you have it.  There's a bunch of aspects behind this workflow that would simply have taken too much time  in a typical Unreal Engine process, and that's exactly why we've built dash, to remove any  redundancies and let you enjoy the creative journey.  Be sure to check our discord to see how others are using dash or get help technical or  artistic domains.  With that, I'll see you next time.

**Frame:** tutorials\frames\new-ue5-plugin---easy-environment-creation\frame_010.jpg


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
