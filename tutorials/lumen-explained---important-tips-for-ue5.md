---
title: Lumen Explained - IMPORTANT Tips for UE5
source: YouTube
url: https://www.youtube.com/watch?v=1e6oOiKh91U
author: William Faucher
ingested: 2026-06-23
ue_version: "UE5"
tags: [lumen, global-illumination, reflections, surface-cache, nanite, performance, ray-tracing, materials, best-practices, rendering]
extraction_status: complete
frames_dir: tutorials/frames/lumen-explained---important-tips-for-ue5/
frame_count: 10
---

# Lumen Explained - IMPORTANT Tips for UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=1e6oOiKh91U)
**Author:** William Faucher
**Duration:** 16m2s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back. It's great to see you again. William Fosha here.  Today's video is about Lumin. Now this video may come across as a little wordy,  long, dry, and while Lumin is fairly user friendly and works very well out of the box,  there are several changes to the way you need to make your models and materials  moving forward. So I promise you, your work will improve. If you just bear with me to the end here,  this is quite possibly one of the most important videos I've made in a while.  I know I've made a video about Lumin back in May, but that video was made three days after  UE5 dropped and I've addressed a few issues there, but Epic has since released additional information,  making that earlier video a bit outdated somewhat. So in this video, I've gathered all,  was the latest and greatest information available, most of which gathered from Epic's amazing  livestream on the topic that said their livestream is over two and a half hours long and while  they are goldmine of information, a lot of it goes way deeper than necessary for the average artist.  So that's where this explain series of videos come in. I want to condense the info from  those livestreams into a much more digestible format. But before we get started, this video does have  a sponsor, so let's get that integration done first as to not break the flow of the video later.

**Frame:** tutorials\frames\lumen-explained---important-tips-for-ue5\frame_000.jpg

### Skillshare [1:15]
**Transcript:** So this video is sponsored by Skillshare, and as you all know by now, Skillshare is an online learning  platform which thousands of classes are creative artists or just curious people to explore new skills  and dive deeper into existing hobbies or passions. It's your curious about virtual production,  shooting video, filmmaking, Skillshare offered a large variety of classes on cinematography,  like this short and sweet 30 minute class by Zach Mulligan called cinematography basics,  understanding filmmaking, which covers the key basics and fundamentals of film,  the mood, the tone, and the feel. Skillshare's classes are curated, they have really high production  quality, they're ad-free, and there is a constant stream of new classes for you to choose from,  and since many of you watching this channel are from all corners of the globe, it's worth  mentioning that Skillshare's entire catalog of classes now offers subtitles in Spanish,  French, Portuguese, and Dutch. Now because Skillshare is sponsoring this video, the first  1000 you to click the link down below will get a one month free trial of Skillshare,  so you can start learning today. So once again, thanks so much for Skillshare for sponsoring this

**Frame:** tutorials\frames\lumen-explained---important-tips-for-ue5\frame_001.jpg

### Project Settings [2:24]
**Transcript:** video, and with that out of the way, let's dive right in starting with the necessary project  settings for Lumen. Now by default, Lumen is active and you don't need to change anything, but in  the event that you've migrated a UE4 project over to UE5, here is what you need to set it to.  Dynamic global illumination method set the Lumen reflection method set to Lumen,  generate meshed in fields, needs to be on, in editor, Lumen is controlled by the following values,  the light properties, the material base color and roughness, and the exposure. Lastly,  you do have some quality control settings in the post process volume,  final gather quality, and Lumen reflection quality, which we're going to dive a little bit deeper  into real soon. Next, let's talk about what Lumen can do, the obvious and the not so obvious.

**Frame:** tutorials\frames\lumen-explained---important-tips-for-ue5\frame_002.jpg

### What Lumen Can Do [3:07]
**Transcript:** The obvious being it achieved real-time indirect lighting with rather surprising accuracy,  and as we all know, immersive lighting does contribute to GI. Just to be clear, when I say GI,  moving forward, I mean global illumination. So if you have a large, bright material, it will  light up your scene. There are several limitations to this, which again, we will get into a little  bit later. Lumen also provides reflections and integrates GI into the reflections as well. So  what I mean by this is you will see all of the GI in the reflections. This is something that  rate rate reflections didn't really do very well in UE4. Lumen also supports clear coat materials  properly so that there are two reflections, not just one, which is really useful for car materials.  Again, this is something that rate rate reflections really can't do at the moment. It also supports  fully shadowed skylight. So drag and dropping a skylight set to movable will shadow everything  automatically with no additional input from the artist. It provides dynamic GI and sky shadowing  on translucency and volumetric fog albeit at a lower quality. Lumen makes things so much easier for  artist. There's a way less fiddling around with hidden settings for lighting and shadow detail.  Most of the heavy lifting is done under the hood, which is absolutely awesome for us.

