---
title: PATH TRACER Explained - Unreal Engine's Underrated Tool
source: YouTube
url: https://www.youtube.com/watch?v=X5zVhc5ahl0
author: William Faucher
ingested: 2026-06-23
ue_version: "UE4.27+"
tags: [path-tracer, rendering, ray-tracing, mrq, materials, glass, subsurface-scattering, denoiser, samples, lighting]
extraction_status: complete
frames_dir: tutorials/frames/path-tracer-explained---unreal-engines-underrated-tool/
frame_count: 13
---

# PATH TRACER Explained - Unreal Engine's Underrated Tool

**Source:** [YouTube](https://www.youtube.com/watch?v=X5zVhc5ahl0)
**Author:** William Faucher
**Duration:** 26m8s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


### B-Roll [0:00]
**Transcript:** This video is sponsored by Skillshare.

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_000.jpg

### Pathtracer Explanation [0:25]
**Transcript:** Hey everyone, it's great to see you again. It's been a while since my last video, but it's good to be back.  I hope you had a great summer. Now the topic of today's video is going to be all about the new and improved  Path Tracer in Unreal Engine 4.27 that just released not too long ago.  Now previously, the Path Tracer had a number of limitations. It was much slower and it didn't  support the vast majority of material types like subsurface scattering, translocency, skies,  so on and so forth. Now, all those features are mostly supported and it's amazing.  So the Path Tracer rendered what we call a ground truth image. So this is similar to offline  renders like V-Ray and Arnold. It works by casting lots of rays into our scene,  together information about light and color to shade a given pixel. It includes feature  complete materials within reflections and refractions, super-sampled anti-aliasing, and approximate  acoustics, which is totally new. But why use it at all? What's the point? It's slow, it's not real time,  it kind of defeats the purpose of using Unreal. The Path Tracer is extremely useful when you want to  compare your real-time lighting with a fully Path Tracer renderer. Path Tracer don't lie.  They're not approximations of what light should do. They are physically accurate, giving you  much, much better result, much better shadows, so much more detail. You can then use this to  measure the quality of your real-time rendering and make adjustments from there. So for me,  coming from a vfx background, I am beyond excited to start working with the Path Tracer again.  I think this is an addition that makes Unreal insanely powerful. But you might be wondering,  well, what's this Path Tracing thing? Nvidia has been trying to sell us on the RTX and Ray Tracing  stuff. What's the difference? They are, more or less, completely interchangeable terms. We  could nitpick about how ray tracing is a bit more of a general term as opposed to Path Tracing,  but outside of people writing render engines, I doubt that definition difference matters.

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_001.jpg

### System Requirements [2:26]
**Transcript:** So in order to enable it and get it running in your engine, you need to make sure that you have  ray tracing enabled in your project. This is a must. There's no way around it. So in order to  enable ray tracing in our project, we need to click on the Settings button up top here, then click  on Project Settings, and you're going to scroll down to the side where it says Platforms, Windows.  Click on the Windows button, and where it says Default RHI, we need to make sure that this is  set to DirectX12. And the next step in the search details panel up top, we can click here and type  ray tracing. And you'll need to make sure that ray tracing is turned on. Now when you click on this  here, a window will pop up asking you to enable the Support Compute SkinCash option. Click yes,  you're going to need this as well. Once that's done, you can restart the engine and you'll be ready  to go. Now we're ready to jump into how to use the Path Tracer and all of its settings.

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_002.jpg

### Using the Path Tracer [3:14]
**Transcript:** So now the best part about the Path Tracer is you can just turn it on without having to do  anything else in your scene. You don't need to change your materials, you don't need to do anything  else. So what we're going to do is we're going to go to the Lit button up top here and switch  just to Path Tracer. Now be careful, things are going to slow down considerably, and this video will  actually get pretty choppy when I click it. So I'm going to turn this on right here, and you'll notice  that it's now starting to do its thing. It's slowly calculating our samples, our image is getting  progressively better and better. But now you might realize that's just one frame. If I turn the  camera, rotate around, you'll see, oh, this does not look so good, this is really slow, especially  if you're used to, you know, working in the real time, this is the real pain to work with. So all of  our Path Tracer settings are controlled through the post process volume right here. And in the details  panel, we're going to search for Path. And you'll see right here, we have samples per pixel 16,384.  For the sake of this video, I'm going to turn this back down to 10. And because we have the  denoiser enabled right down here, pay attention to what happens when I hit Enter.  Now, poof, everything is back to normal, everything kind of denoised. Now what happened there?  Why is it so fast? Now why is it such a clean image? That's because as soon as this 10 samples  here have finished calculating, the denoiser is going to kick in. Whereas previously, it had to  finish the 16,384 samples before being denoised. That's a lot of samples. It's going to take a very  long time. So for previewing purposes, it's often easiest to just tone down your sample counts  so that you can get an easier, quicker, faster, better preview. But now we have a series of things  that are just plain wrong with our scene here. The first of which being our image is very splotchy.  It's kind of, like we've lost a lot of fine detail, especially in the wood floor here.  If I switch this back to lit mode, okay? Notice how we had a whole bunch of like gritty texture,  like we have a lot of grime there, there was lots and lots of details. But switching to the path  tracer, everything is kind of mushy, it's kind of muddy. What's happening? That's because of the  denoiser. The denoiser is incredibly aggressive. And honestly, if you want the absolute crispest,  sharpest, best possible result with the past tracer, you're going to need more samples. There's  really no way around that. You're not going to be able to get the crispest, best possible render  with low samples and a denoiser. Now, there is a very useful console command that you can use  to give you a progress bar of the rendering process. So opening up the console command menu at  the bottom, I'm going to enter r.pass tracing.progress.display1. And by hitting enter,  now when I move the camera, you'll see we have a progress bar at the bottom.  This is super useful for just getting an idea how much longer you need to wait before the  render is complete. If I crank the samples up to 500, now the progress is going much slower,  but it's really nice to know how much longer do I really need to wait.

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_003.jpg

### Why Samples Matter [6:39]
**Transcript:** So jumping into Photoshop real quick, we have two renders here. So one was rendered with 10 samples  plus the denoiser and the other one on the right hand side here was rendered with 500 samples  with the denoiser. So at first glance, especially on a compressed video on YouTube,  they may actually look pretty identical. You might not be able to tell them apart, but the moment  you start zooming in, you'll notice that the version with 10 samples really starts falling apart.  So right here on the base plate, the kind of black plastic thing here, I had a roughness texture  with a bit of roughness break up in there. And you can see it here on the 500 sample version of  the render. Whereas in the 10 sample version of the render, the denoiser completely obliterated  all of that detail. There's just everything that's perfectly smooth here. There is no  spec break up. Same thing for some of the details on the shell of our turtle here. So paying  attention to the scale detail on the shoulder versus here and on the top of the head, we have a  lot of scale detail there. There's lots of little nitty gritty stuff. Same thing was the edge of  the shell right here. Whereas on the 10 sample version of the render, all of these details on the  top of the head and on the shell, it's been completely destroyed by the denoiser because the denoiser  is so aggressive. We can even see on the front of the shell here, we've got a kind of not cheer  a bit of damage on the shell. And here it's barely visible. Let's go ahead and zoom in on the  floor here. And the same thing kind of applies. It's actually surprising how well the denoiser worked,  but it's no comparison to the 500 sample version right here. We get so much more crisp little  details. It's the small details like this that make a substantial difference in a quality of a  render. And same thing applies with just the edge of the wood plank here. We got these little  notches, the ever so subtle break up of the lines. Whereas here it's just kind of smushed.  We've lost a lot of detail here. So again, it's pretty subtle and I'm actually quite impressed with  the performance of the denoiser, especially at higher resolutions. But if you want the best possible  quality, there is really no way around using more samples. In fact, if you have enough samples,  you may be able to omit the denoiser entirely. So it's worth keeping in mind that the denoiser

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_004.jpg

### Denoising for video [9:03]
**Transcript:** really is mainly intended for use with still images. As you can see here, I have a render with  100 spatial samples with the denoiser turned on and you'll notice that right around here,  or really all across the entire image, it's getting really flickery and jittery and it looks like  crap. The reason for this is because the denoiser is not temporal. And what I mean by this is the denoiser  does not denoise the current frame based on the denoising of the previous frame. So each frame will be  denoised in its own way individually resulting in a super jittery mess like this. Now this can  be mitigated somewhat by either having more samples and adding in from temporal samples in the mix  in the movie render queue. So now you can see right here, the results are much better with temporal  samples. But I've increased the contrast here so that we can see more clearly. We still get quite a  little bit of jitteriness and flickriness in the shadowy areas, especially areas with lots of  details right around the head here and in the area that have lots of lens blur. So just keep in  mind that the denoiser does not necessarily work all that well with animated footage.

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_005.jpg

### Other Features [10:17]
**Transcript:** Now next up in the details panel, we also have max bounces. Now the amount of bounces you have  here will also affect your render times. So toning down my samples will say 100 instead and turning  my max bounces to 1, you'll notice that we start getting a lot less indirect lighting. So what's  happening is the light comes in, hits our surface and bounces one time. If I do three bounces,  you'll notice we get a bit more indirect lighting, right? We especially our box right here.  The box in the bottom left hand corner is a great indicator of what's actually happening here. So  by setting this down to 1 again, you'll notice our box in a foreground is very dark. Cranking this  up to 10. Now in the darker areas, things start getting lit up a little bit more. There comes a point  of diminishing return when it comes to the amount of bounces. So you don't need to have an insane  amount of bounces. In fact, for many renders, I've kept it at 7. Really, you should only be using as  many bounces as you need. But we'll get a little bit more into that later when we touch base on  the glass materials. Next up, we have filter width here, which says the anti-aliasing filter. So  lower values will be sharper and more aliased, whereas larger values are softer and blurrier.  So it's switching over to another environment here. I just want to show you a few other nifty features  that we can find in the pass rating settings. So I'm going to go ahead and delete every single light  in my scene here. So delete this directional light. And in my HDRI backdrop, I'm going to make  sure to my skylight it actually disabled. It's not affecting our world, right? So we have no  lights in our scene. The only thing in our scene will be this emissive HDRI texture. So you'll  see everything is pitch dark. And when I turn on the pass tracer, you'll see boom, we've got light.  And the reason for that is because in the post process volume, if we search for pass tracing again,  we have emissive materials. Okay, so everything that is emissive will cast light. So if I turn this  off here, well, there's no more light in our scene. Nothing is happening. So this is the  viruli nifty feature. This is super handy when you just want to throw in a nice looking HDRI.  You don't need to configure any skylight or anything. Everything just works kind of the way you  would expect. Again, because of the denoiser, you'll see everything is kind of splotchy. Doesn't  look that good. So again, you need more samples if you want some crisper results. And now if I want  to throw a directional light in here, well, I could. And now we have a much brighter room.

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_006.jpg

### Changes to Materials [13:02]
**Transcript:** So in this section, I want to talk to you a little bit about changes to the way that materials  are handled with the pass tracer. And we're going to take a look at some of these right here.  So first off, we've got the thin translucent model right here, which is kind of like a clear  plastic type of thing, but also cast colored shadows. And we can see right here. Next up, we have  proper pass tracer glass, which looks phenomenal now. And looking at the example here, we now have  approximate caustic refractions and reflections, which is just so nice to have now. Next up, we have  frosted glass, which is the same material as the regular glass material. However, by upping the  roughness of our glass material, we can now have frosted glass. And lastly, right here, we have  random walk subsurface scattering in 426. The pass tracer did not support subsurface scattering.  So this is a really, really nice addition to have in our project. So let's take a look at these  materials one by one, just so that you know how they are set up. So starting off with the subsurface  scattering, the pass tracer now uses a random walk subsurface scattering method, which all happens  under the hood. You don't need to enable any plug-ins or any settings to get random walk subsurface  scattering to work. It just does right away. So all I have here is the shading model at the bottom  here set to subsurface. And with these four nodes, I can control the color and how far the light will  scatter through my model. Next up, let's take a look at the glass material. You'll see here,  it's nothing complicated. We only have a flat-based color, roughness, opacity, and the  index of refraction of 1.5. With a blend mode, set the translucent here, and the lighting mode set  the surface forward shading. That's it. That's all you need to do in order to get really good looking  pass-traced glass now. And in defense, you want the frosted glass, all you need to do is to  increase the roughness of your glass material. If you want to know more about raytraced glass,  specifically, you can watch my tutorial on it right here, the link of which will be down below.  Now the last one I want to talk about is the thin translucent method right here. And the material  set it for this is a little bit weird. It's a little bit different than the others, so let's take a  look at it right here. Again, the material is pretty simple. Make sure that we have our blend mode  set to translucent, and the shading model set to thin translucent right here. Really, the refraction  of passing and roughness settings are all identical to the raytraced glass material.  The only difference here is you need to add the thin translucent material node right here.  By pressing the tab button, search for thin translucent material output, and you'll find it right here.  And the color right here is what's going to determine the color of your shadow, the color of your  actual plastic or thin translucent material. So this is perfect for like plastic wrap or anything  that's very thin like a bubble. I don't recommend that you use this at the color glass option.  It's not going to look very good. It's going to look more like plastic than glass. Even though those  material types are relatively similar, they are different. And if you're looking for the absolute,  most physically accurate result, you're going to need to differentiate those two. So when working  with glass materials, it is very important that you have enough bounces to work with. So let  me demonstrate right here by selecting our post process volume and going into details panel. We're  going to search for path tracing. And let's demonstrate what happens when I turn down the max  bounces to something like one. You'll notice none of our glass materials are really looking like  glass anymore. If I set it to two, okay, it's starting to look a little bit better. Three, a little  bit better. And let's say 10 now with 10, they look as they should. So again, when using translucent  materials, you need to have enough bounces for them to render correctly. And that last thing I want

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_007.jpg

### Changes to Skylight [17:04]
**Transcript:** to talk about in this section is a few changes to the way that the skylight is handled with the  past racers. So the past racer does not support atmospheric sky or volumetric clouds. So if you have  volumetric clouds sky setup like this, the one that has like really nice sunsets and such,  you'll notice when we go to the past racer here, the sky goes completely black, you're not going  to get anything. But there is a work around this. So by selecting our skylight in our scene,  if you set it to real-time capture like this, it will capture our sky. So you'll notice it's a  little bit blurry. It's a little bit pixelated and low res. But if we go back to lit mode,  you'll see it is pretty much the exact same result of our sky. So it is capturing our sky  and creating a cube map for us. So going back to the past racer here, even though it's low  resolution, we can fix that. So select your skylight again. And in the details panel, we're going to  set the cube map resolution right here to let's say 1024. And now we have a super high resolution  sky, which is almost the same as the sky that we have in lit mode. Not quite the same, but almost  and this should be good enough for most use cases. Now in the event that you don't want to use  the sky system in Unreal, but you would rather use an HDRI or something, then the best way to do that  would be to use the HDRI backdrops you can find right here. If you don't see it in the list here,  you may need to enable the plug-in for the HDRI backdrop to show up. Before I put in my HDRI  backdrop, I'm going to delete my sky system here. And I'm going to drag and drop the HDRI backdrop  into my scene. In the HDRI backdrop, in a detailed panel, don't forget to select your skylight  right here and disable it because otherwise you're going to get a double lighting. You're going to  get the lighting from the emissiveness of the HDRI itself and also the lighting of that's a skylight  that's casting on your scene. So be careful about that. And now our HDRI backdrop is going to be our  source of light. And now we can apply whatever HDRI we want right here in the cube map section.  So now if I go back to the path tracing mode, you'll see everything kind of looks the way that you  would expect. So those are two ways to work with either the skylight or an HDRI when using the  path tracer. Alternatively, what you can do is select your skylight, set the source type to  SLS specified cube map and choose a cube map of your choice. And just like that, we can load in an  HDRI of our choice very quickly and very easily. You're just not going to have the HDRI showing up in  a background like we had with the HDRI backdrop. So while you take the time to process that

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_008.jpg

### Skillshare [19:40]
**Transcript:** information, I want to take a moment to thank the sponsor of this video, Skillshare. Skillshare is an  online learning platform with thousands of classes on just about any topic you can possibly imagine,  such as classes relevant to our field of work, 3D modeling, texturing, rendering, filmmaking,  photography, you name it, they've probably got it. And let's say you want to break from being in  front of your desk all day like this guy, you can alternatively take a class on gardening.  So those of you who've been following this channel know that I haven't been on YouTube for very  long at all. I am unbelievably green and I have a lot to learn. And seeing that market is brown  lead now had a class on YouTube success, scripting, shooting, editing with MKBHD, he talks about getting  your audience hooked and growing your channel. I should probably get on that. Skillshare is curated  for learning and they are constantly releasing new classes. And what I mean by this is that it is  entirely ad-free so you can stay focused. So because Skillshare is sponsoring this video, I have a  special link for you down below the first thousand of you to click on the link in the description below  will get a one month free trial at Skillshare so that you can start learning today. And with that  being said, let's get back to rendering. So with all new amazing features, there are always a

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_009.jpg

### Limitations [20:52]
**Transcript:** series of caveats and limitations and things that don't totally work perfectly. So become the  pasture through now supports more features than it doesn't support. I'm going to go ahead and tell  you about the feature that it does not support. So we got hair strands which are not supported,  cascade particle systems, spline meshes, decals, which is a real bummer because I use decals all the  time and so do you probably. But hopefully that comes in later version. Next up volumetric fog,  exponential height fog, light functions, hair and single layer water material types. There is no  multi GPU support and lastly is semi depth of field support. So it's important to keep in mind that  the pass rate is only using the regular depth of field post process. The depth of field is not a  path traced feature. So just keep that in mind. And you can see right here there is some kind of  jitteryness going on in the depth of field areas. I am pushing the depth of field to its absolute  limits here. And while it's not perfect, it's still pretty good. Like the fact that I can get  this kind of result so quickly is phenomenal. So yeah, I might sound harsh toward the devs at epic  but hats off to them. The fact that they have pulled us off is so awesome. So I will include a link  in the description below to the full list of supported and unsupported content. You can find it  right here. Now a few good things that you should probably know about is that when using really  bright materials for interior renders, you should absolutely keep your albedo values below one.  So more along the lines of 0.8, you should not be using a value of one anyway because there is  virtually nothing in the world that has an albedo of one. Even the purest whiteest snow on the top  of the andes will have an albedo of like 0.8. So to keep your render time lower and get a better  result, you should keep your base color or your albedo at a value of 0.8 or lower. It's a double  whammy. You're really it's a win-win. And that brings us to the next section of this video. How do  you use the movie render queue with the path tracer in order to export amazing looking renders?

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_010.jpg

### Rendering with MRQ [23:06]
**Transcript:** So the path tracer now works flawlessly with the movie render queue as you saw in the intro of  this video. So I'm going to show you how to set it up. Now if you're not familiar with how to  use the movie render queue, you can find a tutorial on it right here and you can find the link down  below. So let's open our movie render queue settings by clicking right here and let's click on  our settings. It is really important to know that when comes to time to render with the movie render  queue, you're not going to control the samples through the post process volume. That is the key takeaway  here. So by going to the settings tab here and adding the anti aliasing tab, the samples of your  path tracer are controlled through the spatial sample count right here. If I wanted to have, let's say,  500 samples, you need to enter 500 right here. You should also override the anti aliasing and set it  to none for better results. But you're also going to want to play around with the temporal sample count.  Because temporal samples will give you much better motion blur than spatial samples. Now keep in mind  that the temporal samples and the spatial samples kind of work together and they multiply one another.  So let's say, for example, I wanted to have five temporal sample counts. You no longer need to have  a spatial sample count of 500. You only need 100. Because it's going to do 100 times 5 for a total  of 500 samples. If you wanted to have 10 temporal samples, then you only need to have 50 spatial  samples. So what I recommend you to do is to start by figuring out how many samples you're really  going to need for your render and then do the math and then figure out how many spatial and temporal  sample counts you need. That is how it works. And that's really the main takeaway here. And now,  lastly, before rendering, you're going to delete the deferred rendering tab here. And we're going to  add path tracer that you can find down here. You'll see here the path tracer had the exact same  settings as a deferred rendering tab. And that's really all you need to do.

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_011.jpg

### Recommended Render Settings [25:07]
**Transcript:** So my preferred rendering settings are as follows. The temporal and spatial sample counts  completely depend on what it is I'm rendering. But in general, 16 spatial samples and 16 temporal  samples are a really good starting point. And lastly, turn off that denoiser. Yeah, you heard me. Noise  is detail. And removing the noise means removing the detail and your results are going to end on  like a splotchy mess. Like we've seen in the examples throughout this video. So in the example  you saw in the intro, absolutely no denoising was used. And the result turned out pretty okay.  In fact, I prefer to denoise my renders in posts like in DaVinci Resolve or something because I have  way, way more control that way. Once you've determined how many samples you need and the movie  render queue is set up correctly, hit that render button. That's a bit of frames out.  So if this video has helped you out, don't forget to hit the subscribe button. It really makes  a big difference. Thanks so much for watching and I'll see you next time.

**Frame:** tutorials\frames\path-tracer-explained---unreal-engines-underrated-tool\frame_012.jpg


---

## Structured Notes

### Core Technique
Path Tracer: ground-truth physically accurate renderer in UE; switch in viewport via Lit → Path Tracer; all settings via Post Process Volume → search "Path"; Samples Per Pixel drives quality (10 for preview + denoiser, 500 for quality); spatial × temporal samples multiply in MRQ. Key UE4.27+ improvements: subsurface scattering, proper glass (caustics), frosted glass, thin translucent, emissive HDRI lighting. NOT real-time — for still renders and quality comparison against Lumen.

### Summary
26-minute William Faucher deep-dive on the UE4.27 Path Tracer (remains fully applicable to UE5). Covers: what Path Tracing is (ground truth, physically accurate; compares to V-Ray/Arnold); enabling (DirectX12 + Ray Tracing project setting); switching on in viewport; Samples Per Pixel vs denoiser trade-off (low samples = denoiser destroys fine detail); progress bar console command; max bounces (7 typical, ≥10 for glass); filter width; emissive HDRI lighting (no skylight needed); material support — subsurface scattering, glass (caustics), frosted glass, thin translucent; skylight limitation (no volumetric clouds; fix: Real-time Capture + cube map resolution 1024); MRQ setup (spatial × temporal samples multiply; override AA to None; delete Deferred Rendering, add Path Tracer tab); recommended settings (16 spatial × 16 temporal, NO denoiser — denoise in post in DaVinci Resolve instead).

### Key Steps
**Enable Path Tracer:**
1. Edit → Project Settings → Platforms → Windows → Default RHI: **DirectX 12**
2. Details panel search: **Ray Tracing** → enable; accept Support Compute Skin Cache prompt
3. Restart engine

**Activate in viewport:**
- Click **Lit** dropdown → **Path Tracer** → scene begins accumulating samples progressively

**Key settings (Post Process Volume → search "Path"):**
- **Samples Per Pixel**: default 16,384 (slow); set to 10-100 for preview; 500+ for quality
- **Denoiser**: toggle; aggressive at low sample counts (destroys fine detail); disable for final renders
- **Max Bounces**: 7 recommended for general use; 10+ required for glass/refractive materials; each bounce adds indirect light
- **Filter Width**: anti-aliasing filter; lower = sharper/more aliased; higher = softer
- **Emissive Materials**: toggle; enables emissive textures (HDRI) to cast light; useful for HDRI-only lighting without skylight

**Progress bar console command:**
- `r.PathTracing.ProgressDisplay 1` → shows render progress bar at bottom of viewport

**Skylight fix for volumetric clouds:**
- Select Skylight → set to **Real-time Capture** → set **Cube Map Resolution** to 1024 (or higher) → captures sky into cubemap usable by Path Tracer

**HDRI alternatives:**
- HDRI Backdrop actor: place in scene → disable its associated Skylight to avoid double-lighting
- OR: Skylight → Source Type: **SLS Specified Cube Map** → select HDRI cubemap

**MRQ setup for Path Tracer renders:**
1. Open MRQ → Settings
2. Add **Anti-Aliasing** tab:
   - Spatial Sample Count: divide total target samples by temporal count (e.g., 100 spatial × 5 temporal = 500 total)
   - Temporal Sample Count: drives motion blur quality (5-16 recommended)
   - Override AA → **None**
3. Delete **Deferred Rendering** tab
4. Add **Path Tracer** tab (same settings as Deferred; replaces render method)
5. Hit Render

**Recommended settings:**
- 16 spatial × 16 temporal = 256 total samples per pixel
- Denoiser: **OFF** — denoise in post (DaVinci Resolve, Nuke) for more control and less detail loss
- Albedo values: keep below 0.8 (no pure-white materials; improves render performance)

### UE Systems / Blueprints / Settings
- **Path Tracer** — ground-truth physically based renderer; viewport Lit dropdown → Path Tracer; requires DX12 + Ray Tracing enabled; not real-time; accumulates progressively
- **Samples Per Pixel (Post Process Volume)** — controls render quality; low = fast + noisy; high = slow + clean; multiplied by temporal in MRQ
- **Denoiser (Path Tracer)** — aggressive; destroys fine detail at low samples; non-temporal (causes flicker in animation); disable for final renders; denoise in post instead
- **Max Bounces** — number of light bounces; 7 for general use; 10+ for glass/refractive materials; diminishing returns beyond 12-15
- **Emissive Materials toggle** — allows emissive textures to contribute lighting; enables HDRI-only lighting without any skylight or directional lights
- **`r.PathTracing.ProgressDisplay 1`** — console command; shows render progress bar in viewport
- **Skylight Real-time Capture** — captures current sky (including volumetric clouds) into cubemap; workaround for path tracer not supporting volumetric clouds natively; set Cube Map Resolution 1024+
- **HDRI Backdrop plugin** — place actor in scene; emissive HDRI lights scene; disable associated skylight to avoid double-lighting
- **MRQ Path Tracer tab** — add in MRQ settings to switch render method to path tracer; remove Deferred Rendering tab; samples controlled by AA tab (not PPV)
- **Temporal Sample Count (MRQ)** — multiplies with spatial samples; improves motion blur; 5-16 recommended
- **Glass material setup** — Blend Mode: Translucent; Lighting Mode: Surface Forward Shading; Roughness: 0 (clear) or >0 (frosted); IOR: 1.5; requires ≥10 bounces
- **Thin Translucent material** — Blend Mode: Translucent; Shading Model: Thin Translucent; add Thin Translucent Material Output node; shadow/material color from that node; use for plastic wrap/bubbles (not glass)
- **Subsurface Scattering** — supported in Path Tracer since UE4.27; Shading Model: Subsurface; random walk method; no plugins needed

**Limitations (UE4.27 era, some addressed in UE5):**
- Hair strands: not supported
- Cascade particle systems: not supported
- Spline meshes: not supported
- Decals: not supported
- Volumetric/exponential height fog: not supported
- Light functions: not supported
- Single layer water: not supported
- No multi-GPU support
- Depth of field: uses regular PP DOF (not path-traced); some jitter at extreme settings

### Difficulty
Intermediate. Enabling is straightforward. Understanding sample counts, denoiser trade-offs, and MRQ setup for animation requires experience. MRQ spatial × temporal math is a key concept.

### UE Version
UE4.27+ (originally released UE4.27; all features apply to UE5; some limitations resolved across UE5.x versions)

### Tags
path-tracer, rendering, ray-tracing, mrq, materials, glass, subsurface-scattering, denoiser, samples, lighting

---

## Related Entries
- `lumen-explained---important-tips-for-ue5.md` — Lumen real-time GI; use Path Tracer to validate/compare against Lumen approximations
- `lighting-in-unreal-engine-5-for-beginners.md` — Lumen lighting setup; Path Tracer is the quality benchmark for comparing
- `the-2025-guide-to-rendering-in-unreal-engine-5.md` — broader rendering overview; Path Tracer as one of the render modes covered
- `make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta.md` — MRQ basics; Path Tracer as alternative render output method
