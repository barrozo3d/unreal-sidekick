---
title: How to Get Clean Lumen Lighting in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=wOx_jPKWYCE
author: TUF
ingested: 2026-08-19
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-get-clean-lumen-lighting-in-unreal-engine-5/
frame_count: 0
frame_status: pending-selection
---

# How to Get Clean Lumen Lighting in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=wOx_jPKWYCE)
**Author:** TUF
**Duration:** 10m34s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-get-clean-lumen-lighting-in-unreal-engine-5 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Lumen is great but let's be honest, for a lot of people it looks really bad and not
[0:07] because Lumen is broken but because how we set it up.
[0:11] In this video, I will show you how we can set up Lumen scene to get clean lighting inside
[0:17] Unreal Engine, nothing fancy, just the basic stuff that I use and actually work and I will
[0:24] be explaining things as I go.
[0:26] So listen carefully and try to watch till the end because all these small things will
[0:31] help you to improve.


### Project Setup [0:33]
**Transcript (timestamped):**
[0:33] So first thing I use game template to create my projects and in third person and I always
[0:41] use quality preset as maximum.
[0:43] You can set it to scalable but maximum is fine, is best for most cases.
[0:49] And here I have a project named Lumen where I have something a level called demo and here
[0:58] I have basic lighting, a room with a character, character is not important, it just I did


### Lumen Project Settings [1:05]
**Transcript (timestamped):**
[1:06] it just for fun.
[1:08] And now go to edit, go to project settings, scroll down and go to rendering and again scroll
[1:17] down and here we have global illumination method set to Lumen, reflection method is
[1:25] also set to Lumen and reflection capture resolution is set to 128.
[1:30] If you have too many reflections, for example if you are working on ArchViz project then
[1:37] you have to increase it.
[1:39] I usually set it to 2048 which is good for getting good reflections and make sure you
[1:47] are using hardware ray tracing when available and also enable sport hardware ray tracing
[1:54] then you will be able to enable it.
[1:57] And you need to have a Nvidia card or AMD graphics card in order to use hardware ray
[2:03] tracing.
[2:04] I think Intel cards sport ray tracing now as well but I am not sure.
[2:07] So since I have Nvidia so I am going to use it.
[2:12] Ray lighting mode should be set to hit lighting for reflections, you can leave it on surface
[2:17] cache but I use this method and here we have software ray tracing mode if you want to use
[2:24] it then you can just change it to detail tracing if you want but we are using hardware ray
[2:30] tracing so I am just going to ignore it.
[2:33] Now also enable ray tracing translucent reflections and I am using ray traced shadows and for
[2:41] shadow maps I am using virtual shadow maps.
[2:44] And next we have mega lights if you have too many lights in your scene then just enable
[2:50] mega lights and that's it for the settings here.
[2:56] Now scroll down and I think go to windows, on the platform go to windows and here change
[3:05] default RHI to directx 12 instead of Vulkan or directx 11.
[3:14] Now close it.
[3:15] Now next we have to add a post process volume to our scene.


### Post Process Volume Setup [3:20]
**Transcript (timestamped):**
[3:20] Let me do it again.
[3:22] Just go to this button and then add a post process volume.
[3:26] First thing I am going to set it to infinity like unbound and now I will search for exposure
[3:35] and I will change the metronome to manual to control the exposure.
[3:41] Okay, now this is set.
[3:46] Next search for lumen.
[3:50] And here we have all the settings.
[3:54] I am going to enable all of them and I am going to explain few things and I don't have
[4:01] any reflections here but if you have you also can enable the reflections and set the bounces
[4:07] to 6 and reflection bounces to 6 and if you have any glass materials or mirrors I think
[4:17] the glass material need reflection or the water materials then set it to 12 if you want.
[4:25] I think 12 is fine for now since I don't have any glass or water materials in my scene so
[4:33] I won't be able to show you.
[4:35] But you get the idea like if you increase the samples you will get better results.
[4:40] Now here some YouTuber shows you fix like if you get any flickering light in your scene
[4:47] then they usually keep their final gather quality to 0.25 so they will see any flickers
[4:54] here if I add a light in my scene for example I have this light right.