**Frame:** tutorials\frames\lumen-explained---important-tips-for-ue5\frame_003.jpg

### How Lumen Works [4:33]
**Transcript:** So how does this all work? In pure nerd talk, it is a hybrid ray tracing pipeline, which uses software  ray tracing. It traces against the depth buffer first, which we call screen traces, then it  traces against the distance field and applies lighting to ray hits with the surface cache.  Lumen relies heavily on mesh distance fields, but what's worth noting here is that the mesh  distance fields have been completely rewritten in UE5 for youth with lumen specifically, and they are  way way better than they ever were in UE4. The mesh distance fields now have mid maps,  they're streamed from disk based on distance, and they cost about half as much in terms of memory  compared to UE4. They also build 10 times faster than before, which is a massive upgrade.  If you remember back in UE4, building mesh distance field took a very long time. That is no  longer the case here. Now while all this takes care of shadows, it can determine material color  and lighting of a surface, so that's where the surface cache comes in. The surface cache

**Frame:** tutorials\frames\lumen-explained---important-tips-for-ue5\frame_004.jpg

### Surface Cache (SUPER IMPORTANT) [5:35]
**Transcript:** essentially splits up your meshes with a bunch of cards. It captures material properties of the mesh,  color, roughness, act very low resolution into an atlas, which does work especially well with  nanite meshes. It also constantly updates its atlas as you fly around your scene. It's worth noting,  however, that these recaptures are very slow on non-nanite meshes. So if you notice your  frame rate just tank for no apparent reason, try and see if your environment has some non-nanite  models lying around. They could be the culprit, especially if those meshes don't have proper  LEDs set up. You can visualize the surface cache with the following console command right here.  TLDR, if you're going to use lumen with any high poly assets, they pretty much need to be  nanite if you want good frame rates. Now that was a whole lot of boring talk. Why should artists  care about this crap? The surface cache has one major, major limitation and this is what's going  to affect how you create your assets and your models. Only simple meshes and interiors can be  supported. And what I mean by this is you can't simply just use one large combined mesh for an  interior, for example, walls, floors, ceilings. All of these need to be separate individual models.  If you're trying to light a scene and thing just look odd or lighting is only screen space,  this could be one of the reasons why. And while having separate walls and floors and ceilings  sounds like a pain in the butt, thanks to nanite you can simply bring all of these separate models  into a single blueprint asset. And from there it's going to be good to go. It's a great little trick  to combine the convenience of having both a single assembled asset and the quality benefits of  Lumen. The reason I bring this up segues into my next topic, the Lumen scene, which is arguably

**Frame:** tutorials\frames\lumen-explained---important-tips-for-ue5\frame_005.jpg

### Lumen Scene (ALSO IMPORTANT) [7:21]
**Transcript:** the most important view mode for Lumen, because if you're a Lumen scene doesn't roughly match  what's on your main screen, there's going to be view dependent artifacts in the GI. If you've  ever noticed that Lumen GI is sometimes screen space, that is why. Something is wrong. The Lumen  scene is your number one tool for seeing what is Lumen doing. Why is there an artifact? You can  A.B. compare this between view ports and make sure they look roughly the same lighting wives,  color rise, etc. It's really convenient to use the G-Short Cut, especially if you're seeing  meshes or objects that are black like this in the Lumen scene. Something is wrong and that object  is not contributing to GI. Black models in the scene means that they are only going to show up in  screen traces, which is why the lighting will appear and disappear in a screen space fashion.  But now, let's talk about some of Lumen's limitation and the very important things to know.

**Frame:** tutorials\frames\lumen-explained---important-tips-for-ue5\frame_006.jpg

