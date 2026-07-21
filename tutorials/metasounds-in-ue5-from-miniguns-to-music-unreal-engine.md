---
title: MetaSounds in UE5: From Miniguns to Music | Unreal Engine
source: YouTube
url: https://www.youtube.com/watch?v=3230-FwCts0
author: Unreal Engine
ingested: 2026-07-20
ue_version: "UE5 Early Access"
tags: [metasounds, audio, blueprint, pipeline, intermediate, advanced, ue5-0]
extraction_status: complete
frames_dir: tutorials/frames/metasounds-in-ue5-from-miniguns-to-music-unreal-engine/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# MetaSounds in UE5: From Miniguns to Music | Unreal Engine

**Source:** [YouTube](https://www.youtube.com/watch?v=3230-FwCts0)
**Author:** Unreal Engine
**Duration:** 28m53s | 11 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, I'm Chris Murphy and today we'll be looking at MetaSounds in the Unreal


### Metasounds [0:07]
**Transcript (timestamped):**
[0:09] Engine 5 Early Access build.
[0:11] Now, UE5 debuted MetaSounds, which are a high performance audio system that gives you complete
[0:16] control over audio rendering.
[0:18] But if you know me, then you'll know that I'm a technical artist.
[0:22] And that's a bit confusing.
[0:23] Like, why would a technical artist look at MetaSounds?
[0:26] Well, I'm kind of hooked.
[0:28] And the reason I'm hooked is because it lets you drive audio in a way that's almost like
[0:32] the Unreal Engine's surface materials.
[0:34] Conceptually, I want you to picture audio shaders.
[0:38] And today we're going to be going from MIDI guns to music to show you some of the cool
[0:41] things that you can do with MetaSounds in Unreal Engine 5.
[0:45] Before we begin, I want to give a big shout out to Dan Reynolds and Aaron McLaren from
[0:49] the audio team for helping out in assembling this demo.
[0:52] So we're going to begin with this MIDI gun.


### Mini Gun [0:53]
**Transcript (timestamped):**
[0:54] This allows to create a rather straightforward setup with multiple layers of audio.
[0:58] It's a great starting point to understand the basics of MetaSounds.
[1:02] Because let's take a look at it.
[1:03] Well, when it begins, we can see that it fires up, it spins up, it starts firing, goes for
[1:09] a little while, it stops firing, and then it spins down.
[1:14] Now, this is perfect for driving something like this through MetaSounds.
[1:18] Because we're actually going to have the audio control all of the spinning up and spinning
[1:21] down, the starting, the stopping, and the repeating of all of the shots through it.
[1:26] And I'll show you how that works now.
[1:28] Let's begin by going ahead and creating our first MetaSound.
[1:31] I'm going to go right-click, sound, MetaSound.
[1:34] It's worth noting that if you don't see this here, it's because you may not have the plugin
[1:38] enabled in your plugins.
[1:41] So I'm going to create a new one, and I'm going to call this MiniGun Audio.
[1:44] Okay, and we're going to double-click on this and work with our first MetaSound.
[1:50] Now, for this first effect, what we need to do is we need to go ahead and set this up
[1:54] such that it will drive the audio that's there.
[1:58] Now there's a few steps to that.
[1:59] We have the spinning, we have the firing.
[2:01] So let's begin with the spinning.
[2:03] Now, if you're familiar with SoundCues already, this all already may be familiar to you.
[2:08] If you're not, then, well, welcome to the Graph Editor.


### Graph Editor [2:09]
**Transcript (timestamped):**
[2:11] I'm going to go to here, and I'm going to drag off of this on-play, and I'm going to
[2:14] say to it, I want to have a wave player.
[2:17] This means I want it to play audio when we start the effect on-play.
[2:22] And the audio that I want to play is going to be the wine's sound.
[2:30] So we can see that we have this barrel wine start.
[2:33] Now, if I was to hit play, nothing happens, and nothing happens because we need to actually
[2:39] tell it what to play.
[2:40] So I need to actually drive this audio stream into this output over here.
[2:45] Okay?
[2:46] So this is the time if I hit play, we can hear that that started to play, but it immediately
[2:52] stopped.
[2:53] And the reason it immediately stopped is that it needs more audio in there to keep functioning.
[2:58] We actually need to go ahead and get another wave player, but this one is going to be the
[3:02] loop.
[3:03] Now, to drive this into this, we actually say, hey, when you finish, I want you to play
[3:09] the looping audio, and I want that looping audio to keep looping indefinitely.
[3:16] Now you may be thinking, well, I guess you just plug that in, but you'll notice that
[3:20] we have a bit of a problem.
[3:21] And that is that I need to have a mixer in place to actually put these things together.
[3:29] So if I connect these up, it'll now combine these two sounds together.
[3:35] Wonderful.
[3:39] So we can see that this is working, and we can get a pretty good idea of like, you know,
[3:43] okay, one thing can feed into another and drive events.
[3:46] Wonderful.
[3:47] So where do we go from here?
[3:49] Well, we have the winding up.
[3:51] We have the wind looping.
[3:52] Let's go ahead and look at having something that's a little bit more interesting than
[3:56] just this looping sound playing itself over and over again.
[3:59] Let's this time take a look at modifying its pitch.
[4:03] Now we can see we have a pitch shift variable here.


### Pitch Shift [4:04]
**Transcript (timestamped):**
[4:07] So if I was to read something into this, say a value of five, it sounds terrible, but
[4:15] it proves my point.
[4:16] And that is to say that the pitch shift is kicking in.
[4:18] So it's going ahead and it's driving that up.
[4:21] But if I want to, I could actually go ahead and set that to programmatically drive itself
[4:25] up over time, maybe not to the level that we just did.
[4:29] But for this, I can use what is called an envelope.


### Envelope [4:31]
**Transcript (timestamped):**
[4:32] And I'm going to use an envelope float, specifically an ADSR.
[4:37] When this effect finishes, so when the first part finishes, it triggers this, which is
[4:42] going to say over this amount of time to go ahead and raise this value to whatever is
[4:47] in the sustain level.
[4:49] So if I was to plug this in, this would go from zero to one.
[4:54] In this situation, I want to go from something that's a little bit higher, but I might go
[4:57] ahead and just pull it out here so it's a little bit easier for me to manage.
[5:02] So I'm going to get this value that's zero to one, and I'm going to multiply it by 2.5
[5:06] so that it's from zero to 2.5.
[5:10] And we're going to plug that into the pitch shift this time.
[5:12] I'm going to take a listen.
[5:23] Excellent.
[5:24] So that's functioning.
[5:25] The next part for me to go ahead and do is to get the Stinger effect and to play the


### Stinger [5:26]
**Transcript (timestamped):**
[5:30] winding down.
[5:31] So I'm going to get this and I'm going to play wind barrel stop.
[5:34] But there's no particularly good place for me to connect this at the moment.
[5:38] But fortunately, I can make one because I can actually go ahead and I can create inputs
[5:44] that trigger via a name that we've set up.
[5:47] So if I was to create one called spin down, spin down is now going to go ahead and say,
[5:52] I want you to play this barrel stop sound.
[5:56] For completeness sake, I want to go ahead and I also want to stop the barrel loop.
[6:01] And in theory, if it's playing, I also want to stop this effect.
[6:04] And let's take a listen.
[6:10] Wonderful.
[6:11] So that actually goes ahead and plays that separate sound that stops the others.
[6:15] Now as one little thing that I'd like to do to get this really working the whole way through
[6:19] is instead of this just being on play, in the event that we haven't fully destroyed the
[6:24] sound and they start spinning it up again, we probably want the ability for this to actually
[6:28] spin up again as well.
[6:29] So I'm going to get my spin down trigger and I'm going to go ahead and create another
[6:34] one this time called spin up.
[6:38] Okay.
[6:39] So we have spin up and we have spin down.
[6:42] I'm going to go ahead and I'm going to set this to play, but I want this to trigger in
[6:48] any situation, whether it is told to play or whether it is told to oops, sorry, this
[6:58] needs to be set as a trigger.
[7:00] It's wondering why that didn't appear.
[7:03] Spin up.
[7:04] Okay.
[7:05] So I can play.
[7:07] Cool.
[7:10] So that's mostly functioning.
[7:19] The only thing I might do here is I might set this spin up to also release it.
[7:25] Wonderful.
[7:43] So we're all set up on that part of things.
[7:45] Let's go ahead and look at how to get the shots firing over the top of this all.
[7:49] So to do this, I'm going to ignore this graph section that we have up here.
[7:53] So I'm going to create a mixer and I'm going to plug this in and I'm going to temporarily
[7:58] set its volume to zero.
[8:00] So we don't really have to think about it.
[8:01] In case you're wondering, this effect is a mono effect, which is why I'm only using
[8:05] the left channel of all of these outputs.
[8:07] If you want to, you can go metasound and you can create a stereo effect as well.
[8:12] But onwards, let's get the firing working.
[8:15] Well the firing working is reasonably straightforward for the initial part, but we're going to do
[8:20] some fancy stuff too.
[8:21] So once again, I'm going to do the same as before.
[8:23] I know I need a wave player and I'm going to go ahead and just play a shot firing.
[8:28] For future reference, I have three separate shot fires.
[8:31] Now I could plug this in and I could on play, go ahead and call play.
[8:39] We'd end up with this and if I was to mash it, not particularly great, but that's okay.
[8:47] So how do we make this better?
[8:49] How do we make this more interesting?
[8:51] To begin with, we want this minigun firing again and again and again and again.
[8:55] So I'm going to go ahead and I'm going to trigger a repeat, which allows me to specify
[9:00] a time period for it to play.
[9:06] That's kind of cool.
[9:07] One thing I'd actually like to do is something along the lines of having a BPM.
[9:11] So actually setting it up with a value that was called shots per minute.
[9:15] So I'm going to go ahead and add that and I will call it shots per minute.
[9:20] And we're going to hit play.
[9:24] All right.
[9:30] That's gross.
[9:32] So the reason that sounds so bad right now is that every single time it's playing, it's
[9:36] going ahead and stopping itself the next time it plays.
[9:40] So that's the first thing that we're going to need to consider.
[9:43] Now the next thing that we need to consider is that it's all the same shot.
[9:47] So how do we go ahead and fix it so that it's not always playing the same effect again
[9:51] and again and again?
[9:53] And the last part is, you know, even if we change the shot sound effects, wouldn't it


### Change the Pitch [9:56]
**Transcript (timestamped):**
[9:56] be great if we could change the pitch of each shot?
[9:59] Well, yes to all.
[10:01] So let's go ahead and step through those.
[10:03] The first of them I'm going to do is I'm actually going to go ahead and play this sound effect
[10:07] by pulling it from a collection of sounds.
[10:10] So I'm going to say, hey, I want you to randomly play a sound.
[10:14] Specifically, I want you to randomly play a sound from an array, which I'm going to
[10:21] make as an input.
[10:22] And I'm going to call this shot array, which is going to be set to fire one, fire two,
[10:33] and fire three.
[10:35] So if I was here, play.
[10:42] Wonderful.
[10:43] So that's changing around each time.
[10:45] It's switching between different shots.
[10:47] That part's working.
[10:48] Now, the next thing that I might want to go ahead and do, as I said, is change the pitch.
[10:52] And once again, I can say, hey, every single time you play, why don't we go again, a random
[10:57] number between negative 0.5 and 2.
[11:02] Sounds good.
[11:03] And the same as before, why don't we then pitch shift that into place?
[11:10] Cool.
[11:14] So that's working.
[11:15] For clarity sake, I could also plug that into here, and that would function in the exact
[11:19] same way.
[11:20] But there is another thing I'd like to do, and that is that I would like to be able to
[11:23] play multiple sounds over the top of each other so that the sounds don't keep clipping
[11:27] again and again and again.
[11:29] Now, fortunately, that part is pretty easy to do as well.
[11:34] However, I need to go ahead and I need to change this just a little bit.
[11:38] And that is that after we say, hey, I want you to play this next sound, what I need to
[11:43] do next is I need to count the sounds.
[11:46] And I'm going to say to these, I want you, this is an important step, is I want you to
[11:54] disconnect this for time being.
[11:56] I want you to count the number of shots that we're up to, and I want you to compare them.
[12:02] So if the current value is a value of 1, because we're on the first shot, play this.
[12:09] If however, it's not, then I'm going to get these, and I'm going to duplicate that entire
[12:16] setup that we have.
[12:18] And if it's not, I'm going to compare it, and I'm going to say to it, well, why don't
[12:22] you see if it's number 2?
[12:24] If it's number 2, play that instead.
[12:27] And finally, if it's neither 1 nor 2, play 3.
[12:34] And once again, we need a mixer to combine these three separate waves together.
[12:43] And I need to plug it in.
[12:46] So, cool.
[12:48] So that's all working.
[12:51] Actually, I'll keep the spin off for the time being.
[12:53] So let's take a listen to what that sounds like.
[12:57] Wonderful.
[13:00] So that's functioning now, and we have the ability to kind of play through here.
[13:13] So that's all playing.
[13:14] And let's go ahead and set this to play as well.
[13:18] Last thing I'm going to do here is instead of just saying on play, do that, I'm going
[13:21] to create a new input, which is going to be called start fire.
[13:28] And I'm going to stop it on stop fire.
[13:31] So we're going to create a new graph input.
[13:51] Wonderful.
[13:52] So that's all it really takes to kind of get this going.
[13:55] If I save it, I can then go back to here and I can apply this to my minigun.
[14:00] Just going to open up the blueprint, and I'm going to set this up such that it's all plugged in.
[14:05] So to do that, I'm going to set minigun audio, which I created earlier, to be the one that
[14:09] I just created called minigun audio.
[14:13] Now, if you want to play any of these triggers, all you need to do is get the parameter interface
[14:16] from the audio and then call the name of the thing you want to do when you want to do it.
[14:21] So what does this look like?
[14:23] Well, let's check it out.
[14:24] I'm going to hit play.
[14:33] Great.
[14:43] Cool.
[14:43] So we have the audio for the minigun done.
[14:46] Next up, let's go ahead and start looking at how we can go ahead and get some music playing
[14:51] out in this environment as an extension on Metasounds.
[14:54] Now, working with music in Metasounds is something that I find really exciting because this is
[14:59] some really cool stuff.
[15:00] So we can already see how the first section works, right?
[15:03] We can see that we can play sounds and whatnot.
[15:06] But let's go ahead and let's set up some music for out here in this environment.
[15:10] I'm going to go ahead and I'm going to create a new Metasound, same as before, and this is going to be
[15:15] called sci-fi music.
[15:18] Now, sci-fi music is going to be very similar to in some ways to before, but also very different
[15:26] because this time I'm not going to use a wave player.
[15:29] In fact, this time I'm going to generate sounds myself.
[15:33] We're going to make some procedural music.
[15:35] So check this out.
[15:36] If I was to create a square generator, you can hear something like this.
[15:39] My apologies.
[15:40] It's not going to sound great.
[15:43] All right.
[15:44] Very loud square wave.
[15:46] Not particularly wonderful to listen to, but it's the first step in making something cool
[15:50] because it takes a frequency and then plays that audio.
[15:53] And if I wanted to, I can go ahead and I can actually look up different notes in different
[16:00] scales.
[16:01] I can then find the frequency of them and play that accordingly.
[16:06] So if I wanted to check this out, I could go ahead and look up a scale.
[16:12] It's going to major scale right now for the time being.
[16:15] And the note I play is going to be a value.
[16:19] Let's get a different note every time.
[16:20] So we're going to get a random float.
[16:23] OK.
[16:24] Can plug this in.
[16:26] OK.
[16:26] So that's plugged in.
[16:27] I'm going to get a random float between 60 and 72 and check this.
[16:37] All right.
[16:38] Yes, that's not exactly Mozart.
[16:40] But it's another step closer to making something that I think is pretty cool because we can
[16:46] now see that that's going to play different notes from a different scale.
[16:50] You know, I can even go ahead and get a minor scale and start to get this.
[16:57] All right.
[16:58] Yep.
[16:58] I know.
[16:58] Still not wonderful.
[16:59] But bear with me for a second.
[17:01] Let's make this more interesting.
[17:03] First thing we've got to do is we need it to sound less horrible whenever a note plays.
[17:10] It's playing that square wave.
[17:12] But if we want to, we can use that same thing as we used before, the envelope, which kind
[17:16] of brought the sound up over time can actually be used to bring it up and down again.
[17:21] So if I wanted to get an envelope that automatically goes down again, I could do that here.
[17:28] I'm just going to multiply them together.
[17:30] And all we're going to do is I'm going to say, hey, when if you play a note, I want you to take this long to go in.
[17:40] Okay, that's kind of working.
[17:43] Let's get this automatically repeating and playing itself to a BPM so that I don't have to keep mashing that button.
[17:50] So same as before, I'm going to set up a BPM and I might as well go ahead and make that a variable.
[17:57] Which I'm just going to call BPM.
[18:01] Okay.
[18:10] All right, that's not great.
[18:12] But that's okay.
[18:13] Because what I'm going to do from here is I'm going to start to treat this as something that we can make a little bit more interesting.
[18:22] Because I can go ahead and I can look up this amount of time and I can make this last for only that period of time.
[18:28] Okay.
[18:29] So for instance, if I wanted to, I could get this and I could get this and I could get this.
[18:36] Okay.
[18:36] So for instance, if I wanted to, I could get this and I could say to this, I want to send this time out as a variable that I'm going to call bar time.
[18:49] This is going to be how long a bar takes.
[18:52] And because of that, I'm going to set this division of whole note to be one so that it takes a little bit longer between.
[18:57] Now over here, I can at any point receive a time, which in this case is bar time.
[19:07] And I can plug this in to make it last for this amount of time, but I don't quite want that.
[19:12] I actually want to get this and make it go for a point three three as the attack.
[19:18] So it takes one third of the bar.
[19:20] It comes in and four zero point six six.
[19:27] It's going to fade out.
[19:29] Let's check that out.
[19:34] Okay.
[19:34] Still, still not great, but we're on the right track here.
[19:38] What I'm actually going to do here as well is instead of just plugging this into here, I'm going to turn this into my own little beatbox.
[19:46] And that is, I'm going to send the trigger as well.
[19:49] And I'm going to call this bar trigger.
[19:53] And over here, we're going to receive bar trigger.
[20:00] Okay.
[20:00] So we're on by hit play.
[20:04] That's kind of just sending itself through.
[20:07] All right, cool.
[20:08] So the reason I did this is I'm also going to go ahead and I'm just going to duplicate it.
[20:12] But this time, instead of having this as the bar, I will actually make one that is beat trigger trigger spelled correctly.
[20:23] And I'm going to make one called beat time.
[20:26] Okay.
[20:27] Because if I wanted to, I could get these.
[20:32] Okay.
[20:32] I could get this exact same logic that we've got right now.
[20:36] And I could start to layer multiple effects on top of each other.
[20:40] It would help if I plug them all in.
[20:43] Okay.
[20:44] And I'm going to multiply that.
[20:47] Oh, sorry.
[20:47] No, multiply it.
[20:48] I'm going to mix that together.
[20:50] And now we're going to have one that controls sound that's playing over the course of the bar and one that is each individual beat.
[20:57] So for here, I just need to set this as beat time.
[21:03] And beat trigger.
[21:08] Okay.
[21:09] Now, another cool thing that I can do just before I completely finish this off is I can grab this and I can also send this as the current note.
[21:20] So now anything can look up the current note.


### Current Note [21:21]
**Transcript (timestamped):**
[21:22] So over here, instead of me just getting a random note to play, I actually could receive a float and find out the current note.
[21:33] More importantly, I could then subtract this number so that we find a note pretty close to the current note.
[21:41] And if I was to subtract a number between say three and eight and highlight chord tones only.
[21:50] Now I'm going to get me a random beat note that's similar.
[22:09] That's kind of cool.
[22:10] So we've started to kind of like get this feeding into this a little bit weird still, but that's okay.
[22:16] Because we're starting at something cool.
[22:18] And you know, I'd love it if this was actually said to say something really short.
[22:22] So it really came in quick like 0.05 and it faded out.
[22:27] So it almost actually cut itself off.
[22:37] All right.
[22:37] So we're starting at something here.
[22:38] That's kind of cool.
[22:39] I want this to sound a bit more sci-fi though.
[22:41] So I'm also going to go ahead and I'm going to make a ladder filter and props to Dan Reynolds for showing me this one.


### Ladder Filter [22:46]
**Transcript (timestamped):**
[22:47] Ladder filter allows me to kind of set a cutoff filter so that the sounds that play through it can actually we can change them up a bit.
[22:56] And it sounds a bit strange if I just hit play.
[22:58] But if I wanted to, I could go ahead and say, hey, every single time you go and you play an envelope for audio, I also want you to get an envelope for audio.
[23:10] And I want you to remap that so to arrange.
[23:13] I'm just going to say 200 to 2000, just as an example.
[23:18] And that is now going to control the ladder filter.
[23:22] So the reason I'm doing this is because if I want to, I can say every bar, I want to trigger this to play again.
[23:30] And I want this to take something pretty similar in terms of timing as this one.
[23:36] So I'm going to duplicate them just to make it a little bit more different.
[23:44] I'll set this one 0.25 and 0.75.
[23:46] Cool.
[23:48] And that's going to remap and play a ladder filter.
[23:50] All right.
[24:01] So that's kind of cool.
[24:03] We're starting to get somewhere.
[24:05] And now, though, as a final little piece is, and this is a little bit cheeky, is I'm going to get this and I'm going to send this value out as ladder filter.
[24:15] So I'm storing this, but I'm not feeding it to anything inside of this one.
[24:19] And the reason I'm doing this is I want you to show you something in the world with what we're creating.
[24:24] If I was to get this sci-fi music and just drag this into the world and I was to see it play.
[24:35] So if I was to set this up, we've got the music playing.
[24:40] But if I ever touch these little sections, notice they flare up.
[24:45] So a fun little thing we can do is those pickups that we saw in the world just now, these things, we can actually have separate sounds play off of them.
[24:57] And you can see that I've already set up the logic to play a sound at their location.
[25:02] OK, now the reason I've gone ahead and done this is because if what if instead of triggering just the bars and the beats, we also triggered the Quaver.
[25:13] You may know this as an eighth.
[25:16] OK, so Quaver.
[25:19] Same logic as before.
[25:21] So this is going to be eight.
[25:23] All right. So why have I done this?
[25:25] Well, let's go ahead.
[25:26] This time I'm going to create a new meta sound, which is going to be called pick up sound.


### Pick Up Sound [25:30]
**Transcript (timestamped):**
[25:34] OK, and pick up sound is actually going to be this section.
[25:43] Control C, except in here.
[25:49] This is now actually just going to receive it because sends and receives are actually global.
[25:55] And what this means I can do is I can actually have all the stuff as before in here to receive it and then output it inside of a separate pickup.
[26:07] So it actually layers these on top of each other.
[26:09] I don't want these to be beat time.
[26:11] I want these to be Quaver time.
[26:17] Current note is still the same.
[26:19] And this will now be on Quaver trigger.
[26:22] OK.
[26:23] Now I'm going to quickly plug pick up sound into my pickup.
[26:26] So I've set up a variable for that already.
[26:32] Check this.
[26:47] So that actually added those extra notes there.
[26:49] But the problem is, is it keeps playing it well to infinity.
[26:53] So let's go ahead and look at how to finish this off.
[26:56] And this part's pretty straightforward.
[26:58] What I need to do here is when we play it, I'm going to actually count the number of Quaver triggers that are coming through.
[27:06] So I'm going to count them.
[27:08] And I want to compare this.
[27:10] And I want to say to this, if this count that's come through is less than or equal to eight, then I want you to keep playing.
[27:23] Now, if it is not less than or equal to eight, then I want to get this and I want to delay for maybe one second and then finish the sound.
[27:34] And with that, we now have this.
[28:04] That's it.
[28:14] We now have procedural music that's being fed information from stuff within the world.
[28:19] And it was honestly pretty easy to make.
[28:22] So I'm really excited to see where this goes.
[28:24] I'm really, really excited to see what folks do with this because honestly, I can't wait to see how folks go ahead and create bigger and more impressive things than what I've just cooked up.
[28:34] So that's all for me.
[28:35] I hope this has been useful and I can't wait to see what everyone puts together with metasounds in an R01105.
[28:41] Thank you very much.



---

## Captured Frames

- [1:05] tutorials/frames/metasounds-in-ue5-from-miniguns-to-music-unreal-engine/frame_000.jpg
- [2:20] tutorials/frames/metasounds-in-ue5-from-miniguns-to-music-unreal-engine/frame_001.jpg
- [5:00] tutorials/frames/metasounds-in-ue5-from-miniguns-to-music-unreal-engine/frame_002.jpg
- [8:30] tutorials/frames/metasounds-in-ue5-from-miniguns-to-music-unreal-engine/frame_003.jpg
- [12:00] tutorials/frames/metasounds-in-ue5-from-miniguns-to-music-unreal-engine/frame_004.jpg
- [16:30] tutorials/frames/metasounds-in-ue5-from-miniguns-to-music-unreal-engine/frame_005.jpg
- [19:45] tutorials/frames/metasounds-in-ue5-from-miniguns-to-music-unreal-engine/frame_006.jpg
- [23:20] tutorials/frames/metasounds-in-ue5-from-miniguns-to-music-unreal-engine/frame_007.jpg

---

## Structured Notes

### Core Technique
MetaSounds graph-based procedural audio in UE5 Early Access — building a layered, triggerable minigun SFX rig (spin-up/loop/spin-down + randomized/pitch-varied overlapping gunfire) and, separately, fully procedural generative sci-fi music (square-wave oscillator driven by scale/note lookups, BPM-synced bar/beat/quaver triggers, envelope shaping, and a ladder filter) that reacts live to world events (touching pickups).

### Summary
Official Epic Games talk by Chris Murphy (technical artist) framing MetaSounds conceptually as "audio shaders" — node-graph audio synthesis analogous to material shader graphs. Part 1 builds a **Minigun** MetaSound: chain a Wave Player (On Play → spin-up "barrel wind start" sample) into a second looping Wave Player (On Finished → looping "barrel wind loop", Loop enabled) combined through a **Mixer**; add a **Pitch Shift** input and drive it over time with an **Envelope (ADSR Float)** node (multiplied/rescaled 0–1 to 0–2.5) so the spin-up pitch rises programmatically instead of via a hardcoded value; add custom graph **inputs** ("Spin Down"/"Spin Up" triggers) to play a spin-down stinger sample and stop the loop/mixer, and to restart the wind-up cleanly if fire resumes mid-spin-down. For the gunfire layer: a Wave Player firing one of 3 sample variants, driven by **Trigger Repeat** (configurable period, later expressed as a "Shots Per Minute" input converted to a repeat period) instead of raw On Play; randomize which sample plays via a **Random (Get) node reading an input array** ("Shot Array" of 3 wave assets) and randomize pitch via **Random Float** (range −0.5 to 2) into Pitch Shift; to allow overlapping/non-clipping shots, duplicate the whole play chain 3x gated by a **Trigger Counter + Trigger Compare (int32)** so shot 1/2/3 route to separate Wave Player instances mixed together, driven by "Start Fire"/"Stop Fire" graph inputs — then wire the whole MetaSound into the minigun's Blueprint by setting an Audio Component's Sound asset and calling the named trigger parameters via the Audio Component's Parameter Interface. Part 2 builds procedural **generative music**: a **Square** oscillator node driven by a frequency input; convert a random/derived note value into frequency via **Scale to Note Array** (Major/Minor scale degrees, Chord Tones Only toggle) → **MIDI Note Quantizer** → **MIDI To Frequency (Float)**; shape each note's amplitude with an **AD Envelope (Float)** (attack/decay durations expressed as fractions of a bar) multiplied into the Square's output, and drive note timing off a **BPM → Send Time (bar duration)** chain feeding parallel **Bar Trigger** / **Beat Trigger** (and later **Quaver Trigger**, an eighth-note subdivision) send/receive pairs so multiple layered elements can sync to the same tempo grid; broadcast the currently-playing note via a **Send/Receive "Current Note"** pair so other layers (e.g. a harmony line) can derive nearby chord tones by offsetting the current note by a random interval (3–8 semitones, chord-tones-only); add sci-fi character with a **Ladder Filter** whose cutoff frequency is itself modulated by another envelope (remapped via **Map Range**) triggered on its own bar-synced schedule; and demonstrate reactivity by broadcasting the ladder-filter/envelope value out as a Send so a separate **Pickup Sound** MetaSound (built by copying the note-generation subgraph and re-triggering it on Quaver instead of Bar/Beat) can layer extra procedurally-pitched notes on top of the music in real time whenever the player touches a world pickup actor — capped with a Trigger Counter comparing against a max quaver count (≤8) before a delayed Finish, so the extra layer doesn't play forever.

### Key Steps
1. **Minigun setup:** Content Browser → right-click → Sound → MetaSound (requires the MetaSounds plugin enabled) → build the spin-up/loop chain: Wave Player (On Play → spin-up sample) → On Finished drives a second looping Wave Player (Loop = true) → combine both through a **Mixer** node → route to the graph's Audio output.
2. Add a **Pitch Shift** float input on the loop's Wave Player; drive it from an **Envelope (ADSR Float)** node triggered by the first Wave Player's On Finished, remapped from its 0–1 output range to a wider range (e.g. multiply by 2.5) for a more pronounced spin-up pitch rise.
3. Add custom graph **Inputs** (right-click in the Inputs panel, set type to Trigger) named e.g. "Spin Down" and "Spin Up": Spin Down plays a stop/stinger sample and stops the loop Wave Player + Mixer; Spin Up re-triggers the wind-up chain and can also Release the envelope so re-firing mid-spin-down behaves correctly.
4. **Gunfire layer:** a separate Wave Player chain, gated by a **Trigger Repeat** node (Period input) — expose a "Shots Per Minute" input and convert it to a repeat period so fire rate is tunable/tempo-based.
5. Randomize which sample fires using a **Random (Get)** node reading from an input **Wave Asset array** ("Shot Array" populated with 3 fire samples); randomize each shot's pitch via a **Random Float** node (e.g. −0.5 to 2) plugged into a Pitch Shift on the fire Wave Player.
6. To let shots overlap without cutting each other off, add a **Trigger Counter** (counts fire triggers) feeding a **Trigger Compare (int32)** chain that routes shot 1 / shot 2 / shot 3 to three separate, duplicated Wave Player instances, mixed together via another Mixer — this avoids each new shot stopping the previous one's playback (as a single shared Wave Player would).
7. Expose "Start Fire" / "Stop Fire" Trigger inputs on the graph instead of driving everything from On Play, so the Blueprint side can start/stop firing on demand.
8. **Wire into gameplay:** in the minigun's Blueprint, assign the built MetaSound as the Sound asset on an Audio Component, then call each named trigger (Spin Up, Spin Down, Start Fire, Stop Fire) via the Audio Component's **Parameter Interface** node from gameplay events (e.g. input press/release).
9. **Procedural music setup:** new MetaSound ("Sci-Fi Music") using a **Square** oscillator node instead of any sample playback; feed it a frequency derived from **Scale to Note Array** (choose Major/Minor scale degrees, optional Chord Tones Only) → **MIDI Note Quantizer** → **MIDI To Frequency (Float)**, sourced initially from a **Random Float** note value (e.g. 60–72 MIDI range).
10. Shape each note's volume with an **AD Envelope (Float)** (Attack/Decay Time) multiplied into the Square oscillator's audio output so notes fade in/out instead of buzzing continuously.
11. Build a shared tempo grid: a **BPM** input → **BPM to Seconds** → a bar-duration Send/Receive pair ("Bar Time," Division of Whole Note = 1) and a matching Bar **Trigger** send/receive pair, then duplicate for **Beat Trigger**/**Beat Time** and later **Quaver Trigger** (an eighth-note subdivision) — express each envelope's Attack/Decay as fractions of the received bar/beat/quaver time (e.g. Attack = 0.33× bar, Decay = 0.66× bar) so timing stays tempo-relative.
12. Broadcast the currently-selected note via a **Send/Receive "Current Note"** pair so other layers can read it; derive a harmony/counter-melody note by subtracting a random interval (e.g. 3–8) from the current note with Chord Tones Only enabled on its own Scale to Note Array.
13. Add sci-fi texture with a **Ladder Filter** node; modulate its Cutoff Frequency from a second envelope remapped via **Map Range** (e.g. 200–2000), triggered on its own bar-synced schedule offset from the main note envelope (e.g. 0.25/0.75 timing) for variation.
14. Demonstrate world reactivity: broadcast the ladder-filter/envelope value out as a Send (not consumed locally) purely so a second MetaSound can read it; drop the finished "Sci-Fi Music" MetaSound into the level and confirm pickups in the scene visually "flare up" when touched (pre-built Blueprint logic).
15. Build a **Pickup Sound** MetaSound by copying the note-generation subgraph into a new asset, but re-trigger its envelope/note logic on **Quaver Trigger** (Receive) instead of Bar/Beat, so touching a pickup layers extra, faster procedurally-pitched notes on top of the ambient music; drive this from the pickup actor's Blueprint via an audio variable.
16. Prevent the pickup layer from playing forever: count incoming Quaver triggers with a **Trigger Counter**, compare against a max count (e.g. ≤8) to keep playing, otherwise Delay ~1 second and call Finish on the MetaSound.

### UE Systems / Blueprints / Settings
- **Asset type:** MetaSound (Content Browser → Sound → MetaSound; requires the MetaSounds plugin).
- **Core nodes used:** Wave Player, Mixer (Mono Mixer for a mono effect — stereo is possible via a stereo MetaSound), Pitch Shift, Envelope (ADSR Float / AD Envelope Float), Trigger Repeat, Trigger Counter, Trigger Compare (int32), Random (Get) on a Wave Asset array, Random Float, Square (oscillator), Scale to Note Array (Major/Minor scale, Chord Tones Only), MIDI Note Quantizer, MIDI To Frequency (Float), Ladder Filter (Cutoff Frequency, Resonance), Map Range (Float), BPM to Seconds, Send/Receive node pairs (used for Bar Time, Bar Trigger, Beat Time, Beat Trigger, Quaver Trigger, Current Note, and the ladder-filter value — all addressed by name and global within/across MetaSound graphs).
- **Custom graph Inputs created:** Spin Down, Spin Up, Start Fire, Stop Fire (Trigger type), Shots Per Minute, Shot Array (Wave Asset array), BPM (Float).
- **Blueprint side:** Audio Component (Sound asset assignment), Parameter Interface node (call named MetaSound trigger inputs from Blueprint events).
- **Concept framing:** MetaSounds described as "audio shaders" — a node-graph synthesis/DSP system analogous to material shader graphs, giving full control over audio rendering.

### Difficulty
Intermediate/Advanced — assumes basic UE Blueprint/node-graph familiarity; the minigun section is approachable, the procedural music section (tempo-synced Send/Receive networks, MIDI/scale quantization, cross-MetaSound communication) is more advanced sound-design/DSP territory.

### UE Version
UE5 Early Access build (MetaSounds debut) — noted explicitly in the intro as an Early Access feature at time of recording.

### Tags
metasounds, audio, blueprint, pipeline, intermediate, advanced, ue5-0

---

## Related Entries
- No other ingested unreal-sidekick tutorial currently covers MetaSounds — this and the companion beginner MetaSounds queue item (ingested in this same session) are the first coverage of `references/audio-metasounds.md`'s primary subject.
