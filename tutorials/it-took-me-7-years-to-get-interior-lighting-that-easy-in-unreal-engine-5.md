---
title: It Took Me 7+ Years To Get Interior Lighting That Easy in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=MJQ-0tmIhQk
author: Karim Yasser
ingested: 2026-06-23
ue_version: "UE5"
tags: [lighting, interior, lumen, fog, ray-tracing, reflections, tone-mapping, color-grading, performance, workflow]
extraction_status: complete
frames_dir: tutorials/frames/it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5/
frame_count: 13
---

# It Took Me 7+ Years To Get Interior Lighting That Easy in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=MJQ-0tmIhQk)
**Author:** Karim Yasser
**Duration:** 33m5s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** And today's video is going to discuss interior lighting to do this scene from scratch step by step  and fix indirect lighting issues with Lumin, eliminate the blotches and flickering,  improve volumetric fog and shadows, and understand the approach of interior lighting in Unreal Engine.

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_000.jpg

### Project Settings [0:12]
**Transcript:** So to start with interior lighting, we need to adjust first our project settings.  So we can go here in Edit, Project Settings, and scroll down for Rendering.  And we need to use bunch of options actually for Lumin and Red Tracing  and to give our scene these kind of soft shadows in it.  So let's scroll down.  We need first to ensure that we have dynamic global eliminations at the Lumin.  Same goes for reflections.  And here in the support hardware ray tracing, this need to be enabled.  And this one as well, ensure it's enabled.  Use hardware ray tracing when available.  And regarding ray lighting mode, we can adjust it later in our process volume  and test out different settings in it.  Also, we don't need to use generate mesh distance fields as we are going to depend on hardware  ray tracing. Scroll down here. I need to ensure local exposure, highlight contrast and shadow  contrast are set to 1. I just like to have it as default on 1.  And here in the G buffer format, set it to high precision normals.  And if you want to use mega lights, it's fine to turn it on.  I want to keep it on actually because mega lights will give me this kind of soft shadows as well  because it uses great ray shadows by default.  So it's already very soft shadows.  And here scroll down in platforms, Windows,  ensure we are using Shader Mode 6 and DirectX12 as our default RHI.  And if you want to follow with the same environment, it's added here.  I think it's for free. By learning this, you can use it and follow up with the tutorial to  get the same results. So now I need to restart the engine to get all of these changes applied  to my scene. Here it might take some time on your side to re-opened,  present to a combined amount of shaders and do all of these calculations to use the new settings.  We need them to ensure here we don't have any lighting actors and no-bake lighting actors.

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_001.jpg

### Lighting Cleanup - Remove Baked Lighting [2:20]
**Transcript:** So let's first of all ensure we don't have any light in here. Remove all of them.  All of these light actors.  And let's ensure we don't have any reflection actors as well.  Sponential height fog, post-process volume. All of these actors needs to be deleted.  And for our sky, for me it's fine to give it as it is for now as we are going to use it.  Maybe we can try different texture or just hide it with the fog or so.  So for now this is our scene, it's completely black but we would need to ensure it doesn't have  any pre-computer lighting. So I can go to Window, World Settings, and here in Lightmass,  up in this option, reset all of these settings, go to Advanced, and here we can see Light Maps.  They are added already. So let's head for Snowpreet commuted lighting. It's okay.  And here if it doesn't work, select build all levels. And just like that, Light Maps will be zero.  And if it's not updating, you can restart the level directly and it will work.  So now we have our scene ready, it's clean, it doesn't have any big lighting, and all good to go.  So what we will need to do first, in my opinion I need to disable all of these  emissives first of all. So I can go here, set the emissive to zero. I don't need any  massive sources in here. And I want to set up a main camera. And here in Prespective, press on it,  go to create camera, see any camera actor, and right click on it, and go to pilot.  So I'm controlling the camera now. And let's have a good  base of our camera. Let's keep it like this just for now. And look our camera,  right click on it, go to transform, look actor movement. So it remains static and doesn't move  by mistake. So for now, let's use this guy, go here in this sky,

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_002.jpg

