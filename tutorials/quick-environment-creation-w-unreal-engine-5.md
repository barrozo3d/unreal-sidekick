---
title: Quick Environment Creation w/ Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=YfHdlxH22cM
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/quick-environment-creation-w-unreal-engine-5/
frame_count: 8
---

# Quick Environment Creation w/ Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=YfHdlxH22cM)
**Author:** Polygonflow Dash
**Duration:** 8m48s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction to HDR Lighting [0:00]
**Transcript:** Hey everyone, Josh Powers with Polygon Flow.  And today we're going to go through step by step on how to create a serene and peaceful  environment like this, leveraging the power of dash inside Unreal Engine 5.  So let's get straight to it.  With an environment like this, I want to utilize the power of high dynamic range image-based  lighting, or HDRI for short.  While Unreal comes with a few images to work with, I do recommend checking out Polyhaven,  which has hundreds of HDR images to download for free.  Just make sure you select the HDR file type before downloading.  And then from there, it's a simple drag and drop into Unreal, and you're ready to go.  To add an HDRI sky in your scene, you can simply click this button up here, select the  light option, and then HDRI backdrop.  This will place an HDRI sky in your scene.  I'm not going to go into all the details about how this works in this video, but what  I want to do in this case is change this teardrop-shaped asset to a spherical model instead.  And then I'm going to change the skylights intensity, as well as the HDRI sky's blueprint  intensity.  Both of these will have an impact on the intensity of the lighting from your ima...

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_000.jpg

### Dash Terrain Creation & Texturing [1:55]
**Transcript:** And we'll start by creating a terrain by typing terrain into Dash's prompt bar, and making  sure to select the create terrain action.  This will drop in a procedurally created terrain mesh into our scene that we can then  adjust various values to give our terrain the type of details we want.  For this scene, I wanted to have some larger rolling hills, so I made sure turbulence  was pretty far down to give us that lower frequency of hills, as well as cranked up the  height to achieve the nice rolling look.  I also bumped up the mid-turbulence value quite a bit, which gives us some chunkier  layers along the hills.  This might feel strange now, but this will really help add some irregularities to our  grass scatters that gives a more natural look later on.  Once we're satisfied with these settings, we can just go ahead and open up the content  library, select a good dirt material, drag it onto the terrain, and then open up the materials  panel from Dash, and make a few adjustments before moving on to the next step.  We should also add a directional light to our scene to give us a strong key light.  We just want to make sure that the direction matches the sunlight in our sky box, and ...

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_001.jpg

### Key Shot Setup [3:18]
**Transcript:** There are a few types of trees in this pack, primarily field and forest.  I'm using the field trees for this scene, but feel free to use whichever works best for  your shot.  And after a few adjustments to its position on the terrain, I'm ready to frame out the  key shot for this scene.  And to do this, I'll go up to the prompt bar and type New Camera to create a new cinematic  camera in my scene.  From here, I'll play with the position, focal length, crop settings, and so on to get  the look I want for this shot.  Every scene will be different because every artist has their own vision of what their  shot should look like.  So be sure to play around with this, and study some photography and films to help strengthen  your knowledge in this area.  Alright, so now it's time to fill out this terrain with some lush vegetation.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_002.jpg

### Adding Vegetation with Dash [4:04]
**Transcript:** To do this, we'll go to our content library and search for grass.  I'll grab these grass patches from Megascans because the assets cover a little more real  estate than just a small tuft of grass like many other assets.  This allows me to get more coverage across the hills with fewer instances being used.  The scatter settings for the grass are important.  Having a decent sized gap between the men's scale and max scale will help break up any  incidental repetition you might come across.  And this can be further enhanced by using fall off along with break up to give you a nice  gradient and scale near the edges of the scatter.  These are really the main settings I play with for all the scattered foliage in this scene.  As I've mentioned in previous videos, it's important for us to think in layers when  it comes to building up our environment.  While I wanted the grass on these hills to feel for the most part very uniform, it's  important to remember that pretty much all natural locations will have many different  plants throughout, even if it's mostly just one type of grass or another.  By following this same principle in our scene, we'll not only break things up a bit, but  we'll a...

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_003.jpg

### Working with Proximity in Dash [5:28]
**Transcript:** For this particular scene, I plan to have a small swing hanging from the tree, and I  want to remove the vegetation beneath and around the swing and tree.  While there are a few different approaches I could take for this, I decided to just  go ahead and use Unreal's in-editor modeling tools to quickly create an oblong shape that  roughly feels like what I want for this area.  Then I can just select my grass scatter, and then the mesh I just created, and then I'll  go ahead and click on the proximity icon up here in the dash prompt bar.  This will only scatter the grass within the set threshold around the proximity mesh.  So I'll go ahead and bump up that threshold a bit, and then when I invert the results,  we'll see that the grass has been removed from the area around my model.  From here I can duplicate the masking model I made to extend the coverage out a little  bit towards the tree.  And then I'll go ahead and apply the same proximity masking techniques to the other vegetation  scatters I put in the scene.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_004.jpg

### Hero Detailing [6:34]
**Transcript:** Because the focal point of the scene is the tree and swing, this is really the only area  that I need to add additional levels of detail to.  And I do this by adding some mega scans, ground assemblies from the content library, using  dash's placement tool to quickly move, scale, and rotate them into a position I'm happy  with.  I'll also add some additional scatters to those newly added meshes, and that'll help  add some extra layers of details for these close-up shots I'm planning.  For shots like this that are geared more towards a cinematic approach, it's good to really  focus our attention on the areas that are closer to the camera, adding up those layers  of details while leaving the areas further away from the camera at those broadstroke passes  we did earlier.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_005.jpg

### Rope Swing Creation [7:20]
**Transcript:** As for the swing, it's a very simple setup.  I created two cylinders in a subdivided plank, both of which were UV mapped to mega  scan surfaces.  I then rigged the asset and blender using two bones, and then I just animated it to look  as if it's gently swaying in a breeze before bringing it into Unreal.  Alright, with the swing in place, we're just about wrapped up.  From here, it's just a matter of tweaking and polishing, which will range from adjusting  the lighting, scatter settings, and various materials in the scene, in order to try and  match both our reference images, as well as what I envision the final result looking  like.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_006.jpg

### Camera Setup [8:02]
**Transcript:** Then lastly, we can go into our camera settings to adjust a few post-process settings,  as well as tell our camera to keep its focus on the swing, no matter where the camera's  located.  Now we'll just cycle through a few pre-made look-up textures for our color grading, and  voila, we have our peaceful retreat finished and ready to render out.  I hope this tutorial was helpful for you, and I would love to see your own interpretation  on this scene.  So feel free to join our Discord channel and post your results in the Art Showcase  channel where many artists, including people from the Dash team, participate in the conversation  to help each other grow.  Thank you so much for watching, and I'll see you next time.

**Frame:** tutorials\frames\quick-environment-creation-w-unreal-engine-5\frame_007.jpg


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
