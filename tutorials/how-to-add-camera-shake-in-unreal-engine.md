---
title: How to Add Camera Shake in Unreal Engine
source: YouTube
url: https://www.youtube.com/watch?v=8eIavj62Mu8
author: William Faucher
ingested: 2026-06-23
ue_version: "UE5"
tags: [camera, sequencer, cinematics, camera-shake, perlin-noise, blueprint, rendering, beginner-friendly]
extraction_status: complete
frames_dir: tutorials/frames/how-to-add-camera-shake-in-unreal-engine/
frame_count: 5
---

# How to Add Camera Shake in Unreal Engine

**Source:** [YouTube](https://www.youtube.com/watch?v=8eIavj62Mu8)
**Author:** William Faucher
**Duration:** 11m53s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back.  It is great to see you.  The topic of today's tutorial is going to be all about Camerashake.  This is something that other people love or completely hate to see with the fiery passion.  You're going to see shaky cameras a thing in lots of action movies, but I'm not here  to talk about whether that's good or bad.  The main reason I bring it up is because Camerashake is a fantastic way to help make your 3D  renders feel a bit more cinematic, a little bit less 3D.  It's going to give your shot a much more organic feeling to them.  If you're interested in getting your render to look more believable and less CGI looking,  I have an entire video dedicated to that right here.  And in fact, I wish that I had cover Camerashake in that video there, but here we are.  Let's dive into how to very easily set a procedural camera shake in Unreal.

**Frame:** tutorials\frames\how-to-add-camera-shake-in-unreal-engine\frame_000.jpg

### Skillshare [0:52]
**Transcript:** Now before we get started, this video is sponsored by Skillshare.  Skillshare is an online learning platform with thousands of classes for creatives.  It is a place to explore new skills or dive deeper into existing hobbies or passions.  It is the perfect place for both beginners and advanced users alike to pick up a skill  set they've always wanted to have.  Whether that's photography, filmmaking, compositing, effect work in Houdini, learning 3D  and blender, that is all available right here.  Now as someone juggling between a lot of roles these days, between teaching photography  on real productions, making YouTube videos, Thomas Frank's class on productivity for creatives,  building a system that brings out your best is a class that I'm likely going to be watching  myself because 24 hours in a day is just not enough.  Skillshare is constantly releasing new classes and they are curated for learning and by this  I mean that all of the classes are entirely ad-free, so you won't get distracted or annoyed.  Now because Skillshare is sponsoring this video, I have a special link for you down below.  The first 1000 of my subscribers to click the link down below will get a one month free  trial of Skillshare so that you can start learning today.  With that being said, let's get this camera shake tutorial started.

**Frame:** tutorials\frames\how-to-add-camera-shake-in-unreal-engine\frame_001.jpg

### Setup [2:06]
**Transcript:** So here I am in the abandoned apartment scene which you can find for free on the epic  marketplace just so you know, the first thing we need to do is to make sure that we have  a sequence set up with a camera in it.  So I've already made a sequence here by going to Cinematics, you can create a new level  sequence there.  I have one created already right here.  I'm going to assume you know how to set up a camera.  Once that's done, going to the camera view mode here, you'll see I have a very simple  panning camera shot, nothing fancy at all.  But now I want to go add camera shake to this to make this feel a little bit less linear,  a little bit less robotic.  Now how do we do that?  We're going to go into our content browser right here and we need to create a blueprint  factor.  Don't worry, it's not advanced at all.  We're going to right click, create blueprint class and where it says all classes here in  the search panel, we're going to search for shake.  And you'll see here we have camera shake base.  Now I've seen other tutorials where people have used the matinee camera shake from my understanding  it is pretty much the same.  You can use whatever one you want.  I like using camera shake base right here.  Click on this and hit the select button.  And I'm going to call this camera shake, either they're one.  So now we have our camera shake blueprint created to what we're going to do now.  We're going to double click on this right here to open up the blueprint and you'll see  we now have the typical blueprint graph showing up here.  I personally prefer to have a more streamlined version of this and pay attention to what happened  when I close this and reopen it.  We've no more graph.  Now we just get a much more streamlined version of this blueprint.  Why that happens?  I'm not entirely sure.  Maybe it's a bug, maybe it's intentional, but now you know.  So what we're going to do here where it says root shake pattern, we're going to click here  and set it to Perlin noise camera shake pattern.  Which now you'll have the option to unfold the setting here.  And now we have a whole bunch of other settings to unfold.  The first one I'm going to unfold here is timing and I'm going to set the duration to  zero because zero means that the camera shake will last throughout the entire shot.  It's going to last infinitely.  So it's going to repeat and loop itself.  Otherwise what's going to happen is you leave it a default is the camera shake will be  applied for one second and you don't want that you don't want camera shake to occur  for only one second.  You want it to shake throughout the entire shot.  So setting it to zero is the first step.  Now we can hit the compile button on the top left hand corner and let's apply this camera  shake actor to our sequence for starters.  So I'm going to move this out of the way like that and going back to our sequence right  here.  We now need to add this blueprint to our camera actor.  So we're going to click on our camera component right here and click on the track button.  Go up to where it says camera shake and you'll see that the blueprint actor that we just  created now shows up.  So we're going to click on this right here and you'll see now in our sequence our camera  shake actor now has a bar that we can't realign here like this.  Now we know that our camera shake will be applied throughout the entirety of our shot.  So if I press the play button now you'll see well there's no camera shake.  There's nothing there.  What's happening?  Why is there nothing going on?  That's because we now need to tell the blueprint actor how much shake we want to have and  that is where the location, rotation and FOV come in real handy.  So the one I use the most in 90% of cases is rotation for the most part.  And you'll see right here we've got a few more settings.  You've got rotation amplitude, rotation frequency, pitch, yaw and roll.  Just for now I'm going to set my rotation amplitude multiplier to something ridiculous  like 10 and just be aware you may get a little bit sick.  Notice how now we've got this like crazy swirling motion going on.  It's obviously over the top.  We don't want this but this is how it works.  So I'm going to tone this back to something like one and you'll see now there is a subtle  camera movement going on.  Now the next option here rotation frequency multiplier that's going to affect how often  those shakes occur.  So amplitude, control the intensity of the shake and the rotation frequency controls how  often that shake is going to occur.  So if I set this frequency to again 10 and you'll notice everything is like really, really  janky and shaky.  Again way too much way too strong.  I just want to demonstrate the effect.  So I'm going to set this back down to one.  So generally I like having a low amplitude and a slightly higher frequency.  I'm going to set this to like two or something and a very low amplitude to like point one,  point two maybe.  So you'll see right now it is much much more subtle.  Adding camera shake is an art of its own.  You really need to apply this tastefully because it is very easy to go overboard with this.  It is way too easy to just kind of go way over the top and just make your audience feel  nauseous.  Now what's that being said we do have control over the individual axes upon which the rotation  shake can occur.  So I'm going to set the pitch, the yaw and the roll tabs here.  So I'm going to start off with the pitch and I'm going to set the yaw to zero and the  roll to zero as well.  And I'm going to exaggerate this for effect.  You'll see the pitch control how the camera looks up and down.  The yaw controls the left and right movement of the camera.  And the roll is going to control the side by side rotation of it as you can see.  So it's a matter of really balancing these three axes to get the look that you want.  So imagine when you're holding a camera you don't really roll the camera like that,  right?  A little bit of roll can be useful.  So again fine tuning these values is an art of its own.  So feel free to go ahead and experiment with that.  So we're going to set this back down to 0.5 or something and turn the roll down to 0.5.  Yaw to one and amplitude to one as well.  So as you can see very simply very easily we've added a subtle camera shake to our camera.  And this makes it feel way more real.  It feels like someone is actually holding this camera.  So I'm going to disable this now.  And the same thing can be done with location.  And location is going to be the actual position of the camera itself.  So if I set this to 1 and let's say 5 notice how that camera is not looking in a different  direction it is purely just moving up, down, left, right, forward and backward.  You can control these movements of each XYZ axis right here.  And lastly we have the FOV which is the field of view which means it's going to zoom in  and out ever so slightly.  So if I set the amplitude to 5 notice how the camera is zooming in and out like this.  This is not something I've ever really used ever because I can't think of a use case  for it but if that is an effect that you want to have in your shot now you know how.

**Frame:** tutorials\frames\how-to-add-camera-shake-in-unreal-engine\frame_002.jpg

### Bonus Tip! [9:42]
**Transcript:** It's also worth noting that you can have multiple camera shakes stacked onto one another.  So let me demonstrate right here.  I'm going to go back to my content browser and I'm going to just duplicate this.  I'm going to call this version 2.  Okay.  We're going to open that and going back into the sequencer clicking on my camera component.  I'm going to click on track.  Camera shake and you'll see we have camera shake version 2 showing up here.  Now we'll see we've got both camera shake 1 and 2 showing up here.  And why would you want to do this?  Are they having one camera shake that is very broad and slow moving just a general rough  pans and having a second one for the micro shakes just a very small shakes like that.  So let me demonstrate here just to show you.  So with the camera shake V1 selected here in the rotation I'm going to set this to like  a slightly higher amplitude than I normally would but with a very low frequency.  So something like 0.5.  Let's see how this looks.  So notice how the camera shake is very subtle.  It's just a very slow swirling movement.  And now in camera shake V2 I'm going to go back to my rotation and set it to a lower amplitude  but a higher frequency.  So something like 0.2 and something like 5.  Maybe not 5, maybe 3 or 2.  So now you may notice we've got some larger, more slower, swirly movements to it but also  some very subtle, slightly janky movements to it.  Starting to camera shake actors on your camera component can really give you a bit more  granular control over the look of your camera shake.  You don't have to do this but I figured this is a great tip to know about and it might  help you a lot in your next project.

**Frame:** tutorials\frames\how-to-add-camera-shake-in-unreal-engine\frame_003.jpg

### Outro [11:45]
**Transcript:** So since this video has helped you out don't forget to hit that like and subscribe button.  It makes a really big difference and as always happy rendering.

**Frame:** tutorials\frames\how-to-add-camera-shake-in-unreal-engine\frame_004.jpg


---

## Structured Notes

### Core Technique
Procedural camera shake in UE5 via Camera Shake Blueprint (CameraShakeBase + Perlin Noise Camera Shake Pattern): Duration=0 for infinite loop; Rotation Amplitude + Frequency for each axis (pitch/yaw/roll) for organic feel; stack two shake actors (one slow/broad + one fast/micro) for more granular control. Apply via Sequencer camera component track → Camera Shake.

### Summary
William Faucher demonstrates procedural camera shake in UE5 to make renders feel organic and less CG. Method: create Blueprint Class → search CameraShakeBase → set Root Shake Pattern = Perlin Noise Camera Shake Pattern → Timing Duration = 0 (infinite loop, otherwise shakes only 1 second). Parameters: Rotation Amplitude Multiplier (intensity), Rotation Frequency Multiplier (speed/rate), per-axis values for Pitch (up/down), Yaw (left/right), Roll (side tilt). Typical tasteful values: Amplitude 0.1-0.2, Frequency ~2. Location shake (XYZ position movement) also available. FOV shake (zoom in/out) exists but rarely used. Stacking tip: duplicate shake BP → assign two shake actors to same camera in Sequencer; one with low frequency + higher amplitude (slow, broad movement) + one with high frequency + low amplitude (micro-jitter) = realistic layered shake.

### Key Steps

**Create the shake blueprint:**
1. Content Browser → Right click → Create Blueprint Class → All Classes search "shake" → select CameraShakeBase → name it (e.g. CameraShake_V1)
2. Double-click to open → close graph (opens streamlined view)
3. Root Shake Pattern → set to Perlin Noise Camera Shake Pattern
4. Expand Timing → set Duration to 0 (infinite loop)
5. Expand Rotation: set Amplitude Multiplier and Frequency Multiplier
6. Per-axis: Pitch (up/down), Yaw (left/right), Roll (tilt) — typical: Amplitude 0.1-0.2, Frequency 1-2
7. Hit Compile

**Apply to Sequencer:**
1. Select camera in Sequencer → click Track button → Camera Shake → select your CameraShake BP
2. Extend track bar to cover shot duration
3. Press Play to preview shake

**Stack two shakes (bonus tip):**
1. Duplicate CameraShake_V1 → name CameraShake_V2
2. Add second Camera Shake track to same camera component in Sequencer → select V2
3. V1: low frequency (0.5), higher amplitude (broad, slow swirl)
4. V2: high frequency (2-3), very low amplitude (micro-jitter)
5. Result: multi-layered handheld feel

**Other shake types:**
- Location: shakes camera position (X/Y/Z) — pure translation, no rotation
- FOV: animates field of view (zoom pulse); rarely used in practice

### UE Systems / Blueprints / Settings
- **CameraShakeBase**: Blueprint parent class for camera shake; used as base for all shake presets
- **Perlin Noise Camera Shake Pattern**: shake implementation using Perlin noise; smooth procedural looping; set via Root Shake Pattern property
- **Duration = 0**: in Timing settings; makes shake loop infinitely (default 1 second = wrong for sustained shots)
- **Rotation Amplitude Multiplier**: controls intensity/magnitude of rotation shake; keep ≤0.2 for subtlety
- **Rotation Frequency Multiplier**: controls speed/rate of shake oscillation; ≥1 for visible motion, >3 gets distracting
- **Per-axis (Pitch/Yaw/Roll)**: individual multipliers for each rotation axis; set Roll to 0 or very low (0.2) to avoid nausea
- **Camera Shake track (Sequencer)**: add from camera component Track button; accepts any CameraShakeBase BP

### Difficulty
Beginner

### UE Version
UE5

### Tags
[camera, sequencer, cinematics, camera-shake, perlin-noise, blueprints, rendering, beginner-friendly]

---

## Related Entries
- how-to-actually-improve-your-films-vfx-dune-in-unreal-5.md (noise tracks in Sequencer as alternative to Camera Shake BP)
- give-me-14-minutes-and-youll-make-cinematic-renders.md (camera movement + Perlin Noise Float for light animation)
