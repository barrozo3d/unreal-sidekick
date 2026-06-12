---
title: Demystifying the Skylight [Unreal Engine 4 & 5]
source: YouTube
url: https://www.youtube.com/watch?v=BGoaPyfZlYg
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 4 & 5"
tags: [lighting, skylight, hdri, cubemap, distance-field-ao, ambient-occlusion, reflections, realtime-capture, william-faucher, beginner, intermediate, ue5]
extraction_status: complete
frames_dir: tutorials/frames/demystifying-the-skylight-unreal-engine-4-5/
frame_count: 0
---

# Demystifying the Skylight [Unreal Engine 4 & 5]

**Source:** [YouTube](https://www.youtube.com/watch?v=BGoaPyfZlYg)
**Author:** William Faucher
**Duration:** 13m46s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hi everyone, welcome back.  It's great to see you again and get a little bit lonely in this void here.  The topic of today's video concerns the Skylight Actor.  So the Skylight is one of the most powerful but most misunderstood and misused lighting  tools in the Unreal Engine.  So most of what we're talking about today has already been covered in last week's livestream  right here, but I wanted to make a dedicated video about this because I totally understand  that not everyone had the time to listen to a two-hour livestream.  That being said, this was last month of a two-hour livestream and more of a two-hour  live course.  I was going ahead and talking about the little skylight, talking about my workflow when  it comes to lighting exteriors.  It was a really good time and not just because I was talking for two hours, but you guys,  the community, would have wanted the best part of this livestream.  You guys asked questions, you answered your own questions as well as offering other tips  and tricks that even I didn't even know about.  I've been using Unreal for what, 10, 12 years now and I'm the first to admit that I'm  still learning new things every single day.  I am an eternal ...


### Setup [1:33]
**Transcript:** is to create a Chrome ball.  So we're going to go ahead and add a sphere here.  I'm going to drop it to the end here and I'm going to add a Chrome material to it.  And you'll see the Chrome material is very simple.  It's just a base color of 0.8 or can be one or any other having a metallic set to one  and a roughness at the zero.  Okay.  So this is going to give you a perfectly reflective surface.  Now the reason I create a Chrome ball here is because it's going to give me a better  visualization of what exactly is being reflected in my scene.  Okay.  So you're going to understand how this works real soon.  So bear with me.  Now that we've created our Chrome ball here, I'm going to go ahead and add into light's  panel up here.  So add the skylight.  Now look at the boring part out of the way.  One of the main things that the skylight is used for is for HDRI.  So if you have an HDRI that you got online and you want to use that, you apply that with  the skylight.  So if you have an HDRI that you found online and you want to use that for your lighting,  you apply it to your skylight.  So in order to do that, you need to go into the details panel and in source type right here,  we're g...


### Distance Field Ambient Occlusion [11:22]
**Transcript:** So I've opened a new level here.  It's part of the Australia package that is available for free on the Epic Marketplace.  Let's demonstrate what distance field the ambient inclusion does.  Okay.  So I'm going to select my skylight right here and in the search detail panel, I'm going  to search for distance fields.  And now you'll see we have a bunch of different settings.  So I'm going to totally disable this just to show you what it's doing.  So now this is with this nothing, no occlusion and with occlusion, no occlusion with occlusion.  You'll notice that distance field AO will give you much more oomph to your scene, it gets  much more depth.  And this is totally not ray trace.  This is one of the major advantages of using the distance fields ambient inclusion is  that you don't need ray tracing for it to work and it looks pretty good as well.  So while I do prefer ray trace ambient inclusion, this is a great alternative if you don't  have an RTX graphics card.  And plus performance wise, I do things that run a lot better.  So if you're you know running, if you're pushing your graphics card to its limits, DFAO  is amazing.  And I'll show you guys how to enable that right here.  S...


### Donations and Thanks [13:10]
**Transcript:** And that my friend concludes this week's video.  In the event of this channel, it helps you out in any way.  And you want to donate.  Don't hesitate to check to buy me a coffee button, found on my channel right here.  You can donate to any amount that you want.  It means the world to me and really goes a long way into helping me justify the time spent  making all these videos, making this content available to everyone for free.  So obviously no pressure, but it's much appreciated.  That being said, thanks so much for watching guys.  I hope you learned a little something.  Don't forget to hit that like button and comment down below if you have any questions.  And I'll see you guys in the next video.



---

## Structured Notes

### Core Technique
Skylight actor setup and configuration — Captured Scene vs HDRI source types, Recapture Sky for realtime updates, Distance Field Ambient Occlusion (DFAO) as a non-raytraced AO alternative, chrome ball reference tool for visualizing Skylight contribution.

### Summary
Short but dense tutorial by William Faucher on the Skylight Actor — frequently misunderstood and misused. Covers using HDRI as skylight source, the difference between SLS Captured Scene (captures everything above) and SLS Specified Cubemap (static HDRI), enabling Real Time Capture, and Distance Field Ambient Occlusion as a performance-friendly AO option for non-RTX machines.

### Key Steps

**Chrome Ball Reference Setup:**
- Add Sphere → apply material: BaseColor=0.8, Metallic=1.0, Roughness=0.0
- Shows what the skylight is reflecting → immediate feedback on sky capture quality

**Skylight Source Types:**
| Source | Behavior |
|--------|----------|
| **SLS Captured Scene** | Captures everything above the horizon in the level (dynamic, updates with scene) |
| **SLS Specified Cubemap** | Uses a static HDRI cubemap file (faster; doesn't react to level changes) |

**Enable Real Time Capture:**
- Skylight Details → Real Time Capture ✓
- Updates continuously (more expensive but necessary for dynamic skies)
- Without it: manually press "Recapture Sky" after scene changes

**HDRI as Skylight Source:**
1. Add Skylight to scene
2. Details → Source Type = SLS Specified Cubemap
3. Cubemap = browse to your HDRI asset (.hdr/.exr imported to Content Browser)
4. Cubemap Resolution = 256 (default) up to 1024 (sharper)

**Distance Field Ambient Occlusion (DFAO):**
- Skylight Details → search "Distance Fields" → Enable DFAO ✓
- Adds contact shadow/AO effect without raytracing
- Good for non-RTX hardware; cheaper than ray-traced AO
- `r.AOQuality 2` — set AO quality (0=off, 1=low, 2=medium, 3=high)

### UE Systems / Blueprints / Settings

**Skylight Detail Settings:**
```
Source Type: SLS Captured Scene | SLS Specified Cubemap
Cubemap: [HDRI asset]
Cubemap Resolution: 256 | 512 | 1024
Real Time Capture: True/False
Intensity: multiplier (1.0 = default)
Tint: color tint the sky contribution
Lower Hemisphere is Solid Color: True (prevent black from below horizon)
Distance Field Ambient Occlusion: True/False
Occlusion Max Distance: cm radius for DFAO
```

**Key Note:** When using Lumen, Skylight with Real Time Capture is essential — it provides the sky contribution to Lumen's final gather. A static skylight will not update with time-of-day changes.

### Difficulty
Beginner to Intermediate

### UE Version
UE 4 & 5 (settings apply to both)

### Tags
lighting, skylight, hdri, cubemap, distance-field-ao, ambient-occlusion, reflections, realtime-capture, william-faucher, beginner, intermediate, ue5

---

## Related Entries
- `tutorials/lighting-in-unreal-engine-5-for-beginners.md` — Full beginner lighting tutorial
- `tutorials/tips-for-sky-atmosphere-fog---unreal-engine-5-ue4.md` — Sky Atmosphere complement
- `references/rendering-pipeline.md` — Lumen + lighting settings reference