### Limitations & Things to Know [8:16]
**Transcript:** For now, only static mesh and instant static meshes are supported, meaning there is no landscape  support for this at the moment, but it is coming in 5.0. World position offset causes artifacts,  so anything win-related can be problematic. Translucent materials are also not yet supported for  Lumen reflections or dynamic GI, so glass is not going to look right. The interesting thing is that  subsurface scattering does not work with Lumen, but subsurface profile does. It's what I used to  give the snow on the ground here a subtle subsurface scattering look. Lumen also happens to rely heavily  on temporal super resolution, which is similar to Nvidia's DLSS. This means that it calculates in 1080p  and it upscaled everything to 4k resolution, all while looking nearly as good as a native 4k.  Temporal super resolution, TSR, is really the key to making Lumen possible in real time. Lumen  does allow hardware ray tracing, which offers the highest quality, but also the highest cost as well.  And it only has partial support in early access, such as raytrade reflections, shadows,  and it is part of the final gather. Hardware ray tracing traces against the Nanite proxy geometry  only, so you may need to raise the proxy triangle if you're running into artifacts or bad shadows,  in a Nanite setting of a given static mesh. If you're using hardware ray tracing, try to avoid  kit bashing too much or have too many overlapping meshes. The performance impact is going to be  massive. So if you do have a lot of kit bashing, maybe stick with software raytracing instead.  Next, when you use the movie render to you, you may notice that the first few frames look  frankly horrible and noisy, and this is because Lumen is intended for real time usage, and it needs  several frames to converge. So you need to use a high amount of warm up frames, which can add here  in the movie render queue under the Anti-Aliasing tab. I often use around 250 to 500 warm up frames,  just to err on the side of caution, it's probably overkill, but works. By default, the Lumen scene is  only active to about 200 meters. Past 200 meters, Lumen goes screen space. So for all intents and  purposes, you can't really tell because things are so far away at that point, but it is worth  noting if you're using a very long focal length on your camera. That said, Lumen can be optimized a  little bit, and the default is to trace meshes and fields for the first two meters, which is  detail tracing, but you can choose to skip the meshes and field tracing entirely with what we call  global tracing. This can give you a handy FPS boost in scene with a lot of overlapping GIA.  Now, I've saved one of the major dropbacks of Lumen for last, and that's the fact the lighting  channels are not supported, and they won't be supported at all, primarily because of how  Lumen is designed and how it works. This really sucks, but it is what it is. It is a very small price  to pay for the incredible lighting that we get. Now this part here is going to be a favorite

**Frame:** tutorials\frames\lumen-explained---important-tips-for-ue5\frame_007.jpg

### Raytraced Reflections [11:18]
**Transcript:** for Archvizardus. You may have noticed that in many cases, reflections are just kind of,  the kind of blare, especially if you're used to the gorgeous, sharp and crisp,  raytrade reflections of Ub4. I'm going to tell you all about the magic sauce to get the raytrade  reflections and Lumen combined together in just a second. By default, Reflection uses Surface  Cache, which is great for performance, but as you know, it doesn't look so hot. Most people  seem to think that you can either use only hardware ray tracing or Lumen not vote. Unfortunately,  you can get the best of both worlds. So first, open up your project setting and in the rendering  section, you need to make sure you hardware ray tracing when available and support hardware raytracing  are turned on. Next, search for default RHI and make sure this is set to DirectX 12. Then restart  on real. Lastly, you need to set the Lumen Reflection quality setting in the post-process volume to four.  That is the magic number and that solves our issue. Now, you can get both Lumen lighting and  raytrade reflection to work together in harmony. Now, for the last part of this video,

**Frame:** tutorials\frames\lumen-explained---important-tips-for-ue5\frame_008.jpg