### Skylight Setup [4:52]
**Transcript:** let's see if we can control the tent. Yeah, we can. Let's control our tent. I want to have  somehow a night lighting, moody, very soft. So let's try to have it like that. Maybe around  0.5 0.6. It's fine. Save. And for the massive, give me that one. And let's add a folder for lighting.  There is lights, let's call it lighting. Right click on it, make current folders. So anything we  add in here will be dropped automatically to this lighting folder. So I'm adding a boss process  volume, scroll down, enabling infinite extent. So it affects all my environment without the need  to rescale it. Go here in exposure. I'll just go with the very basic exposure, set it to one and  one and start working from this base, also setting exposure compensation on zero. So I can now  select my sky, make it a little bit brighter, you're around 5, probably. And I will need to move  this sphere to our lighting folder and add a skylight. So I can start getting more ambient lighting  in there. And in my opinion, it's very blue currently. So I can go in my sphere and reduce the  saturation of my sky. Go here in the tent and reduce the saturation to going to probably or  2.25. Go back to the skylight and hit recapture. And now yeah, I think this is really much better.  I just need to increase the cube map resolution a little bit. 5, 200 would be good. And let's add  that. Actually, let's try first to increase the skylight density. If we try to have it a very high  number like that, it would be very, very bright and it's not working correctly. So we can keep it at first.  This one, we can keep it on three probably. And let's go back to our boss process volume to

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_003.jpg

### Tone Mapping [7:23]
**Transcript:** turn map our scene without the need to add a lot of lights in there. So let's go to local exposure.  Let's try to set this one to 0.6. And let's keep the highlight contrast as it is. Maybe here for  the two, let's reduce it a little bit. And we can see more details in here already without the  need to add a lot of lights. And let's actually try to add our fog volume, reset the location of it.

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_004.jpg

### Fog & Atmospherics [7:54]
**Transcript:** And let's give it a color. Something probably. Just give it one one. Let's try color.  Maybe like that. I just want to give it this color or cyan color. Like it's very saturated actually.  So I'm just trying a new color in here. It's not like blue or very blue night. It's enabled for  the metric fog. And actually it's too bright outside. So I can use the value of it to make it  better. Yeah, like that. And if I try to hide the sky sphere, it might be really looking better,  but our skylight will not be working good. So we need to keep it actually. So let's keep our fog  like that. And let's try to add a spotlight. So it's more like outside or exterior lighting.  Let's give it like this. Let's disable this nabbing. And here let's try to make this 100 maybe a thousand.  That it's right actually to go very crazy number like 10,000. So good color. Let's get the same  hue from here. It's the 94. And almost 2.7. It would be good. Let's try to make the cone smaller.  That. And let's try to add very strong volumetric scattering, but you'll see why I'm doing this now.  Let's get back to the another view board. Switch it to on left. And I can right click on this light.  Go to pilot. And I can move it like this. So I can go here. Let's actually present the rotation. So  it re-ins better. Can give it like this. Can go here. Maybe something like that.  And yeah, this should already block by lighting, but let's select all of these light blockers in here  and add a black only material. If you cannot see it, you can go here and show engine content. You can see  black only material. And let's actually try to add another one. Let's go here in words. Let's add  another one here. Just to plug our light from this side. And yeah, control shift P and we can.  Let's try something like this. Scroll down here. Enable  Cosvolumetric shadow. So it's already working better. It's not going everywhere.  This is too much for sure. Let's try to reduce it. 10. So I can start. And I can select like this  one for example. Try to turn off the shadow from it. It wouldn't work much better actually. And if I try  to select my lighting and here I disabled mega lights or we used virtual shadow map with it, it

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_005.jpg

