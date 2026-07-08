---
title: Introducing EasyWaterscape for Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=dXuwb4PpodQ
author: William Faucher
ingested: 2026-07-08
ue_version: "[PENDING]"
tags: []
extraction_status: needs-review
frames_dir: tutorials/frames/introducing-easywaterscape-for-unreal-engine-5/
frame_count: 21
---

# Introducing EasyWaterscape for Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=dXuwb4PpodQ)
**Author:** William Faucher
**Duration:** 25m7s | 21 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Easy Water Escape is the must-have tool for adding realistic, tile-free water to your  world from complex to rough seas. Drop it into your level, pick a presets and you're ready to  art direct from there. Now, there's a lot of water tools in that right now, so how is this  one any different? My whole design philosophy is to keep things clean, tidy, and as user-friendly as  possible at an affordable price compared to similar tools on the market. Everything run from a single  organized blueprint, presets to get you started, buoyancy, dynamic surface detail, and a  coastmaker that handles your shorelines automatically. It is optimized for games, not just cinematics,  and I provide example level for you to learn from. I might be a little biased, but I really think  it's the cleanest water tool in the market and by far the easiest to use and get great results with.  You'll find Easy Water Escape on Fab linked down below. Also, be sure to follow me on social media  to keep up the date with all of the new features coming later. Let's get right to it! Let me show you  why it belongs in your toolbox and how to use it. Okay, let's start with the basics. To use

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_000.jpg

### Getting Started with the Details Panel [1:26]
**Transcript:** Easy Water Escape, download it on Fab and add it directly to your project. From here, navigate to  the blueprint folder here, try get into your level, and in the details panel under the 0-1 Easy Water  tab, click Run Easy Water. When you want to stop it, just click Stop Easy Water. Everything you  need lives right here. Easy Water, Coastmaker, Optimization and Troubleshooting,  and there's two features in beta, Underwater and Lake Mode. Right here, you have two buttons.  One sends you directly to my Discord server for questions and support. The other sends you  directly to this video, making it easier than ever to find the help that you need. Don't be intimidated.  It looks like there's a whole ton of settings, and that can be scary, but don't worry. Every single  variable here is clearly labeled with a descriptive tooltip telling you exactly what it does.  One of my biggest pet peeves is when a developer is too lazy to add descriptions. I shouldn't have  to dig through tutorials or tedious documentation just to figure out what one slider does, and neither  should you. You deserve better. And one thing, worth clearing up early, the only time you'll ever  have to dive into the material is for the more advanced parameters. I've exposed all of the important  stuff in the blueprint. And when you do go in there, anything controlled by the blueprint is  clearly labeled with a BP suffix, so you know it's already handled. Everything else can be edited  in the material, but in most cases you won't need to. I also made sure to provide example levels  that you can find here to get you started. These won't be kept up to date as new features are added.  Moving on, the easy water section here is where you will spend most of your time. Everything you need  as exposed here is where you will sign your water mesh with five included LEDs.  LED zero and one are really for cinematics. They're very dense. And in fact, LED zero is completely  overkill and ridiculous, but it is therefore the high-end cinematic people.  LEDs 2 through 4 are much more game friendly. Next, we have presets.

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_001.jpg

### PRESETS! [3:22]
**Transcript:** No water system is complete without presets to work from. Just click the drop down menu here  and pick the one you want. Important workflow tip. When you do have an active preset,  the blueprint settings are locked. To make further changes from there, click to remove the preset  and that unlocks the settings, so you can continue to adjust to your taste.  So if you're playing around with the settings and you know nothing is happening, double check  that you don't have a preset enabled. Switching over to the optimization and troubleshooting tab real quick,  that is where we control the frame rate and the resolution of our ocean. These are the  two main dials that you'll use to balance the quality and performance. We'll dive into the  specific later. Let me walk you through some of the main controls for tweaking the look of your

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_002.jpg

