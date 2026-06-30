---
title: The Perfect Sky Light in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=mKZUlyM9oZQ
author: Karim Yasser
ingested: 2026-06-23
ue_version: "UE5"
tags: [lighting, skylight, hdri, ambient, reflections, workflow, technique, pbl, performance, debugging]
extraction_status: complete
frames_dir: tutorials/frames/the-perfect-sky-light-in-unreal-engine-5/
frame_count: 15
---

# The Perfect Sky Light in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=mKZUlyM9oZQ)
**Author:** Karim Yasser
**Duration:** 16m21s | 15 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Skylight might be your downside in your lighting setup.  And in today's video, we are going to see different approaches in the skylight  and know the pros and cons of each one and how to deal with it.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_000.jpg

### Physically Based Lighting Live [0:12]
**Transcript:** So to start here, actually in this scene, this has been done in a free life session before  in our community and you can get the full record of it by just joining the community and ask for it.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_001.jpg

### How Sky Light Works? [0:24]
**Transcript:** So first of all, what actually skylight is?  Basically, to understand the skylight even more, we need to first start with a chrome ball.  So I'm going to create a sphere here and assign a chrome pole material on it.  Because we will need to see the reflections as basically the skylight is our reflections  and that adds the ambient lighting of our scene.  And if I tried here to hide all of my lighting actors,  including the directional light, the fog, the post process, the mesh or the sky mesh,  we can see now a completely black scene, which is kind of expected actually.  Because now the skylight is trying to capture something that is not existing in our scene  because it's using an option called real-time capture.  But to understand it more, actually, basically the skylight takes whatever around it,  captures the data from it, even if it's colors, intensity or brightness,  and then reproject this data in the environment.  So that's how you get this ambient lighting effect.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_002.jpg

### Cubemap Skylight [1:33]
**Transcript:** And actually, if I don't have this real-time capture, which we will go into later,  and I have a different type of capturing by using this option, it's called source type.  So source type basically, it's using even the sky or anything around it in the environment,  or it's using a specific texture that is assigned to it on its own.  So it doesn't depend on the environment.  So if I change this one, this source type, and selected any texture cube here,  get back to the lit view, I now can see some light here, but I need to change the intensity.  Let's try something like a hundred.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_003.jpg

### Fix Lumen Reflections [2:09]
**Transcript:** So now hundred, I can see some reflections, but it's not working correctly,  because I'm using low-men reflections and ray tracing reflections.  So I need to go in my post-process volume, just to ensure that my reflections are working as expected.  I need to turn off low-men reflections and turn off low-men global illumination.  So here it's reflections as you can see now.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_004.jpg

### HDRI Lighting [2:32]
**Transcript:** So that's actually the texture that the sky is capturing.  And if I change it to something else like this, it would be visible on my crumball,  and any other texture it will start to be visible even more.  As you can see here, and if I change the color, it will project the colors of it on the environment,  let's try even higher brightness, it will add more ambient lighting.  So actually this ambient lighting is getting projected from this cube map.  So the source type here defines which method or which way you want the skylight to use  to project this indirect lighting data.  Basically it's better to use the sky around it or the environment,  so that will give you better and more accurate reflections in your environment.  But if you wanted to use a cube map, for example, the best option in my opinion  would be to use a texture that is not having very high-prite spots,  because that will affect your meshes, especially in distance.  You will see weird-prite spots and others will be indoor.  So try to use more overcast textures or neutral textures in general.  So let's try to see if there is any good texture here.  Let's see this one.  Yes, you can see it's quite different.  As I mentioned, as you can see, this one is very, very high,  and if I try to see it from detailed lighting, as you can see, this is very harsh,  and others is not.  So the texture affects your skylighting a lot, and you might not notice it.  If I undo all of these options here, let's try to have a better skylight  and get back to our most processed volume,  ensure that we don't have lumin reflections or lumin G.I.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_005.jpg

### Sky Light Scene Capture [4:21]
**Transcript:** So we can visualize our sky or our reflections in a better way.  So let's keep them off, get back to the skylight, turn off real-time capture,  and now we should see something good.  This is now 500, but 500.  We can see it because we don't have our sky.  But if we have now our sky, and we scroll down here for recapturing,  this will make the skylight read the data again.  Now this is too bright because I have it.  Too high intensity, this is 3.  So now as you can see our lighting or ambient lighting is very soft.  We don't see very sharp shadows, very high spots,  except in some places, which is fine because we can see it in our sky.  But if we use a very high contrast image or texture cube,  this will definitely affect our skylighting.  So here, how we can actually understand it more.  Let's get back to let view, as we can see.  This is now how our sky or reflections work.  This is based on our sky, and it's not actually capturing any details, except the sky.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_006.jpg

