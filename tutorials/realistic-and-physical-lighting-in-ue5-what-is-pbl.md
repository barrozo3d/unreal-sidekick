---
title: Realistic and Physical Lighting in UE5: What is PBL ?
source: YouTube
url: https://www.youtube.com/watch?v=JoxgvwNFc8g
author: arthur tasquin
ingested: 2026-06-23
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
**Transcript:** A common exercise for any aspiring lighting artist is lighting studies.  You've probably seen a ton of them on our station.  The idea is simple.  You take a single environment and you create multiple lighting variations of it.  By working exclusively on those variations that we also call lighting scenarios, you can  focus on what matters.  In 2024, I started to work on one of those projects.  I was inspired by photographs taking during my daily morning commute.  Eventually, it became quite a technical challenge as the project grew over seven distinct scenarios.  So I had to find a workflow to easily switch between lighting setups.  Using a mix of sub-levels and dedicated level sequences, I was able to contain everything  in one place.  Now, with my background in the film industry, I wanted to use reflectors in Unreal.  On movie sets, reflectors are pieces of fabric designed to reflect or absorb lights.  This technique, even in CG, gives you way more control over the lighting.  This kicked off a thought that I couldn't get rid of.  What else can I take from the real world to improve my lighting?  The most straightforward answer was light intensities.  In Unreal, lights are expressed in lux, lumen or candela.  The default values are 10 lux for directional light and 8 candela for local lights.  But why?  Why are these values expressed in different units?  What do those units actually mean?  Why those numbers in particular?  And how do I know what value to input?  These questions led me to the topic of this video.

**Frame:** tutorials\frames\realistic-and-physical-lighting-in-ue5-what-is-pbl\frame_001.jpg

### What is PBL ? [2:53]
**Transcript:** PBL stands for physically-based lighting.  It's a workflow that consists of using real-world light values and exposure settings in CG lighting.  I found out that many studios have adopted this approach, or at least use physically  lighting values to some extent in their work.  However, beyond professional environments, this topic isn't widely known and the resources  are limited.  So where do we start?  What's the first thing you need to understand to work in PBL?  Well, the most fundamental yet surprisingly complex first step is learning the units you  work with.  By understanding the units, the values would make sense.  The problem is, there are a lot of lighting units.  It can take a while to understand how it all fits together, but the good news is, you  don't need to learn all of them.  For digital lighting, we can narrow it down to just four.  Candela, Lumen, Luxe and Candela per meter square.  Let's start with the first two.  If those definitions are just making things more confusing, you're in the same boat I was.  Something that really helped me was to put each unit into context.  Candela is the best lighting unit in the international system of units.  This means it is used by every other lighting unit.  That said, you won't often see it used directly in everyday life.  What makes Candela different from Lumen is that it takes into account the angle of diffusion.  One practical example of this is a flashlight.  This value in Candela will be related on how focused the beam is.  The wider the beam, the lower the value.  Lumen on the other hand is more familiar.  It's the number you'll find on every light bulb and fixtures.  It's the quantity of light emitted by a source, regardless of the angle of diffusion.  You can see it as the brightness of the light source.  In Unreal Engine, Lumen's and Candelas are used by local lights.  While you can specify the unit per light, I would strongly advise you to set the default  light unit to Lumen's in the project settings.  You'll find it under Engine, Rendering, default settings.  Since most lighting references only use Lumen's, working in the same unit will help you  stay consistent and avoid mistakes.  Now the next two units bring surface into the equation.  Eliminance is expressed in Candela per meter square, which indicates that it takes in consideration  both the angle of diffusion and the surface area it's coming from.  You can think of it as the amount of light a surface emits in the given direction.  In daily life, this is what you'll see listed on screens, sometimes referred to as Nits.  In Unreal, it's the unit used for emissive surfaces, from small elements like theroyson  tubes to something as big as the skydome.  Once measured in Lux is about how much light hits a surface.  It is commonly used in architecture, film of the graph, to evaluate how much light is  falling on a subject.  In Unreal, the directional light which usually is the sun is the only lighting actor that  is expressed in Lux.  So out of all these units, we will only use three.  My advice would be to put your energy into understanding what sets each one apart and  how they're used both in the real world and in Unreal.  Understanding the units was just a start.  Once I knew what they meant, I still needed to find the actual values to set my lights  to.  I had way more questions than before.  How many Lux does the sun produce on a bright day?  How do clouds change that?  And most importantly, where can I find that kind of information?

**Frame:** tutorials\frames\realistic-and-physical-lighting-in-ue5-what-is-pbl\frame_002.jpg

