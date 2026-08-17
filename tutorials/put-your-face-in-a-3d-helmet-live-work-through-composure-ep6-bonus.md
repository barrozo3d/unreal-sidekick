---
title: Put your face in a 3D helmet: Live Work-through (Composure EP6 Bonus)
source: YouTube
url: https://www.youtube.com/watch?v=DwUdLow_I4o
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-08-17
ue_version: "[PENDING]"
tags: []
extraction_status: needs-review
frames_dir: tutorials/frames/put-your-face-in-a-3d-helmet-live-work-through-composure-ep6-bonus/
frame_count: 0
frame_status: pending-selection
---

# Put your face in a 3D helmet: Live Work-through (Composure EP6 Bonus)

**Source:** [YouTube](https://www.youtube.com/watch?v=DwUdLow_I4o)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 109m40s | 28 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** ASR hallucination in 'Adding the UFO and Alien Animation': 'da' x10 in last 50 content words. Review and truncate the affected section before extracting.

---

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py put-your-face-in-a-3d-helmet-live-work-through-composure-ep6-bonus <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro and Project Overview [0:00]
**Transcript (timestamped):**
[0:00] There is an animation called flying. Look at that, it worked! Oh, brilliant!
[0:03] In this video, I'm going to put myself inside a helmet and hopefully there's no aliens around here.
[0:13] So this isn't a fancy video, it's just me trying out to the composite depth mesh actor where I have my face.
[0:23] I'm going to put it inside a spacesuit helmet because I think that's probably quite a good use case for it
[0:28] because you might be able to get some light on there and a bit of dimensionality as you move around.
[0:32] But it's not attached to the head, so the head can move around like that shot in Alien.
[0:36] I'm just looking at that for the Alien.
[0:39] So I'm just going to record this kind of for myself. I was going to just do this just for a play thing.
[0:45] And I thought I'll record it because then at least I might put it online and then someone can just watch this.
[0:53] Oh, wait, what is the background kind of thing?
[0:55] I'll try and talk through my process, but it won't be a fancy kind of like whee-joo-joo-joo like I try to do and waste time.
[1:04] So I'm just going to talk to myself and get on with this. I'm going to start from scratch for myself.
[1:08] I'm going to start with File, New Level and make a basic one.
[1:13] So create this new level and I'm going to save it, File, Save Current Level As and make a new directory in my Levels.
[1:21] And I'm using Unreal Engine 5.81. So a new level that's gone.
[1:27] Right mouse button, New Folder and I'm going to call this one Helmet.
[1:36] And I like to call my maps P underscore for persistent level.
[1:45] And then I've got my map in there. It's going to move it into Helmet.
[1:50] There we are. Move there. Yes, yes, yes, yes, yes.
[1:54] Double click on that one.


### Importing the Astronaut Mesh [1:56]
**Transcript (timestamped):**
[1:56] All right, step one. And then I'm also going to turn off this one.
[1:59] Enable tool tips. So when you hover over something, you get that little thing that comes up and it's doing this all the time.
[2:05] All right, so I've got this. Now I just bought a model, a mesh from the fab.
[2:15] And it was called astronaut. And so I'm going to go into here and then go into mesh, full mesh.
[2:23] I think it's this one. Bring him in here.
[2:27] There we are. And then set that to World Zero.
[2:32] Go right here. Have a look. Look at that. Isn't that great?
[2:37] Nice. That should be good enough for my purposes.
[2:39] Let's have a look. What's in here?
[2:41] Let's say that's that. I might have to go in and just get the Helmet one.
[2:46] I've not even explored this yet.
[2:48] So I might. There's the different parts. Full mesh.
[2:53] There's a man. What does this do?
[2:56] Let me just go. I'm going to add a sequencer.
[2:58] So now I'm going to go into my level.


### Setting up the Level Sequencer [3:00]
**Transcript (timestamped):**
[3:05] That's what's helmet.
[3:06] And I'm going to add a sequencer.
[3:08] So cinematics.
[3:13] Level sequence.
[3:14] LS. I want to call this on helmet.
[3:21] I'm going to change the name of this as well to helmet.
[3:24] Yeah.
[3:30] Open up my level sequence.
[3:31] I'm just going to drag this guy in here to see what I've got.
[3:35] So I've got nothing really.
[3:37] What have I got? I've got a forward kinemation.
[3:40] Let's have a look.
[3:41] Let's go in.
[3:48] What is it? Add. Control Rig.
[3:51] Great. Okay.
[3:53] So filter.


### Adding Control Rig and Animation [3:55]
**Transcript (timestamped):**
[3:57] Oh, no, it's got the body rig and maybe.
[4:00] Well, that's UE5.
[4:01] That's so.
[4:02] I think these don't think they came with it.
[4:06] Maybe they did.
[4:14] I'm just going to put the FK rig.
[4:16] See what that does.
[4:17] Okay. It's got everything.
[4:18] Okay. Great.
[4:20] Let's go in here.
[4:22] All right. Good.
[4:24] And then.
[4:25] Oh, good.
[4:26] You see it's got an inside for the helmet.
[4:29] So that's great news.
[4:32] And then what am I going to do?
[4:34] Um, I want to see if I can turn off this piece of glass.
[4:38] So I could probably just go to the materials.
[4:40] Let's have a look.
[4:41] Let's have a look at his material.
[4:43] So I'm going to go to asset.
[4:48] And then browse to asset.
[4:51] And so look inside this one to see what we've got.
[4:54] So we've got in here.
[4:58] And then you got one material slot.
[5:00] I think this guy.
[5:03] Okay.
[5:04] I might have to just use the build it up in pieces.
[5:07] Then let's try that.
[5:11] All right.
[5:12] Just turn them off.
[5:13] Yeah.
[5:14] Just going to delete this one.
[5:16] Delete him.
[5:18] Let's try it.
[5:19] Let's try the way I can know.
[5:21] All right.
[5:22] I don't know what I'm doing.
[5:23] There we go.
[5:24] Well, that's been established, hasn't it?
[5:26] I thought that we've got in here.
[5:28] There's shared route.
[5:30] Oh, I don't know.
[5:33] Delete.
[5:34] Right.


### Building the Character Blueprint [5:35]
**Transcript (timestamped):**
[5:35] I'm going to make it myself.
[5:37] Cut to blueprint.
[5:42] Blueprint class actor.
[5:45] Call him BP Astro.
[5:50] Oh.
[5:54] Call it BP Astro.
[6:02] Astro Dean.
[6:06] Okay.
[6:07] Now, what are we going to add?
[6:10] Let's add all these things.
[6:11] So we're going to add arms, backpack, body, glass, glass,
[6:18] glass, gloves, head.
[6:27] Oh dear.
[6:28] That is not good, is it?
[6:30] Okay.
[6:32] Helmet holds legs, light boots.
[6:40] And that one.
[6:42] I should have just put that button on there, the static mesh button.
[6:47] Oh, you little bugger.
[6:50] Oh no, it's skeletal mesh.
[6:53] Let's go and do that.
[6:55] I should have just done that.
[6:57] That's quicker.
[6:58] All right.
[6:59] We'll cut that.
[7:00] Click on skeletal mesh.
[7:04] And dish, dish, dish, dish, dish, dish, dish, dish.
[7:09] Dish and note.
[7:16] Okay.
[7:20] So grab those, put them in here.
[7:27] All right.
[7:28] All right.
[7:29] Few port.
[7:30] So I've never done this before, because normally I bring in one FBX skeletal mesh
[7:35] and everything's attached to it.
[7:36] And it's one mesh.
[7:38] So I don't do modular, this is called, because I've just been looking it up on the Epic page.
[7:43] And I've got a link in the description working with modular characters in Unreal Engine.
[7:49] And it looks like, so you do add them all together, but then you make an animation blueprint.


### Working with Modular Characters [7:50]
**Transcript (timestamped):**
[7:56] So is it the construction script?
[7:58] I'm just going to look at this thing here.
[8:00] So it's your construction script.
[8:02] And then you set lead a pose component.
[8:05] Let's try that.
[8:06] Set leader pose component.
[8:11] Okay.
[8:12] We don't want to hear it, but we want, which one?
[8:14] The body, that one there.


### Setting up Leader Pose Component [8:15]
**Transcript (timestamped):**
[8:15] So we're going to make him.
[8:16] So set leader, leader pose component.
[8:21] There we are.
[8:22] Okay.
[8:23] So that's going to be our target.
[8:24] Or is that our new leader bone component?
[8:26] That's a lot.
[8:27] And I think it says here, I'm looking in the new leader bone, and then target is those things.
[8:32] So I think I grab anything in here that's got skeletal mesh.
[8:35] And it's all of them.
[8:36] So let's grab all these things except the body.
[8:44] And I bring it in here.
[8:47] And then I think I make him new lead bone component.
[8:52] And then that one, let me just on pick him.
[8:57] And I think I can just grab all of these.
[9:00] Can I drag that into there?
[9:05] No, one at a time.
[9:09] Now I've never done this.
[9:13] So this is half the press.
[9:16] So I don't know if it's going to work.
[9:19] And this is what you get if we ever do like a live streaming thing.
[9:24] Certainly very awkward, kind of slow and me figuring out how to do stuff.
[9:33] I tend to mostly build non characters.
[9:37] I don't tend to do characters so much in Unreal, but I'm really enjoying doing it.
[9:42] I tend to do static environments, spaceships, and then blue screen, green screen stuff inside of hybrid virtual production rather than characters.
[9:52] But I started doing a bit more characters because of the augmented reality things you get with composure.
[9:57] You can add a character and then it works out all the lighting because that's really fun.
[10:02] And I need to come up with more excuses.
[10:04] So I might put him in the background in this video.
[10:08] All right, so I've done that.
[10:10] Now I'm going to hit compile.
[10:11] Now I'm going to hit save.
[10:13] So that's my blueprint, astro team.
[10:15] Is there anything else that's looking here?
[10:17] So this is what I'm looking at.
[10:19] I'm looking at this here, which is I just do a Google it and then it's working with modular characters in Unreal Engine.
[10:30] And I will put a link there if I ever release the video.
[10:35] Hit save, come back here, close that out.
[10:39] There's my character.
[10:41] Here he is.
[10:43] And I'm going to drag him into sequencer.
[10:45] Now, now what?
[10:48] Now what do I do?
[10:49] I guess it's the body.
[10:50] That was the one.
[10:51] And then if I'm hoping if we add an animation, there is an animation called fly.
[10:55] Look at that.
[10:56] It worked.
[10:57] Brilliant.
[10:58] Oh, there we go.
[10:59] So now all these things are working together.
[11:01] Oh, wow.
[11:02] All right.
[11:03] Well, there you are.
[11:04] So I've learned something new today.
[11:06] Very good.
[11:08] So I'm glad I recorded it.
[11:12] I'm going to go to the end of this animation.
[11:15] Put this here.
[11:17] Okay.
[11:18] There he is doing something.
[11:20] He's doing very floaty animation.
[11:23] And then, yeah, I think I just leave this animation.
[11:28] I mean, this is just a test.
[11:29] I just wanted to see if I put my face in here with that 3D composite depth mesh technique.
[11:34] And let's do that.
[11:36] Actually, this is probably going to cycle, isn't that?
[11:39] So let's have a look.
[11:40] Let's just go and drag this out.
[11:41] See what happens here.
[11:43] There you are.
[11:44] Yeah.
[11:45] So this is cycle animation.
[11:46] Great.
[11:47] Right now, I'm going to select this model.
[11:50] That's my astro head.
[11:51] And I'm going to select that piece of glass and just hide it.
[11:54] So go into here and my blueprint hit plus and then look for the glass.
[11:59] I think it was glass one.
[12:01] And then I'm going to add a visible visibility track.
[12:05] Where is it?
[12:06] Where are you?
[12:07] I'll have to look for it.
[12:14] Hide.
[12:15] What's it called?
[12:19] Hidden.
[12:20] What is it normally called?
[12:32] It's just act hidden in game.
[12:34] All right.
[12:35] So do I have to do that for this thing?
[12:40] Act.
[12:41] Oh, it doesn't do it that way.
[12:43] Yeah, interesting.
[12:44] All right.
[12:46] Viz, visible.
[12:48] Visibility based on visibility,
[12:50] so you can capture only,
[12:52] capture visibility and ray tracing.
[12:54] Well, now I turn that piece of glass off.
[12:56] Oh, maybe I can go into the, it's sub piece.
[13:00] Oh, here we go.
[13:00] So I'm gonna turn it off in here.
[13:01] All right, and then look for viz, ability.
[13:04] Turn that off there.
[13:08] Now what happens?
[13:09] It's sort of, oh no, there you go.
[13:11] It's turned off, it just reset the animation.
[13:13] Because if I go into my, here,
[13:16] my animation go to properties,
[13:18] it's condition when finished project default.
[13:21] So it's just keep state.
[13:23] So if I hide things now,
[13:24] and what I'm also going to do is if I,
[13:27] oh, I can't key this here.
[13:30] Oh, interesting.
[13:32] Now normally you can key things like here,
[13:35] down there, I can actually key that.
[13:36] But for some reason it's not that key,
[13:38] I mean the option to key.
[13:39] So don't know the answer to that.
[13:42] I would have to come up with another way of viewing it.
[13:45] All right, anyway, I'm gonna turn him off now
[13:47] because we don't want that on.
[13:48] We probably want this piece of glass on, eventually.
[13:53] What is this one?
[13:54] Let's have a look for the next piece.
[13:58] Glass.
[14:00] Where are you?
[14:04] I'll be up here into, where's the glass to glass to?
[14:09] And I'll just put glass to.
[14:11] And then I see what the material is.
[14:13] I mean, if I can change anything in the material.
[14:15] So go to material, slot one, that's what glasses.
[14:21] Maybe that's the one.
[14:24] See what we've got exposed in here.
[14:27] No, so that material, slot one.
[14:33] There's nothing exposed in there.
[14:34] So maybe I can go into that material and expose it.
[14:37] But for now, I'm just gonna turn it off.
[14:39] Actually, I'm gonna do,
[14:43] yeah, let's just go and hide him again.
[14:45] So select the glasses one and just turn visibility off.
[14:48] All right, I didn't do anything.
[14:50] Okay, there we are.
[14:51] So there's character.
[14:54] There he is.
[14:56] There he's floating.
[14:59] Fab.
[15:00] And then I'm gonna save this.
[15:01] So file, save all.
[15:05] Okay, so it crashes, not the Unreal ever crashes.
[15:11] And then, right.
[15:13] So now I've got a character with a helmet on.
[15:17] And then I'm going to, for now,
[15:19] I'm just gonna grab that footage that I use.
[15:21] But I'm gonna imagine that I'm gonna add a composite from,
[15:24] I'm just gonna do this from scratch.
[15:25] That's the point of this one.
[15:27] So we've got our mechanics in place.
[15:29] I.e. we've got a character with a helmet.
[15:32] Number one.
[15:33] All right, so now I'm going to go to my composite composure.


### Setting up Composure for Deep Mesh [15:35]
**Transcript (timestamped):**
[15:38] So you go to, where is it?
[15:39] Windows, window, first production composure.
[15:43] That's how you get this window up.
[15:45] And then first thing you have to do is,
[15:48] I'm doing that one there.
[15:49] I'm just gonna move that over here in that window there.
[15:54] First thing you're gonna do is place composite actor.
[15:58] So we've got a composite actor in the scene.
[16:00] And now that needs a camera.
[16:01] And what I'm going to do is
[16:03] I'm going to put camera.
[16:06] I'm gonna turn off the animation.
[16:07] So I'm just gonna disable my animation.
[16:10] Oh, now we see.
[16:12] I shouldn't have done that.
[16:14] I should have go and make my properties
[16:15] and make it the default state, project default.
[16:19] So now I'm gonna turn off my animation.
[16:22] I'll put that one there.
[16:23] Yep, animation, turn that off.
[16:25] So now we'll go back to his default
[16:27] zero zero world position animation thing.
[16:31] Make sure I'm at zero zero zero anyway.
[16:33] There we are.
[16:37] Okay, so I'm gonna find the angle roughly
[16:41] to the bit of footage that I've got.
[16:43] Just gonna change my camera zoom.
[16:47] There's under perspective whereas my zoom thing.
[16:50] I might need to make this one a bit bigger.
[16:51] Where are you?
[16:52] Oh, there we are.
[16:53] Change that one to, let's make it point point.
[16:57] Point one and turn.
[16:58] Okay.
[17:03] So I'm going to make a camera now,
[17:06] perspective and then create camera,
[17:11] cine camera actor.
[17:12] So this is gonna be my projection camera.
[17:15] So I'm going to project that footage
[17:17] onto a composite mesh actor.
[17:19] So I've got a camera.
[17:21] Now I'm going to find a composite mesh actor
[17:23] and you go into the camera.
[17:25] So this is my plate.
[17:26] Currently it's just using this SIMTI bar.
[17:29] So it's using a still.
[17:30] And it's gonna project that onto nothing.
[17:32] But inside of here, the plus square button,


### Adding Composite Depth Mesh Actor [17:35]
**Transcript (timestamped):**
[17:35] you can add a composite depth mesh actor.
[17:38] And the default is this, it's a grid.
[17:41] It's a grid and the grid is like 960 by something or other.
[17:46] Wherever it is, composite depth mesh actor.
[17:50] There you are.
[17:51] So that's it.
[17:53] And it's also looking for a depth texture.
[17:55] So if I do anything like that,
[17:56] I need to go and push this away.
[18:00] So the scale is sort of really small.
[18:02] But if I just change the scale,
[18:05] when do you feel like you push the object away?
[18:06] No, there's no depth mesh actor.
[18:08] Let me just put something on here.
[18:10] As a temporary, there we are,
[18:13] as a temporary depth mesh.
[18:16] So let me come out of this one,
[18:18] perspective, perspective,
[18:21] perspective, perspective, perspective,
[18:23] perspective, perspective, perspective,
[18:24] oh, I'm not in the cinema actor.
[18:25] Oh, okay, right.
[18:27] Now we get my perspective.
[18:29] Let's move you away.
[18:30] Okay, here's my camera.
[18:32] Composite depth mesh actor.
[18:38] Scale factor, where are you?
[18:40] Okay, so you're there.
[18:42] What have we got?
[18:42] Composite depth mesh actor.
[18:44] Let me put something on there.
[18:53] All right, there's by anything on there.
[18:54] Let me just,
[18:57] should be something showing up.
[18:59] That and that.
[19:01] So what am I missing?
[19:02] That's on.
[19:04] That's on.
[19:06] That's on.
[19:07] We don't need that one.
[19:08] Okay.
[19:09] So I'm gonna go ahead and move this one.
[19:12] We don't need that one.
[19:13] Okay.
[19:14] Have I set my,
[19:16] oh, I haven't,
[19:18] didn't assign the camera.
[19:19] So camera actor,
[19:20] you have to decide the one that's projecting.
[19:23] So there it is.
[19:24] There we are.
[19:25] We can see it now.
[19:26] Okay.
[19:28] So now this is projecting.
[19:31] See by default,
[19:32] if I come back and the scale is so small,
[19:35] can't see anything.
[19:36] Not tiny little,
[19:37] like it's this big.
[19:39] And then if you look from the,
[19:41] what is it?
[19:42] Default is one.
[19:43] And then if you look from the actual view of the camera,
[19:46] you won't see it.
[19:46] It's kind of too close.
[19:48] So there's a clipping plane.
[19:50] So these things really catch our eye out
[19:53] because at first you're like,
[19:54] I just doesn't want nothing more rubbish.
[19:57] And then you have to kind of go,
[19:58] all right.
[19:59] So hence why I make videos.
[20:00] All right.
[20:01] So I'm gonna change.
[20:02] I'm actually gonna bring my footage now.
[20:03] So here we are.
[20:05] Looks amazing, doesn't that?
[20:06] There we are.
[20:07] All right.
[20:08] But if I look through my perspective camera,
[20:11] my cine camera.
[20:12] So that is the shape of this thing.
[20:14] And the AI spawn point.
[20:16] So we can change that image for something else.
[20:20] Let's go, here we go.
[20:20] Let's go and use that on that alert.
[20:22] Oh, it's too big.
[20:23] Bring them closer.
[20:25] So there we are.
[20:26] So we're actually projecting,
[20:27] go to plate and projecting this texture
[20:30] onto this composite mesh,
[20:34] composite depth mesh actor.
[20:36] And we've scaled everything
[20:39] using our depth texture.
[20:42] And this depth texture is completely solid at the moment.
[20:44] So you're not seeing any sort of depth on it.
[20:48] If I was to find something,
[20:49] I think there's like a sphere or something.
[20:52] There's some sort of something with fall off on.
[20:54] Let me find something in here.
[21:08] Let's try that thing.
[21:17] It's probably not gonna work.
[21:18] But let's look from the side.
[21:21] There you go.
[21:22] See it's doing something odd.
[21:25] All right.
[21:26] Anyway, now what I'm gonna do is I'm gonna set up,
[21:29] I'm gonna bring in the video that I've already got of me.
[21:33] And I will, actually I should just go and shoot something.
[21:38] I'll go and shoot something
[21:40] and have me doing some sort of reaction.
[21:43] Everything.


### Recording the Video Intro [21:45]
**Transcript (timestamped):**
[21:46] Well, I figured I can just use my webcam
[21:49] because I've got a blue screen behind me.
[21:51] And I'm gonna pretend I'm obviously doing,
[21:53] he was doing that, wasn't he?
[21:54] So I could probably say something like,
[21:58] in this video, I'm gonna put myself inside a helmet
[22:02] and hopefully there's no aliens around here.
[22:08] Ah, like that.
[22:10] There you go.
[22:11] That's gonna be my intro.
[22:13] So, but I'll have to stop this now
[22:16] and grab this bit of footage that I'm using over here.
[22:19] And I'm using OBS to record this.
[22:22] And I've took my glasses off
[22:23] because I don't want to have to deal with the lenses.
[22:26] And as we know, the NASA astronauts all have Lasik.
[22:30] No one, your glasses in the space helmet
[22:32] and they're falling off.
[22:33] You know, like, they're like,
[22:36] oh, yeah, you can't do that.
[22:39] There we are.
[22:39] That's why Han Solo doesn't have glasses.
[22:42] All right, okay, so I'm gonna stop this
[22:43] and then come back.
[22:46] So I've recorded that file.
[22:47] I'm just using my webcam
[22:48] and that is just pulling it straight onto my computer.
[22:50] So it's only, what is it?
[22:53] Like 2K camera.
[22:54] And also it's at 30 frames per second.
[22:56] But yeah, well, you get what you get.
[22:58] All right, now I'm going to bring that item into Resolve.
[23:04] So I'm going to fire up DaVinci Resolve
[23:07] and make a new scene.
[23:11] And I'm using DaVinci Resolve Studio
[23:13] and you need the studio to do the depth mesh,


### Extracting Depth Map in DaVinci Resolve [23:15]
**Transcript (timestamped):**
[23:16] sorry, the depth map pass.
[23:20] But there are some free versions out there
[23:23] that uses machine learning to create depth passes.
[23:27] And all you might have a different piece of software
[23:30] than Resolve.
[23:31] So you know, I only use Resolve
[23:33] and all the compositing that I do,
[23:34] you can use any other software to do it.
[23:37] The only critical thing is to use Unreal.
[23:39] You can't really do all the techniques
[23:40] I'm showing you here in Unity or Godot
[23:43] or something like that, but maybe to lay by it.
[23:49] So that's my old one.
[23:51] Now I'm going to go to make a new DirectMove folder in here.
[23:58] So master, I'm just gonna make a new timeline.
[24:02] Create new timeline.
[24:03] No, not using select clips.
[24:07] Just create a new timeline.
[24:08] What's a new timeline?
[24:10] Hello on that.
[24:13] Right, timeline, create a new timeline.
[24:17] Project settings, yep.
[24:21] Yeah, okay.
[24:22] Right, so I'm making a new timeline
[24:24] and I'm gonna call this one LM4 helmet intro.
[24:33] I'm just gonna call it 01.
[24:35] Okay, so here it is.
[24:37] And now I'm going to go and bring this in.
[24:39] Going to go to my capture.
[24:41] I'm gonna make a new one of these as well.
[24:42] Create new bin, capture two.
[24:52] Now I'm gonna bring in my element
[24:53] that we just shot in Port Media
[24:56] and it was helmet blue screen.
[24:58] This one here, open that up.
[25:01] Bring it into here.
[25:03] This final clip.
[25:09] Stay on, don't worry about sound,
[25:10] in fact, I'll just use it for this part here.
[25:13] Where's that's a lot.
[25:15] So blah, blah, blah,
[25:16] looks like I probably start talking around here.
[25:18] It's video, I'm gonna put it in.
[25:20] There we are, all right.
[25:21] It was doing that on this.
[25:22] So I could probably,
[25:25] there's something like this.
[25:28] So here we go.
[25:29] There's my clip.
[25:30] So I'm just gonna delete that part.
[25:34] In this video, I'm gonna put myself,
[25:38] in this video, I'm gonna put myself inside a helmet
[25:42] and hopefully there's no aliens around here.
[25:47] Blah!
[25:52] All right, sorry.
[25:54] Okay, all right, so there's my footage.
[25:57] Now I'm gonna go to Fusion.
[25:58] I make an extraction for this and a depth map.
[26:02] So I'm on the Fusion page.
[26:04] Here's my clip.
[26:11] I'm gonna have a single view.
[26:14] And then I'm going to grab one of my previous,
[26:20] I'm going to drag this,
[26:21] and I'm using a power bin.
[26:23] So this is one that I've already got earlier.
[26:25] So you can set up the power bins
[26:27] and then these go across projects, which is awesome.
[26:30] So there you go.
[26:32] I'm gonna open this one up.
[26:34] And I can look at my node setup and I'll go over this.
[26:37] I'm just gonna control C this one.
[26:39] And I'm gonna go to open the clips.
[26:41] And then this is basically me jumping
[26:42] onto the other project there.
[26:44] So I'm gonna hit V now.
[26:49] Yep.
[26:50] I changed my background.
[26:51] I'm gonna get rid of the clips now.
[26:53] So rather than the black background,
[26:56] I'm gonna put in my foreground.
[26:59] Oh, this one here.
[27:00] And then color correct, but I probably don't need that.
[27:06] That's a look.
[27:08] And then, oh, actually one thing I'm going to do,
[27:10] because we're gonna use this as an EXR sequence.
[27:15] So I am going to see how this looks in Unreal Engine.
[27:21] By going to, so if we bring in an EXR, it's linear EXR,
[27:25] but you need to change the color space.
[27:28] So you got the linear is the kind of container.
[27:32] Oh, that's the gamma.
[27:33] And then you've got the color space, how it ramps it down.
[27:36] Anyway, cut that bit.
[27:38] We go into VFX, IO, and then linear to SRGB.
[27:44] So this, if I brought this footage in now,
[27:47] as I, if I converted it to a, whatever it is,
[27:50] a, in the EXR sequence, this is how it would look.
[27:55] So we want to do some color corrections on this.
[27:56] Anyway, but before we do that, I'm just gonna get my keyer.


### Keying and Color Correction in Fusion [28:00]
**Transcript (timestamped):**
[28:01] I'm gonna turn this off.
[28:01] That's turns that on and off.
[28:03] So there's my keyer, so there's my footage.
[28:06] I've got a color correct on here.
[28:07] So I'm going to reset that.
[28:09] And then I've got a clean plate.
[28:12] And so, you know, to add a clean plate,
[28:15] C-L-E-A-N, clean plate here, add,
[28:19] and then you feed that into the background.
[28:23] Press two.
[28:24] Then I think you go and pick the color
[28:27] that you want it to be.
[28:28] My clean plate is, I think I could hold that one down.
[28:35] All right, anyway, this color, like this,
[28:38] that's my kind of, my color that I want to extend.
[28:42] Okay, here, okay.
[28:43] And then you grow edges like that.
[28:47] And then you fill, so it's a lot like that.
[28:51] And then we're gonna road it.
[28:52] So it's going to do more of this blue next to that.
[28:57] And then, so that's what I've got here.
[28:59] Now it's a different way of doing it.
[29:02] I'm slightly different, I don't know what the difference was,
[29:04] but it kind of works better with a slightly greener color.
[29:07] Anyway, there it is.
[29:08] And then I'm gonna push, put that into here,
[29:11] which is my Delta keyer.
[29:12] So I use a Delta keyer, just do Delta keyer.
[29:17] And then my background goes into the yellow one.
[29:21] And then my clean plate goes into this pink one.
[29:27] And I press two, and that's my result, off the bat.
[29:30] What did I do in this one?
[29:32] Okay, so here is my result.
[29:34] And then I'm just going to go and, oh, I see.
[29:38] Just click it and drag it.
[29:39] There it is.
[29:41] Great.
[29:45] There we are.
[29:46] Ooh.
[29:48] And this will be a little soft
[29:49] because it's a compressed, it's a webcam.
[29:51] Even though the webcam is actually my old Blackmagic camera,
[29:57] but a Blackmagic pocket cinema camera from 15 years ago,
[30:02] whatever it was, and I've got a little HDMI
[30:04] to USB converter on it.
[30:06] So there we are.
[30:07] All right, so that is my element.
[30:10] Press A, there's my alpha, there's my foreground.
[30:13] Now I've got color correct on it,
[30:14] but this is for when I do my picture in pictures,
[30:17] for when I do my YouTubes,
[30:18] but I'm going to convert this one.
[30:20] This is how it would look inside of Unreal Engine.
[30:23] So I can put a color space converter on it.
[30:25] So color, color space transform on here,
[30:31] and so I'm going to add that into the background,
[30:35] and then I'm going to put this into the foreground
[30:37] of this one.
[30:38] So this color correct doesn't have anything on it at the moment.
[30:39] So I've pressed two to view this one.
[30:41] And it's saying the input color space is that and that,
[30:45] and it's not input gamma is rec seven and nine
[30:47] and it's S RGB.
[30:49] So S RGB, there you are.
[30:53] So now we're converting this rec seven and nine G two four
[30:59] display referred color space,
[31:01] basically what it looks like as a JPEG on your monitor.
[31:04] And then I'm converting it to how it would look nice
[31:08] inside of Unreal, because when I convert it to a linear E XR,
[31:15] and then I'm displaying it with this linear to S RGB,
[31:17] because when you bring in E XRs,
[31:20] I think it kind of tone maps them to something.
[31:23] Anyway, that's how it works.
[31:25] Right, so there's my footage, press one and on this guy.
[31:31] And then I'm just going to make him,
[31:32] I've already got a little bit of gamma,
[31:33] a little bit of gain.
[31:35] Let's go and make him a little bit brighter,
[31:37] a little bit more gamma like that.
[31:40] And that's going to be me inside my helmet.
[31:45] And that, okay, great.
[31:49] Now, what I mean here,
[31:50] I will also make a depth mat as well.
[31:53] So just save all this, save project,
[31:57] because things crash.
[31:59] And I can process this and make a depth map


### Generating the Depth Map [32:00]
**Transcript (timestamped):**
[32:01] or I can do them at the same time.
[32:02] So let's just, let's be fancy.
[32:04] Troll space depth map.
[32:08] I think I keep calling it depth mat.
[32:11] And I'm going to use the non-color corrected version.
[32:15] And then press two on here.
[32:18] And then it should kind of work it out.
[32:20] Like it's last time I did it.
[32:21] It went, oh, look at that.
[32:22] That's amazing.
[32:23] That's just nuts.
[32:24] You can kind of see it in here.
[32:26] It's kind of working this out.
[32:27] It's got my nose, my mouth.
[32:29] And then like I said in the video,
[32:31] it likes, Unreal likes it to be inverted.
[32:34] And then what else we got?
[32:35] We got it on better and faster.
[32:38] So that's those two.
[32:39] And then I'm going to now make a write node.
[32:43] Oh, it's called saver.
[32:45] In my day job, I use Nuke.
[32:48] So I kind of keep forgetting what things are called.
[32:52] But I do, I love Fusion because it's pretty much
[32:55] the older functionality of Nuke besides
[32:58] that many percentage that super nerds use.
[33:02] And it's for like 300 bucks forever
[33:04] or three for most of the tools,
[33:07] which is, yeah, can't beat it, can you?
[33:11] Right, so I'm making a saver.
[33:14] And I'm going to browse and then put it in a certain spot.
[33:18] And then I'm going to make a directory in here, new folder.
[33:22] And it's going to be called what?
[33:27] It's called helmet depth.
[33:30] This one.
[33:33] Also just going to copy that.
[33:34] So helmet depth, put it in there.
[33:36] And I'm going to call it dish helmet depth dot dot EXR.
[33:41] So I'll put the frame numbers in between the two dots, save.
[33:44] And now I'm going to go to format.
[33:48] And when you tell it to be EXR,
[33:50] it defaults to this sort of compression,
[33:52] which is low compression, but we don't,
[33:55] we want high compression because this is great
[33:57] if you're rendering stuff or compositing
[34:00] and you need really high quality depth,
[34:02] depth maps and bit maps and stuff.
[34:03] But I don't, I'm just, you're going to make it
[34:06] 100 DWA compression.


### Exporting EXR Sequences [34:10]
**Transcript (timestamped):**
[34:10] So it's light and doesn't take up as much space.
[34:13] So there's my helmet.
[34:14] I'm going to copy this one, copy and paste it.
[34:18] And then I'm also going to call this one, go to my browse.
[34:22] So we're going to put this one helmet color.
[34:25] We're going to call this one new folder helmet color.
[34:32] Color, all right.
[34:34] There we are.
[34:35] Put it in there.
[34:37] Helmet color.
[34:45] And there we are.
[34:47] And then one thing I'm going to do,
[34:48] I'm just going to put it onto the media out.
[34:50] I don't need, well, it's not going to be,
[34:52] it's not going to affect any of these renders,
[34:54] but what I've noticed, I'm on version 21 of DaVinci Resolve
[34:58] and I've had it in the past where even though I've saved
[35:01] my project and it all looks good,
[35:03] if it's not connected to a media out,
[35:09] then it's not saved the fusion file.
[35:13] So that really scared me.
[35:15] So I make sure that I put it onto the media out
[35:18] because that seems to force it to save.
[35:20] If you want to save your fusion script just for yourself
[35:24] and we want to move it to another project,
[35:26] you can just go file, export, fusion composition, like that.
[35:32] And I tend to do that as I go through and work anyway,
[35:35] just as a double backup.
[35:38] Oops.
[35:40] Double backup.
[35:43] Put it in fusion two.
[35:45] I'm just going to put it in there.
[35:46] Cool, what was this one?
[35:47] This is just a comp and blue screen.
[35:53] And I'm going to now go fusion render all savers.
[35:58] Yeah, so I'm going to render these out.
[36:00] It's going to take five minutes.
[36:01] And while that's happening,
[36:03] I'm actually going to go and do a task and come back later.
[36:08] Okay, so both of those are rendered
[36:10] and now I'm going to do one more thing.
[36:11] And that is render out sound
[36:14] because that way I've got something as a reference
[36:17] inside of Unreal Engine to know what my animation is saying
[36:20] at the same time.
[36:21] And so it's good to have a sanity check too
[36:23] because these are actually recorded at 30 frames per second
[36:26] on my video camera.
[36:27] As normally I record on my Ursa Blackmagic at 24 frames
[36:31] and I do everything at 24 frames,
[36:33] but my camera kind of acts a bit weird at 24.
[36:36] So I have to kind of do it at 30 then compress it.
[36:39] It's exciting.
[36:41] All right, anyway, so it was recorded at 30.
[36:44] So I'm going to do my timeline at 30.
[36:46] Here's my audio.
[36:47] I'm going to export my audio by going into my out here,


### Exporting Audio for Unreal [36:50]
**Transcript (timestamped):**
[36:51] my right stuff out.
[36:53] And then I'm going to go and I've got an export here.
[36:57] Oh, except you can't see it's going on the other screen.
[36:59] Wave for Unreal file.
[37:01] And so I'm going to go and just go into the audio section
[37:05] and export audio as a waveform at linear PCM 48,000,
[37:11] sample rate depth 24.
[37:13] And the important part is the output track.
[37:16] So it will default to a timeline track
[37:20] and it'll be number one, which is this one.
[37:23] In this case, it'll actually be fine.
[37:24] That'll work.
[37:25] But sometimes your audio might be split over several tracks.
[37:29] So I'll often change it to just boss one.
[37:32] Then I'm going to put it somewhere
[37:34] that I'll be able to find it.
[37:36] Let's get into it.
[37:37] I'm going to put it actually with the render of the color.
[37:40] And I'm going to call it AA.
[37:44] No, I'm going to call it audio.
[37:46] Audio, audio, audio, helmet color.
[37:51] And then no extension and it'll add a dot WAV to it.
[37:55] And then add that to the render queue.
[37:56] And so I've got video is off on this track.
[37:59] It's just the audio.
[38:01] And then I hit render all.
[38:02] And then that's it, it's done it.
[38:04] Okay.
[38:05] Then I'm going to come out of this now
[38:09] and go into Unreal Engine, which is actually still open.
[38:13] So let me just lower this down.
[38:15] And then if I go into my helmet color
[38:19] and double click on this one.
[38:21] And this video, I'm going to put myself inside of it.
[38:23] And then I can hear it here.
[38:24] And hopefully there's no aliens around here.
[38:29] Great.
[38:30] Right.
[38:31] So step two is done.
[38:34] So we've done one, we've got our model
[38:37] and we've set up partial amount of the composure.
[38:42] And now we're going to bring in those tracks.
[38:43] So go to content browser, go to my blueprint,
[38:49] go to my level.
[38:52] What was this one called?
[38:54] Helmet, that was the one.
[38:55] And so in here, I'm going to make a directory new folder.
[38:57] I'm just going to call it media.
[39:02] If you press two, F2 media, it'll give you the option
[39:09] to rename and then right mouse button,


### Importing Media into Unreal Engine [39:10]
**Transcript (timestamped):**
[39:11] import to current folder.
[39:13] Now I'm going to go and find those files.
[39:16] And they were in here.
[39:19] So I'm going to go and grab,
[39:22] actually let's go and grab the helmet, the way file first.
[39:27] There we are.
[39:28] So now we've got our way file in here.
[39:29] Now I'm going to bring in the image media source,
[39:33] right mouse button, media, image media source.
[39:40] And that's what you use for EXR sequences or PNGs.
[39:45] I don't use those.
[39:47] IMS and we call this one helmet color.
[39:54] Here we are.
[39:55] And then double click on that.
[39:56] And then it's going to look for,
[39:58] under here sequence path, it's going to look for those files.
[40:00] So we're going to navigate to where I just render those out
[40:03] to and then you click on the first frame and then hit open.
[40:08] And then if you press this button here,
[40:09] this will actually open the clip.
[40:11] There I am.
[40:13] Beautiful.
[40:14] Okay.
[40:15] And then it's safe.
[40:18] I'm hoping there's an alpha is black,
[40:19] but normally it should have an alpha with that.
[40:25] I'll see if it's rendered an alpha.
[40:27] Yes, it did.
[40:28] Yes, I'm sure it did.
[40:29] All right.
[40:30] And I'm also going to bring in the depth now.
[40:31] So media, image media source, IMS, helmet depth.
[40:41] So click on that one.
[40:43] Go to the directory that they're in.
[40:48] Got the first frame.
[40:49] I just press that just to check it.
[40:51] There we are.
[40:52] And like I said on the last video,
[40:54] this doesn't have to be the same size as the color,
[40:59] but it does need to be exactly the same aspect ratio
[41:02] so that you can scale it and it'll fit on top.
[41:04] But it'll save you, give you a bit more performance
[41:07] if it isn't, if it's smaller.
[41:10] Right.
[41:11] So there's those two.
[41:12] Now we go into sequencer and what I'm going to do
[41:15] is I'm going to use that rather than this picture,
[41:19] which is using a texture of the color bars,
[41:24] I'm going to grab my composite depth mesh act down.
[41:27] We're going to change this for the color
[41:28] that I just rendered as a media track
[41:30] rather than this depth texture here.
[41:32] Oh no.
[41:33] So that'll be the color.
[41:34] And then under the depth texture of this asset,
[41:37] we're going to put in another track for the depth.
[41:40] So I'm going to add those right now.
[41:42] I'm going to get to my first frame.
[41:45] All right, we'll start at zero, zero, zero, zero, zero.
[41:47] That'll do.
[41:48] And then I'm going to go to add media track.
[41:54] And then under media, hit plus media source.
[41:57] And it can look for that file media source
[41:59] or image media source and we call it helmet color.


### Linking Media Textures to Sequencer [42:00]
**Transcript (timestamped):**
[42:04] And then this is great in five eight.
[42:06] It now creates the texture for you.
[42:08] So you hit create texture,
[42:10] and then put that into my,
[42:15] into here.
[42:16] And I'm going to call it, I'm just going to click on that.
[42:19] And I'm going to change it from IMS just to MT.
[42:22] So it's media texture.
[42:23] Save that one.
[42:24] So there we are.
[42:25] So 24 frames per second and the sequences at 30.
[42:28] Oh, it's actually, it's saying that's 24 frames.
[42:31] Okay.
[42:34] I don't know if it is or not.
[42:35] I see, because I rendered it out at,
[42:37] my video web camera is 30 frames per second,
[42:40] but my project was up to 24.
[42:44] So when I ran my files out through,
[42:49] whatever it is, fusion, even though they're at 30 frames,
[42:52] it might have just told it that it was 24.
[42:54] So we'll see what happens.
[42:57] And then I'm going to do the same
[42:58] with the other track as well.
[43:01] So I'm going to add a second track,
[43:03] come back here for media track
[43:06] and second media track for our depth,
[43:08] plus media source and then helmet depth.
[43:13] There we are.
[43:14] We're going to create a texture.
[43:15] Do the same.
[43:16] Why doesn't it remember that?
[43:17] We're going to do the same.
[43:20] This one, click on that one.
[43:23] Call it MT.
[43:25] And there we are.
[43:26] So we've got our two now.
[43:29] And then in this, for this video track,
[43:32] where it says texture,
[43:33] I'm going to change this now to this media source.
[43:37] So we're going to here,
[43:39] and then I'm going to type MT,
[43:40] because I called them MT and then helmet color.
[43:43] So now it's projecting that helmet color on there.
[43:45] And then in, I'm selected composite depth mesh actor.
[43:48] In here, where I've got my temporary depth texture,
[43:52] I'm going to select this media texture.
[43:55] So MT, helmet depth, like that.
[43:59] Oh, there we are.


### Finalizing the Composite Setup [44:00]
**Transcript (timestamped):**
[44:01] And now, yeah, so media textures,
[44:05] what they do is they will read,
[44:07] per, they will read whatever this is pointing to,
[44:11] the media texture,
[44:12] and it's pointing to this media track.
[44:17] So as you move forward,
[44:19] there we are.
[44:20] Look at that.
[44:20] That's kind of, look at my head.
[44:22] All right, anyway,
[44:23] I'm just going to scale this up a bit
[44:24] and put me a little bit back in here, like that.
[44:28] So we can turn off our actor now.
[44:31] Let's go into here and under my blueprint,
[44:35] if I go, I can expand this and look in here.
[44:38] So we've got, where is he?
[44:40] There's his head here.
[44:42] So we can go into that sub object, I guess.
[44:47] And then I'm going to look for visible,
[44:51] visibility and turn that off.
[44:54] So that's just me in there.
[44:56] And now, there we are.
[44:59] Oh man, that's not bad, is it?
[45:01] That's a bit not.
[45:03] Look at that.
[45:07] Oh, that's crazy.
[45:10] Oh dear, look at that, that's great.
[45:12] Now, I think I'm default to unlit.
[45:16] So let's go and put me over here a bit.
[45:19] We need to crop this bit out here.
[45:23] And probably, he's about the right size.
[45:27] And so, there we go.
[45:30] All right, what I might do is, look at the alpha.
[45:35] So the alpha is working then.
[45:43] Right, so I'm going to select my composite depth mesh actor
[45:46] and then under here, turn is hold out enabled off
[45:49] and now it should get the lighting from the scene.
[45:51] Oh, there we are.
[45:53] So actually getting the correct lighting now.
[45:56] But he looks a bit shiny.
[45:58] I know I'm shiny because he's hot today,
[46:00] but I'm not that shiny.
[46:02] So I'm going to grab my composite depth mesh actor
[46:05] and drag that into the sequencer.
[46:09] And that way, I can expose the material of this
[46:13] that rather than duplicating the material
[46:15] and editing it in the material.
[46:17] So hit plus, then we go to default components,
[46:21] default composite mesh component.
[46:23] And then under that, we can then go into the material,
[46:26] material parameters, slot zero.


### Adjusting Material Parameters and Lighting [46:30]
**Transcript (timestamped):**
[46:30] And then under that, you've got your metallic,
[46:33] roughness, scale factor, all these things.
[46:35] I'm going to click on all of them.
[46:37] So it'll just add all of them and then wiggle them
[46:40] and see which one makes it look good.
[46:45] Scale factor, to change that,
[46:46] I'm not going to animate the scale factor.
[46:48] So that procedure normal looks a bit weird.
[46:51] Okay, all right, so one, let's make,
[46:55] what's this one doing?
[46:56] All right, okay, let's this one do.
[46:59] Okay, metallic, we don't want him to be metallic
[47:02] and we want the roughness
[47:03] because we want him to be not rough like that.
[47:07] Speculer, let's bring you down.
[47:10] Okay, so roughness one, specular,
[47:13] proceed metallic and make you zero.
[47:15] Okay, now procedure normal, let's whack that one up.
[47:20] Okay, let's take my directional light
[47:30] and then rotate this around
[47:32] and then we should get some light on my face.
[47:34] Oh man, that's nuts.
[47:36] That's pretty good.
[47:39] Okay, now go into here,
[47:42] let's go ahead and hide this light.
[47:44] All right, what I do to hide my light,
[47:46] I can press G to hide it,
[47:49] but I like to just select my light
[47:51] and then go into look forth mesh in here
[47:55] and under you've got the camera mesh
[47:57] and I'll just clear it.
[47:59] So don't have to have the icon there being annoying.
[48:03] Right, so there's my,
[48:05] oh, there's my, that's my projection camera.
[48:07] Let me move him over,
[48:09] let me just move my head over a bit.
[48:13] Where are we?
[48:14] Where's my composite mesh actor?
[48:17] Just get to move him over a bit
[48:20] and probably push him back a bit more.
[48:31] Turns out, where are you?
[48:32] Where's my, oh, I'm gonna hit M.
[48:37] Oh no, it's alt, alt M.
[48:38] You can get that you can,
[48:41] oh, well, you won't matter where that one is,
[48:44] well, it's actually my,
[48:45] which one do I need to move?
[48:46] All right, hang on.
[48:50] That's not that one, it's my projection
[48:52] because this is projecting onto an image
[48:54] that's attached to the camera.
[48:55] So I need to actually grab my camera
[48:57] because it's being projected from this camera.
[49:00] Gets a little confusing, doesn't it?
[49:01] Transform.
[49:02] So now there we are.
[49:03] All right, so there's our projection camera.
[49:11] There we are, I'm pushing back a little bit.
[49:17] And we can add a mask to this as well
[49:19] with the new masking layer, so I can crop that out.
[49:22] But for now, let's just leave this in here.
[49:24] So, all right, so I'm gonna move my head over there.
[49:31] Let me make sure I'm...
[49:32] Okay, now change my directional light,
[49:35] I'm gonna make my shadow softer.
[49:37] So I can get rid of some of this, so let's make it 50.
[49:40] There we are, let's go for 30, 20.
[49:56] Okay, so you've got a little bit of footage
[49:59] Okay, so you've got a little bit of space,
[50:04] but not too much because I'll break it.
[50:07] Let's go and shrink this in a little bit.
[50:11] So I'm going to grab my composite depth mesh actor
[50:15] and then under my plate layer,
[50:17] I've got some things I can add.
[50:18] So I can add under media passes, hit plus,
[50:24] and then let's go for masking.
[50:27] So let me, in fact, I can add another mask.
[50:29] Let's go for a mask,
[50:31] and then I can add another texture here.
[50:33] So I need one that's just cropped out a little bit.
[50:36] So I wonder if I can find a square.
[50:39] I wonder if we've got a square somewhere.
[50:41] That's a lot, there's a gray,
[50:42] so that's gonna make me a bit more transparent.
[50:45] I need something a bit more like this,
[50:47] but it's gonna have a hole in the middle there,
[50:50] so that's no good.
[50:52] Maybe I've got a sphere, a circle.
[50:54] Is there a circle in here?
[50:56] There it is.
[50:57] Go into my masking again.
[50:59] Now change this, I can just drag that into there.


### Adding Custom Masking [51:00]
**Transcript (timestamped):**
[51:02] There we are.
[51:04] There we are.
[51:05] Sequencer.
[51:08] There we are.
[51:08] Bum, bum, bum, bum, bum, bum, bum.
[51:10] I was gonna turn our animation on.
[51:11] Oh no, before I turn the animation on,
[51:13] because if I turn the animation on,
[51:14] this head will just stick here.
[51:16] So I will, I'm gonna turn these on.
[51:19] So there we go.
[51:20] So it's left the head behind,
[51:21] and you see the head back there.
[51:22] So what I want to do is I want to turn off my animation,
[51:25] and I want to parent this head to the object,
[51:29] to the head object in here.
[51:30] Probably actually not the head,
[51:31] probably the pelvis or, well,
[51:34] it's gonna need to be stuck to the chest.
[51:36] So let's find that spine three.
[51:38] And then I'm also going to parent the camera
[51:43] to the same thing.
[51:44] So we need to create a null,
[51:45] so I can parent my camera and my projection,
[51:49] composite projection mesh and my camera
[51:51] onto another thing,
[51:52] so I can move them both at the same time.
[51:54] And I might need to add another node under that,
[51:56] so I can offset it relative to those two.
[52:00] So I will do.
[52:01] So I'm going to go and just go for tools.
[52:03] No, not tools, square plus button,
[52:06] whatever that's called, basics add an actor,
[52:09] and then go into its position, just reset it.
[52:12] So it is at zero, zero, zero, zero.
[52:14] So actually, do I want it there?
[52:15] I probably don't want to put it there.
[52:17] I want to put it, oh, here's it, zero, zero, zero.
[52:19] So let's put him up here.
[52:21] So that's where he's going to go here.
[52:26] So actor one, so I'll call this my position, root, root,
[52:33] root projection.
[52:36] Okay, now I'm going to duplicate that,
[52:40] edit duplicate, and I'm going to call this one
[52:44] projection offset, offset, offset projection.
[52:52] And I'm going to make him a child of that one.
[52:54] So there's my root projection,
[52:56] and then on the same spot, I've got my offset projection.
[52:59] Now I'm going to parent my composite depth mesh actor,
[53:02] and he's movable, onto my offset projection.
[53:06] And I'm going to parent the camera that I'm using.
[53:10] This is our camera that we're using to project
[53:13] onto the same root there.
[53:15] So now if I take this root projection,
[53:19] and I should be able to just move this around,
[53:21] everything goes with it, great.
[53:23] Okay, so now we're going to parent this
[53:26] to the static mesh, no, the skeletal mesh,
[53:30] and that skeletal mesh is the astronaut body.
[53:33] So we go right mouse button, parent, where's parent,
[53:37] attach, is it called attach parent level, transform,
[53:42] where is it, I forgot what it's called now.
[53:48] I think I just might just drag it onto it.
[53:50] I think that's what I do.
[53:51] I can't remember.
[53:53] Right, so drag that onto here.
[53:56] No, that's parented to that one.
[53:59] How do you parent it?


### Parent Camera and Mesh to Character Bone [54:00]
**Transcript (timestamped):**
[54:00] I've forgotten, where's the parent, so attach,
[54:02] where's attach, oh, attach to, sorry, there it is.
[54:05] Okay, so I've grabbed my root projection,
[54:09] that's all my little collection of bits there.
[54:12] Right mouse button, attach to,
[54:14] then find my static mesh under here.
[54:17] I wonder if it'll say,
[54:18] oh, it's not saying which one to go to.
[54:21] So I wonder how I do this.
[54:22] I wonder if I've got to attach it in here.
[54:27] Yeah, because it's going to the actor,
[54:29] not the exposed actor.
[54:30] So this, in here, I wonder if I can,
[54:33] I don't think I can drag it onto here, can I know?
[54:36] Let me unattach this.
[54:39] Right, oh, no, you're attached, let's go to here.
[54:41] Detach this, oh, get off.
[54:44] Right, just, I'm detaching them again.
[54:47] So they're detached.
[54:51] Root projection, no, I can't do it like that.
[54:54] All right, so I'm going to drag the root projection
[54:55] into the sequencer, and I'm going to try it from here.
[54:59] So root projection, go to attach,
[55:03] attach to this actor.
[55:06] Oh, great, okay, so now I can do it to the body, okay,
[55:10] and then which part of the body?
[55:11] Let's go for spine three, okay, now it's pushed it off,
[55:15] but I think if I just refresh it,
[55:17] I'll move it in the right spot.
[55:19] Oh, no, let's see what happens here.
[55:21] It's from my animation, is that,
[55:23] so that is, looks like it's moving.
[55:25] All right, so now we'll grab this guy here,
[55:30] and I'm here, so if I move him, let's go for reset there.
[55:35] Okay, so he's attached to that bone,
[55:38] and maybe I can push him up, oh, here we are, all right.
[55:42] And then rotate him around, runway,
[55:46] go that way like that.
[55:50] See what he looks about right there.
[56:02] Back a bit, and come into here now.
[56:12] Selecting that guy.
[56:29] Okay, now I wanna get rid of this ugliness around there,
[56:33] so let me think, it's stretching that
[56:37] because it's got a soft edge, so I'm just going to,
[56:40] oh, here we go, I am,
[56:53] just gonna select something else.
[56:55] I am going to go into this composite depth mesh actor
[57:00] under media passes, I'm gonna hit plus,
[57:04] and then do a dilation, before I do that though,
[57:08] I'm going to change off the, let's go to my media pass,
[57:11] and I'm going to, it's like add a pre-mult or un-pre-mult,
[57:15] I'm not sure which one it is, so let's try pre-multiplied.
[57:20] One of these will kind of get rid of that edge,
[57:23] not quite sure, all right, let's go media passes,
[57:25] let's add plus, dilation, and then we're gonna dilate,


### Fine-Tuning Alpha and Dilations [57:30]
**Transcript (timestamped):**
[57:31] it's gonna make it look crazy,
[57:32] gonna dilate just the alpha,
[57:37] so I'm gonna turn off the others, there we are,
[57:40] so now we've made our alpha bigger,
[57:43] yes, and we're gonna make him smaller,
[57:46] so we're gonna shrink him in a bit, there we are,
[57:47] so that's gonna eat on those, eat those edges up,
[57:51] and then we're going to add a blur note as well,
[57:53] so add a blur, and so we're going to just blur this,
[57:57] gonna go crazy, just to show it's blurring everything,
[57:59] so I'm gonna turn it from, where are you,
[58:04] advanced alpha only, so I'm just gonna blur that edge a bit,
[58:10] and what you could do as well,
[58:11] rather than making me blue screen,
[58:13] you could probably put the back part of the helmet
[58:16] over here, like a dark area, that's pretty what I would do,
[58:20] and then that way you've got some of that
[58:24] in the environment, actually in the shot itself,
[58:28] so yeah, maybe do a soft edge on that,
[58:31] like so you've got an area back there,
[58:34] and then, because it's gonna be dark in there,
[58:36] so yeah, maybe, all right,
[58:39] and now I'm gonna shrink that in a bit,
[58:42] so make that blur a little bit less bad,
[58:45] oh okay, so now, isn't there one where it carries on,
[58:48] the dilation, I think there's a button that carry,
[58:54] there we are, this one, carry RGB with alpha,
[58:57] so we turn that one off, and there it is,
[58:58] it's sort of expanded that edge a bit,
[59:01] so there we are, I'm still seeing this, why is that,
[59:05] it's my masking, why is that coming through there,
[59:10] is this not on, oh no it is on,
[59:12] I just need to shrink that down a bit,
[59:14] all right, let's go back into resolve,
[59:19] change this a bit smaller,
[59:23] like that, and then,
[59:28] infusion,
[59:32] render savers, blah blah blah blah blah blah,
[59:34] cancel, yes, so now, and then I come back into here,
[59:41] and then, select this, and then just re-import,
[59:47] where is it, re-import,
[59:48] and it should shrink it down a bit,
[59:53] and porting that to here, great,
[59:58] there's my custom mask,
[60:01] got that bit there, this'll do, for now, all right,
[60:04] oh no, I'll edit it in a bit, oh no, it was okay,
[60:11] and let's just extend the length of this to,
[60:15] match my media track, which it does, okay, great,
[60:25] okay,
[60:28] okay,
[60:42] that's pretty neat,
[60:49] let's go hide the floor,
[60:52] let's go hide the sky, clouds,
[60:58] atmosphere, oh look at that, now I'm in space,


### Setting up the Space Environment [61:00]
**Transcript (timestamped):**
[61:03] skylight, we can increase the skylight brightness,
[61:09] is that working, is that doing anything,
[61:11] oh no, I think I need the sky atmosphere for that,
[61:13] don't know, okay,
[61:17] let's turn it off,
[61:19] just gotta move this around,
[61:29] okay,
[61:33] that material isn't awesome,
[61:37] it's doing some weird stuff,
[61:40] I made that one,
[61:43] okay,
[61:45] I can increase the resolution of this times two,
[61:52] so this is our mesh, that is projection mesh,
[61:56] and I've increased that resolution,
[61:59] so it should make it a finer amount of bits,
[62:05] technical term, I'm always gonna crash,
[62:10] don't crash,
[62:11] okay,
[62:24] oh no, it's doing it,
[62:25] a few,
[62:25] I'm running out of memory then,
[62:37] let's save this,
[62:42] there we go,
[62:47] yeah, I like it very much,
[62:48] the sky sphere in here, the volumetric,
[62:51] which one is it, sky atmosphere,
[62:52] which is one that's adding the most contribution,
[62:59] what's your, what's it, skylight,
[63:03] was it you, oh that's why,
[63:05] I've got my intensities too low,
[63:07] my intensity's too low,
[63:09] give it one,
[63:10] two,
[63:11] three,
[63:12] two, like that one,
[63:13] and there's this volumetric,
[63:16] ray trace,
[63:18] cast ray trace shadows,
[63:19] that's enable that one,
[63:20] so I should work better,
[63:22] let's go for my directional light,
[63:24] I'm gonna make him ray trace two,
[63:26] ah, there, that will help,
[63:29] and then let's go and change the source angle now,
[63:34] I think it can be smaller,
[63:38] and then I can bump,
[63:41] bumpy because of my material here,
[63:45] this procedural normal,
[63:46] so we increase that one,
[63:47] that'll get rid of that,
[63:49] but it's blurring it,
[63:50] so it's not the most accurate thing,
[63:53] but there we are,
[63:53] that's without any blur,
[63:56] so he's going to give that a blur,
[64:01] like that,
[64:02] and since he's got animation,
[64:13] and what have you,
[64:16] we can actually just move him around,
[64:19] actually if I do this in the sequence,
[64:20] so it doesn't,
[64:21] if I have to update it,
[64:22] oh, okay, that's interesting,
[64:23] he's moved you,
[64:25] he's moved you,
[64:27] oh, why is he not,
[64:28] oh, it's because I didn't save a key for this,
[64:31] okay, all right, that's interesting,
[64:33] so I moved him,
[64:34] and he's moved him around,
[64:38] my root projection,
[64:41] oh yeah, look,
[64:42] he didn't save the key,
[64:43] so I needed to save a key,
[64:44] all right, important to know,
[64:46] let's go back to my stop frame,
[64:49] and let's just move this up,
[64:52] rotate him around,
[64:55] like so,
[64:56] so,
[64:57] about 270,
[64:58] I like to do it in,
[64:59] oh, 19,
[65:02] nope, minus 19,
[65:05] okay,
[65:09] there we are,
[65:11] make sure I'm inside my helmet,
[65:13] I sure, yeah, I wouldn't go too far out, would I,
[65:15] because I wouldn't be able to go through the class,
[65:26] oh, I'm gonna save it,
[65:29] so, root projection,
[65:31] drag that,
[65:32] oh, he's already in the sequencer, of course,
[65:33] and then I'm gonna hit plus,
[65:36] transform,
[65:37] and then under transform,
[65:39] just save a key,
[65:40] so now,
[65:41] if I move,
[65:42] fingers crossed,
[65:43] if I move my,
[65:47] astro, the whole thing,
[65:49] and put an offset on there,
[65:51] not that I want to,
[65:52] I want to kind of animate the body,
[65:53] but for now,
[65:55] let's just go add a transform onto this,
[65:59] and then if I go into this transform,


### Animating Camera and Head Position [66:00]
**Transcript (timestamped):**
[66:00] it should all go with it,
[66:01] there we are,
[66:03] whoa, I'm floating, hello,
[66:06] now a bit long in the face,
[66:09] so, to adjust that,
[66:11] I would go into,
[66:15] into fusion,
[66:18] and change the contrast of this map,
[66:20] and I'm hoping that they will add a,
[66:24] some sort of,
[66:25] something into the composite depth mesh itself,
[66:28] so we can change that value here,
[66:30] because I thought that's what this scale was,
[66:32] but that's the overall projection scale,
[66:37] so there we go,
[66:38] all right, so there's my thing,
[66:39] and then here we go,
[66:40] so you'll see that it'll break,
[66:41] depending on how much room you've got,
[66:44] but the nice thing is,
[66:45] is the lighting,
[66:47] kind of works for being inside this thing,
[66:52] like that,
[66:54] I think, you know,
[66:55] if I was doing this properly,
[66:55] I'd have,
[66:56] yeah, like the back of the helmet,
[66:58] or at least something to kind of constrain me into that,
[67:02] so yeah, maybe just,
[67:03] hold yourself down and do that,
[67:06] and get actors in here,
[67:07] now, just to check my frame rate,
[67:09] I'm gonna bring in my audio clip,
[67:12] where is it here,
[67:13] and then I'm going to add that into my sequencer,
[67:15] so I'm going to go to my first frame,
[67:17] under add,
[67:18] audio track,
[67:21] and then under audio,
[67:22] plus, and find that one,
[67:25] which one was it,
[67:26] what was it I called it?
[67:27] Audio helmet color,
[67:28] so,
[67:32] because I think it might be off on the timing,
[67:34] I think it might have to set the timing of this onto 24,
[67:37] let's see how I go,
[67:39] I can't hear anything,
[67:41] hello, hello, hello, hello,
[67:47] it's gonna turn my clouds off,
[67:49] volumetric cloud,
[67:51] okay, let me go for exponential height four,
[67:55] okay, so we want that one on,
[67:56] as if there's earth beyond there,
[67:59] and what was the other one, sky atmosphere,
[68:00] I don't tend to use the sky atmosphere,
[68:03] but let's have a look at this thing,
[68:09] well, I guess it's time to learn it,
[68:11] turn these down,
[68:14] so I turn it off,
[68:20] is that the same just turning off?
[68:22] I've got some,
[68:23] I'm getting contribution,
[68:25] that's what I want,
[68:26] I want contribution from the skylight,
[68:29] so if I turn that off,
[68:30] do I get any contribution,
[68:31] so I don't get any contribution,
[68:33] so I need sky atmosphere on,
[68:35] let me turn that thing,
[68:37] maybe I delete it,
[68:39] okay, so you're there,
[68:49] oh, ground albedo,
[68:51] is it this one,
[68:52] there we are,
[68:53] and let me if I can move that down,
[68:55] we can hint that there's an earth below us,
[68:57] ground radius,
[68:58] so that's what I want,
[68:59] oh, I see,
[69:00] let's,
[69:02] okay, ground radius,
[69:06] is there a height,
[69:07] atmosphere height,
[69:09] okay,
[69:10] well, an advanced,
[69:14] yeah, I've never used that one before,
[69:17] can I move it,
[69:20] let's go, minus 600,000,
[69:23] oh yeah, you can move it,
[69:25] all right, well, that's pretty bit low,
[69:29] let's go minus 20,
[69:31] so if I hint at that,
[69:34] here we are, open space,
[69:36] okay, and I'm getting a little bit too much
[69:39] of this funkiness here,
[69:41] I thought I saved that,
[69:44] procedural normal,
[69:45] let's go on,
[69:47] have it a bit lower,
[69:48] okay,
[69:59] you change the resolution of this,
[70:00] okay,
[70:03] nine,
[70:05] what was it,
[70:05] it was 960 by 540,
[70:18] okay,
[70:19] let's see if I make it smaller,
[70:21] make it smaller,
[70:22] what's it gonna do,
[70:23] I think I have to update this as well,
[70:25] no time,
[70:26] oh, let's get rid of that key frame,
[70:38] I'll turn that,
[70:48] okay,
[71:15] oh, interesting,
[71:19] that's kind of interesting,
[71:21] what was it in there,
[71:22] so very low procedural normal,
[71:24] what was the procedural normal,
[71:27] oh, interesting,
[71:29] roughness,
[71:33] yeah, wiggle until it looks good,
[71:35] I don't know why,
[71:37] but for some reason,
[71:39] that looks way better,
[71:41] save this,
[71:44] and then hit that one there,
[71:46] and then delete those there,
[72:03] and of course,
[72:04] I'd be dead at this point,
[72:05] because my mask's open,
[72:07] so we've got the character in place,
[72:08] and I just wanted to show you the character
[72:10] where he came from,
[72:11] and I bought him off the fab store,
[72:14] and this is a modular character,
[72:15] which I've never tried before,
[72:17] so that was all new for me,
[72:19] and there we have it,
[72:21] so go and buy yours today,
[72:24] okay,
[72:25] now,
[72:26] one thing I wanted to do,
[72:27] that I've just done offline without you,
[72:29] is I took the little helmet,
[72:32] and I've added a rotation in here,
[72:35] and then we've got the second helmet underneath,
[72:40] so that I can not die in space,
[72:43] space,
[72:44] here we go,
[72:45] so,
[72:46] what else shall I do?
[72:48] I think next,
[72:51] here's my character,
[72:53] I should move that down a touch,
[72:54] let me just go to here,
[72:55] it's not quite,
[72:56] I had to kind of cut it and attach it in a strange way,
[73:00] so this wasn't quite working exactly how I wanted it,
[73:06] oh, what's wrong?
[73:08] Let's go into the curves,
[73:13] and let's just go and adjust this curve
[73:15] a little bit so that I'm not poking out so much,
[73:17] oh, that's my rotation,
[73:20] there we go,
[73:21] and then let's see,
[73:22] I go to my location,
[73:24] which one's that one?
[73:25] There's my Y,


### Final Camera and Animation Pass [73:30]
**Transcript (timestamped):**
[73:30] flink,
[73:31] flink,
[73:32] flink, flink, flink, flink,
[73:34] that'll do,
[73:34] that's enough,
[73:35] okay,
[73:36] now I'm gonna add a camera,
[73:39] just go to perspective,
[73:41] cinematic,
[73:43] create camera,
[73:44] cine camera actor,
[73:47] and I'm going to drag him into the sequencer,
[73:50] let's give him a name,
[73:52] CM space shot,
[73:57] drag that into here,
[73:58] and then that should have automatically added it up there,
[74:01] but let's go and grab this one here,
[74:04] and let's move him up,
[74:06] oh,
[74:07] can I move him to the top?
[74:11] Where is it?
[74:13] Yeah, it's gonna move him up there,
[74:14] so it's easier to grab,
[74:15] okay,
[74:16] there it is,
[74:17] I'm looking through that camera now,
[74:19] because he's a cine camera actor,
[74:20] I can change the
[74:24] focal length,
[74:26] and then that,
[74:28] where it's focused on,
[74:31] change the aperture,
[74:33] I am going to go into the camera settings,
[74:38] and change the minimal f-stop,
[74:41] minimal f-stop,
[74:43] there should be a minimal,
[74:47] minimal focal length,
[74:48] minimal f-stop,
[74:49] so I'm gonna make that point two,
[74:50] so I can go over it,
[74:52] so I can make it more and more out of focus if I want,
[74:56] actually look at that,
[74:57] that's going,
[74:58] so I need to change the transparency of the glass to after,
[75:05] but I'm actually gonna have it quite deep focus,
[75:08] let's go like that,
[75:09] okay,
[75:11] and then what else am I going to do?
[75:15] Let's look at the animation,
[75:16] so it's gonna go,
[75:17] jump,
[75:18] blah, blah, blah, blah, blah, blah, blah,
[75:21] and I'm gonna animate my head over,
[75:23] because I'm banging into the side of this,
[75:24] so let me turn that off,
[75:26] let me just go into here,
[75:29] yeah, we're getting a bit too close to the edge,
[75:31] so comes up,
[75:32] there he is,
[75:34] let's go and select my route projection,
[75:37] let's save key for those,
[75:40] there he is,
[75:41] there,
[75:42] just have him there,
[75:43] actually it's having like that,
[75:45] as he moves across there,
[75:47] like I said,
[75:47] my whole body moves,
[75:48] I think if you're doing this properly,
[75:50] you'd kind of create a little rig or something,
[75:52] put the interior helmet,
[75:55] it's gonna push him over a bit,
[75:56] so it doesn't go too far,
[75:59] there we are,
[76:00] jump,
[76:02] push him out there,
[76:04] no,
[76:05] push him out there,
[76:12] jump,
[76:22] oh, I don't wanna bring him too far forward,
[76:24] there we're getting that,
[76:25] he's poking through,
[76:30] this is amazing though,
[76:31] that I'm getting the shadow from this
[76:33] onto the head,
[76:34] in here that,
[76:36] that's just great,
[76:37] and then as he pokes through the glass,
[76:41] that's just undo that,
[76:49] right here,
[76:57] ooh,
[76:58] all right,
[76:59] let's push him over here a bit more,
[77:01] oops,
[77:02] like that,
[77:09] okay,
[77:12] let's kind of have our camera,
[77:14] a bit more,
[77:15] where is my camera,
[77:16] oh, there he is,
[77:17] I'm sort of looking down like that,
[77:21] and that's what I'm,
[77:23] I'm gonna put him in there,
[77:24] I'm gonna put him in there,
[77:25] I'm gonna put him in there,
[77:25] so,
[77:32] I'm gonna clip in my mask a bit more,
[77:41] let's go and grab my sequence curves,
[77:44] and let's go and grab my location,
[77:49] let's wind it up,
[77:50] that's amazing,
[77:51] so if I took my light,
[77:57] now I just rotated it around,
[78:01] there he's going into shadow there,
[78:04] and there he is,
[78:05] it's on his face,
[78:10] so that's pretty neat,
[78:12] let's do that with the lighting,
[78:13] and then what I might do,
[78:14] is I'm just gonna make the intensity of that light
[78:17] a little less,
[78:17] so I can see that light a little less,
[78:19] so let's make him like six,
[78:20] because this is all gonna get blown out,
[78:22] so let's make him less than that,
[78:25] no, let's keep him like that,
[78:26] because what I can do now is my face,
[78:28] it looks,
[78:29] wanna brighten that up a bit,
[78:31] so I'm going to go into my composure,
[78:33] composite depth mesh actor,
[78:36] then under the composure tab,
[78:39] we're going to add,
[78:40] I'm under the plate,
[78:42] and we're going to add,
[78:43] A plus,
[78:45] color grading,
[78:47] now in the color grading,
[78:49] I can give it a bit more gain,
[78:52] so there's my gain,
[78:53] and let's just give it a couple bit,
[78:55] so there you are,
[78:56] you see it's just lightening that up a bit,
[79:00] like that,
[79:01] and if I press escape,
[79:03] so that's that,
[79:04] oh that feels about right,
[79:05] kind of natural,
[79:07] what are we on?
[79:08] Well the game actually was a bit darker,
[79:09] let's go.
[79:16] I think we used it again,
[79:19] I just need to,
[79:20] oh I should go and clip that out,
[79:23] oh it's annoying isn't it?
[79:24] Alright, I just can't be bothered doing that,
[79:26] so I'm just going to go into my curves,
[79:29] and,
[79:31] I'd animate that down for that,
[79:32] that bit,
[79:33] where is it,
[79:34] we're going to grab him,
[79:35] and,
[79:38] route projection,
[79:39] that was you wasn't it,
[79:40] transform,
[79:42] and then I'm going to go,
[79:43] I'm going to go back and drag it,
[79:46] what's this one,
[79:47] this is the X,
[79:50] and then,
[79:53] said,
[79:54] right, I'm just going to move you down,
[79:56] move you down there,
[79:57] and then,
[79:58] bring him up when his chin gets too low,
[80:01] let's bring him up here,
[80:02] so he's,
[80:05] like that,
[80:05] he comes down a bit,
[80:07] so he comes a bit low there,
[80:08] so let's bring him up a bit,
[80:12] bring him up a bit more there,
[80:16] so this works great for these sort of,
[80:19] NASA type helmets,
[80:20] where the helmets don't move,
[80:25] oh,
[80:26] there we are,
[80:28] I don't think these helmets move, do they?
[80:31] Well, they don't in my film,
[80:32] alright, there we are,
[80:33] bye all,
[80:34] save all,
[80:36] I was thinking that shot from Maylion,
[80:37] where it's going to move,
[80:39] so look it over there,
[80:40] try not to look,
[80:41] okay, there we are,
[80:43] alright,
[80:45] now what else do I want to do?
[80:46] So I'm just going to add some animation,
[80:49] I'm going to add my UFO into the background,
[80:51] I'm going to also save this,
[80:52] come out,
[80:53] come back in,
[80:54] because I want to hear my audio,
[80:55] so I don't know why I'm not hearing my audio,
[80:57] so I'm going to go file,
[80:59] save all,
[81:01] and just stop these for now,
[81:03] okay, so I've just found an image on NASA's website,
[81:08] for some stars,
[81:09] so I'm going to go and add,
[81:12] tool,
[81:13] square plus button,
[81:15] basics,
[81:16] and let's look,
[81:18] shapes,
[81:19] a plane,
[81:20] going to add a plane,
[81:22] make him very big,
[81:25] let's go 100,
[81:27] okay, so I've got a plane back there,
[81:28] let's move it back here,
[81:31] like that,
[81:32] rotate him around,
[81:34] oops, not quite,
[81:35] okay, there's my plane,
[81:37] I'm going to drag my stars onto that plane,
[81:39] and it will make a texture for you,
[81:41] make a material,
[81:42] there it is,
[81:43] beautiful,
[81:44] that was very interesting,
[81:46] very cool,
[81:47] and then I'm just going to scale him in the X,
[81:52] back, so there we are,
[81:53] and I'm going to go into that material,
[81:55] make him unlit,
[81:57] so it's probably default lit,
[81:59] let's just go to unlit,
[82:01] and then change that to the emissive,
[82:04] and then hit apply,
[82:05] there we are,
[82:07] some stars back there,
[82:10] and,
[82:13] let's go and make him,
[82:15] make him 1000,
[82:18] and then push him far, far away,
[82:21] that way,
[82:23] there we are,
[82:24] doosh,
[82:27] like that,
[82:28] okay, so some stars back there,
[82:32] and then I'm going to go into the X,
[82:34] make him 1200,
[82:41] right,
[82:46] there's that,
[82:47] oh, and then something else I just did
[82:50] while I wasn't here,
[82:51] I shot,
[82:53] like I was saying,
[82:54] my webcam is 30 frames per second,
[82:56] my sequencer was 30 frames per second,
[82:58] but when I made my frames in DaVinci Resolve,
[83:03] the timeline was set to 24,
[83:07] so when I wrote the frames out,
[83:09] it kind of gave them,
[83:10] it told it the metadata was 24 frames per second,
[83:12] so it was actually kind of slowing it down in here,
[83:15] but now if I go to say here,
[83:16] I can go,
[83:17] I'll go,
[83:18] whoa, like that,
[83:19] so that's,
[83:21] the timing's right now,
[83:23] but I did that by going into the file media,
[83:28] image media source,
[83:29] double clicking on it,
[83:30] and then I went down to here,
[83:31] frame rate override and changed it there,
[83:34] so you go into here and you can change it,
[83:35] because it was kind of confused a little bit,
[83:38] what I should do really is make sure next time,
[83:41] my timeline is set to the right frame rate,
[83:45] but I didn't do that,
[83:47] bad person,
[83:48] okay, now,
[83:49] so I've got my,
[83:50] oh, that's the other thing,
[83:51] I accidentally to make sure my audio is working,
[83:56] so I'll talk about aliens here,
[83:58] and then,
[83:59] and then,
[84:01] let's see an alien,
[84:01] so what I should do is get my UFO to come over here,
[84:05] and have it land here,
[84:06] and then have the alien pop up,
[84:08] so that's what I'm going to do now,
[84:10] and I will probably fast forward this bit,
[84:12] and what else can I do?
[84:15] I can also,
[84:15] now I've got background in here,
[84:17] I'm going to animate my camera a little bit,
[84:19] so for now,
[84:20] let's grab my camera,
[84:22] and then I go to transform,
[84:25] and let's go to the location,
[84:27] so we've got a location,
[84:30] but let's calm in a bit,
[84:32] I mean, you're not going to see any distance here, are we?
[84:36] Let's go like that,
[84:37] okay, so we can go,
[84:38] whoop,
[84:40] so that should be,
[84:41] I'll ask something,
[84:43] in this video,
[84:44] I'm going to follow through,
[84:45] in the video,
[84:46] who I didn't,
[84:47] one thing I'm going to do now,
[84:48] at this point,
[84:49] is to annoy the heck out of everyone,
[84:52] press this button here,
[84:54] which disables my audio track,
[84:55] so I don't need that anymore,
[84:57] and let's move that over here,
[84:58] I can also remove these markers by going,
[85:01] delete selected marker,
[85:03] there we are,
[85:04] I think you hit make those by pressing,
[85:06] is it the M,
[85:07] or the right mouse button,
[85:08] one of them,
[85:09] they keep popping up,
[85:11] and I really don't want them,
[85:12] so it's my animation,
[85:13] so let's go and,
[85:16] pilot my camera,
[85:18] and I selected my camera here to pilot it,
[85:20] so let's go in here,
[85:22] let's,
[85:26] there we are,
[85:30] all right,
[85:30] so that's going to be my first frame,
[85:31] it's going to be like this,
[85:35] let's let my camera,
[85:36] tush, tush, tush,
[85:38] transform,
[85:40] save a key,
[85:42] come in,
[85:56] yeah,
[85:57] there we are,
[86:00] a bit fast,
[86:01] okay,
[86:02] let's do this,
[86:03] like that,
[86:06] that's a lot,
[86:25] okay,
[86:47] so that's the thing with all this stuff,
[86:48] it's easier to edit than it is to come up with an idea,
[86:52] so you just throw something out the wall,
[86:55] and then play it back and go,
[86:56] ah, my app kind of works,
[86:58] just winging it,
[86:59] now I'm going to change my focal distance,
[87:03] so that I'm in focus here,
[87:06] there we are,
[87:07] and I'm going to check my aperture a little bit more,
[87:10] that's 100%,
[87:11] that's too much,
[87:12] let's make it,
[87:15] like so,
[87:16] there's my aperture,
[87:18] and oh, I've got an animation on that,
[87:20] so I don't want that,
[87:21] I'll delete that one there,
[87:22] delete that one there,
[87:23] so it's my focal distance,
[87:25] so,
[87:29] and we can check our focal distance
[87:30] by selecting our camera,
[87:32] and then down here,
[87:35] there is,
[87:36] under this purple thing,
[87:39] draw, debug,
[87:39] focal plane,
[87:41] and then you can say,
[87:42] oh, it's bang on,
[87:43] so who,
[87:44] I'm just going to save another key here,
[87:45] make sure he's in focus there,
[87:48] yeah,
[87:49] I'm pretty much in focus all the way there,
[87:51] so let's come into frame a little bit,
[87:54] I don't know,
[87:59] okay, great, turn that off,
[88:02] that's my animation,
[88:04] I've hit low there,
[88:05] so I'm going to go and go into my rotation,
[88:11] camera,
[88:12] now I've got to bring it off a bit,
[88:14] go to go into here,
[88:18] wee,
[88:19] wee,
[88:20] wee,
[88:24] I'm sort of spreading them out,
[88:26] bending them around,
[88:27] so it just feels a bit more floaty,
[88:37] there we are,
[88:40] pressing play,
[88:48] and I got a bit too high there,
[88:50] so,
[88:52] what is this one,
[88:53] oh, it's the focal distance,
[88:54] damn it,
[88:55] I thought that was my rotation,
[89:01] sorry,
[89:02] just undoing that,
[89:04] I didn't get it in my camera,
[89:06] that one there,
[89:07] and my transform,
[89:09] my rotation,
[89:12] there we are,
[89:14] oh,
[89:15] oh,
[89:16] oh,
[89:17] yeah,
[89:18] a bit of that,
[89:19] doesn't it,
[89:21] so we go,
[89:22] oh,
[89:25] look at that,
[89:26] stunning,
[89:27] right,
[89:28] and now he's too low,
[89:29] so I'm going to move him up here,
[89:30] and I'm kind of looking up that way,
[89:31] so that I can kind of interest him,
[89:34] right,
[89:35] so,
[89:36] oh, no,
[89:37] undo,
[89:38] there we are,
[89:39] that's pretty neat,
[89:41] and especially this,
[89:42] like this light on here,
[89:44] as I get closer to this part,
[89:47] that is
[89:49] pretty cool,
[89:54] oh, it's ripping up there,
[89:55] isn't it,
[89:56] oh, that's the texture of the glass though,
[89:58] isn't it,
[89:59] this is the glass,
[90:00] and I've got a bit of a
[90:01] bit of a nice little bit of
[90:02] detail there,
[90:03] and I've got some,
[90:04] a bit of a nice little bit of detail there,
[90:05] and I've got a bit of a bit of detail there,
[90:06] and I've got some,
[90:07] this is the glass though, isn't it,
[90:08] this is the glass,
[90:09] is that distorting it,
[90:10] so if I just select my glass,
[90:14] and I can probably turn that down
[90:15] in the material,
[90:16] but let me just select my glass,
[90:17] in my sequencer,
[90:20] which one was he,
[90:21] let's have a look,
[90:25] there's glass one,
[90:26] just,
[90:27] oh, no,
[90:28] it's easy,
[90:29] oh, is it,
[90:30] because I'm too far over there,
[90:31] yeah,
[90:32] that's my projection,
[90:33] isn't it,
[90:34] I'm a bit too,
[90:35] so I'm okay there,
[90:37] so I need to come across a bit,
[90:38] so I'm sort of pushing it a bit too far,
[90:40] I could select this and rotate it a bit,
[90:43] but if I look at this camera,
[90:45] this is the bang on one,
[90:47] then he's actually not too bad,
[90:49] so let me,
[90:51] let's try rotating it,
[90:52] just to kind of make him feel a bit better,
[90:55] let's go and grab my,
[90:57] off route projection,
[91:00] let's go and grab,
[91:01] is it this one,
[91:02] route projection,
[91:03] actually, let's go and grab his rotation,
[91:06] and then let's go and
[91:08] rotate him around,
[91:10] that's right,
[91:11] ah, ah, ah,
[91:14] okay,
[91:15] that's not that way,
[91:17] this,
[91:18] no, you're not going that way,
[91:20] why are you rotating that way?
[91:23] Oh, I see,
[91:25] it's because my,
[91:26] he's initially rotated the other world,
[91:29] right, let's stop that,
[91:30] let's go back
[91:32] to how we were,
[91:33] zero, zero, zero,
[91:35] select him again,
[91:36] go back into
[91:39] the offset projection,
[91:42] because I've already,
[91:43] he's rotated and positioned,
[91:45] and then I've got a second
[91:46] null on this one,
[91:48] the offset one,
[91:49] so I can select that,
[91:50] drag that into here,
[91:52] and then add a transform,
[91:55] and now on this transform,
[91:58] let's have a look at you,
[91:59] so that's that way,
[92:02] that's that way,
[92:03] and then that's that way,
[92:04] so there we are,
[92:05] that's what I wanted to do,
[92:06] I just wanted to rotate this around
[92:07] a little bit here,
[92:09] because he was just pushing it
[92:10] too far on this edge,
[92:14] so, okay,
[92:15] what am I,
[92:16] what am I here,
[92:17] nine, let's do that,
[92:19] so that will
[92:21] just give us a little bit of
[92:23] wiggle room,
[92:26] and let's go and rotate it that,
[92:28] that way,
[92:32] and let's go and see what I can do
[92:35] with the expanding that edge a bit,
[92:39] because we don't want it to be
[92:40] that cut off all the time,
[92:42] that's why I'm sort of suggesting
[92:43] having the rest of the
[92:45] the back of the helmet,
[92:47] so that will blend into it better,
[92:50] all wrong one,


### Adding the UFO and Alien Animation [93:00]
**Transcript (timestamped):**
[93:01] so,
[93:13] now I'm going to add my UFO
[93:15] into the shot,
[93:17] I've got that model that I used
[93:20] on
[93:23] here,
[93:25] let's go and add him in,
[93:26] where is he,
[93:27] he's going to take a sec
[93:28] to rebuild, to build him up,
[93:30] and throw it back and see,
[93:35] I think he's quite small,
[93:39] it's going to make him bigger,
[94:00] let's go to about here,
[94:05] drag the UFO into the timeline,
[94:08] transform,
[94:10] let's save key,
[94:22] using the space bar just to
[94:25] change the transformation,
[94:29] let's do this,
[94:54] I'm over there,
[94:59] Okay.
[95:29] Okay.
[95:47] File, Save all.
[95:50] Now I'm going to bring Alien into the shop.
[95:53] Where is he?
[95:54] So good content browser.
[95:56] Let's find my Alien guy.
[96:00] Where is he?
[96:02] Realistic Alien 2.
[96:04] There he is.
[96:05] Demo.
[96:07] I could try that animation as well,
[96:08] because when he goes,
[96:09] I can just bring him into frame.
[96:11] There you are.
[96:13] Demo maps, materials mesh 2.
[96:17] Skeletal mesh.
[96:19] Let's bring him in.
[96:20] And then I can have him right by the camera.
[96:23] So he is actually a quick way of bringing these things
[96:26] to where the camera is.
[96:27] As you select your model, right mouse button,
[96:30] move object to camera.
[96:31] There he is.
[96:32] So now there's my character.
[96:35] Oh, there he is.
[96:35] There's his feet.
[96:37] Let's go move him a little bit further back.
[96:38] There's his foot.
[96:40] There we are.
[96:41] Okay.
[96:42] All right.
[96:42] I'm going to have him just appear right next to me.
[96:44] Okay.
[96:45] So I'm going to bring him,
[96:46] put him in the sequencer,
[96:48] go to transform.
[96:50] Actually, I'm going to find that animation.
[96:53] Where he's standing there.
[96:54] Remember that bit?
[96:56] He, when he was standing there, it was me.
[96:59] Dang.
[97:00] All right.
[97:01] This one, what is that one there?
[97:05] Walk around sofa.
[97:06] That was the one.
[97:07] I hope you see my walk around sofa thing.
[97:11] All right.
[97:11] Let's go and just come out of here.
[97:16] Sequence curves.
[97:22] I'm just going to find that bit of animation.
[97:25] I'll select him.
[97:29] Let's move this around because it goes like that.
[97:32] And then he sort of comes forward and backwards.
[97:34] And he starts going,
[97:39] that one there like that.
[97:40] Now I can just go,
[97:42] see if there's another cool bit.
[97:47] Sit down.
[97:52] You know what?
[97:52] I could have that bit again.
[97:53] Couldn't I?
[97:55] The only good thing is that's the only head.
[98:00] Let's do that.
[98:01] All right.
[98:02] Let's use that.
[98:02] Can't.
[98:03] Okay.
[98:04] Let's go and move him over here.
[98:24] Going in.
[98:26] He's like going to tap some on the shoulder.
[98:29] So then I'll turn him on just here.
[98:31] And he's like, no.
[98:33] That's great.
[98:34] All right.
[98:34] And then I'll have his face.
[98:36] So I'm going to add now,
[98:38] go into the plus thing and add control rig and add a layered control rig.
[98:43] So you go that one there.
[98:45] Control rig, led.
[98:46] Now that's on.
[98:47] I can add the forward kinematic control rig.
[98:50] And I should be able to select his head.
[98:52] There we go.
[98:53] So let's go and rotate that round.
[98:56] And I can use this one here.
[99:03] That's funny.
[99:04] And that's how that one like that.
[99:06] And then let's save the key for that.
[99:19] All right.
[99:20] And he's visible there.
[99:22] So it's turning on there as well.
[99:24] So let's go up here.
[99:29] Where are we?
[99:30] Rip protection?
[99:31] Nope.
[99:31] I want my character.
[99:33] Where's my skeleton?
[99:35] There he is.
[99:37] Back to hidden again.
[99:42] There he is.
[99:43] Save the key for that.
[99:44] And now I'll turn him off here.
[99:46] There we go.
[99:49] He arrives.
[99:51] We're looking over here at the UFO.
[99:53] Then da, da, da.
[99:54] Da, da, da.
[99:55] Ah, da, da, da.
[99:56] Right.
[99:57] And then we can make him very right.
[100:01] Ah.
[100:01] I can put the sound on.
[100:10] Where is my sound?
[100:13] There's my sound.
[100:16] Ah.
[100:17] Ah.
[100:18] Ah.
[100:19] Da, da.
[100:20] Da, da, da.
[100:21] Oh, there you go.
[100:22] Da, da.
[100:23] Ah.
[100:25] Da, da.
[100:27] Da.
[100:28] Ah.
[100:39] Now I'm going to go and render this out.


### Rendering from Unreal Movie Render Graph [100:40]
**Transcript (timestamped):**
[100:42] So going to my sequencer.
[100:49] The type of old.
[100:50] I'm going to change this for render local.
[100:52] No, hang on.
[100:53] I'm going to change it from basic to movie render graph.
[100:57] And then I'm going to just use the movie render graph for now.
[101:01] And I'm going to save this as a new name.
[101:08] Save all.
[101:10] Oh.
[101:12] Save as.
[101:13] And then I'm going to put it.
[101:15] I'm going to put it.
[101:16] So it's the default is in the engine part.
[101:19] So we don't want to edit the engine one.
[101:21] We want to put it in here.
[101:22] I've got my made my own.
[101:23] I've made some before in the last video.
[101:26] MRG.
[101:27] And they call this MRG movie render graph.
[101:29] And then we're going to call it helmet.
[101:33] So that's good because now I've got the helmet up
[101:36] and they can edit this one.
[101:38] But I'm going to go to my movie render queue.
[101:40] And rather than running this one,
[101:42] I'm going to change it to the helmet that we just did.
[101:45] MRG helmet.
[101:47] That's a now it'll be looking at this file.
[101:50] And we got warm up settings.
[101:51] Leave that as is.
[101:52] And I'm going to go to my globals.
[101:54] And I'm going to use camera.
[101:58] The first thing I'm going to add is camera settings.
[102:01] Change the shutter timing to frame open.
[102:03] And that means that every frame,
[102:05] it will be calculating the motion blur
[102:07] based on the temporal start of the frame
[102:10] rather than halfway through.
[102:11] And otherwise it kind of blends the frame before
[102:14] and the frame after.
[102:15] So if you ever get that weird double imaging,
[102:17] camera settings is what you use for that.
[102:20] Drag that put it into warm up settings.
[102:22] And I'm going to change this from a JPEG sequence to loop that.
[102:26] Drag out here and look for EXR sequence.
[102:30] And I think nowadays by default, tone mapping is off.
[102:36] I think so.
[102:38] In here, the deferred renderer normally,
[102:41] well, in the olden days, like 5.7,
[102:43] I used to do disable tone curve and enable that.
[102:47] But now I think when it makes an EXR,
[102:50] I think it knows not to do that.
[102:51] And it knows just to make it linear color space.
[102:57] Maybe we'll find out.
[102:59] And I'm going to change the name of my camera to,
[103:03] what am I going to call this?
[103:05] I'm going to call it CM helmet.
[103:10] Beauty.
[103:13] Okay.
[103:14] And then we're going to global output settings.
[103:16] I'm going to choose my output directory.
[103:19] I'm going to make a render to new folder, R and DR2.
[103:26] Okay.
[103:27] Select folder.
[103:29] And I'm going to output resolution.
[103:31] I actually like to do 1440p.
[103:34] And then what else is going to render the length of the beginning
[103:37] and the end of this?
[103:39] And I am going to also, under here,
[103:43] I'm going to add spatial samples.
[103:45] There's one temporal super resolution.
[103:48] I'm going to leave all those.
[103:49] There's default.
[103:49] I could just leave that off.
[103:50] But I'm going to add a sampling method.
[103:56] And I'm going to change this to temporal samples
[103:59] and make that five.
[104:01] So now we've got five steps.
[104:04] Very good.
[104:05] And hit save.
[104:09] I'm also going to hit save here, save all.
[104:13] And now I'm going to hit render.
[104:16] So go back into here and then hit render local.
[104:19] Now it's going to put my, on the other screen,
[104:21] it's calculating my shaders.
[104:25] There we are.
[104:26] So I'm going to pull this over here.
[104:27] It's going to do the warm up frames.
[104:30] And that's doing our animation.
[104:33] Our renders.
[104:36] Okay.
[104:36] So that, those frames have rendered.
[104:37] And now I'm in DaVinci Resolve.
[104:39] And I'm going to make a new timeline to bring those images in.


### Final Compositing in DaVinci Resolve [104:40]
**Transcript (timestamped):**
[104:44] And then edit them together.
[104:46] I mean, why not?
[104:46] I'm doing it anyway.
[104:47] So I may as well show you how I do it.
[104:48] So create a new timeline.
[104:50] And this is going to be called a helmet.
[104:56] L for latest and use project settings.
[104:58] I'm going to turn that off because I'm going to go
[105:00] and change it to 2560 by 1440.
[105:05] And I can see here my default is 24 frames,
[105:07] but I'm going to make this one 30 because my webcam
[105:10] and everything is 30.
[105:11] And so in this case, I'm just going to,
[105:13] since I use the 30 frame webcam to record the video,
[105:16] I'm going to stick to 30 for now.
[105:18] What else have we got?
[105:19] So I'm just going to hit create.
[105:21] Now I'm in this timeline helmet.
[105:24] And I'm going to go into my render directory.
[105:26] And I'm going to go and go into,
[105:30] go into, into here and go to my depth measure.
[105:37] And in under render two is where I've got my render.
[105:41] And I can actually just grab the root directory
[105:43] and put it into here.
[105:45] And it'll make that it'll bring them all in
[105:50] as an image media sequence.
[105:52] So now I've got my frames out rendered there.
[105:54] And I'm going to bring them into my timeline.
[105:56] And these will be in linear sRGB color space.
[106:01] There we are.
[106:09] Okay.
[106:09] And so I'm going to convert those using in the color page.
[106:14] I'm going to add a color, color, transform, color.
[106:21] Where are you?
[106:22] What's it called?
[106:22] No.
[106:25] Transform.
[106:25] Transform, transform, transform, transform color space.
[106:33] Where is it?
[106:34] Color space transform.
[106:35] I'm going to add this here.
[106:36] And then input color space is linear.
[106:41] Is it linear?
[106:42] Or is that the gamma?
[106:44] Oh no, it's sRGB.
[106:48] Come on.
[106:49] sRGB and it's linear sRGB.
[106:54] Linear.
[106:55] So that is what Unreal renders out as the default color space.
[107:00] So yeah, I think it's not adding.
[107:02] In the old days, you used to have to add a tone map.
[107:05] But now it just seems to know that it's tone mapped.
[107:09] So there's my video.
[107:10] There's my thing.
[107:11] Yeah, you see like this dark edge around there.
[107:13] Yeah, definitely if I was doing it again properly,
[107:15] I would put the darkness over there.
[107:18] But for now, it'll do.
[107:21] Let's just hide it all with some craziness.
[107:25] Oh, actually one thing.
[107:26] If I go into the color space,
[107:27] I'm going to go into gamut mapping saturation compensation.
[107:32] And that will do.
[107:33] And then I'm going to add, this is in the paid version,
[107:37] but a film look, the film look creator.
[107:43] Let's just drag that over here.
[107:44] And then we can just pick one.
[107:46] We go through this and we'll just have a look
[107:48] at which one would be good.
[107:49] Alaska.
[107:51] Let's go for vintage.
[107:52] Give it a more of a look.
[107:53] Oh, look at that.
[107:54] The old days.
[107:57] All right, here we go.
[107:59] And I want to go into this one.
[108:01] Just change the color space a bit.
[108:16] Yeah, I don't like this darkness around there.
[108:19] We go in and fix that, edit that around.
[108:23] And I think I might make this a little bit more shiny as well.
[108:27] A little bit more opaque.
[108:32] And I think I get a bit low in the video there.
[108:34] I start a bit low.
[108:35] So I'm going to tilt my camera up too.
[108:41] So that is the process of being granular and iterations.
[108:47] And then this is why I love Unreal.
[108:49] And this is why I love DaVinci Resolve.
[108:51] Because I'm using these EXR frames.
[108:55] And I can just overwrite these frames.
[108:58] And the edit will stay exactly the same.
[109:01] So I love this workflow.
[109:04] And then I'm going to go in and add some noise and sound effects.
[109:09] And then I'm going to edit the video together.
[109:12] That's it for today.
[109:14] Bye.
[109:16] In this video, I'm going to put myself inside a helmet.
[109:20] And hopefully there's no aliens around here.
[109:28] In this video, I'm going to put myself inside a helmet.
[109:32] And hopefully there's no aliens around here.



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
