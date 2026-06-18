---
title: How I Remade the BACKROOMS using VFX
source: YouTube
url: https://www.youtube.com/watch?v=N4hq0WUaPmk
author: Josh Toonen
ingested: 2026-06-18
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-i-remade-the-backrooms-using-vfx/
frame_count: 6
---

# How I Remade the BACKROOMS using VFX

**Source:** [YouTube](https://www.youtube.com/watch?v=N4hq0WUaPmk)
**Author:** Josh Toonen
**Duration:** 33m58s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### How to make the Backrooms in Unreal Engine 5 [0:00]
**Transcript:** Let's make our own back rooms inspired short film using Unreal Engine 5.  I'll show you the fastest way to build your own back rooms film set from scratch.  Then I'll show you how to turn your gameplay into animation, so you can act out your movie using just a mouse and keyboard.  And finally, I'll give you a free download of this VHS effect that you can adjust in real time to apply to any game or short film,  so you can preview your movie as you're making it. With these three skills, you can make your own found footage horror movies from home.  Let's dive right in.  Before our first step, let's start building the back rooms.

**Frame:** tutorials\frames\how-i-remade-the-backrooms-using-vfx\frame_000.jpg

### Step One: Build the Backrooms [0:45]
**Transcript:** Even if you've never used Unreal, I want to make sure you can follow along.  So we're going to get started using one of Unreal's templates for the third person character.  And then we're going to modify this to build our environment and eventually build a customizable controller for that handheld found footage look.  You can load this into any project.  Just start out by pressing Ctrl-space to open up your content browser where you'll find all your files.  And then we can click on this little add icon and let's add in a feature or content pack.  And then we can add in the third person project.  Then we'll go to our content browser and find this new third person folder.  Then just double click on a level to open it up.  Now when you load in this template, all you need to do is press the play button to start controlling your character.  And we'll come back to this in just a second.  But let's start out by building the environment first.  Now if we look at some references, you can see that the environments are actually pretty simple.  We're going to need a custom material for our walls where we'll have this generic wallpaper look.  Then we'll need our ceiling tiles and these fluoresce...

**Frame:** tutorials\frames\how-i-remade-the-backrooms-using-vfx\frame_001.jpg

### Step Two: Set Up Your Character [13:27]
**Transcript:** So there's a couple of things you need to know about setting up playable characters in Unreal.  The first thing is how they actually are created when you press the play button.  Right now when we press play, our character is spawned and then we can move around in our 3D world.  Now if I press escape, this will kick us out of game mode.  And you'll notice right here in the center of our world, we have this player start object.  This comes from the original template that we started with.  Now whenever you have a player start object in your scene, this will tell Unreal Engine to spawn your character.  And the specific way it's doing that is if you click on this little blueprint chain right here,  we can go down to our current game mode.  And if you look down here, you'll notice that our pawn or our playable controller is our third person character.  That's how Unreal Engine knows to spawn our third person controller when we press play.  Now in our case, we want to replace this with our own custom first person character.  So let's remove this for now by going to select pawn class and selecting none.  And then let's open up our content browser.  Underneath the third person folder in Blu...

**Frame:** tutorials\frames\how-i-remade-the-backrooms-using-vfx\frame_002.jpg

### Step Three: Record Your Gameplay [18:43]
**Transcript:** So if you ever want to record your gameplay into keyframes that you can animate,  just go to the Windows tab at the very top, then we'll go down to Cinematics,  and let's open up Take Recorder.  Now if we want to record the gameplay for this character, then we need to add this into Take Recorder right here.  So to do this, we'll click on our character, then we'll jump to the Outliner,  and then we can click and drag our first person character into the box right here at the top of Take Recorder.  Take Recorder will create a keyframe for every single detail in the Details panel,  and there's quite a few, so we don't need to record animation for every single property.  We just need to record two different things, our characters transformation, and our characters animations,  like when they're running or jumping.  So if I expand on Take Recorder right here, and we click on our first person character,  right now you can see it's recording 208 different details.  So at first, what I like to do here is let's deselect all the different animation tracks that we're going to record,  and all we need to do is enable the transformation track right here at the top,  then we'll scroll down until ...

**Frame:** tutorials\frames\how-i-remade-the-backrooms-using-vfx\frame_003.jpg

### Step Four: Upgrade Your Enviroment [26:27]
**Transcript:** To make this feel like a liminal space,  think we should add an endless hallway down here.  Let me show you the fastest way to expand your environment,  make hallway super fast.  On the top left, let's jump over to modeling mode.  So let's start up by making a gap for a hallway right here.  Let's delete both of these cylinders,  and then let's make two copies of this hallway.  With Grid Snapping enabled, we'll have one side here,  and then we'll alt-click and drag to make a duplicate that expands to the other side.  Then let's make a copy of this wall here,  and we can seal this down until we have a simple door frame.  And at any point you can press play,  and now we can walk through the doorway to see if the scale is right.  Seems like this might be a little bit too big.  Now we can press escape and jump right into our scene and adjust the three model.  Let's turn our snapping off, now we can drag this to be a little bit lower.  So next, we need to model a hallway on the other side of this door.  So the fastest way to do this is to use the cube grid tool.  Like it sounds, you can just click, drag, and draw geometry on this cube grid.  Let's make this four squares wide,  and then w...

**Frame:** tutorials\frames\how-i-remade-the-backrooms-using-vfx\frame_004.jpg

### Step Five: Photo Realism to Improve Your Film [29:47]
**Transcript:** So there's two things we can do to dirty up our camera and make it feel more realistic.  The first thing we can do that will have the biggest impact is adding volumetric fog into our scene.  All you need to do is search for your exponential height fog, and then at the bottom,  just make sure you have volumetric fog enabled.  We don't want to have a global fog affecting everything.  We want to have volumetric fog coming from each one of our light sources,  but volumetric fog enabled. Here I've cranked up the fog density, so it's really obvious.  But another way you can control fog is just click on any one of our lights,  and then let's search for the volumetric scattering intensity right here.  By boost this up to a value of five, we'll get way more volumetric fog from this one light.  And this way you can art direct by adding more fog or less fog on any one of these lights.  For now, let's dial this back and set our fog density to a value of 0.1.  So we still have some, but it's not too obvious.  Now the next thing we can do is add more imperfections to our camera lens.  So we can jump back to our post process volume, and then let's scroll down and make sure  bloom is enabled. Now ...

**Frame:** tutorials\frames\how-i-remade-the-backrooms-using-vfx\frame_005.jpg


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