### Fix Ray Tracing Shadows [12:11]
**Transcript:** will work much better. Cosratorate shadows doesn't work perfectly with submeshes, especially like translucent  meshes or so. So we can try it like this. And let's try to increase the attenuation radius a little  bit. Try 1500. This is too much actually my opinion. Back intensity, but I can reduce it like 5000  or try 2000. Yeah, maybe 2000 is good. And this increases the volumetric scattering to 100 probably.  As you can see now it's very soft. Like it's already much better. And if I try to increase the  outer context just increases the intensity here. So I can try 40. And so it could be adding more  intense light as the fall of is going to be sharper. So it's stick to 20 could be good. And here for  this light it's very very sharp currently as you can see. These shadows are too sharp. So we can  increase the source radius like that. And the source radius basically increases the size of the  light itself. So as you can see this yellow sphere is the source radius. And the bigger it becomes  the softer the shadow will be. Let's actually try to add another  I just need to plug my light in that better way. So this should be better actually.  So let's try here to increase the source radius. Let's try 100 probably. And you might notice  this here it's already getting bigger light source or it's very noticeable. And we can fix that

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_006.jpg

### Soft Shadow & Specular Fix [14:16]
**Transcript:** or actually before fixing it. If we try to see it from a chrome bowl let's apply a chrome  material to it. We try to see it from here. As you can see there is a big big sphere from our  light source. So in order to fix it there is two ways. You can go down here and reduce the  specular scale. But that will make you lose your specular reflections on your meshes.  Or you can increase this one soft source radius. Increasing it will make it softer. So it will  be more diffused and much better. So we can get back here. And as you can see the soft source radius  is already making it much much better softer. And it does make more sense actually as light source.  So let's reduce this light source a little bit. So as you can see now it's very soft like that.  Maybe the fog is too thick and we will reduce it. And the soft source radius could be reduced as well.  Maybe 200 could be good. So now our light is very very soft actually and it's not eliminating

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_007.jpg

### Adding Lights & Polishing [15:36]
**Transcript:** everything in the scene like that. It's not very good. I'm just limiting it to this specific  place. So it's feeding out and it looks much better. And if we try to make it like that could be  even better. Like this. So it's even softer. You can try a lot of things in here actually.  But let's stick to it like this. You might notice there is some noise still in here. This is  related to Lumin and yeah same goes here. So we will need to fix it for sure. But I think the  intensity is too much for now. Let's reduce the intensity a little bit. Maybe it's still too intense.  I think 1000 could be good. Yeah, let's give it 1000 but reduce the volumetric scattering.  Let's try 80 could be good or actually let's give it on thread.  Yeah, 100 could be good. Yeah, 100 is good. And here for indirect light intensity if we try it  more. Because you can see it adds even more to your eye in there. Let's stick to two or three  could in our case. And here's still I want to add more lighting actually to fill in these very  dark shadows. So I can use other point lights probably. Let's add one here.  And it's very very sharp right now. So we need to fix it. As you can see this very sharp  doesn't work like that in real life. So we can sit it to let's try 100. Let's try 10. As  I start let's reduce the radius a little bit. Try 300 and temperature. And before temperature  we can just increase the source radius. Five. Yeah, five could be good.  Just like that. So let's try five. Give it on five. And for the temperature,  let's try something like that. Or if you want to control it with color it's totally fine.  So if you wanted to have more contrasty color yellowish color. So it's really valid. It's up to you.  Actually I like it more like let's stick to it as a yellowish color. Like that was very high  contrast between them. And for indirect lighting, let's give it one. And for the sketch,  let's try five probably. And for the reflection, if you want to fix it, you can use source radius  as mentioned. So it's already softer and really really better. And it's a noticeable here on that  glass. So we can increase the source radius a little bit.  So I think maybe intensity is too much. I think five could be good. And we can duplicate this one  to add on other locations. Like this one.  Yeah. Just like that.  To add more lighting in there. And it might even in this might be too small. So let's increase it  to 500. Add more GI.  Actually, let's try 600. It could be good. Here for this one is try 400. It's 500.  Actually 400 could be better. So it doesn't have everything elevated in a very bright way.  Actually, let's try to reduce the saturation.  Maybe this could be better.  Instead of having very strong tenth of yellow. So yeah, let's try to keep it like this.  Yeah, this could be good. And for the immeasive, I just need to go here in this one.  And I will duplicate it. Apply it for these two. Because I want to have this one.  The immeasives. Like that.  But I need to change the color of it.  So I can have it like this. 4000 and reduce the strength of the immeasive.  Then, let's apply the same material here for this one.  Last one. And now our scene is ready. Looks better with just 304 light sources. The fog, the sky,  two wind lights and one spotlight. We need then to go in our post-process volume to start

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_008.jpg

