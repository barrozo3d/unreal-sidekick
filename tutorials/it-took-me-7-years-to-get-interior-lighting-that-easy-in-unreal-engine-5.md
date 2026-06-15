---
title: It Took Me 7+ Years To Get Interior Lighting That Easy in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=MJQ-0tmIhQk
author: Karim Yasser
ingested: 2026-06-15
ue_version: "[PENDING]"
tags: []
extraction_status: pending
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
**Transcript:** So to start with interior lighting, we need to adjust first our project settings.  So we can go here in Edit, Project Settings, and scroll down for Rendering.  And we need to use bunch of options actually for Lumin and Red Tracing  and to give our scene these kind of soft shadows in it.  So let's scroll down.  We need first to ensure that we have dynamic global eliminations at the Lumin.  Same goes for reflections.  And here in the support hardware ray tracing, this need to be enabled.  And this one as well, ensure it's enabled.  Use hardware ray tracing when available.  And regarding ray lighting mode, we can adjust it later in our process volume  and test out different settings in it.  Also, we don't need to use generate mesh distance fields as we are going to depend on hardware  ray tracing. Scroll down here. I need to ensure local exposure, highlight contrast and shadow  contrast are set to 1. I just like to have it as default on 1.  And here in the G buffer format, set it to high precision normals.  And if you want to use mega lights, it's fine to turn it on.  I want to keep it on actually because mega lights will give me this kind of soft shadows as well  because it uses grea...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_001.jpg

### Lighting Cleanup - Remove Baked Lighting [2:20]
**Transcript:** So let's first of all ensure we don't have any light in here. Remove all of them.  All of these light actors.  And let's ensure we don't have any reflection actors as well.  Sponential height fog, post-process volume. All of these actors needs to be deleted.  And for our sky, for me it's fine to give it as it is for now as we are going to use it.  Maybe we can try different texture or just hide it with the fog or so.  So for now this is our scene, it's completely black but we would need to ensure it doesn't have  any pre-computer lighting. So I can go to Window, World Settings, and here in Lightmass,  up in this option, reset all of these settings, go to Advanced, and here we can see Light Maps.  They are added already. So let's head for Snowpreet commuted lighting. It's okay.  And here if it doesn't work, select build all levels. And just like that, Light Maps will be zero.  And if it's not updating, you can restart the level directly and it will work.  So now we have our scene ready, it's clean, it doesn't have any big lighting, and all good to go.  So what we will need to do first, in my opinion I need to disable all of these  emissives first of all. So I can go here, set the em...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_002.jpg

### Skylight Setup [4:52]
**Transcript:** let's see if we can control the tent. Yeah, we can. Let's control our tent. I want to have  somehow a night lighting, moody, very soft. So let's try to have it like that. Maybe around  0.5 0.6. It's fine. Save. And for the massive, give me that one. And let's add a folder for lighting.  There is lights, let's call it lighting. Right click on it, make current folders. So anything we  add in here will be dropped automatically to this lighting folder. So I'm adding a boss process  volume, scroll down, enabling infinite extent. So it affects all my environment without the need  to rescale it. Go here in exposure. I'll just go with the very basic exposure, set it to one and  one and start working from this base, also setting exposure compensation on zero. So I can now  select my sky, make it a little bit brighter, you're around 5, probably. And I will need to move  this sphere to our lighting folder and add a skylight. So I can start getting more ambient lighting  in there. And in my opinion, it's very blue currently. So I can go in my sphere and reduce the  saturation of my sky. Go here in the tent and reduce the saturation to going to probably or  2.25. Go back to the skylight and hit...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_003.jpg

### Tone Mapping [7:23]
**Transcript:** turn map our scene without the need to add a lot of lights in there. So let's go to local exposure.  Let's try to set this one to 0.6. And let's keep the highlight contrast as it is. Maybe here for  the two, let's reduce it a little bit. And we can see more details in here already without the  need to add a lot of lights. And let's actually try to add our fog volume, reset the location of it.

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_004.jpg

### Fog & Atmospherics [7:54]
**Transcript:** And let's give it a color. Something probably. Just give it one one. Let's try color.  Maybe like that. I just want to give it this color or cyan color. Like it's very saturated actually.  So I'm just trying a new color in here. It's not like blue or very blue night. It's enabled for  the metric fog. And actually it's too bright outside. So I can use the value of it to make it  better. Yeah, like that. And if I try to hide the sky sphere, it might be really looking better,  but our skylight will not be working good. So we need to keep it actually. So let's keep our fog  like that. And let's try to add a spotlight. So it's more like outside or exterior lighting.  Let's give it like this. Let's disable this nabbing. And here let's try to make this 100 maybe a thousand.  That it's right actually to go very crazy number like 10,000. So good color. Let's get the same  hue from here. It's the 94. And almost 2.7. It would be good. Let's try to make the cone smaller.  That. And let's try to add very strong volumetric scattering, but you'll see why I'm doing this now.  Let's get back to the another view board. Switch it to on left. And I can right click on this light.  Go to pilot. And I ca...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_005.jpg

### Fix Ray Tracing Shadows [12:11]
**Transcript:** will work much better. Cosratorate shadows doesn't work perfectly with submeshes, especially like translucent  meshes or so. So we can try it like this. And let's try to increase the attenuation radius a little  bit. Try 1500. This is too much actually my opinion. Back intensity, but I can reduce it like 5000  or try 2000. Yeah, maybe 2000 is good. And this increases the volumetric scattering to 100 probably.  As you can see now it's very soft. Like it's already much better. And if I try to increase the  outer context just increases the intensity here. So I can try 40. And so it could be adding more  intense light as the fall of is going to be sharper. So it's stick to 20 could be good. And here for  this light it's very very sharp currently as you can see. These shadows are too sharp. So we can  increase the source radius like that. And the source radius basically increases the size of the  light itself. So as you can see this yellow sphere is the source radius. And the bigger it becomes  the softer the shadow will be. Let's actually try to add another  I just need to plug my light in that better way. So this should be better actually.  So let's try here to increase the source rad...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_006.jpg

