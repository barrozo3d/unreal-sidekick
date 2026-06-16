---
title: Unreal Engine Depth Fog TUTORIAL [Path Traced]
source: YouTube
url: https://www.youtube.com/watch?v=0ltfUCHwevY
author: Boundless Entertainment
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-depth-fog-tutorial-path-traced/
frame_count: 6
---

# Unreal Engine Depth Fog TUTORIAL [Path Traced]

**Source:** [YouTube](https://www.youtube.com/watch?v=0ltfUCHwevY)
**Author:** Boundless Entertainment
**Duration:** 9m6s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Let's go on guys. So in today's video I had a lot of requests to go over how to create fog and unreal engine without using exponential height fog and an important part of this is that we want to have fog that works with the path tracer and unreal engines.  So if you don't know what path tracing is, I have a video, I'll link it up in the corner here. But essentially it's like ray tracing where it shoots light into your scene.  So the light comes in, it bounces off of the objects in your scene and it causes indirect lighting, bounce lighting and reactive lighting. Path tracing doesn't work with exponential height fog and fog is a big thing that you want to be able to add. It just adds a lot of depth to your scene.  And it's kind of a big deal that path tracing doesn't work with exponential height fog. So we want to find a way around that. I'm going to show you guys how to do that right now.

**Frame:** tutorials\frames\unreal-engine-depth-fog-tutorial-path-traced\frame_000.jpg

### Demonstration [0:45]
**Transcript:** Alright guys, so we're here in unreal engine and what I want to do here is show you guys how you can get this fog effect. So I'll show you what it looks like with the turned off. So that's it turned off and I'll turn it back on.  So that's what we're going to be creating and you can see that it works in path tracing fully.  So we can go back to lit mode if we want and it'll work there or we go back into path tracing and we get our nice realistic lighting here. So you can see it works very well.  Alright, so I'm going to show you guys how you can do this. I'll turn off this post processing volume and I'm going to just do your thing from scratch.

**Frame:** tutorials\frames\unreal-engine-depth-fog-tutorial-path-traced\frame_001.jpg

### Post Processing Volume Setup [1:16]
**Transcript:** So the first thing that we need to do is add a new post processing volume. So I'm going to search post process volume and we're just going to drag it into our scene here.  The first thing we're going to do is search bounds. So you can see under our post process volume settings right here we have infinite extend and we're just going to click true. So that's going to extend the bounds of our post processing volume to the entire scene so that we're not only getting a small area that's affected.  And the next thing that we're going to do is we're going to search material and we're eventually going to do this. But first we have to do is create a new material.  So I'm going to hit right click and create a new material and we'll call it fog.  I'm just call it to have a unique name. And then what we're going to do is we'll go over here to where we search material within our post process volume.  And we're just going to click this little plus button to add an array element and then we're going to hit asset reference so that we can then take our fog here.  And we're just going to drag it over and we're going to drop this material into our asset reference. So what's that what that's going to ...

**Frame:** tutorials\frames\unreal-engine-depth-fog-tutorial-path-traced\frame_002.jpg

### Creating Fog Material [2:50]
**Transcript:** Okay, so we're in our fog material and now there's a couple things that I want to set up before we actually get into creating this material. It's very simple, very basic.  But the first thing I want to do is we're just click out into so we have our general material selected and we're go over here to the details panel.  And what we're going to do is change the material domain from surface or whatever it's currently said to down to post process.  That's going to allow us to only affect the emissive color and it's also going to make sure that we're only affecting this post process volume.  If you don't do this, you're going to get some errors. So make sure that you do that before you start or at least before you apply the material.  So then the next thing that we're going to do is we have to change blendable location. So we're going to go to our details and search blendable.  And you can see it comes up here, blendable location. And what we're going to do is change it from after tone mapping to before tone mapping.  And what that's going to do is if you don't do this, I'm not sure if it has this effect in the path tracing mode.  But if you are viewing your scene in the lit mode, it ma...

**Frame:** tutorials\frames\unreal-engine-depth-fog-tutorial-path-traced\frame_003.jpg

### Modifying the Fog [6:45]
**Transcript:** And now we have this nice layer of fog and we can always turn this off to see what we're doing.  So that's what it was before. And now we have the fog. And as you can see, it works with path tracing.  So this is very effective and you can move throughout your scene and it constantly stays the same thickness as you move.  And it's very quick. It's not very heavy on your GPU.  And once again, it also works in the lit mode. This is what we're going for.  And if you go back into your fog material, you can change all the settings you want so we can change our distance so that it's much closer to us.  So we'll set it to a thousand. We'll click apply. And now we have really, really thick fog.  That's very close to us. And then we can also increase our density or opacity.  And maybe I'll just make this a little further away so that you can still see something.  So I'll set the 5,000. We'll click apply. And there we go. We have very thick fog in our scene.  So you can basically just customize this any way you want. And we can also always change the color of the fog by changing that vector parameter.  So we set it to something like a nice teal color. Click OK. And we'll apply that. And now w...

**Frame:** tutorials\frames\unreal-engine-depth-fog-tutorial-path-traced\frame_004.jpg

### Final Thoughts [8:29]
**Transcript:** So I just want to say thank you to everybody supporting the channel. We've passed 1,000 subscribers, which is amazing.  If you guys like this video, leave a like and also leave a comment if you guys have any suggestions for future videos or if you want to say something about this video.  I love to hear the discussion. And also don't forget to subscribe for future content. I'm working on a course for filmmaking and Unreal Engine.  And I have a lot of new content coming up from that as well as a lot of other things. So you don't want to miss that stuff.  So thank you guys for watching and have a good one.

**Frame:** tutorials\frames\unreal-engine-depth-fog-tutorial-path-traced\frame_005.jpg


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
