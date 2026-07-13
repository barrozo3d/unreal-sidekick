---
title: Introducing EasyWaterscape for Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=dXuwb4PpodQ
author: William Faucher
ingested: 2026-07-13
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/introducing-easywaterscape-for-unreal-engine-5/
frame_count: 0
frame_status: pending-selection
---

# Introducing EasyWaterscape for Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=dXuwb4PpodQ)
**Author:** William Faucher
**Duration:** 25m7s | 21 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py introducing-easywaterscape-for-unreal-engine-5 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Easy Water Escape is the must-have tool for adding realistic, tile-free water to your
[0:29] friend.
[0:50] run from a single organized blueprint, presets to get you started, buoyancy, dynamic surface
[0:55] detail, and a coastmaker that handles your shorelines automatically.
[0:59] It is optimized for games, not just cinematics, and I provide example level for you to learn
[1:03] from.
[1:04] I might be a little biased, but I really think it's the cleanest water tool in the market
[1:08] and by far, the easiest to use and get great results with.
[1:11] You'll find easy water escape on Fab, link down below.
[1:14] Also, be sure to follow me on social media to keep up the date with all of the new features
[1:18] coming later.
[1:19] Let's get right to it.
[1:20] Let me show you why it belongs in your toolbox and how to use it.
[1:25] Okay, let's start with the basics.


### Getting Started with the Details Panel [1:26]
**Transcript (timestamped):**
[1:27] To use Easy Water Escape, download it on Fab and add it directly to your project.
[1:32] From here, navigate to the blueprint folder here, try it into your level, and in the
[1:38] details panel under the 0-1 Easy Water tab, click Run Easy Water.
[1:42] When you want to stop it, just click Stop Easy Water.
[1:45] Everything you need lives right here.
[1:48] Easy Water, Coast Maker, Optimizations and troubleshooting, and there are two features
[1:51] in beta, underwater and lake mode.
[1:54] Right here, you have two buttons.
[1:56] One sends you directly to my Discord server for questions and support.
[2:00] The other sends you directly to this video, making it easier than ever to find the help
[2:05] that you need.
[2:06] Don't be intimidated.
[2:07] It looks like there's a whole ton of settings, and that can be scary, but don't worry.
[2:12] Every single variable here is clearly labeled with a descriptive tool tip telling you exactly
[2:17] what it does.
[2:18] One of my biggest pet peeves is when a developer is too lazy to add descriptions, I shouldn't
[2:23] have to dig through tutorials or tedious documentation just to figure out what one slider does, and
[2:28] neither should you.
[2:30] You deserve better.
[2:31] And one thing worth clearing up early, the only time you'll ever have to dive into the
[2:34] material is for the more advanced parameters.
[2:37] I've exposed all of the important stuff in the blueprint.
[2:41] And when you do go in there, anything controlled by the blueprint is clearly labeled with a
[2:44] BP suffix, so you know it's already handled.
[2:47] Everything else can be edited in the material, but in most cases you won't need to.
[2:52] I also made sure to provide example levels that you can find here to get you started.
[2:56] These won't be kept up to date as new features are added.
[2:59] Moving on, the easy water section here is where you will spend most of your time.
[3:03] Everything you need is exposed here, it's where you assign your water mesh, with five
[3:07] included LEDs, LED zero and one are really for a cinematics, they're very dense, and
[3:12] in fact, LED zero is completely overkill and ridiculous, but it is therefore the high
[3:18] end cinematic people.
[3:19] LODs 2 through 4 are much more game friendly.


### PRESETS! [3:22]
**Transcript (timestamped):**
[3:22] Next, we have presets.
[3:25] No water system is complete without presets to work from, just click the drop down menu
[3:29] here and pick the one you want.
[3:31] Important workflow tip, when you do have an active preset, the blueprint settings are
[3:36] locked.
[3:37] To make further changes from there, click to remove the preset, and that unlocks the
[3:42] settings, so you can continue to adjust to your taste.
[3:45] So if you're playing around with the settings and nothing is happening, double check that
[3:49] you don't have a preset enabled.
[3:51] Switching over to the optimization and troubleshooting tab real quick, that is where we control
[3:55] the frame rate and the resolution of our ocean.
[3:58] These are the two main dials that you'll use to balance the quality and performance.
[4:03] We'll dive into the specific later.


