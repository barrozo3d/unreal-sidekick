---
title: Unreal Engine Black Eye Cameras: Car Cameras! Gameplay and Cinematics.
source: YouTube
url: https://www.youtube.com/watch?v=4X16gnNVD1E
author: Black Eye Technologies
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics/
frame_count: 8
---

# Unreal Engine Black Eye Cameras: Car Cameras! Gameplay and Cinematics.

**Source:** [YouTube](https://www.youtube.com/watch?v=4X16gnNVD1E)
**Author:** Black Eye Technologies
**Duration:** 24m45s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Thanks for tuning in. In this video we're going to show you how BlackI's going to transform your  gameplay driving cameras and cinematic cameras. Anything you're shooting cars, BlackI's going to help.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics\frame_000.jpg

### Gameplay Driving Camera [0:09]
**Transcript:** Okay, let's get into gameplay driving cameras. We've come a long way where we should have  where cars aren't stuck to the middle of the screen. This is what 1996? You can't feel the car  physics. There's no camera car relationship. And in this example, I'm going a little too far,  but look, you can feel the braking, you can feel the acceleration, you can feel the tire grip,  the car's not stuck to the middle of the screen. Let's make your driving camera. Okay, so drop  a BlackI simple look at in the scene, set your auto assigned to be player zero and set the look at  in the follow. Let's get automatically buying the camera to the car, turn on, save and play.  And then let's adjust the positions. This is a follow-off set. You can use this to set how far  you want the camera away from whatever you're following. The car, of course, here. And then let's  look at the car. We're going to go from screen space to world space. This enables a velocity look  ahead. We're going to get into that in a second. Let's adjust the screen space composition, get  the framing right. And then we're going to put in a little bit of follow-damping. This is the  decoupling between the camera and the vehicle....

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics\frame_001.jpg

### Cinematic Car Sequences [9:50]
**Transcript:** drop a black eye camera in your scene. You can move it to wherever. Pick look at and then pick the  little eyedropper under subject and pick your car. Move the cameras now looking at the car  and we have this dynamic tracking although not very well composed shot. Let's take this camera and  drop it on to sequencer and add a transform track. So what we're going to do is we're going to  and we'll just put the in the camera cuts track too so we can see it. Here's our shot. Not so amazing  yet. So what we're going to do is we're going to have the camera move. We're going to do a couple of  keyframes very basic. So we're going to have the camera you know here. Let's keyframe that keyframe  that transform and then as a car drives by we'll do a little swoosh behind it.  And this is part of the joy and power of black eye is you can do these like hybrid modes where  just a couple of camera keyframes but all the rotation stuff is figured out the tracking. Let's  just make this a bit shorter. It was a bit too crazy. All right, and the car is going to smash into  the camera. Maybe not ideal. Let's move it out a bit more. We'll just go to curves and just fix  this up a little bit. A bit too far...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics\frame_002.jpg

### Follow Camera Rig [15:07]
**Transcript:** Follow camera rig. So where the last one had some keyframes on the movement this one we're going to  make follow the car. So pick follow. Open your subject and pick the car. The camera's  snaps to a position we just defaulted 300 to the side. Let's play it. Those are the keyframe offsets  on the screen composition from the shot just now. So let's get rid of those because we're going to  do our own compositions. I'll just delete these keys. So now the car is the camera is following the car  on the side. So what we're going to do is we're going to add a follow offset track. We're going to  put some keyframes in the relationship between the camera and the car. So you can see it's stuck there  but we can move it. We can change this offset and we're going to keyframe the offset positions.  So let's start from the side. We'll go to the middle and then we'll go to the other side. So you  can see just a few keyframes and this is the offset between the camera and the car.  So look at this. Come in, zoom around the car. It's probably a bit high. Let's make it go low.  Okay. Now the composition is not great. So let's put some keyframes on the composition. So what we're  going to do is we're g...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics\frame_003.jpg

### Follow Fly-by Rig [17:09]
**Transcript:** So we start from the side. Focus on the front of the car.  Just let down a little bit and then we hinge away to the side.  And then off the car goes. So let's show you how to make this shot.  So drop out black eye camera in the scene and tell it to follow the car.  Tell it to look at the car.  So we'll just start with this offset here. Just to get started.  You can see you move the camera around. It's always looking at the car.  So we're going to add a track. Let's pull the camera down onto sequencer. We're going to add a follow  channel and we're going to add extra yaw and a follow offset. We're also going to add a look at  in a screen space position. These are the main tracks for everything.  So that extra yaw is the camera's raw yaw. Sorry, the camera's yaw around whatever it's looking at.  The follow offset is the camera's offset relationship between what it's following.  So let's put some keys here. Let's keep playing the composition.  And we're going to add a little bit of offset here. So we're looking at the front of the car.  See that offset in local space. We're going to put that where the logo is.  And then adjust the composition. There we go. We got the car going. The ca...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics\frame_004.jpg

### Camera Shakes [20:46]
**Transcript:** Camera shakes. I'm going to use the default UE camera system. We're working on our own.  Well, I want to show you how you can do this now. So add a camera shake track. I've added two  noise camera shakes in black eye. They're not great. I'm going to be honest with you. I don't love  noise-based camera systems. Camera shake systems. Here it is. That's where they are  under the examples content in our black eye. Make sure you get the show plug and content on.  And here's here they are. They're really just a quick start. You can spend a long time  tuning this stuff and you're never going to get it to look amazing because I don't think noise-based  camera systems or camera shake systems are the right approach. But they're not bad.  So the main thing here, really nice, right? Too strong. The main thing here is I set the  duration to be zero and then that makes it last for an infinity. And let's just turn these  to speed down. That's a bit drifty. But it's that easy. You create a camera shake track.  You drop one of the noise profiles that are included with a black eye.  And you'll need to tune it because I don't know what kind of noise you want or what lens you've  got on. I'm just goin...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics\frame_005.jpg

### Velocity Look Ahead [22:55]
**Transcript:** into velocity. Look ahead because it's so powerful. Okay, this camera is looking at an offset  that's on the front of the car. And that's cool while you're driving. But look, we're stopped.  The composition is terrible. Look at the composition to be more like this.  But when it's like this, then the camera's looking at the center of the car.  And that's not great. So here is velocity. Look ahead, cranked up way too far. You can see as you go  faster, the point moves forward. Let's tune it down a little bit. So now, when you drive,  the composition shifts forward. And now we're looking at the nose of the car.  See that? That point will move forward with the velocity of the car.  But then when you stop, it looks at the middle of the car. It's magic. It's actually great.  Works in reverse too. Works in any direction. And what this does is it's like a camera operator.  It gives you a little bit of that lead. Like we showed you before, the gameplay cameras.  That velocity look ahead works great for gameplay too. Look at that.  Looking at the front. Now as it stops, it looks at the middle of the car. As you speed up, looks ahead.  Thanks for watching. Black Eye is pretty awesome for driv...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics\frame_006.jpg

### End [24:08]
**Transcript:** Hope you love it. Reach out in our discord or comments below. Thank you so much for being part of the Black Eye Family.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics\frame_007.jpg


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
