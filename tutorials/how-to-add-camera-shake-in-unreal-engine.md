---
title: How to Add Camera Shake in Unreal Engine
source: YouTube
url: https://www.youtube.com/watch?v=8eIavj62Mu8
author: William Faucher
ingested: 2026-06-12
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-add-camera-shake-in-unreal-engine/
frame_count: 0
---

# How to Add Camera Shake in Unreal Engine

**Source:** [YouTube](https://www.youtube.com/watch?v=8eIavj62Mu8)
**Author:** William Faucher
**Duration:** 11m53s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back.  It is great to see you.  The topic of today's tutorial is going to be all about Camerashake.  This is something that other people love or completely hate to see with the fiery passion.  You're going to see shaky cameras a thing in lots of action movies, but I'm not here  to talk about whether that's good or bad.  The main reason I bring it up is because Camerashake is a fantastic way to help make your 3D  renders feel a bit more cinematic, a little bit less 3D.  It's going to give your shot a much more organic feeling to them.  If you're interested in getting your render to look more believable and less CGI looking,  I have an entire video dedicated to that right here.  And in fact, I wish that I had cover Camerashake in that video there, but here we are.  Let's dive into how to very easily set a procedural camera shake in Unreal.


### Skillshare [0:52]
**Transcript:** Now before we get started, this video is sponsored by Skillshare.  Skillshare is an online learning platform with thousands of classes for creatives.  It is a place to explore new skills or dive deeper into existing hobbies or passions.  It is the perfect place for both beginners and advanced users alike to pick up a skill  set they've always wanted to have.  Whether that's photography, filmmaking, compositing, effect work in Houdini, learning 3D  and blender, that is all available right here.  Now as someone juggling between a lot of roles these days, between teaching photography  on real productions, making YouTube videos, Thomas Frank's class on productivity for creatives,  building a system that brings out your best is a class that I'm likely going to be watching  myself because 24 hours in a day is just not enough.  Skillshare is constantly releasing new classes and they are curated for learning and by this  I mean that all of the classes are entirely ad-free, so you won't get distracted or annoyed.  Now because Skillshare is sponsoring this video, I have a special link for you down below.  The first 1000 of my subscribers to click the link down below will get a one month free...


### Setup [2:06]
**Transcript:** So here I am in the abandoned apartment scene which you can find for free on the epic  marketplace just so you know, the first thing we need to do is to make sure that we have  a sequence set up with a camera in it.  So I've already made a sequence here by going to Cinematics, you can create a new level  sequence there.  I have one created already right here.  I'm going to assume you know how to set up a camera.  Once that's done, going to the camera view mode here, you'll see I have a very simple  panning camera shot, nothing fancy at all.  But now I want to go add camera shake to this to make this feel a little bit less linear,  a little bit less robotic.  Now how do we do that?  We're going to go into our content browser right here and we need to create a blueprint  factor.  Don't worry, it's not advanced at all.  We're going to right click, create blueprint class and where it says all classes here in  the search panel, we're going to search for shake.  And you'll see here we have camera shake base.  Now I've seen other tutorials where people have used the matinee camera shake from my understanding  it is pretty much the same.  You can use whatever one you want.  I like using ca...


### Bonus Tip! [9:42]
**Transcript:** It's also worth noting that you can have multiple camera shakes stacked onto one another.  So let me demonstrate right here.  I'm going to go back to my content browser and I'm going to just duplicate this.  I'm going to call this version 2.  Okay.  We're going to open that and going back into the sequencer clicking on my camera component.  I'm going to click on track.  Camera shake and you'll see we have camera shake version 2 showing up here.  Now we'll see we've got both camera shake 1 and 2 showing up here.  And why would you want to do this?  Are they having one camera shake that is very broad and slow moving just a general rough  pans and having a second one for the micro shakes just a very small shakes like that.  So let me demonstrate here just to show you.  So with the camera shake V1 selected here in the rotation I'm going to set this to like  a slightly higher amplitude than I normally would but with a very low frequency.  So something like 0.5.  Let's see how this looks.  So notice how the camera shake is very subtle.  It's just a very slow swirling movement.  And now in camera shake V2 I'm going to go back to my rotation and set it to a lower amplitude  but a higher fr...


### Outro [11:45]
**Transcript:** So since this video has helped you out don't forget to hit that like and subscribe button.  It makes a really big difference and as always happy rendering.



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
