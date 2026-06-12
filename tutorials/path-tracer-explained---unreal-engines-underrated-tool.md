---
title: PATH TRACER Explained - Unreal Engine's Underrated Tool
source: YouTube
url: https://www.youtube.com/watch?v=X5zVhc5ahl0
author: William Faucher
ingested: 2026-06-12
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/path-tracer-explained---unreal-engines-underrated-tool/
frame_count: 0
---

# PATH TRACER Explained - Unreal Engine's Underrated Tool

**Source:** [YouTube](https://www.youtube.com/watch?v=X5zVhc5ahl0)
**Author:** William Faucher
**Duration:** 26m8s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


### B-Roll [0:00]
**Transcript:** This video is sponsored by Skillshare.


### Pathtracer Explanation [0:25]
**Transcript:** Hey everyone, it's great to see you again. It's been a while since my last video, but it's good to be back.  I hope you had a great summer. Now the topic of today's video is going to be all about the new and improved  Path Tracer in Unreal Engine 4.27 that just released not too long ago.  Now previously, the Path Tracer had a number of limitations. It was much slower and it didn't  support the vast majority of material types like subsurface scattering, translocency, skies,  so on and so forth. Now, all those features are mostly supported and it's amazing.  So the Path Tracer rendered what we call a ground truth image. So this is similar to offline  renders like V-Ray and Arnold. It works by casting lots of rays into our scene,  together information about light and color to shade a given pixel. It includes feature  complete materials within reflections and refractions, super-sampled anti-aliasing, and approximate  acoustics, which is totally new. But why use it at all? What's the point? It's slow, it's not real time,  it kind of defeats the purpose of using Unreal. The Path Tracer is extremely useful when you want to  compare your real-time lighting with a fully Path Tracer renderer...


### System Requirements [2:26]
**Transcript:** So in order to enable it and get it running in your engine, you need to make sure that you have  ray tracing enabled in your project. This is a must. There's no way around it. So in order to  enable ray tracing in our project, we need to click on the Settings button up top here, then click  on Project Settings, and you're going to scroll down to the side where it says Platforms, Windows.  Click on the Windows button, and where it says Default RHI, we need to make sure that this is  set to DirectX12. And the next step in the search details panel up top, we can click here and type  ray tracing. And you'll need to make sure that ray tracing is turned on. Now when you click on this  here, a window will pop up asking you to enable the Support Compute SkinCash option. Click yes,  you're going to need this as well. Once that's done, you can restart the engine and you'll be ready  to go. Now we're ready to jump into how to use the Path Tracer and all of its settings.


### Using the Path Tracer [3:14]
**Transcript:** So now the best part about the Path Tracer is you can just turn it on without having to do  anything else in your scene. You don't need to change your materials, you don't need to do anything  else. So what we're going to do is we're going to go to the Lit button up top here and switch  just to Path Tracer. Now be careful, things are going to slow down considerably, and this video will  actually get pretty choppy when I click it. So I'm going to turn this on right here, and you'll notice  that it's now starting to do its thing. It's slowly calculating our samples, our image is getting  progressively better and better. But now you might realize that's just one frame. If I turn the  camera, rotate around, you'll see, oh, this does not look so good, this is really slow, especially  if you're used to, you know, working in the real time, this is the real pain to work with. So all of  our Path Tracer settings are controlled through the post process volume right here. And in the details  panel, we're going to search for Path. And you'll see right here, we have samples per pixel 16,384.  For the sake of this video, I'm going to turn this back down to 10. And because we have the  denoiser e...


### Why Samples Matter [6:39]
**Transcript:** So jumping into Photoshop real quick, we have two renders here. So one was rendered with 10 samples  plus the denoiser and the other one on the right hand side here was rendered with 500 samples  with the denoiser. So at first glance, especially on a compressed video on YouTube,  they may actually look pretty identical. You might not be able to tell them apart, but the moment  you start zooming in, you'll notice that the version with 10 samples really starts falling apart.  So right here on the base plate, the kind of black plastic thing here, I had a roughness texture  with a bit of roughness break up in there. And you can see it here on the 500 sample version of  the render. Whereas in the 10 sample version of the render, the denoiser completely obliterated  all of that detail. There's just everything that's perfectly smooth here. There is no  spec break up. Same thing for some of the details on the shell of our turtle here. So paying  attention to the scale detail on the shoulder versus here and on the top of the head, we have a  lot of scale detail there. There's lots of little nitty gritty stuff. Same thing was the edge of  the shell right here. Whereas on the 10 sample versio...


### Denoising for video [9:03]
**Transcript:** really is mainly intended for use with still images. As you can see here, I have a render with  100 spatial samples with the denoiser turned on and you'll notice that right around here,  or really all across the entire image, it's getting really flickery and jittery and it looks like  crap. The reason for this is because the denoiser is not temporal. And what I mean by this is the denoiser  does not denoise the current frame based on the denoising of the previous frame. So each frame will be  denoised in its own way individually resulting in a super jittery mess like this. Now this can  be mitigated somewhat by either having more samples and adding in from temporal samples in the mix  in the movie render queue. So now you can see right here, the results are much better with temporal  samples. But I've increased the contrast here so that we can see more clearly. We still get quite a  little bit of jitteriness and flickriness in the shadowy areas, especially areas with lots of  details right around the head here and in the area that have lots of lens blur. So just keep in  mind that the denoiser does not necessarily work all that well with animated footage.


### Other Features [10:17]
**Transcript:** Now next up in the details panel, we also have max bounces. Now the amount of bounces you have  here will also affect your render times. So toning down my samples will say 100 instead and turning  my max bounces to 1, you'll notice that we start getting a lot less indirect lighting. So what's  happening is the light comes in, hits our surface and bounces one time. If I do three bounces,  you'll notice we get a bit more indirect lighting, right? We especially our box right here.  The box in the bottom left hand corner is a great indicator of what's actually happening here. So  by setting this down to 1 again, you'll notice our box in a foreground is very dark. Cranking this  up to 10. Now in the darker areas, things start getting lit up a little bit more. There comes a point  of diminishing return when it comes to the amount of bounces. So you don't need to have an insane  amount of bounces. In fact, for many renders, I've kept it at 7. Really, you should only be using as  many bounces as you need. But we'll get a little bit more into that later when we touch base on  the glass materials. Next up, we have filter width here, which says the anti-aliasing filter. So  lower values will ...


### Changes to Materials [13:02]
**Transcript:** So in this section, I want to talk to you a little bit about changes to the way that materials  are handled with the pass tracer. And we're going to take a look at some of these right here.  So first off, we've got the thin translucent model right here, which is kind of like a clear  plastic type of thing, but also cast colored shadows. And we can see right here. Next up, we have  proper pass tracer glass, which looks phenomenal now. And looking at the example here, we now have  approximate caustic refractions and reflections, which is just so nice to have now. Next up, we have  frosted glass, which is the same material as the regular glass material. However, by upping the  roughness of our glass material, we can now have frosted glass. And lastly, right here, we have  random walk subsurface scattering in 426. The pass tracer did not support subsurface scattering.  So this is a really, really nice addition to have in our project. So let's take a look at these  materials one by one, just so that you know how they are set up. So starting off with the subsurface  scattering, the pass tracer now uses a random walk subsurface scattering method, which all happens  under the hood. You don...


### Changes to Skylight [17:04]
**Transcript:** to talk about in this section is a few changes to the way that the skylight is handled with the  past racers. So the past racer does not support atmospheric sky or volumetric clouds. So if you have  volumetric clouds sky setup like this, the one that has like really nice sunsets and such,  you'll notice when we go to the past racer here, the sky goes completely black, you're not going  to get anything. But there is a work around this. So by selecting our skylight in our scene,  if you set it to real-time capture like this, it will capture our sky. So you'll notice it's a  little bit blurry. It's a little bit pixelated and low res. But if we go back to lit mode,  you'll see it is pretty much the exact same result of our sky. So it is capturing our sky  and creating a cube map for us. So going back to the past racer here, even though it's low  resolution, we can fix that. So select your skylight again. And in the details panel, we're going to  set the cube map resolution right here to let's say 1024. And now we have a super high resolution  sky, which is almost the same as the sky that we have in lit mode. Not quite the same, but almost  and this should be good enough for most use ca...


### Skillshare [19:40]
**Transcript:** information, I want to take a moment to thank the sponsor of this video, Skillshare. Skillshare is an  online learning platform with thousands of classes on just about any topic you can possibly imagine,  such as classes relevant to our field of work, 3D modeling, texturing, rendering, filmmaking,  photography, you name it, they've probably got it. And let's say you want to break from being in  front of your desk all day like this guy, you can alternatively take a class on gardening.  So those of you who've been following this channel know that I haven't been on YouTube for very  long at all. I am unbelievably green and I have a lot to learn. And seeing that market is brown  lead now had a class on YouTube success, scripting, shooting, editing with MKBHD, he talks about getting  your audience hooked and growing your channel. I should probably get on that. Skillshare is curated  for learning and they are constantly releasing new classes. And what I mean by this is that it is  entirely ad-free so you can stay focused. So because Skillshare is sponsoring this video, I have a  special link for you down below the first thousand of you to click on the link in the description below  will ...


### Limitations [20:52]
**Transcript:** series of caveats and limitations and things that don't totally work perfectly. So become the  pasture through now supports more features than it doesn't support. I'm going to go ahead and tell  you about the feature that it does not support. So we got hair strands which are not supported,  cascade particle systems, spline meshes, decals, which is a real bummer because I use decals all the  time and so do you probably. But hopefully that comes in later version. Next up volumetric fog,  exponential height fog, light functions, hair and single layer water material types. There is no  multi GPU support and lastly is semi depth of field support. So it's important to keep in mind that  the pass rate is only using the regular depth of field post process. The depth of field is not a  path traced feature. So just keep that in mind. And you can see right here there is some kind of  jitteryness going on in the depth of field areas. I am pushing the depth of field to its absolute  limits here. And while it's not perfect, it's still pretty good. Like the fact that I can get  this kind of result so quickly is phenomenal. So yeah, I might sound harsh toward the devs at epic  but hats off to them...


### Rendering with MRQ [23:06]
**Transcript:** So the path tracer now works flawlessly with the movie render queue as you saw in the intro of  this video. So I'm going to show you how to set it up. Now if you're not familiar with how to  use the movie render queue, you can find a tutorial on it right here and you can find the link down  below. So let's open our movie render queue settings by clicking right here and let's click on  our settings. It is really important to know that when comes to time to render with the movie render  queue, you're not going to control the samples through the post process volume. That is the key takeaway  here. So by going to the settings tab here and adding the anti aliasing tab, the samples of your  path tracer are controlled through the spatial sample count right here. If I wanted to have, let's say,  500 samples, you need to enter 500 right here. You should also override the anti aliasing and set it  to none for better results. But you're also going to want to play around with the temporal sample count.  Because temporal samples will give you much better motion blur than spatial samples. Now keep in mind  that the temporal samples and the spatial samples kind of work together and they multiply ...


### Recommended Render Settings [25:07]
**Transcript:** So my preferred rendering settings are as follows. The temporal and spatial sample counts  completely depend on what it is I'm rendering. But in general, 16 spatial samples and 16 temporal  samples are a really good starting point. And lastly, turn off that denoiser. Yeah, you heard me. Noise  is detail. And removing the noise means removing the detail and your results are going to end on  like a splotchy mess. Like we've seen in the examples throughout this video. So in the example  you saw in the intro, absolutely no denoising was used. And the result turned out pretty okay.  In fact, I prefer to denoise my renders in posts like in DaVinci Resolve or something because I have  way, way more control that way. Once you've determined how many samples you need and the movie  render queue is set up correctly, hit that render button. That's a bit of frames out.  So if this video has helped you out, don't forget to hit the subscribe button. It really makes  a big difference. Thanks so much for watching and I'll see you next time.



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