### Main Controls [4:05]
**Transcript:** water. Wind speed and fetch are what you'll use to adjust the size, energy and frequency of your  waves. The higher the wind speed, the larger the waves. Same as fetch. Amplitude, height and  normals are fairly self-explanatory. Amplitude affects both vertical and horizontal displacement,  where at height, we'll only affect the vertical displacement and normal strength as a result.  And normals affect the normals. Pro tip, very often the water will look a little better.  When you tone down the normal intensity to 0.75 or even 0.5, try it out and see.  Choppiness affects how sharp the crest of your wave will be and how the direct impact on how  much foam is generated. We will get into that soon. Over here, you can adjust the wind direction,  with one slider. But you can also control with this handy little gizmo if you prefer a more  visual indication. My favorite feature of this entire tool is the wave directionality.  By cranking up that slider, our wave go from omnidirectional to fully directional,  giving you a much more natural look. I'm not a huge fan of omnidirectional waves in general,  so I think the best range between 0.75 and 0.95, this works in tandem with wave spread.  That is how you get those longer, straighter waves. For a spread to work, you need a wave  directionality value closer to 1, otherwise it will not have very much effect.  From there, you can adjust how fast they travel with the wave speed.  Next up, patch size and tiling scale. These two also work together. Patch size is basically how  large an area of ocean you are capturing and have a big impact on how well everything tiles.  Raise the patch size and you capture more waves over a larger area. But each wave end up at a  lower resolution, which can be offset by upping the resolution. Lower the value and each wave gets  bigger, more detailed, but tiling becomes a huge problem. Let me exaggerate the value to give  us a worst case scenario. This looks awful. And that seg waves into the tile breaking section.

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_003.jpg

### Tile Breaking [6:10]
**Transcript:** So what we do is we set the offset to minus 1,500 and the blend range also to 1,500.  And just like that, we massively mitigated that horrible tiling. It isn't perfect, but remember,  this is an absolute worst case scenario. Leaving these and patch size at default is usually a good  starting point. You can also adjust the cell size to adjust that breakup a little bit more to,  depending on your water surface and the size of the waves. Sometimes that can use some tweaking.  Now, if your water is very smooth with not much detail, you may notice the cell bombing pattern  here when the camera is really high up. I'm aware of it. I don't want to keep it from you. It is not  noticeable under a normal ocean, but it can show up. This is on the top of my roadmap priority,  and will be replaced with a newer, better tile breaking system in the near future. That should be

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_004.jpg

### Foam Controls [7:04]
**Transcript:** truly seamless. Next up, foam. Let's hope that the foam example level and run water.  You often see foam in other water tools just spawn foam out of nowhere, randomly, and that's  not how foam works. Whitewater forms when a wave gets too steep, it topples over, and traps air  as it collapses. That is the whitewater, those trapped bubbles. This is probably the part that I am  most proud of in this tool. It feels like the waves themselves are generating the whitewater,  and it leaves a nice trail behind it. Foam is primarily affected by wave choppiness here.  The higher the choppiness value, the more foam shows up. This is how real waves behave,  but of course, sometimes you may want really choppy waves without the foam. Here in the Open  Ocean tab is where we go to set that. Foam intensity, how visible do you want it to be?  Foam threshold, higher values limit the foam to the tip of the crests. Lower values give you a much  more diffused look. Choppiness limiter here is essentially a divider to offset the effect of chop  without affecting the wave itself. These two settings are the main  dials you'll have to balance. There's no magical settings, it all depends on how strong your  choppiness and amplitude values are. Decay here is how long the foam remains visible. Low values  make the foam fade quickly. Valued closer to one, make it linger for a very long time.  Smoothing will reduce the sharpness of the foam edge. This one is especially handy if you are using  a very high resolution water. Let me show you what I mean. If I set my water to 4k here,  we'll see the way the detail here looks deliciously crispy and looks amazing. This had a direct  effect on the detail of the foam. But maybe you feel that detail is too sharp, too noisy, too busy.  You can soften that look by upping that value. If it helps, our direction feature.  I'll admit, this is probably the trickiest part of this whole tool to really wrap your head  around. There's a lot of settings here, but fiddle with the values a bit and you will get the  hang of it. Eventually, I want to simplify this process a bit. There's maybe one or two dials,  too many, but in this specific situation, I opted for better control over simplicity. Now,  you'll see we have the open ocean and coast under the foam sub menu. Adjusting the coast  sliders won't do anything yet because we haven't generated our coast. And that's like we  is right into the built-in coastmaker tool. Let's open the coastmaker example level. Everything's

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_005.jpg

