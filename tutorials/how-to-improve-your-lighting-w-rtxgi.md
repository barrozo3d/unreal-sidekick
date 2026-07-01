---
title: How To Improve Your Lighting w/ RTXGI
source: YouTube
url: https://www.youtube.com/watch?v=hJohX8T5O-8
author: William Faucher
ingested: 2026-06-23
ue_version: "UE4"
tags: [lighting, rtxgi, nvidia, global-illumination, irradiance-probes, ray-tracing, ue4, performance, indirect-lighting]
extraction_status: complete
frames_dir: tutorials/frames/how-to-improve-your-lighting-w-rtxgi/
frame_count: 11
---

# How To Improve Your Lighting w/ RTXGI

**Source:** [YouTube](https://www.youtube.com/watch?v=hJohX8T5O-8)
**Author:** William Faucher
**Duration:** 21m15s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back, William Fosha here.  Today we're going to be talking about Nvidia's RTX GI plugin.  Now normally I wouldn't even be talking about this because Lumin and UE5 is absolutely  amazing.  But I know many of you, myself included, are sticking with UE4 for stability and production  reasons.  So for those of you still in Unreal Engine 4, RTX GI delivered a fantastic way to get high  quality indirect lighting with way, way better performance than the vanilla raytrace  global illumination options available in UE4.  So let's take a look at how to set it up, how it works, what you can do with it, and  how it compares with the other GI offerings in Unreal Engine 4.

**Frame:** tutorials\frames\how-to-improve-your-lighting-w-rtxgi\frame_000.jpg

### Skillshare [1:01]
**Transcript:** Now full disclosure, this video is sponsored by Skillshare.  Skillshare is an online learning platform with thousands of classes for creative like us  to explore new skills and dive deeper into existing hobbies or passions.  If you've always been on the fence about picking up a new skill like photography, for example,  Skillshare is the perfect place for that, whether you're a beginner or an advanced photographer.  You're going to find something that fits your needs right here.  Which brings me to this Skillshare original, Jessica Kabaici's class on portrait photography,  which tells you everything you need to know about shooting in various conditions and styles,  and a class open to photographers of all levels, whether you're completely green or a  season veteran.  Skillshare classes are curated, high quality, they're ad-free, and they're a constant stream  of new classes for you to choose from.  Now because Skillshare is sponsoring this video, the first 1000 of my subscribers to click  the link down below will get a one month free trial of Skillshare so that you can start  learning today.  And now, let's get global illumination set up.

**Frame:** tutorials\frames\how-to-improve-your-lighting-w-rtxgi\frame_001.jpg

### How RTXGI Works [2:10]
**Transcript:** So for the nerds like me out there, here is how it works.  RTXGI is based on irradiance probed, which is a common solution used in many game engines  today.  In fact, this is not new technology.  This has been around since something like 1998.  It starts off by placing probes in the scene, then it uses ray tracing to trace and shade  rays from probes in the relevant volume or your scene.  And finally, with that information, it's going to compute the indirect lighting and the  visibility from the ray trace probes without any leaks.  So in super dumb down, simplified terms, think of each lighting probe as a reflection  capture actor of sorts, it's going to capture all the lighting and visibility information  around it.  In real time, it's fully ray trace, which means it's going to update as soon as there are  changes in the scene, like a character walking by or changes in the lighting situation.  And with all that information stored, it's going to essentially re-project all that  lighting information around it, similarly to how a decal would in several different locations.  And this is why having more probes will give you a more accurate lighting.  I'm really simplifying this, but that is the gist of it.  Now, let's talk about some of the probes and some of the cons.

**Frame:** tutorials\frames\how-to-improve-your-lighting-w-rtxgi\frame_002.jpg

### Pros & Cons [3:23]
**Transcript:** RTXGI is extremely flexible, it is scalable, which means that you can tailor it to your  specific needs within your project.  It runs on all DXR capable GPUs, which means you can use anything from a 1060 all the  way to a 3090 if you so desire.  It has full ray trace and quality with no denoising necessary, which is a huge plus compared  to the legacy ray trace global elimination options in UE4.  And because the lighting results are so good, it allows for much faster content creation,  which means you don't need to bake any more lighting, there's no more light leaks,  you don't need any more light map UVs, what you see in your viewport is what you get  at runtime.  It works on any material and lighting model, and to top it off you have fantastic performance.  You're going to get double the frame rate you had with the legacy ray traced global elimination.  And it looks better so it's a win-win.  Now some of the cons are it does not work with the sky atmosphere systems, and you might  run into issues with batch rendering in the movie render queue.  So if you're using the queue feature of the movie render queue, because what's going  to happen is RTX GI needs to be recalculated at the start of each shot, which means when  it renders the first shot in the batch, it's going to be fine.  But the second shot, it starts off totally off.  And as the shot renders frame by frame, RTX GI slowly fades back in.  So if you're using batch rendering a lot, use this with caution because you may run into  that issue.  When I had to render the three shots for the intro of this video, I had to render each  shot individually.  The batch rendering feature could not be used unfortunately.  So hopefully that comes with the patch fix, but who knows.  And lastly, one of the cons of RTX GI is that it can be a little bit finicky to set up  between the console variables and getting the DDGI volume to be placed perfectly.  You kind of have to wiggle it and nudge it and move it around a little bit to get some  better results.  So like I said, it's a little bit finicky, but the pros vastly outweigh the cons of RTX  GI.

**Frame:** tutorials\frames\how-to-improve-your-lighting-w-rtxgi\frame_003.jpg

### How To Install RTXGI [5:33]
**Transcript:** So let's talk about how to get RTX GI set up.  For starters, you're going to need to go to the Epic Marketplace and search for Nvidia  RTX Global Illumination right here.  Now unlike most plugins, this one cannot simply be downloaded and automatically added to your  project.  You'll need to click on the external link button right here and in turn, that is going  to bring you to Nvidia's own website where you can download the plugin from there and  we're going to have to manually install it right here where it says download RTX GI UE4  plugin, hit the accept button and download it right there.  You'll have a zip file to download.  Now once you've downloaded that file from the Nvidia website, unzip that file and in that  folder, you're going to have the RTX GI folder.  You're going to select this folder right here.  You're going to copy it and you're going to paste it wherever the engine is installed.  So in my case, it is in program files, Epic Games, UE4.27, engine, plugins, runtime,  Nvidia, and there you're going to paste the RTX GI folder right here.  Now once we're in Unreal, there's still one more thing that we need to do.  We're going to go to the settings tab up here, go to plugin and we're going to search  for RTX and that's going to bring in the RTX global illumination plugin.  Make sure that's enabled.  If it's not, turn it on, restart the engine and then we'll be ready to go.

**Frame:** tutorials\frames\how-to-improve-your-lighting-w-rtxgi\frame_004.jpg

### How To Use RTXGI [7:00]
**Transcript:** So now that we have our RTX GI plugin downloaded, installed, and enabled in our project, let's  jump right into how to set it up and get started.  The first thing we need to do is to go to the volumes tab on the left hand side, scroll  down until you see the RTX GI, DDGI volume.  I know it's a word salad, but bear with me.  We're going to drag and drop this right here into our scene and you'll see it creates  a typical Unreal volume.  So what we need to do is this is we need to make sure that this end compasses the entirety  of our level.  So I'm going to scale this up and make sure that is at least as large as my environment.  But you want to keep it just large enough to barely encompass the level itself.  You don't want to make it this big.  We want to make it about this big.  Again, just so that the size is slightly bigger than our playable level here.  And also I'm going to scale this down so that it fits snugly with our environment right  here.  Like so, something like that.  That should be fine for now.  Now you'll see, well, still nothing happened.  We still don't have any indirect lighting.  What do we do?  There are, you guessed it, two console variables that we need to enable.  The first one we want to use is r.globalillumination.experimentalplugin1.  And the second one is r.rtxgci.ddgci1.  Both of these console commands will be found down in the description below.  Don't worry.  And now you'll see we have global illumination showing up in our scene here.  If I move my directional light around, you'll see the lighting is updating accordingly.  Now you may be thinking this looks a whole lot like lumen and you're not wrong.  It's a completely different technology than lumen.  But fundamentally, the results are very similar.  Now all of the rtxgci settings are controlled in our ddgci volume that we find in our  outliner right here.

**Frame:** tutorials\frames\how-to-improve-your-lighting-w-rtxgi\frame_005.jpg

### Nvidia's Documentation [9:07]
**Transcript:** Now Nvidia has made a series of dedicated videos on the rtxgci plugin and they go in  depth on every single setting you can find here.  So if you want to learn more about the specific setting in rtxgci, I'll have a link to those  videos in the description below as well.  So let's dive into some of the settings that you are going to want to use as a content  creator, as an artist to get the best possible looking results.  So first off, by selecting the ddgci volume here, let's go into the details panel and  scroll down until we see the visualized probed button right here.  We're going to turn that on.  And you'll see just like that, we have a whole bunch of other dots showing up in our  scene.  These are essentially our irradiant probes.  The more probed you have in your scene, the more accurate your lighting will be.  And these are why it's very important to have your ddgci volume in compath the entirety  of your level and fit your level as closely as possible because pay attention to what happens  here.  Take a look at the probe density that we have here.  If I take this ddgci volume and I scale it way up like that, suddenly we have way fewer  probed in our scene.  Now we only have two of them in the height.  You know, we do get some indirect lighting here, but it's, you know, it could be much better.  And that's why it's good to keep your ddgci volume kind of fitting your level very snugly.  You're going to get a maximum efficiency when it comes to the density of those probes.  So I'm going to reset this here like that.  Now we can also increase the probe count right here in the details panel where it says  probe count by default is at the 8 by 8 by 8.  I'm going to set it to 16 by 16 by 16.  And now you'll see we have way, way, way, way more probed in our scene.  Our lighting is going to be a lot more accurate.  Now next up, a setting that I loved to use is the light multiplier setting right here.  I'm going to set this to a value of five.  And as the name implies, it's going to boost the intensity of your lighting.  So in this case, it's overkill, but in many, many situations, and we're going to look  at this a little bit later, the light multiplier is often extremely necessary because in some  very dark interior scenes, you're going to need to bump that up by a lot.  Now one thing I do want to show you is pay attention right here.  We got this nice soft blue lighting coming in from the top of our roof here.  And that's thanks to our hderi backdrop.  If I hide the hderi backdrop, we lose all that nice soft GI that we got from the sky  because this is an actual mesh with an emissive material on it.  That is why the probes here are capturing that lighting detail.  It is also worth noting that emissive materials also contribute lighting to GI just like an  unrelingent five with lumen.  So I'm going to apply this emissive material to my sphere here.  And you'll see it is actually emitting light in my scene.  Very much in the same way that lumen does.  Now it's not quite as good as lumen, but it's about as close as it can possibly be.  Now in the event that you're working with a very large scale open world game or just

**Frame:** tutorials\frames\how-to-improve-your-lighting-w-rtxgi\frame_006.jpg

### Using RTXGI in Large Environments/Worlds [12:18]
**Transcript:** a huge scene in general, let me dive into some of the settings here that could be very  important for you to know about.  So I'm going to select my hderi backdrop here, press the F key, and notice how the hderi  backdrop is not very big.  So to clearly demonstrate what I mean here, I'm going to set the size here to a ridiculously  large value like 50,000.  And let's go back to the inside of our scene here.  You'll notice we kind of lost our indirect lighting.  We still have a little bit, but not very much.  Why is that?  Why was it much brighter before?  And the reason for this because now our hderi is so much further away.  And the ray traced rays cast by our irradiance probes here, they just don't reach the distant  hderi here.  They don't reach our sky.  So in order to fix that, we're going to scroll down here and in a details panel, pay attention  to where it says probe max ray distance.  I'm going to click on this and add another zero or two.  And now we got our nice sky lighting back.  So again, if you're working with a very large scale environment, something huge, this trick  here might be very good for you to know about.  Now with that being said, that kind of segway to my next point, one of the caveats of our  DXGI is I'm going to hide my hderi backdrop here.  And using the environment light mixer, I'm going to create a sky atmosphere and a volumetric  cloud.  Now you'll see I have a sky atmosphere system set up correctly.  But you'll see while the sunlight itself is contributing to global elimination, you'll  see here we got the bounce light hitting the ceiling here.  But we don't have any sky information affecting our scene.  We don't get that nice soft blue lighting that we had with the hderi backdrop.  The sky atmosphere system is not currently compatible with RTX GI.  And video is aware of this.  But for now, if you need to have skylight coming into a window or something, you should  use an hderi backdrop or an hderi itself or some kind of skylight or something, but  not the sky atmosphere system.

**Frame:** tutorials\frames\how-to-improve-your-lighting-w-rtxgi\frame_007.jpg

### Fixing odd Lighting Artifacts [14:32]
**Transcript:** And the event that you do run into these odd light leaks and issues like this in the  corners of the models, you're choosing you can do either select your ddgi volume in  your outliner and kind of nudge it to try and fix it like that.  Or you can increase the amount of probes right here.  So by default, it's said to 8 by 8 by 8.  If I increase this to 16 by 16 by 16, you'll notice our lighting will be a little bit  more accurate and all those light leaks are completely gone.  So in general, 16 works pretty well, depending on the size of your level.  So showing off how RTX GI works in a very simple, basic environment like this is all fine  and dandy.  But let's jump into the cave environment that you saw in the intro of this video and see  how RTX GI works in a real world situation.

**Frame:** tutorials\frames\how-to-improve-your-lighting-w-rtxgi\frame_008.jpg

### Using RTXGI in Detailed Scenes [15:22]
**Transcript:** So here is the cave entrance level.  The first and foremost, I cannot take credit for making this level right here.  This is part of the ICvfx production test package that you can find on the epic marketplace.  All I did here was I redid the lighting entirely for the sake of this tutorial.  So you'll see we've got some nice direct lighting shining in here.  You'll see my directional light is my main one right here and I've got some rec lights  and a few point lights to help with the directionality of the light coming in here.  But our entire scene is really dark.  We don't have any RTX GI going on here.  So let's add RTX GI here and really bring this scene to life.  So again, on the left hand side, I'm going to go to the Volumes tab, scroll down, get the  RTX GI DDGI volume.  Drag and drop this into our scene.  Make sure it is large enough to fit our entire scene here.  Maybe lift it up like that, something like this.  And now again, enable those two console variables.  R.Galibal Illumination.Experimental plugin, want?  And the second one being R.RTXGI.DDGI1.  But now, hey, we have the DDGI volume here.  We've added the console variables.  Why do we not see anything?  Why is this not working?  The reason for that is because this is a classic example of what I was talking about earlier.  We need to bump up that brightness of our DDGI volume.  So going in the details panel, I've got to scroll down and I'm going to set the light  multiplier to 20.  And that is how we get some stronger indirect lighting in our scene like this.  Now you'll see some parts are a little bit too dark.  So I need to adjust my DDGI volume.  Pay attention right here as I move the DDGI volume.  It just means that we need to make sure that it encompasses the entirety of our level.  I can probably make this a little bit larger like this to get some more lighting in the  hallway.  And there we go.  With RTXGI, without RTXGI, the difference is day and night.  Normally, this works really well with UE5, but like I said, if you're still in UE4, this  is a fantastic way to work.  Now there's one more thing I want to talk to you about here and that's getting some  more accurate lighting.  Being able to achieve a greater probe density.  So if I select my DDGI volume here, I'm going to go ahead and click on Visualize  Probes and you'll see we have, you know, we have a few probes in our scene, right?  We've got a series, we've got enough to get a decent lighting.  But in some cases, we need more probes.  We just need more detail.  We need a more accurate lighting.  Now there are two ways of going about this.  Either I select a DDGI volume and I increase the probe count to something like 32.  You'll see here I'm already using 16 by 16 by 16 probes.  My frame rate is about 20 FPS or so.  That's not very good.  I don't want to have to increase the density more.  So what can we do?  You can use multiple volumes in your scene if you need a higher density in some location.  So in this area here, I really want to have a more accurate lighting, right?  So I'm going to go ahead and add a new RTX GI DDGI volume right here.  I'm going to scroll down and set the light multiplier to 20 so that boats are matching.  And I'm going to scale this up.  Something like this, but I'm going to scale it up so that it encompasses the entrance  here a little bit, okay?  Because I want to focus my lighting on this area here.  So again, I'm going to click on visualize probes and now you'll see we have a much better  probe density than we had previously.  Again, if I hide this, you'll see we don't have very many probes here, right?  We can kind of see them.  But if I turn this on, we got way more to work with here, but it's localized.  So again, we can have multiple DDGI volumes in select spots where we want a better lighting  quality instead of having an even distribution of all the probe across your entire scene  and your frame rate just tanks.  So going back into my camera view right here, I'm going to select my two DDGI volumes  and uncheck visualize probes.  So I'm going to hide the new DDGI volume that we just created.  And this is before and this is after.  You'll see the difference is rather subtle.  But there's a few areas that look substantially better.  I want you to pay attention to this line right here, the area right here with these rocks  and the area on the left hand side here.  When I turn it on, you'll notice off, on, off, on these plants have gotten much better  shadows and lighting coming down from underneath.  We've got some much better shadow information right around here.  You'll see these rocks kind of, they don't necessarily feel like they're separate rocks  anymore.  They feel that they're all kind of blended in in a much more cohesive way.  Over here as well, we got a lot more bounce lighting.  It's a little bit less contrasting.  Now of course, this is a little bit subjective.  Some people will think this looks better, some people will think it's not.  The whole point, the whole reason I'm showing you this is you can use multiple volumes  to improve the quality of your lighting in select areas to increase that probe density.

**Frame:** tutorials\frames\how-to-improve-your-lighting-w-rtxgi\frame_009.jpg

### Outro & Thanks [20:59]
**Transcript:** And that's really all there is to it.  So I really hope this kind of clarifies and demystifies what RTXGI is all about.  And that's it folks.  If this video has helped you out, do consider subscribing.  But if this video didn't help you out, then I don't know.

**Frame:** tutorials\frames\how-to-improve-your-lighting-w-rtxgi\frame_010.jpg


---

## Structured Notes

### Core Technique
Nvidia RTXGI plugin for UE4: ray-traced irradiance probe global illumination. Alternative to Lumen for UE4 projects — fully dynamic indirect lighting with no baking, no lightmap UVs, no light leaks, real-time updates, and emissive material GI contribution. Configured via DDGI Volume placed in scene + two console variables.

### Summary
21-minute tutorial by William Faucher covering the Nvidia RTX Global Illumination plugin for UE4 (not UE5/Lumen). RTXGI uses ray-traced irradiance probes in a DDGI volume to compute indirect lighting in real time. Offers 2x performance over legacy UE4 ray-traced GI, no baking needed, supports emissive material GI. Caveats: incompatible with Sky Atmosphere (use HDRI backdrop instead); batch rendering in Movie Render Queue breaks between shots. Multiple DDGI volumes can be stacked for higher probe density in specific areas.

### Key Steps
1. **Download plugin** — Epic Marketplace → search "Nvidia RTX Global Illumination" → External Link → Nvidia website → download zip; unzip → paste RTX GI folder to: `Program Files/Epic Games/UE4.27/Engine/Plugins/Runtime/Nvidia/`
2. **Enable plugin** — UE4 → Settings → Plugins → search "RTX" → enable RTX Global Illumination → restart engine
3. **Add DDGI volume** — Volumes tab → RTX GI DDGI volume → drag into scene
4. **Scale volume** — scale to encompass entire level, fitting snugly (not too large — probe density decreases with volume size)
5. **Enable console variables** — open console (backtick `), type:
   - `r.globalillumination.experimentalplugin 1`
   - `r.rtxgi.ddgi 1`
6. **Visualize probes** — select DDGI volume → Details → enable "Visualize Probes" to see probe density
7. **Set probe count** — default: 8x8x8; increase to 16x16x16 for better accuracy; 32x32x32 heavy on performance (~20fps)
8. **Light Multiplier** — set to 5-20 for dark interiors where GI is too dim; essential for cave/interior scenes
9. **Probe Max Ray Distance** — increase (add extra zeros) for very large HDRI backdrops or huge open worlds
10. **Multiple DDGI volumes** — add additional smaller DDGI volumes in key areas for higher local probe density without destroying scene-wide performance; match light multiplier between volumes
11. **Fix light leaks** — nudge DDGI volume position, or increase probe count from 8x8x8 to 16x16x16
12. **Sky atmosphere workaround** — Sky Atmosphere is incompatible with RTXGI; use HDRI Backdrop or Sky Light instead for sky contribution to GI
13. **Batch rendering workaround** — RTXGI resets between batch render shots in MRQ; render each shot individually (not batched)

### UE Systems / Blueprints / Settings
- **RTX GI DDGI Volume** — core actor; placed in scene; controls all RTXGI settings via Details panel; must encompass entire level
- **Console variables** — `r.globalillumination.experimentalplugin 1` + `r.rtxgi.ddgi 1`; both required to activate
- **Probe Count** — DDGI volume setting; default 8x8x8; 16x16x16 good balance; higher count = more accurate but heavier performance
- **Visualize Probes** — DDGI volume detail toggle; shows probe distribution to verify density
- **Light Multiplier** — DDGI volume setting; multiplies GI brightness; essential for dark interiors; set 5-20 typical range
- **Probe Max Ray Distance** — DDGI volume setting; default covers small/medium scenes; increase for large HDRI or open world
- **Multiple DDGI volumes** — stack smaller volumes in high-priority areas for localized probe density boost; independent light multiplier per volume
- **Sky Atmosphere incompatibility** — known limitation; Nvidia aware but not yet fixed (at time of video); use HDRI Backdrop instead for sky color contribution to GI
- **Batch rendering bug** — MRQ batch mode resets RTXGI probes at start of each shot, causing GI to fade in during render; workaround: render shots one at a time
- **Emissive materials** — contribute to GI just like Lumen (probes capture emissive light)
- **HDRI backdrop distance** — if HDRI scale is very large, probes can't reach it; fix with Probe Max Ray Distance increase
- **Light leaks** — fix by: (1) nudging DDGI volume position, (2) increasing probe count
- **DXR requirement** — needs DXR-capable GPU (GTX 1060 minimum up to RTX 3090)
- **Performance** — 2x faster than legacy UE4 ray-traced GI; 16x16x16 typically maintains playable frame rates

### Difficulty
Intermediate. Installation requires manual file copy. Two console variables required. DDGI volume sizing and light multiplier tuning are the main iterative steps.

### UE Version
UE4 (UE4.27 specifically referenced; UE5 users should use Lumen instead)

### Tags
lighting, rtxgi, nvidia, global-illumination, irradiance-probes, ray-tracing, ue4, performance, indirect-lighting

---

## Related Entries
- `how-i-use-lumen-in-aaa-projects-unreal-engine-5.md` — UE5 Lumen GI (the modern successor to RTXGI for UE5 users)
- `lighting-in-unreal-engine-5-for-beginners.md` — foundational UE5 lighting concepts
- `realistic-and-physical-lighting-in-ue5-the-pbl-workflow.md` — PBL lighting workflow for production-accurate scenes
