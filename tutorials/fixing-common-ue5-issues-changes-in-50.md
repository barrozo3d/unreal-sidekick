---
title: Fixing Common UE5 Issues! Changes in 5.0
source: YouTube
url: https://www.youtube.com/watch?v=wTYM9TfckOQ
author: William Faucher
ingested: 2026-06-23
ue_version: "UE 5.0"
tags: [lumen, reflections, ray-tracing, translucency, glass, nanite, path-tracing, project-settings, rendering, troubleshooting, beginner]
extraction_status: complete
frames_dir: tutorials/frames/fixing-common-ue5-issues-changes-in-50/
frame_count: 10
---

# Fixing Common UE5 Issues! Changes in 5.0

**Source:** [YouTube](https://www.youtube.com/watch?v=wTYM9TfckOQ)
**Author:** William Faucher
**Duration:** 15m51s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** So with the 5.0 release of Unreal, I've noticed across many message boards and forums that a lot of people are actually  Pretty confused about some of the changes we've had so far  Notably with the Lumen reflections, refractions, and even things like how do we even turn on the path tracer?  So this is going to be a very quick and dirty video just to help clarify a few issues that some of you may have run into and  I'll be pointing you towards some other videos on my channel that will go more in-depth about those topics.  Now for starters, Lumen does not require RTX or hardware ray tracing to work.  UE5 will work with older GPUs like the 1070 to 1080. Lumen is not dependent on that.  But those of you coming from UE4 will undoubtedly have noticed that  the Lumen reflections and refraction are not nearly as good as they were with  raytrade reflections in UE4, but don't worry. This is not a step back.  There's just a few settings that we need to change to get both the benefits of the GI and Lumen and  Gorgeous raytrade reflections. And the easiest way to do that is when you're creating a brand new project  Just turn on the little raytracing checkbox right here. That's going to enable all of the raytracing settings  But you're also going to keep Lumen as well. But of course if you have an existing project that you want to just enable hardware raytracing on

**Frame:** tutorials\frames\fixing-common-ue5-issues-changes-in-50\frame_000.jpg

### Important Project Settings [1:18]
**Transcript:** Let's take a dive into the necessary project settings to get that to work.  We need to go to the settings tab here  go to project settings and  We're going to go down to the rendering tab down here on the left hand side and  scroll down and the following settings are the one that you really need to have  Dynamic global lumination set to Lumen reflection method. We can leave that aluminum for now  We can override this in the post-process volume later  But what we really want is support hardware ray tracing turned on and  Here in the Lumen tab use hardware raytracing when available make sure that the checkbox is turned on as well  You may get a message that says something along the lines of  Enabling the skin cache when turning on the hardware ray tracing. Just click yes  You need to have that enabled. We're also going to turn on the path tracing checkbox right here  I believe it's actually off by default. So if you want to use the path tracer  You can turn it on right here  I have a more detailed tutorial on the path tracer right here. So check that out if that interests you and  One last thing that should be on by default, but isn't always it we're gonna search for direct X and  Be sure that it's set to direct X12 and direct X11 and 12 SM5 is turned on  I've seen some people who project were set to direct X11 and that was breaking a whole bunch of things so  just  Keep that in mind pro tip now with these projects setting change you may need to restart the engine

**Frame:** tutorials\frames\fixing-common-ue5-issues-changes-in-50\frame_001.jpg

### Pathtracer Tips [2:43]
**Transcript:** It's gonna have to recompile the shaders, but once that's done you're good to go and now if we go to the lit tab here  You should have the path tracer show up and it'll work as intended  Just a bit of a quick segue here the path tracer doesn't work with Nanite if you turn the path tracer on with a whole bunch of  Nanite meshes  It's only going to pass trace the Nanite proxy mesh and not the actual high-read Nanite mesh  So that is another thing you really need to keep in mind because Nanite is not exactly what we call real geo  It's virtual as geo and the path tracer doesn't really know how to read that it's the same thing if you use ray traced shadows  And not the virtual shadow map that luminesces the ray trace shadows will be tracing on the  Nanite proxy mesh not the high-res models so if you use hardware ray tracing for a few things  Nanite might not behave the way you expect it to

**Frame:** tutorials\frames\fixing-common-ue5-issues-changes-in-50\frame_002.jpg

### Quixel Bridge is gone? [3:42]
**Transcript:** Just keep that in mind also if you've noticed that you cannot find the Quixel Bridge or you can't access any of the mega scans assets  Directly within Unreal Engine 5 like you could previously  You're gonna have to go into the Epic Games launcher and in the library tab in the search vault section  You need to search for bridge and  Install the Quixel Bridge plugin to your version of the engine  Once that is done the Quixel Bridge plugin will work correctly as  Intended so now with the project setting changed. I want to show you some tips for getting better reflections and

**Frame:** tutorials\frames\fixing-common-ue5-issues-changes-in-50\frame_003.jpg

### Lumen Tips [4:11]
**Transcript:** Translucency and refraction using lumines so for starters. I've got a blank scene here  I'm going to make the lighting from scratch  So we're going to go to the windows tab here go to environment light mixer and I'm gonna create a skylight  Atmospheric light zero sky atmosphere volumetric fog and height fog  And so right now I have a very very simple quick and dirty scene  I'm going to click my skylight here and set it to real-time capture  Like that. So now we get some proper sky bouncing in my scene and  Using the control L shortcut. I can move my son like this and as we can see we get this nice  Gorgeous indirect lighting on the underside of this very bare-bones scene. It's just a quick demo scene  I know it's not super pretty, but it gets the point across so taking a look at the five spheres here  I've got a black one and 18% gray one a white one  This here is supposed to be glass using the same right trace glass material  I use in this video right here  Which again you should go watch if you want to learn how to make a nice glass material and  Here I've got a chrome material a perfectly reflective chrome material  Mirror ball if you will. I'm just gonna select these and hide them for now  The two problematic ones are these guys now obviously this glass material looks like but it's really bad  We're not getting proper refraction in there. It just does not look right in any way and on the right here

**Frame:** tutorials\frames\fixing-common-ue5-issues-changes-in-50\frame_004.jpg

### Reflection Options [5:42]
**Transcript:** I've got a chrome material, but you'll see the reflections are kind of  Eh, they're very mediocre not super great  This is a classic case of lemon reflection now the cool thing about lemon reflections is as I move the sun around  You actually see the global elimination being reflected in the chrome ball, which is great  We were never able to get  Global elimination to reflect with raytrade reflection to new e4  But you know the reflections are not super great as I zoom in here. You'll see they're very  blurry and not sharp for people who work in archbiz. I hear you  This does not hold up. This is usually fine for anything that's kind of like a soft chrome a soft metal like these tables here  This works fine. It's usually good enough  But for those of you who need the absolute best possible reflections  This is not good enough. So what do we do?  There's a few things that we can do here  We're gonna select our post-process volume here and of course make sure that it is  Unbound to make sure that the post-process volume affects the entire scene and  We're gonna search for  Lumin and here is where we have a whole bunch of options to shoot from the one that we want right here is  the reflection section at the bottom and  We've got the Lumin reflections quality now if I zoom in here a little bit now the Lumin quality if I  Toggle this between off you'll see it softens a little bit it doesn't  Really do that much. So I'm gonna leave this at two

**Frame:** tutorials\frames\fixing-common-ue5-issues-changes-in-50\frame_005.jpg

### New Lumen Reflection Options [7:15]
**Transcript:** But what really is interesting is the ray lighting mode and if I click on this and set this from project default to  Hit lighting for reflections  Notice how suddenly our reflection got a whole lot sharper. I'm gonna zoom in as much as possible pay attention to the floor here if I toggle  This back to default it went from this which is very soft and kind of blurry to  This which is much sharper and actually does look  Substantially better. It is quite a big improvement. I'm gonna go over here where I have some other  Chrome balls here and in the shadowed area just to get a different camera angle on this I'm gonna revert this to default  so this is a default Lumin reflections and  This is the hit lighting for reflections the reflection got a bit sharper  But notice the reflection of the reflection right here as I zoom closer we kind of see  This we don't see the reflection of the reflection in the chrome ball in theory this chrome ball should be reflecting  It's neighbor here and it sort of does but only on a screen space basis. Okay, so if not a perfect solution  It's a bit of a trade off you get some sharper cleaner reflections at the cost of losing subsequent bounces  So if you have a lot of shiny object reflecting one another this might not be the best approach  But I did want to point out that you can absolutely get sharper cleaner reflection using Lumin reflections with the  Hit lighting for reflections method here again. This is default settings and  This is with the  Hit lighting reflections. So this is a very useful tip to know about now as you know

**Frame:** tutorials\frames\fixing-common-ue5-issues-changes-in-50\frame_006.jpg

### Raytraced Reflections [8:58]
**Transcript:** This is not perfect. It's not exactly what we're looking for  So we're gonna go ahead and instead of using Lumin reflections  We're going to use the hardware raytrade reflections  Which we have access to now because it'll be changed our project settings earlier  So again in the post process volume I'm going to search for  Ref for reflection and you'll see here in the reflections method  Lumin I'm gonna turn this off  And I'm going to set it to stand-alone raytrade  deprecated and you'll see our reflections got  Super tack sharp like really really crisp and clean reflections pay attention to the shadows in the reflection  This is Lumin and this is hardware raytrade everything is way sharper weight cleaner  You get much better reflections that way, but now you'll notice that we kind of lost our global illumination in our scene  Pay attention to the whole top of the chrome ball here  Hardware raytrade thing never did reflect global illumination and that's kind of a bummer  We kind of lost that nice lemon reflection seat feel here, right? If I reset it to lemon reflections  We get a better reflection. It's not a sharp but it's a more accurate one  But we still have a few tricks of our sleeve  So again, I'm going to set my reflection method to raytrade in the post process volume and  We're going to go to the raytracing reflection section here and we're gonna turn on a few things  I'm gonna turn on max roughness  Max bounces and I'm gonna set the max bounces to something like five and before I hit five  I want you to pay attention to the black spots in the spheres here and the ceiling  So when I set this to something like five you'll see suddenly boom  We now have all of those subsequent bounces pay attention right here  This sphere is reflecting the reflection of the reflection of the reflection. It looks much more realistic and  We kind of got our reflections back on our roof  It's not quite the same as  Lumin reflections right if I go back to lemon reflections we do get a more accurate  Visualization and now we can also in a mac roughness  I'm gonna set this to one for maximum quality  But keep in mind this could have a performance impact on your scene  So again getting a little bit better and if you notice that your reflections are a little bit noisy  I'm not sure if you'll be able to see this on YouTube because of the compression and the denoising that happens  But my reflections are very noisy so I can  Fixed that by increasing the sample per pixel down here and set it to something like 10 and now again  This will have a performance impact, but it will clean things up nicely. So again  Not the perfect solution because you know the reflection of the chrome balls here are not  quite  matching the  Environment they are in like we're not getting the same dark shadows as we did with the Lumin reflection right again  I'm gonna toggle it back and forth just for demonstration purposes  This is with Lumin reflections you'll see the chrome balls here do seem to integrate into the scene much better than  They did with the ray trace reflections and ray traced so  You know it doesn't quite integrate as well, but sometimes you need this sometimes you need to get the better  Chris brisch upper reflections depending on your scene. So in true  Classic Unreal engine fashion you're going to have to pick the lesser of two evils here  You're going to have to pick and choose which of these options suits your specific use case the best  It's just something that you need to be aware of and art direct accordingly  Now with that out of the way the last thing I want to touch base on is the

**Frame:** tutorials\frames\fixing-common-ue5-issues-changes-in-50\frame_007.jpg

### Raytraced Translucency [12:41]
**Transcript:** Refraction here you'll see the refraction here. It looks really really bad  And so this glass material is very simple. I just have a base color of zero a  Specular of one a roughness of 0.05 and opacity set to 0.1 and the refraction set to 1.5  1.5 because the IOR or the index of refraction of glass is  1.5 then I have my blend modes at the translucent and  Lighting mode set to surface forward shading and that's it hit apply  I go way deeper into the glass setting in this video right here  But obviously this glass doesn't look very good. So what do we need to do?  What do we need to change to get this to display properly the same way it did in UE4?  So again, we're going to go now our post process volume and in the search details panel of the post process volume  we're going to search for translusancy and  We're going to change the type from raster to ray tracing  And now this is actually behaving the way it should be the same way it was in UE4  This is now possible all because of the project settings that we changed at the start of this video  So that's very very important and it should go without saying but I'm gonna say it again because people seem to not realize this  If you're going to be using hardware ray tracing you need to have a ray tracing capable graphics card  So ideally an RTX GPU  I  Shouldn't have to say it, but I'm gonna say it  Now the downside is we seem to have lost the shadows cast by the glass in UE5 in unreal engine 4.27  We did have  Glass casting shadows, so I'm not sure why we lost that it kind of sucks because it was really cool to have and  We don't have any caustic so we don't have any of that refraction being cast  On the ground the only way to get shadows and proper caustics it was the path tracer  So I'm going to go ahead to the lit tab here  Turn on the path tracing and you'll see now glass looks way way way better  We're getting proper shadows and  Costics being refracted here if I use this glass material on one of the tables here  You'll see it is actually casting its correct shadows  It's refracting light in a really pleasant way. It looks way better than in  Regular lit mode like this just doesn't  this look weird  real-time  glass  Still does not look nearly as good as true  pass trace glass  That's just a limitation of real-time engines at the moment, but at least now with ray trace translucency

**Frame:** tutorials\frames\fixing-common-ue5-issues-changes-in-50\frame_008.jpg

### Outro and Recommendations [15:21]
**Transcript:** We can get proper  Refraction in our glass materials and so that covers the main  Issues I've seen a lot of people struggle with this week if you want to learn more about the path tracer or ray trace  Translucency or lumen or nanite you can watch all of my videos on the topic right here  So I hope you guys found this video helpful and if you did do consider subscribing because I do have a whole bunch more  Tutorials like this coming soon. So as always, thank you so much for watching and I'll see you next time

**Frame:** tutorials\frames\fixing-common-ue5-issues-changes-in-50\frame_009.jpg


---

## Structured Notes

### Core Technique
UE 5.0 migration troubleshooting: project settings for hardware RT + Lumen combo, reflection quality options (Lumen vs. Hit Lighting vs. Hardware RT trade-offs), fixing glass refraction with ray-traced translucency, Nanite + path tracer proxy caveat, and Quixel Bridge reinstall.

### Summary
William Faucher addresses common UE 5.0 migration issues. Key clarification: Lumen works without RTX (GTX 1070+). RT reflections require project setting changes. Three reflection choices: (1) default Lumen (soft, GI-accurate), (2) Lumen Hit Lighting (sharper, loses multi-bounce), (3) Hardware RT Standalone (crispest, loses GI in reflections — fix with Max Bounces=5 + Max Roughness=1). Glass refraction: PPV → Translucency → Ray Tracing. Path Tracer: Nanite proxy caveat. Quixel Bridge: must reinstall as plugin from Launcher. 15 minutes, UE 5.0 specific but largely applies to UE 5.x.

### Key Steps
1. **Enable hardware RT + path tracing:** Project Settings → Rendering → Dynamic GI=Lumen; Reflections=Lumen; Support Hardware Ray Tracing=true; Lumen tab → Use Hardware Ray Tracing When Available=true; Path Tracing=true; search "DirectX" → DirectX 12 + DirectX 11/12 SM5 = enabled; accept Skin Cache when prompted; restart
2. **Quick scene setup (Lumen):** Window → Environment Light Mixer → create: Skylight, Atmospheric Light 0, Sky Atmosphere, Volumetric Fog, Height Fog; Skylight → Real-Time Capture=true; Ctrl+L to move sun
3. **Improve Lumen reflection sharpness:** PPV → search "Lumin" → Lumen section; Reflections Quality=2 (minor); Ray Lighting Mode → Hit Lighting for Reflections (much sharper — but loses mirror-on-mirror bounces)
4. **Hardware RT reflections:** PPV → Reflections Method → Standalone Ray Traced (deprecated); sharper/crisper; loses GI in reflections; fix multi-bounce: RT Reflections section → Max Bounces=5; Max Roughness=1; Samples Per Pixel=10 (reduce noise); trade-off: worse scene GI integration vs. Lumen
5. **Ray-traced glass refraction:** PPV → Translucency → Type → Ray Tracing; requires hardware RT GPU; note: glass shadows and caustics only work in Path Tracer (not real-time lit mode)
6. **Path Tracer:** lit dropdown → Path Tracing; Nanite meshes = traced on proxy not high-res (same for RT shadows + virtual shadow maps); requires DirectX 12
7. **Quixel Bridge reinstall:** Epic Launcher → Library → search "Bridge" → install to target engine version → restart UE
8. **Nanite + hardware RT caveats:** RT shadows + Standalone RT reflections trace Nanite proxy mesh (not high-res Nanite geo); use Lumen's virtual shadow maps for Nanite compatibility

### UE Systems / Blueprints / Settings
- **Hardware RT Project Settings**: Support Hardware Ray Tracing + Use HW RT When Available (Lumen tab) + Path Tracing checkbox + DirectX 12
- **PPV Lumen Reflections**: Quality slider (minor), Ray Lighting Mode: Project Default vs. Hit Lighting for Reflections (sharper, no multi-bounce)
- **PPV Reflections Method**: Lumen (default, GI-accurate) vs. Standalone Ray Traced (crisp, no GI in reflections); deprecated term but still works
- **PPV Ray Trace Reflections section**: Max Bounces, Max Roughness, Samples Per Pixel (denoise tradeoff)
- **PPV Translucency Type**: Raster (default, broken glass in UE5) vs. Ray Tracing (correct refraction, needs RT GPU)
- **Nanite + RT caveat**: hardware shadows, reflections, and path tracer all trace proxy mesh not Nanite virtual geo; use Lumen + virtual shadow maps for Nanite scenes
- **Glass material basics**: Base Color=0, Specular=1, Roughness=0.05, Opacity=0.1, Refraction=1.5 (IOR); Blend Mode=Translucent; Lighting Mode=Surface Forward Shading

### Difficulty
Beginner — project settings focused, practical fixes

### UE Version
UE 5.0 (most settings still apply in UE 5.x)

### Tags
[lumen, reflections, ray-tracing, translucency, glass, nanite, path-tracing, project-settings, rendering, troubleshooting, beginner]

---

## Related Entries
- demystifying-the-skylight-unreal-engine-4-5.md (skylight setup for scene integration)
- easiest-way-to-get-cinematic-renders-in-unreal-engine---path-tracing.md (Path Tracer deeper setup)
- fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro.md (Nanite + Path Tracer fix)
