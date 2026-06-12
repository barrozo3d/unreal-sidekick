---
title: Fixing Common UE5 Issues! Changes in 5.0
source: YouTube
url: https://www.youtube.com/watch?v=wTYM9TfckOQ
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 5.0"
tags: [lumen, reflections, hardware-ray-tracing, translucency, glass, nanite, project-settings, william-faucher, beginner, ue5]
extraction_status: complete
frames_dir: tutorials/frames/fixing-common-ue5-issues-changes-in-50/
frame_count: 0
---

# Fixing Common UE5 Issues! Changes in 5.0

**Source:** [YouTube](https://www.youtube.com/watch?v=wTYM9TfckOQ)
**Author:** William Faucher
**Duration:** 15m51s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** So with the 5.0 release of Unreal, I've noticed across many message boards and forums that a lot of people are actually  Pretty confused about some of the changes we've had so far  Notably with the Lumen reflections, refractions, and even things like how do we even turn on the path tracer?  So this is going to be a very quick and dirty video just to help clarify a few issues that some of you may have run into and  I'll be pointing you towards some other videos on my channel that will go more in-depth about those topics.  Now for starters, Lumen does not require RTX or hardware ray tracing to work.  UE5 will work with older GPUs like the 1070 to 1080. Lumen is not dependent on that.  But those of you coming from UE4 will undoubtedly have noticed that  the Lumen reflections and refraction are not nearly as good as they were with  raytrade reflections in UE4, but don't worry. This is not a step back.  There's just a few settings that we need to change to get both the benefits of the GI and Lumen and  Gorgeous raytrade reflections. And the easiest way to do that is when you're creating a brand new project  Just turn on the little raytracing checkbox right here. That's going to enable a...


### Important Project Settings [1:18]
**Transcript:** Let's take a dive into the necessary project settings to get that to work.  We need to go to the settings tab here  go to project settings and  We're going to go down to the rendering tab down here on the left hand side and  scroll down and the following settings are the one that you really need to have  Dynamic global lumination set to Lumen reflection method. We can leave that aluminum for now  We can override this in the post-process volume later  But what we really want is support hardware ray tracing turned on and  Here in the Lumen tab use hardware raytracing when available make sure that the checkbox is turned on as well  You may get a message that says something along the lines of  Enabling the skin cache when turning on the hardware ray tracing. Just click yes  You need to have that enabled. We're also going to turn on the path tracing checkbox right here  I believe it's actually off by default. So if you want to use the path tracer  You can turn it on right here  I have a more detailed tutorial on the path tracer right here. So check that out if that interests you and  One last thing that should be on by default, but isn't always it we're gonna search for direct X and  Be...


### Pathtracer Tips [2:43]
**Transcript:** It's gonna have to recompile the shaders, but once that's done you're good to go and now if we go to the lit tab here  You should have the path tracer show up and it'll work as intended  Just a bit of a quick segue here the path tracer doesn't work with Nanite if you turn the path tracer on with a whole bunch of  Nanite meshes  It's only going to pass trace the Nanite proxy mesh and not the actual high-read Nanite mesh  So that is another thing you really need to keep in mind because Nanite is not exactly what we call real geo  It's virtual as geo and the path tracer doesn't really know how to read that it's the same thing if you use ray traced shadows  And not the virtual shadow map that luminesces the ray trace shadows will be tracing on the  Nanite proxy mesh not the high-res models so if you use hardware ray tracing for a few things  Nanite might not behave the way you expect it to


### Quixel Bridge is gone? [3:42]
**Transcript:** Just keep that in mind also if you've noticed that you cannot find the Quixel Bridge or you can't access any of the mega scans assets  Directly within Unreal Engine 5 like you could previously  You're gonna have to go into the Epic Games launcher and in the library tab in the search vault section  You need to search for bridge and  Install the Quixel Bridge plugin to your version of the engine  Once that is done the Quixel Bridge plugin will work correctly as  Intended so now with the project setting changed. I want to show you some tips for getting better reflections and


### Lumen Tips [4:11]
**Transcript:** Translucency and refraction using lumines so for starters. I've got a blank scene here  I'm going to make the lighting from scratch  So we're going to go to the windows tab here go to environment light mixer and I'm gonna create a skylight  Atmospheric light zero sky atmosphere volumetric fog and height fog  And so right now I have a very very simple quick and dirty scene  I'm going to click my skylight here and set it to real-time capture  Like that. So now we get some proper sky bouncing in my scene and  Using the control L shortcut. I can move my son like this and as we can see we get this nice  Gorgeous indirect lighting on the underside of this very bare-bones scene. It's just a quick demo scene  I know it's not super pretty, but it gets the point across so taking a look at the five spheres here  I've got a black one and 18% gray one a white one  This here is supposed to be glass using the same right trace glass material  I use in this video right here  Which again you should go watch if you want to learn how to make a nice glass material and  Here I've got a chrome material a perfectly reflective chrome material  Mirror ball if you will. I'm just gonna select these and hide t...


### Reflection Options [5:42]
**Transcript:** I've got a chrome material, but you'll see the reflections are kind of  Eh, they're very mediocre not super great  This is a classic case of lemon reflection now the cool thing about lemon reflections is as I move the sun around  You actually see the global elimination being reflected in the chrome ball, which is great  We were never able to get  Global elimination to reflect with raytrade reflection to new e4  But you know the reflections are not super great as I zoom in here. You'll see they're very  blurry and not sharp for people who work in archbiz. I hear you  This does not hold up. This is usually fine for anything that's kind of like a soft chrome a soft metal like these tables here  This works fine. It's usually good enough  But for those of you who need the absolute best possible reflections  This is not good enough. So what do we do?  There's a few things that we can do here  We're gonna select our post-process volume here and of course make sure that it is  Unbound to make sure that the post-process volume affects the entire scene and  We're gonna search for  Lumin and here is where we have a whole bunch of options to shoot from the one that we want right here is  the r...


### New Lumen Reflection Options [7:15]
**Transcript:** But what really is interesting is the ray lighting mode and if I click on this and set this from project default to  Hit lighting for reflections  Notice how suddenly our reflection got a whole lot sharper. I'm gonna zoom in as much as possible pay attention to the floor here if I toggle  This back to default it went from this which is very soft and kind of blurry to  This which is much sharper and actually does look  Substantially better. It is quite a big improvement. I'm gonna go over here where I have some other  Chrome balls here and in the shadowed area just to get a different camera angle on this I'm gonna revert this to default  so this is a default Lumin reflections and  This is the hit lighting for reflections the reflection got a bit sharper  But notice the reflection of the reflection right here as I zoom closer we kind of see  This we don't see the reflection of the reflection in the chrome ball in theory this chrome ball should be reflecting  It's neighbor here and it sort of does but only on a screen space basis. Okay, so if not a perfect solution  It's a bit of a trade off you get some sharper cleaner reflections at the cost of losing subsequent bounces  So if you h...


### Raytraced Reflections [8:58]
**Transcript:** This is not perfect. It's not exactly what we're looking for  So we're gonna go ahead and instead of using Lumin reflections  We're going to use the hardware raytrade reflections  Which we have access to now because it'll be changed our project settings earlier  So again in the post process volume I'm going to search for  Ref for reflection and you'll see here in the reflections method  Lumin I'm gonna turn this off  And I'm going to set it to stand-alone raytrade  deprecated and you'll see our reflections got  Super tack sharp like really really crisp and clean reflections pay attention to the shadows in the reflection  This is Lumin and this is hardware raytrade everything is way sharper weight cleaner  You get much better reflections that way, but now you'll notice that we kind of lost our global illumination in our scene  Pay attention to the whole top of the chrome ball here  Hardware raytrade thing never did reflect global illumination and that's kind of a bummer  We kind of lost that nice lemon reflection seat feel here, right? If I reset it to lemon reflections  We get a better reflection. It's not a sharp but it's a more accurate one  But we still have a few tricks of our ...


### Raytraced Translucency [12:41]
**Transcript:** Refraction here you'll see the refraction here. It looks really really bad  And so this glass material is very simple. I just have a base color of zero a  Specular of one a roughness of 0.05 and opacity set to 0.1 and the refraction set to 1.5  1.5 because the IOR or the index of refraction of glass is  1.5 then I have my blend modes at the translucent and  Lighting mode set to surface forward shading and that's it hit apply  I go way deeper into the glass setting in this video right here  But obviously this glass doesn't look very good. So what do we need to do?  What do we need to change to get this to display properly the same way it did in UE4?  So again, we're going to go now our post process volume and in the search details panel of the post process volume  we're going to search for translusancy and  We're going to change the type from raster to ray tracing  And now this is actually behaving the way it should be the same way it was in UE4  This is now possible all because of the project settings that we changed at the start of this video  So that's very very important and it should go without saying but I'm gonna say it again because people seem to not realize this  If you're...


### Outro and Recommendations [15:21]
**Transcript:** We can get proper  Refraction in our glass materials and so that covers the main  Issues I've seen a lot of people struggle with this week if you want to learn more about the path tracer or ray trace  Translucency or lumen or nanite you can watch all of my videos on the topic right here  So I hope you guys found this video helpful and if you did do consider subscribing because I do have a whole bunch more  Tutorials like this coming soon. So as always, thank you so much for watching and I'll see you next time



---

## Structured Notes

### Core Technique
Fixing the three most common UE5.0 confusion points for UE4 migrants: getting sharp Lumen reflections (hit lighting mode + HWRT option), restoring ray-traced glass refraction (translucency type = Ray Tracing), and understanding Nanite's path tracer limitation.

### Summary
15-minute troubleshoot video clarifying UE5.0 changes that confused many UE4 users. Core message: Lumen doesn't need RTX hardware for GI, but if you want sharp reflections you have options. Covers the full reflection quality ladder, correct translucency settings for glass materials, and the Nanite + path tracer caveat.

### Key Steps

**Project Settings (HWRT + Path Tracing):**
- Settings → Project Settings → Rendering:
  - Dynamic Global Illumination = Lumen
  - Support Hardware Ray Tracing ✓
  - Use Hardware Ray Tracing When Available ✓
  - Path Tracing ✓
  - Default RHI = DirectX 12
- Note: Lumen GI works without HWRT (software Lumen runs on GTX 1070-1080)

**Lumen Reflection Quality Ladder (worst → best):**
1. Default Lumen reflections: blurry, soft, but captures GI in reflections
2. **Hit Lighting for Reflections** (PPV): Lumen → Ray Lighting Mode → Hit Lighting for Reflections
   - Much sharper reflections
   - Loses multi-bounce reflection-of-reflections
3. **Hardware Ray-Traced Reflections** (PPV): Reflections → Reflection Method → Standalone Ray-Traced *(deprecated)*
   - Sharpest possible
   - Loses GI in reflections entirely (reverts to old UE4 behavior)
4. **Best of both (Lumen + HWRT)**: keep Lumen reflections but set `Lumen Reflection Quality = 4` in PPV
   - Sharpness of HWRT + GI capture of Lumen

**Fix Glass/Translucency Refraction (UE4 → UE5 migration):**
- PPV → Translucency → Type: change from **Raster** to **Ray Tracing**
- This restores the correct glass refraction behavior from UE4

**Glass Material Setup (quick reference):**
```
Base Color: 0
Specular: 1
Roughness: 0.05
Opacity: 0.1
Refraction: 1.5 (IOR of glass)
Blend Mode: Translucent
Lighting Mode: Surface Forward Shading
```

**Nanite + Path Tracer Limitation:**
- Path Tracer traces against Nanite fallback mesh (proxy), NOT the full Nanite geo
- Same issue as ray-traced shadows — low-res proxy used for performance
- Aware of this when path tracing Nanite-heavy scenes

**Quixel Bridge (UE5 migration):**
- No longer built into UE5 editor
- Fix: Epic Games Launcher → Library → Vault → search "Bridge" → install to engine version

**Skylight Real Time Capture + Environment Light Mixer:**
- Window → Env Light Mixer → create Skylight + Atmospheric Light + Sky Atmosphere + Fog
- Skylight → Real Time Capture ✓ → updates GI with sky movement (Ctrl+L shortcut)

### UE Systems / Blueprints / Settings

**Reflections PPV Settings:**
```
Post Process Volume > Lumen:
  Ray Lighting Mode: Hit Lighting for Reflections   // sharper Lumen reflections
  Lumen Reflections Quality: 4                       // HWRT-quality with Lumen GI

Post Process Volume > Reflections:
  Reflection Method: Standalone Ray-Traced           // sharpest; loses GI in reflections (deprecated)
  
Post Process Volume > Translucency:
  Type: Ray Tracing                                  // proper glass refraction
```

### Difficulty
Beginner — migration guide for UE4 users confused by UE5 changes

### UE Version
UE 5.0 (some settings apply to all UE5 versions)

### Tags
lumen, reflections, hardware-ray-tracing, translucency, glass, nanite, project-settings, william-faucher, beginner, ue5

---

## Related Entries
- `tutorials/lumen-explained---important-tips-for-ue5.md` — Lumen internals deep dive
- `tutorials/fixing-the-ugly-shadow-issues-in-unreal-engine-5.md` — Nanite ray-traced shadow issues
- `tutorials/path-tracer-explained---unreal-engines-underrated-tool.md` — Path Tracer details
- `references/rendering-pipeline.md` — Full rendering settings reference