### Sky Distance Threshold - Fix Black Sky [5:44]
**Transcript:** And that's related to this option, sky distance, search.  This means that after 150,000 units, I believe it's Unreal Unit, which is centimeter,  the skylight will start to capture the data after this distance.  So it will not capture any data before it.  So that's why the skylight, even if it's placed like here,  it's not capturing any data around it.  But this option could sometimes make our reflections or sky  feels it's not capturing anything or it's totally black.  And that might be because of our sky poke size.  Here in this example, it's set to 15,000, so it's big enough to make the sky capture all the details.  But what if it's around 150?  It's fine for now, but we need to check that by recapturing.  And it's still totally fine.  Let's try 15.  Now the skybox is smaller.  And let's see our skylight.  It's totally black.  Why?  Because the size of the sky,  folks, is not big enough for the sky distance,  searchable.  So here in this case,  I have two options to solve this problem.  Whether to increase the skybox mesh size or to decrease sky distance threshold.  So let's try here to decrease it to 15,000.  Now it works because it's not bigger than the skybox size.  So what if I want to have even more details?  And also, as you can see, you start to notice more details in here.  And even if it's lower, let's try one.  Now it captures all the details around it.  And this will be affected by its location.  So if it's under the ground and here I hit recapture,  now it's capturing everything and even that affected our skylight.  But with real-time capture, it will make it better actually.  And yeah, it will have slight differences in the reflection as you can see.  But it's not starting to capturing from a distance of one.  Let's get back to our skybooks and make it actually bigger.  15,000. So it's way better in capturing the details.  And here in real-time capture, you might use it with the skybooks.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_007.jpg

### Fix Realtime Capture Sky Light Error [8:06]
**Transcript:** And it gives you an error like that.  And your skylight is not working. It's totally black.  What you can do here may be turn off with a skycatcher or just keep it on and start to fix it.  And how to fix it is kind of easy.  You can go to the skybox mesh, open the material,  go to the master material of it.  And here search for is sky.  Turn it on.  And this mesh now will be tagged as a sky.  So the skylight will be able to read it as a sky component.  So it will capture the details from it.  That's why it works now.  Or you can turn it off and depend on recapturing every time you want to have a change in your sky.  So it will update with you.  But for now, real-time capture is good.  And even it's better for performance compared to recapturing.  Because recapturing takes almost 120 milliseconds to calculate.  But real-time capture is not taking that amount of time.  Because it's not doing it every frame or every seconds.  So now we know how to use real-time capture, the source time, the cube map.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_008.jpg

### Cubemap Resolution & Rotation [9:17]
**Transcript:** And here if you are using a cube map, let's change it now for a cube map.  Let's try this one again.  And you can hear in the source cube map angle, you can rotate it.  As if you are rotating your sky doom or sky books.  So you can do that if you want to have the reflections from a specific side.  Or you have a sky and another cube map.  And you want to match like the highest or the hottest spot in it with the actual sky.  So you can do that from here.  And regarding the cube map resolution, this is a power of two numbers.  So usually good to have it maybe around 256 or 512.  Higher than that doesn't have actually really not small effect or difference.  And even 128 is good for a lot of cases.  But be aware of it because this affects your memory and the GPU.  So let's set it to 512 actually.  And you will see it's more sharp.  And even if we try to get back to SLS capture scene, let's take a look into it here.  This is 128.  It's very blurry.  You can see a lot of details, which is fine because it's just capturing the colors,  the data, the brightness.  So even if it's not very sharp, it's totally fine.  But this will affect the reflections as well if you have any reflective surfaces.  So if I try to increase it to 512, let's try 512,  this will be sharper.  You can see more details in here.  And it's like actually getting better reflections like ray tracing or so.  The intensity scale controls the brightness, how much brightness you want.  And the color if you want to override it with the color.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_009.jpg

### Fix Lower Hemisphere Color [11:03]
**Transcript:** But the most important options here, there is lower hemisphere solid color.  If you unchecked it, notice what will happen to this side of the sphere.  It will capture the sky again.  But that will add more indirect lighting and will make your scene looks flat,  especially for interiors.  So it's not really recommended and a lot of practices to use this option.  So as you can see now, like this has been very, very bright.  It could be good in some cases.  You can keep it on and change the color a little bit.  So let's try to have it at white color.  As you can see, if this is 100, it will be brighter like this.  But let's keep it as default.  And other options are usually fine to keep them as default.  It's not about getting in each option here and changing.  It's the matter of understanding which capturing method you want.  And if you are going to use a cube map, the intensity,  the resolution, the color.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_010.jpg