### Main Controls [4:05]
**Transcript (timestamped):**
[4:05] Let me walk you through some of the main controls for tweaking the look of your water.
[4:10] In speed and fetch, or what you'll use to adjust the size, energy, and frequency of
[4:14] your waves, the higher the wind speed, the larger the waves.
[4:18] Same as fetch.
[4:20] Amplitude, height, and normals are fairly self-explanatory.
[4:24] Amplitude affects both vertical and horizontal displacement, whereas height will only affect
[4:29] the vertical displacement and normal strength as a result.
[4:33] And normals affect the normals.
[4:35] Pro tip, very often the water will look a little better.
[4:38] When you tone down the normal intensity to 0.75 or even 0.5, try it out and see.
[4:46] Choppiness affects how sharp the crest of your wave will be and have a direct impact
[4:49] on how much foam is generated.
[4:51] We will get into that soon.
[4:53] Over here, you can adjust the wind direction with one slider.
[4:58] But you can also control with this handy little gizmo if you prefer a more visual indication.
[5:03] My favorite feature of this entire tool is the wave directionality.
[5:07] By cranking up that slider, our waves go from omnidirectional to fully directional,
[5:13] giving you a much more natural look.
[5:15] I'm not a huge fan of omnidirectional waves in general, so I think the best range between
[5:20] 0.75 and 0.95, this works in tandem with wave spread.
[5:25] That is how you get those longer, straighter waves.
[5:28] For a spread to work, you need a wave directionality value closer to one, otherwise it will not
[5:33] have very much effect.
[5:35] From there, you can adjust how fast they travel with the wave speed.
[5:39] Next up, patch size and tiling scale.
[5:42] These two also work together.
[5:44] Patch size is basically how large an area of ocean you are capturing and have a big impact
[5:48] on how well everything tiles.
[5:50] Raise the patch size and you capture more waves over a larger area.
[5:54] But each wave ends up at a lower resolution, which can be offset by upping the resolution.
[5:59] Lower the value and each wave gets bigger, more detailed, but tiling becomes a huge problem.
[6:05] Let me exaggerate the value to give us a worst case scenario.
[6:08] This looks awful.


### Tile Breaking [6:10]
**Transcript (timestamped):**
[6:11] And that segues into the tile breaking section.
[6:14] So what we do is we set the offset to minus 1,500 and the blend range also to 1,500.
[6:20] And just like that, we massively mitigated that horrible tiling.
[6:24] It isn't perfect, but remember, this is an absolute worst case scenario.
[6:28] Leaving these and patch size at default is usually a good starting point.
[6:32] You can also adjust the cell size to adjust that breakup a little bit more to,
[6:36] depending on your water surface and the size of the waves.
[6:39] Sometimes that can use some tweaking.
[6:43] Now if your water is very smooth with not much detail,
[6:46] you may notice the cell bombing pattern here when the camera is really high up.
[6:51] I'm aware of it.
[6:51] I don't want to keep this from you.
[6:53] It is not noticeable under a normal ocean, but it can show up.
[6:57] This is on the top of my roadmap priority and will be replaced with a newer,
[7:01] better tile breaking system in the near future.


