---
title: Unreal Engine: Understanding Subscenes in Sequencer
source: YouTube
url: https://www.youtube.com/watch?v=5pK6JmarYhM
author: 3D Education with JC
ingested: 2026-07-20
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-understanding-subscenes-in-sequencer/
frame_count: 0
frame_status: pending-selection
---

# Unreal Engine: Understanding Subscenes in Sequencer

**Source:** [YouTube](https://www.youtube.com/watch?v=5pK6JmarYhM)
**Author:** 3D Education with JC
**Duration:** 15m17s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py unreal-engine-understanding-subscenes-in-sequencer <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hello, in this potentially brief video, we're going to freestyle and see how far we get,
[0:04] and hopefully it's quick and to the point.
[0:06] We're going to pick up after the Unreal Engine Jumpstart video and go over a few more sequencer
[0:13] options that you have.
[0:14] So if you haven't seen this video, the Unreal Engine Jumpstart from my VFX and animation
[0:19] friends, watch that first.
[0:21] Then come back here because we're going a little deeper on some of the concepts that
[0:24] were introduced in that video.
[0:27] After that video landed, we were in a shot.
[0:30] For example, you hit play and here's your character moving.
[0:33] In this case, it's nothing crazy.
[0:35] Oops, I actually forgot to look through the camera.
[0:37] I just have a simple track on, a look at setting.
[0:42] On that, don't know if we covered in the last video.
[0:44] So if I go to the camera just to show that, there's a look at track settings.


### Track Settings [0:46]
**Transcript (timestamped):**
[0:47] You can add what you want to have looked at, turn on tracking.
[0:51] In this case, I had to bump an offset because the track is at our feet.
[0:54] So just bump it up in Z a little bit and see if you can offset your look at it a little
[0:58] bit.
[0:59] But anyway, so I have a camera and my female here with a little bit of a transform and
[1:03] some cycles added.
[1:07] So we covered that in the other video.
[1:09] In that other video, we made two shots.
[1:11] So back to the CompteProtent browser.
[1:13] Here's one shot.
[1:14] We made two shots and then we strung them together in yet another level sequence where
[1:20] we added two shots together.
[1:22] That works and that's fine.
[1:24] The good thing about sequencer and level sequences, so level sequence is just a container of
[1:29] information.
[1:30] You can put all of your shot data with one camera and your animation in one shot and
[1:34] then put it in another shot and then put them together.
[1:38] Though I often get asked, well, what if I want this animation and I want multiple cameras
[1:44] to cover it?
[1:45] So we're going to go over two additional things you can do that the slight catch here is there's
[1:49] no right answer.
[1:50] There's no one way to do it, which kind of frustrates some people because they want
[1:54] to say, don't tell me all the options, just tell me the best way to do it.
[1:57] There's kind of not a best way.
[1:59] There's a way that works for you.
[2:01] It's like going to the beach, you can take one freeway, you can take a different freeway,
[2:05] you could ride your bike there, it would depend on where you live.
[2:08] You could walk there.
[2:09] As long as you get to the beach, that's what matters.
[2:12] As long as you output some cinematics, that's what matters.
[2:15] There's some ways are better than others, but it still is kind of situation dependent.
[2:20] Everything's fine if you don't have a car, but you might want to drive, but then you
[2:24] have parking to deal with.
[2:25] So again, totally up to you.
[2:28] My goal here is to show you some of the options that you have with Sequencer.
[2:33] In this one particular shot, I just happen to call it shot one.
[2:37] In animation, usually in one shot you have one camera, but Unreal doesn't.
[2:41] That's not a thing for it.
[2:42] So let's talk about what you can do in here.
[2:45] I'm going to delete this half of this here.
[2:48] We haven't talked about this in the other class so much as this camera cuts.
[2:51] This allows you to have more than one camera in a shot if you choose.
[2:57] The default of this is you'll usually find when you make a new spawnable camera that
[3:03] your camera cuts track comes automatic and it just fills up the whole thing with whatever
[3:07] camera got created.
[3:09] However, I'm going to eject out of the camera here just to get a little bit of a bigger
[3:15] view here.
[3:16] Add another camera just for a super extreme of a super high top view.
[3:21] So I'm going to add another camera just using the spawnable button here, which means if
[3:26] I hit this button versus drag one in from the cinematics, this camera will only exist
[3:32] in this shot.
[3:33] If I have other level sequences, it won't be in those.
[3:35] It's not getting added permanently to the outliner.
[3:38] It's only going to be there when you have this shot open.
[3:42] Hit this button and I'll get Cine Camera Actor 2.
[3:46] I'm going to hit F2 so I can rename this.
[3:49] I'll just call this Top Cam to make bluntly obvious that it's a different camera.
[3:54] Otherwise the names are kind of similar.
[3:57] And here's my view from it.
[3:59] I'm going to go even higher.
[4:00] I'm just going to get the whole world here.
[4:04] If I am clicking on this icon here, that is my top cam specifically.
[4:10] That is my view from my top cam.
[4:13] So I get the whole action from way up there.


### Camera Cuts [4:17]
**Transcript (timestamped):**
[4:17] But when you click here on Camera Cuts, that shows you the cameras that you have chosen
[4:22] for this particular shot as a whole.
[4:25] I guess you could call it.
[4:26] So if I hit play, it's going to play my camera cut from only this camera because this is what
[4:35] drives when you're running your shot and this is selected.
[4:38] This is also what carries through when you bring it up into higher sequences.
[4:43] This is what defines what camera gets used.
[4:45] I want this camera in the first half.
[4:50] So I'm going to click here.
[4:51] I want this camera, the Cine Camera Actor, this one, right?
[4:57] Same view.
[4:59] I want this camera, Cine Camera Actor to be used for the first part of the shot.
[5:04] And then once I hit here, I want to switch over and use the top cam.
[5:09] So in the Camera Cuts, what I do is I just hit Add a Camera where the play hit is, New
[5:14] Binding, and I want to add the top cam as my camera to take over when I hit that spot,
[5:22] right?
[5:23] So right now you're looking at it and you're like, hey, how come it's only that first camera
[5:25] still?
[5:26] This is really important.
[5:28] Keep an eye on where this button is.
[5:31] If I click this, I'm only going to see that for the whole length.
[5:33] But the overall final output when you would potentially hit the render button is going
[5:38] to be what's defined here in the Camera Cuts.
[5:40] So I'm going to click that button, go back to beginning of the sequence.
[5:44] It's going to play through here.
[5:45] Then it's going to pop over to the top cam to play the rest of the sequence.
[5:50] That is a viable way of working.
[5:53] You can do that.
[5:55] I'm going to show a slightly alternate but similar kind of version.
[6:00] And that is using a sub-scene in your sequence.


### Using a Subscene in Your Sequence [6:03]
**Transcript (timestamped):**
[6:03] So let's try not to make too much of a mess of this.
[6:07] I'm going to say that the animation in this shot is all that I want.
[6:12] I actually don't want cameras in this shot.
[6:16] I'll get back to that in a minute.
[6:18] Let me just delete this.
[6:20] Delete this.
[6:21] I'm going to delete the whole Camera Cuts.
[6:23] I'm going to delete these two cameras.
[6:25] All that's going on in this level sequence now is my character from far, far away.
[6:30] You can see her way down there.
[6:32] So she's way down there doing her thing.
[6:36] That is the only thing animated in this particular level sequence.
[6:40] I just deleted everything else.
[6:42] You're going to think, well, how are you supposed to render anything?
[6:46] As is, you can't in the sense of that there's, I don't even have a camera to render through.
[6:50] But that's because I'm looking at this from the beginning.
[6:53] But that's because I'm looking at this from a different way of organizing my project.
[6:59] So this is a self-contained, let's see, it's called shot one.
[7:02] I'm going to save this.
[7:04] I'm going to go back to my content browser and I'm actually going to rename it just to
[7:08] try and make life a little easier here.
[7:10] I'm going to call this char anim.
[7:12] So this is my level sequence where the only thing going on is animation of the character.
[7:19] And this, especially when you're working with more people, this probably is a valuable way of working.
[7:25] If you're in the Unreal Fellowship and you're doing your own short all by yourself and you don't need to collaborate with anybody,
[7:31] this still may be useful for you.
[7:33] And it's good to know that this is how it works because, you know, eventually you work with people,
[7:37] but you may not have to do this level of detail when you're working on your own project.
[7:41] But definitely when you're working with others, this comes in handy.
[7:44] So this is a self-contained level sequence called char anim with just a character walking.
[7:49] So now I'm going to go and I'm going to make another level sequence.
[7:54] Remember, a level sequence is just a container.
[7:57] I'm going to make another one.
[7:58] I'll call this scout game level, you know, whatever.
[8:04] So I'm going to just scout the camera a little bit for all the action that's going on.
[8:09] So I'm going to double click and it opens a brand new sequencer, scout game level, nothing in it like we've seen before.
[8:16] However, this time I'm going to pull in that sub scene.
[8:21] I'm going to pull in the animation of the character at this point in this scout game level.
[8:27] Hit play, nothing's happening, right?
[8:28] Because just like we've seen before, it's just a basic no, there's nothing in here.
[8:33] So we're not going to see anything.
[8:34] I'm going to add a track and I'm going to add a sub scene.


### Add a Subscene [8:37]
**Transcript (timestamped):**
[8:39] So a sub scene itself is the terminology should almost say like add a sub sequence because really what you're pointing at when you do this,
[8:51] you're pointing at another sequence and bringing it in to this level sequence.
[8:56] I add the track itself is just still empty.
[8:59] And now I add the sequence that I want to bring in here and I want to bring in the char anim.
[9:05] Oh, it comes in where your playhead was my play heads at the end.
[9:08] So I'm just going to slide it back here.
[9:11] Right.
[9:12] So now when I hit play, I get my animation, but the animation is not occurring in this level sequence.
[9:20] The only thing this level sequence holding at the moment is a sub scene track that's pointing to that other level sequence, the char anim.
[9:28] Why might you do this?
[9:30] You might have one person working on the character animation or say yourself working on the character animation a little bit separate than maybe an effects animation that you have that you're working on.
[9:42] And then maybe there's like a disco scene.
[9:44] So somebody else is kind of working on like the lighting effects and having all this crazy animation going on.
[9:49] Each person can be working separately in their own level sequence.
[9:53] And then you have, you know, in this case, it's called scouting level, but you call it your master sequence that you're pulling in a bunch of different sub scenes and pulling those in.
[10:03] And the advantage there is, you know, I can, I can change the timing of what's going on here as well.
[10:09] Right.
[10:10] So I can hit play and she's already halfway done with what she's doing.
[10:13] So I can adjust, you know, my clips a little bit, but that aside, why else might you do this?
[10:19] This action is going to happen.
[10:21] And then in this level sequence, I can add multiple cameras.


### Add Multiple Cameras [10:24]
**Transcript (timestamped):**
[10:27] So I just added three cameras in this.
[10:30] And from here, it's not that much different than what we've seen before.
[10:34] I have three cameras.
[10:36] So let's, what am I looking through first?
[10:39] Let's look through this camera first and go the beginning of the shot.
[10:43] Right.
[10:44] So where's she going to go really close.
[10:47] So my first shot, come here, you, my first shot with using camera one.
[10:55] I mean, I'm saying the word shot, but let's just say the first camera, this in a camera actor is going to be here really close.
[11:02] So I can hit play.
[11:04] She kind of instantly walks out of scene.
[11:06] So it's not that exciting, right?
[11:08] So maybe, you know, I have to back up a little bit.
[11:11] You know, I could deal with focus.
[11:12] We dealt with focus and all that stuff in the other ones.
[11:14] So I'm not going to bore you with that here.
[11:16] Let's just say I get a little bit of it from this first camera here.
[11:19] And then as she walks, I want to go ahead and cut to camera two.
[11:24] Whoops.
[11:25] Got to grab the end of that.
[11:26] Come here.
[11:27] There we go.
[11:28] Right.
[11:29] So camera two, I got to look through camera two here.
[11:32] This I'm going to make a side view.
[11:38] Come here, you at that point and have her walk for a little bit from this camera's point of view.
[11:45] I need to add that I want this camera to take over.
[11:48] So I'm going to go to add camera.
[11:50] I can also, I can just grab it here as well.
[11:52] Say camera two.
[11:53] So from here, she's going to be walking.
[11:56] And then let's say from here, because I don't want to move the camera.
[12:00] I'm just going to slip over here, jump over to camera three, look through it.
[12:04] And that's the way here.
[12:06] Let's do some like artsy shower.
[12:08] I got a really low, low camera and see if she like runs at it.
[12:12] I need to add it to my.
[12:14] Well, actually I'm viewing it here.
[12:15] So I don't, I haven't clicked this to designate.
[12:18] I want to look through the mashed camera here.
[12:20] I'm going to just look through there.
[12:22] So she comes running at the camera.
[12:24] Oh, I missed her feet, whatever.
[12:26] So let's go really close here.
[12:28] So it's just going to land on her feet at the end.
[12:31] And she's hovering, but who cares.
[12:33] So then let's go back and drop in camera three to take over there.
[12:37] So just add a camera, camera three.
[12:40] All right.
[12:41] So now if this is selected, all I'm going to see is that camera's point of view for the whole time.
[12:47] But the camera cuts track is defining again what this overall level sequence is going to use as the camera.
[12:54] So I click here to have that take over.
[12:57] So it's going to go through camera one, then camera two, then camera three, camera one, camera two, camera three.
[13:03] All right.
[13:04] You can also add, again, you can add other kinds of sub-scenes.
[13:08] Now the difference between this and a master sequence is when we were doing the master sequence,
[13:12] in that case you're building a sequence of shots that are end to end.
[13:17] Right.
[13:18] So if you go back to that other video, we had shot one play and then shot two play and then shot three play.
[13:23] So it's a very linear workflow.
[13:24] In this case, we're playing multiple sub-scenes or those other level sequences in parallel.
[13:31] So I can have the animation track running at the same time.
[13:34] I can have the effects track running and I can have the lighting track running and they're all playing simultaneously,
[13:40] but they're also available.
[13:42] I can double click here to char anim.
[13:44] That opens into the sequencer.
[13:46] It opens the level sequence for just the character animation that I can make changes to if I want.
[13:52] You know, if I actually wanted to get back on the ground here, I could just nudge her down just a little bit.
[13:59] Right.
[14:00] So now I've fixed that.
[14:01] My character animation is fixed.
[14:03] I save my changes.
[14:07] I go back out up to this top level and it's fixed at the top level as well.
[14:14] So again, hopefully you get the idea that you can separate the animations into multiple level sequences and then pull them into a parent of sorts level sequence.
[14:29] Again, they're all just level sequences and you can pull them into each other kind of like what you can do static wise with the different levels.
[14:36] But here you're doing it on a time-based workflow.
[14:40] You can add your cameras here.
[14:42] You could also add audio track.


### Audio Track [14:43]
**Transcript (timestamped):**
[14:45] I can come here and add an audio track, but I could also add the audio track here in the char anim and that's going to get pulled in as well because it's kind of built into that down there.
[14:57] So you can mix and match and put stuff kind of wherever works that works for you.
[15:03] Hopefully that gives you an idea of what you can do and how you can work with level sequences, specifically how do you sub-scene and where you can put different cameras to cover different shots.
[15:14] Alright.
[15:15] Enjoy.



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
