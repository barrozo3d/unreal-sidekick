---
title: 🥊Beat Yourself up with Unreal! RAGDOLL Physics for Filmmaking made Easy (or Hard) in UE5.6!🥊
source: YouTube
url: https://www.youtube.com/watch?v=ye0gjAx50oU
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in/
frame_count: 21
---

# 🥊Beat Yourself up with Unreal! RAGDOLL Physics for Filmmaking made Easy (or Hard) in UE5.6!🥊

**Source:** [YouTube](https://www.youtube.com/watch?v=ye0gjAx50oU)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 62m43s | 21 section(s)

---

## Raw Data (for Claude Code extraction)


### How to beat yourself up with Unreal Engine physics [0:00]
**Transcript:** So in this video, in this video, I'm going to show you how I do it.  So in this video, I'm going to show you how I do Ragdoll.  Okay, I'm fine. Nothing to see here. I meant to do that.

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_000.jpg

### The two methods I use for ragdoll [0:22]
**Transcript:** Okay, so in this video, I'm going to show you how I do my Ragdoll animation.  Now it's quite complicated, so I give you two methods to do this.  Now the first method is the simplest way, and that is to use Unreal's third person character, Manny,  because he's got a brilliant physics asset already built in.  And then you can animate that character, apply your Ragdoll, and then retarget that animation onto your custom FBX, and then you're done.  Now the second way of doing it is for the purest out there, and that is when you take your digital double,  and then you set it all up for your physics asset, and it's a little bit more complex, and so I've left that to the end.  So let's get on with the fun part first.

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_001.jpg

### What are ragdoll and physics assets? [1:08]
**Transcript:** So I've opened up Unreal 5.61 with a blank project, and into that I've added the third person template.  So if you hit add, add feature content pack, add third person template, add project, and the reason why is because in here, if you go to characters, meshes,  and there's a skeletal mesh Manny, and Quinn, I'm going to drag him into my viewport.  And the great thing about this character is he's already got an amazing physics asset already sort of worked out for him,  because it takes a while to kind of set up all those things.  So I just wanted to kind of have fun, and this is like the quickest way of doing it, is that you use this character,  and then you retarget your custom character onto this, and that way you use all the animation from this,  and so you have to set up all of those physics assets.  But at the end of the video, in the section 2, I will go over how to do it from scratch.  It's just a bit boring, so I wanted to get on with the fun part.  So using this character, if we go into our main window here, and we hit simulate, press this button here,  this is basically what happens when you're using the movie render queue, or you're actually playing a game,  is that Unrea...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_002.jpg

### METHOD 1 - Create a sequencer and add animation [4:48]
**Transcript:** So here we have our character, and we're going to create a sequencer and put some animation on him.  So right mouse button level sequence, and I call them LS underscore, and then we'll call this raggy, raggy.  And now I'm going to save the level as well, because I haven't saved this level yet.  So I'm just going to go file, save current level as, and then I'm going to put it into that ragdoll test.  And I'm going to call it P for persistent level, and then raggy.  Okay, so now we've got our level, and now we've got our level sequence.  And at the moment it's blank, so I'm going to first thing I'm going to do is set my time rate, my playback rate to 24 frames per second,  because I'm doing motion pictures.  And now we've got our character, and we've got a sequencer, so I'm going to drag the character into here.  So it defaults to adding the control rig, which is fantastic.  So you can grab bits, so you can move things, and you've got inverse kinematics, and all sorts of stuff.  But for now, what I'm going to do is delete the control rig.  You can add this back later, and we're going to add it as a lead control rig.  Ooh, that's your hook for later on.  Okay, so I'm just going to sel...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_003.jpg

### Keyframe simulation on or off [7:22]
**Transcript:** And then what we'll do is we'll have physics turn on during the simulation.  So it'll calculate all of the inertia, and all those things this character has.  So what I'm going to do is you go into a character, and then you see you've got simulate physics, and then you hit a keyframe here,  and then if when I hit that, you watch in here, it'll add it into the sequencer.  So there we go, so rather than having to navigate and find skeletal mesh component simulate physics, it'll just add it by saving a keyframe.  So now it's going to be permanently on when we press simulate.  So now it's going to just turn on, but it's on right from the beginning before we even moved him to that position.  So what you need to do is have it off to begin with.  So let's just turn it off here.  So now when I press play, you see it's not going to work until it's turned on here in the sequencer.  So if I go back with a frame, it's using that last keyframe, it's all animation, and at this point physics comes on.  And the nice thing is it's smart enough to know the inertia of the animation.  So if I hit play now, so I'm in simulate mode, and I hit play, it should go forward, and it's taking all of that weight...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_004.jpg

### Adding objects to collide with [9:18]
**Transcript:** So we just scale him down, and then rather than having to place him like that, because I've got step mode on, I'm going to turn those off.  And that's those are the things to lock. If you just hit end, it'll land on the nearer surface, like that.  So if you're going to blow over there, bronch, like that.  Okay, so I'm going to add him here, actually, let's make him a bit taller. So it'd be more exciting to when it falls over.  Fun we have on a hit end. There we go.  Okay, so now he looks like he'll collide with this, like that.  So at the moment, if I was just to go into simulate mode, you see this doesn't do anything, because it's not got physics turned on.  So if I was to hit play here, and then he'll turn his physics on, but he's actually working as a collision object, so that's good.  Stop play mode, I'm just going to move him a bit closer, so that he's going to bump into him.  Okay, now I'm going to turn on simulate mode, and then hit play, and then he's going to go, ow, poor fella.  See how to beat people up for fun.  Oh, that's not nice.  All right.  Okay, so I'm stopping the simulation, and I'm going to select my object, there's my cylinder, and then if I go to physics, I'm...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_005.jpg

### Weird thing with simulating animated meshes [11:47]
**Transcript:** A little side note, I found a weird thing with animating a static mesh in sequence that for simulation, and that is, normally what would happen is we'd go to the frame just before our simulation,  and then we'd select our model, save a key in the simulate physics, and then we'd go to our start frame, and then save another key so that it turns off.  So there's no simulation, and then simulation would happen here. But if we press simulate and then press play, you can see you get weirdness.  And that is because the transform is kind of competing with the simulation, and it doesn't do that with the manny, but it does it with static meshes.  So I don't know why, but the solution is to go to the frame before your simulation, right mouse button on this track, and then go to edit, trim selection, right, and that will delete any animation after that.  And then, right mouse button, properties, when finished, you keep state. So that'll mean that it's going to set this object to this position, then after that, it's just going to keep it hanging there until the simulation starts.  So now, we've got simulation going, press play, and there it is. It took me ages to work out.  All right, back to t...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_006.jpg

### How to use the Take Recorder to bake simulations [13:15]
**Transcript:** Okay, and so to do that, we use the take recorder. So to find your take recorder, you go to window, cinematics, and take recorder, and then you dock that with your window here.  And then the important thing is you need to add the things that you want to record. So we hit source, and we say from actor, and then we're going to hit the money simple.  So that's added it to into the take recorder, then we're going to add from actor, or cylinder, if you want to recall both of those.  Now, we also need it to add in our sequence. So you have to go to source, and then level sequence, and then select level sequence, and then you have to level sequence to trigger, and it's saying zero at the moment.  So again, you need to add the actual level sequence here. So there it is. So now it'll play this level sequence, and it'll record the animation from these characters.  So that's set up like that. And so we could do that. However, before we do that, there's some other things I want to turn off and change.  So we go into the cog here, the settings, and then under here, the take recorder, let's move this one up. You've got some things by default. Record time code is on, and also record sources into ...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_007.jpg

### Best practices for smooth recording using take recorder [16:11]
**Transcript:** But with your animation and your physics, it's actually running at like as fast as it can go like 240 frames per second or as fast as unreal can run its little legs.  So often you'll get like jitters and with things like that, and it'll look fine when it's playing it. And you go, this is great. But when you load up the animation, things will be doing this and that because it's kind of rounding out to the nearest frame, whereas reality, it's got a lot more frames in there.  So you can set that to the maximum as 240 because this sub sequencer, the frames, the keys are time based rather than frame based effectively.  So you can bring in a 240 frames per second sequencer into your regular 24 frames per second sequencer because it's just looking at the real time of one second, two seconds, three seconds rather than frames.  Anyway, so that's a good one. Now the other thing to be aware of as well as it's going to record this animation in real time. So if you've got a really heavy scene and it's chugging along, the animation will be, yeah, and it'll record it like that.  So make sure that your sequence will play at the highest frame rate that it can. A couple of tricks are to just go into...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_008.jpg

### PRESS SIMULATE before recording! [18:09]
**Transcript:** Alright, so then you hit the big red button here. And now it's going to do a countdown. And it's going to play that animation you see it's playing at half speed.  And here it's recording all those frames. And then you stop it when you're kind of ready and I'll say, stop, stop there. So now I've got a recording.  And here it's saying pending takes starting to do a new one. So if I want to see this take that I just saved. So you're going to your content browser.  And then you're going to your cinematics, your takes, and your date. And then you've got your sequence here. And if I try and play this back at the moment, it's got the two things loaded.  So if I just press stop simulation. So now it will play my actual animation like that. So this is a sub sequencer and it's spawning these things. That's why we're getting two of everything.  Because we've got this all open. And you see we've got a manny simple got cylinder on a manny in here. And then when I've opened up this sequencer, these are actually spawning. That's what that little lightning bolt means. It's actually grabbing this from the content browser, not from the outline.  Anyway, that's just an interesting fun. So say we're h...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_009.jpg

### Fine tune animation with a layered control rig [22:27]
**Transcript:** So what we do is we select our character and then we go to plus control rig and then you turn on layered control rig and that will make it an additive control rig.  Otherwise, it will be binary. It'll be on or off and it'll overwrite everything in the sequence. So you hit layered.  And now you can use the mannequin that comes this is actually got this another great reason to use the money is that he comes with this wonderful control rig.  So let's just go and select that. And if he didn't have that, then you would add the FK control rig every single FBX skeletal mesh has an FK control rig. And that's just the joint rotations.  So we can add either of those. In fact, let's just do I'll make it really simple. I'm just keep to the FK control rig.  So now here in the outliner and the animal outliner, you've got every single one of your bones and you can edit these.  So let's go and find say his head and click here is that closest there's your neck there's his head. So now I'm going to go into rotate mode.  And then let's just save a key like that. So let's save a key here. So then you add a keyframe. And I'm going to change my keyframes to cubic.  Let's just do cubic. All right. So hit...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_010.jpg

### OPTIONAL Bake layered anim and transform onto Skeletal Mesh root [24:38]
**Transcript:** So at this point, you're ready to retarget this animation onto your custom character. But now this is optional. I like to take my transform and bake that onto the actual animation track.  So at the moment, you've got an FBX animation and you've got a transform. And if I turn off the transform, you'll see what's happening to the animation.  So he's running on the spot because this animation started as a loop and we had to add a transform and animating him along when he comes to a stop and the simulation starts.  That's done relative to his root position. And so you've basically got a counter animation. So if I turn this back on, you've got both of them. And you don't notice it when you're actually playing it.  Again, it's optional, but I don't like to have the two things going. So what I like to do is combine the two together. And all we have to do is select our character.  Right mouse button. And then we say bake animation sequence.  Calling it a bakey.  And then hit OK. And then it comes up with some options. And the important one is to enable record in world space.  So that is off by default. So we hit OK on that one. And then we hit export to animation sequence. Press OK. And th...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_011.jpg

### Retarget animation onto custom character. [26:43]
**Transcript:** So this is the character that I made in character creator for as my Digi double for doing my ragdoll simulation. And then what we're going to do is take the animation that we just made and then retarget that animation onto this character.  So we go and find the animation a right mouse button. Retarget animations. And then we choose our target skeletal mesh, which is the character I just showed you.  And now you down here, you pick a animation sequence. And then you can see that it's automatically retargeting it, which is fanatastic. Thank you, Unreal for writing that.  Now, it's not quite bang on, but you can now export a retarget asset and then customize that to be much more closer up.  But I'm not going to do that in this case because what I'm going to do is make adjustments in the animation with a little bit of fine tuning with another lead control rig later.  Now we go to export animations, put them into place, give them a name and then hit export. And then I just say export.  And now that character is completely ready to use in whatever animation you want. And since it's got the transforms applied to the root position, then there's no messing around having to kind of slide it ...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_012.jpg

### METHOD 2 - Create custom Physics Asset [30:50]
**Transcript:** So part one was using my preferred method of taking the many character animating him adding physics, coding that and then retargeting a custom character to that animation.  And that's what I did for the opening scene with me running along the beam. This part now is more for the traditionalists who like to do things in a more complicated way.  It makes more sense if you're doing a character that's going to be in a game or you're using the character again and again and again, then this is really the way to do it. But it's a bit more of a pain.  And I'll show you how to do it. All right. So when you bring in your custom character, and this guy came from my clone, if you go to Rhymas button, create and physics asset, this is what happens automatically when you import a character that does never physics assets.  So you'll see, you know, when you bring in a character, it'll say skeleton, skeleton and then physics asset. And it basically runs this little tool. So you go to create physics asset create.  And then it brings this in. And I'm just going to say, OK, create asset. And this is what it gives you. And so you've got in here, you've got effectively for each joint that you decide, you...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_013.jpg

### Assign bodies to correct bones and make them fit. [32:00]
**Transcript:** And then you've got a collider object that attaches to that bone. And so when that moves around, it'll collide and it'll stop. And then the way that it moves and its limits are all based on that constraint.  OK, so effectively what we want to do is make sure that these bones are in the right place or these colliders fit the bones that we want. And that these angular limits are set in the correct way.  Because by default, if I just pressed simulate right now, if you go up here to these three little lines and go to simulate, you'll see that, you know, he's less than perfect.  So I wait and move this character around as if you hit shift and then the Rhymas button, you can drag parts of his body and see how he works.  So yeah, it's you can see why I like to use the money skeleton. OK, to stop it, you can go up here and hit simulate and that stops it.  And an alternate way is if you use the hockey, old I and then that makes it simulate, alt, I stops it. And when we get into the simulating the angular limits, you can actually select one of these constraints.  And then you hit alt shift, I and then it'll simulate just from that bone down, you can see some weird things are happening with t...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_014.jpg

### Setting how much the limbs bend with Angular Limits [40:25]
**Transcript:** So we'll act more like a human made of flesh and bones.  Okay. So now we're at the exciting part. This is the angular limits.  So here we have our angular limit and it's set down here.  And this one, it's all round and it's set to free at the moment.  So which means that if I press it and then do alt shift I, you'll see that it's just moving freely wherever it wants to.  But we want to kind of limit it so that it won't go through his chest or go too far forward or back.  So to kind of basically give each of these joint constraints the kind of angular limit of a real human.  So what we do is we go from free to limited.  Like that. So we're going to change all of these from free to limited.  So now if you look at it, it's got like a different setting for your swing.  It's basically your x, y and z. But it's kind of hard to understand what's what.  So what I do is I just turn two of them off and I'll just have one on like this.  And so that's my angular limit.  And at the moment, the bone is oriented along this line here.  And you see this line here. That's the direction of the bone even though it's going this way and that.  They work either way. They work the same as long as that's p...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_015.jpg

### Rotate Angular limits by holding alt LMB [43:40]
**Transcript:** Now I'm not 100% sure or even 12% sure why that does that.  What the difference is between rotating this, you see the whole bone goes with it and the orientation.  And it just kind of gets confusing.  So I'm not quite sure why it does any of that.  But I just know that if you hold down alt and then it lets you move this relative to that.  Because if you look at all these bones, they're all facing by default along the joint, the real joints of the skeleton.  So we have alt and grab your line.  So now we've got one axis that's working.  So now he's going great. He's sort of stopping where you kind of think he should.  To about there, that's his limit. I can't go any further than that. That looks pretty good.  Okay. Alt shift, I to stop that.  Now I'm going to just move around this way.  And now we're going to try our next axis.  And then I'm going to just do one at a time. So that was 92.  So we'll think 92. We'll remember that.  And then this next one is this direction.  So this will show you how far it will swing that way.  So now if I do alt shift, I see you can't move down.  He's only going to move left and right.  And then I'm holding shift just to drag it so he can go that far ...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_016.jpg

### Joint stiffness and springy-ness with Target Orientation and Velocity [49:22]
**Transcript:** I want to set the target orientation and target velocity of all of the joints and that's  effectively the springiness and the stiffness of all of the joints.  And that is under angular motor down here at the bottom of my details panel and you've  got target orientation and target velocity.  So target velocities turn that one on and we're going to turn on once this slurp.  So if I just do old shift I just sort of see how loose that arm is at the moment.  Now if we want to make that stiffer you change this dampening under target velocity.  So if we make him something like 50 now I do old shift I see he's got a bit more  rake like that.  And if I make him 100, old shift I then it's pretty stiff.  So now if I try and move him around with the shift right mouse button so you can see  he's a little rake.  So he needs a bit of oil.  Okay so that's just stiffness and turn him off.  And now we've got the target orientation and that is you see the disc here and you see  these angles you know your XYZ angles along this line here is effectively your target  orientation.  If we turn this on and we set it to the default what's 50 right so if I go old shift I see  what happens to that arm it's get...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_017.jpg

### Limb self collision [52:45]
**Transcript:** themselves when they go into the physics mode so in the real world we bump into ourselves  but if we were to just press alt i at this point and we were going to grab his arm and at the  moment it's going to pass through his body so we don't want that we want it to collide with  it so we have to set up our collisions so we go alt i and then sometimes if you were when  you were modeling this all when we first started out you'll see some of these are purple that  means there's a relationship a collision relationship with them so what we're going to do is just  clear off all of these collision relationships first so we grab the pelvis shift to the end and  then hit at the top here we've got enable collision and disable collision so we're going to hit  disable collision so now whichever one I grab is going to be this nice blue color which means  there's no relationships so we want to tell for example the forearm not to penetrate that this  this bone this bone and this bone or this collision object what you kind of think what you  should be able to do is just select all of them just grab grab grab grab grab grab grab grab grab grab  I have to have the sound effect grab grab grab grab gra...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_018.jpg

### Assign Physics Asset to character [57:42]
**Transcript:** So if that happens to you,  what you do is you go and find your character here  and then you write mouse button and then you edit it.  So then you go into the mesh  and then under here under asset details,  you go down to the bottom  and that's where you assign under physics,  physics asset, that's where you assign your physics asset.  So you select that one and now,  when you come out of this,  now that will be assigned to this.  So then when I press simulate,  you will now have that asset.  And then one thing I thought was,  oh, you can change,  so you can make multiple physics assets.  And so if it's got exactly the same naming  between characters and say like this is an eye clone character,  so if I brought in another eye clone character,  I'm thinking that I should be able to just retarget  the physics asset onto it  or just choose that same physics asset.  But I thought, well, let's try and see what happens  if I go and use the one that exists for the mannequin.  So it's like, oh, I wonder what happened there.  So if I now assigned that one and I press simulate,  ta da, so you can see,  it's not quite working.  All right, so that was good  because I thought, right at the end,...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_019.jpg

### Recap of Method 2 [59:00]
**Transcript:** alas, not, all right, so I'm going to do a recap now.  In summary, so we have our character,  and in this case, I've built a physics asset  for that character,  and now I'm going to make a sequencer,  cinematics, level sequence,  open that up, drag my character into there,  give him some animation, I don't know if I've got any in here.  Oh, I've got this retarget thing here, okay?  So yeah, so we've got this animation,  he's already got that in there.  So we'll use it up to this point,  and we will put something here.  So we'll have another object, so we'll bring in,  we'll go and add a cube,  bring him here, and he will have a physics asset,  like that, and then what I'll do is I'll slam this cube into him.  Bring the cube, put him in the sequencer, save a key.  Okay, so now at this point,  where he's just about to hit him,  I'm going to turn on the simulate,  so you go to select the character,  and then you can add a keyframe here,  that's the easiest way,  and then we're going to turn off simulation here,  to put in an off, so now he will play,  and then simulate at this point.  So we must go into simulate mode, right?  And boom, oh, there we are, all right.  We're not all rated...

**Frame:** tutorials\frames\beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in\frame_020.jpg


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
