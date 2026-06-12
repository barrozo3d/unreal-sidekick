---
title: Bake Lighting FASTER with GPU Lightmass - Unreal Engine 4.26
source: YouTube
url: https://www.youtube.com/watch?v=hq1WFFF6iD0
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 4.26"
tags: [lighting, baked-lighting, gpu-lightmass, lightmap-uv, rtx, ray-tracing, virtual-texturing, hdri, william-faucher, intermediate, ue4]
extraction_status: complete
frames_dir: tutorials/frames/bake-lighting-faster-with-gpu-lightmass---unreal-engine-426/
frame_count: 0
---

# Bake Lighting FASTER with GPU Lightmass - Unreal Engine 4.26

**Source:** [YouTube](https://www.youtube.com/watch?v=hq1WFFF6iD0)
**Author:** William Faucher
**Duration:** 21m23s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, it's great to see you again.  This week's video is going to be about GPU lightmasks and lighting for interiors.  Now, I've already covered everything in this video in last week's live stream,  but I'm fully aware that not everyone wants to or has a time to sift through a two hour  live stream for the useful bits of information.  So, this is going to be a very bare bones, very to the point video on how to set up GPU  lightmasks and how to fix any issues your may or may not have in your scene.  So, with that being said, let's jump right in.


### Boring (But important!) Part [0:30]
**Transcript:** So before we even get started with the fun stuff, we need to go through the really boring  part.  And that is ensuring that your project is set up correctly.  So there's a few things that you really need to be made aware of here,  things that you absolutely need to get GPU lightmasks to work.  And that is as of 4.26, you need an RTX capable graphics card.  Next up, you need to enable ray tracing in your project settings.  And third, you need to enable virtual texturing as well.  Now, if that all sounds real scary, don't worry.  I've included a link to the official epic documentation in the description below.  So go ahead and read through that.  There's an enabling GPU lightmasks section and they will guide you through the process  of enabling ray tracing and virtual texturing.  Okay?  So just to be clear, if you don't have a graphic card that supports ray tracing, you won't  be able to use GPU lightmasks as of 4.26.  If you're not sure how to enable virtual texturing and that's what it's saying,  we can go to the edit tab up top.  You're going to go to project settings and then you're going to click type virtual.  And down below, you'll see virtual textures, enable virtual texture ...


### Scene Setup [2:24]
**Transcript:** So in the past, baked lighting had always been a little bit scary.  It's been tedious.  There's lots of things that can go wrong.  Don't worry, I'm here to start this whole scene from scratch and hold your hand all  the way to a result that looks pretty good.  So the first thing I like to do when you're creating a new blank scene is adding a new  Proof Browser's volume.  This should always be your first step.  So we're going to go ahead and drag and post Browser's volume in here.  So we're going to select our post process volume and in the details panel, we're going  to search for unbound and make sure that infinite extent unbound is checked.  The second thing we want to do, it turn off auto exposure.  So we're going to type EXP and right here in the exposure settings, min and max, we're  going to set these both to one.  This effectively disables auto exposure because it's just the worst.  So once that's done, we can go ahead and exit this out and there's still one more thing  we need to do before we get started.  Epic recommends that we disable ray tracing effects in our viewport entirely when using  baked lighting.  So I noticed it's a bit confusing because they say that you need...


### Lightmap UV's [7:02]
**Transcript:** But before we get into it, it is critically important to understand what light map UVs  are.  So I'm going to select this wall here and I'm going to open double click and open up  the static mesh editor right here.  So here I have my static mesh of my wall segment was the window.  And if we click on a UV button up here, you'll see there's UV channel zero and UV channel  one.  When it comes to baking lights, you absolutely need to have two UV channels.  So channel zero up here, you'll see that's for your texturing.  Those are the UVs that you use for texturing your model.  UV channel one.  Let's click this here.  These are the UVs that are used for the light baking.  So light maps are going to be baked on your second UV channel.  There's no way around this.  And so it is imperative.  It is critical that every single model in your scene has light map UVs, a second UV  channel for light maps.  It is also critically important to know that not a single UV shell can overlap.  It is super important that they don't overlap.  So it's fine if you're a zero one UV space is not as super efficiently packed.  It's more important that the UV shell don't overlap because then you're going to get  r...


### Lightmap Resolution [9:04]
**Transcript:** So in order to fix this kind of bad result, we're going to select all our shapes here.  Select all your wall segments.  And again, once more in the details panel, we're going to go ahead and search for res.  And you'll see overwritten light map res.  Okay.  I'm going to set this to for this, you know, to get a nice clean result.  I'm going to set it to 2024.  So once that's done, we're going to have to go ahead and bake one more time.  So I'm going to go ahead and build lighting again, slow mode shows up and it's going to  take what I'm going to hit control R to go into fast mode.  And you'll see already takes way longer to bake.  And the reason for that is because the light map resolution, the larger the light map  resolution, the longer it's going to take to bake, but the better your results will be.  And now we've just added away.  And now you'll see, hey, we're getting a much better result here, right?  Now we got our light hitting the ground shadows and not splodging and misshapen.  We're getting some bounce light, but you'll see it's things are still looking a little  bit odd.  It's a little bit dark.  So what do we do?  We're going to have increased the brightness over direc...


### Slow Mode Fix [10:33]
**Transcript:** you know, so you know, as you can't seem to control R to escape slow mode down here,  you need to go to the little arrow here and click on disable real time override.  That should turn off the real time mode and your build lighting will go back to full speed.  So to speak, I'm not sure why this happens sometimes, probably a shortcut that I'm unaware  of, but just so you know, and now, wow, we have a much brighter room.  We got a lot more bounce coming in here, but we still have some some weird things in  notice like these edges seem very dark and that's because of ambient occlusion.  So by default ambient occlusion that turned on.  So we're going to select our post-process volume and in the details panel, we're going  to search for ambient occlusion and you'll see let's have the intensity to zero.  When I'm baking light, I usually turn off ambient occlusion and you'll see already we're  looking getting a result that's a little bit better by default as this and I don't like  how strong it is by default.  So I'm going to turn it off entirely.  So now we're getting some pretty much, much better result.  This is a very bright room.  Now let's say for example, I don't want to be that br...


### Lightmap Compression (Get Cleaner Bakes) [12:08]
**Transcript:** Now one thing you may notice is let's zoom in real close here and notice how this wall  is very splotchy and not smooth.  We're not getting any smooth gradients here, right?  This is no good, especially right here where there's like nice soft bounce light.  The gradients are really harsh and aggressive and why is that?  Just because of light map compression and fortunately, there's a way to turn this off.  So in order to do that, we're going to go to window up here and we're going to open  world settings.  And that should open up to world setting window here.  And what you need to do is in a light map setting where it says compressed light maps, we're  going to uncheck this.  Okay, so move this out of the way.  And we're going to go ahead and bake the lighting one more time and you'll see all  the splotchyness right here.  It's all going to be gone.  You're going to get a perfectly smooth gradient.  Now one thing to keep in mind is when you uncheck compressed light maps, it's going to reduce  your artifacts, but it's going to increase the memory and this size by four times.  So if you're running low on memory, you may want to keep this enabled.  But if you have the memory to spare,...


### Baking HDRI's (Skylight) [13:49]
**Transcript:** create an HDRI backdrop.  OK, so I find it right here in lights.  If you don't see HDRI backdrop in your light, you need to go ahead and enable the plug-in  for it.  OK, so I'm going to try this into here.  I'm going to lower this like that.  And I'm going to leave it like that for now.  There's a few things you really need to be made aware of when using the HDRI backdrop,  when baking, specifically.  So what we're going to do is we're going to click on the HDRI backdrop.  And in the details panel, you'll see the skylight in the Add Component section here.  OK, you're going to want to make sure it's set to static.  I had issues getting it to work in stationary.  So for the sake of this video, I'm going to leave it at static because I know it works.  Next up in the source type, I'm going to set this to SLS specified QMAP and set it  to make sure it uses the same HDRI as the backdrop itself.  So right now, just using approaching storm 4K, this one will also use approaching  storm 4K.  And now we should be ready to bake.  So we're just going to hit the build lighting button.  And just like that, now we have bake lighting.  That actually looks pretty good.  Now, just to demonstrate, I'...


### Bake What You See Mode [15:19]
**Transcript:** Now before I bake, however, I want to show you guys one nifty little feature.  So if you notice in your GPU light math window, we're going to see mode.  We have full bake.  If you click on it, you'll see bake which you see as well.  Now what this does is it does what the name implies, it's only going to bake with the  camera's seeing.  So let's demonstrate right here by clicking build lighting.  Now, did you notice how fast that baked?  What I've got to do now is I've got to hit the save button all the way down here.  Very important to hit save.  And I'm going to hit the stop button next.  Now you'll see now it's been denoiced, but you'll notice how it didn't bake anything  else.  It only baked the area that we were looking at, right?  So that's what bake which you see does.  It's a super handy feature for really speeding up your lighting process, especially when you  don't want to have to bake your entire level.  If you want to, you have the option to only bake what you're looking at.  Super useful pro tip.  So but for now, I just wanted to show you guys how that worked.  I got to set this back to full bake and build the lighting one more time.  And now we can see now we got a muc...


### Bonus Tip! [17:31]
**Transcript:** And that was time for this week's bonus tip.  This is something that you should very much be aware of.  And that has to do with the brightness of your materials and how that contributes to the  lighting of your scene.  OK, so right now I have a material on my walls that has a brightness of 0.7.  OK, so you can see here it says 0.7 in value.  It's just a flat, constant color.  That's the brightness of my wall right now.  And here's what I'm going to do.  I'm going to I'm going to darken this color to something like 0.2 or 0.3, which is still  not very dark, but you'll see how drastically it affects the bounce lighting in your scene.  And it's really and you may actually get some artifacts which your materials are too  dark.  So let's go ahead and I'm going to change this to let's say 0.2.  And you'll see looking at it 0.2 is not that dark, right?  It's still a reasonable brightness.  And what I'm going to do now is I'm going to go ahead and build lighting and that's the  color of the material is the only thing I've changed here.  OK, just so you know, let's build and we're going to notice that we're going to start  running into some artifacts.  Things that don't look very good, shad...



---

## Structured Notes

### Core Technique
GPU Lightmass for accelerated lightmap baking in UE4.26 — full interior setup from scratch including requirements (RTX GPU + ray tracing + virtual texturing), lightmap UV setup, resolution tuning, compressed lightmap disable for smooth gradients, HDRI backdrop baking, and "Bake What You See" mode for rapid iteration.

### Summary
21-minute practical guide to GPU Lightmass interior baking. Walks through all the gotchas: lightmap UVs must be on UV channel 1 (no overlapping), resolution must be cranked up (default is too low), ambient occlusion should be disabled during baking, compressed lightmaps cause splotchy gradients and should be unchecked, and material brightness (albedo) dramatically affects bounce light quantity. The "Bake What You See" mode is a hidden gem for fast testing.

### Key Steps

**Requirements (all three required):**
1. RTX-capable GPU (required as of UE4.26)
2. Project Settings → enable Ray Tracing
3. Project Settings → search "virtual" → enable Virtual Texturing

**Scene Setup:**
1. Add Post Process Volume → check **Infinite Extent (Unbound)**
2. Disable Auto Exposure: PPV → Exposure → set Min/Max to **1**
3. In viewport settings → disable Ray Tracing effects (recommended by Epic for baked lighting scenes)

**Lightmap UV Requirements:**
- Every static mesh needs two UV channels: UV0 = texturing, UV1 = lightmap baking
- Static Mesh Editor → UV button → verify channel 1 exists
- No UV shells in channel 1 may overlap (unlike texturing UVs)

**Lightmap Resolution:**
1. Select all wall/floor/ceiling meshes
2. Details panel → search "res" → **Overridden Light Map Res** → set to 1024 or 2048
3. Higher resolution = cleaner bake + longer bake time

**Slow Mode Fix:**
- If lightmass hangs or builds seem slow: look for "Disable Real Time Override" in the GPU Lightmass window
- Ctrl+R accidentally enables viewport real-time override, which slows baking
- Click the arrow dropdown → Disable Real Time Override

**After Bake Cleanup:**
- PPV → search "ambient" → Ambient Occlusion intensity → set to **0** (AO from baked lighting is too aggressive by default)

**Compressed Lightmaps (Critical Quality Fix):**
1. Window → World Settings → Lightmap Settings
2. Uncheck **Compress Lightmaps** → rebake
3. Result: smooth gradients instead of splotchy banding
4. Cost: 4× lightmap file size (only disable if you have memory budget)

**HDRI Backdrop:**
1. Place + → search "HDRI Backdrop" → drag in
2. Click HDRI Backdrop actor → Details:
   - Add Component section → Skylight → set Mobility to **Static**
   - Source Type → **SLS Specified Cubemap** → pick same HDRI as the backdrop
3. Build Lighting → HDRI will be baked

**Bake What You See Mode:**
1. GPU Lightmass window → Mode dropdown → select **Bake What You See**
2. Click Build Lighting → only bakes the area currently visible in the camera
3. IMPORTANT: Hit **Save** button in GPU Lightmass window before stopping
4. Hit Stop → bake is applied + denoised for only the visible area

**Material Albedo and Bounce Light:**
- Material brightness directly affects indirect light bounce in baked scenes
- Dark albedo (0.2) = much less bounce light + possible dark artifacts
- Keep wall/floor albedo reasonable (0.4–0.7) for good bounce
- If scene is too dark after bake: check material albedo before adjusting light intensity

### UE Systems / Blueprints / Settings

**Minimum setup for GPU Lightmass:**
```
Project Settings:
  Hardware Ray Tracing: Enabled
  Virtual Texture: Enabled

Post Process Volume:
  Infinite Extent: True
  Auto Exposure Min/Max: 1.0 (disables auto-exp)
  Ambient Occlusion Intensity: 0.0

World Settings → Lightmap:
  Compress Lightmaps: False  // smooth gradients

GPU Lightmass Window:
  Mode: Full Bake (or Bake What You See for test iterations)
```

**Lightmap resolution override per-mesh:**
```
Select meshes → Details:
  Overridden Light Map Res: 1024  // default 64 is too low
                           2048  // high quality interiors
```

### Difficulty
Intermediate — several required settings across multiple panels; pitfalls easy to hit

### UE Version
UE 4.26 (GPU Lightmass was introduced in 4.26; core workflow same in UE5 but Lumen is usually preferred)

### Tags
lighting, baked-lighting, gpu-lightmass, lightmap-uv, rtx, ray-tracing, virtual-texturing, hdri, william-faucher, intermediate, ue4

---

## Related Entries
- `tutorials/lighting-interiors-in-unreal-engine-5.md` — Interior lighting with Lumen (UE5 alternative to baked)
- `tutorials/demystifying-the-skylight-unreal-engine-4-5.md` — Skylight for baking HDRI contribution
- `references/lighting-systems.md` — Lighting systems reference
