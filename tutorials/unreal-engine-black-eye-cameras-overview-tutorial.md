---
title: Unreal Engine Black Eye Cameras: Overview Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=JGnNpbWiT_0
author: Black Eye Technologies
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-overview-tutorial/
frame_count: 11
---

# Unreal Engine Black Eye Cameras: Overview Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=JGnNpbWiT_0)
**Author:** Black Eye Technologies
**Duration:** 20m10s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey, welcome to this Black Eye Camera tutorial. We covered a lot of stuff in this one. My name is Adam. Let's go  So thank you for

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_000.jpg

### Installation [0:11]
**Transcript:** Purchasing Black Eye if you did here it is at the buy button  It goes into your library folder and you pick which project you'd like to edit to which version of Unreal  Open your plugins folder  There it is. We've got documentation. We've got a discord server super active go there lots of questions and help

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_001.jpg

### LookAt [0:33]
**Transcript:** Okay, let's jump in the basic look at this is one of the most powerful features in Black Eye  This is responsible for camera rotation what it's looking at and what's unique about this is is it looks through the lens and it gives you compositional controls  Okay, so let's put a camera in the scene. So open up your drawer  Go to your plugins folder. Make sure you've got that turned on  right here  You'll see the  You'll see the black eye folder and you'll see cameras and we've got a few different ones and  Just grab the basic look at the cine one drop in the scene  Okay, so you can see it's not looking at anything. It's just a zombie camera in the world  With the real zombie in the world  Okay, let's set up a look at shot. So here's how it goes. You select the camera  Let's make a bit more room here select the camera and you'll see there's follow look at the camera. We're gonna pick look at  so  It's simple you find your subject you hit the eyedropper you click on a subject now the camera is looking at this thing  And by default it's looking at the entire thing the bounding box. That's the  blue cube that's there  What's cool is you can move the camera around and it'll still look at ...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_002.jpg

### Dynamic FoV [2:30]
**Transcript:** So let's turn it on go to enable dynamic epi and the desired subject viewport size is how big you want that thing on screen  We're gonna change the damping. This is the zoom damping. So how aggressively it'll zoom  To keep the subject on the screen and you can see now as you get closer to the camera  The camera's widening the calculated FOV value there is showing what the FOV is and it'll  dynamically zoom between the two limits the telephoto limit and the wide limit  So now you've got a camera that's dynamically looking at something and  dynamically zooming in order to keep it in frame  So this is I mean, this is just super powerful for creating cutscenes and cinematics  When you've got variable sized objects or you just don't do the work of keyframing all this zoom  These are the composition presets are kind of handy  You can just hit them and it'll put the subject at all the standard rule of thirds. So let's just put it at the bottom left  And with the damping control  The camera will  Are very aggressively or very like thick viscous lots of camera weight  Move to track and to rotate and to zoom to keep the subject in the same spot  So super quickly no keyframes  We've got a cam...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_003.jpg

### Bone Tracking [5:20]
**Transcript:** So  Let's not track the that let's track bones. So when I turn that off it shows it is root who's back there  But if you type in his head  Now we're tracking his head bone  And that size that you get you can change the size of  Basically the cube the volume of the head and what I'm doing now is I'm changing the screen size position to  Adjust the composition slightly  So this is a different shot now  It's a bit more consistent framing because we're not framing this dynamic  You know the outer shape of something we're just tracking its head  I'm just messing with ideas. Let's move the camera around  Let's try to focus the length effectively different focal lengths because it's dynamically zooming to keep that head that size on screen  So I'm going to decouple the damping here

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_004.jpg

### Damping [6:25]
**Transcript:** Or link them but look at this. This is with no damping  I'm gonna zoom in a bit  You can see we're just like hard pinned and this is horrible or maybe useful but  That's up, you know very hard pin camera and then just by opening that up the damping where we've added a bunch of weight to the camera  And this is obviously crazy like a number of five you can almost think of this is like seconds like how many seconds  It takes the camera to catch up  So anything over one is a lot depending on the speed of what you're tracking like look at this. This is so goopy and heavy now  We change the  Screen size a little bit  And this is you know probably too much. Let's move that up there  Change the telephoto limit you can see that we were banging on the limit of the lens and I had to go down to you know 2.4 whatever  very telephoto  The dynamic zoom will only work inside the ranges of  The lens limits  So I've decoupled the damping here. What's cool about this is you can  Damp more aggressively left to right than up to down or vice versa  So  Because he's got like a lot of up and down motion. We've got  More pitch damping and less yaw damping pitch being up and down  And these are only two co...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_005.jpg