### Foam Controls [7:04]
**Transcript (timestamped):**
[7:04] That should be truly seamless.
[7:06] Next up, foam.
[7:08] Let's open up the foam example level and run water.
[7:11] You often see foam in other water tools.
[7:13] Just spawn foam out of nowhere randomly.
[7:16] And that's not how foam works.
[7:18] Whitewater forms when a wave gets too steep,
[7:20] it topples over and traps air as it collapses.
[7:23] That is the whitewater, those trapped bubbles.
[7:26] This is probably the part that I am most proud of in this tool.
[7:29] It feels like the waves themselves are generating the whitewater
[7:31] and it leaves a nice trail behind it.
[7:34] Foam is primarily affected by wave choppiness here.
[7:37] The higher the choppiness value, the more foam shows up.
[7:40] This is how real waves behave.
[7:42] But of course, sometimes you may want really choppy waves without the foam.
[7:46] And here in the open ocean tab is where we go to set that.
[7:50] So foam intensity, how visible do you want it to be?
[7:54] Yeah.
[7:55] Foam threshold, higher values limit the foam to the tip of the crests.
[7:59] Lower values give you a much more diffuse look.
[8:02] Choppiness limiter here is essentially a divider
[8:05] to offset the effect of chop without affecting the wave itself.
[8:08] These two settings are the main dials you'll have to balance.
[8:11] There's no magical settings.
[8:13] It all depends on how strong your choppiness and amplitude values are.
[8:17] Decay here is how long the foam remains visible.
[8:20] Low values make the foam fade quickly.
[8:22] Fowl the closer to one, make it linger for a very long time.
[8:26] Smoothing will reduce the sharpness of the foam edge.
[8:29] This one is especially handy if you are using a very high resolution water.
[8:34] Let me show you what I mean.
[8:35] If I set my water to 4k here, we'll see the wave detail here looks deliciously crispy
[8:39] and looks amazing.
[8:40] This had a direct effect on the detail of the foam.
[8:43] But maybe you feel that detail is too sharp, too noisy, too busy.
[8:48] You can soften that look by upping that value.
[8:51] Make the helpful art direction feature.
[8:54] I'll admit, this is probably the trickiest part of this whole tool to really wrap your
[8:58] head around.
[8:59] There's a lot of settings here, but fiddle with the values a bit and you will get the
[9:02] hang of it.
[9:03] Eventually, I want to simplify this process a bit.
[9:06] There's maybe one or two dials too many, but in this specific situation, I opted for
[9:12] better control over simplicity.
[9:15] Now, you'll see we have the open ocean and coast under the foam submenu.
[9:20] Starting the coast sliders won't do anything yet because we haven't generated our coast.
[9:24] And that's the way it's right into the built in coastmaker tool.


