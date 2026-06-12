---
title: How To Improve Your Lighting w/ RTXGI
source: YouTube
url: https://www.youtube.com/watch?v=hJohX8T5O-8
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 4.27"
tags: [lighting, rtxgi, global-illumination, irradiance-probes, dynamic-gi, indirect-lighting, nvidia, william-faucher, intermediate, ue4]
extraction_status: complete
frames_dir: tutorials/frames/how-to-improve-your-lighting-w-rtxgi/
frame_count: 0
---

# How To Improve Your Lighting w/ RTXGI

**Source:** [YouTube](https://www.youtube.com/watch?v=hJohX8T5O-8)
**Author:** William Faucher
**Duration:** 21m15s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back, William Fosha here.  Today we're going to be talking about Nvidia's RTX GI plugin.  Now normally I wouldn't even be talking about this because Lumin and UE5 is absolutely  amazing.  But I know many of you, myself included, are sticking with UE4 for stability and production  reasons.  So for those of you still in Unreal Engine 4, RTX GI delivered a fantastic way to get high  quality indirect lighting with way, way better performance than the vanilla raytrace  global illumination options available in UE4.  So let's take a look at how to set it up, how it works, what you can do with it, and  how it compares with the other GI offerings in Unreal Engine 4.


### Skillshare [1:01]
**Transcript:** Now full disclosure, this video is sponsored by Skillshare.  Skillshare is an online learning platform with thousands of classes for creative like us  to explore new skills and dive deeper into existing hobbies or passions.  If you've always been on the fence about picking up a new skill like photography, for example,  Skillshare is the perfect place for that, whether you're a beginner or an advanced photographer.  You're going to find something that fits your needs right here.  Which brings me to this Skillshare original, Jessica Kabaici's class on portrait photography,  which tells you everything you need to know about shooting in various conditions and styles,  and a class open to photographers of all levels, whether you're completely green or a  season veteran.  Skillshare classes are curated, high quality, they're ad-free, and they're a constant stream  of new classes for you to choose from.  Now because Skillshare is sponsoring this video, the first 1000 of my subscribers to click  the link down below will get a one month free trial of Skillshare so that you can start  learning today.  And now, let's get global illumination set up.


### How RTXGI Works [2:10]
**Transcript:** So for the nerds like me out there, here is how it works.  RTXGI is based on irradiance probed, which is a common solution used in many game engines  today.  In fact, this is not new technology.  This has been around since something like 1998.  It starts off by placing probes in the scene, then it uses ray tracing to trace and shade  rays from probes in the relevant volume or your scene.  And finally, with that information, it's going to compute the indirect lighting and the  visibility from the ray trace probes without any leaks.  So in super dumb down, simplified terms, think of each lighting probe as a reflection  capture actor of sorts, it's going to capture all the lighting and visibility information  around it.  In real time, it's fully ray trace, which means it's going to update as soon as there are  changes in the scene, like a character walking by or changes in the lighting situation.  And with all that information stored, it's going to essentially re-project all that  lighting information around it, similarly to how a decal would in several different locations.  And this is why having more probes will give you a more accurate lighting.  I'm really simplifying this, but th...


### Pros & Cons [3:23]
**Transcript:** RTXGI is extremely flexible, it is scalable, which means that you can tailor it to your  specific needs within your project.  It runs on all DXR capable GPUs, which means you can use anything from a 1060 all the  way to a 3090 if you so desire.  It has full ray trace and quality with no denoising necessary, which is a huge plus compared  to the legacy ray trace global elimination options in UE4.  And because the lighting results are so good, it allows for much faster content creation,  which means you don't need to bake any more lighting, there's no more light leaks,  you don't need any more light map UVs, what you see in your viewport is what you get  at runtime.  It works on any material and lighting model, and to top it off you have fantastic performance.  You're going to get double the frame rate you had with the legacy ray traced global elimination.  And it looks better so it's a win-win.  Now some of the cons are it does not work with the sky atmosphere systems, and you might  run into issues with batch rendering in the movie render queue.  So if you're using the queue feature of the movie render queue, because what's going  to happen is RTX GI needs to be recalculated at the...


### How To Install RTXGI [5:33]
**Transcript:** So let's talk about how to get RTX GI set up.  For starters, you're going to need to go to the Epic Marketplace and search for Nvidia  RTX Global Illumination right here.  Now unlike most plugins, this one cannot simply be downloaded and automatically added to your  project.  You'll need to click on the external link button right here and in turn, that is going  to bring you to Nvidia's own website where you can download the plugin from there and  we're going to have to manually install it right here where it says download RTX GI UE4  plugin, hit the accept button and download it right there.  You'll have a zip file to download.  Now once you've downloaded that file from the Nvidia website, unzip that file and in that  folder, you're going to have the RTX GI folder.  You're going to select this folder right here.  You're going to copy it and you're going to paste it wherever the engine is installed.  So in my case, it is in program files, Epic Games, UE4.27, engine, plugins, runtime,  Nvidia, and there you're going to paste the RTX GI folder right here.  Now once we're in Unreal, there's still one more thing that we need to do.  We're going to go to the settings tab up here, go to ...


### How To Use RTXGI [7:00]
**Transcript:** So now that we have our RTX GI plugin downloaded, installed, and enabled in our project, let's  jump right into how to set it up and get started.  The first thing we need to do is to go to the volumes tab on the left hand side, scroll  down until you see the RTX GI, DDGI volume.  I know it's a word salad, but bear with me.  We're going to drag and drop this right here into our scene and you'll see it creates  a typical Unreal volume.  So what we need to do is this is we need to make sure that this end compasses the entirety  of our level.  So I'm going to scale this up and make sure that is at least as large as my environment.  But you want to keep it just large enough to barely encompass the level itself.  You don't want to make it this big.  We want to make it about this big.  Again, just so that the size is slightly bigger than our playable level here.  And also I'm going to scale this down so that it fits snugly with our environment right  here.  Like so, something like that.  That should be fine for now.  Now you'll see, well, still nothing happened.  We still don't have any indirect lighting.  What do we do?  There are, you guessed it, two console variables that we need to en...


### Nvidia's Documentation [9:07]
**Transcript:** Now Nvidia has made a series of dedicated videos on the rtxgci plugin and they go in  depth on every single setting you can find here.  So if you want to learn more about the specific setting in rtxgci, I'll have a link to those  videos in the description below as well.  So let's dive into some of the settings that you are going to want to use as a content  creator, as an artist to get the best possible looking results.  So first off, by selecting the ddgci volume here, let's go into the details panel and  scroll down until we see the visualized probed button right here.  We're going to turn that on.  And you'll see just like that, we have a whole bunch of other dots showing up in our  scene.  These are essentially our irradiant probes.  The more probed you have in your scene, the more accurate your lighting will be.  And these are why it's very important to have your ddgci volume in compath the entirety  of your level and fit your level as closely as possible because pay attention to what happens  here.  Take a look at the probe density that we have here.  If I take this ddgci volume and I scale it way up like that, suddenly we have way fewer  probed in our scene.  Now we only hav...


### Using RTXGI in Large Environments/Worlds [12:18]
**Transcript:** a huge scene in general, let me dive into some of the settings here that could be very  important for you to know about.  So I'm going to select my hderi backdrop here, press the F key, and notice how the hderi  backdrop is not very big.  So to clearly demonstrate what I mean here, I'm going to set the size here to a ridiculously  large value like 50,000.  And let's go back to the inside of our scene here.  You'll notice we kind of lost our indirect lighting.  We still have a little bit, but not very much.  Why is that?  Why was it much brighter before?  And the reason for this because now our hderi is so much further away.  And the ray traced rays cast by our irradiance probes here, they just don't reach the distant  hderi here.  They don't reach our sky.  So in order to fix that, we're going to scroll down here and in a details panel, pay attention  to where it says probe max ray distance.  I'm going to click on this and add another zero or two.  And now we got our nice sky lighting back.  So again, if you're working with a very large scale environment, something huge, this trick  here might be very good for you to know about.  Now with that being said, that kind of segway to my ...


### Fixing odd Lighting Artifacts [14:32]
**Transcript:** And the event that you do run into these odd light leaks and issues like this in the  corners of the models, you're choosing you can do either select your ddgi volume in  your outliner and kind of nudge it to try and fix it like that.  Or you can increase the amount of probes right here.  So by default, it's said to 8 by 8 by 8.  If I increase this to 16 by 16 by 16, you'll notice our lighting will be a little bit  more accurate and all those light leaks are completely gone.  So in general, 16 works pretty well, depending on the size of your level.  So showing off how RTX GI works in a very simple, basic environment like this is all fine  and dandy.  But let's jump into the cave environment that you saw in the intro of this video and see  how RTX GI works in a real world situation.


### Using RTXGI in Detailed Scenes [15:22]
**Transcript:** So here is the cave entrance level.  The first and foremost, I cannot take credit for making this level right here.  This is part of the ICVFX production test package that you can find on the epic marketplace.  All I did here was I redid the lighting entirely for the sake of this tutorial.  So you'll see we've got some nice direct lighting shining in here.  You'll see my directional light is my main one right here and I've got some rec lights  and a few point lights to help with the directionality of the light coming in here.  But our entire scene is really dark.  We don't have any RTX GI going on here.  So let's add RTX GI here and really bring this scene to life.  So again, on the left hand side, I'm going to go to the Volumes tab, scroll down, get the  RTX GI DDGI volume.  Drag and drop this into our scene.  Make sure it is large enough to fit our entire scene here.  Maybe lift it up like that, something like this.  And now again, enable those two console variables.  R.Galibal Illumination.Experimental plugin, want?  And the second one being R.RTXGI.DDGI1.  But now, hey, we have the DDGI volume here.  We've added the console variables.  Why do we not see anything?  Why is this n...


### Outro & Thanks [20:59]
**Transcript:** And that's really all there is to it.  So I really hope this kind of clarifies and demystifies what RTXGI is all about.  And that's it folks.  If this video has helped you out, do consider subscribing.  But if this video didn't help you out, then I don't know.



---

## Structured Notes

### Core Technique
Setting up Nvidia's RTXGI (DDGI) plugin for UE4 — irradiance-probe-based global illumination providing fully dynamic, ray-traced indirect lighting without lightmap baking, with 2× better performance than UE4's legacy ray-traced GI.

### Summary
21-minute tutorial on Nvidia's RTXGI plugin for UE4 — the best GI option for UE4 users who want dynamic, high-quality indirect lighting without baking. RTXGI uses ray-traced irradiance probes (fully dynamic, no denoising needed, no lightmap UVs). Covers installation, DDGI volume setup, probe density tuning, large-scene fixes, and light leak resolution. Particularly valuable for productions that must stay on UE4 for stability.

### Key Steps

**How RTXGI Works:**
- Places irradiance probes throughout the scene volume
- Each probe traces and shades rays from its position (like a tiny reflection capture)
- Computes indirect lighting and visibility from all probes
- More probes = more accurate lighting; probes update in real-time (character walks by → GI updates)

**Pros vs UE4 Legacy RTGI:**
- Works on ANY DXR GPU (GTX 1060 → RTX 3090)
- No denoising noise artifacts
- No light leaks (visibility information is baked into probes)
- No lightmap UVs required
- What you see in viewport = runtime result
- ~2× better performance than legacy ray-traced GI

**Cons / Limitations:**
- No Sky Atmosphere support
- Movie Render Queue batch rendering: RTXGI needs to recalculate at the start of each frame — problematic for batch jobs
- Requires manual Nvidia download and engine plugin install

**Installation:**
1. Epic Marketplace → search "Nvidia RTX Global Illumination" → click External Link button
2. On Nvidia's website: Download RTX GI UE4 Plugin → extract ZIP
3. Copy `RTXGI` folder to: `C:\Program Files\Epic Games\UE_4.27\Engine\Plugins\Runtime\Nvidia\`
4. Open UE4 → Edit → Plugins → search "RTXGI" → Enable → Restart

**DDGI Volume Setup:**
1. Modes/Place Actors → Volumes tab → scroll to **RTX GI DDGI Volume** → drag into scene
2. Scale volume to fit entire playable area (just slightly larger than level bounds)
3. Do NOT make it enormous — it dilutes probe density
4. Enable GI via console commands:
```
r.GlobalIllumination.ExperimentalPlugin 1
r.RTXGI.DDGI 1
```

**Tuning Probe Density:**
- DDGI Volume Details → **Visualize Probes** ✓ → see probe spheres in scene
- Default: 8×8×8 = 512 probes
- Light leaks? → increase to 16×16×16 or higher
- Large volume = fewer probes per area → increase probe count proportionally

**Fix for Large/Outdoor Environments:**
- Probes trace rays; if HDRI is very far, rays don't reach the sky
- DDGI Volume Details → **Probe Max Ray Distance** → add a zero (e.g. 1000 → 10000)
- Restores sky/HDRI contribution in large-scale environments

**Fix Light Leaks:**
1. Nudge the DDGI Volume slightly in position
2. Or increase probe count (8×8×8 → 16×16×16)

### UE Systems / Blueprints / Settings

**Console Variables:**
```
r.GlobalIllumination.ExperimentalPlugin 1  // enable experimental GI plugin
r.RTXGI.DDGI 1                              // enable DDGI
```

**Key DDGI Volume Settings:**
```
Visualize Probes: True/False    // debug view
Probe Count: 8×8×8 (default) → 16×16×16 (better quality/leaks fix)
Probe Max Ray Distance: 1000 (default) → increase for large outdoor scenes
```

**Probe Density Rule:** Volume size is fixed triangular/voxel distribution — smaller volume = denser probes. Always fit volume as tightly around the playable level as possible.

### Difficulty
Intermediate — UE4-specific plugin; involves manual installation

### UE Version
UE 4.27 (plugin is UE4-only; UE5 uses Lumen instead)

### Tags
lighting, rtxgi, global-illumination, irradiance-probes, dynamic-gi, indirect-lighting, nvidia, william-faucher, intermediate, ue4

---

## Related Entries
- `tutorials/lumen-explained---important-tips-for-ue5.md` — UE5 equivalent (Lumen)
- `tutorials/lighting-in-unreal-engine-5-for-beginners.md` — Indirect lighting in UE5
- `tutorials/lighting-interiors-in-unreal-engine-5.md` — Interior GI workflow (UE5)
- `references/rendering-pipeline.md` — Rendering settings overview
