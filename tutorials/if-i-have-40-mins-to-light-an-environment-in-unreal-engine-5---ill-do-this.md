---
title: If I Have 40 Mins to Light an Environment in Unreal Engine 5 - I’ll Do This
source: YouTube
url: https://www.youtube.com/watch?v=64JnVJBgoos
author: Karim Yasser
ingested: 2026-06-17
ue_version: "5.x"
tags: [lighting, physically-based-lighting, pbl, directional-light, sky-light, exponential-height-fog, volumetric-fog, post-process, color-grading, lumen, tone-mapping, exposure, ev100, local-exposure, environment, game-ready, ue5]
extraction_status: complete
frames_dir: tutorials/frames/if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this/
frame_count: 19
---

# If I Have 40 Mins to Light an Environment in Unreal Engine 5 - I’ll Do This

**Source:** [YouTube](https://www.youtube.com/watch?v=64JnVJBgoos)
**Author:** Karim Yasser
**Duration:** 42m28s | 19 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In today's video, we are going to go in a step by step,  relight this scene using physically based lighting  and make it game-ready.  By understanding the concept of a V100,  luminance versus illuminance, contrast ratios,  proper setup for directional lights,  with custom skybox materials,  and then understand the tone map,  color grading to finally get this scene  with just global lighting actors.

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_000.jpg

### Physically Based Lighting [0:23]
**Transcript:** So physically based lighting,  it's a workflow or approach  in which you use real world values,  making your scenes looks consistently better.  So you are not guessing what are your lighting values are.  Simply you are following these rules as a reference,  and then you can break these rules as an artist.

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_001.jpg

### Luminance vs Illuminance [0:44]
**Transcript:** And in order to measure these values,  we have two different terms,  luminance and illuminance.  Each one of them describes different type of lighting.  Like for example, for luminance.  If we are talking about luminance,  this would be the amount of light that is projected  or emitted from the light source itself.  And usually for the measurement,  it's measured using candle labber meter square,  which is candleless in underid engine,  and it's usually the default values  for your lighting unit.  But on the other side,  illuminance would describe then the amount of light  that is pulling onto a specific surface.  So it's usually not the same amount of luminance  because when you have a very bright light source,  it doesn't mean that it will spread  or emit all these light photons on the same surface area.  Like for example, for point lights,  there's spread the light or in metal light  everywhere around it.  It's not specified for a specific angle.  So it's kind of different from the luminance.  And the illuminance is measured by lux.  And lux means lumens bare meter square,  which is usually defined in Unreal for directional lights.  And why we are using lux for directional light...

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_002.jpg

### Scene Clean Up [3:28]
**Transcript:** So let's get started here in this scene.  This is a free sample provided by Epic Games.  So you can use it on your own or use any other scene as you want.  First, all we need to remove any lighting data.  It's better to start with a blank scene.  And here I mean that it's not having any lights  except if you are going to improve the existing light.  But for this example, I'm going to remove any light actor,  all of them from here.  And to ensure we can search for any light here,  see and set up this move, all of that.  And let's scroll down to ensure we don't have any other  existing lights.  And also, let's ensure that we don't have sky  or boss process volumes or any reflection capture actors.  So here, let's see if there is any boss process volume.  And for reflection, we have another reflection actor.  So it should be all good now.  And for an extra step of ensuring that our lighting is working well,  we can go to Window and then World Settings  to ensure that we don't have any light maps here.  And if you have, you can go here and force  no pre-computer lighting and then go to Build  and Head Build lighting only.  This will remove all your baked lighting data in your scene.  S...

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_003.jpg

### PBL Sky Material & Sky Light [5:39]
**Transcript:** And now we need to hide our directional light  because we will add our skydume,  which is the primary object that will add our mode  and attention for the player.  So in order to create a sky that is more closely  going to be like a golden hour or so,  I'm using here a back-old skyse LA from FAP.  And let's scroll down and use this skyse fear.  Usually for skyse fears, it's inversed, normal smash  because you see the sky from inside, not from the outside.  So instead of creating your material as a two-sided material,  you can simply use an inversed skyseer.  So we are adding it here.  Now we can see it in on-lit view.  It's reset the position for the location.  And for the scale, I'm going to sit it to 15,000.  You can go bigger if you want.  But the thing is, the skylight threshold  is going to be very large.  And making the skyse fear bigger than the threshold,  it will make the skylight works better  without any black reflections spotted.  So your skylight will perform much better.  And here for the material, let's choose a material like,  maybe like this one, and assign it here.  And now we can see our material.  For sure, it's not completely like golden hour,  but it's basical...

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_004.jpg

### EV100 - Exposure Curve for Interiors & Exteriors [9:58]
**Transcript:** Sposure could be a bit tricky for a lot of people.  And you might not know which is a proper value for exposure  commutation, for your minimum and maximum EV 100.  And what does actually EV 100 means?  So basically exposure is like equation.  You are using different or multiple factors that are added  in a specific equation.  And then you can get your brightness.  It's calculated then with this measure.  So for manual exposure, you can find F-stop or aperture.  You can find the shutter speed, the ISO, et cetera.  But for auto exposure, it's not using all of these values.  So to go over it, let's add a post process volume.  Go down here, enable infinite extent unbound.  So our post process volume is covering the entire space.  We don't need to rescale it to a very big volume.  Then get back to exposure.  Here to start, it's better to set the exposure  commutation to zero.  And if we try to go inside, actually,  it will start to be brighter and inside.  That's the auto exposure adaptation, our eye adaptation,  which is currently happening now in this histogram.  As you can see now, exposure is trying to go lower  in this value.  So it's usually brighter.  And if you get out, it's goi...

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_005.jpg

### Contrast Ratio [18:51]
**Transcript:** And let's then adjust our contrast ratio.  And what actually that mean is that difference between  even 100 values in light versus in challenge.  And this could be a very good metric.  It's always ratio to start with to light your scenes in an easier way.  And for golden hour sunrise or sunset,  usually the contrast ratio is not too big around 2 to 1 in difference.  If we are looking at light side.  If the heavy 100 is 2, then on the shadow side should be around 0.  We can measure it by using cube.  And assign a gray material.  Basically, this is 18% white.  And this is the proper value for middle gray.  It's not 0.5 because exposure is not linear.  It's look at it makes so it's not working as.  The half between 0 and 1 is 0.5.  Now it's not like that.  It's not linear.  You can look for other references for it.  But basically it's not taking an average.  Between the 0 and 100 it's taking the geometric mean,  which is the square root of the average values.  So let's get back now to the HDRI adaptation.  As we can see now it's almost the same because we only have skylight.  So we can start adding a lot of directional light.  And for the directional light, usually for low sun is usua...

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_006.jpg

### PBL Directional Light (Sun Light) [21:00]
**Transcript:** Let's add it like this and use the control L shortcut to position our sun in a proper way.  Let's try to have it like this.  Basically most of the environment would be in shadow.  Just totally fine.  And now for the color.  If you want a specific color, basically it's around 2000 maybe temperature.  But if we started with it as a base, it would be 200 to.  Orangey color.  Let's try to keep it as 3000 or if you don't want to use the bridge or you can use the color.  Have a specific color but be careful with that because it might not be very accurate as temperature especially for natural lights.

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_007.jpg

### Hard Shadow vs Soft Shadow [21:59]
**Transcript:** Then for source angle.  Let's try higher number like 5.  So it's softer in shadows.  Usually you don't go like 25 or 15.  It might be good for some situations for cinematics maybe.  So let's try 405 as a start.

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_008.jpg

### Tone Mapping & Local Exposure [22:16]
**Transcript:** But for now I still see shadowed area is still too dark.  So it comes then to tone mapping.  And we don't see that very harsh contrast between light and shadow.  And for player visibility to ensure better player experience as well.  It's better to have more bright shadows usually in games.  You will see shadows are brighter.  And you don't need to add a lot of fill lights like can go here and add a point light like this.  Freeze the intensity.  Even higher.  Make it higher like that.  To add a lot of fill lights.  This is not a proper workflow.  We are trying here to make everything with just global lights.  For tone mapping.  It's in post process volume.  Can go down in local exposure.  There is shadow contrast and highlight contrast.  Let's start with shadow contrast.  Usually this value Epic Games doesn't recommend to go lower than 0.6.  So start with 0.6 as a piece.  See this is quite drastically big difference between four and after.  For sure it still looks a bit flat and not a lot of areas.  But if you are looking at it like that, our sunlight is not very harsh usually.  Just like the golden hour and the shadows are not too dark.  Let's start with 0.6 like that.  And for hig...

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_009.jpg

### PBL Exponential & Volumetric Fog [25:52]
**Transcript:** Let's first start with the exponential height fog.  And to add it here, it might not work as before,  because we are using physically based values here as a start.  So even if you try to make it white like this, you might not notice it.  Except if you are going to make it brighter like 100, for example.  I want to make it a bit thick fog.  Let's make it like 200.  Or actually, it's keep the 100 and increase the fog density to 0.04.  Let's give it a little bit of color.  Actually, if we try to make it very orangey like this could work.  Or if we can go to the other side of making it very lowish.  Maybe let's try 220 and here and around 0.06 in saturation.  It's good work, but if you want to try the other side of it to make it more like this,  for example, this could be good as well in other cases.  So I prefer to start with a bit of lowish light like the sky.  And then we need to enable for sure the volumetric fog.  Because it's a potential high fog only and it's on it's making it very flat.  And in interest, you will see very bad lighting for sure.  So let's give it like that with volumetric fog.  And then we can increase extinction scale.  And then we can change the color of view ...

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_010.jpg

### Sun Disc in Sky Material [28:07]
**Transcript:** Just like this.  And we also need to add a sun disk to our material.  And we can save all of that.  And let's basically add this material.  So here's quickly the sun disk material that you can use and add to your shader.  So if we get back and open our material in instance, we can now see the sun disk.  There is some brightness.  Let's make it very high like this.  As you can see now, our sun disk is added to our material.  And the radius of it, let's make it smaller, maybe even smaller.  We like that.  And right this should be higher.  And for the color, I want to make it very orangey or with reddish like that.  Same goes for the sun glow.  So I will copy it and paste it here.  And for the softness of it, as you can see, you can control softness.  Skip it as it is.  You can control the radius of the glow.  So now we have our sun disk.  You can quickly add it to your material like that.  So for exponential height fog, if we scroll down, you can see now scattering distribution is looking much, much better.  Because we can actually see a sun disk added in here with the sky.  If you try to rotate this one, the directional light will stay the same.  Because it separates from the sky sp...

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_011.jpg

### Color Grading in Post Process [30:36]
**Transcript:** Let's go down here.  We can adjust the richer to make it cooler or warmer as you want.  You can adjust the tent.  I usually prefer to start with shadows, midtones, highlights, and then get back to global settings.  So to start with shadows, I prefer to reduce the saturation of it.  Try 0.07.  So it's not very saturated in colors.  And then we can control the gamma.  So we can add a color for it.  Let's try for example something a little bit loose like that.  It's very subtle, but it's adding a lot to the scene.  For midtones, let's try to increase the contrast.  1.05.  Just like that.  And for the gain, we can increase the gain just by 10%.  For highlights, you can control your highlights from here.  You can add more contrast.  This will be visible in these surfaces, as you can see.  You can keep it as it is for one.  Same goes for gain and contrast.  And then let's get back to global control.  Let's reduce the saturation a little bit.  And for contrast, we can try different things.  But actually, I prefer to keep it as default and maybe increase the amount of contrast.  Just slightly.  So this is a set by 7%.

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_012.jpg

### Final Exposure Settings [32:17]
**Transcript:** But now this is very global setup.  And it doesn't work for interiors.  So let's get back to exposure.  We can use the exposure compensation curve.  Get back to it.  Enable the HDRI adaptation.  Disable these two.  So now it's around 4.2.  Let's say four should be brighter.  But minus 2.5.  So we are not losing highlights.  And here this is around seven.  Let's add another point for seven.  This could be better.  So we are not losing a lot of contrast in here.  So basically seven is around zero.  And now we need to adjust the shadow area.  So let's just go for interior.  Here this is around minus 4.8.  Let's give this one.  Around minus three.  Just like that.  And you can control the curve from here.  Let's give it that it is.  This one.  Let's make it look like this.  Let's give it that it is.  This one.  Let's make it a bit brighter.  So it's brighter outside.  Just like that.  So even if we are in shadows,  we can still see the lighting in a good way.  Just like that.  So now our shadows look good.  In interior looks good as well.  We don't need to add a lot of boss versus volumes.  And remember this is a base lighting,  a global lighting.  And here in.  Even in very bright are...

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_013.jpg

### Better Directional Light [34:45]
**Transcript:** use the light shaft.  Acneusion.  So it's working better.  Let's try to keep it around 0.5.

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_014.jpg

### Fake Cloud Shadow Gobo Light Function [34:53]
**Transcript:** And let's even add a global light for our directional light.  I'm using this material.  This is basically.  light function material to add a fake shadow. So our shadows doesn't look very very  flat. So let's try to make it like this.  So we are clothing this one and we are just giving light in specific areas  and it's looking even softer.  We can even adjust the location of our sun. So it corresponds to the material  and if we get back even in here, let's try 2000. It might seem a bit too bright in a lot of  equations but this looks very good actually. But if we wanted to use 2000 and our lighting looks  very bright, we can reduce the highlight contrast in our local exposure settings. But let's  give it as it is for now and then go in our skylight. We can increase it a little bit.

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_015.jpg

### Better Sky Light [35:58]
**Transcript:** Now we can break the rules of the PPL because we are artists and we need to create good looking  scenes. So let's try to make this one a bit loose. Just 20% saturation and maybe let's make  the intensity to instead of one. Can you still see it's looking? It might be a bit dark in some  cases but later you cannot adjust the post process volume. As you can see, this looks very very  cinematic. This very soft light that's coming from directional light and it's going or added on  objects like that. Can make it even try to make it even higher. Can try 1500. Let's give it  a thousand and if it's softer in angle, it will not be very good actually. So let's give it  five as it is. The four-volumetric scattering intensity, you want more fog, but I don't  admit it actually. It's too much fog like that. So now in post process volume, we can do

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_016.jpg

### Better Post Process, Lumen Settings, Film Grain, Bloom [37:18]
**Transcript:** final touches to make our scene looks even better and more playable. For final,  Lumen settings, which we explained before in details for our community, feel free to check  the link down below if you want to join us. We discussed in depth the different  pre-lighting modes and how actually Lumen works. It was under the hot experiment to know more about  Lumen and fix all the flickering issues and everything that might look very bad or very weird to  control with Lumen. So first of all, for game lighting, it's better to keep it for surface cash  but if you want much better results, for sure, you can use at lighting. But let's keep it surface  cash. And as you can see, also at the background, foliage is much better with that lighting.  Keep it at surface cash. Every other option, keep it to default. And here you can see the  few-sculler boost. If we wanted to check that, we can go to Lumen. Lumen scene. And let's try to  sit to four. It's much, much brighter now. And actually what it does is it makes the base color  maps brighter so it contributes more to the indirect lighting. This is a quick fix if you don't  need to fix your materials, but it's not really recommended to go very hig...

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_017.jpg

### Outro & Final Note [41:50]
**Transcript:** the global lighting. This could be as a base for your game, for your scene. And then you can add  later on other light actors for more polishing levels. So that's it for our today's video. I hope  you liked it. And if you want to learn more about lighting and other topics that you might be  struggling with, feel free to join our community and ask for your customized learning path. So we  can craft it for you. Thank you so much for watching. See you next time.

**Frame:** tutorials\frames\if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this\frame_018.jpg


---

## Structured Notes

### Core Technique
Physically-based lighting (PBL) full re-light using only global actors — Directional Light, Sky Light, Exponential Height Fog + Volumetric Fog, and Post Process Volume (EV100 curve, Local Exposure, Color Grading, Lumen). No fill lights.

### Summary
Karim Yasser walks through a complete PBL lighting workflow for a game-ready UE5 environment using only global lighting actors (no fill lights). Covers the theory of luminance vs illuminance, EV100 exposure curves for interior/exterior transitions, contrast ratio measurement with an 18% gray proxy cube, sky dome setup from FAB with inverted normals and sun disk material, Sky Light threshold sizing, Directional Light golden-hour setup (Ctrl+L, 2000–3000K color temperature, source angle), Local Exposure shadow/highlight contrast, Exponential Height Fog with Volumetric Fog, fake cloud gobo via Light Function material, color grading per shadow/midtone/highlight channel, and Lumen Surface Cache tuning with albedo boost. Intended as a base global lighting layer before adding local fill/accent lights.

### Key Steps
1. **Scene prep**: remove all light actors, sky sphere, post process volumes, reflection captures via Outliner search; World Settings → Force No Pre-computed Lighting → Build → Build Lighting Only (clears baked data)
2. **Sky dome**: add inverted-normals sky sphere mesh from FAB, scale to 15,000+ (must exceed Sky Light capture threshold); assign sky dome material instance
3. **Sky Light**: add Sky Light actor; real-time capture; intensity ~1; ensure sky sphere scale > Sky Light threshold to avoid black reflections
4. **Post Process Volume**: enable Infinite Extent Unbound; go to Exposure → set Exposure Compensation Bias to 0; enable HDRI Adaptation (auto exposure via histogram)
5. **EV100 curve**: add Exposure Compensation Curve; set exterior EV100 (~4), interior shadow EV100 (~-3 to -4.8) to smooth interior/exterior transition without losing highlights
6. **Directional Light**: Ctrl+L to drag sun angle; Color Temperature 2000–3000K (golden hour orange); Source Angle 4–5° for soft virtual shadows
7. **Local Exposure**: Post Process → Local Exposure → Shadow Contrast 0.6 (Epic minimum), Highlight Contrast as needed; avoids need for fill lights in shadow areas
8. **Exponential Height Fog**: Fog Density 0.04–0.06; slight warm/cool tint; enable Volumetric Fog; adjust Extinction Scale; Scattering Distribution improved by adding sun disk to sky material
9. **Sun disk material**: open sky dome material instance; add Sun Disk + Sun Glow nodes; adjust radius (small), color (orange/red), softness; sync with Directional Light rotation
10. **Cloud gobo**: assign Light Function Material (cloud shadow pattern) to Directional Light → Light → Light Function → light breaks up flat shadow cast
11. **Color grading**: Post Process → Color Grading; Shadows: saturation ~0.07, add subtle blue/teal offset; Midtones: contrast 1.05, gain +10%; Global: -5–10% saturation, +7% contrast
12. **Lumen**: keep Global Illumination = Lumen, Surface Cache (hardware RT for higher quality); albedo boost 2–4 in Lumen scene view if indirect lighting too dark; Film Grain + Bloom final polish

### UE Systems / Blueprints / Settings
- **Directional Light** — Ctrl+L shortcut (drag sun), Temperature (K), Source Angle (shadow softness), Light Function Material (cloud gobo), Light Shaft Occlusion (0.5)
- **Sky Light** — Real-Time Capture, Intensity, scale threshold must exceed sky sphere scale
- **Exponential Height Fog** — Fog Density, Volumetric Fog checkbox, Extinction Scale, Scattering Distribution, Albedo color tint
- **Post Process Volume** — Infinite Extent Unbound, EV100 / Exposure Compensation Curve, Auto Exposure (HDRI), Local Exposure (Shadow Contrast min 0.6 / Highlight Contrast), Color Grading (Shadows/Midtones/Highlights/Global channels), Bloom, Film Grain
- **Lumen** — Surface Cache mode (faster/game-ready), Hardware RT (quality), Albedo Boost (Scene View Mode → Lumen Scene for tuning)
- **World Settings** — Force No Pre-computed Lighting + Build Lighting to clear baked data

### Difficulty
Intermediate

### UE Version
UE5 (FAB integration; Lumen Surface Cache = UE5.0+)

### Tags
lighting, physically-based-lighting, pbl, directional-light, sky-light, exponential-height-fog, volumetric-fog, post-process, color-grading, lumen, tone-mapping, exposure, ev100, local-exposure, environment, game-ready, ue5

---

## Related Entries
- Rendering docs (Lumen, Volumetric Fog, Post Process)
- Boundless Entertainment lighting tutorials (Dune look, cinematic lighting secrets)
- Dean Yurke volumetric fog tutorial
