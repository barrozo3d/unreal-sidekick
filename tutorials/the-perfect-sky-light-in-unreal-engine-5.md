---
title: The Perfect Sky Light in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=mKZUlyM9oZQ
author: Karim Yasser
ingested: 2026-06-15
ue_version: "[PENDING]"
tags: []
extraction_status: pending
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
**Transcript:** So that's actually the texture that the sky is capturing.  And if I change it to something else like this, it would be visible on my crumball,  and any other texture it will start to be visible even more.  As you can see here, and if I change the color, it will project the colors of it on the environment,  let's try even higher brightness, it will add more ambient lighting.  So actually this ambient lighting is getting projected from this cube map.  So the source type here defines which method or which way you want the skylight to use  to project this indirect lighting data.  Basically it's better to use the sky around it or the environment,  so that will give you better and more accurate reflections in your environment.  But if you wanted to use a cube map, for example, the best option in my opinion  would be to use a texture that is not having very high-prite spots,  because that will affect your meshes, especially in distance.  You will see weird-prite spots and others will be indoor.  So try to use more overcast textures or neutral textures in general.  So let's try to see if there is any good texture here.  Let's see this one.  Yes, you can see it's quite different.  As I ment...

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_005.jpg

### Sky Light Scene Capture [4:21]
**Transcript:** So we can visualize our sky or our reflections in a better way.  So let's keep them off, get back to the skylight, turn off real-time capture,  and now we should see something good.  This is now 500, but 500.  We can see it because we don't have our sky.  But if we have now our sky, and we scroll down here for recapturing,  this will make the skylight read the data again.  Now this is too bright because I have it.  Too high intensity, this is 3.  So now as you can see our lighting or ambient lighting is very soft.  We don't see very sharp shadows, very high spots,  except in some places, which is fine because we can see it in our sky.  But if we use a very high contrast image or texture cube,  this will definitely affect our skylighting.  So here, how we can actually understand it more.  Let's get back to let view, as we can see.  This is now how our sky or reflections work.  This is based on our sky, and it's not actually capturing any details, except the sky.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_006.jpg

### Sky Distance Threshold - Fix Black Sky [5:44]
**Transcript:** And that's related to this option, sky distance, search.  This means that after 150,000 units, I believe it's Unreal Unit, which is centimeter,  the skylight will start to capture the data after this distance.  So it will not capture any data before it.  So that's why the skylight, even if it's placed like here,  it's not capturing any data around it.  But this option could sometimes make our reflections or sky  feels it's not capturing anything or it's totally black.  And that might be because of our sky poke size.  Here in this example, it's set to 15,000, so it's big enough to make the sky capture all the details.  But what if it's around 150?  It's fine for now, but we need to check that by recapturing.  And it's still totally fine.  Let's try 15.  Now the skybox is smaller.  And let's see our skylight.  It's totally black.  Why?  Because the size of the sky,  folks, is not big enough for the sky distance,  searchable.  So here in this case,  I have two options to solve this problem.  Whether to increase the skybox mesh size or to decrease sky distance threshold.  So let's try here to decrease it to 15,000.  Now it works because it's not bigger than the skybox size.  So what if...

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_007.jpg

### Fix Realtime Capture Sky Light Error [8:06]
**Transcript:** And it gives you an error like that.  And your skylight is not working. It's totally black.  What you can do here may be turn off with a skycatcher or just keep it on and start to fix it.  And how to fix it is kind of easy.  You can go to the skybox mesh, open the material,  go to the master material of it.  And here search for is sky.  Turn it on.  And this mesh now will be tagged as a sky.  So the skylight will be able to read it as a sky component.  So it will capture the details from it.  That's why it works now.  Or you can turn it off and depend on recapturing every time you want to have a change in your sky.  So it will update with you.  But for now, real-time capture is good.  And even it's better for performance compared to recapturing.  Because recapturing takes almost 120 milliseconds to calculate.  But real-time capture is not taking that amount of time.  Because it's not doing it every frame or every seconds.  So now we know how to use real-time capture, the source time, the cube map.

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_008.jpg

### Cubemap Resolution & Rotation [9:17]
**Transcript:** And here if you are using a cube map, let's change it now for a cube map.  Let's try this one again.  And you can hear in the source cube map angle, you can rotate it.  As if you are rotating your sky doom or sky books.  So you can do that if you want to have the reflections from a specific side.  Or you have a sky and another cube map.  And you want to match like the highest or the hottest spot in it with the actual sky.  So you can do that from here.  And regarding the cube map resolution, this is a power of two numbers.  So usually good to have it maybe around 256 or 512.  Higher than that doesn't have actually really not small effect or difference.  And even 128 is good for a lot of cases.  But be aware of it because this affects your memory and the GPU.  So let's set it to 512 actually.  And you will see it's more sharp.  And even if we try to get back to SLS capture scene, let's take a look into it here.  This is 128.  It's very blurry.  You can see a lot of details, which is fine because it's just capturing the colors,  the data, the brightness.  So even if it's not very sharp, it's totally fine.  But this will affect the reflections as well if you have any reflective surfac...

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
**Transcript:** So actually, skylights in a lot of cases, they are not taking a lot of  interest, but it could draw in your scene or it could make your scene much, much  better or very bad flat looking scene or it's very bright.  It's very bad with the shadows, where it's the light, all of this stuff.  Or it's very, very dark that you cannot see anything in it.  So skylight is really important and there is no one way to work with it and to  have a specific setup that works for all scenarios.  It really depends on your scene, your sky, the way that you are working with it,  if you are working with BBL setup or just regular setup as you want.  If you are working with a sky like this, if you want to have a cube map,  each one has its own pros and cons, but there is nothing that is one way to go with it or  this is the best option for it.  And this is important to understand how to make your skylights perfect,  how to visualize them, how to debug them.  And here in the detail lighting mode, it's usually good to have your skylights  not too bright compared to the skybooks or vice versa.  So I cannot have my skybooks very, very dark just like this.  This is very, very dark and yeah skylight automaticall...

**Frame:** tutorials\frames\the-perfect-sky-light-in-unreal-engine-5\frame_014.jpg


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
