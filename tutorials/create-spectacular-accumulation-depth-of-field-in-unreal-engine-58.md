---
title: Create SPECTACULAR Accumulation Depth of Field in Unreal Engine 5.8
source: YouTube
url: https://www.youtube.com/watch?v=H3OfTUhMmmc
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-23
ue_version: "UE 5.8"
tags: [depth-of-field, accumulation-dof, bokeh, cinematics, camera, groom, hair, movie-render-graph, exr, anamorphic, lens-distortion, rendering, experimental, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/create-spectacular-accumulation-depth-of-field-in-unreal-engine-58/
frame_count: 15
---

# Create SPECTACULAR Accumulation Depth of Field in Unreal Engine 5.8

**Source:** [YouTube](https://www.youtube.com/watch?v=H3OfTUhMmmc)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 14m58s | 15 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro: The "Ugly Bokeh" Problem in Unreal [0:00]
**Transcript:** So I love Unreal Engine for filmmaking, but until now with shots like this, with shallow  depth of feel, what do you get this ugly bokeh?  But in Unreal Engine 5.8 there's a new Accumulation depth of feel plugin, which turns your ugly  bokeh into beautiful bokeh!  Hurry!  And so I'm going to show you how to do that in this video.  So here's the issue that we get with shallow depth of feel using the deferred render in  Unreal Engine.  It has a hard time working out where the bokeh and the blurry bits should be, especially  with hairs and grooves and transparent objects.  So like here, we've got hair that whisker that's coming off the front of his face, and so  it looks right here, but then when he goes over something that's further away behind him,  then it has problems working out what that should be, the bokeh for that.  In the past, what people would do was they would use path tracers, but the path tracer  is exponentially slower.  And if I'm going to use path tracering, then I may as well just use three studio max and  V-ray and have a render form.  But I don't have a render form, so I like to use deferred rendering.  And until now, we haven't really had the option of having nice bokeh, but with Unreal  5.8 there is now the depth of feel Accumulation plugin, which I'll show you how to use.  And so what we have to do is the first thing is it's not on by default, so you have to

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_000.jpg

### Enabling the Experimental Accumulation DOF Plugin [1:21]
**Transcript:** enable it by going into your edit plug-ins and then we look for Accumulation Depths of  Field, Experimental, and then you enable that and then it'll say, you want to always  say, it's an experimental version, blah, blah, blah, blah, blah, don't use it, blah,  blah, blah, blah, blah, honest.  And then you say yes, and then you have to restart.  So I'm going to get it safe, select it and restart, then we're going to come back into  the engine.  So now we've installed the plugin.

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_001.jpg

### Adding the Accumulation Camera Component [1:50]
**Transcript:** The next thing to do is to select our camera and add a camera component.  And so we go to grab our camera that we're viewing through and then under here, where  it says details, you go to this add button and here you can go down or search for rendering  and then Accumulation Depths of Field, Camera Component.  And you select that and then it'll appear down here, give it a name if you want, I don't  want to.  And so you have to select this.  If you want to change the values rather than like normally when you to select the top  layer, you won't see it.  So you actually have to go and select the Accumulation Depth of Field Camera Component and then it'll  give you the options and these are the defaults.  And for now, I'm just going to show you what the result would look like.  So let's just go to a frame, say here and you can see like the Depth of Field here is  kind of weird and it's kind of strange here on these whiskers.  So we're going to enable the Accumulation Depth of Field by going into real time settings,

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_002.jpg

### Real-time Viewport Settings & Setup [2:43]
**Transcript:** maybe and we go to Accumulation Depth of Field and if you don't see this, it's because  that plugin isn't installed.  So if you don't see it, it's all the plugin.  Then you go to Settings and then I use Use Camera Settings.  So this will look at the Accumulation Depth of Field Camera Component of whatever camera  you're currently looking through and in the sequence I'm looking through this camera.  And so now what we need to do is we go back into the here and we turn on Accumulate and  it'll start basically working out the view of every single pixel based on, I don't know,  something clever.  Anyway, here's the magic and then we hit Accept and then, did it, did it, did it, did it,

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_003.jpg

### Hair and Groom Depth of Field Comparison [3:26]
**Transcript:** look at that.  It's giving you absolutely lovely bokeh.  And look on this hair now, it's actually in the right spot.  And so now I'm just going to move in around to this little hairs on these chinny chin chin  and you can see here now it's calculating each hair correctly based on the depth from the  camera.  So that is wonderful.  Well, one thing you'll notice, if I come back to my main timeline, as I let go, you'll  see, I mean, it's got this lovely depth field, but it's not as strong as when I was using  the standard renderer.  So if I just turn this off, that's, it's much stronger.  So what I'm going to do is just compensate for that on my actual camera.  So I'm going to go into my camera settings.

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_004.jpg

### Camera Exposure & Manual Metering Tips [4:11]
**Transcript:** And so what I like to do for all of my cameras, I like to make them as manual as possible.  So I go into the post-process and turn on metering mode to manual.  I've made little favorites here, but you find these under, about halfway down here under  post-process lens exposure.  And by default, this is on auto exposure, but I like to turn onto metering mode manual  and exposure compensation.  And that way I can change the aperture and then basically change the exposure compensation,  which is effectively like adding more or less neutral density filters if it was a real  camera.  So I'm going to open up my aperture a little bit more here by changing it from 1.2 to 0.5  and everything's going to go brighter.  And then I'm going to change the exposure compensation to 2.5.  And then it's not automatically updating it.  So I'm just going to change the frame, come back.  And now you can see here that we're getting much softer, more gorgeous, the bokeh, which  is lovely.

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_005.jpg

### Adjusting Accumulation Samples & DOF Splat Size [5:13]
**Transcript:** So I've selected my camera and I'm going to the Accumulation Depth of Field settings.  And then we're going to look at the, this number samples and it's basically the more samples,  the more accurate and the nicer it looks, but it's going to take longer.  250x is pretty nice.  You can go down to like 64, but if you look at say something like this, you'll start  seeing little striations in there as it calculates it.  So there's not as many samples.  So you can see some jiles, zoom in on that.  And if I go down to say 32, that'll become more apparent.  There's less, basically variations in there, but it'll be faster to render.  There's also this doff splat size.  And so that again, I think that one's something to do with how accurate it is, round the  edges of high contrast things.  Not quite sure, but basically the higher this number goes, the faster it renders, but you'll  get sort of thing kind of break here.  If you look, I'm going to zoom in close up on this, you get like this little jiggy jaggedy  sort of jag bits.  And they're going to go up really high.  And then you'll see like this on these nodes, it's kind of breaking a little bit and you  can see this is a bit more.  So I'm going to leave it at the default value.  One thing I've noticed though, certain distances or sometimes when you're moving around, you'll  get these like, I'm going to show you, it's going to move this around, it's kind of  weird dark edge appearing here it is.  So you get this sort of kind of weird clippy plane.  I don't quite know what causes it, or even if it'll be there when we come to render.  But if you just change this doff splat size, certain values will get rid of it.  That's your technical answer.

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_006.jpg

### Custom Bokeh Textures & Lens Kernels [6:53]
**Transcript:** Another great feature and that is under bokeh, you can specify the bokeh texture.  So if you go into your content browser and here I've loaded up a lens kernel image from  I can't remember where I found it, there's online somewhere but basically you can find  a lens kernel, it's just an image, a piece of bokeh and I've made this one anamorphic.  And then you can drag that into here.  So if I drag this into our bokeh texture, you'll see the shape of the bokeh changes and  it's now going to be smaller.  So I'm going to go back into my sequencer, change my aperture and make it wider.  Make two, let's make it two and make this one one.  And I have to move my frame, it's not dating.  Let's make this zero.  Let's move that one down.  And then I'm going to change my bokeh softness and reduce that down.  So hopefully we should see a bit more of that shape here.  There we are.  It's going to have no bokeh softness.  So this is getting some nice shapes that match that kernel.  You can see them there, it's quite gorgeous, that is.

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_007.jpg

### Anamorphic Squeeze & Crop Settings [8:01]
**Transcript:** So I just wanted to show you something that I'm doing in this shot.  And I've got anamorphic looking bokeh and this is the standard depth field but also works  with the accumulation depth field.  And I'm getting this by changing the squeeze factor and the crop settings on the camera.  So I'm just going to show you how to do that.  So you go to your slightly camera and then under lens settings, you go down to the  squeeze factor and by default, it's one.  And then you can see my, I've got spherical looking bokeh now.  And then the other thing is, it starts with no crop as well.  So if I was going to turn this on, I've got a normal scene, going to turn it on, I'm  going to set my squeeze factor to two, but then you get something strange happens.  And you go, ah, okay, so it's gone super wide screen.  So what you do is you basically go into crop settings and then you set that to your desired  movie making format.  And I was actually using 177 in this case.  So there we go.  Now there is something else that we're missing now because of the accumulation depth of  field.  And that is we can't use the petsful bokeh.  It's not actually making any difference besides breaking it.  So you don't get that lovely kind of curved petful cat-side kind of look with the accumulation  depth of field, which is a bit a sad or any, oh no, but I'll take this any day.  But you can always turn it off and go back to the other one if you need that look.

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_008.jpg

### Performance & Render Time Expectations [9:23]
**Transcript:** The another disadvantage, obviously, is the amount of time it takes to render a frame  because you've got a lot more calculations.  And then you also want to put on temporal sampling as well.  So you got, you know, it's exponentially slower than your deferred renderer.  And I like to sort of take normally render about say five, ten seconds of frame for the  deferred renderer.  And this one, I'll kind of like once I've got everything good and I'll just kick it off  and it's more of an overnight render in that it's probably about thirty seconds to a minute  depending.  I'd say depending on what your sample size is and how big your frame is as well.  That makes a big difference in this case.  But it's much faster than rendering with a path tracer because that one it would take  overnight with a render form.  And I don't have those.  So talking of rendering, I'm going to show you my movie render graph setting.

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_009.jpg

### Movie Render Graph Setup for 5.8 [10:11]
**Transcript:** So you go into your movie render queue, open this up here, go down to movie render graph  and then select the one that you want.  And then I've got my custom range one here.  This is what I rendered that opening sequence with the nice bit.  You click on this and then it comes up with the movie render graph.  Now if you want a little bit more of a detailed explanation of this, watch my previous video  on the the new movie render graph in 5.8.  All right, go for a very basic setup and it's basically this setup.  But I'll give you a very quick pricey right now.  So there's your input, there's your master sort of settings, you grab a pin, drag it  out, it'll give you all of the things that used to be in the movie render queue down the  side.  And now they're basically all here stacked up like that.  So that's how you find them.  The weird thing though is if you want temporal samples, you have to add this sampling method.

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_010.jpg

### Temporal Sampling & Output Settings (EXR/DWAA) [11:00]
**Transcript:** So you just type in sampling method and that's how you get your temporal samples.  And so you enable that and you give it a value.  And this one here, I've got a value of five camera settings.  I've got this on set to frame open because I've got some video with using composure and  then warm up settings, the default game overrides, that's the default global output settings  basically specify your output directories and the resolution and I see a very bad my frames  and I'm using a custom playback range.  And then down here, this is per layer, I'm using the deferred renderer and I just turned  on temporal super resolution and a spatial sample count of one.  And then I like to disable the tone curve because I like to have a linear SRGB color space  so I can then bring it into divinci and do some more bells and whistles and color corrections  on it.  And then I've set this to an EXR sequence rather than the default, which is a JPEG.  And then I have also set it to the DWAA compression.  And then I turn off render layer because I don't need multiple layers.  So I've just turned that off and then we go to output like that and then don't do anything  there.  So you hit save, then you come down here and then when you're ready to render, you just  hit render.  And if you want to render a camera without the accumulation depth of field option, if you

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_011.jpg

### Auto-Activate vs. Viewport Rendering [12:20]
**Transcript:** go into accumulation depth of field and then you come down to auto activate.  So if you turn that off, even though it's showing you in the viewport, it won't render  it with the movie render graph.  So that's the important one there.  If you want to render with it on or off to do a comparison or something.  So one more thing, thanks for watching this far and there is a bonus for you.

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_012.jpg

### Bonus: Panini Lens Distortion Tricks [12:48]
**Transcript:** And that is since we couldn't have the pets for looking bokeh with the lovely cat size,  there is another lens distortion that actually works with this and it is a C-VAR.  And what it is is, I'm going to type it in, our dark lens distortion, Penini D. And then  let's set that.  I think the default is zero.  So I put the default zero should look the same.  And then if I make this say point two, you see it's like pushing in on the lens.  So let's go for point five.  And you see it's actually doing proper lens distortion.  So it's non-rectal linear.  So it's actually bowing the center of the frame more than it is the outsides.  And then what you do is you compensate by like zooming out a little bit on your camera.  You can actually go over one, you can go to two, you can go for like craziness, let's go  for it.  So four is the maximum, you see it's really bowing it right here in the middle.  So you can get some interesting looking weirdness there.  So let's go back to the value of one.  And then there's another one as well, which is the S. And at that one, actually sort of  scales the sides of the frame up like that.  So let's go for one.  You see, so it's like pushing those up.  And then two.  And so you can get some extreme looking effects, which is fantastic.  Because it's like calculating those before it calculates the actual rendering stuff.  I don't know what it's doing, but you can kind of do some pretty exaggerated looking things  in engine, which is really fun.  So now you can have as much fun as you can throw a stick at, warping yourself and coming  up with some creative looks in your next video and talking to the next videos.

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_013.jpg

### Coming Next: Composure Updates in 5.8 [14:40]
**Transcript:** I'm going to be doing one on the new updates in composure for 5.8.  And there's some really cool little things and some big things too.  So make sure that you subscribe because you don't want to miss that.  And if you've already subscribed, thank you.  I really appreciate it.  And I'll see you on that one.

**Frame:** tutorials\frames\create-spectacular-accumulation-depth-of-field-in-unreal-engine-58\frame_014.jpg


---

## Structured Notes

### Core Technique
UE 5.8 Accumulation Depth of Field (experimental plugin): replaces deferred bokeh with accurate per-pixel accumulation sampling, correctly handling hair/groom and transparent objects. Setup: enable plugin → add Camera Component → enable via Real-time Settings. Custom bokeh textures, anamorphic squeeze, and Panini lens distortion CVars available.

### Summary
Dean Yurke demonstrates the new Accumulation DOF plugin in UE 5.8, which solves the longstanding ugly/incorrect bokeh on hair, groom, and transparent objects in deferred rendering. The plugin adds a Camera Component with configurable sample counts (250 recommended) and custom bokeh texture slot. Caveats: ~30-60 seconds per frame (vs 5-10 sec deferred), no petal bokeh support. Movie Render Graph setup includes temporal sampling method node, disable tone curve, EXR/DWAA output. Bonus: Panini lens distortion CVars (`r.lens.distortion.panini.d` and `.s`) work with accumulation DOF for cinematic lens warp effects.

### Key Steps
1. **Enable plugin:** Edit → Plugins → search "Accumulation Depth of Field" → enable (Experimental) → restart editor
2. **Add Camera Component:** select camera actor → Details → Add → search "rendering" → "Accumulation Depth of Field Camera Component"; must select this sub-component (not camera root) to edit settings
3. **Activate in viewport:** Real-time Settings (⋯ button) → Accumulation Depth of Field → Settings → Use Camera Settings; in component → check "Accumulate" → Accept
4. **Compensate weaker DOF:** camera aperture setting (e.g., f/0.5 for wider DOF than f/1.2); Post-Process → Metering Mode=Manual → Exposure Compensation (e.g., -2.5) to offset brightness from aperture change
5. **Tune sample quality:** component → Number Samples: 250=quality, 64=faster with visible banding, 32=fastest; DOF Splat Size: default recommended; adjust to fix dark clipping-plane artifact at certain distances
6. **Custom bokeh:** component → Bokeh Texture → drag in lens kernel image (import anamorphic bokeh PNG); Bokeh Softness=0 for crisp kernel shapes; widen aperture to make shapes visible
7. **Anamorphic look:** Camera → Lens Settings → Squeeze Factor=2; Crop Settings=1.77 (compensates width); note: petal bokeh not supported with accumulation DOF
8. **Render via Movie Render Graph (5.8):** MRQ → Movie Render Graph → open; drag from input pin to add: Sampling Method (temporal samples=5), Deferred Renderer (TSR on, spatial samples=1, disable tone curve), Global Output Settings (EXR, DWAA compression, output dir, resolution); auto-activate toggle on component=off skips accumulation DOF in render for comparison
9. **Panini lens distortion (bonus CVar):** `r.lens.distortion.panini.d` 0-4 = center push/barrel distortion; `r.lens.distortion.panini.s` = scales frame sides outward; works with accumulation DOF (petal bokeh doesn't)

### UE Systems / Blueprints / Settings
- **Accumulation Depth of Field Plugin (Experimental, UE 5.8)**: per-pixel accumulation sampling; correct bokeh for hair/groom/transparents; much slower than deferred
- **Accumulation DOF Camera Component**: Number Samples (quality vs speed); DOF Splat Size (edge accuracy vs render speed; fix dark clipping artifact by adjusting); Bokeh Texture slot; Bokeh Softness; Auto Activate (toggle off to skip in render)
- **Real-time Settings → Accumulation DOF → Use Camera Settings**: reads component settings from active sequencer camera
- **Movie Render Graph (UE 5.8)**: new node-based replacement for MRQ settings; Sampling Method node for temporal samples; deferred renderer node with TSR+disable tone curve; EXR/DWAA output
- **Panini CVars**: `r.lens.distortion.panini.d` (0-4, barrel distortion); `r.lens.distortion.panini.s` (side scale); computed before renderer so works with accumulation DOF
- **Camera: Manual Metering + Exposure Compensation**: essential to control brightness when changing aperture for DOF strength; mirrors ND filter behavior
- **Camera Squeeze Factor + Crop Settings**: anamorphic look without anamorphic lens; squeeze=2 + crop=1.77 is cinematic widescreen

### Difficulty
Intermediate — plugin-based, requires understanding of DOF, aperture, and render pipeline

### UE Version
UE 5.8

### Tags
[depth-of-field, accumulation-dof, bokeh, cinematics, camera, groom, hair, movie-render-graph, exr, anamorphic, lens-distortion, rendering, experimental, intermediate]

---

## Related Entries
- cinematography-deepdive-for-beginners---camera-and-render-settings-tutorial---un.md (camera settings, MRQ, DOF fundamentals)
- advanced-groom-dataflow-setup-in-ue-57-unreal-fest-stockholm-2025.md (groom system that benefits from accurate accumulation DOF)
