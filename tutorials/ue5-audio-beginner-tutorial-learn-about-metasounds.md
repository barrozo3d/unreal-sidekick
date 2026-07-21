---
title: UE5 Audio Beginner Tutorial Learn About Metasounds!
source: YouTube
url: https://www.youtube.com/watch?v=0H7PiqIl0Io
author: Taken Grace
ingested: 2026-07-20
ue_version: "Not specified (UE5.x)"
tags: [metasounds, audio, blueprint, beginner]
extraction_status: complete
frames_dir: tutorials/frames/ue5-audio-beginner-tutorial-learn-about-metasounds/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# UE5 Audio Beginner Tutorial Learn About Metasounds!

**Source:** [YouTube](https://www.youtube.com/watch?v=0H7PiqIl0Io)
**Author:** Taken Grace
**Duration:** 25m20s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### How to Add Audio in Unreal Engine 5 [0:00]
**Transcript (timestamped):**
[0:00] I've been working with Sound for over 12 years.
[0:02] I was a boom operator and a sound assist in the film and television industry.
[0:05] I've done voiceovers, ADR, and podcasting.
[0:09] And today, I'm going to give you guys a crash course in audio in Unreal Engine 5.
[0:13] There's a couple of great tools in Unreal Engine 5 that can help get your soundscape to the next level.
[0:18] So in this video, we are going to be learning about metasounds.
[0:20] We're going to be learning about different types of audio and how to implement them into your game, including music.
[0:25] New to the channel, my name's TakenGrace and I make Unreal Engine tutorials and videos for you and me to become better game devs.
[0:31] You want to become a better game dev with me, subscribe to the channel, and join the Discord,
[0:35] with lots of great members on there that are willing to help you out with your project.
[0:39] Alright, let's get started on your audio.
[0:42] Alright, everybody, so to get started, we are going to learn about sounds in general.
[0:47] So I will go over some overview stuff.
[0:49] I will show you guys metasounds, which is very powerful in Unreal Engine 5.
[0:54] And obviously, I'm going to go over just a couple of basic sound things just so you know what they are.
[0:58] I'll talk about it later in the video, but I do have a link to Epidemic Sounds down in the description below.
[1:02] It will help you guys get some sound effects and some music, and it's a free trial, so nothing to lose there.
[1:07] I'll talk about that more later in the video. Let's get started here.
[1:10] Okay, so we're in the project for the first-person shooter series that we did that finished a couple of months ago.
[1:16] So there's no sound in this game because we didn't have any sounds available, and now that we have Epidemic Sounds, we can get some stuff.
[1:23] I also have a couple of sounds that I'm going to give you guys for free, also in the description down below there.
[1:28] So let's go into content. Let's make a new folder and call it audio.
[1:33] Okay, and I'm just going to drag these sounds in.
[1:36] And before we get started, I'm going to put on my headphones because I don't normally wear them when I record, but obviously audio is important, so we need to wear them now.


### Quickly Implement a 2D Sound in a Blueprint [1:43]
**Transcript (timestamped):**
[1:43] So we are going to do some sound stuff in here.
[1:47] So you can put sounds in basically anything in the game, right?
[1:50] So the first thing I'm going to show you is called a one-shot sound.
[1:53] So what a one-shot sound is, is it plays.
[1:56] Once it's finished playing, it stops and is removed immediately from memory.
[1:59] So it only plays once, okay, but it's called a one-shot sound.
[2:02] So we're going to do one of those inside of this guy.
[2:04] So this is our health pack.
[2:06] We're going to hit Ctrl E to open that health pack up.
[2:08] Okay, so we have this interact thing here.
[2:12] So when we interact with our health pack, we're checking to see if our player's health is full, if it is, we're not doing anything.
[2:18] If it isn't, we are destroying this actor and then we are gaining the health associated with this actor.
[2:22] Okay, so, so to be honest, actually, this should be on the other side of this.
[2:26] Pardon me.
[2:27] So yeah, destroy actors.
[2:28] The last thing you want to do before we connect this up, what we want to do is we want to get a play sound 2D.
[2:35] Okay, when you play sound 2D, it will play a sound and then it will.
[2:39] Once it's done playing, we're moving from memory.
[2:41] Okay, so that's how that works.
[2:43] So the sound we want is the bandage.
[2:46] Okay, so we're going to play that sound with a compile.
[2:49] So remember that there will be 2D and 3D sounds.
[2:52] Okay, so we're just focusing on 2D right now.
[2:53] 2D means that no matter where the player is, it's going to play the same sound at a specific volume in your headphones.
[2:59] Okay.
[3:00] Okay, we'll hit play here.
[3:02] We'll go and we will let's turn off the flash here.
[3:05] We'll interact with this and come on.
[3:07] Oh, you need to take some health damage.
[3:09] Sorry, there we go.
[3:10] There we go.
[3:11] And there's our sound.
[3:12] Okay, so our sound played in our headphones when we interact with that item.
[3:15] So that is a 2D sound.


### Intro to Meta Sounds [3:16]
**Transcript (timestamped):**
[3:16] Super easy.
[3:18] However, there is another thing in here in Unreal Engine 5 that is super powerful.
[3:23] That is actually new as of Unreal Engine 5 called MetaSounds.
[3:28] Okay, so I'm going to show you those in our audio folder here.
[3:30] So we will just make a new folder called MetaSounds.
[3:35] Okay, MetaSounds are very, very good at getting the exact kind of look that you're looking for.
[3:41] So you're going to right click and go to audio, MetaSounds source.
[3:45] We're going to open that up and we'll call this BP fire.
[3:48] Okay, we are going to just put a fire in the world here somewhere,
[3:51] which will be in our starter pack of some variety somewhere.
[3:56] There we go.
[3:57] Part of the effect fire.
[3:58] So we got a fire now.
[3:59] So what we can do is we can put a 3D sound into the world and we can have it affect basically.
[4:07] So if the player is over here, it's going to be much quieter than if we're right up against it.
[4:11] Right. So that's the benefit of having some 3D sounds.
[4:14] Okay, but 3D sounds will play at a location itself.
[4:17] So that we need to obviously tell it where it needs to be.
[4:20] But anyway, so what we're going to do is we're going to get rid of this.
[4:23] We will go into our where did it first or first person this one?
[4:27] There we go.
[4:28] So there's our audio folder MetaSounds.
[4:30] We're going to open up our fire MetaSound and I'm going to show you guys some stuff.
[4:35] Okay, so number one, you'll notice this looks pretty different than most of the other Blueprint stuff
[4:39] that you've dealt with before.
[4:40] The first thing you'll notice is there's no components up here.
[4:43] Okay, the next thing you'll notice is we have two outputs here and I'll explain how these work in a sec here.
[4:49] So mono, if you guys don't know, mono is obviously one channel of audio.
[4:54] It will play an identical sound in both the left and the right channel.
[4:57] Okay, stereo, if you come up to MetaSound up here, you can change it to stereo.
[5:02] Stereo plays two unique sounds in the left channel and the right channel.
[5:06] Okay, so this is how you can really kind of design your soundscape to be immersive with the player.
[5:13] Okay, so I like stereo personally.
[5:16] It just gives me more control over what I can do.
[5:19] So we're going to right click here and we're going to type in wave.
[5:22] What you need is a wave player and it's either going to be mono if it's a mono sound or stereo if it's a stereo sound.
[5:27] Okay, so then sorry, just for simplicity, we're just going to do mono on this.
[5:30] Pardon me.
[5:32] So we're going to do a mono wave player.
[5:35] Okay, so we'll plug out mono into out mono.
[5:39] If you don't have this plugged in, no sound is going to play.
[5:42] Okay, and then this treat this the same as a function essentially.
[5:46] So this will be your input.
[5:47] This is when we have triggered the sound to start playing.
[5:50] Okay, so we want to do obviously certain things.
[5:52] So we're going to want to play the sound.
[5:54] So the asset we're going to want here is the fire sound effect.
[5:58] This one here, the fire outside fireplace.
[6:00] Okay, okay, so what this is and the reason there's a warning here is because we have this set to be a one shot sound.
[6:07] Okay, so this will be here because it's expecting me to plug this in in order for it to do stuff and destroy this actor once it's finished playing.
[6:15] Okay, in this case, we want it to be a looping sound.
[6:18] So we'll click looping.
[6:19] This is still here though.
[6:20] So what you need to do to get rid of this and make this work is you need to come over where it says ue.source.oneShot and you need to delete this.
[6:28] Okay, that will get rid of that node.
[6:29] It will get rid of that warning.
[6:30] Now this is truly a looping sound.
[6:33] So first off, we need to go to source and this virtualization mode is very important.
[6:39] This is a this is an optimization thing where you tell the engine what you want to do when you're no longer in this attenuation of radius, which we'll actually talk about right now.


### What is Attenuation and Why you Need it [6:48]
**Transcript (timestamped):**
[6:48] So in order for 3D sounds to exist, you need attenuation.
[6:52] And what that is is it's generally a sphere that is telling Unreal Engine where the player is in relation to the sound and how basically it'll fade the volume in from zero to one based on where this player is.
[7:05] Okay, so we need to create one.
[7:06] So we'll come up to sound attenuation, create new assets, sound attenuation.
[7:11] We can put this in our first person audio.
[7:15] We'll just new folder attenuation.
[7:18] How do you spell it?
[7:19] I spelled it right already?
[7:21] Yeah, the UAC.
[7:22] There we go.
[7:23] So we'll open that up and we'll call this fire attend.
[7:27] So we've created that now.
[7:31] You can open the attenuation and you can edit all of these different settings in here.
[7:35] This will you can really customize the sound here.
[7:38] We're not going to get into that into this video here, but you can do stuff like air absorption absorption.
[7:43] So for example, higher wave frequencies don't travel as far as lower end frequencies.
[7:49] So this is saying air absorption, basically how long until the lower end frequencies start to kind of disappear and then the sound actually changes.
[7:59] Okay, so that's like a real life thing, right?
[8:01] So that's what that would be.
[8:03] You can do panning.
[8:05] You can do omnidirectional, direct, surround, whatever.
[8:08] You can do all sorts of different settings in here for this attenuation.
[8:12] But for now, we can just leave it as default just for the sake of this tutorial here.
[8:18] Okay, so now that we have that set.
[8:20] So when we enter the attenuation, do we want to restart the sound or do we want to continue to play it after we have left the attenuation sphere, which is obviously not great for for optimization, or you can just disable it, right?
[8:32] So restart for looping is the best because when you leave the attenuation, it's going to stop it.
[8:37] It's going to remove it from memory.
[8:38] And then when you enter the attenuation radius again, it's going to restart it.
[8:42] Okay, so that is the most optimal way of doing it.
[8:45] Okay, so we told to loop.
[8:47] We've set our attenuation settings and we've plugged all this in.
[8:50] We actually need to call this event now or drag it into the world.
[8:53] Okay, so we are going to go into our world now and we are going to drag in our fire sound.
[9:01] Right there.
[9:03] And you want this to be relatively, you know, accurate in terms of placement because it's going to be a 3D sound, right?
[9:08] So now you can see that we have these giant spheres.
[9:12] So the inner circle is it playing at full volume?
[9:15] Okay, the outer circle is the attenuation radius in regards to where it's going to start fading it down to zero.
[9:21] Once you're outside the sphere, it's zero.
[9:23] It's done. The sound is removed from memory.
[9:25] Once you're inside, it's going to start fading it up from zero to one.
[9:27] Okay, one is obviously full volume and zero is no volume.
[9:30] Okay, so what we can do here is I believe we can adjust the attenuation radius.
[9:35] Or you might have to edit it in the actual thing here.
[9:38] You do.
[9:39] Okay, so the inner radius and the outer radius are falloff distance.
[9:41] So let's just make this just for the sake of, you know, the tutorial like, you know, a thousand.
[9:46] Okay, and we'll save that.


### Showcasing our 3D Fire SFX in our World [9:47]
**Transcript (timestamped):**
[9:48] And that's much better. That'll kind of prove our point here.
[9:51] So now we're going to hit play.
[9:52] There's our fire playing. We can't hear anything because we're not inside the radius.
[9:55] But once we enter it, you can now hear the fire in your headphones actually start in the closer we get.
[10:03] The louder guess. Okay, so that is a 3D sound.
[10:06] And that is how meta sounds work.
[10:08] Okay, so there's lots of really cool stuff you could do with meta sounds.
[10:12] First off, you can basically create a bunch of different sounds to play.
[10:18] Okay, so for example, we will close this and we will close this.


### How to Create a bunch of sounds and get a Random one [10:22]
**Transcript (timestamped):**
[10:23] We'll make a new meta sound.
[10:25] Okay.
[10:27] Audio meta sound source, we're going to call this.
[10:30] Oh, I called it BP fire because that's just what I did.
[10:33] Sorry, we don't want BP fire.
[10:34] We want MS fire meta sound and MS underscore AK 47 fire.
[10:42] Okay, so we'll make a new sound here.
[10:44] We'll open that up.
[10:46] We will these will be one shots.
[10:48] Okay, so we are going to get a another wave player mono.
[10:53] We're going to play on this and then on finish, we're going to plug in here.
[10:58] So that once the sound is finished playing, it's going to destroy this or remove this sound from memory.
[11:03] And then we will add it again if we need it.
[11:05] So out mono, we are going to plug in.
[11:08] All right, so what we're going to do now is we have three sound effects in for our firing.
[11:13] So it's different every single time.
[11:14] So we're going to drag out of here and we're going to just type array and we want to random get array.
[11:20] Okay, so this is going to make a new node.
[11:22] Okay, so once we've gotten this one here and we've plugged it into the value, we are going to right click in array and we're going to promote to graph variable.
[11:29] Okay, so now we've created an array.
[11:32] We'll call this fire sounds.
[11:35] Okay, right down here is the default value.
[11:38] We're just going to add three and then we're going to plug in our we'll go to our audio sounds.
[11:42] Where are they?
[11:43] Here's our gunshots will perfect.
[11:45] So there's our three shots all different, right?
[11:47] So so now it's going to pull a random sound out of this and it's going to plug it in here and every time we play this, it's going to get one of those three sounds.
[11:54] Okay, weights, if you want to play around with that, that'll just determine which sounds played more than often or more than others.
[12:00] Okay, and then you can return the index of the one that's played and all that kind of stuff.
[12:04] So, Kate, if we hit play, you'll notice that it's immediately going on to on finish and I believe that's because we don't have attenuation.
[12:10] Yes, it is.
[12:11] So we are going to make a new attenuation and we'll call this AK 47 firing.
[12:19] Okay, we'll hit save.
[12:22] Let play.
[12:23] And it's still not exporting a sound.
[12:25] Why would that be?
[12:26] All right, so the one thing I forgot to actually do sorry is we need to plug this into next and then on next we plug it into place.
[12:34] So we're going to get the next sound and we're going to play that in.
[12:38] Okay, so Chesed out here by coming up here and pushing play.
[12:41] So you can notice that we don't sound and if you think that that's not loud enough, that's fine.
[12:47] We'll click on I believe it's on metasound or is it source?
[12:51] Okay, so generally you want volume between zero, which is nothing and one which is full volume.
[12:56] You can go above this.
[12:58] Generally you shouldn't.
[13:01] But I mean if you have to you have to so we'll just put it at two just to see what it does.
[13:06] So it's got a bit more punch to it now.
[13:09] Okay, so we're going to go with that.
[13:11] So we're going to close this metasound now we are going to open up.
[13:15] So what you could do we'll do in this video, but what you could do is in your data folder.
[13:20] We have our weapon data asset that has all of our guns data asset stuff in here.
[13:25] So what you could do is maybe make another data asset primary one and then make it all of your audio stuff.
[13:30] So firing, reloading, rechambering, you know, anything to do with that weapon that it's all to do with audio right.
[13:37] You can make that a separate primary data asset and then make one for each individual weapon set all of the different sounds that you want.
[13:42] And then you just have to implement that in your weapon class or your weapon parent, which we have right here.
[13:48] Okay, so I'm going to open my weapon class because we have a couple spots in here.
[13:54] I think specifically, so I have right here in my weapon class in my single fire graph to add recoil radical and gunshots.
[14:01] So the gunshot we can probably put right at the end here.
[14:04] So what we're going to do is we're going to play sound 2D.
[14:07] This is also going to be a 2D sound and then we're going to select the better sound we made, which was AK fire.
[14:13] Okay, so it's going to play that meta sound now.
[14:15] So we will just do the single fire, but you could obviously implement that into your auto fire graph as well.
[14:22] AK fire source. Perfect.
[14:24] All right, so we'll even want those.
[14:26] Now we'll test it out and we'll see what it sounds like.
[14:28] So we'll first off, well, I guess it doesn't matter which gun we use, but because it's going to play the same sound, but there.
[14:35] So it's playing the same sound and they're playing different sounds every single time.
[14:41] I'm just going to kill these guys. I can pick up his weapon.
[14:46] And okay, so there's this weapon. We're on automatic mode now.
[14:56] So it doesn't sound great. You have to refine it a little bit, obviously, but yeah, so that's essentially what how you do sounds for weapons, right?


### Playing Sounds at locations [15:00]
**Transcript (timestamped):**
[15:04] You just create a meta sound.
[15:05] So all right, so let's focus more on 3D sounds now.
[15:08] So we're going to make another meta sound and it's going to be a explosion one.
[15:12] Meta sound underscore explosion.
[15:15] Okay, we'll open that up here.
[15:16] This will be a 3D sound. It's going to be a one shot.
[15:19] So we are only going to drag it here and we will get the wave.
[15:22] We'll get the wave mono on finished and plug that all in.
[15:28] We do need attenuation settings.
[15:30] So we'll go to our source, make a new one, call it explosion.
[15:36] Okay, let's select our the explosion that I put in there.
[15:40] Okay, so we got this explosion.
[15:41] We'll put this explosion in here, drag it in there.
[15:44] Boom.
[15:45] Okay, so this is done.
[15:46] We got the attenuation.
[15:47] It's set to restart and all that kind of stuff.
[15:50] So we're going to play now we're going to go into our, I have a projectile base in this particular project.
[15:58] So we'll go to projectiles projectile base.
[16:00] We will have to do this.
[16:02] We'll have to add a variable and we'll call this sound impact sound.
[16:07] Make sure that that will be a, I think it's a meta sound, right?
[16:11] Sound wave is sound.
[16:13] It might be sound wave.
[16:14] I'm just going to compile the blueprint and make sure that is the one.
[16:17] So Ms.
[16:19] Okay, it is the one.
[16:20] So sound wave is what you want.
[16:22] We are going to make this not instance editable, but now all of the projectiles you have.
[16:27] So I have this rocket projectile and this grenade and this bullet.
[16:29] So you can put different sounds in based on which ones you have.
[16:33] So the bullet one, we don't have anything right now.
[16:35] So, but for the grenade, well, we go to class defaults and we'll now set this impact sound to Ms. Explosion.
[16:42] So this one is a little bit different because we're going to do off explosion that are off explode.
[16:47] We are going to play this sound.
[16:49] So we are going to play a sort of spawn sound at location.
[16:56] Okay.
[16:57] And the location we're just going to get basically wherever we are.
[17:00] So we'll get the actually, sorry, get world location.
[17:03] We already got it here.
[17:04] So we will drag this over and we'll plug this in.
[17:06] And then the sound will be our, we'll get impact sound and we'll plug this in.
[17:13] Okay.
[17:14] All right.
[17:15] So for the grenade, obviously it's a little bit different, but for the projectile base,
[17:17] everything else is the same on component hit.
[17:20] When we hit something, we are going to obviously play a sound at location as well.
[17:25] So play sound at location or spawn sound, pardon me, at location, because it's a 3D sound.
[17:31] We're spawning it into the world and we are going to plug in the impact points.
[17:36] So sorry, this actually should only work.
[17:40] This should be up here and then this should plug in here.
[17:43] Sorry, this is for those following the series just because we don't want to play a sound if we don't hit anything.
[17:48] Right.
[17:49] So we're going to hit compile.
[17:50] We're going to test this out.
[17:51] So we're going to play.
[17:52] I got the rocket launcher right here.
[17:53] I'm going to play it.
[17:54] Didn't make sound.
[17:56] Is it because we're too far away?
[17:59] Interesting that it didn't play sound.
[18:01] Let's have a look.
[18:02] Oh, I didn't plug it in.
[18:03] Sorry.
[18:04] Look at that.
[18:05] Impact sound.
[18:06] Did I, oh, you know what?
[18:07] Did I not set it in the rocket projectile?
[18:08] That is what we didn't do.
[18:09] So we didn't do that.
[18:10] The impact sound here will be MS explosion.
[18:14] Okay.
[18:15] For the love of God, this will work.
[18:20] So we'll do a little quiet for an explosion, to be honest.
[18:23] So perhaps we make that slightly louder.
[18:26] Maybe we'll do like three.
[18:30] That seems relatively appropriate.
[18:32] This, obviously that explosion sound of rock probably could be better, but.
[18:37] Okay.
[18:38] So now we'll shoot it again, but way over here.
[18:42] Okay.
[18:43] So it didn't play the particle effect because we called it to be, I think 2000 or something.
[18:47] So obviously that's not enough.
[18:49] I don't know how to fix that, but yeah, so it played in the distance.


### How to Build your Sound Library with Epidemic Sound [18:52]
**Transcript (timestamped):**
[18:52] So.
[18:53] Okay.
[18:54] So I know it's really hard to find good sound effects and music for your commercial projects.
[18:58] So now I'm going to tell you about Epidemic Sound.
[19:01] Epidemic Sound is royalty free music and sound effects with over 40,000 tracks and 90,000 sound effects.
[19:07] You can use Epidemic Sound without worrying about licensing and publish anywhere online.
[19:12] You can also upload a song and search by emotion or mood so that you can have all of your music be consistent across your project.
[19:18] It's never been easier to get free high quality sound effects and music with my link in the description below.
[19:23] You get a 30 day free trial for Epidemic Sound.
[19:26] If you decide to sign up for a subscription after the free trial ends, you'll be directly supporting the channel.
[19:31] So check them out.
[19:32] Epidemic Sound.
[19:33] I'm going to get back to editing the video.


### How to Add Music into your Game [19:36]
**Transcript (timestamped):**
[19:36] Okay.
[19:37] So you're probably wondering how you would tackle music.
[19:39] So what you can do for music is I would actually make a music manager.
[19:43] So in audio, I would make a new blueprint class, which will be an actor type and we'll call it BP Music Manager.
[19:52] Okay, let's open that up.
[19:54] Okay, so for this, I think what we'll do is we will add an audio components to this.
[20:02] Okay, there would probably need to be something in the level for you to pull what song you're supposed to have with or whatever the case is, right?
[20:12] So but anyways, we'll have the audio.
[20:14] We're going to go into the event graph on event begin play.
[20:17] We are going to play.
[20:19] We'll just do this just to show you guys how to get audio in your game.
[20:22] Okay, so we will set audio or set sound.
[20:27] Sorry.
[20:28] Okay, the new system.
[20:30] Okay, the new sound is going to be, you know, whatever one you want.
[20:34] So we'll do portal to life to start.
[20:36] Okay, and so we'll set that sound and then we are going to play sound to D or sorry.
[20:44] Yeah, play.
[20:46] Pardon me is all we need.
[20:47] So we're going to play and we're going to fade this in.
[20:50] Okay, so we're going to get the audio.
[20:51] We're going to get a fade in audio.
[20:55] Okay, fade in duration.
[20:56] Let's say like, you know, three seconds.
[20:59] Okay, so we'll fade it in.
[21:02] I believe does that play it?
[21:04] This function allows us our designers to call play on audio component instance while applying a volume curve over time.
[21:09] Okay, so we don't need to play one.
[21:11] So this just fades it in and it starts to play.
[21:12] Okay, we are going to add a, well, obviously this needs to be in the world.
[21:18] So we're going to put our music manager in the world somewhere over here.
[21:21] Okay, let's say we, you know, enter a trigger here.
[21:26] So let's make a music trigger box.
[21:28] We'll make another blueprint class.
[21:30] We'll do an actor type.
[21:32] We'll call this BP music trigger box.
[21:39] Okay, so we have made a trigger box.
[21:42] We're going to add a box collision.
[21:47] Okay, and that is just going to be, you know, whatever size it is.
[21:50] Let's just in the construction script, just quickly, you know, set box extent, promote this to a very high level.
[21:55] Promote this to a variable.
[21:57] In box extent, we'll make that instance editable so that we can edit how big this box is in the world.
[22:02] And then we are going to make another one and we're going to call it music to play.
[22:07] Okay, and we'll make that a sound, what do we call it earlier sound wave object reference.
[22:16] Okay, we'll make that instance editable as well so we can set our music and sound to play.
[22:20] Okay, so let's put that in the world now.
[22:22] So this is where we're starting.
[22:24] We're going to put this trigger box over here and we'll make the trigger box, we'll say 500 by 500 by 50.
[22:35] Okay, so I'll make it a bit taller, maybe 100 or 1000.
[22:42] Okay, so there's our music trigger box.
[22:44] When we enter this music trigger box, we are going to play a different song.
[22:47] So we played portal to life and this one we'll play is what's the other music when I had wind farm.
[22:55] Okay, so we'll play that and then so we'll go back into our event graph here and let's create, actually let's go back into our music manager.
[23:04] Let's create an event here to fade out the current song.
[23:09] Okay, so we'll do a custom event and we'll do fade out current song.
[23:17] Okay, so we'll fade that out and then we will get our audio.
[23:22] Oh, and sorry, let's change just the change track instead and we'll make an input there of a sound base.
[23:33] Yes, no, not sound base, just we'll just say music and we'll change this to sound.
[23:41] I can't ever remember what it's called wave.
[23:44] Okay, so make an input there, it will compile.
[23:46] Now what we'll do is we'll take our audio and we'll fade out.
[23:53] Okay, fade out duration, we'll do like four seconds.
[23:56] That's too long, let's see two seconds.
[23:58] Okay, and after we've faded out what we want to do is we'll do a delay.
[24:07] So yeah, maybe after it fades out, we'll just add a delay here, I just want to see if we can get this working here.
[24:12] So we'll add a delay for our fade out time, get our audio, we will set the sound and then I hit audio, sorry, is that not working?
[24:20] Oh yeah, music.
[24:21] And we'll do new sound, we'll plug this in.
[24:25] And then we will do fade in, we'll see if this works.
[24:32] Because when it plays a sound, it should work, but we'll see.
[24:39] Fades out.
[24:45] The other one does not fade in.
[24:47] What you can do actually is you can hit, oh it did fade in, it's just delayed as hell.
[24:52] Hopefully this video was helpful, if you guys want me to do a follow up video on designing sound, let me know in the comments down below.
[24:58] Don't forget to like and hike the video.
[25:01] If you want to keep learning in Unreal Engine with some great tutorials, you can check out those videos right there.
[25:05] Special thanks to my Rua Coffee Members, if you do want to become a coffee member and get access to these great perks, the data in the description below is a link to my coffee page.
[25:13] Check it out, see if what works for you.
[25:14] But until then, keep learning till you game over. Peace.



---

## Captured Frames

- [2:00] tutorials/frames/ue5-audio-beginner-tutorial-learn-about-metasounds/frame_000.jpg
- [5:30] tutorials/frames/ue5-audio-beginner-tutorial-learn-about-metasounds/frame_001.jpg
- [7:10] tutorials/frames/ue5-audio-beginner-tutorial-learn-about-metasounds/frame_002.jpg
- [9:55] tutorials/frames/ue5-audio-beginner-tutorial-learn-about-metasounds/frame_003.jpg
- [11:20] tutorials/frames/ue5-audio-beginner-tutorial-learn-about-metasounds/frame_004.jpg
- [16:00] tutorials/frames/ue5-audio-beginner-tutorial-learn-about-metasounds/frame_005.jpg
- [17:35] tutorials/frames/ue5-audio-beginner-tutorial-learn-about-metasounds/frame_006.jpg
- [21:00] tutorials/frames/ue5-audio-beginner-tutorial-learn-about-metasounds/frame_007.jpg

---

## Structured Notes

### Core Technique
Beginner-level tour of UE5 audio fundamentals applied to a first-person shooter project: 2D one-shot Blueprint sounds, MetaSounds (mono vs. stereo, looping 3D fire ambience, sound attenuation), randomized weapon-fire MetaSounds via Random Get Array, 3D "spawn sound at location" for explosions/impacts, and a simple fade-in/fade-out music manager with trigger-box-driven track changes.

### Summary
TakenGrace's crash-course (25m20s) on adding audio to an existing FPS project. Starts with the simplest case — a **Play Sound 2D** node called from a health pack's Blueprint interact event (2D = plays at a fixed volume regardless of player position; a "one-shot" sound is automatically removed from memory once finished). Introduces **MetaSounds** (Content Browser → Audio → MetaSound Source) as the more powerful alternative to plain Sound Cues: explains Mono vs. Stereo output pins (Stereo can be selected via the MetaSound's asset settings for two independent channels), building a looping 3D fire-ambience MetaSound with a **Wave Player (Mono)** node — deleting the default `UE.Source.OneShot` interface node and enabling **Looping** on the Wave Player converts it from a one-shot to an ambient loop; covers **Virtualization Mode** on the Source settings (governs what happens when the sound leaves its attenuation range) and walks through creating a **Sound Attenuation** asset (Content Browser → Sound Attenuation) — explaining the attenuation sphere concept (inner radius = full volume, falloff to the outer radius = silence), Air Absorption (simulates high frequencies attenuating faster over distance), panning modes, and the "restart on re-enter vs. continue vs. disable" setting for when a looping sound re-enters its attenuation volume (Restart recommended for optimization — it fully unloads outside the sphere). Demonstrates dragging the finished fire MetaSound into the level and tuning the attenuation radius (visualized as concentric spheres in the viewport) to hear real-time distance-based volume falloff in PIE. Builds a **randomized weapon-fire MetaSound**: a one-shot Wave Player whose asset input is fed by a **Random Get Array** node (right-click → Array → Random Get Array), with the array promoted to a graph variable ("Fire Sounds") populated with 3 different gunshot samples so each shot plays a different sample — notes the array node also exposes optional per-entry Weights and an index-out for advanced use; also needs its own Sound Attenuation asset and the **Next → Play** trigger wiring (a common early mistake shown live: forgetting to chain On Play → Get Next → Play, which silently produces no sound), plus a note that MetaSound Source volume is normally kept in the 0–1 range but can be pushed above 1 for extra punch if needed. Shows implementing this MetaSound via a plain **Play Sound 2D** call inside a weapon Blueprint's fire graph, and suggests organizing per-weapon audio (firing/reloading/rechambering) as a dedicated Primary Data Asset referenced by each weapon class. Covers 3D "spawn sound at location" for a one-shot explosion MetaSound: exposing an `Impact Sound` (Sound Wave/MetaSound reference) variable on a shared Projectile Base class, set per-subclass (e.g. only the grenade projectile gets the explosion MetaSound assigned in Class Defaults), and calling **Spawn Sound at Location** on both the explicit "OnExplode" event and the generic On Component Hit event, passing the hit/impact world location. Also briefly promotes Epidemic Sound as a royalty-free SFX/music library option (sponsor segment). Finishes with a simple **Music Manager** actor: an Audio Component set/played on Begin Play via **Fade In Audio** (duration in seconds instead of an instant Play), plus a custom **Fade Out Current Song** event (Fade Out → Delay for the fade duration → Set Sound to the new track → Fade In again) exposed with a `Music` (Sound Wave) input parameter, triggered by a separate **Music Trigger Box** actor (Box Collision sized in the construction script, with an instance-editable `Music to Play` sound reference) placed in the level to swap tracks when the player enters a new area.

### Key Steps
1. **2D one-shot sound:** in any actor Blueprint's event graph, call **Play Sound 2D** with a Sound Wave/Cue asset — plays at a flat volume regardless of player position and is automatically freed from memory once finished.
2. **Basic looping 3D MetaSound:** Content Browser → Audio → MetaSound Source → add a **Wave Player (Mono)** node, wire its `Out Mono` to the graph's Audio output (`Out Mono`), assign the source Wave Asset, delete the default `UE.Source.OneShot` interface node, and enable **Looping** on the Wave Player to make it a persistent ambient loop instead of a one-shot.
3. Check **Virtualization Mode** in the MetaSound's Source settings — controls what happens to the sound when it's outside its attenuation range (an optimization setting).
4. Create a **Sound Attenuation** asset (Content Browser → Sound Attenuation) and assign it on the MetaSound's Attenuation Settings; key settings: inner radius (full volume) vs. outer/falloff radius (fades to silence), Air Absorption (simulates high-frequency loss over distance), panning mode, and the re-entry behavior for looping sounds (Restart recommended — fully unloads outside the sphere, reloads/restarts on re-entry, most memory-efficient).
5. Drag the finished MetaSound into the level as a 3D sound actor; the viewport shows two concentric attenuation spheres (inner = full volume, outer = falloff boundary) — adjust the attenuation asset's inner/outer radius values to tune audible range, then verify by walking toward/away from it in PIE.
6. **Randomized one-shot MetaSound (weapon fire):** Wave Player (Mono, one-shot — On Finished wired to the graph's Finished output so it's freed from memory after playing) whose Wave Asset input is driven by a **Random Get Array** node; promote the array to a graph variable (e.g. "Fire Sounds"), populate it with multiple sample variants (e.g. 3 gunshot takes) so each play picks a different one — remember to wire `On Play` → the array node's `Next` execution pin → `Play` (a commonly-missed step that otherwise produces silent playback); assign a dedicated Sound Attenuation asset; adjust MetaSound Source volume (normally 0–1, can exceed 1 for extra punch).
7. Call the randomized weapon MetaSound from a weapon Blueprint's fire graph via **Play Sound 2D**; consider organizing per-weapon audio (fire/reload/rechamber) as a dedicated audio Primary Data Asset referenced by each weapon subclass.
8. **3D impact/explosion sound:** build a one-shot 3D MetaSound (Wave Player + attenuation asset) and expose an `Impact Sound` variable (Sound Wave/MetaSound reference, not-instance-editable on the base class) on a shared Projectile Base Blueprint; assign the specific sound per-subclass in Class Defaults (e.g. only the grenade gets the explosion sound).
9. Trigger 3D impact audio with **Spawn Sound at Location**, passing the relevant world location (explicit explosion event → actor's own location; generic On Component Hit → the hit impact point) — guard the hit-event call so it only plays when something was actually hit.
10. **Music Manager:** create an Actor Blueprint with an Audio Component; on Begin Play, Set Sound to a starting track and call **Fade In Audio** (with a duration, e.g. 3 seconds) instead of a plain Play for a smooth start.
11. Add a custom **Fade Out Current Song** event exposing a `Music` (Sound Wave) input: Fade Out the current track (e.g. 2 seconds) → Delay for that same duration → Set Sound to the new track → Fade In again.
12. Build a **Music Trigger Box** actor (Box Collision sized via the construction script with an instance-editable extent, plus an instance-editable `Music to Play` sound reference); on overlap, call the Music Manager's Fade Out Current Song / track-change logic to transition tracks as the player moves between level areas.

### UE Systems / Blueprints / Settings
- **Blueprint audio nodes:** Play Sound 2D, Spawn Sound at Location, Fade In Audio, Fade Out (Audio Component), Set Sound (Audio Component).
- **MetaSound nodes/settings:** Wave Player (Mono/Stereo), `UE.Source.OneShot` interface node (delete to make a Wave Player loop-capable), Looping toggle, Virtualization Mode, Random Get Array (with optional per-entry Weights and index output), MetaSound Source volume (0–1 typical range, can exceed 1).
- **Assets:** MetaSound Source (Mono or Stereo), Sound Attenuation (inner/outer radius, Air Absorption, panning mode, re-entry behavior: Restart/Continue/Disable), Primary Data Asset (suggested pattern for per-weapon audio sets).
- **Actors built:** Music Manager (Audio Component, Fade In/Out logic), Music Trigger Box (Box Collision, instance-editable extent + music reference).
- **Sourcing content:** Epidemic Sound (royalty-free SFX/music library, sponsor mention — 40,000+ tracks, 90,000+ SFX, 30-day free trial).

### Difficulty
Beginner — explicitly framed as a "crash course"; no MetaSound DSP/synthesis techniques (compare to the companion "MetaSounds: From Miniguns to Music" video for procedural/generative audio).

### UE Version
Not explicitly stated (recent UE5.x FPS project).

### Tags
metasounds, audio, blueprint, beginner

---

## Related Entries
- `tutorials/metasounds-in-ue5-from-miniguns-to-music-unreal-engine.md` — the advanced companion covering procedural/generative MetaSounds synthesis (oscillators, envelopes, tempo-synced triggers) beyond this video's sample-playback-only scope; shares tags: metasounds, audio, blueprint.