### Post Process Color Grading [21:44]
**Transcript:** adding more effects in there. So we can use convolution bloom if you want to have  a different shape of the bloom like that.  But as you can see, this is not very good. This is too much. And it's not working as expected.  So let's reduce it. We can just keep it on one or two. Maybe.  Two could be good. One. Maybe 1.5. And for chromatic aberration,  we need slightly more chromatic aberration.  Still a wind one. Look at exposure. We can adjust the shadow contrast now. Instead of the  0.6, we can have a light layer number like that. Same goes for highlight contrast if we want  to reduce it. So it affects our exterior lighting like that. But I like it. I actually  just give it as it is. Or if you wanted to increase it to have more contrast in there.  For detailed strength, I like to increase it. Maybe 1.2. But that will affect our highlights.  So we need to get back to our bloom and reduce it. One.  And major effects. Let's add some more sharpen and slightly. That in color grading,  I like to reduce the shadow saturation. Let's try to wind 4.5. And in the gain.  Maybe I can give it a little bit of finish or close attempt.  But this is too much actually. Maybe increase it.  So it's the color. Yes, you can see. This is light adjustment, but it already adds a lot to the scene.  For mid-tones, let's increase the contrast a little bit. So 1.2.  0.5 is too much. 0.3. 1.2 could be 1.2 could be good. And how about the gain?  0.1 for the gain could be good as well. And for global, if you wanted to increase the offset a little bit,  to add more to your scene in general, it's quite okay to have it like that.  And here in saturation, 3 depends on your preference if you want to reduce saturation or increase the saturation.  But I prefer to reduce it a little bit. So just slightly less like that. And we can hear  just the temperature again. We increase it. It will be pretty much different about.  So we can go colder or warmer. 3 depends on your preference.  I think I can go slightly warmer like that around 7000. And slightly more intent.  Like that. Now here in global elimination. Let's go in the global elimination. Let's try to use headlighting.

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_009.jpg

### Fix Lumen Noise [25:18]
**Transcript:** So this is already the best version of looming that it is possible. You might notice this kind of  flickering in here and in there as well. So we will need to use this console command.  R.looming.c.in.radiosity.visualized.prox.  As you can see now, this is how the Omin is trying to work. So that's why it's  flickering a lot. We can fix that by using R.looming.c.in.radiosity.emisphere from resolution.  And the default value of it currently is 4. So let's try 32. So it's already much better.  So this is 4. As you can see it's very, very fast and it's trying to update very fast way.  This is slightly better now. So we can try to use that to fix this problem. Let's get back to zero.  And here we can increase the lumensine lighting quality and lumensine data. Let's say post 4.  And this affects our lumensine view. We can go here in lumensine and see it probably.  As we can see now, our process volume, we try to set this one to the lowest possible.  Like a lot of objects are already removed from the renderer of the domain.  So increasing it will make it better. And here in final gather quality, let's try to increase it for.  And in advanced settings, if you wanted to use lumensine to reduce it. So you can reduce that  lacquering as well. This is a trick that you can do. But I just want to give it as a fault.  Get back to your left view mode. And here in reflections, let's try to keep this one. High  quality translucent zero reflections enabled. It's already affecting our light bulbs here.  So this is how it looks without it. It's very fake and it captures the sky. But this is much better.  And it's really reading the environment around it. And max roughness to trace.  If you want to debug it really well, you can go to lumens,  dedicated reflection rays. Here anything that is red is calculated in lumens reflections.  And once you increase it, you can increase the amount of the meshes that is being included.  So reducing that will for sure improve the performance, but will make our reflections look  slightly worse. So if you don't care about performance a lot in this scene, you can go all the way up.  What? So here the difference, as you can see, you can notice it on the ceilings, on the  ground, on the chairs, tables, anything actually in the scene. It already looks much better.  And for max reflection bounces, it is if you want to get more bounces of your reflections  inside your reflections. So this could be noticeable. Not sure if it will be noticeable here.  But this is basically more noticeable if you have a chrome ball. And there is another mirror  or a chrome ball in front of it or beside it. So you cannot see the reflection of the first  chrome ball in the second one unless you keep this option more than one. And usually in most cases,  like this one, it's very, very small change. So you don't need all the time to increase this one.  Same goes for max reflection bounces, but in this scene it will affect it much better.  And we are already having much better reflections here. It was a lighting without the leaking  that we are getting now from our sky because these are like, trust me, meshes. So this is already  much better. Here I just want to increase the phone green, try one. And then we give these shadows  a little bit. Six, four, three, two, one. Highlights. That's basically in our indoor lighting. It's

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_010.jpg

