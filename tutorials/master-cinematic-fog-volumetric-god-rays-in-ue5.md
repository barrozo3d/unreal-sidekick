---
title: Master Cinematic Fog & Volumetric God Rays in UE5
source: YouTube
url: https://www.youtube.com/watch?v=Kjg6kCW2BtY
author: Josh Toonen
ingested: 2026-06-18
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/master-cinematic-fog-volumetric-god-rays-in-ue5/
frame_count: 12
---

# Master Cinematic Fog & Volumetric God Rays in UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=Kjg6kCW2BtY)
**Author:** Josh Toonen
**Duration:** 17m43s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Why you need to use Volumetric Fog [0:00]
**Transcript:** In Unreal 5, why do I use volumetric fog in every single scene?  It's because volumetrics and fog are great tools to add depth to your renders.  And whether you realize it or not,  haze and fog are used every single day on set of your favorite Hollywood movies.  And now I hate this term, but a lot of people have asked me,  how do I make my shots look cinematic?  And this is one of those key elements that you need in your shots.  But if you come from old school VFX,  so that volumetrics come in really noisy and can take a really long time.  That's where Unreal comes with the rescue,  with fast, real-time volumetrics with zero noise.  And I'm not kidding.  But there's two big problems.  One is that the system is kind of hidden and spread out  between a bunch of different menus.  And number two, how do you art direct your volumetrics  to improve the lighting in your shot?  So today, you're going to learn the ins and outs of the volumetric fog system  in Unreal 5 and how to make your renders look like your favorite Hollywood movies.  What's up?  My name's Josh Tudor, and for the last eight years,  I've worked as an artist and supervisor on movies like Star Wars,  Dungeons & Dragons, an...

**Frame:** tutorials\frames\master-cinematic-fog-volumetric-god-rays-in-ue5\frame_000.jpg

### How to enable Volumetric Fog [1:31]
**Transcript:** This is one of the sample projects I've included  in my beginner's roadmap PDF  where you can find the best free sample projects  to download at every single skill level.  And this is one of my favorite projects  because it's a great intro into photorealism inside of Unreal Engine.  And I've gone ahead and converted this  from baked lighting to Lumen.  So first things first, let's press the Quick Add Actors icon here  and we'll go to the Visual Effects tab  and select Exponential Hide Fog  and just drag this into our scene.  And you're probably thinking,  well, this really didn't do anything in my scene.  So I probably want to increase the fog density.  So I'm going to set that to one  and it just kind of goes black.  Well, first off, that's because the fog in scattering color  is set to zero.  But you can see even when we raise that to one,  it doesn't really do what we'd expect it to do.  And this is because volumetric fog  is actually a completely different tool set inside of Unreal.  But it only exists and can be enabled  by having an exponential hide fog actor in your scene.  This is confusing at first, but just stay with me.  So I'm going to reset the fog density back to 0.02...

**Frame:** tutorials\frames\master-cinematic-fog-volumetric-god-rays-in-ue5\frame_001.jpg

### Add light blockers to shape your god rays [3:41]
**Transcript:** but it's getting a little bit blown out on screen left.  So what can we do to break up our fog?  Well, obviously you could just start throwing in  different cubes and planes  and let's start off with that.  What we can just make different blockers inside of our scene.  We can just move this  in just a few seconds.  We can start to block out whatever we don't like.  So just by tweaking that around here,  you can see, okay,  we have some pretty interesting shapes here.  But another way that I like to break up  different areas like this is by using a gobo.

**Frame:** tutorials\frames\master-cinematic-fog-volumetric-god-rays-in-ue5\frame_002.jpg

### How to Create Gobo Materials [4:13]
**Transcript:** So a gobo is also known as a cookie cutter.  It's a little stencil that you'll put in front  of a practical light fixture  to break up the shape and add some interesting shadows  from that light.  So we can do the same thing in CG.  So I'm going to create a brand new material really quick  and call it M underscore gobo.  And this is going to be extremely basic.  So I'm going to make this two sided.  And all I'm going to do is change our blend mode  from opaque to mask.  So now I'm going to bring in a texture sample here.  I'm going to plug this into our new opacity mask  and let's just search for noise.  There's a lot of default textures  that just come with the engine.  So we have this T noise 01.  So now if I preview this as a plane,  you can see this is our texture.  And it kind of resembles the idea of take gobo.  So let's save this out.  So now let's bring this into our scene.  Let's just create a plane, scale this up.  And we'll drag our gobo material onto it.  So now instead of using a giant cube to block out our light,  we can drag this through our scene  and be a bit more creative with how we want to cut out our light.  Now we move this out of view of the camera.  We can g...

