---
title: Tips for Sky Atmosphere & Fog - Unreal Engine 5 (& UE4)
source: YouTube
url: https://www.youtube.com/watch?v=SbxO-Z5rzwk
author: William Faucher
ingested: 2026-06-12
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tips-for-sky-atmosphere-fog---unreal-engine-5-ue4/
frame_count: 0
---

# Tips for Sky Atmosphere & Fog - Unreal Engine 5 (& UE4)

**Source:** [YouTube](https://www.youtube.com/watch?v=SbxO-Z5rzwk)
**Author:** William Faucher
**Duration:** 5m26s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, welcome back. It's great to see you. The topic of today's tutorial is going to be all about  how does that with sky atmosphere to drastically change the look of your scenes?  So with just a few sliders we can go from having something that looks like a regular  average sunny day to something that looks like it's a totally different planet. So with that being said, let's jump right in. Get started.  Alright, so now that we're in Unreal, what we're going to be looking at in this tutorial,


### Setup [0:31]
**Transcript:** Borks in Boats, Unreal Engine 4, and Unreal Engine 5. I'm using UE5 here, but don't worry the process is exactly the same in UE4.  The scene I have right here is a scene that I created during my last livestream.  I'll put the link to it in the description below.  So for starters, we're just going to re-light this completely and I'm going to show you how you can completely change the mood of your scene with just a few sliders.  So let's get started. The first thing I'm going to do is I'm going to use the environment light,  make sure to establish a default sky atmosphere system. So you'll find a tab right here.  If you don't have the tab right there, you can go to Window and then Open ENV Light Mixer.  If you don't know how to use it, I made a tutorial about it right here.  I'll put the link to which in the description as well.  So go check that out if you don't know how to use the environment light mixer.  So I'm going to go into Lit Mode so we'd see what we're doing.  And in the environment light mixer, you're going to want to create skylight, create atmospheric light zero, and create sky atmosphere.  Now you'll notice everything's still kind of black. That's normal. Don't worry. ...


### Sky Atmos Settings [2:05]
**Transcript:** So zooming out here, let's take a look at our sky atmosphere in the outliner here.  And in the details panel, let's scroll down all the way to where it says atmosphere, my right here.  And if you play with the play around with my scattering scale, you'll notice that things start looking very different.  Like you'll notice like, whoa, it almost feels like a desert storm or something.  This is a very interesting look that it gives with just a very simple adjustment to slider.  Another thing you can change is the Rayleigh scattering.  Okay, so we're going to play around with this right here and you'll notice suddenly, like, whoa, things look totally different.  So if you play with these two sliders, both the Rayleigh scattering scale and the My scattering scale, you can definitely achieve some very interesting looking sunset, things that you wouldn't be able to find by default.  So these are two of my favorite settings to play around with.  You also have the My Absorption scale as well, you can play out as well here.  So there's a few sliders here that you really should know about.  Obviously, I'm not here to tell you that there's a right or wrong answer to use here.  You need to be t...


### Correct Exponential Heightfog Settings [3:42]
**Transcript:** And now, the last thing I want to talk to you guys about is how to use the exponential height fog in conjunction with the sky atmosphere.  So I see this misused all the time, and I'm going to show you how to use it properly.  So we're going to go up here into place actors menu.  We're going to create a height fog.  And you'll notice obviously things get way too bright, really over the top, but this is fine for now.  I just want to show you, notice what happened if I rotate the sun below the horizon.  Okay, notice how everything should be black, but it's not.  Like notice how everything is still very bright blue.  Why is this?  The reason for this is because the exponential height fog is an additive process.  Okay, and you'll notice here, we have a few settings to change.  So going to again, to the details panel, we want to change the fog in scattering color here.  Make this black and scroll down a little bit further, and you want to change the directional in scattering color and make this black as well.  And now, notice how the fog will correctly change color and inherit the color of your sun, depending on how high it is on the horizon.  So now if we move the sun below the horizon,...



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
