---
title: How to use 500+ Motion Matching Animations for Cinematics in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=d_YyHUk_C-4
author: HUSSIN KHAN (UAI)
ingested: 2026-07-20
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-use-500-motion-matching-animations-for-cinematics-in-unreal-engine-5/
frame_count: 0
frame_status: pending-selection
---

# How to use 500+ Motion Matching Animations for Cinematics in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=d_YyHUk_C-4)
**Author:** HUSSIN KHAN (UAI)
**Duration:** 12m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-use-500-motion-matching-animations-for-cinematics-in-unreal-engine-5 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone, Hussein here, welcome back to my channel.
[0:04] So recently Epic released this game animation sample project.
[0:09] They say that we have 500 plus AQA animations that you can use for motion tracking.
[0:14] So they gave you a sample project, or they gave us a sample project and also some animation
[0:18] sample walkthrough.
[0:19] A lot of YouTube channels have showed this.
[0:22] They were talking about the motion matching site.
[0:24] So my question was, is it possible for us to use the sample projects for cinematic stuff?
[0:30] So I did some experiments and I found out that you can.
[0:32] So in this video, I'm going to show you how you can do it.
[0:35] So go ahead and download the sample project from the news or the samples tab here under
[0:40] game animation samples.
[0:43] And once you have it installed, you will have to open the project up and you will get something
[0:47] like this.
[0:48] So I was playing with this earlier and I did some experiments and I will show you how I
[0:52] came about doing this.
[0:54] So let's start by actually going and creating a new project.
[0:57] So you've got a file and say new level.
[1:01] And I want to choose the basic level over here.
[1:04] Click on create.
[1:05] All right.
[1:06] They have a basic project.
[1:07] If you open up the content browser, you should be able to see there are a couple of folders
[1:12] here.
[1:13] And I was looking for the animations.
[1:14] I couldn't find them.
[1:16] So you really have to dig deep and find where exactly they are.
[1:19] So I found out that they are actually in the corrective folder and then it's in the UEF
[1:23] and mannequin folder.
[1:24] I'm just going to make this a bit bigger.
[1:26] So it's in the characters folder.
[1:28] I've colored my folder so you can see it easily.
[1:31] And in the UEF and mannequin folder, you'll see that you have animations and then they
[1:34] are categorized into idle jump, run, knowledge stuff.
[1:39] To better see this, I'll just go back to my UEF and mannequin here, open up the meshes
[1:44] and we have the UEF and skeletal mesh.
[1:46] I'm going to just double click on it.
[1:48] And this is the skeletal mesh that you come with for the UEF and skeletal.
[1:52] So on the right hand side, you will see that you have a couple of tabs here.
[1:55] So you have the skeleton, you have the...
[1:58] I'm just going to talk it up here.
[2:00] Then you have the mannequin and then you have the animations.
[2:04] So if you click on animation, you click on asset browser, you will see that they have
[2:07] all these animations that comes with it.
[2:10] And at the bottom, you can see there are 551 items selected, one selected.
[2:14] So you have this animation of this guy climbing up the stairs or something like that, climbing
[2:18] up the wall.
[2:19] All right.
[2:20] So I'm going to convert this into an animation.
[2:22] I'm going to use in my level for instance.
[2:25] I can hear the sound by the way.
[2:26] It comes with audio as well.
[2:27] It's kind of cool.
[2:28] I'll choose one of these, this neutral jump F land run left, right foot to mouthful.
[2:34] So I'm going to do a right click on this and guess what?
[2:37] We have something called export to FBX.
[2:40] So I'm going to click on export to FBX, asking me where do I want to save this?
[2:44] I got a folder called animation.
[2:46] So I'm going to put it over here.
[2:47] So we can rename it if you want to.
[2:48] I'm going to rename this into AA underscore, call this jump.
[2:53] Let's call it land.
[2:54] Keep it simple.
[2:55] All right.
[2:56] AA jump land.
[2:57] So I'm going to click on save.
[2:58] Okay.
[2:59] The FBX export options will pop up.
[3:01] So in this case, I'm just going to leave everything on its own.
[3:04] Everything should be okay.
[3:05] And then click on export.
[3:06] So now we have this FBX export options that pops up.
[3:10] And I'm just going to go through this quickly.
[3:12] You need to assign the animations to a skeleton.
[3:15] In this case, let's use the UEFN skeleton here that comes with the project.
[3:19] I'm going to scroll all the way down until I see SKEUFN mannequin.
[3:22] Let's try with this first and then we'll try with some of the other skeletons.
[3:25] All right.
[3:26] Export at time is fine.
[3:27] I'm going to go down.
[3:29] Frame rate is fine.
[3:30] I think everything should be okay.
[3:32] Just click on import all.
[3:34] If you have a message that pops up on the bottom right, asking you to import the animation,
[3:39] go ahead and do it.
[3:40] So let's jump back to here.
[3:42] And now I'm going to create a new sequence.
[3:44] So up here, click on this button up here for sequence, then add a level sequence.
[3:49] And then I'm going to put it in my animation folder.
[3:51] I'm going to call this test underscore sequence and click on save.
[3:55] Right.
[3:56] So we got a sequence now.
[3:57] So I like doing the sequence this way because as soon as you create the sequence, it's going
[4:01] to appear in your outliner.
[4:03] So whenever next time when you open up this level or this project, you can find the sequence
[4:07] in your outliner and then it's easy as selecting it and then clicking on open level sequence.
[4:13] It's always going to be there, but this is kind of cool.
[4:15] So let's bring in the UEFN character.
[4:18] So I'm going to go and grab it, drop it into my scene here.
[4:21] I'm going to zero rise its location.
[4:23] I'm going to give it a 90 on the rotation on the Z.
[4:28] So it faces us and then we'll drag SKM, UEFN, mannequin into the sequencer.
[4:33] As soon as I click on the plus sign, you'll see that I have the animation here.
[4:37] I've made a few, but let's find the one that I was looking for, the AA jump line.
[4:42] Right.
[4:43] So we have the animation that is just jumping and then it's running across.
[4:46] So that worked.
[4:47] Okay.
[4:48] And then of course you can convert the others into FBX and import that again and you can
[4:51] keep on adding it to here to become your cinematic sequence.
[4:57] So this is with the UEFN character.
[4:59] I'm just going to zoom out a bit.
[5:00] You can see the whole thing is jumping out from the whatever that that place is up there.
[5:05] Okay.
[5:06] The pack also came with another character under Paragon.
[5:08] We have this nice twin blast character here.
[5:12] I'm going to just open the meshes up.
[5:13] Here we go.
[5:14] Right.
[5:15] So I'm going to double click on the skeletal mesh and this dude is kind of cool.
[5:19] Nice setup here.
[5:21] Right.
[5:22] He has a mesh stick in his mouth.
[5:24] Kind of cool.
[5:25] Right.
[5:26] So I'm going to convert the animation to use on him.
[5:28] Right.
[5:29] So let's jump to the animation again.
[5:31] So this was the one I've done previously.
[5:33] So you wouldn't have this in your project right now.
[5:36] So I'm going to show you how you can convert that.
[5:38] And what I'm going to do is I'm going to go back to the UEFN character animation.
[5:42] Right.
[5:43] This is kind of cool.
[5:44] Right.
[5:45] So I came across this one is the neutral jump F land roll left foot.
[5:49] So I'm going to use this for the character.
[5:50] So just press control B to look for it in the browser.
[5:53] We can do a right click on it and then go to retarget animation retarget animation panel
[5:58] will open up.
[5:59] And then here we have the source skeletal mesh, which is going to be the UEFN.
[6:03] And I'm going to retarget it for the Paragon character.
[6:06] So if you click on this target skeletal mesh, click on the none and it gives you a list
[6:10] of a drop down list.
[6:12] So I'm going to look for the twin blast character should be in the list here.
[6:15] If you scroll all the way down, you can should be able to see twin blast.
[6:17] There we go.
[6:18] As can twin blast action hero.
[6:20] And then you can now export this animation.
[6:23] If you want to copy that control C, right.
[6:26] Jump back here and then press control V. There you go.
[6:28] Right.
[6:29] This one click on it, export the animation.
[6:31] And I'm going to put in my animation folder.
[6:32] I'm going to put in TB for twin blast land and walk.
[6:36] So I'm going to click on export.
[6:37] It's going to be a pop up here, batch export options over existing file.
[6:41] Just press export.
[6:43] And on the bottom right, you see this has been retargeted.
[6:46] And now in your animations folder, you should have an image that we just brought in TB
[6:52] land.
[6:53] Well, there you go.
[6:54] Right.
[6:55] That's the one.
[6:56] Okay.
[6:57] So let's bring the twin blast character into the sequencer, Paragon heroes, twin blasts,
[7:00] a skeletal mesh, drag and drop into the sequence.
[7:04] And we're going to drag him into the sequencer.
[7:07] Animation plus sign, TB land walk.
[7:10] Just click on that.
[7:11] Let's bring it forward.
[7:12] And now you can see that we have the animation that you can use for your sequence.
[7:16] Nice.
[7:17] Okay.
[7:18] Landing and rolling.
[7:22] The only thing that that's the issue here is that you don't see the class simulation.
[7:26] Right.
[7:27] See that everything's the code is not.
[7:29] It doesn't have the class simulation, which is kind of sad.
[7:32] But what I can do is select the animation here and go into the details panel, go down
[7:37] to the custom mode here, animation, just change it to assets.
[7:41] And now it becomes class simulation.
[7:44] So we have used the UEF and character.
[7:46] We have used a twin blast character that comes with the sample project.
[7:50] And I want to use a metahuman.
[7:52] Right.
[7:53] Unfortunately, there's no metahuman that comes with the sample project.
[7:55] I looked for it.
[7:56] If you can find it, let me know.
[7:58] So what I did was I brought in my own metahuman.
[8:00] So I'm going to just drag him into the scene here.
[8:03] Okay.
[8:04] Of course, he's going to have issues with this LOD.
[8:08] And as usual with metahumans, you have to select the blueprint of the metahuman.
[8:12] And in the details panel, scroll down in this part over here, lot sync and make this to
[8:17] either one or zero.
[8:18] I'll make it mine to zero.
[8:19] So now we have a full featured face.
[8:22] So again, it's the same process.
[8:24] We are going to convert a animation into a metahuman animation.
[8:29] Right.
[8:30] So go back and look for the animation.
[8:32] So I'm going to use this, this neutral stand idle break v06.
[8:38] So control B, look for it, right click on it.
[8:41] Again, go to retarget animation.
[8:43] So instead of now using the twin blast character, we are going to use the metahumans.
[8:49] M, tall, narrow body mocap, skeletal mesh.
[8:53] Here we go.
[8:54] Right.
[8:55] And again, I'm going to do an F2 on this one, control C, jump back to the popup here, control
[9:01] V, look for it, select that export animation.
[9:05] Okay.
[9:06] It's telling you where you want to save it.
[9:07] Again, I'm going to put in my animations folder.
[9:09] This time around, I'm going to put a prefix as m page underscore and let it have its own
[9:14] the name that comes with the animation.
[9:16] Right.
[9:17] Click on export.
[9:18] Click on export again.
[9:20] Jump back to sequencer.
[9:22] Let's bring metahuman into the scene.
[9:25] And I've got my control rig, which we don't need for this.
[9:28] So I'm going to just disable that.
[9:30] Phase rig, I don't need, we just disable that.
[9:32] Right.
[9:33] Bring the play hit to the beginning.
[9:34] I'm going to click on body, click on plus, go to animation.
[9:38] That's 07.
[9:39] This is 06.
[9:40] This is the one.
[9:41] Yeah.
[9:42] And now you can see if I double click on this, the animation is like that and it's looking
[9:49] around.
[9:51] And we can actually combine this with another animation.
[9:53] I've made one earlier.
[9:54] I'm going to show you how you can do that.
[9:56] Just use my control key to scroll out a bit and just extend it a bit.
[9:59] Yeah.
[10:00] Open the animation part.
[10:01] It's animation.
[10:03] So I made another one.
[10:05] So let's put it over here and I'm going to click another plus sign.
[10:08] And I think there's one called walking forward mh start to walk, walk start.
[10:15] And I'm going to combine them up.
[10:17] Let's have this thing enable, combine that up.
[10:20] And then you can see now it's animating and then it starts walking.
[10:25] So notice his foot.
[10:26] Make sure that the foot doesn't slip.
[10:28] So he's going to use his left foot to walk.
[10:31] Right.
[10:32] So I'm going to do a right click on the second animation, match this bone with the previous
[10:37] clip and we're going to look for something called foot.
[10:40] And then we're going to be the left foot.
[10:41] Right.
[10:42] So now if you notice the foot doesn't slip anymore and it's just start walking.
[10:45] It's kind of cool.
[10:46] Right.
[10:47] So you can actually convert this into cinematic sequences if you want to for all three characters.
[10:52] In fact, you can bring it also the characters from mixamo.
[10:55] So now you have a range of animation that you can use in Unreal Engine.
[10:59] We have a few hundred in mixamo.
[11:00] We have now a few hundred from Epic themselves.
[11:03] I hope this has helped you in being able to use animation for your cinematics.
[11:09] So let me just open this guys up again and they are all coming down jumping.
[11:13] And then I want to open up my other animation.
[11:15] Show you something cool.
[11:17] Animation test.
[11:18] So here I have the same thing.
[11:20] All right.
[11:21] So let me open up the sequence.
[11:23] Anyway, it's always here.
[11:25] All right.
[11:26] Open it up.
[11:27] I will sequence.
[11:28] And now we have this character, which is basically the same animation that I did for him.
[11:33] So instead of him jumping and landing, I made him that he can fly up.
[11:38] So let's see that twin blast character flying like Neo.
[11:43] Right.
[11:44] So if I do that, basically I just click on the animation.
[11:47] I went to properties and I say reverse the animation.
[11:50] So essentially, I will show you the actual animation.
[11:53] It should be like that.
[11:55] He lands and he walks backward.
[11:57] Right.
[11:58] That's part of the animation that comes with the project.
[12:00] So what I did was I do a right click.
[12:02] I went to properties and I say reverse animation.
[12:05] So you have something different, which is sound now.
[12:07] It looks like as if he's taking off or flying away.
[12:14] And again, he doesn't have his cloth simulation.
[12:16] Right.
[12:17] You can see that.
[12:18] So you can click on that in the details panel, change to animation asset.
[12:23] And now the cloth simulation comes back.
[12:25] Okay.
[12:26] Give that a try.
[12:27] Let me know how it goes.
[12:28] If you have any comments, if you have any questions, please leave it in the comment section below.
[12:33] And I hope you have learned something from this.
[12:35] So this is Hussein signing off.
[12:37] I'll see you soon and take care.
[12:38] Bye bye.



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