### Best Practices [12:29]
**Transcript:** I want to talk about the best practices using Lumen. So this is a very important part of the video.  First off, you cannot use Lumen and the Mrs. Meshes to replace light sources. They're going to have  a bad time if you do. Results are going to be noisy and inconsistent and possibly even screen space  in many cases. Lumen does pick up a Mrs. materials as we've seen before. But the smaller and brighter  that a Mrs. source is, the noisy or the result will be. So if you're using a Mrs. materials with  Lumen, keep those sources large and dim for best quality and then go ahead and add an actual light  to give your scene the brightness you want. You the rec light or a point light, spot light,  whatever, just don't rely on only using a Mrs. materials. It's going to look bad. Very small  and bright material sources like particles or small lights on the wall of a sci-fi scene  are going to be notably problematic. Next, the base color has a huge impact on GI.  Now for note of us coming from an offline rendering or a VFX background, this is obvious. Dark and  busy base colors are going to have a poor impact on GI while bright Abyto values will bounce  the light around more. Again, obviously, of course it does. But it is important to never use an  Albedo of one or pure white. A perfectly bright Albedo means it reflects 100% of the light's  energy. And that simply never happens in real life. All surfaces absorb a small portion of light.  Even the purest snow on the top of the Himalayas will have an Albedo 0.8 or 0.9 or so. So even though  it's very very bright, it still absorbs 10 or 20% of the light. It's important to keep this in  mind when setting up your base colors. It's also important to not use a material that's too dark as  well. And that's just going to suck away all of that lovely indirect lighting in your scene.  So taking a look at this example right here, you're going to see just how impactful a brighter Albedo  can be. Again, you want to turn on the Lumin scene to visualize what's going on in your scene.  If you have object that are black or things don't look similar to your main scene here,  you're going to get Screen Space GI. This is a problem a lot of people have run into,  and they just write it off at, oh, Lumin's is a Screen Space effect. No, no it's not. Lumin is not  just Screen Space, but if you're seeing a setup wrong, it will be. Just to give you a classic  example in my previous environment I made here, I have some snowman from Megascans, and they were  showing up as black in the Lumin scene. The reason for this wasn't the model. The reason would  be because of the master material it was using. It was, by default, using the Megascans transmission  master material as opposed to the default vanilla Megascans material. And the transmission one here  is the one that broke Lumin on these assets. That transmission material was automatically created  by Quixel Bridge, so pay attention to the materials if not just a mesh that could trigger a black  mesh in the Lumin scene here, like combined walls and ceilings and floors. Unsupported materials  can break Lumin 2. So keep an eye on the Lumin scene view mode and be sure it stays in sync  with your main scene. Yes, these content requirements really suck, but it is so much better than  authoring Lightmap UVs and baked lighting. Gotta hate baked lighting, that would painful.  And that's it for today folks, thank you so much for watching. If you did find this video helpful,  do consider subscribing and hitting the like button down below. And as always, happy rendering.

**Frame:** tutorials\frames\lumen-explained---important-tips-for-ue5\frame_009.jpg


---

## Structured Notes

### Core Technique
Lumen is a hybrid software ray tracing pipeline: screen traces (depth buffer) → distance field traces → surface cache lighting. Surface Cache splits meshes into cards and captures material properties at low resolution into an atlas. Critical rule: individual walls/floors/ceilings must be separate meshes (not one combined mesh) for surface cache to work correctly; pack into a Blueprint for convenience. Ray-traced reflections + Lumen GI both: set PPV Lumen Reflection Quality = 4. Lumen scene view mode is the primary debug tool — black objects = only screen space GI.

### Summary
16-minute William Faucher deep-dive on Lumen in UE5: project settings, capabilities, how it works (hybrid RT pipeline, surface cache, mesh distance fields), Surface Cache limitations (separate meshes required), Lumen Scene view mode debugging, full limitations list, how to combine ray-traced reflections with Lumen (PPV Reflection Quality = 4), and best practices (emissive sources, albedo values, material compatibility). Key context: Epic's Lumen livestream condensed. Originally written close to UE5 launch but updated with latest Epic guidance.

### Key Steps
1. **Project Settings** (critical for UE4→UE5 migrations):
   - Dynamic Global Illumination: Lumen
   - Reflection Method: Lumen
   - Generate Mesh Distance Fields: ON
   - PPV: Final Gather Quality, Lumen Reflection Quality (quality control levers)
