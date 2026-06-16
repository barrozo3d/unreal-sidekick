---
title: Easiest Way to Get CINEMATIC Renders in UNREAL ENGINE - Path Tracing
source: YouTube
url: https://www.youtube.com/watch?v=g8aHQqbQfOU
author: Boundless Entertainment
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/easiest-way-to-get-cinematic-renders-in-unreal-engine---path-tracing/
frame_count: 9
---

# Easiest Way to Get CINEMATIC Renders in UNREAL ENGINE - Path Tracing

**Source:** [YouTube](https://www.youtube.com/watch?v=g8aHQqbQfOU)
**Author:** Boundless Entertainment
**Duration:** 9m50s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey guys, Sam here and in today's video I'm going to go over something that I recently discovered in Unreal Engine.  It's a new feature that's been released in the Unreal Engine 4.27 and this is a great feature.  It's been in development for a while but it's just become much more usable in real projects and it's really going to bring your renders coming out of Unreal to life.  Now I want to point out that this is primarily for people using Unreal Engine for filmmaking purposes or for creating realistic cutscenes or animations.  It's not a real-time renderer so you won't be able to apply it to your games but there are alternatives that I'll go over for in-game application if you guys are interested in that.

**Frame:** tutorials\frames\easiest-way-to-get-cinematic-renders-in-unreal-engine---path-tracing\frame_000.jpg

### Lumen [0:33]
**Transcript:** So the new version of Unreal Engine which is Unreal Engine 5 and it's in beta has something similar to what I'm going to talk to you about today called Lumen which works in real time.  So that's a better option to pursue for game developers and real-time performance and I'd be happy to make a video about that if you guys are interested.  But what I want to talk to you about today is called Path Tracing.

**Frame:** tutorials\frames\easiest-way-to-get-cinematic-renders-in-unreal-engine---path-tracing\frame_001.jpg

### Intro to Path Tracing [0:50]
**Transcript:** Now some of you may already be familiar with this concept as it's not a fully new feature in Unreal and it's essentially the same thing as ray tracing which is used in things like V-Ray and 3ds Max and cycles and Blender.  And the concept is that the renderer shoots light into the scene and based on the values you specify in the render it bounces the light off of objects in the scene which creates indirect lighting.  Now this means that Unreal is computing lighting data in a much more accurate way as this is how light behaves in the real world rather than simply estimating or approximating lighting values and behavior which Unreal Engine normally does in order to save resources and allow you to render things in real time.  So as I said before using Path Tracing is going to increase your render times and as a filmmaker render times aren't really a huge deal to me because the alternatives to Unreal like 3ds Max or Blender have monstrous render times and also lack the huge asset of being able to use Quixel Megascans.  Which I went over in a previous video so if you guys want to see more about Quixel head over and check that out.  So the introduction of these new added features to Path...

**Frame:** tutorials\frames\easiest-way-to-get-cinematic-renders-in-unreal-engine---path-tracing\frame_002.jpg

### Setting Up Your Project [2:05]
**Transcript:** So the first thing you're going to want to do is enable ray tracing in your project and to do so we're going to go to the Settings menu and then we're going to go to Project Settings.  And in the Details box here we'll just search for ray tracing and it'll come up here we're going to click the little check box to enable it and it might come up with a little dialogue box asking about something just click OK because we're going to need to enable anything that it asks you about.  The next thing that we're going to do is we're going to go down here to Platforms and we're going to go to Windows and make sure that your default RHI is set to DirectX 12.  OK so once you do all that stuff you're going to have to restart your engine. So now we can enable Path Tracing and to do so we're going to go up here to where it says Lit and we're going to click on that and we can go down here and now we have this Path Tracing option.

**Frame:** tutorials\frames\easiest-way-to-get-cinematic-renders-in-unreal-engine---path-tracing\frame_003.jpg

### Enabling Path Tracing [2:46]
**Transcript:** And so I'm going to click that and immediately you'll see it gets very grainy and the grainyness goes away but as you can see we can look around here and our lighting is much different now.  So our lighting is much more realistic if we go back to the Lit mode. So we go back to Path Tracing now you can see we have all this all this extra stuff all this light that's filling in the shadows and that's being bounced off of the objects in the scene.  And it's also coming from our HDI SkyMap so if we go to our camera here we can see there's a huge difference between the Lit and the Path Tracing.  So when you first enable Path Tracing it might be very slow and it might be really really grainy so the reason for that is because your sample count is too high.

**Frame:** tutorials\frames\easiest-way-to-get-cinematic-renders-in-unreal-engine---path-tracing\frame_004.jpg

### PathTracing Parameters [3:34]
**Transcript:** So what you can do is add a post processing volume and I've already done that so I have it here and in our details we're going to search for Path Tracing.  Okay so it already comes up here. Now yours might be set to 32 and some like really high number like 16,000 or something.  What you want to do is click little checkbox next to these enable them and then you're going to be able to adjust your bounces your samples also this denoiser which is can be a bit of a hassle.  So the first thing I'm going to talk about is your samples. Now the reason your computer is probably lagging is because you have too many samples so if you reduce this number it's going to fix that problem.  For the more samples you have the more detail you're going to have in your scene. So you want to keep this as high as possible while also not overloading your computers.  So for the sample setting I'd recommend something round 500 you don't want this to be too high because it's going to increase your render time and you don't want it to be too low because they're not going to get as much detail.  Now for the max bounce setting it's initially set around 32. I find this to be a bit overkill because for our bounces ...

**Frame:** tutorials\frames\easiest-way-to-get-cinematic-renders-in-unreal-engine---path-tracing\frame_005.jpg

### Unsupported Features Demonstration [6:28]
**Transcript:** So those are the main settings for enabling path tracing it's very convenient no modifying textures or objects or anything like that just a few parameters and we're done.  Now I do want to point out that not all features of Unreal Engine are supported for path tracing.  Volume metric fog and exponential height fog are two big ones that are not supported but I'll leave a full list below.  So if I go to my exponential height fog in this scene if I set it to visible you can see it doesn't turn on and then if I go to the lit version now it's here.  So exponential height fog is not supported so that's unfortunate but there are ways to add things like fog to your scene using alternative methods as you can see here I've added fog back into my scene.  So if you guys wanted to tutorial on how to add fog to your scene without using exponential height fog let me know and I will gladly make one.  So now we're about ready to render our scene with path tracing so I've opened up our sequence here and now what I'm going to do is we're going to click on render and that's going to bring up our movie render queue.

**Frame:** tutorials\frames\easiest-way-to-get-cinematic-renders-in-unreal-engine---path-tracing\frame_006.jpg

### Render Settings for Path Tracing [7:17]
**Transcript:** And we're going to go into our settings here and we're actually I'm actually just going to make a new job and we'll go down and find our shot here.  Okay and we're going to go into our settings and we're going to delete the export settings and we can go to our output settings instead of whatever you want but that's not important for this part of the tutorial.  So what I'm going to do is add anti aliasing and then I'm also going to go down here and add the path tracer and then you can choose your your format of output.  I'm just going to do pro res but you could do you know an ex r for as much detail as possible it's going to give you a lot of information but for now I'll just do a pro res.  We don't have to modify anything in this but that's just going to tell us to render using the path tracer and then if we go into the anti aliasing we can go into our sample count and we have our spatial samples and temporal samples and now what that's going to do.  These two values actually multiply each other but you need to have some some value for each of them because if you don't have spatial samples you're not going to get as much detail in each frame and if you don't have temporal samples ...

**Frame:** tutorials\frames\easiest-way-to-get-cinematic-renders-in-unreal-engine---path-tracing\frame_007.jpg

### Closing Thoughts [9:20]
**Transcript:** This is an excellent tool for filmmakers especially indie filmmakers and I imagine that it's only going to improve with time don't forget to like and subscribe it really helps me to grow my channel and make better videos for you guys.  So as always thanks for watching and have a good one.  Thanks for watching.

**Frame:** tutorials\frames\easiest-way-to-get-cinematic-renders-in-unreal-engine---path-tracing\frame_008.jpg


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