**Frame:** tutorials\frames\master-cinematic-fog-volumetric-god-rays-in-ue5\frame_003.jpg

### Spotlights and Volumetric Fog [5:40]
**Transcript:** Let's take a closer look at that volumetric shadow.  Now this is really cool.  It gives us a nice swath of light.  It's not everywhere like we were getting  with our directional light.  But let's see what happens when we turn  Cats volumetric shadow on.  You can see it does start to cast these really nice God raise.  And now is we can kind of rotate this through our scene  or put it behind this different geometry.  It casts them really clean, the volumetric light.

**Frame:** tutorials\frames\master-cinematic-fog-volumetric-god-rays-in-ue5\frame_004.jpg

### How to Increase Render Quality [6:05]
**Transcript:** The right away people are going to freak out  because you can get some pixelated looking fog  at first.  Sometimes the quality is not quite there,  but it's actually really simple to adjust.  If you ever need to increase the quality settings  of your light rays,  you're going to have to use the command variables.  All you have to do is go to your output log  where you can enter in some command variables  and type in r.volumetric fog.rid pixel size.  So if we type in any command  and just throw in a question mark after it,  you can see what the setting currently is inside of the scene.  So here our grid pixel size is set to 16.  So how this works is all of the fog in the scene  is basically a grid of voxels or 3D pixels  where there's pixels going in x, y, and z.  So if you want to increase the resolution,  we actually want to make each one of our voxels smaller.  So we want to decrease this to increase the resolution.  So the smaller the size of each grid pixel,  the higher resolution we will have.  So if we type in r.volumetric fog.rid pixel size  and set this to 4,  this is going to give us a much, much cleaner result.  Now we can go even smaller than that.  We go all the way to ...

**Frame:** tutorials\frames\master-cinematic-fog-volumetric-god-rays-in-ue5\frame_005.jpg

### stat gpu profiling [7:18]
**Transcript:** If you're not careful,  this can really start to fry your GPU.  So if you're ever worried about pushing this too far,  if you just like been static GPU,  you'll get all of the different things  calculating in your scene at a given time.  And if we look here,  we can see it takes 0.27 milliseconds  to render volume magic fog in your scene.  So when you say it's real time,  it really is real time.  Let's increase our resolution here.  Let's set it to something like two,  which is very high resolution.  You'll see that this volumetric fog is going to start climbing up here.  It's become the most expensive thing inside of our scene.  It's actually going to take six milliseconds per frame,  which again, it's still much cheaper than any sort of offline renderer.  But if you have a lot of things going on,  a lot of lights that are casting shadows inside your scene,  it'll very quickly start to fry your GPU.  So I like to set this to four by default.  Usually this gives us a good trade off  between quality and performance.  And you can always increase this  inside of the movie render queue settings.

**Frame:** tutorials\frames\master-cinematic-fog-volumetric-god-rays-in-ue5\frame_006.jpg

### 4 Settings to Art Direct your Fog [8:17]
**Transcript:** So before we move on,  here are the last four settings you need to know  so that you can art direct your fog.  You can tint the albedo of your smoke,  although very quickly this starts to get  into an unrealistic territory.  So I almost never do this.  Typically it's going to be a much better idea  to just grade your footage after the facts.  And the same goes for extinction scale.  If you set this up higher,  it'll make your god rays more apparent.  But Epic has done a good job  of all these defaults being fairly true to life.  So the more you can keep close to the default values,  the more accurate your lighting is going to look.  But it is worth noting our exponential hype fog  setting haven't effect on our volumetric fog.  So we change the density here.  It's also going to change our volumetric fog.  And if we look at the fog hype fall off,  if we increase this,  it'll keep most of the fog localized towards the ground  for aesthetic reasons can look good.  But in the case of god rays,  they should be the brightest closest to the light source,  which is going to be towards the sky  and just be very intentional about when you want to change these  and get away from the default se...

**Frame:** tutorials\frames\master-cinematic-fog-volumetric-god-rays-in-ue5\frame_007.jpg