### Soft Shadow & Specular Fix [14:16]
**Transcript:** or actually before fixing it. If we try to see it from a chrome bowl let's apply a chrome  material to it. We try to see it from here. As you can see there is a big big sphere from our  light source. So in order to fix it there is two ways. You can go down here and reduce the  specular scale. But that will make you lose your specular reflections on your meshes.  Or you can increase this one soft source radius. Increasing it will make it softer. So it will  be more diffused and much better. So we can get back here. And as you can see the soft source radius  is already making it much much better softer. And it does make more sense actually as light source.  So let's reduce this light source a little bit. So as you can see now it's very soft like that.  Maybe the fog is too thick and we will reduce it. And the soft source radius could be reduced as well.  Maybe 200 could be good. So now our light is very very soft actually and it's not eliminating

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_007.jpg

### Adding Lights & Polishing [15:36]
**Transcript:** everything in the scene like that. It's not very good. I'm just limiting it to this specific  place. So it's feeding out and it looks much better. And if we try to make it like that could be  even better. Like this. So it's even softer. You can try a lot of things in here actually.  But let's stick to it like this. You might notice there is some noise still in here. This is  related to Lumin and yeah same goes here. So we will need to fix it for sure. But I think the  intensity is too much for now. Let's reduce the intensity a little bit. Maybe it's still too intense.  I think 1000 could be good. Yeah, let's give it 1000 but reduce the volumetric scattering.  Let's try 80 could be good or actually let's give it on thread.  Yeah, 100 could be good. Yeah, 100 is good. And here for indirect light intensity if we try it  more. Because you can see it adds even more to your eye in there. Let's stick to two or three  could in our case. And here's still I want to add more lighting actually to fill in these very  dark shadows. So I can use other point lights probably. Let's add one here.  And it's very very sharp right now. So we need to fix it. As you can see this very sharp  doesn't work ...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_008.jpg

### Post Process Color Grading [21:44]
**Transcript:** adding more effects in there. So we can use convolution bloom if you want to have  a different shape of the bloom like that.  But as you can see, this is not very good. This is too much. And it's not working as expected.  So let's reduce it. We can just keep it on one or two. Maybe.  Two could be good. One. Maybe 1.5. And for chromatic aberration,  we need slightly more chromatic aberration.  Still a wind one. Look at exposure. We can adjust the shadow contrast now. Instead of the  0.6, we can have a light layer number like that. Same goes for highlight contrast if we want  to reduce it. So it affects our exterior lighting like that. But I like it. I actually  just give it as it is. Or if you wanted to increase it to have more contrast in there.  For detailed strength, I like to increase it. Maybe 1.2. But that will affect our highlights.  So we need to get back to our bloom and reduce it. One.  And major effects. Let's add some more sharpen and slightly. That in color grading,  I like to reduce the shadow saturation. Let's try to wind 4.5. And in the gain.  Maybe I can give it a little bit of finish or close attempt.  But this is too much actually. Maybe increase it.  So it's the ...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_009.jpg

### Fix Lumen Noise [25:18]
**Transcript:** So this is already the best version of looming that it is possible. You might notice this kind of  flickering in here and in there as well. So we will need to use this console command.  R.looming.c.in.radiosity.visualized.prox.  As you can see now, this is how the Omin is trying to work. So that's why it's  flickering a lot. We can fix that by using R.looming.c.in.radiosity.emisphere from resolution.  And the default value of it currently is 4. So let's try 32. So it's already much better.  So this is 4. As you can see it's very, very fast and it's trying to update very fast way.  This is slightly better now. So we can try to use that to fix this problem. Let's get back to zero.  And here we can increase the lumensine lighting quality and lumensine data. Let's say post 4.  And this affects our lumensine view. We can go here in lumensine and see it probably.  As we can see now, our process volume, we try to set this one to the lowest possible.  Like a lot of objects are already removed from the renderer of the domain.  So increasing it will make it better. And here in final gather quality, let's try to increase it for.  And in advanced settings, if you wanted to use lumensine to red...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_010.jpg

### Improve Volumetric Fog Sampling [30:03]
**Transcript:** how you think about it if you have a light source or a big opening like that and how you can  use effects, your shadows make it softer and get even better lighting. And we have still one  thing left. We can see here in the volumetric fog, it could be even better. So we could try  our dot volumetric fog. Let's try grid pixel size. Divoled value is eight. And if you are going  lower you will basically get better fog. But be careful with it because it could draw  when you were to be performance and it might crash. So I'm trying to go to four.  As you can see now four is even softer and much, much better. This is eight. It's not looking good.  This is 16 if you want to get bad. This is four. This is one. As you can see one is very, very soft  because it's casting the volumetric shadowing actually from these meshes. So that's why it's  looking very soft and good. Let's give it to three. It could be good in this case. And there is  another one actually which is a red size z. It's default value is 128 and you can go higher.  So let's try 512. See how it looks. This is 512 and this is 128. This is 32. 32 as you can see  it's really, really bad. So you'll need to increase it. 12 could be go...

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_011.jpg

### Quick Note [32:41]
**Transcript:** Render lighting. I hope you enjoyed it. And don't forget to join our discord community if you  want to get more tips and learn more about lighting, the environment, characters, anything related  to game art. Feel free to join our discord community and stay in touch with other talented people  so that's it for today's video. See you next time.

**Frame:** tutorials\frames\it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5\frame_012.jpg


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