### CoastMaker [9:26]
**Transcript:** already placed for you. So you just run easy water, head over to the coastmaker tab and click  coastmaker. Right away, you'll see waves and foam all around your coastline.  Coastmaker captures all the land within this bounding box right here, which you can place wherever  you want and resize with the coverage slider, followed by adjusting the resolution of the maps it  generates. It runs automatically at runtime, but only once, so there's no performance impact after  the game starts. Of course, you can tell it not to run at all if you don't need it. And clear  coastmaker just wipes the bake data, which is helpful if you're switching between levels and the  previous bake is showing up in your water here. Now, back in the foam section, the coast foam has  the exact same settings as the open ocean, intensity threshold, decay, and so on. This works really  well for rocky coasts. It's nice to have coast foam and ocean foam decoupled. For the coast waves,  let's jump back into coastmaker and under the coastline section is where we control the waves  themselves, intensity, amount, speed, breaking foam, all of it, play around those settings.  As you adjust the size of the capture area or change the resolution, the waves might start to  look a little odd or different. The variable to reach for our distortion, distance from shore,  and wave amount. Since they are all tied to the resolution and size of the coastmaker texture,  if you cram, for example, 50 waves into 5 meters, each one's going to look a little weird,  right? So you need to spread it out and are directed for your level. There is no one size  fits all here. And now that the new mesh terrain features in 5.8 are here, if your landscape has  overhang or caves, lower the capture height Z to a point below that overhang, otherwise it will  capture the top of the landscape, and that's no good. But also, if you place a static mesh in your  scene and you don't want it to show up around it, select your mesh, search for scene capture,  and tick hidden in scene capture. We also have an advanced hub here. In general, I advise against  touching these, but there is one example where it does help. In very tight areas or place it with  a small bay, waves coming in like this looks pretty bad. So these settings will blur out our maps  to smooth it. Raise these values a fair bit, hit coastmaker again, and now the waves come in  much more naturally. One more tips, notice we've got waves and foam coming in from all sides.  Because our ocean has a directionality to it, coast waves and foam coming in from the opposite  direction looks weird. So I added a windward mask for the coast waves and foam, which make them  only appear in the direction the wind is coming from. Essentially sheltering the opposite side of  your island. I made use of that feature in this shot here, which makes it feel a whole lot more  real and natural. Now I want to be completely transparent. The shoreline waves and the way they  crash on beaches is honestly the weakest part of this entire tool. It doesn't look the best,  and I'm not going to hide it from you. It works a little less well with those long,  breaking waves over shallow shorelines, the kind you see at beaches where easy waterscape  really shines though its environments with steeper cliffs. Places where water crashes directly  against rocks, like what you're seeing here. Included for free is a Niagara system that  generates splashes for a pretty convincing effect from a distance. Improved shoreline waves are  absolutely in the works, something I will be adding in a future version update. We've got three

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_006.jpg

### Surface Details [13:02]
**Transcript:** more categories here in the detailed panel. Swells, Currents, and Windgun. These are extra detailed  that add a layer realism to your water. Swells add a large scale wave pattern in the distance,  which you can adjust right here. I've also included three different normal maps that you can  plug in. They're labeled as such, each one giving you a completely different look to choose from.  See Currents add that kind of swirly breakout pattern that you see on real oceans,  and the feature I'm really glad to have added. It's all noise-based, so you won't get any  tiling, but I'm not using 3D noise, which keeps it relatively cheap. I expose a whole bunch of  controls so you can really fine-tune exactly how it looks. In my opinion, adds a really nice level  of polish and realism that you just don't often see in water systems. And lastly, Windguests add,  well, Windguests. Just one more realism feature I wanted to include. One that breaks up the repetitive  nature of water and literally breathes life into your environment. Stack all three and your water  stops looking like a repeating texture and feels alive. Easy water offers three different types of

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_007.jpg

### Buoyancy [14:06]
**Transcript:** buoyancy as well. Each with their own pros and cons, first and the cheapest, but lowest  visual quality, is the material function. You can slap it onto any material connected to the world  position offset pin, and it'll fake buoyancy by sampling the waves of the ocean. But  bear in mind, there's no actual physics involved here, so it looks, you know, bad. That said,  it worked great for a simple movement in the background. Next, we have the Niagara Blueprint.  You drop it into your level, assign a static measure to your choice. You can choose how many  objects you spawn, their radius, their scale, their scale variation. Perfect. For a scattering,  a bunch of degree, your floating rebel on the water. This isn't the one you should be using most of  the time. It is highly performant, runs on the GPU, the buoyancy looks great, and if you ever  notice something not lining up or being a little floaty, no pun intended. Just nudge it and it'll  snap right into place. Lastly, they're the Blueprint component that you can assign to just about  anything, a static mesh, an animation blueprint, a camera, whatever. This is the ideal for a hero  object that needs logic or gameplay mechanics. It behaves the same way as the Niagara Blueprint,  the same controls exposed. Just select your actor, click Add Component, and search for Easywater  in the list here. Make sure your object is set to removable. To see how it looks, jump into  the Pi mode or simulate in Editor, there's a take rate limit for performance. Just be aware it has  an immediate impact on how things look, at least you have the option to lower it if you need to.  This is probably the part that will get the most feedback, and that is by design. I want to build  out the buoyancy system together with you so I could use some feedback on what your project needs.

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_008.jpg