### Building a Database [7:00]
**Transcript:** After weeks of research and matter, I realized there wasn't any database available to the  public.  This was a problem.  As without any data, there's no point of using this workflow.  I started gathering everything I could find online in two spreadsheets, but it was far  from consistent.  I had no way to verify the values and I was missing a lot of scenarios.  The only option left was to sample the data myself.  So I did.  For a year, I carried a light meter with me everywhere I went.  A light meter is a device that captures different kinds of lighting data.  The most common ones are incident light meter and reflective light meter.  Incident light meter, also called Lux meter, reads the intensity of the light falling onto  a white emisfer sensor.  This is how you capture the illuminance of a scene.  It is used by photographers and filmmakers to figure out the right amount of light needed  for their subjects.  To do so, they place the device just in front of them and read the values.  A reflective light meter, also called Spot meter, measures the light reflected off the  surface.  To use it, you need to aim the device at the source.  Almost every modern camera now comes with a built-in Spot meter, which helps evaluate  the proper exposure of your scene.  Looking on the use case, light meter can come with specific features like camera settings.  In my case, I was using the MT912 light meter, a simple incident light meter that only captures  illuminance.  Now, Unreal also comes with its own built-in light meter system.  The HDR view mode is essential when working in PBL.  By using the two white calibration squares, you can read both the illuminance and luminance  of your scene and use that to validate your lighting.  To build a decent database, I had to cover many lighting scenarios in three different units.  Lux, Lumance and Candala per meter square.  My lux meter was handling the illuminance.  I just had to get out there and sample as many times as I could.  For lumens, I could just scout retailers' websites.  But luminance was trickier.  Professional Spot meters can get very expensive.  So I decided to left that part out and rely on online data.  Sampling all that data made me realize a couple of things.  First, the range of lighting intensity is massive.  A clear sky at noon can hit over 100,000 lux, while an indoor living room with artificial  lighting might sit around 300 lux.  Second, the numbers vary a lot.  Other, pollution, time of day, season, location, surroundings, even the shape of clouds, the  all influenced the results.  With that in mind, having a single value for one scenario doesn't make any sense.  Each of those should have a range from which you can iterate to see what you see.  Because in PBL, what really matters is the scale of things.  While I was working on these database, I kept thinking, how can I help others who are  also trying to figure this out?  After releasing my lighting studies, I got in touch with the team at 80 level to write  a full breakdown of the project and share everything I'd learned so far.  The next step was to share the database itself, but I needed to find a way to make it more  user friendly.  At the end of the article, I shared the proof of concept for tool I was working on.

**Frame:** tutorials\frames\realistic-and-physical-lighting-in-ue5-what-is-pbl\frame_003.jpg

### Developing a Tool [10:41]
**Transcript:** I was exploring how to make the database directly accessible in Unreal Engine.  After six months of development, my plugin, PBL database, was launched on FAP.  The plugin serves two main purposes, to simplify learning PBL and to spot your lighting work  flow on a daily basis.  To do that, I needed a system that was both user friendly and scalable, something that  could organize the data clearly.  So I created a way to filter the data using tags.  You just speak a few categories that match what you're looking for, then select a specific  lighting scenario.  This system is based on how lighting is used in Unreal and how it's measured in real  life.  The best way to organize the data was to split it into two categories, artificial and natural  light sources.  From there, the data is sorted by units, location and scenario.  All of this will be further explained in my next video, in which I will tackle practical  cases.  Along with the main features, I decided to add a third type to the interface.  This one will be focused on camera-specific tools.  That brings me to a topic we haven't covered yet, exposure, and how it plays a major role  in lighting.  Unreal Engine works just like a real camera.  If you're in a dark scene, you have two options.  You can increase the intensity of the lights or you can adjust the exposure of the camera.  Exposure refers to the amount of light heating the camera sensor.  It dictates how bright or dark your image appears.  This implies something really important for us.  Using PBL values for your lighting isn't enough on its own.  Your camera settings also need to match the intended lighting scenario.  In Unreal, you can control the exposure manually, just like real camera, through the aperture,  shutter speed and ISO.  However, there's also a system called Exposure Value or EV100, which in my opinion is easier  to use.  Over time, photographers have established guidelines that cover many different scenarios  and you can use those to estimate the proper exposure of your scene.  When we talk about proper exposure, we're just referring to well-balanced settings that  keep as much visual information as possible and avoid over or under-exposure the image.  I won't go further into detail here as this topic could have its own dedicated video.  But if this is new to you, I would highly recommend to learn the basics.  I will leave very interesting resources in the description.  In the final stage of the development, I started to share lighting studies made with the  plugin.  I also reach out to Atelevologin for a second article that would cover how to use it.  The only thing missing was a video, something clear and easier to follow.

**Frame:** tutorials\frames\realistic-and-physical-lighting-in-ue5-what-is-pbl\frame_004.jpg

### Outro [13:50]
**Transcript:** I hope sharing my journey helped you see the big picture and gave you the tools to overcome  some of the challenges you might face.  In the next video, we'll see how to implement what we've learned so far in Unreal, how  the theory translates into practice.  I'll show you how I use the plugin in my own work and we'll dive into different lighting  scenarios together.  If you have any feedback about this video, but also all the content I've put out there,  please don't hesitate to reach out or leave a comment.  The real world isn't perfect.  It's rough, raw, full of flaws and it's what we seek when making 3D.  Whether it's materials, textures, animation or other steps of the production, we always  try to emulate the imperfections of our world.  So why don't we do the same with lighting?  Some might say that as Unreal relies on camera exposure, it doesn't change anything to have  to physically accurate lighting intensities.  If I double the exposure and reduce by half the lighting, the image will in the end look  the same.  The biggest issue though with using arbitrary values is the lack of consistency and coherence  between your different lights.  As we saw it, the scale of intensity is huge and if you don't pay attention, the ratio  between your different lights will not be realistic.  Using PBL workflow is the best way to emulate the camera's dynamic range and confront yourself  to the rules of the real world.  Furthermore, sharing the same set of rules improves collaboration between lighting artists  and ensures consistency throughout projects.  I'm strong believer that learning how things operate under the hood will only improve  your work and ground it into reality.

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