### Improve Volumetric Fog Sampling [30:03]
**Transcript:** how you think about it if you have a light source or a big opening like that and how you can  use effects, your shadows make it softer and get even better lighting. And we have still one  thing left. We can see here in the volumetric fog, it could be even better. So we could try  our dot volumetric fog. Let's try grid pixel size. Divoled value is eight. And if you are going  lower you will basically get better fog. But be careful with it because it could draw  when you were to be performance and it might crash. So I'm trying to go to four.  As you can see now four is even softer and much, much better. This is eight. It's not looking good.  This is 16 if you want to get bad. This is four. This is one. As you can see one is very, very soft  because it's casting the volumetric shadowing actually from these meshes. So that's why it's  looking very soft and good. Let's give it to three. It could be good in this case. And there is  another one actually which is a red size z. It's default value is 128 and you can go higher.  So let's try 512. See how it looks. This is 512 and this is 128. This is 32. 32 as you can see  it's really, really bad. So you'll need to increase it. 12 could be good.  For 1024 it's even even better. But now as I'm noticing my performance is starting to  drop down a lot like 40 years. If I get back this one to default 128 and this one as well to  default 8 it's ready better. But for rendering purposes it's fine to have these ones on some high  numbers like that.  It's totally okay because you don't need to worry about rendering time when you're  getting some good cinematic sequences. So yeah that's pretty much it about today's video.

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_011.jpg

### Quick Note [32:41]
**Transcript:** Render lighting. I hope you enjoyed it. And don't forget to join our discord community if you  want to get more tips and learn more about lighting, the environment, characters, anything related  to game art. Feel free to join our discord community and stay in touch with other talented people  so that's it for today's video. See you next time.

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_012.jpg


---

## Structured Notes

### Core Technique
Interior lighting from scratch using Lumen + Hardware Ray Tracing + Mega Lights for cinematic-quality soft shadows. Key techniques: project settings configuration (DX12, hardware RT, High Precision G-Buffer, Mega Lights) → lighting cleanup → sky sphere + skylight as ambient base → spotlight for exterior-beam key light with shaped **light blockers** (black-only material meshes) → Source Radius + **Soft Source Radius** for area light behavior → Lumen noise fix via `r.Lumen.Radiosity.HemisphereProbeResolution 32` → volumetric fog quality with `r.VolumetricFog.GridPixelSize` → reflections polish via PPV Lumen settings.

### Summary
33-minute Karim Yasser tutorial for interior lighting in UE5, targeting cinematic quality. Starts with critical project settings (Lumen DX12 pipeline, hardware ray tracing, Mega Lights for soft shadows, G-Buffer High Precision Normals). Cleans all pre-baked lighting. Establishes ambient base with sky sphere + skylight; sets tone with Local Exposure Shadow Contrast 0.6; adds Exponential Height Fog with volumetric. Main key light: spotlight simulating exterior beam entering interior, shaped by black-material mesh blockers (Cosine Volumetric Shadow), very high Source Radius for soft shadows, Soft Source Radius to remove specular artifacts. Adds warm point lights as practicals. Full PPV color grade. Fixes Lumen flickering via console variable for probe resolution. Improves reflections via PPV Lumen settings (High Quality Translucent Zero Reflections, Max Roughness to Trace). Optimizes volumetric fog with `r.VolumetricFog.GridPixelSize` console variable.