### CoastMaker [9:26]
**Transcript (timestamped):**
[9:27] Let's open the coastmaker example level.
[9:30] Everything's already placed for you.
[9:31] You just run into water, head over to the coastmaker tab and click coastmaker.
[9:36] Right away, you'll see waves and foam all around your coastline.
[9:40] Coastmaker captures all the land within this bounding box right here, which you can
[9:44] place wherever you want and resize with the coverage slider.
[9:48] All of by adjusting the resolution of the maps it generates.
[9:52] It runs automatically at runtime, but only once, so there's no performance impact after
[9:55] the game starts.
[9:57] Of course, you can tell it not to run at all if you don't need it.
[10:00] And clear coastmaker just wipes the bake data, which is helpful if you're switching between
[10:05] levels and the previous bake is showing up in your water here.
[10:09] Now back in the foam section, the coast foam has the exact same settings as the open ocean,
[10:14] intensity threshold, decay, and so on.
[10:17] This works really well for rocky coasts.
[10:20] If nice to have coast foam and ocean foam decoupled for the coast waves, let's jump back into
[10:25] coastmaker and under the coastline section is where we control the waves themselves, intensity,
[10:31] amount, speed, breaking foam, all of it, play around those settings.
[10:36] As you adjust the side of the capture area or change the resolution, the waves might start
[10:42] to look a little odd or different.
[10:44] The variable to reach for our distortion, distance from shore, and wave amount.
[10:48] Since they are all tied to the resolution inside of the coastmaker texture, if you cram,
[10:53] for example, 50 waves into 5 meters, each one's going to look a little weird, right?
[10:58] So you need to spread it out and are directed for your level.
[11:02] There is no one side fits all here.
[11:05] And now that the new mesh terrain features in 5.8 are here, if your landscape has overhang
[11:10] or caves, lower the capture height Z to a point below that
[11:14] overhang, otherwise it will capture the top of the landscape.
[11:17] And that's no good.
[11:19] But also, if you place a static mesh in your scene and you don't want it to show up around
[11:23] it, select your mesh, search for scene capture, and tick hidden in scene capture.
[11:31] We also have an advanced hub here.
[11:33] In general, I advise against touching these, but there is one example where it does help.
[11:38] In very tight areas or places with a small bay, waves coming in like this looks pretty
[11:43] bad.
[11:44] So these settings will blur out our maps to smooth it.
[11:48] Raise these values a fair bit, hit coastmaker again, and now the waves come in much more
[11:52] naturally.
[11:54] One more tips, notice we've got waves and foam coming in from all sides.
[11:59] Because our ocean has a directionality to it, coast waves and foam coming in from the opposite
[12:04] direction looks weird.
[12:07] So I added a windward mask for the coast waves and foam, which make them only appear in
[12:12] the direction the wind is coming from.
[12:14] Essentially, sheltering the opposite side of your island.
[12:17] I made use of that feature in this shot here, which makes it feel a whole lot more real
[12:22] and natural.
[12:23] Now, I want to be completely transparent.
[12:25] The shoreline waves and the way they crash on beaches is honestly the weakest part of
[12:30] this entire tool.
[12:31] It doesn't look the best and I'm not going to hide it from you.
[12:34] It works a little less well with the long breaking waves over shallow shorelines, the kind
[12:39] you see at beaches where easy waterscape really shines though its environments with steeper
[12:44] cliffs, places where water crashes directly against rocks, like what you're seeing here.
[12:49] Included for free is an Niagara system that generates splashes for a pretty convincing effect
[12:53] from a distance.
[12:56] Improved shoreline waves are absolutely in the works, something that I will be adding
[13:00] in a future version update.


### Surface Details [13:02]
**Transcript (timestamped):**
[13:02] We've got three more categories here in the detailed panel, swells, currents, and wind
[13:07] These are actually detailed that add a layer realism to your water.
[13:11] Swelves add a large scale wave pattern in the distance, which you can adjust right here.
[13:16] I've also included three different normal maps that you can plug in, they're labeled
[13:20] as such, each one giving you a completely different look to choose from.
[13:24] See currents, add that kind of swirly break up pattern that you see on real oceans, and
[13:29] the feature I'm really glad to have added.
[13:31] It's all noise based, so you won't get any tiling, but I'm not using 3D noise, which keeps
[13:36] it relatively cheap.
[13:38] I expose a whole bunch of controls so you can really fine tune exactly how it looks,
[13:42] and in my opinion adds a really nice level of polish and realism that you just don't
[13:47] often see in water systems.
[13:49] And lastly, wind gusts add, well, wind gusts.
[13:53] Just one more realism feature I wanted to include, one that breaks up the repetitive nature
[13:57] of water, and literally breathes life into your environment.
[14:00] Stack all three and your water stops looking like a repeating texture and feels alive.