### Fix for light flickering in Lumen [5:00]
**Transcript (timestamped):**
[5:08] But I don't see any flickers I don't know maybe my preset is set to maximum but that's
[5:14] why there is no flickering here but in some cases yes if I reset this the scalability to
[5:22] epic now we can see the flickers but instead of increasing that the scalability we can
[5:29] just change gather quality Lumen gather quality to 1 and you can see it is fixed most YouTuber
[5:37] will show you that's how you fix it but that's not the actual fix for that.
[5:44] In order to fix that there is one method select your light and search for ray trace and here
[5:50] we you can enable it and then here we have the samples per pixel and we can increase
[5:56] the samples if we get flickering on one then you can increase it to 4 it is going to fix
[6:02] most of the flickering but you have to do it for each light and I don't suggest you
[6:07] to do like change lighting for every light just do it for the one that are closer to
[6:13] your camera so you don't tank your FPS you know the scene would get heavier if we have
[6:21] more samples I mean extra samples means load on your GPU.
[6:27] Now let's save all and let me open this abandoned apartment project by Megascans and then let
[6:35] me show you something so this you can just download it from fair marketplace and then
[6:42] you can practice the lighting if you want but I just want to show you some basic things
[6:47] from here not the basic but the fixes I know for most cases for example now we have a scene
[6:55] completely built and the scalability is set to cinematic and we still see the flickering
[7:00] right so to fix that there are methods and in this case let's go for here we have the
[7:11] light here we have the direction light for example first let's search for ray trace and


### reason for FPS tanking [7:14]
**Transcript (timestamped):**
[7:19] the samples are 16 it means the direction light has higher sample there is no problem
[7:24] with that but let's go to skylight so here we have the samples are set to one so if we
[7:30] increase it to four as you can see the flickering is going away and if I set it to 16 like direction
[7:36] light now you can see the flickering is completely gone but it is tanking my FPS for sure so
[7:46] if I search for FPS here we have 30 FPS but like 50 60 FPS so if we have it one now you
[7:56] can see the FPS boost but if I set it to 16 the FPS will drop so that's the way to fix
[8:04] it if you are working on our quiz then this is the method you should use I mean you can
[8:10] get the higher quality results and you have to do it for all the lights not just for this
[8:16] one for example I just have skylight and direction light here but if you have rack light point
[8:22] lights I mean all type of lights you need to increase it but depending on the distance
[8:26] from your camera now some of you may one may wonder like if you guys have post process
[8:35] volume and change the value for final gather quality for example here and if we increase
[8:43] it but it won't fix everything if the lights have lower samples the increasing the final
[8:48] gather quality won't help unless you are optimizing your scene and setting the values according
[8:53] to your scene and more lights means you need to change more settings and here I have this
[9:00] light right and the samples are also set to 16 that's why there is no flickering around
[9:07] here so this is that's all for this video because there is nothing else I can show you
[9:16] not to improve your lighting for interior and exterior the lighting is different the
[9:20] values will be different according to your setup and all the project so this is the important
[9:27] things I thought I should cover I covered the project settings I also covered how we can
[9:33] set fix the lighting and yes there is one more thing for example if we are changing
[9:41] the settings if we already change everything in project setting then leave it on project
[9:46] default but if you are did not change anything there like you did not change the relighting
[9:54] mode to reflections then you can change it here and also there are advanced settings
[9:59] for example for diffuse color boost I don't know what's the use of it but if we increase
[10:05] it we get the diffuse color boost as you can see I mean why it's there I don't know but
[10:11] yes sometimes it's helpful okay so thanks for watching if you still need any help with
[10:19] lumen setting up lumen is easier use post process volume if you have different volumes
[10:25] in your scene then always make a global process volume that can control the lumen quality



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
