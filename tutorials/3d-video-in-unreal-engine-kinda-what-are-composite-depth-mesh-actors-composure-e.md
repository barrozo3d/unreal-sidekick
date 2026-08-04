---
title: 3D VIDEO in Unreal Engine? Kinda? What are Composite Depth Mesh Actors? (Composure EP6)
source: YouTube
url: https://www.youtube.com/watch?v=C9yvCd3uzHM
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-08-04
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/3d-video-in-unreal-engine-kinda-what-are-composite-depth-mesh-actors-composure-e/
frame_count: 0
frame_status: pending-selection
---

# 3D VIDEO in Unreal Engine? Kinda? What are Composite Depth Mesh Actors? (Composure EP6)

**Source:** [YouTube](https://www.youtube.com/watch?v=C9yvCd3uzHM)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 21m59s | 16 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py 3d-video-in-unreal-engine-kinda-what-are-composite-depth-mesh-actors-composure-e <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction to Composite Depth Mesh Actors [0:00]
**Transcript (timestamped):**
[0:00] In Unreal Engine 5.8 there's a new tool for composure called the composite depth mesh actor
[0:06] which allows you to project video onto a surface and give it a displacement
[0:10] and then you can actually look around and see what's going on inside Dean's head.
[0:15] So the technique is basically using a piece of geometry and it's displacing that geometry directly towards the camera
[0:23] and so you get this sort of depth of recreation effect
[0:26] but if you look from the side you'll see that it's kind of just doing a height field from the point of view of the camera
[0:33] so it breaks, it's not perfect but it can allow for some cool stuff, like you can take a light
[0:38] and then you can move it around and it'll actually light up the surface
[0:42] and you can take geometry and you can move that around and it'll actually cast a shadow onto the surface
[0:47] so it allows for some neat fun tricks in Visual Effects in Unreal Engine
[0:52] and I'm going to show you how we can do those right now.


### Live vs. Offline Workflow Explained [0:56]
**Transcript (timestamped):**
[0:56] So my intro was done offline which means I recorded the video, I made an extraction, made a depth matte,
[1:01] brought it into Sequencer and did it that way but in this case, just to kind of show the principles,
[1:06] I am doing this live with a still frame of my depth matte so you can kind of see how the illusion works
[1:15] but if you had like a budget and some sort of depth matte type camera and a way of getting that depth matte out
[1:21] then you could do all of this stuff in your live virtual production world
[1:25] but I don't do that, I'm an offline type person.
[1:28] So I'm going to show you how to get to this sort of live state first because it's fun
[1:34] and then I'll show you how to do the offline, the higher fidelity with creating a depth matte, etc.


### Setting up a New Scene in Unreal Engine 5.8 [1:40]
**Transcript (timestamped):**
[1:40] So what we're going to do is just clear this scene and I'll just start with the back scene.
[1:46] I'm going to create a new empty level and I'm using Unreal Engine 5.81
[1:51] and with all things unreal it's constantly changing, constantly updating,
[1:55] workflows are always improving or being disregarded like blueprints.
[2:00] So make sure that you're subscribed because I will be updating this every time there's an update.
[2:06] So there you go.
[2:09] Now so we're going to go to file, new level, I'm just going to go and create a basic one,
[2:14] there we are. Now I'm going to use composure, so we go to the windows


### Composure Basics: Composite and Camera Actors [2:15]
**Transcript (timestamped):**
[2:19] and virtual production and composure to open up our composure window
[2:23] and so we're going to add a composite actor.
[2:27] So that's kind of like the basics of composure and it needs a camera.
[2:31] So we're going to go to perspective up here and I'm going to say create camera
[2:37] and create cine camera actor. So now I've got a cine camera actor and a composite actor
[2:42] and so we go and select our composite actor and up here in the composure window
[2:48] and under here says camera actor, this is none and I'm going to select the camera that we just made.
[2:54] So we've got a camera and that is assigned to our composite actor.
[2:58] Now for our plate, in the intro I was doing offline which means I recorded some video
[3:03] and I was using a media texture but for right now I'm going to use this one which is a media profile
[3:08] and that will allow us to use our webcam or if you're broadcast something else,
[3:13] whatever broadcast users, I don't know broadcast, I do everything offline,
[3:17] I'm a visual effects person by day. So I'm going to make a media profile.
[3:22] So go into content browser, right mouse button, under media you go to media profile
[3:29] and then you give it a name MP, Dini, there we are, double click on that one.
[3:35] Then under here you go and select media sources and then add media source
[3:40] and then under media source we go down to stream media source
[3:46] and then under there we go to stream URL, you go and click the down arrow
[3:52] and then here it will list anything that's connected to your computer.
[3:55] So hopefully you'll have something that says USB video or webcam or whatever.
[4:00] So I'm going to click on that one. So now here I am in the signal
[4:04] and because I'm using the webcam now as the media profile,
[4:07] then you're going to miss me in the bottom corner for a bit.
[4:11] I'm sure you'll really miss me. Okay, save that, come out of here.
[4:15] Now we can go into our composure and plate and change this texture for the media profile.
[4:23] Let me click here, text it from media profile and we change it to stream media source like that.
[4:29] So now our texture is going to be projected from our camera's point of view onto an object.


### Adding the Composite Depth Mesh Actor [4:35]
**Transcript (timestamped):**
[4:36] In my other videos I've been using composite mesh actors
[4:40] and that is basically a piece of geometry that it project onto and it lands on that surface.
[4:45] So it uses the surface and then the light's basically just hitting it
[4:48] and if you want to just add one now for fun, you go into here the square plus button
[4:52] and you hit place composite mesh actor.
[4:55] So there we go, that's what our sort of previous pipeline was and probably still will be.
[5:01] But in this case we're going to delete this and we're going to use,
[5:07] delete where it says none too, we're going to use a place composite depth mesh actor.
[5:12] Now this one, you won't see anything straight away but if you look at the camera,
[5:17] if you go to your camera and when I select my composite depth mesh actor
[5:21] you can see something's happening right here at the center of the camera.
[5:25] And so the composite depth mesh actor needs a video signal
[5:31] and it also needs an object and this comes by default and it's a grid
[5:36] that's attached right to the center of the camera and it's looking for a depth texture.
[5:41] And once you apply a depth texture, it will project this material,
[5:47] which is this texture, onto the grid and displace it from the camera's point of view
[5:53] with a depth texture. So I'm going to go and find depth texture and here's one I made earlier


### Applying and Scaling Depth Textures [5:54]
**Transcript (timestamped):**
[5:59] and it was this little guy here and this is one I made in DaVinci Resolve
[6:04] and I'm just using a still for now. I'm just going to drag him onto the depth texture
[6:08] and now you can see something's happened here. So hooray!
[6:13] But it's a little small and even if I'm looking through our camera, we're not seeing anything
[6:17] and that's because our clipping plane is actually clipping this out.
[6:21] So to be able to see this thing, we need to push it, basically scale it further away from the camera.
[6:27] So I'm going to go under here, under scale factor and this just scales the object
[6:33] further away from the camera like that. There we are. So I'm going to move around
[6:38] and there is our object like that and then I'm going to increase the scale factor
[6:44] and this is just scaling everything unilaterally away from the centre of the lens.
[6:50] Now someone was asking me, is this the same as a regular displacement map?
[6:54] And effectively it is except the unique part is that you can see here that everything is bending
[7:01] towards the centre of the lens. So when I look through the camera, then all of these pixels
[7:07] look like they're exactly in the right place, screen space wise, but if we come from the side
[7:12] then you can see it's kind of mush in it and we can change the depth texture to anything else that we want.
[7:17] So if I grab in this low res blurred, put that on there and then you can see we're getting some
[7:24] odd things going on. You want to have a hall of mirrors type of fact.


### Relighting Video Surfaces in the Scene [7:30]
**Transcript (timestamped):**
[7:31] Let's quickly change that back. But what does this mean in practical terms?
[7:36] Well, if we now add a light into this scene, so I'm going to go add plus light, point light.
[7:45] So if we add a light into the scene, we should be able to relight this geometry, but by default
[7:51] if we go into the plate layer and go down to the bottom, we're using is holdout enabled,
[7:56] which basically means that it's not using any of the lighting of the scene.
[8:00] It's using exactly what the camera is projecting through onto a surface.
[8:04] So we turn that off and now you'll see, there's the light and it's actually lighting up that surface like that.
[8:11] And then if I look through my cine camera, you can kind of see this is amazingly beautiful lighting here
[8:18] and not at all broken. But in the next section, I'm actually going to show you how to get this look
[8:25] much nicer. So we're in my opening scene that I did earlier and I'm going to give you an overview


### Overview of the High-Fidelity Offline Scene [8:26]
**Transcript (timestamped):**
[8:30] of what I did differently in this one compared to the thing I just showed you.
[8:34] And then I'm going to put a link up here for anyone who's new to the channel and not seen my composure series
[8:40] where I go for in detail every one of them, like how I bring in image sequences and how I do camera tracking
[8:46] and how I use a projection composite, no all sorts of stuff. Anyway, it's up there and I hope you're enjoying it so far.
[8:54] Alright, so here is my sequencer and in here I have got my composite depth mesh actor and I'm using two media tracks
[9:04] and I've got one for the RGBA and then one for the depth down here. And I wanted to point out something up here.
[9:11] If you go to the texture, I'm using a media texture and I'm going to show you how I set that up a little bit later
[9:19] rather than using the media profile. So I just want to say thank you to Stephen Palmer for having a look at an early version
[9:25] of this video and pointing that out. So thank you Stephen. Now our image media sources are in DWA-AEXR in linear
[9:33] sRGB color space and these are at 3840x2160 UHD format and for the depth mat I actually kept it the same size
[9:43] but I could make it a lot smaller because it doesn't really matter that much how I'm softening it anyway.
[9:48] Anyway, there's my media sources and there they are playing on my composite depth mesh actor.
[9:54] Now you can see with this one I'm getting nicer looking lighting on this guy compared to the one I did earlier.
[10:03] There we are, like that. So we're getting a sort of nicer lighting and the reason is because I'm basically mushing the normals
[10:12] technical term on the material, the composite depth mesh material. So to access the composite depth mesh material parameters


### Accessing Material Parameters in Sequencer [10:17]
**Transcript (timestamped):**
[10:21] you have to add it into the sequencer and here's the one I did earlier and I've got my values here like I've got my roughness at one, metallic, blah blah blah blah blah
[10:30] but I'll show you if I delete this from the sequencer and it's kind of remembered on my settings but what you do is you get your composite depth mesh act
[10:39] and you drag it into your sequencer and under the plus button here you add default composite mesh component and then under the plus there
[10:48] then you add the slot material. I didn't write this and then under the plus here then you'll see the material parameters exposed.
[10:57] So you can add your metallic, your roughness and your specular and then in this one the procedural normal textual offset.
[11:08] I don't know what any of this really means but never mind. I just wiggle stuff and go, oh that looks better, oh that looks worse.
[11:17] So I'm just going to set these back to the default. Okay now you can see it's kind of gone a little bit blocky, a bit Minecraft so I'm just going to zoom in here so we can kind of see this surface
[11:29] and let's go and change these values. There we are. So now that looks kind of a bit more broken and how we were kind of getting on the, oh dear you got to stare at that face.


### Refining Lighting and Fixing "Blockiness" [11:40]
**Transcript (timestamped):**
[11:41] Imagine how I feel. Alright so this roughness down. So there you can see the sort of blockiness of this material and if I go into my projection camera you can kind of see this is one to one pixel wise
[11:57] and if I move my point line around you can kind of see you getting some wild effects. Brilliant. So I hope you're going to have fun playing with this because I want to see what everyone's going to make
[12:12] because when I first saw this I was like, oh I'm never going to use this, this is mental. And now I'm like, oh you can kind of come up with some fun things.
[12:20] But the kind of trick to this was to get your roughness, set it to one because then that's not sort of shiny. My metallic, I can't remember what I put that on, pretty low.
[12:30] But this procedural normal textual offset is the thing that you kind of bend this one around and you can see there that it's getting rid of that.
[12:39] And then yeah, so if you move this procedural normal around you can kind of see it gets rid of that and then you go extreme and get it inverted normals.
[12:47] So I'm not 100% sure on what it's doing. I kind of think it's blurring the normals but then other things will sort of break.
[12:57] So I'm not quite sure why it does what it does but if you're one of those smart people who knows materials and things, let me know in the comments and I will have better knowledge for the future.


### Directional Light and Shadow Softening [13:10]
**Transcript (timestamped):**
[13:10] Another thing, if I turn off these lights now, just go to a different frame. Let's go to a frame where the lights are off.
[13:17] Now if I grab my directional light, I've made the source angle really wide because if I zoom this down, just put it down to normal and then move my light around, you can see that I get a very hard looking shadows here.
[13:32] So it's not perfect. So I basically make my source angle as bigger, bigger, bigger, like 30. Let's go for a huge one. Let's go for 80 and it kind of softens this off.
[13:44] But it's still not perfect and again, it'll be probably playing with the normals here and getting that right and there's probably some sort of magic sweet spot.
[13:54] But what I did for the opening sequence was I left my light however I wanted it and I went into the plate layer and I re-rendered it again but turning on is holdout enabled.
[14:07] So when you're using is holdout enabled and I'll turn off my color grading, then you're getting the actual projection of the texture without any of the lighting on it.
[14:16] So then you can mix through in the comp later on.


### Enabling Shadows from Depth Mesh Actors [14:20]
**Transcript (timestamped):**
[14:20] Now for shadows by default, let me put on is holdout enabled off.
[14:25] You'll get shadows cast from the object onto the composite depth mesh actor, but you won't get shadows from the composite depth mesh actor onto the environment or self shadows like this.
[14:38] So to enable that you select your composite depth mesh actor and then you search for shadow and cast shadow in the details panel.
[14:45] Then you enable that.
[14:47] I've not found a way yet inside of Unreal Engine to create a depth matte natively.


### Generating Depth Maps in DaVinci Resolve Fusion [14:50]
**Transcript (timestamped):**
[14:52] So if you know a way of making it or if there's a freeware way of making a depth matte, let me know in the comments.
[14:59] Currently I'm using DaVinci Resolve Studio which is the paid version because it's got a depth matte generator.
[15:05] And I'm going to show you how you can do that right now.
[15:08] So I've got my green screen set up and I'm just going to go to my result.
[15:13] I'm going to zoom in by pressing 2 and then I'm going to I'm in fusion by the way.
[15:18] DaVinci Resolve Fusion which is awesome.
[15:20] I press control space and then look for depth map and then I press add.
[15:27] And then to get the result, it's very complicated.
[15:30] You have to press 2 and that's it.
[15:33] Isn't that brilliant?
[15:34] So it's worth the price just for that.
[15:36] So I love it.
[15:37] I don't know how it works.
[15:38] Some sort of weird strangeness.
[15:40] Now, to end of strangeness, Unreal Engine likes white to be far away and black to be close.
[15:47] So we have to invert this and thankfully inside of the depth matte node, there's actually invert function.
[15:53] And so now that should work correctly inside of Unreal Engine.
[15:57] Now, another thing is when I ran this out last time, I ran it at the same resolution as the plate,
[16:03] but I didn't need to because it's ultra high definition and for a depth matte, it can be much lower resolution.
[16:10] So I'm going to add a resize node in here.
[16:14] Resize and then just make it half the resolution.
[16:17] So here is 3840.
[16:19] So I'm going to just divide it by 2.
[16:21] 2160 divided by 2.
[16:23] And now as long as aspect ratio stays the same, it'll fit for your RGB, which is my green screen.
[16:29] Now I'm going to now render these out by pressing control space and looking for a saver node.
[16:38] So I add a saver node and then I'm going to go and browse to where I'm going to put these.
[16:43] And then I'm going to call them depth dot dot exr.
[16:49] And between the two dots is where it'll put its file numbers.
[16:52] So you hit save and then under here under format, I'm going to change it to from compression zip to compression dwaa,
[17:01] which is much lighter format and also going to put the compression higher as well.
[17:05] So it'll be lighter and smaller.
[17:07] So it won't be as much of a memory draw as my original one, which was at 4k.
[17:13] So that all looks good to me.
[17:15] Now just go to fusion, render all savers and it will start rendering these frames out.


### Importing Image Media Sources into UE 5.8 [17:21]
**Transcript (timestamped):**
[17:21] So I'm back in Unreal Engine and I just wanted to show you how to bring in those image media files.
[17:26] I'm assuming you've done it before, but if you've not watched my last video,
[17:30] then Unreal changed the way you bring things in a little bit and actually made it a little bit easier,
[17:34] which is good news.
[17:35] So I'm going to bring in that image media source.
[17:37] So we go right mouse button in our content browser, look for media, then image media source.
[17:44] And then we're going to call this IMS.
[17:47] I'm going to call it depth to how original double click on that.
[17:53] And then we're going to navigate to under sequence path where we rendered those files.
[17:58] I'm going to click on the first frame here.
[18:00] And then if you press this button down here, that will open them up and play them.
[18:04] And so they're actually the small enough now and light enough to be able to play in real time here.
[18:09] So great, that's done.
[18:11] So we just save that and then we close that window.
[18:14] Now I'm going to go into my sequencer and obviously I've already got my depth in here,


### Setting up Media Tracks in Sequencer [18:16]
**Transcript (timestamped):**
[18:19] but we're going to pretend I didn't.
[18:21] So if we were adding this from scratch, then I go to my first frame and then my hit add media track.
[18:30] And then under here, I add plus media source.
[18:35] And then I go down to whatever we call this IMS depth to here we are.
[18:41] And now it says add a media texture to the new section and you say create texture.
[18:47] And this will now let you create a media texture.
[18:51] And then I'm going to give it a name, M T call it depth to hit save.
[18:58] And so now it's automatically put it in here.
[19:01] And if I go to the right mouse button properties, we don't need a media player anymore.
[19:07] So right, that's good.
[19:09] So I just wanted to show you that one.
[19:11] So now if we go and select our composite depth mesh actor and then we'll go to a frame like this.
[19:17] Currently it's using the one that's already in the sequencer, this one.
[19:20] And so I'm just going to change it to this one.
[19:22] And I go under here under the little arrow and then look for empty depth to and there it is.
[19:31] While we're in here, I'm going to go to the composure window and just show you that the texture that I'm using
[19:37] rather than in the first part of the video, I was using the media profile.
[19:41] Whereas in this one, I'm using a texture and a texture is the same way we made the media texture for the depth to pass just then.
[19:49] That's basically what I did for this one here.
[19:51] Hooray! So one more thing was with the depth pass, it's working great out of the box.
[19:57] The depth is looking right.
[19:59] So something's going right somewhere.
[20:01] But if the depth was kind of squashed or elongated, originally I thought that you'd go into here and change this one, the scale factor.
[20:10] But that basically just scales everything relative to the center of the frame.


### Dynamic Camera Animation & Parenting Tricks [20:11]
**Transcript (timestamped):**
[20:13] So you'd actually need to go into the material and change the contrast of this.
[20:17] And currently I would do that inside of DaVinci Resolve or I would add a color contrast into the material.
[20:26] But I'm not going to do that this time and I'll do that on the next video.
[20:30] So before I say goodbye and see you next time, I wanted to show you one last thing and that is at the beginning of the video,
[20:37] you can see that I'm bouncing into frame.
[20:39] Dink, dink, dink, dink.
[20:40] Also, if you just want to get faster playback and you don't want to have to have all the frames loaded,
[20:46] you can go into your media tracks and just turn them off like that.
[20:51] And so everything will just stay on the last frame that you're on.
[20:54] So this is good if you just want to see what your animation looks like and you don't really care about the image update.
[21:00] So at the beginning I've got some animation and in order to do that, I had to parent the camera and the composite depth mesh actor to the same object.
[21:10] So I added an actor and so I've parented those together.
[21:14] But I also wanted it to pivot around here rather than here.
[21:18] And if I move this actor, then the camera and the projection goes with it.
[21:22] So I had to add another actor upstream and then offset this one against it.
[21:27] So now I can rotate him here rather than here.
[21:32] So he's rotating around that axis.
[21:35] What fun.
[21:36] So my next video is going to be on improvements in adding live action into virtual environments
[21:41] and some material tricks so we can get some better lighting.
[21:44] Might use some of this composite depth mesh actor, some normal passes, some additive passes and directly inside of the material.
[21:52] So that'll be fun and I will see you on that one.
[21:56] Thanks for watching.



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