### Fog Materials [9:22]
**Transcript:** And now the last feature that I want to talk about  that I haven't really seen discussed elsewhere  is that you can actually have fog in your materials.  So I'm going to add this sphere into our scene  and right now it just has the default material.  But I've built this volume fog material  that if I apply here is actually going to change our sphere  into fog.  So depending on where I move this,  it's actually going to contribute  into our voxel grid of volumetric.  As we drag this sphere across our scene,  it's going to create localized fog.  We can make this really small  and keep it in these little pockets  or we can make it really big and fill up our scene.  So if you want to download this material  so you can just drag it into your own scenes  on put a download link for free in the description  on unrealforvidefacts.com.  Let me open up this material  and let's take a closer look.  So to create a fog and material,  instead of our default surface material domain,  we have to change it to a volume  and we're going to change the blend mode to additive.  This is going to give us the extinction option in our material  which changes how light will pass through our material.  So the ...

**Frame:** tutorials\frames\master-cinematic-fog-volumetric-god-rays-in-ue5\frame_008.jpg

### Improve your interior lighting [11:24]
**Transcript:** at last year's SIGRA,  where we had one hour to create an environment from nothing,  but Quixel Assets.  And I took advantage of the volumetric fog system.  So this entire scene is made from just four different Quixel Assets  and just trying to reuse them  and create an interesting composition  out of this parallel mirror dimension type world.  But let's take a closer look at how the volumetrics are set up.  But in this interior scene,  it's the same as we had before,  where we have this exponential height fog.  I left the fog density at 0.02,  and then if I look at any one of these spotlights,  you can see that I just cranked up  the volumetric scattering intensity to 10.  And looking back at this project,  one thing I didn't even realize  when you add a new spotlight into your scene,  the cast volumetric shadow is actually turned off by default.  So if you look through here,  if I just crank this volumetric scattering intensity,  it'll actually just clip through objects.  So when I bring this through our wall here,  we can see that it actually just clips right through,  but you have to check this to true  to make sure that everything calculates correctly.  Another thing worth not...

**Frame:** tutorials\frames\master-cinematic-fog-volumetric-god-rays-in-ue5\frame_009.jpg

### Render Volumetric Fog AOVs [13:35]
**Transcript:** so that you can composite them together  with some Hollywood level VFX techniques  that I'll show you in nuke in just a second.  So I have this scene from this Mr. Freeze short film  that I'm putting together.  And we have his wife Nora here  and the idea is to put her inside of this cryogenic ice chamber  but having materials that are refractive  like ice are really hard to get out of any render engine quickly.  So the fastest way in my opinion  is going to be rendering out a couple of different AOVs  so that we can assemble everything together in comp.  So I have my volume light here  that I can just toggle on and off.  So to render out our volumetrics,  I'm actually gonna have to render this out in three different passes.  The first one is gonna be just disabling  this volumetric light entirely.  So we're gonna just disable this from the scene  to make sure that a light doesn't show up inside of movie render queue.  You have to make sure that you uncheck either effects world or visible  just hiding it here in the outliner  is not going to hide it from a movie render queue render.  Yeah, I'm gonna render out with our path tracing settings here.  After that, I'm going to enable th...

**Frame:** tutorials\frames\master-cinematic-fog-volumetric-god-rays-in-ue5\frame_010.jpg

### Advanced Compositing Techniques in Nuke [15:35]
**Transcript:** Now we have our render here in Nuke.  I just went ahead and added a nice to focus to it  with a nice anamorphic kernel.  Now we have a photographic quality  to some of our spec hits and things like that.  But now let's go to our volumetric render.  So I'm just shuffling out our two passes,  our detail lighting and our lighting only passes.  And if we take a look at this,  our volumetric detail lighting pass,  it has our volumetrics,  but it also has the light that's cast onto our skin,  the diffuse lighting.  So the lighting only pass isolates that diffuse light on her  and through a really simple operation  of just subtracting this from the other.  So we're just taking this image and subtracting it  from our volume image.  We'll get a clean render where the volumetrics  are isolated by themselves.  And when compositing,  I always, always try to use live action footage  in one way or another.  So a really cool thing we can do is combine our volume metrics  with live action footage.  So I'm just multiplying this  by this lingering fog element.  So here I've imported my camera.  I've taken this video clip  and just put it on an image plane in 3D space  so that it tracks to the motion...

**Frame:** tutorials\frames\master-cinematic-fog-volumetric-god-rays-in-ue5\frame_011.jpg


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