### BETA Features (Underwater & Lake Mode) [15:49]
**Transcript:** Next, I have two features that are in beta. I want a version 1.0 to ship with an underwater  option because for a lot of shots, it's kind of essential, so it's in there. It's the most  early stage feature in the tool, and I'll be building it out a lot, adding God rays,  particularly matter bubbles, distortion. So think of this as the foundation, there's plenty more  coming. Lake mode is for when you don't want an endless ocean, stretching out to horizon. It lets  you shape and rotate your water to sit exactly where you need it. Just take the Lake mode checkbox  and adjust it from there. It's still maturing, I'll make it a lot more robust and efficient  deadline, and remember, if you'd rather use your own mesh, you can load a custom one right here

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_009.jpg

### Custom Mesh/Water Plane [16:28]
**Transcript:** and disable camera follow here, giving you a water plane that is exactly what you need and where  you need it. Included is a material function that adds wetness and darkening around the base of

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_010.jpg

### Wetness Material Function [16:38]
**Transcript:** your meshes right along the coastline. You read the exact water level, so it always lines up.  All you have to do is add this material function to your master material. It supports both material  attributes and regular pins. You just designate which one with a static boolean here.  Once you've compiled your master material, in this case I applied it to my Megascans master material,  every Megascans asset now has this wetness applied to it. Open up the material instance of your choice,  and you'll find a wetness variable ready for you to adjust on a per material basis.

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_011.jpg

### Single Layer Water vs. Default Lit [17:17]
**Transcript:** Single air water is the de facto standard for rendering water in Unreal Engine. It looks  amazing. You get translucency, caustics, but it does come with a few drawbacks, for example,  it won't cast or receive shadows from any light other than your primary directional light.  Most of the time, that's totally okay, but in some situation like this here, where you want more  dramatic lighting, it just won't work. This shot would primarily lit with one spotlight.  And because there's no shadows being cast by this rock here, the whole illusion just falls apart.  That is when switching over to default lit. In shots where you don't actually need translucency,  can work way better. In this one, I also set the metallic value to one to make it look better.  See here, the water in my reference is just kind of dark and deep, and that is exactly the kind of  look that lets us get away with default lit. To switch it, open up your easy water scape material  instance, search for a shading model, and change it over here. There is no one is better than the other,  it always depends on your shot and what you need. There are pros and cons to both. Work mentioning,  you can control your water surface values for both the default lit and single layer water,  right here. I made sure it's as easy as possible for people to optimize and fix things easily.

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_012.jpg

### Performance & Optimizations [18:35]
**Transcript:** In this tab here, you'll find a few checkboxes that can help you out in some situations.  In a material instance itself, I added a dedicated optimization section where you can quickly find and  disable features like swells, currents, coast waves, two or drop your instruction count when you  need it. I deliberately put every toggle in one place rather than scattered across each category,  so you're not dancing around the groups hunting for them. As I talked about in the beginning of  the video, resolution and frame rate are the main dials for balancing performance and quality.  You're going to want to keep the frame rate as low as you can get away with. You would be surprised  how low it can go before you notice, especially if your camera is far away from the water.  For aerial shots, sometimes even 10 to 15 works. This will have a tremendous performance boost for  you. For revolution, 4k looks amazing, but in most cases, even I find it to be a bit overkill.  256 to 2048 is usually the range that I work with. If you're not using the underwater feature at all,  I recommend disabling it, and in the material instance, setting two sided to false, it recommended.  There is no need to render two sided if you don't need it. The water mesh itself up here does have  quite an impact on performance. There is very little visual difference between LOD 0 and LOD 1.  2 to 4 is recommended for games. In fact, LOD 4 is maybe a bit excessively low and does have the  occasional artifacts depending on your wave size. For an additional performance boost,  if you don't need the coastline foam or even the open ocean foam, you can disable both checkboxes  Let me take a moment to walk you through some handy good things to know when using easy water

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_013.jpg

