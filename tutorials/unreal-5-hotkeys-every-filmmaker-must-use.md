---
title: Unreal 5 Hotkeys Every Filmmaker Must Use
source: YouTube
url: https://www.youtube.com/watch?v=HU7qHi6bn9A
author: Josh Toonen
ingested: 2026-06-18
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-5-hotkeys-every-filmmaker-must-use/
frame_count: 14
---

# Unreal 5 Hotkeys Every Filmmaker Must Use

**Source:** [YouTube](https://www.youtube.com/watch?v=HU7qHi6bn9A)
**Author:** Josh Toonen
**Duration:** 20m29s | 14 section(s)

---

## Raw Data (for Claude Code extraction)


### Unreal 5 Filmmaking Starts with Sequencer [0:00]
**Transcript:** You can't make films and unreal if you haven't mastered sequencer.  This is the timeline where you can add animations to characters, lights and effects,  whether you're completely new to Unreal filmmaking or you just want to speed up your workflow,  this is for you.  To make it easy to get up and running inside of sequencer and take everything I've learned from last eight years,  I worked as an artist and supervisor on Hollywood Visual Effects.  I'm movies like Star Wars 9, Fantastic Beasts, and Across the Spider-Verse.  And I started using Unreal Engine as an on-set operator in virtual production on Netflix's Avatar, The Last Airbender.  And when you use Unreal on set, you have to be ready to make any change at the last minute.  And when the whole crew around you is waiting, you have to make those changes in seconds.  That's why you have to be fast, nimble, and smarter inside of sequencer.  So I put together a list of 20 of my favorite sequencer hotkeys and tips  to make your workflows even faster inside of sequencer.  We're going to move quick, select this video so you can jump back to it later and stick around until the end,  because I'll share my favorite tip on how to add slow...

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_000.jpg

### Sequencer Hotkeys You'll Use Everyday [1:08]
**Transcript:** So here I am in the project file for War of Being,  and I'm going to open up one of these level sequences and let's start with the basics.  So pressing play will play through your sequence.  This thing in the middle is our time indicator that we can scrub along and decide on a frame.  A really important note for visual effects is you need to have this magnet icon enabled.  D is the hot key here, and this will snap your time indicator to a whole frame.  If I zoom in here and I disable this magnet, you can see I can scrub in between our frames here,  but this will add stuttering and jitteriness to your renders if you create key frames in between any whole frames.  So make sure that's enabled.  The next hot key to know is jackal.  So jk and l j will reverse your timeline.  K will pause it and l will play it forward.  So just remember jackal, and if you don't want to use hot keys,  you can do the same thing with these buttons down here.  We have play forward, play in reverse, and then we can step forward by one frame.  You can also use your arrow keys to step forward by one frame,  or you can press shift and then the left and right arrow keys to jump ahead.  Or backwards by five frames...

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_001.jpg

### Must-Use Settings when Starting from Scratch [3:57]
**Transcript:** graveyard sequence. And I've taken our two characters and we've imported them in the scene.  So from here, all we'd have to do is right click in our content browser, go to Cinematics and  create a new level sequence. So now we have an empty level sequence. Now you'll also want to change  over your frames per second here from 30 frames per second over to 24, which is the standard  frame rate for movies. And the first thing to do is start to add our characters and cameras into  sequencer. So there's a couple ways we can do this. The first and easiest is just to drag that  reference from the outliner into sequencer and it'll automatically add it. The other way,  I'll click on our other samurai is to add this actor to sequencer through the add track button.  And this will be the same exact thing. And the last way, the hot key that I try to use is you have  to select your object in the viewport and then press Control A. And you'll see that pops into our  sequencer here. And if this isn't working for you, just make sure you right click inside of sequencer  before pressing any hot keys to make sure you're communicating with sequencer. Now with characters,  the first thing to do is to add ...

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_002.jpg

### Animating Cine Cameras in Unreal 5 [5:12]
**Transcript:** sequencer. One is a cine camera and the other is a camera cut track. So there's two methods for  that. The easiest by far is just to click on this create a new camera icon. And this will create a  camera from your specific view. But you should also know it's easy to create custom hot keys for any

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_003.jpg

### Create Customized Hotkeys in Unreal 5 [5:30]
**Transcript:** option inside of sequencer to make that even faster. So let's make a hot key for creating a new camera.  If I go to edit editor preferences, I'm going to type in camera and scroll down to the sequencer hot  keys here. And you can see that the create camera currently doesn't have a hot key. So one that I  like to use so that I don't press it on accent is Control Shift Alt C. I still like to use the C  for the camera icon. But obviously with Control C it's a widely used hot key. But now I can go  around in the scene, find a nice spot and just press Control Shift Alt C and it will create a new  camera. Now this camera came in with this little lightning bolt icon and that just means that this  is a spawned actor. Meaning if I close this level sequence, there's no camera inside of our 3D  world. And now I can even search for a cine camera and it won't show up. For cameras, I almost  always convert these to possessible because I just want them to live inside of the scene.  And now it'll exist regardless if I close sequencer or not. Now this isn't a hot key, but this is my  most useful tip in terms of animating characters and cameras. And that's using a stage actor.  I like to parent both...

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_004.jpg

### Animating the Easy Way [7:16]
**Transcript:** sequencer is animating different details of any actor inside of sequencer. Now you'll notice by  just looking through the camera options here that we have a couple little keyframe icons inside  of the details panel. And this is by far the fastest way to add keyframes for things like focal  length and aperture. Now we have these three keyframes set. And if I enable auto keyframe, this icon here,  I can scrub later on and adjust something like the zoom. And it'll automatically animate between  our two keyframes. But one thing that can be really confusing early on is that you don't see any of  these ad keyframes next to our location and rotation option. But obviously the most common thing to do  is to animate the transform. So to create any property inside of sequencer, we need to add a track.  So for our Cine camera actor, let's add in a transform track. And this will give us location,  rotation and scale and allow us to set two keyframes and animate between them. Now I can see that the  animation is a little offset here. So I'm just going to select all of these keyframes and then press  control and write arrow key. And that will just nudge these keyframes by one frame until I like t...

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_005.jpg

### Piloting Cameras in Sequencer [9:15]
**Transcript:** cine camera actor. The hot key here is shift P to pilot your camera. You can see whether we're  piloting on the top left. And now we can pilot this around. And because we have auto keyframe enabled,  this will automatically update and we can quickly change our animation. So that's piloting your  camera. But the first track of any sequencer should be this camera cuts track. This is what movie  render queue will decide to render. And when you view this camera instead of piloting it,  which is shift C for the hot key, if you're viewing your camera cut, you can't adjust this camera  at all. I'm right clicking in the viewport, but I'm not able to actually change the transform.  So when you're ready to lock down your camera, this is the best option is don't pilot your camera.  View the camera cut and then you'll never have to worry about changing your animation.  Another way to set this up is you can right click on any actor and lock this actor. You'll see that  all of our tracks turn red. And this means that we can't adjust any keyframes inside of sequencer.  Just make sure to right click and unlock it when you want to make any changes. You can also pin  any actor to the top of sequence...

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_006.jpg

### Animating Materials + Blueprints in Sequencer [10:36]
**Transcript:** any property inside of sequencer even down to the materials. So what if I wanted to change the color  or intensity of our gold samurai's eyes here? Well that exists in this element zero material.  Well we could adjust that in this first material here by changing the emissive strength,  brighter or lower by setting it to zero. It turns off. But what if I only wanted to change it  inside of this one shot and not for our entire project file? Well I can't drag this emissive  strength into sequencer. But I can keep adding in tracks until I can find this emissive strength.  So let's go to add a track. And here we can see this skeletal mesh component. Now if I look on the  right side of our details panel, we can see that it's the skeletal mesh component is inside of this  actor that has all of these details underneath it. So we need to add in the skeletal mesh component  track in order to animate anything inside of here. Once this is added, we can add another track  to adjust the material parameters of any one of our materials. So let's select element zero  and add a parameter here. And now we can easily find that emissive strength. And it'll automatically  create a keyframe. So now if I ...

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_007.jpg

### Camera Preview (and when to use it) [12:14]
**Transcript:** I personally like to disable this, but people have different preferences. So if you go to the  editor preferences and type in camera preview, I'll toggle back on preview selected camera. And this  will give us an additional viewport that we can pin at any time. Let me change this down to a size  of three and minimize this window. And how this works is you'll just press on this little pin icon.  And now you'll have this little preview window docked to the side of your viewport at any time.  And this can make it easier to adjust your scene while still previewing your camera. All you have  to do is unpin this preview and as soon as you select anything else in your scene, that preview will  go away. Now I tend to always just use the shift to see hot key to view the camera cut, but use  whatever is easier. Now if you ever want to hide the details of any object and sequencer, just select

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_008.jpg

### Organize Sequencer in Seconds [13:00]
**Transcript:** it and press the V key and that will hide everything below it. Or if you want to expand any detail that  can be key framed, press shift V to reveal it. And that will show you every single object and  expand any of these hidden drop downs. Now as soon as you start to add a lot of things in,  your sequencer can get pretty messy. So to organize it, you can just press control F to search for  anything inside the sequencer. I'm just going to search for the samurai. And now I can select both  of these and press control G. This will create a new folder and add these actors into that folder.  So now I can just rename this as characters and now it's really easy to hide these or show them  whenever they're needed. Oftentimes I'll make anywhere from 20 to 40 cameras for a single shot.  So when I find something I'm happy with, I'll take all of the old cameras and throw them into  a folder so they still exist, but they're hidden from the rest of sequencer. Now if you have character

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_009.jpg

### Character Animation (FK Control Rigs) [13:58]
**Transcript:** animation and you want to modify it further inside of sequencer, you have two options for that.  You can either edit this with an FK control rig. Now this will not give you the controls you're  probably looking for if you have a humanoid character, but this will convert your skeleton into an  FK control rig so you can modify any bone. But the way we did this on War of Being was we created  control rigs for all of our characters so we could bake our animation onto this control rig that  makes it very easy for us to go back and add any modifications to certain keyframes. But in this  case we have an IK rig, so our hands and feet will stay in the same exact place but we can still  move around at the rest of the body. Now you can also add in additive tracks so you don't have to  modify every single keyframe. You can just identify a single bone that you want to adjust like these  hips. So as an example, I'll just tilt him over to do something really obvious and awkward and  just create a single keyframe. And now for the entire rest of the animation will have that offset.  So you can do this for the hands, feet or anything else inside of your scene to make quick adjustments  to your anim...

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_010.jpg

### The Best Method for Slow Motion (Bullet Time) [15:05]
**Transcript:** sequencer. Now if you want to stretch and squash or just re-time your keyframes, you have a couple  options here which make it pretty easy. The first if I want to change these transform keyframes would  be to grab this gray track at the top of any property that's keyframe and you can simply drag  these in and out points and you'll see that they scale in re-time correctly. But let's say you just  wanted to re-time the end and not the entire sequence that could get a little tricky but they  built a tool for that as well. If you press control M you'll get this hidden transform menu here  and this will let you offset your keyframes forwards or backwards by 10 units or you can make this twice  as long or you can divide these by two so they'll go twice as fast. So you can quickly double or  half any amount of keyframe animation but with this transform menu you just select the keyframes  you want so you don't affect your entire frame range. But in my opinion the best way to add slow  motion is to create a time dilation track. Just look through this drop down here and add it into  your scene and this will give us a time multiplier we can apply across our entire world. So if I set  this dow...

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_011.jpg

### Preview Your Render in the Viewport [16:51]
**Transcript:** totally get it. This was definitely the hardest thing to comprehend at the very beginning but the  real important thing that you have to know which will hopefully demystify this entire thing is that  whenever you go to render local out of movie render queue what happens is our game starts to play  and our physics begin to simulate. Now this can be very confusing because we're not really  playing a video game inside of Unreal Engine. We really just want to play back sequencer but we  can't preview our final render because this is not through our camera but even if we did and look  through our camera cut here we could start on the first frame but the timing is not exact here  it's not correct and our render would actually look slightly different than what we're seeing here.  So how can we fix that? Well the way to preview your render exactly inside of your viewport  is actually really simple so let's browse to our level sequence here. All we have to do is click  and drag this level sequence and add it into our scene. Now this is an actor just like anything else  just like our camera or our particles or our lights there's actors inside of the scene and all we  have to do is set this t...

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_012.jpg

### Join our Unreal Filmmaking Bootcamp [19:00]
**Transcript:** back you can press shift and f1 and now you can select anything inside of your scene and start making  adjustments while your game is playing. Now this took me just a couple seconds to explain but  honestly it took me months to learn how this entire system works together so leave a like down  below if you learned something new now did you know you can master all the skills to make your own  films inside of Unreal 5 and be job ready in just 21 days and no you don't need to know how to  model how to animate or how to code you can go from a complete beginner to creating Hollywood level  visuals in just 30 minutes a day we've helped complete beginners and industry pros just like you  learn the skills to be job ready at visual effects in virtual production studios all you have to do  is go to on real for vfx.com slash fundamentals I've taken every lesson every template and every  cheat sheet that I use on my own commercial projects and I'm giving them away for free when you  join unreal fundamentals this is filmmaker focused training so you can create your own action scenes  entirely in unreal 5 these are battle tested on real world productions and I'm giving all of my  best secrets awa...

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_013.jpg


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