### Buoyancy [14:06]
**Transcript (timestamped):**
[14:06] These water offers three different types of buoyancy as well.
[14:09] Each with their own pros and cons, first and the cheapest, but lowest visual quality,
[14:15] is the material function.
[14:16] You can slap it onto any material connected to the world position offset pin, and it'll
[14:20] fake buoyancy by sampling the waves of the ocean.
[14:23] But bear in mind, there's no actual physics involved here, so it looks, you know, bad.
[14:29] That said, it worked great for a simple movement in the background.
[14:33] Next, we have the Niagara Blueprint.
[14:35] You drop it into your level, assign a static measure to your choice.
[14:38] You can choose how many objects you spawn, their radius, their scale, their scale variation,
[14:43] perfect for scattering a bunch of degree or floating rubble on the water.
[14:46] This is the one you should be using most of the time.
[14:50] It is highly performant, runs on the GPU, the buoyancy looks great, and if you ever notice
[14:55] something not lining up or being a little floaty, no pun intended.
[14:59] It's just a magic, nudge it, and it'll snap right into place.
[15:02] Lastly, there's a Blueprint component that you can assign to just about anything, a static
[15:07] mesh, an animation blueprint, a camera, whatever.
[15:10] This is the ideal for a hero object that needs logic or gameplay mechanics.
[15:14] It behaves the same way as the Niagara Blueprint, the same controls exposed, just select your
[15:19] actor, click Add Component, and search for Easy Water in the list here.
[15:25] Make sure your object is set to Immovable, to see how it looks, jump into Pi Mode or
[15:29] simulate in Editor, there's a take rate limit for performance, just be aware it has an
[15:35] immediate impact on how things look, at least you have the option to lower it if you need
[15:40] to.
[15:41] This is probably the part that will get the most feedback, and that is by design.
[15:44] I want to build out the buoyancy system together with you, so I could use some feedback on
[15:48] what your project needs.


### BETA Features (Underwater & Lake Mode) [15:49]
**Transcript (timestamped):**
[15:50] Next, I have two features that are in beta.
[15:52] A 1 in version 1.0 to ship with an underwater option, because, you know, for a lot of shots,
[15:57] it's kind of essential, so it's in there, it's the most early stage feature in the tool,
[16:01] and I'll be building it out a lot, adding Godraids, particularly matter, bubbles, distortion.
[16:06] So think of this as the foundation, there's plenty more coming.
[16:11] Lake Mode is for when you don't want an endless ocean, stretching out to the horizon, it lets
[16:16] you shape and rotate your water to sit exactly where you need it.
[16:20] Take the Lake Mode checkbox and adjust it from there.
[16:23] It's still maturing, I'll make it a lot more robust and efficient deadline, and remember,


### Custom Mesh/Water Plane [16:28]
**Transcript (timestamped):**
[16:28] if you'd rather use your own mesh, you can load a custom one right here and disable camera
[16:32] follow here, giving you a water plane that is exactly what you need and where you need


### Wetness Material Function [16:38]
**Transcript (timestamped):**
[16:38] it.
[16:39] Included is a material function that adds wetness and darkening around the base of your
[16:43] meshes right along the coastline.
[16:45] You read the exact water level, so it always lines up.
[16:49] All you have to do is add this material function to your master material.
[16:53] It supports both material attributes and regular pins, you just designate which one with a static
[16:58] boolean here.
[17:00] Once you've compiled your master material, in this case I applied it to my Megascans
[17:04] master material, every Megascans asset now has this wetness applied to it.
[17:10] Open up the material instance of your choice, and you'll find a wetness variable ready for
[17:14] you to adjust on a per material basis.


### Single Layer Water vs. Default Lit [17:17]
**Transcript (timestamped):**
[17:18] The layer of water is the de facto standard for rendering water in Unreal Engine.
[17:22] It looks amazing.
[17:24] You get translucency, caustics, but it does come with a few drawbacks, for example, it won't
[17:30] cast or receive shadows from any light other than your primary directional light.
[17:35] Most of the time, that's totally okay, but in some situations like this here, where you
[17:40] want more dramatic lighting, it just won't work.
[17:44] This shot would primarily lit with one spotlight.
[17:48] And because there's no shadow being cast by this rock here, the whole illusion just falls
[17:53] apart.
[17:54] That is when switching over to default lit.
[17:56] In shots where you don't actually need translucency, can work way better.
[18:01] In this one, I also set the metallic value to one to make it look better.
[18:05] See here, the water in my reference is just kind of dark and deep, and that is exactly
[18:11] the kind of look that lets us get away with default lit.
[18:14] To switch it, open up your easy water scape material instance, search for a shading model,
[18:19] and change it over here.
[18:21] There is no one is better than the other.
[18:22] It always depends on your shot and what you need.
[18:25] There are pros and cons to both.
[18:28] Work mentioning you can control your water surface values for both the default lit and
[18:32] single layer water right here.
[18:34] I made sure it's as easy as possible for people to optimize and fix things easily.