### PBL Sky [12:03]
**Transcript:** And usually if you are working with physically based lighting,  maybe the intensity scale in a lot of cases, it could be set to one.  So it's taking the actual brightness of the sky.  But increasing it, meaning it's increasing the amount of reflections  and it's like three times brighter.  So it might be good in some cases to have brighter indirect lighting or  ambient lighting overall.  So intensity scale could be a really good option to make your scene looks better.  But don't overdo it and don't make it too dark or don't make it too bright.  It's just a balance here and maybe just slight color or tint to  are directed and make it slightly better.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_011.jpg

### Distance Field AO [12:43]
**Transcript:** And here in the mobility nowadays, we are using movable because it calculates or adds  better distance field ambient occlusion.  But if you are using the looming, this would be calculated automatically.  So you don't need to take care about it or  bear a lot of attention for it to have a good distance field ambient occlusion.  Looming does all the work on its own.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_012.jpg

### Physically Based Lighting [13:05]
**Transcript:** And as I mentioned, they are physically based lighting.  If you want to know more about your setup for the sky, for the directional light,  for the fog, feel free to check this video.  So you have a more inside and deeper look about this setup.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_013.jpg

### Best Practice [13:21]
**Transcript:** So actually, skylights in a lot of cases, they are not taking a lot of  interest, but it could draw in your scene or it could make your scene much, much  better or very bad flat looking scene or it's very bright.  It's very bad with the shadows, where it's the light, all of this stuff.  Or it's very, very dark that you cannot see anything in it.  So skylight is really important and there is no one way to work with it and to  have a specific setup that works for all scenarios.  It really depends on your scene, your sky, the way that you are working with it,  if you are working with BBL setup or just regular setup as you want.  If you are working with a sky like this, if you want to have a cube map,  each one has its own pros and cons, but there is nothing that is one way to go with it or  this is the best option for it.  And this is important to understand how to make your skylights perfect,  how to visualize them, how to debug them.  And here in the detail lighting mode, it's usually good to have your skylights  not too bright compared to the skybooks or vice versa.  So I cannot have my skybooks very, very dark just like this.  This is very, very dark and yeah skylight automatically adjusted to it because I have real time  capture, I have it on 100, this is too bright compared to the skybooks itself.  So I have to balance them to have a good looking lighting and it does make sense.  So if I have it here on around 6000 and my skylight, if I hit recaptures,  this will be 6 times brighter, but if I have it on one, this is too dark.  And the difference is here between this object or this part compared to the sky,  there is a noticeable difference between them.  So I have to take care that my skylight is not very bright or it's not very dark.  The detail lighting mode in my opinion is the best view mode that you can  calibrate or see how your skylight is working compared to your sky.  Because you can see textures in here or a lot of things that is going on and  distracting you from comparing and visualizing the lighting.  So you can use this view mode or just lighting only to see how it looks and start then make it  brighter or darker based on your art direction, your game, your project.  So in this case, it might be good but it might be a bit different on your side.  So it's totally up to you.  But as mentioned, you need to understand how it works like that so you can do whatever you want  in it and make it perfect.  Let me know what are your thoughts about the skylights in the comment section below and  don't forget to join our discord community for any upcoming sessions like this when we  relate a scene from scratch.  And thank you so much for watching this video.  See you next time.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_014.jpg


---

## Structured Notes

### Core Technique
Deep dive into UE5 Skylight: two source types (Captured Scene vs Specified Cubemap), Real Time Capture behavior, `Is Sky` material flag, Sky Distance Threshold (must be smaller than sky sphere size), cubemap resolution/rotation, Lower Hemisphere Solid Color, and calibration with Detail Lighting viewmode.

### Summary
16-minute Karim Yasser tutorial explaining how Skylight works under the hood in UE5. Chrome ball used throughout to visualize reflections. Covers: Skylight as ambient+reflection reprojection from environment; Source Type: Captured Scene (best) vs Specified Cubemap; Real Time Capture (efficient, requires `Is Sky` material flag) vs manual Recapture (~120ms cost); Sky Distance Threshold (black skylight fix — must be smaller than sky sphere mesh scale); cubemap resolution (128-512, power of 2); Source Cubemap Angle for rotating cubemap; Lower Hemisphere Solid Color (keep ON for interiors); PBL intensity (keep at 1 for accurate, adjust slightly as artistic control). Calibration: use Detail Lighting viewmode to compare skylight brightness against sky mesh brightness.

### Key Steps
1. **Understand what Skylight does**: captures environment around it (colors, brightness, indirect data) and reprojects as ambient fill light + reflections
2. **Source Type** — two methods:
   - **Captured Scene** (default): captures sky mesh/environment in the scene; most accurate; requires a sky to be visible in the scene
   - **Specified Cubemap**: uses a cubemap texture directly; not tied to scene; good when no dynamic sky; use neutral/overcast textures (avoid high-contrast textures — bright spots will appear as harsh blotches on meshes)
