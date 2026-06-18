---
title: Realistic and Physical Lighting in UE5: What is PBL ?
source: YouTube
url: https://www.youtube.com/watch?v=JoxgvwNFc8g
author: arthur tasquin
ingested: 2026-06-18
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/realistic-and-physical-lighting-in-ue5-what-is-pbl/
frame_count: 6
---

# Realistic and Physical Lighting in UE5: What is PBL ?

**Source:** [YouTube](https://www.youtube.com/watch?v=JoxgvwNFc8g)
**Author:** arthur tasquin
**Duration:** 15m52s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, my name is Arthur and I'm a real-time artist with past experience in the  VFX industry.  This is the first video of a two-part tutorial series in which we'll be talking about  lighting and most specifically the science behind it.  While I will be using and relinging to demonstrate my points, what I'm seeing here can be applied  to many different cases.  Whether you're lighting for films, animations, games or cinematics, I'm convinced it can  take something out of these tutorials.  In this video, I'll go through my own journey learning physically based lighting and break  it down in a way that makes sense for digital artists.  As I share my experience, including the hiccups along the way, we'll dive into the basics  and how it all fits in an relangion.

**Frame:** tutorials\frames\realistic-and-physical-lighting-in-ue5-what-is-pbl\frame_000.jpg

### Lighting Studies [1:00]
**Transcript:** A common exercise for any aspiring lighting artist is lighting studies.  You've probably seen a ton of them on our station.  The idea is simple.  You take a single environment and you create multiple lighting variations of it.  By working exclusively on those variations that we also call lighting scenarios, you can  focus on what matters.  In 2024, I started to work on one of those projects.  I was inspired by photographs taking during my daily morning commute.  Eventually, it became quite a technical challenge as the project grew over seven distinct scenarios.  So I had to find a workflow to easily switch between lighting setups.  Using a mix of sub-levels and dedicated level sequences, I was able to contain everything  in one place.  Now, with my background in the film industry, I wanted to use reflectors in Unreal.  On movie sets, reflectors are pieces of fabric designed to reflect or absorb lights.  This technique, even in CG, gives you way more control over the lighting.  This kicked off a thought that I couldn't get rid of.  What else can I take from the real world to improve my lighting?  The most straightforward answer was light intensities.  In Unreal, lights are expressed...

**Frame:** tutorials\frames\realistic-and-physical-lighting-in-ue5-what-is-pbl\frame_001.jpg

### What is PBL ? [2:53]
**Transcript:** PBL stands for physically-based lighting.  It's a workflow that consists of using real-world light values and exposure settings in CG lighting.  I found out that many studios have adopted this approach, or at least use physically  lighting values to some extent in their work.  However, beyond professional environments, this topic isn't widely known and the resources  are limited.  So where do we start?  What's the first thing you need to understand to work in PBL?  Well, the most fundamental yet surprisingly complex first step is learning the units you  work with.  By understanding the units, the values would make sense.  The problem is, there are a lot of lighting units.  It can take a while to understand how it all fits together, but the good news is, you  don't need to learn all of them.  For digital lighting, we can narrow it down to just four.  Candela, Lumen, Luxe and Candela per meter square.  Let's start with the first two.  If those definitions are just making things more confusing, you're in the same boat I was.  Something that really helped me was to put each unit into context.  Candela is the best lighting unit in the international system of units.  This means it is use...

**Frame:** tutorials\frames\realistic-and-physical-lighting-in-ue5-what-is-pbl\frame_002.jpg

### Building a Database [7:00]
**Transcript:** After weeks of research and matter, I realized there wasn't any database available to the  public.  This was a problem.  As without any data, there's no point of using this workflow.  I started gathering everything I could find online in two spreadsheets, but it was far  from consistent.  I had no way to verify the values and I was missing a lot of scenarios.  The only option left was to sample the data myself.  So I did.  For a year, I carried a light meter with me everywhere I went.  A light meter is a device that captures different kinds of lighting data.  The most common ones are incident light meter and reflective light meter.  Incident light meter, also called Lux meter, reads the intensity of the light falling onto  a white emisfer sensor.  This is how you capture the illuminance of a scene.  It is used by photographers and filmmakers to figure out the right amount of light needed  for their subjects.  To do so, they place the device just in front of them and read the values.  A reflective light meter, also called Spot meter, measures the light reflected off the  surface.  To use it, you need to aim the device at the source.  Almost every modern camera now comes with a built...

**Frame:** tutorials\frames\realistic-and-physical-lighting-in-ue5-what-is-pbl\frame_003.jpg

### Developing a Tool [10:41]
**Transcript:** I was exploring how to make the database directly accessible in Unreal Engine.  After six months of development, my plugin, PBL database, was launched on FAP.  The plugin serves two main purposes, to simplify learning PBL and to spot your lighting work  flow on a daily basis.  To do that, I needed a system that was both user friendly and scalable, something that  could organize the data clearly.  So I created a way to filter the data using tags.  You just speak a few categories that match what you're looking for, then select a specific  lighting scenario.  This system is based on how lighting is used in Unreal and how it's measured in real  life.  The best way to organize the data was to split it into two categories, artificial and natural  light sources.  From there, the data is sorted by units, location and scenario.  All of this will be further explained in my next video, in which I will tackle practical  cases.  Along with the main features, I decided to add a third type to the interface.  This one will be focused on camera-specific tools.  That brings me to a topic we haven't covered yet, exposure, and how it plays a major role  in lighting.  Unreal Engine works just like a re...

**Frame:** tutorials\frames\realistic-and-physical-lighting-in-ue5-what-is-pbl\frame_004.jpg

### Outro [13:50]
**Transcript:** I hope sharing my journey helped you see the big picture and gave you the tools to overcome  some of the challenges you might face.  In the next video, we'll see how to implement what we've learned so far in Unreal, how  the theory translates into practice.  I'll show you how I use the plugin in my own work and we'll dive into different lighting  scenarios together.  If you have any feedback about this video, but also all the content I've put out there,  please don't hesitate to reach out or leave a comment.  The real world isn't perfect.  It's rough, raw, full of flaws and it's what we seek when making 3D.  Whether it's materials, textures, animation or other steps of the production, we always  try to emulate the imperfections of our world.  So why don't we do the same with lighting?  Some might say that as Unreal relies on camera exposure, it doesn't change anything to have  to physically accurate lighting intensities.  If I double the exposure and reduce by half the lighting, the image will in the end look  the same.  The biggest issue though with using arbitrary values is the lack of consistency and coherence  between your different lights.  As we saw it, the scale of intensity...

**Frame:** tutorials\frames\realistic-and-physical-lighting-in-ue5-what-is-pbl\frame_005.jpg


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
