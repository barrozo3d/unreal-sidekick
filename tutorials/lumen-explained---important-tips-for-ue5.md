---
title: Lumen Explained - IMPORTANT Tips for UE5
source: YouTube
url: https://www.youtube.com/watch?v=1e6oOiKh91U
author: William Faucher
ingested: 2026-06-12
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/lumen-explained---important-tips-for-ue5/
frame_count: 0
---

# Lumen Explained - IMPORTANT Tips for UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=1e6oOiKh91U)
**Author:** William Faucher
**Duration:** 16m2s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back. It's great to see you again. William Fosha here.  Today's video is about Lumin. Now this video may come across as a little wordy,  long, dry, and while Lumin is fairly user friendly and works very well out of the box,  there are several changes to the way you need to make your models and materials  moving forward. So I promise you, your work will improve. If you just bear with me to the end here,  this is quite possibly one of the most important videos I've made in a while.  I know I've made a video about Lumin back in May, but that video was made three days after  UE5 dropped and I've addressed a few issues there, but Epic has since released additional information,  making that earlier video a bit outdated somewhat. So in this video, I've gathered all,  was the latest and greatest information available, most of which gathered from Epic's amazing  livestream on the topic that said their livestream is over two and a half hours long and while  they are goldmine of information, a lot of it goes way deeper than necessary for the average artist.  So that's where this explain series of videos come in. I want to condense the info from  those livestreams into a ...


### Skillshare [1:15]
**Transcript:** So this video is sponsored by Skillshare, and as you all know by now, Skillshare is an online learning  platform which thousands of classes are creative artists or just curious people to explore new skills  and dive deeper into existing hobbies or passions. It's your curious about virtual production,  shooting video, filmmaking, Skillshare offered a large variety of classes on cinematography,  like this short and sweet 30 minute class by Zach Mulligan called cinematography basics,  understanding filmmaking, which covers the key basics and fundamentals of film,  the mood, the tone, and the feel. Skillshare's classes are curated, they have really high production  quality, they're ad-free, and there is a constant stream of new classes for you to choose from,  and since many of you watching this channel are from all corners of the globe, it's worth  mentioning that Skillshare's entire catalog of classes now offers subtitles in Spanish,  French, Portuguese, and Dutch. Now because Skillshare is sponsoring this video, the first  1000 you to click the link down below will get a one month free trial of Skillshare,  so you can start learning today. So once again, thanks so much for Skillshar...


### Project Settings [2:24]
**Transcript:** video, and with that out of the way, let's dive right in starting with the necessary project  settings for Lumen. Now by default, Lumen is active and you don't need to change anything, but in  the event that you've migrated a UE4 project over to UE5, here is what you need to set it to.  Dynamic global illumination method set the Lumen reflection method set to Lumen,  generate meshed in fields, needs to be on, in editor, Lumen is controlled by the following values,  the light properties, the material base color and roughness, and the exposure. Lastly,  you do have some quality control settings in the post process volume,  final gather quality, and Lumen reflection quality, which we're going to dive a little bit deeper  into real soon. Next, let's talk about what Lumen can do, the obvious and the not so obvious.


### What Lumen Can Do [3:07]
**Transcript:** The obvious being it achieved real-time indirect lighting with rather surprising accuracy,  and as we all know, immersive lighting does contribute to GI. Just to be clear, when I say GI,  moving forward, I mean global illumination. So if you have a large, bright material, it will  light up your scene. There are several limitations to this, which again, we will get into a little  bit later. Lumen also provides reflections and integrates GI into the reflections as well. So  what I mean by this is you will see all of the GI in the reflections. This is something that  rate rate reflections didn't really do very well in UE4. Lumen also supports clear coat materials  properly so that there are two reflections, not just one, which is really useful for car materials.  Again, this is something that rate rate reflections really can't do at the moment. It also supports  fully shadowed skylight. So drag and dropping a skylight set to movable will shadow everything  automatically with no additional input from the artist. It provides dynamic GI and sky shadowing  on translucency and volumetric fog albeit at a lower quality. Lumen makes things so much easier for  artist. There's a way less fiddli...


### How Lumen Works [4:33]
**Transcript:** So how does this all work? In pure nerd talk, it is a hybrid ray tracing pipeline, which uses software  ray tracing. It traces against the depth buffer first, which we call screen traces, then it  traces against the distance field and applies lighting to ray hits with the surface cache.  Lumen relies heavily on mesh distance fields, but what's worth noting here is that the mesh  distance fields have been completely rewritten in UE5 for youth with lumen specifically, and they are  way way better than they ever were in UE4. The mesh distance fields now have mid maps,  they're streamed from disk based on distance, and they cost about half as much in terms of memory  compared to UE4. They also build 10 times faster than before, which is a massive upgrade.  If you remember back in UE4, building mesh distance field took a very long time. That is no  longer the case here. Now while all this takes care of shadows, it can determine material color  and lighting of a surface, so that's where the surface cache comes in. The surface cache


