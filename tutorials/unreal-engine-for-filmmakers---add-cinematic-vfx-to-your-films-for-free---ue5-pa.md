---
title: Unreal Engine for Filmmakers - Add Cinematic VFX to your Films for FREE - UE5 [PART 1]
source: YouTube
url: https://www.youtube.com/watch?v=Yl_VJqmll-E
author: Boundless Entertainment
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-for-filmmakers---add-cinematic-vfx-to-your-films-for-free---ue5-pa/
frame_count: 8
---

# Unreal Engine for Filmmakers - Add Cinematic VFX to your Films for FREE - UE5 [PART 1]

**Source:** [YouTube](https://www.youtube.com/watch?v=Yl_VJqmll-E)
**Author:** Boundless Entertainment
**Duration:** 13m8s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### What is a Fluid Simulation? [0:00]
**Transcript:** What's going on guys, Sam here, and today I want to talk to you guys about a somewhat overlooked  huge advancement in Unreal Engine 5, something that feels a bit overshadowed by Lumen and Nanite,  which are our incredible advancements, but this is another groundbreaking feature of UE5,  which is another game changer, and that is the addition of fluid simulation into the real-time  UE5 editor through Niagara.  So what a fluid simulation is, is it essentially sends out simulated gas or fluid into the scene  based on your inputted vector settings, so direction, intensity, and speed, and then  it applies physics and forces to that simulated gas or fluid, which are specified by you  much like a physics collision simulation except with fluids.  So this means that it will act in a realistic way, and it's going to be able to interact  with objects in your scene rather than just being a particle system which shoots out particles  and uses image projection or specified physics to create the look.  So what that means is that you're going to have completely dynamic fluid simulations,  so fire, smoke, explosions, things like that, and also water, and that's all going to  be inside your real-tim...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---add-cinematic-vfx-to-your-films-for-free---ue5-pa\frame_000.jpg

### Scene Overview [2:22]
**Transcript:** So let's just take a quick look at this fluid simulation now.  So this is what we're going to be creating here, and as you can see, we have this ship  kind of flying through this cloud of smoke, and I'm just going to go over some of the basics  of how you can achieve this look, and just how to basically set up your fluid simulation  inside of Unreal Engine 5.  So if you go inside of Unreal Engine 5 here, you can see that I've set up the scene for  you guys.  So if you guys want to learn how to build this scene, this is kind of what my new course  in Unreal Engine 5 goes over.  So we go over from start to finish building the scene from the ground up, from scratch,  all the way through rendering with render passes and getting the best render settings for  the most cinematic results out of your renders, all the way through using those tools to composite  in Adobe After Effects and Blackmagic Design Fusion.  And it basically teaches you the full process, full pipeline of creating a visual effect  shot in Unreal Engine and using it with pretty much any compositor.  So it's a really valuable training, I highly recommend it, and you can pick that up on  balance-resource.com, I'll leave a ...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---add-cinematic-vfx-to-your-films-for-free---ue5-pa\frame_001.jpg

### Setting up Niagara [3:38]
**Transcript:** So before we actually can have access to the new Niagara fluid simulations, we have to  go up here into edit and go down to plugins, and we're going to have to enable this plugin.  So we're going to search for Niagara.  And we have a lot of different options here, but we want to turn on this Niagara Fluids,  which is the Fluid Simulation Toolkit for an Niagara.  So we're going to click on that, and it's going to warn you that this is a beta version.  That's okay, we're going to hit yes, and then we're going to have to restart our engine,  so we're going to go ahead and click on restart now.  All right, so we're back inside of Unreal Engine here, and it might take some time  for some shaders to compile.  It actually was really quick for me, so be patient with that.  Now we have our scene here, and what I want to do is maybe add some smoke

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---add-cinematic-vfx-to-your-films-for-free---ue5-pa\frame_002.jpg

### Adding a Niagara System [4:18]
**Transcript:** coming out from this building to have our ship be able to fly through it.  So what we're going to do is go down into our content drawer.  I've created this new folder called Niagara Fluids, and we're going to right click in here.  I'm going to go to FX, and we're going to go down to Niagara System.  What we're going to do is create a new system from a template or behavior example.  We're going to hit next.  And now you can see we have a lot of different options for our 2D gas simulations,  our 2D liquid, our 3D gas, and our 3D liquid simulations.  This is really powerful, and as you can see, even just from these thumbnails here,  we have some pretty high resolution stuff.  We have a lot of control of that, which I'm going to get into in this tutorial.  So for what we want to do, I'm going to just go with this grid 3D gas simple particle source.  This is going to give us a good starting point for a lot of our effects here.  So it's going to create this Niagara System, and it's going to take some time to prepare the shaders here,  but we can in the meantime name it.  We'll just call this NS underscore fire.  Our shaders have compiled, so all we have to do right now is just take this ...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---add-cinematic-vfx-to-your-films-for-free---ue5-pa\frame_003.jpg

### Voxel & Resolution Explanation [5:48]
**Transcript:** And what that is is a voxel is basically a three-dimensional pixel.  So if we go into our Niagara actor here, and we go down here and we find our resolution max axis here,  if we increase this value to something like 250, you can see that now it's starting to look much higher quality.  We're getting a lot more resolution in here, and it's looking more realistic.  So basically what that means is that there are more voxels here in our simulation.  So basically more pixels and therefore higher resolution.  Just like increasing the resolution of an image, it's going to cost you more in terms of your computer's resources,  but it's also going to look much better and more realistic.  So we can set our resolution maybe somewhere around 250 for now.  We can always increase this later.  And then also I'm going to show you a little bit about how you can actually increase that resolution only for your rendering,  so that it's not going to cost you a bunch when you're just moving around in your viewport.  And it will only increase that resolution when you render.  So let's try 350 and see what happens.  And as you can see, it's starting to significantly slow down my computer,  so our frame rat...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---add-cinematic-vfx-to-your-films-for-free---ue5-pa\frame_004.jpg

### Adding Collider Objects [7:08]
**Transcript:** Like I said before, we actually want our ship to interact with the smoke in our scene.  And the reason this doesn't happen immediately, so if I take my ship here and I just,  and I start moving it through the smoke, you can see it's not doing anything.  And the reason that's not happening is because by default, nothing in your scene is set to collide with the particle simulation or your fluid simulation.  And that's because if it was, if everything was set to automatically collide,  if you pulled out one of these particle systems into your scene,  it might crash your computer because calculating all this data and all these crazy interactions with all the objects in your scene.  So you're going to have to enable that through the use of tags.  So just to kind of demonstrate a little bit here what I'm about to do  and how we can get our objects in our scene to interact with our Niagara actor is,  if we grab a cube basic actor here and we just drag it into our scene,  we pull it up here around where we're going to be working with our fluid,  I'm just going to demonstrate what this whole collider system does.  So if we go into our cube settings and we search for tags and we go down here...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---add-cinematic-vfx-to-your-films-for-free---ue5-pa\frame_005.jpg

### How Niagara Fluid Sim Works [9:57]
**Transcript:** So if we click on this box, we see our NS Fire instance and we can X out of this,  get rid of that filter and we can double click on our Niagara system.  So now what you can see in here is we have basically these two boxes right here.  And if you're familiar at all with how Niagara works in the past,  you had your particle source emitters and then you could add a bunch of other emitters  and things like that to your system.  But if I just go down here and turn the sprite renderer,  and if I turn off my grid gas controls emitter,  what you can see is that if I zoom in here,  all this is doing here because I've soloed this particle emitter.  The fluid simulation works by emitting particles,  which act as your fluid into your scene,  and then it applies physics and forces to them and simulates the reaction of your fluid.  So this is basically just the building block or the starting point  of how your fluid simulation is going to be emitted from the source.  Okay, so once it's emitted, then this gas control emitter  kind of takes over and simulates using the physics that you input into this parameters of this box,  it will then simulate the fluid simulation.  So your particle source em...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---add-cinematic-vfx-to-your-films-for-free---ue5-pa\frame_006.jpg

### Conclusion [12:13]
**Transcript:** If you are interested in learning how to build this scene,  you see here from the ground up, from scratch,  make sure you go over to boundless-resource.com  and check out that course.  I'll put the link in the description.  I'm also offering a bundle, which includes the original  Unreligion for filmmakers advance course,  and this new course at a huge discount.  I think the total is like $70 or $100 discount total.  So make sure you guys go over and check that out as well.  Subscribe and also comment any new videos or courses  that you guys would like to see.  So I just kind of wanted to introduce you guys  to the world of Niagara fluid simulations.  Obviously, there's a lot more to go into on this,  but I just want to kind of introduce this to you  and get this in your head so you can start playing with it.  So thanks for watching guys and have a good one.  You guys could live az in the community.

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---add-cinematic-vfx-to-your-films-for-free---ue5-pa\frame_007.jpg


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
