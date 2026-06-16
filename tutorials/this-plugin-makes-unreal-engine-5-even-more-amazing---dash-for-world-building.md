---
title: This Plugin Makes Unreal Engine 5 Even More Amazing - Dash for World Building
source: YouTube
url: https://www.youtube.com/watch?v=EezUW6MSqfE
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/this-plugin-makes-unreal-engine-5-even-more-amazing---dash-for-world-building/
frame_count: 9
---

# This Plugin Makes Unreal Engine 5 Even More Amazing - Dash for World Building

**Source:** [YouTube](https://www.youtube.com/watch?v=EezUW6MSqfE)
**Author:** Polygonflow Dash
**Duration:** 6m36s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, Josh Powers for Polygonflow.  And in today's video, we're going to go over how I created this scene inspired by William  Foshet.  So let's get to it.  So I'm going to start here with a simple displaced terrain and texture.

**Frame:** tutorials\frames\this-plugin-makes-unreal-engine-5-even-more-amazing---dash-for-world-building\frame_000.jpg

### Terrain [0:14]
**Transcript:** You could build this using the modeling program of your choice, unreal's built in modeling  tools, or even creating a small terrain with dash.  And in this case, I also used the Megascans surface to displace the mesh to give it a bit  of undulation so that it wasn't a perfectly smooth surface.  So the first thing we want to do is place a log in the scene since the rifle, which is

**Frame:** tutorials\frames\this-plugin-makes-unreal-engine-5-even-more-amazing---dash-for-world-building\frame_001.jpg

### Placing Log [0:37]
**Transcript:** the focal point, will be propped up against it.  So we'll go ahead and open up dash and then open the content library.  So make sure that we're on the Megascans menu and then search for a log.  Because this scene will have a lot of really busy detail on the forest floor when we're  finished, I want to go with a fairly simple log that is a bit smoother looking.  So we'll drag and drop this one into the scene and move scale and rotate it into position  using dash's placement tool.

**Frame:** tutorials\frames\this-plugin-makes-unreal-engine-5-even-more-amazing---dash-for-world-building\frame_002.jpg

### Adding a Camera [1:12]
**Transcript:** I want to get a jump on the camera work since I'm going to only detail out the parts of  the scene I'll see in this frame.  So I'll add a new camera through dash's prompt bar and then move it roughly into the position  I want for this particular shot.  And before I move on, I'll go to the camera settings and change the focal length to 50  millimeters to get a nice and up close angle.  And then I'll play with the position a little more until I'm happy with where it is.  And we'll come back for the other settings a bit later.

**Frame:** tutorials\frames\this-plugin-makes-unreal-engine-5-even-more-amazing---dash-for-world-building\frame_003.jpg

### Placing Assets [1:42]
**Transcript:** Alright, let's go ahead and place the rifle.  This is a free model I got off Sketchfab, which of course will be linked in the comments  below.  Using dash's new AI tagging system, I'm able to simply go to my custom assets tab in the  content library and type gun.  And right here you can see that the model is ready to go.  Now I can drag it into the scene.  I'll go ahead and place the rifle so that it's leaning up against the log.  And once I'm pretty happy with where it's positioned, I'll go ahead and switch back  to my camera to fine tune the placement so it looks best from the camera's perspective.  And I do the same thing with the hat, which I also downloaded for free from Sketchfab.  Again, the AI tagging system makes asset management incredibly easy in dash with minimal effort.  It's truly a game changing system I wish I had had access to all my career.  I also went ahead and added a few trees.  Though these trees will not be visible in frame, they do act as an important light locker  to give the darker, flatter look I'm going for with this shot.  Alright, for the most part we can go ahead and stay locked into our camera's perspective  now, since the majority of the assets wil...

**Frame:** tutorials\frames\this-plugin-makes-unreal-engine-5-even-more-amazing---dash-for-world-building\frame_004.jpg

### Scattering 3D Assets [3:35]
**Transcript:** If you've used dash for any time, I don't need to tell you how powerful the scatter feature  is.  So let's go ahead and search for some Megascans assets to start scattering.  We'll start with this one here by dragging it out into the scene, and while holding down  control, I'll let off the mouse button and this menu will pop up.  And I'll go ahead and select the scatter option.  Then it's just a matter of tweaking the settings to get the results we want.  As always, I like to build up my scenes and layers.  What this oftentimes means is that I'm going to use the same asset multiple times in various  scales and densities to not only help sell the variety of debris we would see on the  forest floor like this, but it'll also allow me to add more depth to my scene using the  same asset multiple times, saving on the texture memory.  Something like this would take ages to do by hand, but in just a few minutes I was able  to achieve it with Dash.  Okay, as I mentioned before, there's a great new feature in Dash that you might not know

**Frame:** tutorials\frames\this-plugin-makes-unreal-engine-5-even-more-amazing---dash-for-world-building\frame_005.jpg

### Setting up Standalone Bridge Library [4:34]
**Transcript:** about, and that's the ability for Dash to load Megascans that you might have downloaded  from Quixil's standalone bridge application.  This means that certain asset types, such as Atlas Maps, are now available to import  through Dash.  All you need to do is open the content library, press on the three dots over here, and set  your standalone bridge download folder.  Once that's set, the content library will show you the assets that are currently in that  folder.  While this feature is great on its own, you might be wondering how it can help speed  up your workflow.

**Frame:** tutorials\frames\this-plugin-makes-unreal-engine-5-even-more-amazing---dash-for-world-building\frame_006.jpg

### Scattering Atlas Texture Assets [5:11]
**Transcript:** Well, let's go ahead and find an Atlas map we like, and then we'll simply drag it into  the scene, and like before, we'll hold down Control before letting go of the mouse button,  and then we select Scatter.  And boom, in one action, Dash took the Atlas texture from the standalone bridge downloads,  use the opacity to create alpha-card meshes for each of the objects on the Atlas texture,  and then scattered them on the ground.  Now we can make some adjustments to the scatter settings, and then add another Atlas,  and then another, and another.  And just like that, we've added unprecedented depth to this forest floor with literally  just a couple of clicks.  Alright, now we can hop back into the camera settings menu, and start playing with all

**Frame:** tutorials\frames\this-plugin-makes-unreal-engine-5-even-more-amazing---dash-for-world-building\frame_007.jpg

### Camera Settings [5:55]
**Transcript:** the nicely organized settings that'll let us adjust the post-effects, color grading,  and more just to let us really enhance the mood of this shot.  And turn on Path Tracer, and Voila.  We went from a simple terrain mesh with a texture to a complex forest floor in just a few  minutes.  A feat that would be impossible without Dash.  So be sure to check out Dash for yourself, and see how it can help improve your workflow.  Thank you so much for watching, and we'll see you in the next one.

**Frame:** tutorials\frames\this-plugin-makes-unreal-engine-5-even-more-amazing---dash-for-world-building\frame_008.jpg


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