### Surface Cache (SUPER IMPORTANT) [5:35]
**Transcript:** essentially splits up your meshes with a bunch of cards. It captures material properties of the mesh,  color, roughness, act very low resolution into an atlas, which does work especially well with  nanite meshes. It also constantly updates its atlas as you fly around your scene. It's worth noting,  however, that these recaptures are very slow on non-nanite meshes. So if you notice your  frame rate just tank for no apparent reason, try and see if your environment has some non-nanite  models lying around. They could be the culprit, especially if those meshes don't have proper  LEDs set up. You can visualize the surface cache with the following console command right here.  TLDR, if you're going to use lumen with any high poly assets, they pretty much need to be  nanite if you want good frame rates. Now that was a whole lot of boring talk. Why should artists  care about this crap? The surface cache has one major, major limitation and this is what's going  to affect how you create your assets and your models. Only simple meshes and interiors can be  supported. And what I mean by this is you can't simply just use one large combined mesh for an  interior, for example, walls, floors, ceili...


### Lumen Scene (ALSO IMPORTANT) [7:21]
**Transcript:** the most important view mode for Lumen, because if you're a Lumen scene doesn't roughly match  what's on your main screen, there's going to be view dependent artifacts in the GI. If you've  ever noticed that Lumen GI is sometimes screen space, that is why. Something is wrong. The Lumen  scene is your number one tool for seeing what is Lumen doing. Why is there an artifact? You can  A.B. compare this between view ports and make sure they look roughly the same lighting wives,  color rise, etc. It's really convenient to use the G-Short Cut, especially if you're seeing  meshes or objects that are black like this in the Lumen scene. Something is wrong and that object  is not contributing to GI. Black models in the scene means that they are only going to show up in  screen traces, which is why the lighting will appear and disappear in a screen space fashion.  But now, let's talk about some of Lumen's limitation and the very important things to know.


### Limitations & Things to Know [8:16]
**Transcript:** For now, only static mesh and instant static meshes are supported, meaning there is no landscape  support for this at the moment, but it is coming in 5.0. World position offset causes artifacts,  so anything win-related can be problematic. Translucent materials are also not yet supported for  Lumen reflections or dynamic GI, so glass is not going to look right. The interesting thing is that  subsurface scattering does not work with Lumen, but subsurface profile does. It's what I used to  give the snow on the ground here a subtle subsurface scattering look. Lumen also happens to rely heavily  on temporal super resolution, which is similar to Nvidia's DLSS. This means that it calculates in 1080p  and it upscaled everything to 4k resolution, all while looking nearly as good as a native 4k.  Temporal super resolution, TSR, is really the key to making Lumen possible in real time. Lumen  does allow hardware ray tracing, which offers the highest quality, but also the highest cost as well.  And it only has partial support in early access, such as raytrade reflections, shadows,  and it is part of the final gather. Hardware ray tracing traces against the Nanite proxy geometry  only, so you m...


### Raytraced Reflections [11:18]
**Transcript:** for Archvizardus. You may have noticed that in many cases, reflections are just kind of,  the kind of blare, especially if you're used to the gorgeous, sharp and crisp,  raytrade reflections of Ub4. I'm going to tell you all about the magic sauce to get the raytrade  reflections and Lumen combined together in just a second. By default, Reflection uses Surface  Cache, which is great for performance, but as you know, it doesn't look so hot. Most people  seem to think that you can either use only hardware ray tracing or Lumen not vote. Unfortunately,  you can get the best of both worlds. So first, open up your project setting and in the rendering  section, you need to make sure you hardware ray tracing when available and support hardware raytracing  are turned on. Next, search for default RHI and make sure this is set to DirectX 12. Then restart  on real. Lastly, you need to set the Lumen Reflection quality setting in the post-process volume to four.  That is the magic number and that solves our issue. Now, you can get both Lumen lighting and  raytrade reflection to work together in harmony. Now, for the last part of this video,


### Best Practices [12:29]
**Transcript:** I want to talk about the best practices using Lumen. So this is a very important part of the video.  First off, you cannot use Lumen and the Mrs. Meshes to replace light sources. They're going to have  a bad time if you do. Results are going to be noisy and inconsistent and possibly even screen space  in many cases. Lumen does pick up a Mrs. materials as we've seen before. But the smaller and brighter  that a Mrs. source is, the noisy or the result will be. So if you're using a Mrs. materials with  Lumen, keep those sources large and dim for best quality and then go ahead and add an actual light  to give your scene the brightness you want. You the rec light or a point light, spot light,  whatever, just don't rely on only using a Mrs. materials. It's going to look bad. Very small  and bright material sources like particles or small lights on the wall of a sci-fi scene  are going to be notably problematic. Next, the base color has a huge impact on GI.  Now for note of us coming from an offline rendering or a VFX background, this is obvious. Dark and  busy base colors are going to have a poor impact on GI while bright Abyto values will bounce  the light around more. Again, obviously, ...



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