### Handy Tips [20:16]
**Transcript:** skate. A few bugs, known artifacts, and how to deal with them. If you're using hardware  accelerator lumen or if you're not using lumen at all, you'll be fine red on the box.  But if you disable things like reflection screen traces, you might run into these weird black  artifacts for worse, this kind of thing. Don't worry, it's an easy fix. One, we just need to  disable, evaluate and ray tracing. And then you'll see this horrible thing, just apply the lumen  offset fix. To push the height above 0 so there's no negative displacement values, I do recommend  using screen traces when possible, as you can see here the results are a lot better. Ghosting,

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_014.jpg

### TSR Smearing/Pixelation [20:58]
**Transcript:** smearing, pixelated water, it caused by temporal super resolution, or TSR, the anti aliasing,  and it's a major complaint from just about anyone who uses Unreal. Here's the thing.  Easy water can look really good even with TSR. The real issue is that your viewport is lying to you.  It's not native resolution. It's probably sitting somewhere between 80% and 90% screen percentage,  rarely 100%. That means it is upscaling and what makes the water look so bad. It is entirely TSR  at fault. Set it to 100% here, and you'll see the result look way better. Push it to 125 or even  200% and it'll be tack sharp. Now, I know that's not a realistic option for everyone, so  fortunately you can change the AA method itself. Use this console variable, or if you're using  easy tool bag, you can toggle it here. And you'll see there are five other AA methods to choose from.  You can also use the tomepper sharpen variable here, as 0.5 or 1 to clean up the smearing a little  more. Every little bit helps. So, bottom line avoid any kind of upscaling if you can.  If you see this kind of popping effect of runtime, that's because you need to  click stop easy water before you render or play. And for the cinematics people among you,

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_015.jpg

### Movie Render Queue settings for Cinematics [22:17]
**Transcript:** there's one thing you really need to know. Due to the way that the water is generated,  you determine the frame rate. How often the water takes forward every second. If you set it to  your target frame rate, let's say 24 FPS, you won't get any motion blur between frames,  even with temporal samples. Your wave will look choppy and not in a good way. Instead, you'll want to  set this to at least at least five to ten times your actual rendered frame rate. That way,  you get sampling in between the frames, which gives you nice, smooth motion blur on your waves.

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_016.jpg

### Performance Benchmarks [22:47]
**Transcript:** Many of you will want to know how easy water skate performs, so here are the benchmark results for  two GPUs. A 1590 and a 3080 Ti, which is over five years old now. The benchmark settings are very  much middle to road, so there's wiggle room on both sides, whether you want to optimize even more or  crank the quality up higher. As we've covered throughout this video, you've got tons of dials to  fine tune in the performance, the quality ratio for your project. Of course, that can vary based on  things out of my control, like whether you use lumen or reflection quality, lighting quality,  and so on. Now, you might have heard that blueprints will be deprecated sometimes after

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_017.jpg

### Blueprints & Unreal Engine 6 [23:20]
**Transcript:** unreleension six comes out. And yeah, that is unfortunate, but it is not as bad as it sounds.  First, the full launch of UE6 is not for another two to three years, and two, Epic has stated that  once the new framework has matured enough, only then will blueprints be deprecated, and they will  provide tools for migrating to the new architecture. So we're looking at roughly half a decade in the  future here, if not longer. So what does this mean for you? Nothing, UE5 and blueprints are still  going to be highly relevant for the next five years, at least. I pledged to keep developing  Easy WaterScape, and once UE6 comes out, it will be migrated over and continue working unexpected.  Easy WaterScape is a result of months of work, if the most complex tool I've ever built in UE5 so far,  and realistically, there are things I've missed, or I didn't notice. So help me help you.  If you hit a bug, post it in Discord, and you have my word, I'll fix it as fast as I can.

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_018.jpg

### Roadmap Poll [24:21]
**Transcript:** One last thing, down below is a link to a poll where you can vote on which roadmap features you are  most excited to see. Your input will genuinely shape where this goes. And that covered using  Easy WaterScape. You can find it on FAB, link down below. I hope you found it video helpful.  Remember to join the Discord server for support, questions, discussions. Thank you so much for  watching, and as always, folks. Happy rendering.

**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_019.jpg

### Bloopers [24:46]
**Frame:** tutorials\frames\introducing-easywaterscape-for-unreal-engine-5\frame_020.jpg


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