### Multiple Subjects [8:48]
**Transcript:** Multiple subjects you can track more than one thing it's super useful. So pick your look at  Open a subject add more little plus  So we got two subjects now, and I'm gonna make the second one  Also looking at the character. We're gonna track two things on the same character  So we'll turn off actor bounds and look at this pelvis. So we're tracking the head and  The pelvis you can see top left the two little blue boxes one on the head and one on the pelvis  And what's really powerful about this?  Let's just adjust the  composition here with a screen space position and  Make them a little bigger in the screen  So  What's powerful about this is you can get very specific character framing like a cowboy shot or a midshot  But the characters can be different sizes. Let's say you got a cutscene and  There's some small characters and some big characters. You can have a single camera handle them  So right now because we're tracking you can see up on the top left we're tracking his pelvis and his head  Combining to make the white box in the viewport, which is containing both of those volumes  The camera is gonna zoom to always keep his pelvis and his head in the frame  And that's really powe...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_006.jpg

### Plate + Pedestal [10:22]
**Transcript:** Plate and pedestal it's these little things they add up to make the camera feel more realistic  So the camera plate distance and the pedestal height give you a pivot point that's not on the camera sensor  Which is the default and unreal you can see now that we're  mimicking the pivot point of where this thing would be if it was on a fluid head tripod  So like that's what it normally is and the camera very unrealistically rotates around this pivot point  Now that on its own it's not the most amazing thing of course, but  When you combine that with the dynamic look at and the fact that the camera is  Moving from this position, which is far more realistic like this is how we've seen a camera rotate and twist and turn and all the movies and  TV and when you get that  Automatically framing and you get the pivot point right just feels right and that's big

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_007.jpg

### Follow [11:16]
**Transcript:** Follow camera movement a big topic. Let's go to the follow module pick the eyedropper pick the character  By default, we just throw the camera back 300 units  So that's probably not what you want so you can either punch it in  In the transform inspector or just grab the camera and move it to where you'd like  I'm gonna put a little damping in here. So we've got a bit of positional damping  And you can see now in seconds we've created a track shot  Set the camera to follow the subject move the camera to where you want it put a little bit of damping on it  And the camera will automatically follow  Different damping settings are gonna change the behavior of the camera drastically. So going from point one to one  The camera's now really heavy and you can see as I move this back and forth and look at that slow heavy  Maybe that's too much. Maybe that's what you want and check it out with zero  100% right camera is following locked not realistic probably not useful  But give the camera just a little kiss of damping small values point to here  And you now have this nice weight feels like somebody's carrying it the camera's got mass  It's more believable and in no time at all  You've creat...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_008.jpg

### Sequencer [12:40]
**Transcript:** Sequencer all right, let's get some cameras on a timeline and do some cuts and blends. I'm gonna throw another camera in the scene  And then you take that camera and call it something and  You drag that on to the camera cuts track  You can obviously do this with as many cameras as you want. Let me just clean up this naming a little bit. We got a medium  We've got a wide  And I'm gonna drag the wide onto the timeline and because it's a brand new camera. It's  Not doing anything yet just staring  Off into a direction. So click look at click  Mr. Zombie now it's looking at Mr. Zombie  We'll just clean up the composition a little bit  And we're gonna move this back. This is gonna be like a big wide shot  Let's push him down the frame kind of rule of thirds him  I could have just hit the rule of thirds button  Okay, there's some there's a little bit of damping on there and we've got this wide side shot  Cool  Okay  What am I doing?  Um, I'm gonna pick the lens here could use a dynamic f ove but  Just gonna set an f ove  All right, so buddies moving along  There's that shot. Okay, we're gonna duplicate the medium shot. We're gonna make that a follow shot  We use a how to set up a follow ...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_009.jpg

### Hybrid Workflows [17:10]
**Transcript:** Hybrid setups. This is my favorite and one of the most powerful ways of working  So what we're gonna do is we're gonna add a transform track to this side camera  So it's the why shot  And we're gonna just keyframe that camera position and  There he goes he walks the cameras  Still with that same position  Let's drop a keyframe though. Let's  Move that camera you can see it's still doing the dynamic gaming with a look at module  And let's put that camera right here. Okay, so that's  Great the cameras pushing in  Okay, so let's add another layer to this we need to  We need to fix the composition. This isn't great composition. So select the camera  Let's go back to the start  Select the camera  Hit plus go to look at because we're gonna keyframe some look at attributes and then  Let's add a channel for subject screen position  So this is where the subject is in the screen position. So  We've got a key here and you can see I just moved the composition over  I just fix it damping a little bit  Now that subjects of the bottom left rule of thirds, but that's not great for here. That doesn't look so good  So let's center it and let's push it up  And  What that's doing now is we're keyframi...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_010.jpg


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
