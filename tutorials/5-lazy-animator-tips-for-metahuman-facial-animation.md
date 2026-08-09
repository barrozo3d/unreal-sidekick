---
title: 5 Lazy Animator Tips for Metahuman Facial Animation
source: YouTube
url: https://www.youtube.com/watch?v=vNe9TfYasyA
author: MX Bell — Realtime Workflows 
ingested: 2026-08-09
ue_version: "5.7"
tags: [metahuman, facial-animation, live-link, take-recorder, metahuman-performance, control-rig, sequencer, animation-layers, lip-sync, idle-animation, constraints]
extraction_status: complete
frames_dir: tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/
frame_count: 12
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# 5 Lazy Animator Tips for Metahuman Facial Animation

**Source:** [YouTube](https://www.youtube.com/watch?v=vNe9TfYasyA)
**Author:** MX Bell — Realtime Workflows 
**Duration:** 25m24s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Now it's still looking a little bit dead.
[0:02] Hello and welcome back to the lazy animators guide to Unreal Engine, where today we're going to look at MetaHuman faces.
[0:09] I've got five techniques to show you for how to cheat an animator in MetaHuman faces, so let's just get straight on with it.
[0:15] How to create idle animations. Now you've also been talking about idle animations for bodies on this channel,
[0:20] but we can actually do it for faces as well.
[0:22] So we're going to record idle animations.
[0:25] We're going to generate performance using just an audio file.
[0:28] I'm not getting excited. Do I sound excited?
[0:31] See that's really good, right?
[0:33] We're going to derive the head animation from either of those methods and use it additively on our body performance.
[0:40] We're going to blend them together and we're going to override them with some good old layered animation as well.
[0:46] My name's Emix Bell and I work on all these things and I'm here to teach you how to make films in Unreal Engine.
[0:51] Welcome to Real-Time Workflows.
[0:54] Let's start with an idle animation.


### Recording idle face animation with Take Recorder [0:56]
**Transcript (timestamped):**
[0:59] We're going to take record to do this.
[1:01] I'm using Unreal Engine 5.7.
[1:04] There's just a little thing you need to know about the difference between 5.7 and 5.8 when it comes to this and we'll get into that.
[1:10] All I've got here is an empty level with a MetaHuman.
[1:14] This is my MetaHuman from Spacewalker, which is the feature film I'm making live on this channel.
[1:19] Every week I do a new video diary.
[1:21] This is the lead character from there.
[1:23] He's not in his astronaut suit, he's just in his PJs.
[1:26] It's worth noting that our takes will be recorded always to cinematics and takes by default, which is what we want.
[1:32] You'll see I recorded something at least a day, so our animations are going to come into here.
[1:39] We're going to record an idle. We can record a performance like this if we want to,
[1:43] but if you're recording dialogue, I found generating it is a better way and we'll get to generation next.
[1:49] Tools and Live Link Hub.
[1:52] Watch how disgustingly simple this is.
[1:56] Live Link Hub, my webcam is up here on top of the screen and we're on Live Data.
[2:03] We're going to add a source, we're going to go MetaHuman Video, click on MetaHuman Video, then click on Connect.
[2:10] Your webcam will blink on like that one just did there.
[2:14] Now we can move this over, come to our MetaHuman.
[2:19] Oh look, there is already active because I left the settings on.
[2:24] You need to activate Use Live Link and select your Live Link subject, which is the camera feed.
[2:31] Look, we're animating a MetaHuman using just my face. You see how it broke there when I looked away.
[2:37] Now I said you can record a performance like this, but you can see the lip sync isn't that.
[2:42] It's okay, it's good for free, but we'll see that the generation is better.
[2:48] However, for what I want to do here, this is the way to do it.
[2:51] I'm going to record an idol. An idol, as you've seen, was something that I would record for a body and then animate on top of.
[2:59] And no different for a face. We just want the face to have some ambient motion so it's not dead.
[3:04] So in order to do that, with this now set up, we're going to go to Cinematics and take recorder.
[3:10] And we're going to grab Tom and add into this. There he is.
[3:15] And now we can literally just hit record. Now all I'm going to do to record an idol, I'm just going to look bang square head.
[3:24] Right, and I'm just going to allow my eyes to dart just around the viewport area on my screen.
[3:31] And I'm going to hit record. We'll get a little countdown to...
[3:41] Okay, all right, so now we've done with this Tom so we can turn off Live Link if we want.
[3:46] We can come over here and turn it off.
[3:49] And we should probably hide him because we're going to open the thing that we just recorded.
[3:54] So we can see it. Now I didn't set a scene name there, which you should probably do.
[3:58] I didn't do it, but you should probably do that. Like I did it earlier. I recorded the thing earlier.
[4:02] So this is scene 102. This is the one we just did. We can see that it's the previous one.
[4:07] So I'm going to open this now and we can look at what we got.
[4:12] Okay, great. And we can click through. Now here's the thing. Here's the complication.


### Face animation clip bug in 5.7 - solved! [4:13]
**Transcript (timestamped):**
[4:20] If you recorded this on 5.7, we can come and browse through to what we recorded, right?
[4:25] So we've got some animation clips. And we see we've got three clips.
[4:27] There's one for his head and two for his body.
[4:31] Now you would think that the head motion will contain all this motion, the head animation.
[4:38] But if we open it up, we will find actually it doesn't.
[4:43] Let's just turn the buttons off.
[4:46] So we can see that actually it doesn't... there's nothing in the animation file.
[4:50] Okay. And we can verify that by coming to sequencer.
[4:54] And if I were to turn off the face entirely, so there's the face, I turn that off.
[4:59] We can see that it's actually... it's still animated, right?
[5:02] So there's a weird thing there. And ideally what we want is we want this to be a face animation
[5:07] because we're going to have a body animation and we're going to drop the face animation into the face slot to use alongside it.
[5:13] So this perplexed me for a little while and I figured out how to make it work.
[5:19] If you do this on 5.8, I think it just does this anyway.
[5:22] But if you're using 5.7 and possibly earlier versions, this is how we do it.
[5:27] We're going to come to face and we're going to bake it to the face rig, bake to control rig face board.
[5:34] Okay, and then we get our baking controls and we hit create.
[5:38] And note that I've unlocked this. I didn't mention it, but I unlocked this as a lock thing here.
[5:44] You have to unlock it before you do this.
[5:47] Okay, so now it's baked. If we turn off the body, we still get the face animation.
[5:52] So that's what we want. That's what we want to get. I don't know why it does that. I don't know why.
[5:57] But now it's done it. Now we can go right click and bake animation sequence.
[6:04] I'm going to call this animation sequence.
[6:08] So, yes, Tom, idle, let's call it 02.
[6:14] I think I've recorded one before. So Tom, idle, 02 and hit OK.
[6:20] Then we get the export controls and we go export. Great.
[6:24] And now if we come and browse to that animation that we just exported, we will see now that Tom, idle, 02 has all the animation, including the head animation.
[6:34] Let's just put that to the test now. Very quickly, new level sequence.
[6:38] Let's just grab Tom and drop him into sequence set now.
[6:43] If we're going to try this, we'll get rid of the control rigs.
[6:47] What we're going to do is we're going to add an idle to this.


### Detached head bug - solved! [6:50]
**Transcript (timestamped):**
[6:51] Now in theory, we should add an idle for his face and we should be good, right?
[6:56] Not so fast. Not so fast.
[7:00] Oh, look, it's broken. Oh, no. It's broken.
[7:04] And it's not just a little bit broken. If I was to make this a bit more of an ambitious animation,
[7:12] where it actually moves, we can see that the head staying there is a problem.
[7:16] So how do we solve the problem of the head? Well, here's how we do it.
[7:20] We're going to find the animation that we just created.
[7:23] Now, you might have seen in other videos that we have a technique for actually creating an editable version of these things
[7:29] by coming, opening the animation sequence and clicking on here and going edit in sequencer and baking to our control rig.
[7:36] So we're going to bake this to a face control board, hit bake.
[7:40] And this, as I've discussed in other videos, will now open up a level sequence that directly controls this animation sequence.
[7:49] So here it is. Again, ignore those pajamas.
[7:52] This is, as we can see, this is our level sequence with the bake to the control rig.
[7:58] And any changes that we make here and save will be updated in the animation clip itself.
[8:04] And so there's a simple change we need to make to make the head work.
[8:08] When I open up these controls come right down to the bottom.
[8:10] We'll see there's a head, IK switch control.
[8:13] Okay. And what we're going to do is grab all those keys and delete them.
[8:17] And this is just simple on or off and it's on and we turn it off.
[8:22] So hit zero and hit save.
[8:25] What we'll notice is now we've killed the head animation.
[8:29] Now that's probably all right for an idol because actually you might just want there to be animation.
[8:34] You might have body motion that's controlling the face.
[8:36] So that's probably fine anyway.
[8:38] So we can see now head motion is gone.
[8:40] And if I were to come back to here, we will see that the head now goes along and we can see that it's animated.
[8:50] Well, the fact that we can move this and we can see the updates on the face.
[8:55] So that's an idol for the face.
[8:58] All right. It keeps him alive.


### Generating lip sync and performance from an audio clip [9:00]
**Transcript (timestamped):**
[9:00] Right. So let's look now how to use an audio clip to generate a metahuman performance.
[9:04] Now for space walker, as I said, I've recorded actors.
[9:07] So I've got all the lines separated out.
[9:09] So here's an audio clip, for example.
[9:12] I'm not getting excited.
[9:14] Sound excited.
[9:16] Just to mean it's progress through speaking to me.
[9:22] Okay. I've also left two seconds at either side because I'm going to use those as my blend windows.
[9:27] So if I wanted to mix an idol into this performance, I'm going to need a bit of a buffer so there's no clicking as the animation clip turns on.
[9:37] So I've left two seconds at either side when I do these.
[9:41] So in order to do this, I'm going to create a metahuman performance.
[9:45] So we right click and go to metahuman and metahuman performance.
[9:50] And I'm going to name it the name of my file with MHP at the front as the prefix for metahuman performance.
[9:57] And that just keeps everything nice and tidy.
[10:00] Tom, raw, V01, as you explain the naming convention there, there is an affected version of this, the effects version.
[10:09] That's actually the one that's going to go into the film, but I'm using the raw one, the clean one, to generate this performance.
[10:17] Just in case the distortion that comes with the comms effect throws it off and makes it impure in any way.
[10:23] And then V01, just in case, I ask the actor to re-record the line in some way and then I'll change it to VO2.
[10:30] So that's the naming system there.
[10:31] So we can open this up and we're going to choose audio.
[10:34] We're going to drop our audio file into it.
[10:38] I've changed this to control rig.
[10:39] That's to control the head movement.
[10:41] I've just found that's the best one to use.
[10:43] We can set a mood.
[10:44] Choose one of these.
[10:45] He's a little bit sad.
[10:47] He's a little bit sad.
[10:48] He's a little bit angry.
[10:49] He's a little bit surprised.
[10:50] It's a little bit nuanced.
[10:51] I might put it on anger and just add it to 0.25.
[10:53] Let's see what comes up.
[10:54] So we're going to hit process.
[10:56] We can always reprocess if we're not happy.
[10:59] So once this process, the green bar comes up, now I'm going to choose a visualization mesh.
[11:03] I didn't do this first because I found that it can crash.
[11:07] So we choose the visualization mesh and I'll just wait a minute and then we'll come and
[11:11] see what we've got.
[11:12] We can play this back now.
[11:13] I'm not getting excited.
[11:16] Do I sound excited?
[11:18] It just means progress through speaking to me.
[11:24] See that's really good, right?
[11:26] That's really good.
[11:27] Now the nuance in that compared to what I was capturing when I was speaking to the webcam,
[11:32] I think that's leagues ahead.
[11:34] I think that's really good actually.
[11:36] I'm not getting excited.
[11:37] The anger, you can just say that little flash of anger there.
[11:40] She's good, right?
[11:41] What we're going to do is we're going to export a level sequence.
[11:44] All right, and I'm going to put it in the same folder here for the level sequence.
[11:50] So save that.
[11:51] I'm going to choose our target metahuman, which is of course Tom.
[11:55] Now, ultimately, we're going to create an animation clip, but the reason I want it in
[11:58] an animation sequence first will become apparent now.
[12:02] So we can turn this off and we're going to open up the animation sequence.
[12:06] And we've got Tom in here in all these regalia.
[12:09] And we've got a camera, which we don't need to.
[12:11] We can get rid of that camera and we can get rid of this camera cuts track as well.
[12:15] Now we've got the audio and Tom and we can see what's going on.
[12:18] I'm not getting excited.
[12:22] Do I sound excited?
[12:24] Just mean it's progress through speaking to me.
[12:29] Okay, so the next thing we're going to want to do is we're going to need to, as we've
[12:34] already discovered, we need to turn off the head motion.
[12:37] Now, the weights of the head motion in this is exactly the same as we already did.


### Retaining natural head motion from a generated performance [12:42]
**Transcript (timestamped):**
[12:42] But I don't want to lose the head motion.
[12:45] I want to take it and I want to apply it to the character when he's making this performance.
[12:49] So we're going to do an extra step first.
[12:52] I'm going to grab an basic actor, which comes down here.
[12:58] All right, and we're going to come to the start and we're going to choose our face mesh
[13:03] and we're going to come to constraints in the animation menu.
[13:07] Constraints and with the face mesh selected, I am going to press this button here to set from current
[13:14] selection and I'm going to choose face and then head.
[13:18] Now, what this is going to select is the head bone that's driving those motions.
[13:24] So if I just actually, let's just demonstrate this first off.
[13:28] We can see our head control and we'll see that actually the head controls not moving, right?
[13:33] The head is moving independently of the head control and that's because that head motion
[13:37] has been driven by an interior joint and that is in world space, which is why when this body
[13:43] moves off the origin, it's going to keep the head where it is because it's in world space.
[13:48] But actually, all I really want to retain is the rotations that are on this head.
[13:52] I just want to be able to have a little bit of that because it's cool and I got it for free.
[13:57] I want to be able to retain a little bit of it and have the option to use it down the line.
[14:01] And that's the reason we made this level sequence and not just an animation clip.
[14:05] So we've got our Tom head from the face selected as the parent here.
[14:12] I'm going to grab my acta, I'm going to add and another rotation and turn off the offsets.
[14:18] Let's actually, we'll come to the star frame first.
[14:20] I always remember to come to the star frame when you're doing constraints if you mean it to be on the whole thing.
[14:24] So offset, turn on that and hit create.
[14:27] And now we saw that actor move and now if we scrub this, we can see that the actor is moving.
[14:32] Which is what we want.
[14:34] And what we want to do now is we just want to bake this to that actor so that we've got the animation curves
[14:40] and we can copy them onto an animation layer when we want to use this animation.
[14:45] However, as of version 5.7 and I know that 5.8 is out but 5.8 is currently I'm finding for the things I'm doing
[14:52] a little bit unreliable and a little bit prone to crashing.
[14:56] So maybe when it gets more stable, this will be fixed but as of right now, we can't bake that constraint.
[15:02] When we do, it does nothing.
[15:04] All right, which is not what we want. We don't want to do nothing.
[15:07] So what we're actually going to do instead is go to our take recorder again.
[15:13] And what we'll do is we're where it says here.
[15:15] So we're going to see that this is called ls is 0138.
[15:18] We're going to add 0138 to our take recorder to record into which now opens our shop back up
[15:26] and we can add our actor that we've got here.
[15:31] And we can literally just hit record.
[15:34] And that will bake the actor down, give it some animation curves and all will be fine.
[15:41] So it gets to the end.
[15:43] It stops is going to create as a sub level sequence.
[15:46] So now we can see that we've got that animation baked onto the actor inside this level sequence, which is good.
[15:52] And so the other thing to do now is take the animation sequence,
[15:57] I'm going to go OK and export.
[16:00] And now we can come and check that out and we'll see that it's baked down and there's no head motion, which is what we want.
[16:08] So now let's do a test and actually add this now to a performance.
[16:14] So we can come to it and we'll add our Tom astronaut.
[16:20] We're going to add an animation to him.
[16:22] So I'm going to give him one of my floaty idle animations.
[16:25] So we've got our idle space idle slope.
[16:29] Here he is.
[16:30] So he's floating as astronauts want to do.
[16:33] And then in order to get access to the controls, we are going to, of course, bake that down to a control rig as as ever,
[16:40] baking down default options.
[16:43] And there we go.
[16:45] And now we'll come to our face and we know that we can add our face to this.
[16:50] So we'll go to face and we'll add animation to face animation 138.
[16:55] See it.
[16:56] So now the animation, the face animation is on.
[17:00] Let's add the audio so we can hear it.
[17:02] OK, so that'll do.
[17:04] And then we might want to add the motion that we got from from the head.
[17:09] We want to add that to this to this performance.
[17:12] Let's go and get it.
[17:14] So we're going to get it from this subsequence.
[17:18] So we can do to get access to the actor that we baked things down to.
[17:21] We can just quickly add a subsequence and we know that we called that 138.
[17:26] And it's the actor.
[17:28] This is the one that we recorded.
[17:30] So here it is.
[17:31] So now we can click it through into here and we can find it and get our rotation.
[17:36] And the way we're going to do this is we're going to grab a curve at a time in here and copy and paste.
[17:42] So to grab them all copy.
[17:45] They go back out and that was that was the X curve.
[17:49] We're going to add our head control to a layer, an additive layer, come to here.
[17:54] So that's our base animation and then we come to our head control and rotation role.
[17:59] Come to the start frame and hit paste.
[18:02] When I come into subsequence, grab our pitch and grab that and control seek back out into our animal layer, paste, back in one more time.
[18:15] We're not going to want all of this either.
[18:16] We just want to make sure that we've got just some of the animation from it.
[18:20] This isn't perfect.
[18:21] On the other face, I would like to be able to just have this work by default, but I also really value those nuances.
[18:26] And so I'm working to try and get them in.
[18:28] And so here we go and paste that.
[18:30] So now what we should have now is some of that nuance on the head from the performance.
[18:36] There we go.
[18:37] I'm not getting excited.
[18:39] I sound excited.
[18:41] Just mean it's progress through speaking.
[18:46] And of course, if that was too much, and in my case, it might be because there's only so much room with your movie's head before it has a poke out the helmet.
[18:54] We can of course turn down the layer strength.
[18:56] So this is half of the animation.
[18:59] I'm not getting excited.
[19:00] I sound excited.
[19:02] Just mean it's progress through.
[19:06] All right.
[19:07] I think you can see the value, right?
[19:09] The value of doing that, of getting this in.
[19:11] Not getting excited.
[19:12] See a little head shake there?
[19:13] Like, that's valuable, valuable data to go into your animation.
[19:19] It brings it brings it alive a bit more.


### Adding life with layered eye controls [19:21]
**Transcript (timestamped):**
[19:21] Now it's still looking a little bit dead.
[19:24] So we're going to add another thing.
[19:27] We're going to, we're going to bake his animation to the face rig.
[19:34] Bake to face rig.
[19:36] The thing that is missing now is eye direction.
[19:39] Okay.
[19:40] And the thing to remember is that very rarely do we look straight ahead at one thing just forever.
[19:45] We will constantly be adding eye dots and things like that.
[19:48] Now, one thing that we could do is we could go and we could grab the curves from our eye direction from our eye.
[19:54] That would be a good start, right?
[19:56] So we could do that, but we can also, we can just add layers to this.
[20:00] So that's the eye direction there.
[20:01] We can see that it's got, it's got animation that's, that's basically dead because if we come to look at the curves, there's no, there's no animation there.
[20:09] We're pretty sure, I'm pretty sure there's no animation there.
[20:13] So we can just delete that and we can, we can go in and we can just start looking at what's going on.
[20:19] So we can see this how we control it.
[20:21] So we can set a key and all we're going to do is add a tiny bit of animation to this now.
[20:28] I might even just square it back up slightly.
[20:32] So excited.
[20:33] Are we sound excited?
[20:35] Just mean it's progress.
[20:38] Now eyes move very quickly.
[20:39] So when you do an eye dots, move the keys very close together.
[20:44] I'm not getting excited.
[20:47] And then when you've moved one, hit key to say there again, and then a few frames over and then move it back.
[20:56] I'm not getting excited.
[20:57] Are we sound excited?
[20:59] Are we sound excited?
[21:02] And the other thing that we might want to do is add blinks.
[21:05] Now, if we come and look at this blink control,
[21:07] we can see that there's actually only one blink over here that looks like is that a blink?
[21:13] It's not even a blink.
[21:14] Like that's the, there's one right at the very end.
[21:18] There's a blink.
[21:19] So adding some blinks would be useful and we can add those onto a, onto an animation layer.
[21:26] So we can go blink.
[21:27] We might want to add our left eye blink to that as well.
[21:31] I'd selected.
[21:34] And then we come down here and we can just wherever we feel like it,
[21:37] we can just add two frames there, one or three on each and then come over it, two or three key frames and set this to one.
[21:45] Come over another key frame, set again.
[21:47] This is generally how you animate a blink.
[21:49] And then two or three frames over again and zero, zero back out.
[21:54] And now we've just added a blink.
[21:57] And if you were timed that over one of the eye dots, watch this.
[22:01] So down and then we come back up the eyes moved.
[22:04] Right.
[22:05] So that's how I actually move.
[22:07] And what of course we do is we copy these and we'll just paste them down here to create another one.
[22:11] And what we want to do is you want to cover that down up there, cover it with an eye blink and you'll find it looks pretty cool.
[22:19] Right.
[22:22] I'm not getting excited.
[22:25] I sound excited.
[22:27] There we go.
[22:28] How to add extra animation to our performances.
[22:31] And we can also of course, as I said, copy them from other from other animations that we've recorded.


### Blending between an idle and a full performance [22:36]
**Transcript (timestamped):**
[22:37] Now, the final thing that I want to show very quickly is how to blend between them.
[22:41] This is my idol that we recorded for.
[22:44] And now if we want to go from an idol since it's a really long take.
[22:49] And we want to come from my idol and we want to blend into the into the lip sync performance.
[22:56] What we're going to do is we're going to bring another animation in at the start here.
[23:01] So go to animation, I want to be eight.
[23:05] And we can see that now the two of them on top of each other.
[23:08] So what's happening now is that these two are combined.
[23:11] So effectively, they're both at kind of 50% of each other.
[23:15] I'm not getting excited.
[23:16] We sound excited.
[23:17] So it's kind of suppressing the lip sync, which we don't want.
[23:20] So what we're going to do is we're going to expand these down and we see we get weights.
[23:25] And we remember we've got a two second delay here, right?
[23:28] And that's what this is for.
[23:29] So two second delay, we want to make sure this is on one and this is on zero.
[23:36] All right.
[23:37] So now we can see it's completely dead because the idols have no effect.
[23:43] But right here, we can set the idol to one.
[23:46] So the idols on and then our facial performance starts, but we can see and it's pretty good.
[23:52] It's not bad.
[23:53] We see there's a slight pop where this one comes on.
[23:56] So all we need to do really is just take this down at this key frame to zero.
[24:01] And so now as they blend across from each other, we get a blend off of the idol and a blend on the facial performance.
[24:14] And we can make that time be less, of course, because that's completely valid as well.
[24:20] So we keep the idol on.
[24:23] I'm getting excited.
[24:24] So those are my lazy animated tips for animating metahuman faces.
[24:33] I hope that has been useful.
[24:34] I am using this on my film Space Walker for the rough cut.
[24:38] Space Walker will be a live action movie.
[24:40] But the first, the rough cut will be using this guy as a metahuman stand in for our eventual actor for his face only.
[24:48] And so this is going to be super important for when I present the film as a finished rough cut with a real performance on it.
[24:55] So I hope that was useful and you can get me in the comments and whatnot.
[24:58] Feel free if you're a struggle with any stuff, you can get me on a one to one as well.
[25:01] There's a link down below and I'll catch you down the road.
[25:10] Music



---

## Captured Frames

- [2:03] tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/frame_000.jpg
- [2:31] tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/frame_001.jpg
- [5:27] tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/frame_002.jpg
- [7:04] tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/frame_003.jpg
- [8:10] tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/frame_004.jpg
- [9:45] tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/frame_005.jpg
- [10:45] tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/frame_006.jpg
- [13:07] tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/frame_007.jpg
- [17:54] tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/frame_008.jpg
- [20:21] tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/frame_009.jpg
- [21:37] tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/frame_010.jpg
- [23:20] tutorials/frames/5-lazy-animator-tips-for-metahuman-facial-animation/frame_011.jpg

---

## Structured Notes

### Core Technique
Five workflow shortcuts for making a MetaHuman's face feel alive without full hand-keyed animation: (1) record/generate an idle face performance to layer under body idles, (2) generate lip-sync + emotional performance from a dry audio file via MetaHuman Performance, (3) recover and layer the *head* rotation the performance generator computes internally (normally discarded) as an additive on top of a body animation, (4) hand-add small eye-dart and blink layers on top of a generated performance, (5) blend an idle into a full performance across a short crossfade window using Sequencer section weight curves.

### Summary
Working in a live level sequence with a MetaHuman ("Tom") from the presenter's in-progress film *Spacewalker*, the video walks through cheap ways to add life to MetaHuman facial animation. It opens with idle capture via Take Recorder + Live Link Hub's webcam-based "MetaHuman Video" source, then hits and fixes two real UE 5.7 bugs: (a) Take Recorder's face clip is empty until you bake to the Face Control Board first, and (b) a baked idle drags the head off model when reused elsewhere unless you zero the Head IK switch control. It then covers generating a full lip-sync performance from an audio clip via MetaHuman Performance (mood/mood-intensity dropdown), a trick to preserve the natural head-bob the generator computes (constrain an actor to the interior head joint, bake via Take Recorder since direct constraint-baking is broken/no-ops in 5.7, then copy the actor's rotation curves onto an additive Animation Layer), manually sweetening eye direction and blink curves on an additive layer, and finally crossfading an idle into a generated performance using the two 2-second blend-window weight curves left on either end of the audio clip.