### Performance & Optimizations [18:35]
**Transcript (timestamped):**
[18:39] In this tab here, you'll find a few checkboxes that can help you out in some situations.
[18:43] In a material instance itself, I added a dedicated optimization section where you can quickly
[18:48] find and disable features like swells, currents, coast waves, two or drop your instruction
[18:54] count when you need it.
[18:55] I deliberately put every toggle in one place rather than scattered across each category,
[19:00] so you're not dancing around the group's hunting for them.
[19:04] As I talked about in the beginning of the video, resolution and frame rate are the main
[19:08] dials for balancing performance and quality.
[19:11] You're going to want to keep the frame rate as low as you can get away with.
[19:14] You would be surprised how low it can go before you notice, especially if your camera is
[19:18] far away from the water.
[19:19] For aerial shots, sometimes even 10 to 15 works.
[19:22] This will have a tremendous performance boost for you.
[19:26] For resolution, 4K looks amazing, but in most cases, even I find it to be a bit overkill.
[19:31] 256 to 2048 is usually the range that I work with.
[19:35] If you're not using the underwater feature at all, I recommend disabling it, and in
[19:39] the material instance, setting two-sided to false, it recommended.
[19:43] There is no need to render two-sided if you don't need it.
[19:47] The water mesh itself up here does have quite an impact on performance.
[19:51] There is very little visual difference between LED zero and LED one.
[19:56] 2 to 4 is recommended for games.
[19:58] In fact, LED 4 is a bit excessively low and does have the occasional artifacts depending
[20:05] on your wave size.
[20:07] For an additional performance boost, if you don't need the coastline foam or even the
[20:11] open ocean foam, you can disable both checkboxes here.
[20:15] Let me take a moment to walk you through some handy, good things to know when using easy


### Handy Tips [20:16]
**Transcript (timestamped):**
[20:19] waterscape.
[20:20] A few bugs and known artifacts and how to deal with them.
[20:23] If you're using hardware accelerated lumen or if you're not using lumen at all, you'll
[20:27] be fine red on the box.
[20:29] But if you disable things like reflection screen traces, you might run into these weird
[20:34] black artifacts for worse, this kind of thing.
[20:39] Don't worry, it's an easy fix.
[20:41] One, we just need to disable, evaluate and ray tracing, and then you'll see this horrible
[20:46] thing just apply the lumen offset fix to push the height above zero so there's no negative
[20:51] displacement values.
[20:52] I do recommend using screen traces when possible, as you can see here the results are a lot
[20:57] better.


### TSR Smearing/Pixelation [20:58]
**Transcript (timestamped):**
[20:58] Ghosting, smearing, pixelated water is caused by temporal super resolution or TSR, the
[21:03] anti aliasing, and it's a major complaint from just about anyone who uses Unreal.
[21:09] Here's the thing, easy water can look really good even with TSR.
[21:13] The real issue is that your viewport is lying to you.
[21:17] It's not native resolution.
[21:18] It's probably sitting somewhere between 80% and 90% screen percentage, rarely 100%.
[21:23] That means it is upscaling and what makes the water look so bad.
[21:28] It is entirely TSR at fault.
[21:30] Set it to 100% here, and you'll see the result look way better.
[21:36] Push it to 125% or even 200%, and it'll be tack sharp.
[21:41] Now I know that's not a realistic option for everyone, so fortunately you can change
[21:46] the AA method itself.
[21:48] Here's this console variable, or if you're using Easy Toolback, you can toggle it here,
[21:52] and you'll see there are five other AA methods to choose from.
[21:56] You can also use the Toe Mapper sharpen variable here, as 0.5 or 1, to clean up the smearing
[22:01] a little bit more, every little bit helps.
[22:05] So bottom line, avoid any kind of upscaling if you can.
[22:09] If you see this kind of popping effect of runtime, that's because you need to click
[22:13] stop Easy Water before you render or play.