### Key Steps
1. **Project Settings** (Edit → Project Settings → Rendering):
   - Dynamic Global Illumination: **Lumen**
   - Reflections: **Lumen**
   - Support Hardware Ray Tracing: **ON**
   - Use Hardware Ray Tracing When Available: **ON**
   - Generate Mesh Distance Fields: **OFF** (hardware RT replaces SDFs)
   - Local Exposure Highlight Contrast + Shadow Contrast: reset to **1** (defaults)
   - G-Buffer Format: **High Precision Normals**
   - Mega Lights: **ON** (provides ray-traced soft shadows with low overhead)
   - Platform → Windows: Shader Model 6, DirectX12 as default RHI
   - Restart engine after changes
2. **Lighting cleanup**:
   - Remove all Lights, Reflection Captures, Exponential Height Fog, PPV from level
   - Window → World Settings → Lightmass → Force No Pre-Computed Lighting → Build All Levels (zeroes lightmaps)
   - Restart level if lightmaps don't update
   - Set all emissive material values to 0 before starting
3. **Camera**: create camera actor → right-click → Pilot; right-click → Transform → Lock Actor Movement (prevents accidental move)
4. **Sky sphere**: adjust material tint/saturation for desired time of day (night = blue/low saturation ≈ 0.5 saturation)
5. **PPV**: infinite extent; exposure min=1 max=1, compensation=0 (temporary base to see the scene)
6. **Skylight**: Movable; Real Time Capture; Cube Map Resolution 512; Recapture after sky changes; reduce sky sphere saturation if skylight is too blue
7. **Tone Mapping**: Local Exposure Shadow Contrast → **0.6** to open up dark areas; Highlight Contrast reduce if needed
8. **Exponential Height Fog + Volumetric Fog**: add fog volume; set color (cool cyan for night); enable Volumetric Fog; use fog value control to prevent over-bright exterior bleed
9. **Key spotlight** (exterior beam entering through window):
   - Add Spotlight; disable nabbing; intensity 1000-2000; small outer cone angle 20-40°
   - **Volumetric Scattering Intensity**: 80-100 for god ray beam
   - **Light Blockers**: place mesh planes with **Black Only material** (search Engine Content for "Black Only") to block unwanted light spill on sides
   - Pilot the spotlight to position beam (right-click → Pilot)
   - Enable **Cast Volumetric Shadow** (Cosine Volumetric Shadow) for fog/mesh shadows
   - If using Virtual Shadow Map → switch to **Mega Lights** for soft shadows (VSM doesn't work correctly with sub-meshes/translucent)
10. **Source Radius** (for area shadows): increase Source Radius to soften shadows (yellow sphere in viewport shows light source size)
    - **Soft Source Radius**: increase to diffuse specular highlight from enlarged Source Radius (prevents distracting specular blob); use a chrome ball to inspect
    - Source Radius 100, Soft Source Radius 200 is a reasonable starting point
11. **Fill point lights** (practical/ambient fill):
    - Source Radius: 5; Attenuation Radius: 300-600; Indirect Light Intensity: 2-3
    - Temperature: warm (yellowish ~4000K) for warm interior practical look
    - Reduce saturation if too orange
12. **Emissive practical lights**: duplicate and apply emissive material (e.g., 4000K, reduced emissive multiplier)
13. **PPV Color Grading**: Convolution Bloom; Chromatic Aberration (slight); Shadow Contrast 0.6; reduce shadow saturation; midtone contrast 1.2, gain 0.1; global saturation reduce slightly; temperature ≈ 7000K for slightly warm look
14. **Fix Lumen flickering/noise**:
    - Console: `r.Lumen.Radiosity.ProbeOcclusion` → visualize probe pattern
    - Console: `r.Lumen.Radiosity.HemisphereProbeResolution 32` (default 4; increasing to 32 drastically reduces flickering)
    - PPV → Global Illumination → Lumen: increase **Final Gather Quality** and **Lumen Scene Lighting Quality**
15. **Lumen Reflections (PPV)**:
    - Enable **High Quality Translucent Zero Reflections** (correct reflections in translucent meshes like glass)
    - Debug: Lumen → **Dedicated Reflection Rays** visualization (red = RT-calculated; increase Max Roughness to Trace for more surfaces)
    - Max Reflection Bounces: increase to 2+ for scenes with mirrors/chrome surfaces
16. **Volumetric Fog quality console variables** (for rendering, not realtime):
    - `r.VolumetricFog.GridPixelSize 4` (default 8; lower = better quality but heavier; 3 is a good balance)
    - `r.VolumetricFog.GridSizeZ 512` (default 128; increase to 512-1024 for rendering; adds volumetric shadowing depth)
    - Reset to default (8 / 128) for real-time/game use

### UE Systems / Blueprints / Settings
- **Mega Lights** — experimental lighting system in UE5; provides ray-traced soft shadows automatically; uses fewer shadow map artifacts than Virtual Shadow Maps for sub-meshes; enable in Project Settings
- **Hardware Ray Tracing** — Project Settings → Rendering; replaces Signed Distance Field approach; required for accurate interior lighting and reflections; requires DX12 + compatible GPU
- **High Precision Normals (G-Buffer Format)** — reduces banding artifacts in normal-dependent lighting (Lumen GI, specular)
- **Source Radius** — size of the physical light source; larger = softer contact shadows; visible as yellow sphere in editor; large values cause distracting specular highlights
- **Soft Source Radius** — diffuses the specular highlight from a large Source Radius without affecting shadow softness; fix for over-bright specular from area lights
- **Black Only material** — engine content material that renders fully black (opaque, no light pass); used as light blocker mesh to shape spotlight beams
- **Cast Volumetric Shadow / Cosine Volumetric Shadow** — per-light option to cast fog/volumetric shadows; essential for shaping god-ray beams through mesh occluders
- **`r.Lumen.Radiosity.HemisphereProbeResolution`** — console variable; default 4; increase to 16-32 to dramatically reduce Lumen radiosity probe flickering; significant quality improvement for interiors
- **`r.VolumetricFog.GridPixelSize`** — console variable; default 8 (screen-pixel size of each fog voxel); lower = more precise fog/shadow at cost of performance; 4 for quality render, 8 for game
- **`r.VolumetricFog.GridSizeZ`** — console variable; default 128 (vertical fog grid resolution); increase to 512-1024 for better fog depth and volumetric shadow detail in renders
- **High Quality Translucent Zero Reflections** — PPV → Global Illumination → Lumen Reflections; enables Lumen RT in translucent/glass materials instead of sky-capture fallback; large visual improvement on glass/water

**Typical 4-actor interior base:**
| Actor | Purpose |
|-------|---------|
| Sky Sphere + Skylight | Ambient light/color from exterior |
| Spotlight | Exterior key beam (shaped with blockers) |
| Point Lights (2+) | Warm practical fill / emissive sources |
| Post Process Volume | Tone map + Lumen settings + color grade |

### Difficulty
Intermediate-Advanced. Project settings configuration requires understanding of ray tracing pipeline. Lumen console variables and source radius vs soft source radius distinctions are non-obvious. Light blocking with black-material meshes requires spatial thinking.

### UE Version
UE5 (Mega Lights, Lumen Hardware RT, High Precision G-Buffer — UE5.x features; Mega Lights is experimental as of UE5.4)

### Tags
lighting, interior, lumen, fog, ray-tracing, reflections, tone-mapping, color-grading, performance, workflow

---

## Related Entries
- `if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this.md` — same Karim Yasser; companion exterior PBL tutorial; EV100 curve and global lighting setup
- `realistic-and-physical-lighting-in-ue5-what-is-pbl.md` — PBL theory (units, EV100); foundational to this workflow
- `realistic-and-physical-lighting-in-ue5-the-pbl-workflow.md` — PBL workflow (HDR Viewmode meters, lighting studies)
- `things-to-know-about-lumen-unreal-engine-5.md` — Lumen GI deep dive (surface cache, hardware RT, quality settings)
- `the-perfect-sky-light-in-unreal-engine-5.md` — Skylight settings and configuration
