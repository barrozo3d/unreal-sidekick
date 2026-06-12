---
title: How I Made This Shot in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=HbGJyQVq3tk
author: William Faucher
ingested: 2026-06-12
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-i-made-this-shot-in-unreal-engine-5/
frame_count: 0
---

# How I Made This Shot in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=HbGJyQVq3tk)
**Author:** William Faucher
**Duration:** 14m31s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In a video I made a few months ago, I 3D scanned my old, reliable acts and I made these  3 shots in Unreal Engine 5.  Now a lot of you asked me to make a video about how these shots were made.  So here it is.  I'll show you my workflow and process from start to finish, from the 3D scanning part  to mesh clean up and texturing, to flushing out the environment in Unreal Engine 5, lighting,  rendering, and color grading as always.  Now full disclosure, this video is sponsored by Catchering Reality and I use Reality  Capture to scan this acts.


### 3D Scanning [0:32]
**Transcript:** I have many tutorials on 3D scanning, but this time around the process was a little bit  different.  Reason being, the acts itself has many different material types.  A well aged wooden shaft, high carbon steel, a leather sheet with brass rivets, so I wanted  to make a high quality asset that rendered cleanly in Unreal Engine because I knew this  would be a close up shot.  And when you're doing a hero shot like this, the 3D models need to hold up to a whole  lot more scrutiny.  So step one, scanning the acts itself with the help of photogrammetry.  To make my life a whole lot easier, to not have to move the camera around so much, I mounted  the acts on the ceiling with a rotatable arm.  That way the camera can stay fixed on a tripod and all I need to do is spin the acts at  5 degree increments and taking photos from every angle.  The chunker camera rig you see here is a cross polarized setup.  The purpose of this flash and filter is to cut out all reflections on an object, giving  you a very matte look, which is ideal for photogrammetry because you need consistency between photos.  And when you have reflections, note reflections shift and change based on view angles, right?  Which ...


### Texturing [3:56]
**Transcript:** That provide a good foundation to work from, but it's really only the base color that  we get, the albedo map.  I needed to bring this texture into the substance painter because we need to ensure proper, fitically  based material definition between the various types of surfaces.  Wood, steel, leather and brass.  Like I said, the base color and normal map texture we get out of reality capture is fantastic.  Working in painter however just allows us to push this even further.  With our model exported, our textured, exported out of something painter, now the time to jump


### Into Unreal Engine 5 [4:31]
**Transcript:** into Unreal Engine 5.  With Unreal Open, the first thing I love to do is to set up a basic daylight system using  the environment light mixer.  And in just a few clicks, we've got a fully dynamic sky and clouds, totally free, which  helps us see what we're doing.  I like doing it because I don't like working in a black void.  So having a decent lighting setup to work with is a good starting point.  Now after that, the first step in creating any shot is establishing the composition, the  framing, setting up the camera early on.  Really this should be roughly one of the first things you do.  Place your subject in the frame, place a camera, and get that composition nailed down before  you start spending any time flushing out your scene.  You want to start working on only the things the camera will see.  There's no point in spending hours making a beautiful level, only to realize that most  of your hard work isn't even going to be in the frame.  You get the point.  Then I just move my directional light in the rough direction I want it to come from to  establish the initial lighting path.  But because my end goal here is to render a top quality, no exceptions kind of image,  I went with...


### Times of Day [11:06]
**Transcript:** But that done.  Before rendering, I decided to have a little bit of fun.  Just the tries in different times of day, I went for an overcast feel and a night time shot.  Really, this is purely creative work.  Having fun with the various lighting tools in Unreal, I recommend watching my dedicated  lighting tutorial right here to learn the basics, as there are a hundred ways to light  a shot and all of them are valid.  You just need to know what you're going for and the tools available to you.  For the overcast day, I simply use a skylight with an htri found on htrihaven.  And for the night time shot, it's really just the blueish direction of light and I added  a point light to simulate campfire.  With our shots done now, we move on to the rendering and collocrating phase.


### Rendering [11:48]
**Transcript:** So I'm going to be rendering these out at max quality using the movie render queue.  Here we can determine the resolution we want, the console variables we want, and the anti-aliasing  or sampling settings.  Then the post-process volume under the path tracing tab, I'm going to disable the denoiser  because I will denoise myself in the vintage resolve, but we're going to get into that  real soon.  In the movie render queue, be sure to delete the deferred rendering tab and add the path  tracing tab instead because we want the path tracer.  Always render in 16 bit exr to get the highest bit depth, which gives us flexibility and  post.  In color output, be sure to disable the tone curve.  And under anti-aliasing, override anti-aliasing should be checked, set AA metad to none, and  with the path tracer, 16 by 16 is a good starting point.  Troubleshooting path tracer renders is really easy.  It's your shot to noisy, you need more samples.  That's all there is to it.  In the output tab is where I determine my desired resolution, and in this case, I want  4K.  When you're ready, hit that render local button, and wait.  The path tracer is way slower than a deferred renderer, so go make a sa...


### Davinci Resolve Denoising [13:04]
**Transcript:** 6 hours later.  Now, I've talked about this in many videos.  I even have a whole video dedicated to color grading and vintage resolve, but really,  this part of the process is where you really make your render shine.  Color grading is entirely subjective.  What one person might like, another person won't.  There isn't a good or bad way to grade.  It's all about the taste and getting to look you want.  I don't want to spend too much time on nitty-gritty here, because again, I've made two whole videos  on color grading and resolve already.  The one thing I do want to show you, however, is denoising and resolve.  Because the path tracer by nature is going to be substantially grainyer than when you use  the deferred rendering.  In the free version of resolve, select your imported clip and go to the Fusion page, press  SHIFT, space, and add the noise reduction tool.  From there, your denoise setting will be on the right.  If you own the $300 studio version of resolve, you can add the noise reduction in the color  page, which is, by far, my preferred way of working.  I generally don't really enjoy using Fusion.  So here's a quick before and after of each of the three final renders I did....



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