3. **Real Time Capture**:
   - Enable for automatic recapture when sky changes; more efficient than manual Recapture (~120ms per recapture)
   - **Requirement**: sky sphere mesh material must have **Is Sky** property enabled; without it → skylight goes black with Real Time Capture
   - Fix: open sky material → search `Is Sky` → enable; marks mesh as "sky component" that skylight recognizes
4. **Sky Distance Threshold** (critical for black skylight fix):
   - Default: 150,000 (cm units); skylight only captures data BEYOND this distance
   - If sky sphere mesh scale < 150,000 → skylight sees no sky → appears black
   - Fix options: (A) increase sky sphere mesh scale to exceed threshold; (B) decrease Sky Distance Threshold to match sky sphere size (e.g., if sky sphere is scale 15,000 → set threshold to 14,000)
   - Set to very low (e.g., 1) to capture all details around it (including nearby objects)
5. **Cubemap Resolution**: power of 2 (128/256/512); sweet spot is 256 or 512; higher = sharper reflections + more GPU memory; 128 fine for colors/ambient, 512 for reflective surfaces
6. **Source Cubemap Angle**: rotate cubemap independently; use to align hottest cubemap spot with directional light direction
7. **Lower Hemisphere Solid Color**: keep ON (default = black) for interiors; prevents flat over-brightening from underside sky; turning OFF = sky captured on underside = brighter/flatter ambient; can change from black to white for brighter underside fill
8. **Mobility**: Movable recommended; adds Distance Field AO; Lumen handles DFAO automatically so less critical with Lumen enabled
9. **PBL intensity**: 1.0 = accurate to captured sky brightness; increase slightly for artistic ambient boost; don't over-brighten
10. **Calibration method** (Debug → Detail Lighting viewmode):
    - Switch to Detail Lighting to remove texture distraction and see pure diffuse+ambient
    - Skylight brightness should roughly match the sky mesh's own apparent brightness
    - If skylight is much brighter than sky mesh → reduce intensity; if too dark → increase
    - This viewmode is the cleanest way to see how skylight contributes relative to sky

### UE Systems / Blueprints / Settings
- **Source Type: Captured Scene** — skylight reads the sky mesh/environment; preferred for exterior scenes with dynamic sky; requires `Is Sky` material flag on sky mesh for Real Time Capture
- **Source Type: Specified Cubemap** — uses a cubemap texture asset; independent of scene sky; adjust Source Cubemap Angle to rotate; use neutral textures; best for indoor scenes without dynamic sky
- **Real Time Capture** — continuous sky capture at minimal performance cost; requires `Is Sky` material tag; compare: manual Recapture = ~120ms per update
- **Is Sky (material flag)** — per-material boolean; marks this mesh as a sky dome; enables Real Time Capture to see it; search `Is Sky` in material editor to find
- **Sky Distance Threshold** — minimum distance from skylight before it captures data; default 150,000 cm; must be < sky sphere mesh world scale; most common cause of mysteriously black skylights
- **Cubemap Resolution** — 128, 256, 512 (power of 2); affects quality of reflections and ambient lighting; 512 recommended when scene has shiny/reflective surfaces
- **Lower Hemisphere Solid Color** — ON (solid color, default black): prevents underside sky from brightening interiors; OFF: captures below too (brighter/flatter result); keep ON for interiors
- **Intensity Scale** — multiplier on captured brightness; 1.0 = true to capture; can be slightly increased for artistic purposes; higher values = brighter ambient but more washed out
- **Detail Lighting viewmode** — Editor viewport mode; strips all textures/colors; shows only direct + indirect light contribution; ideal for comparing skylight brightness against sky mesh

### Difficulty
Beginner-Intermediate. Most settings can stay default but the Sky Distance Threshold and `Is Sky` material flag are critical non-obvious settings that cause common black-skylight issues.

### UE Version
UE5 (Lumen referenced; Real Time Capture behavior as of UE5)

### Tags
lighting, skylight, hdri, ambient, reflections, workflow, technique, pbl, performance, debugging

---

## Related Entries
- `if-i-have-40-mins-to-light-an-environment-in-unreal-engine-5---ill-do-this.md` — Karim Yasser exterior PBL; uses skylight as one of 5 global actors; Real Time Capture setup
- `realistic-and-physical-lighting-in-ue5-what-is-pbl.md` — PBL theory (EV100, units); pairs with skylight calibration
- `the-fastest-way-to-learn-lighting-in-ue5.md` — Josh Toonen; exterior lighting system (directional + skylight + sky); mentions HDRI Backdrop plugin as skylight alternative
- `tips-for-sky-atmosphere-fog---unreal-engine-5-ue4.md` — Sky Atmosphere + fog (skylight's companion systems for exterior scenes)