### Key Steps
1. **Idle capture:** Live Link Hub → Add Source → "MetaHuman Video" → Connect (activates webcam). On the MetaHuman, enable "Use Live Link" and pick the Live Link subject (camera feed). Take Recorder → add the MetaHuman actor → Record while performing small ambient head/eye motion (no dialogue) → produces 3 clips (head + 2 body).
2. **5.7 empty-face-clip bug fix:** the recorded "head" animation clip is actually empty (verify in Sequencer by toggling the face track off — the face is still animated from elsewhere). Fix: open the Face track → **Bake to Control Rig → Face Control Board** (must unlock the track first) → right-click the baked layer → **Bake Animation Sequence** → export. The exported sequence now genuinely contains the head motion. Presenter believes 5.8 may not need this step.
3. **Detached-head bug fix:** dropping that idle face-anim sequence onto a *different* body animation leaves the head floating in place while the body moves. Fix: open the animation sequence → **Edit in Sequencer** (bakes to a live-editable Control Rig level sequence) → scroll controls to the bottom → find **Head IK switch control** → select all its keys → set to 0 → save. This kills head-follow-body IK but is normally fine for an idle since body motion should drive the head anyway.
4. **Generate a performance from audio:** Content Browser → right-click → **MetaHuman → MetaHuman Performance**. Naming convention used: `MHP_<clipname>_V01` (raw/clean audio preferred over FX-processed audio, since audio effects can throw off the solver; leave ~2s silence padding at both ends of the source audio for later blend windows). Inside the asset: assign the audio file, set Head Movement Mode to **Control Rig**, optionally pick a **Mood** + mood intensity (Happy/Sad/Angry/Surprised, etc., 0–1 slider) to bias the emotional read, hit **Process**, then assign a **Visualization Mesh** only *after* processing (assigning it first was found to crash). Export as a **Level Sequence** targeting the MetaHuman.
5. **Preserve the generated head motion:** the performance's head sway lives on an internal joint in world space (not exposed on the rig's Head control), so it would normally be lost when only the face-anim portion is reused. Workaround: spawn a **Basic Actor**, go to the actor's transform, use **Constraints → Set from Current Selection** with the face mesh's **Head** joint chosen as parent, add a rotation constraint (offset off) from the frame the level sequence starts on, hit Create. Direct "Bake to actor" on this constraint is broken/no-ops as of 5.7 — instead, add the actor into **Take Recorder** on the same take and hit Record to bake real curves onto it. Copy the actor's rotation curves (X/Y/Z, i.e. roll/pitch/yaw) and paste them onto an **additive animation layer** driving the MetaHuman's Head control in the final sequence; trim to keep only the useful portion, and use the layer's strength slider to dial the effect down if it's too strong for the framing (e.g. inside a helmet).
6. **Manual eye life:** after baking the performance to the Face Control Board, select the eye direction control (often has zero/dead keys by default) and hand-key small eye-dart movements — keys placed close together since eyes move fast. Add blinks on a separate additive layer: for each blink, key ~2-3 frames apart (0 → 1 → 0) on the blink control(s) (left/right eye blink selected together), ideally timed to land during an eye-dart so the movement reads as a natural look-away.
7. **Idle → performance crossfade:** in Sequencer, place the idle face-anim section starting at the top of the timeline, overlapping the performance section which starts after the audio's leading 2s pad. Expand both sections to show their weight curves. At the start: idle weight = 1, performance weight = 0. At the point the audio's silence padding ends (2s in): keyframe idle weight down to 0 and performance weight up to 1, so the two crossfade smoothly instead of the lip-sync being suppressed by a 50/50 blend for the whole clip.

### UE Systems / Blueprints / Settings
Live Link Hub (MetaHuman Video source, webcam-driven), Take Recorder, MetaHuman Control Rig (Face Control Board, Head IK switch control), MetaHuman Performance asset (Head Movement Mode: Control Rig, Mood/Mood Intensity), Sequencer (Bake to Control Rig, additive Animation Layers, section weight curves, Constraints panel / Set from Current Selection).

### Difficulty
Intermediate — no Blueprint/code work, but requires comfort with Sequencer layers, Control Rig baking, and animation constraints; several steps exist specifically to route around 5.7 bugs, so the mental model (why each workaround is needed) matters more than rote steps.

### UE Version
5.7 (presenter notes 5.8 is out but was unreliable/crash-prone for this workflow at time of recording; some bugs described, e.g. the empty face-bake clip, may not reproduce on 5.8).

### Tags
metahuman, facial-animation, live-link, take-recorder, metahuman-performance, control-rig, sequencer, animation-layers, lip-sync, idle-animation, constraints

---

## Related Entries
None yet — first MetaHuman facial-performance-specific entry in this library. Cross-link future MetaHuman animation/performance tutorials here.
