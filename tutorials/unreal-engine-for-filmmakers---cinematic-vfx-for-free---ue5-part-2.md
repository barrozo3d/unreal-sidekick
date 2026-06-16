---
title: Unreal Engine for Filmmakers - Cinematic VFX for FREE - UE5 [PART 2]
source: YouTube
url: https://www.youtube.com/watch?v=5zJktaYwK-I
author: Boundless Entertainment
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-for-filmmakers---cinematic-vfx-for-free---ue5-part-2/
frame_count: 5
---

# Unreal Engine for Filmmakers - Cinematic VFX for FREE - UE5 [PART 2]

**Source:** [YouTube](https://www.youtube.com/watch?v=5zJktaYwK-I)
**Author:** Boundless Entertainment
**Duration:** 19m24s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro & Updates - GEMINI [0:00]
**Transcript:** What's going on guys Sam here and in today's video we're going to be going into part two of our Niagara fluid simulation tutorial  So in the first part I kind of walked through the basics and the setup of how you can get a Niagara fluid simulation working in real time in your scene  But in this video I'm going to go into more detail about how you can actually tweak the settings and  Modify the look of your Niagara actor in your scene and then at the end we're going to go into how to actually light that so that it's looking  Like it actually belongs in your scene. So if you haven't seen part one of this video check that out in the upper right hand corner of the screen and  Let's go ahead and get started into this video  So before we get into the main part of this video  I want to do two really quick plugs the first one is for my new film called Gemini  Which I've just finished and I released the trailer a couple weeks ago  So if you haven't seen that I'm gonna go ahead and roll the trailer right now so you guys can check that out  I can't remember anything before that day  It was like being reborn  Resurrected into this hell  It was a name  Oh  Nightmare  So Gemini is the main sourc...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-vfx-for-free---ue5-part-2\frame_000.jpg

### Modifying the Look of a Fluid Simulation [2:47]
**Transcript:** If we zoom in and we click on our emitter summary  What's really nice about this new version of Niagara is that they've kind of organized things into  tabs here and these are common parameters  You can expand this menu and have a full list to see exactly what's going on here and access all of your controls  But for the most part most of your controls are going to be right here in your emitter summary  You can see that we have our simulation render debug scalability source and all most of this stuff should be set up by default  But if you're having trouble if for some reason your mesh is not colliding with your simulation  Just make sure when you go in here into your emitter summary and go to simulation  Make sure that static mesh here is checked  You can also turn on these other parameters  But the main one is going to be our static mesh especially for what we're doing  So just make sure that's checked if we go into our simulation  Now we actually have a lot of great parameters in here  And this is going to mainly be where you control the look of your fluid simulation  So if we go in here to a vorticity confinement  Basically, it's going to add a lot of detail into your render  I'l...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-vfx-for-free---ue5-part-2\frame_001.jpg

### Modifying your Particle Emitter [9:49]
**Transcript:** But what we want to work on now is actually controlling the source emitter  That's going to control kind of how our particle shoot out into our scene  The first thing that you're going to want to keep in mind  Is that if you want to use a particle system as a fluid source  You're going to have to specify that down here  Where it says set fluid source attributes  This is where you're going to be able to set  The amount of smoke and fire in your fluid simulation  You also have some control over the velocity scale  And a couple of other things  But you're going to need this parameter in your particle source emitter  In order for it to properly pass the information to your gas controls emitter  And we're also going to show you  I'm going to show you in a second how you can make sure that that's  Receiving the information properly  So we're just going to modify this setting a little bit  So if we turn up our density to like one  Now we're going to have a lot more smoke  And it's going to be much more dense  If we turn this back down to point two  And then we actually let's turn this to zero  Now we're going to only go into have fire  So we have just the very minimal amount of smoke  And...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-vfx-for-free---ue5-part-2\frame_002.jpg

### Lighting a Niagara Fluid Sim [14:39]
**Transcript:** Alright so all I've done here is  Just kind of you know move this around a little bit  And I scaled it up using  The world space size parameter here  On our NS fire asset  And so now if I go into my camera view  If we play through this you can see that now our ship  Is actually impacting our fog here  Or our  Niagara actor  Unfortunately one of the drawbacks to using Niagara at this point  Is that it doesn't seem to be able to accept the lighting in your scene inherently  So you actually have to kind of set that up  The way you can do that is if you go down here to  Where you have your directional light settings  In your Niagara actor  So I have my Niagara actor selected  And we have directional light one directional light two  So it comes with two directional lights  Automatically applied to it  These are just kind of default the default lighting setting  What we can do is pick a  An actor in our scene or we can just find it on the list here  So if I type in directional light  We can select our directional light for our scene  And as you can see since I picked the light  That we have actually lighting our scene here  Unfortunately it doesn't take into account the fact  That it's s...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-vfx-for-free---ue5-part-2\frame_003.jpg

### Conclusion [18:28]
**Transcript:** So that's about it for this video guys  If you are interested in learning how to build this scene  You see here  From the ground up, from scratch  Make sure you go over to boundless-resource.com  And check out that course  I'll put the link in the description  I'm also offering a bundle  Which includes the original Unreal Engine for filmmakers' advanced course  And this new course at a huge discount  I think the total is like 70 or $100 discount total  So make sure you guys go over and check that out as well  Subscribe and also comment any new videos  Or courses that you guys would like to see  So I just kind of wanted to introduce you guys to the world of Niagara fluid simulations  Obviously there's a lot more to go into on this  But I just want to kind of introduce this to you  And you know get this in your head so you can start playing with it  So thanks for watching guys and have a good one

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---cinematic-vfx-for-free---ue5-part-2\frame_004.jpg


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
