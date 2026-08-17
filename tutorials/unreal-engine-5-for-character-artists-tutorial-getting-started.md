---
title: UNREAL ENGINE 5 FOR CHARACTER ARTISTS | Tutorial | Getting Started
source: YouTube
url: https://www.youtube.com/watch?v=hsCMGA6pwcc
author: Jared Chavez
ingested: 2026-08-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-5-for-character-artists-tutorial-getting-started/
frame_count: 0
frame_status: pending-selection
---

# UNREAL ENGINE 5 FOR CHARACTER ARTISTS | Tutorial | Getting Started

**Source:** [YouTube](https://www.youtube.com/watch?v=hsCMGA6pwcc)
**Author:** Jared Chavez
**Duration:** 11m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py unreal-engine-5-for-character-artists-tutorial-getting-started <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey, welcome to our new series. We're going to be taking a look at Unreal Engine as a character artist.
[0:05] So let's go ahead and get started. The first thing that we're going to want to do is we're going to want to open up the Unreal Engine Epic Games Launcher.
[0:12] Inside of here, you're going to have this Unreal Engine tab.
[0:15] So we're going to go ahead and click on that and you're going to be
[0:17] greeted with a page that looks similar to this, right?
[0:20] Now the first thing that you're going to want to do if you haven't already is install an engine version.
[0:25] I have a couple of versions installed.
[0:27] The one that I have most up to date is 5.3.2, but there's versions all the way up to 5.8 available for you.
[0:35] Now, once you have that created, what you're going to want to do is you're going to want to hit this launch button.
[0:41] Now let's go ahead and hit that and it's going to bring up a prompt window.
[0:44] And that prompt window is going to think for a second and it's going to bring up a new display for us.
[0:49] Okay, great.
[0:51] Now the window is finished thinking and that's going to bring us to this tab.
[0:56] So we're going to have a couple of different projects that we can create here.
[0:59] We can create game projects, film projects, architecture, and a couple of other resources that we have to start a project.
[1:06] For this case, I'm going to go ahead and click on the Games tab.
[1:10] Now in here, we have a couple of projects that are pre-projects and pause.
[1:15] So my editing team, I'm my editing team.
[1:19] I'm looking at the analytics here told me that 56% of you guys don't subscribe to the channel.
[1:23] That's a lot. That's that's more than 50%. That's 6% more than 50%.
[1:28] Not only are 56% of you not subscribed, there's also only 9% of you that have the notifications turned on.
[1:34] So if you want to see all of my content, make sure to hit that bell to turn that on as well.
[1:38] So if you guys could go ahead and do me a favor, make sure to subscribe to the channel so that you can watch more cool content about 3D character art.
[1:45] And if you did it, well, well, thanks.
[1:47] If you haven't yet, go click the button.
[1:49] Now back to what we were talking about.
[1:53] In here, we have a couple of templates that we can start to use to create our projects.
[1:57] I personally like to start from a blank canvas.
[2:00] So that's what I'm going to start with.
[2:01] So I will click blank and then over here in our project defaults, I'm going to set my quality preset to maximum.
[2:08] And I'm also going to make sure to enable starter content.
[2:11] If you want, you can enable ray tracing if that's something that your GPU has available to you.
[2:17] But for just base level, I wanted to introduce it without ray tracing so that we can have just as straight out of the box generic unreal project as we possibly can.
[2:28] Now, the next thing you're going to want to do is you're going to want to come over here to our project location.
[2:33] And we're going to want to set where this file directory is located at.
[2:36] I have a file here where I place all of my character projects.
[2:40] So I went ahead and created that.
[2:42] And then we're going to set our name.
[2:44] Once you've done that, you're going to go ahead and hit create.
[2:47] And we're going to get another thinking window for the project to open.
[2:51] OK. And so this is what unreal should open up to once you create our project.
[2:56] You're going to see this big old area of terrain, which obviously this is not very exciting.
[3:01] It's just a big area of terrain.
[3:02] And you notice that if you start to move around or pan around, things are going to look a little bit wonky.
[3:07] So the first thing that I wanted to talk about is going to be the keys that we're going to want to use to pilot.
[3:12] So if you right click on your mouse and hold, that's going to allow you to pan around the camera.
[3:18] If you hold that same key and use the W keys, that's going to push you forward.
[3:26] S is going to pull you back.
[3:29] A is going to pull you left and D is going to pull you right.
[3:33] So it's going to work similar to how it would be if you are playing on mouse and keyboard.
[3:38] Now, you'll notice we're not moving very far in distance.
[3:41] That's because this scene is pretty huge.
[3:43] So in order to change out the scene, because we enabled starter content, we're going to come here
[3:49] and we're going to have a bunch of these folders in here.
[3:50] This is where our content is all going to reside and be located at.
[3:55] Since we enabled starter content, we have a couple of resources at our disposal right off the bat.
[4:00] So I'm going to come here to maps and I'm going to go to advanced lighting.
[4:04] Now, this is going to just open up a stage for us.
[4:07] This is pretty bare bones, just a generic stage with a cube for lighting and some material balls
[4:12] and an HDRI image in the background.
[4:16] Now, this is a great place to start our character.
[4:19] So the first thing that we're going to want to do just before we get into actually bringing our character in
[4:26] is just setting up the unreal space to work a little bit easier for us.
[4:31] So what we're going to do is we're going to come over here to.
[4:36] Edit editor preferences and we're going to open up our preference window.
[4:43] Now, in here, if we go to viewports and we look for this invert orbit,
[4:50] Y axis, invert middle mouse pan axis and then invert right mouse Dolly.
[4:56] These are going to be a couple of the parameters that we can enable if we don't feel super comfortable
[5:01] with the look in up and down inside of our unreal project.
[5:06] When I middle mouse click, I don't like that when I push my mouse up, it does this.
[5:11] I want it to actually do the inverse of that.
[5:14] So that's where we're going to go ahead and change this real quick.
[5:17] So we're going to go ahead and click invert middle mouse pan.
[5:21] And now that will pan correctly.
[5:24] Now, the other movements, those ones are fine for me.
[5:28] I'm, I'm okay and comfortable with those, but that's the one that usually kind of
[5:32] throws me off is when that's inverted.
[5:34] So I like to change that right out of the box.
[5:37] Now we have that in place.
[5:39] The next thing that we're going to talk about is bringing our character into unreal.
[5:44] So let's go back up here to our starter content.
[5:46] And in this directory, I usually like to make my own personal folder.
[5:52] You could do this in the starter content or one above that, which can be your own
[5:56] personal folder.
[5:57] So I'm going to right click in this space and do this here.
[6:00] And I'm going to go up here to new folder.
[6:03] So I'm going to name this Jared.
[6:07] Content and hit enter.
[6:10] Now in here, I'm going to create a couple more sub folders just to keep myself a
[6:14] little bit more organized.
[6:16] I'm going to right click again, create a new folder and name this mesh.
[6:21] And then I'm going to create another folder and name this materials.
[6:27] So the first part that we're going to dive into is going to be bringing our mesh
[6:31] into the engine.
[6:32] So we'll come in here and this is where our mesh and our model is going to reside.
[6:37] So like we did to create the folder, we're going to right click one more time.
[6:42] And we're going to come up here to import to game.
[6:45] Now, once we do that, that's going to bring up our project directories.
[6:48] So we're going to have to go and search for a model in order to bring it in.
[6:52] So I'm going to do that real quick.
[6:55] And click this and hit open.
[6:58] Once you hit that, you're going to be hit with this dialogue box.
[7:02] Now, if you just go ahead and hit import all, what you'll notice is you're actually
[7:07] going to get some wonkiness.
[7:08] It's going to think for a second and it's going to spit out all of these materials
[7:12] as well as all of these individual assets that are separated the way that your
[7:17] FBX file is separated, which is not optimal.
[7:20] So if we go ahead and drag this out into the scene, you can see that this is only
[7:24] one part of the model that I actually want imported, not all of these pieces
[7:29] combined together.
[7:30] So we're going to delete that.
[7:32] And then we're going to select all this and just delete it real quick.
[7:36] And we're going to re-import.
[7:38] So we'll come up here, select our torso and hit open.
[7:42] Now, in this dialogue box, what we're going to want to do is we're going to want
[7:46] to hit this advanced section, drop this down, and we're going to search for
[7:51] combined meshes.
[7:53] We'll check that.
[7:56] Then down here in our material section, there's going to be this material
[8:01] import method and it's set to create new materials.
[8:04] That one was creating based on our texture sets, new materials that were in
[8:10] relation to what we had created inside of Maya associated with this model.
[8:14] I don't want any materials assigned to this because we're going to create
[8:17] some new and unique ones for the purpose of our own characters.
[8:21] So I will come down here to do not create material.
[8:25] Now, if we hit import all, we'll see a different result, which is going to be
[8:29] our static mesh loaded in here.
[8:31] Now, if we double click this, we're going to have another window that's going
[8:35] to open up and it's going to look something like this.
[8:37] So in here, we'll be able to just kind of pan around our 3D model that we brought in.
[8:43] If you notice that when you are moving around it, you're zooming a little bit too
[8:47] quickly, you can come up here to your camera speed and actually change that to
[8:53] something a little bit slower.
[8:55] So I changed it to 0.33 still a little bit fast.
[8:58] We'll lower that a little bit more.
[9:01] So now you can pan around your model and look at it in this viewport section.
[9:09] So right here is just getting the model into Unreal.
[9:15] There's a couple of things to call out.
[9:17] And here you'll notice this material slot selection.
[9:21] Each one of these materials is going to correspond to the way that I set up in
[9:26] the materials in something like Maya, which should look like this.
[9:30] In here, though, you'll notice that none of those materials exist because I told
[9:35] Unreal not to create those materials.
[9:38] But it's going to still have the slots.
[9:40] You can come here and play with the highlight and isolate and see where those
[9:47] assets reside in the actual mesh.
[9:50] So if I go through, you can see how all of this is broken up in the actual model,
[9:55] which is great.
[9:56] But we're going to want to pipe in our materials here, but we're going to do that
[10:00] at a later step.
[10:01] But this is where you're going to do it.
[10:02] And the reason that you're going to do it here is because once you save this
[10:06] asset, it's going to ensure that that asset always retains those materials
[10:12] associated to it.
[10:14] You don't want to have to go through and reassign materials every single
[10:17] time you drag and drop this model into the scene.
[10:21] So that's what it's going to allow you to do is have a little bit more
[10:23] finite control over the model from the content browser area.
[10:29] So we can see here again, now we will just drag this out and we have a model
[10:35] in side of our scene.
[10:37] Now, as I mentioned, when we opened this up and we were able to assign the
[10:43] materials in here, you want to do it in there as opposed to assigning them here
[10:49] once you've drug the model into the scene.
[10:51] If you do it here, it's going to assign it just to this single individual
[10:55] static mesh that you drop into your scene, not all of them that are drug
[11:00] into the scene.
[11:01] So that's just a way to save yourself some time and effort of having to
[11:05] reassign those materials.
[11:07] With that said, we've gone ahead and gotten the model inside of unreal.
[11:11] And now we have the groundwork to start building off with later steps
[11:15] that we need in order to add materials and textures, lighting and presentation
[11:19] for our character art.
[11:21] So if you like this and if you want to keep following along, make sure to
[11:24] like, subscribe and follow for more.
[11:26] And I'll see you guys in the next one.



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