### Movie Render Queue settings for Cinematics [22:17]
**Transcript (timestamped):**
[22:17] And for the cinematics people among you, there's one thing you really need to know.
[22:20] Due to the way the water generated, you determine the frame rate.
[22:24] How often the water takes forward every second.
[22:27] If you set it to your target frame rate, let's say 24 FPS, you won't get any motion blur
[22:31] between frames, even with temporal samples.
[22:33] Your wave will look choppy, and not in a good way.
[22:36] Instead you'll want to set this to at least 5 to 10 times your actual rendered frame rate.
[22:42] That way you get sampling in between the frames, which gives you nice, smooth motion blur


### Performance Benchmarks [22:47]
**Transcript (timestamped):**
[22:47] on your waves.
[22:49] Many of you will want to know how Easy Water skate performs, so here are the benchmark
[22:52] results for 2 GPUs.
[22:54] A 5090 and a 3080 Ti, which is over 5 years old now.
[22:58] The benchmark settings are very much middle to road, so there's wiggle room on both sides,
[23:01] whether you want to optimize even more or crank the quality up higher.
[23:06] As we've covered throughout this video, you've got tons of dials to fine tune in the performance
[23:10] of the quality ratio for your project.
[23:13] Of course, that can vary based on things out of my control, like whether you use Lumen
[23:17] or reflection quality, lighting quality, and so on.


### Blueprints & Unreal Engine 6 [23:20]
**Transcript (timestamped):**
[23:20] Now you might have heard that Blueprints will be deprecated sometimes after Unreal Engine
[23:25] 6 comes out, and yeah, that is unfortunate, but it is not as bad as it sounds.
[23:30] First, the full launch of UE6 is not for another 2-3 years, and two, Epic and stated that
[23:36] once the new framework has matured enough, only then will Blueprints be deprecated, and
[23:41] they will provide tools for migrating to the new architecture.
[23:44] So we're looking at roughly half a decade in the future here, if not longer.
[23:49] So what does this mean for you?
[23:52] Nothing.
[23:53] UE5 and Blueprints are still going to be highly relevant for the next 5 years, at least.
[23:57] I pledged to keep developing Easy Water Skate, and once UE6 comes out, it will be migrated
[24:02] over and continue working unexpected.
[24:04] Easy Water Skate is a result of months of work, if the most complex tool I've ever built
[24:09] in UE5 so far, and realistically, there are things I've missed, or I didn't notice.
[24:14] So help me help you.
[24:17] If you hit a bug, post it in Discord, and you have my word, I'll fix it as fast as I


### Roadmap Poll [24:21]
**Transcript (timestamped):**
[24:21] can.
[24:22] One last thing, down below is a link to a poll where you can vote on which roadmap features
[24:25] you are most excited to see.
[24:27] Your input will genuinely shape where this goes.
[24:30] And that covered using Easy Water Skate.
[24:33] You can slide it on FAB, link down below.
[24:35] I hope you found it helpful.
[24:37] Remember to join the Discord server for support, questions, discussions.
[24:41] Thank you so much for watching, and as always, folks.
[24:44] Happy rendering.
[24:45] Easy Water Skate is the must have.


### Bloopers [24:46]
**Transcript (timestamped):**
[24:49] Easy Water Skate.
[24:51] Easy Water Skate only then.
[24:54] Only then will Blueprints.
[24:57] Only then will Blueprints.
[25:00] Hate this so much.
[25:01] Oh man, that was a long one.
[25:03] Hit.



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