2. **What Lumen provides**:
   - Real-time indirect lighting (emissive materials contribute to GI)
   - GI-integrated reflections (ray-traced reflections in UE4 didn't capture GI)
   - Clear coat support (two reflections)
   - Fully shadowed Skylight (movable → auto-shadows everything)
   - Dynamic GI + sky shadowing on translucency and volumetric fog (lower quality)
3. **How it works internally**:
   - Screen traces (depth buffer) → distance field traces → surface cache applies lighting at ray hits
   - Mesh distance fields in UE5: MIP maps, streamed from disk, 50% less memory vs UE4, 10× faster to build
4. **Surface Cache — CRITICAL for artists**:
   - Splits meshes into "cards"; captures color, roughness at very low res into atlas
   - Non-Nanite meshes: slow recaptures → frame rate drops
   - **Walls/floors/ceilings MUST be separate individual meshes** — one combined interior mesh breaks surface cache
   - Fix: put separate mesh components into a single Blueprint Actor for assembly convenience
   - Visualize: console command for Surface Cache visualization
5. **Lumen Scene view mode** (most important debugging tool):
   - Toggle via Lit dropdown → Lumen Scene
   - Must roughly match main scene; if different → view-dependent GI artifacts
   - **Black objects = only screen space GI** (not contributing to bounces) → check material
   - Common causes: Megascans Transmission master material breaks Lumen; combined meshes; unsupported material domains
   - Use G shortcut to hide UI while A/B comparing viewports
6. **Limitations**:
   - Static Meshes + Instanced Static Meshes only (no Landscape at UE5 launch, later added)
   - World Position Offset (wind, cloth) causes artifacts
   - Translucent materials: not supported for Lumen reflections or dynamic GI (glass looks wrong)
   - Subsurface Scattering: not supported; **Subsurface Profile**: supported
   - Relies on Temporal Super Resolution (TSR): renders at 1080p, upscales to 4K
   - Hardware ray tracing: traces against Nanite proxy geometry only → may need to raise proxy triangle count; avoid heavy kitbashing/overlapping meshes (massive perf cost)
   - **Lighting Channels**: NOT supported (design constraint, will not be added)
   - MRQ: Lumen needs many frames to converge → set 250–500 warm-up frames (MRQ → Anti-Aliasing tab)
   - Active range: ~200 meters; beyond = screen space only (relevant for telephoto/long focal length shots)
   - Detail tracing default: first 2 meters; switch to Global Tracing for FPS boost in dense GI scenes
7. **Ray-traced reflections + Lumen GI together**:
   - Project Settings → Support Hardware Ray Tracing: ON + Hardware Ray Tracing When Available: ON
   - Default RHI: DirectX 12; restart engine
   - PPV → Lumen Reflection Quality: **4** (magic number — enables both RT reflections + Lumen GI)
8. **Best practices**:
   - Emissive as accent only: noisy + disappears at distance; keep emissive sources large + dim; add actual light for brightness
   - Never albedo/base color = 1 (pure white → reflects 100% light = physically impossible); keep 0.04–0.85
   - Dark albedo kills indirect — bright materials = more free bounce light
   - Check Lumen Scene after importing any asset; Megascans Transmission material is a known Lumen breaker
   - High-poly assets essentially require Nanite for good Lumen performance

### UE Systems / Blueprints / Settings
- **Lumen** — UE5 default dynamic GI system; hybrid software RT; Project Settings → Dynamic Global Illumination = Lumen; Reflection Method = Lumen
- **Surface Cache** — low-res card-based material property atlas; requires separate mesh components for interiors; recaptures slowly on non-Nanite; fundamental reason Nanite + Lumen pair well
- **Mesh Distance Fields** — UE5 rewrite: MIP maps, disk streaming, 50% less memory, 10× faster build vs UE4; `Generate Mesh Distance Fields` Project Setting
- **Lumen Scene view mode** — Lit dropdown → Lumen Scene; primary debug view; black objects = screen-space only GI; must match main scene
- **Hardware Ray Tracing (Lumen)** — Project Settings → Support Hardware Ray Tracing + Hardware Ray Tracing When Available; DirectX 12 only; traces Nanite proxy geometry; massive perf cost with overlapping meshes
- **Lumen Reflection Quality (PPV)** — values 1–4; set to 4 to activate ray-traced reflections while keeping Lumen GI (both work together at 4)
- **Final Gather Quality (PPV)** — controls Lumen GI sample quality; higher = less noise/flickering
- **Temporal Super Resolution (TSR)** — UE5 upscaling tech; Lumen depends on it; renders 1080p → upscales to 4K
- **Warm-up Frames (MRQ)** — MRQ → Anti-Aliasing tab; 250–500 for Lumen to converge before first frame is captured
- **Subsurface Profile** — works with Lumen; Subsurface Scattering shading model does NOT work with Lumen
- **Lighting Channels** — NOT supported with Lumen (by design)
- **Global Tracing** — skip per-mesh distance field tracing; FPS boost in dense scenes with heavy GI; sacrifice some detail tracing quality
- **Detail Tracing** — default; traces mesh distance fields in first 2 meters; highest quality short-range GI

### Difficulty
Intermediate-Advanced. Technical deep-dive requiring knowledge of UE's rendering pipeline. Most important practical takeaways (separate meshes, Lumen Scene debugging, albedo values) apply at all skill levels. Hardware RT + Lumen reflection quality = 4 is the key practical trick for archviz/film artists.

### UE Version
UE5 (recorded at UE5.0 launch timeframe; surface cache, TSR, and Lumen are UE5-only; some limitations noted as temporary were addressed in later UE5 point releases)

### Tags
lumen, global-illumination, reflections, surface-cache, nanite, performance, ray-tracing, materials, best-practices, rendering

---

## Related Entries
- `lighting-in-unreal-engine-5-for-beginners.md` — Lumen used in practice; beginner lighting workflow
- `lighting-interiors-in-unreal-engine-5.md` — interior Lumen setup; path tracer comparison
- `lighting-a-night-time-exterior-in-unreal.md` — nighttime Lumen + volumetric fog workflow
