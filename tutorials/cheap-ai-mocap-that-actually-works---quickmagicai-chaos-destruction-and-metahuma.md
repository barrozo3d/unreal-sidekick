---
title: Cheap AI Mocap that Actually Works - QuickMagic.Ai, Chaos Destruction, and Metahumans in UE5
source: YouTube
url: https://www.youtube.com/watch?v=7xYyfWeAHiA
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma/
frame_count: 14
---

# Cheap AI Mocap that Actually Works - QuickMagic.Ai, Chaos Destruction, and Metahumans in UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=7xYyfWeAHiA)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 19m43s | 14 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In this video, we'll mix professional mo-cap animation with QuickMagic AI,  a cheap motion capture solution that might be the best in its class.  Also, your QuickMagic's unique game-changing feature that allow me to capture a  continuous running tracking shot using a single Android phone camera.  Using Unreal Engine 5, we will build an entire medieval battle scene around our animation,  utilizing some basic chaos physics to create dynamic environmental destruction.  And in the end, we'll see how close we can get to our animation using the latest cutting-edge AI  video generation tools. And the results might surprise you.  So, for the motion capture I produce for this channel, I use mostly Move Pro,

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_000.jpg

### The hidden feature of Quickmagic [0:37]
**Transcript:** the multi-camera solution from Move AI, which yields great results.  However, this comes with a few major caveats. For one, it's expensive,  costing $7,000 per year for a license. And the other is that your performances will always  be limited to what you can do inside the volume that you set up.  So, if you wanted to capture a really long running animation, maybe someone running through a battle,  or two people walking and talking through a complex environment like my last project,  you don't have a lot of options other than to run back and forth in your space and chop the  animation up. Or use a treadmill, or use an inertial suit, all of which come with their own  limitations. What would be amazing is if you could track with your actor with a camera,  and it would track your movement across the ground in 3D space, giving you basically an unlimited  volume size and decent fidelity of the animation, because the camera can stay close to the actor  the whole time. And that's where Quick Magic AI enters the picture. Now, this is easily the best  single camera mo cap solution I have used or seen. I've tried Move One from Move AI,  and the results were pretty good when it came to the ge...

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_001.jpg

### Concept for the Tracking Shot [2:55]
**Transcript:** had this feature, so I thought of a continuous tracking shot following a guy running. What would he  be running from? I don't know, but I figured it would be a giant monster or something. At first,

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_002.jpg

### Capturing the Animation [3:09]
**Transcript:** I thought it would make more sense to try tracking with my motion from the side,  getting a clear view of how fast I was going and how much ground I was covering. This, however,  didn't seem to work as intended, and as you can see, makes it look a little like I was running  on a treadmill. What did end up working was filming, well following me from behind or from the front.  My friend filmed me with my Samsung Note 23 Ultra, well we ran about 50 meters, or roughly  half a football field, as I pretended to dodge round objects running from something big chasing me.  Also, we are filming on the camera's neutral main lens to avoid any distortion you might get from  a wide angle lens. My friend kept the camera as steady as possible and kept me in frame the whole time.  Also, the camera needs to stay pointed in the same general direction for this to work.  If you try to orbit around your subject, it rotates the character, which is not what you want.

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_003.jpg

### Processing the Animation with Quickmagic [4:08]
**Transcript:** I then brought the footage into QuickMagic's browser-based platform.  So, here we are at this perfectly normal, unremarkable login screen for a QuickMagic AI.  If you are greeted by this lovely young lady, you know you've come to the right place.  So, you just click on AI MoCab over here on the left and drag your clip into the window.  You can trim your clip if you want, and here I did a T-pose, which isn't necessary, but  you'll want to do that for the best results. It will then detect the subject, and you just drag  the skeleton you want to use from the selection on the right. I chose the Unreal Engine 4 mannequin.  You're then given some options for what you want to track, and based on what you choose,  it will charge you the corresponding amount of credits, which in this case is 28V coins,  which seems to equal roughly $1.86. So, for this, I want to track full body and hands,  T-Pose for starting frame, moving camera, and export format on real floor.  Then, it processes, and it's as easy as that. You can see here it seems to be working as intended,  so we will download the animation and bring it into Unreal Engine 5.

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_004.jpg

### Applying Quickmagic Aniamtion to Metahumans in UE5 [5:19]
**Transcript:** So, when you import, just make sure you have the skeleton set to none, and it will bring it right in.  I want to show really quickly the entire raw animation and video side by side,  so you can see how good the capture was. I mean, this looks really good. It's not perfect.  There are a few moments where it looks like I'm shuffling a little, but I'm also kind of running  weird. It was a little slow since it was icy out, and I was hamming up the exaggerated movements.  I'm pretty sure the actual distance covered isn't accurately captured by the animation,  but it is good enough for a starting point. So, really quickly, I'll show you how to get this  animation retargeted into a sequence and onto a medicumin, so we can make any adjustments to the  animation, and add cameras, and everything else. So, just right click on your animation,  and go up here to Retarget Animation, which will bring up this window. Double-click on the animation  over here in the list, and then select the target skeletal mesh, which can be any of the  metahuman skeletons. In our case, I'll just select the male tall normal weight, then just click  export animation, select a folder, and it's retargeted, as easy as ...

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_005.jpg

### Deep-dive Metahuman Performance Capture Tutorial [7:37]
**Transcript:** dive on this process, and that's because I have a very comprehensive step-by-step tutorial  right here on this channel that will show you in great detail the workflow for doing full face,  and body performance capture with metahumans. It is designed to be as accessible as possible,  and uses the cheapest tools available. Now, the tutorial uses Move 1 for the body capture,  but you can really swap that part of the tutorial out with this one and use Quick Magic instead.  Once you have the animation captured and imported into Unreal, the process is exactly the same  for cleaning up the animation, using metahuman animator for the face, building the environment, etc.  So, stay tuned for an updated version of the tutorial, which will likely feature Quick Magic.

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_006.jpg

### Rokoko Headrig with Quickmagic [8:27]
**Transcript:** Now, as you can see, I recorded this wearing a Rococo head rig to see if Quick Magic would work  while doing face capture as well. I didn't see too much of a problem with the head tracking,  which is great, and means you could probably use this for full performance capture.  I won't go over the process for using metahuman animator since that is covered in the tutorial I  mentioned, but I wanted to show that it is possible. Okay, so on to building the scene itself.

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_007.jpg

### Building the Scene and Destroying it with Chaos Destruction [8:53]
**Transcript:** I decided to go with a medieval battle scene since the assets I had on hand seemed to fit  this idea the best. I used this awesome castle, which has this great bridge I could have the guy  running on. I also used the medieval armor pack from Polyphoria, which I have used multiple times  in my past videos, as well as the modular medieval NPC version 2, which has all these amazing,  high quality outfits, which all fit metahuman's right out of the box. And I decided to use the  King outfit since I just love the cloth physics on the cape and the tunic, all of which just work  and really added to the animation itself. I decided having giant explosions in the background  all around would be really cool. And since this castle is this large stone structure, I figured I  could get away with some basic destruction without having to get too detailed. Now, I just want to say  this is definitely not meant to be a tutorial on Unreal Engine's Chaos physics engine. Chaos is  super powerful and you can get some amazing results if you know what you're doing, but you're  definitely opening up a can of worms that will add a lot of complexity to the shot. I have tried a  few times to do a video on Chao...

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_008.jpg

### Background Metahuman Characters and Mocap Asset Packs [14:25]
**Transcript:** like a battle. I added some background characters. And these were all metahumans and they're all  using either the medieval armor or modular medieval NPC version 2 clothing from Polyphoria.  Now I want to be clear, I'm not claiming I use quick magic for the animations and the background  characters. I used a few different animation packs like this pirate mocap for the sword fighting  animation and these animations from the reallusion run for your life pack which are pretty great quality.  Okay, with all that said, let's take a look at the final tracking shot.

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_009.jpg

### FINAL SHOT [15:06]
**Transcript:** Okay, thanks for watching. So for this little test, I think it turned out pretty good.

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_010.jpg

### Extra Battle Scene Shots [15:37]
**Transcript:** Now since the purpose of this video was to make a continuous tracking shot, I didn't  cut in any shots of any of the background characters. So to spice it up a little, I just rendered  out a few shots to get a little more juice for the squeeze, so to speak. It really gets the  imagination going for some cool battle scenes that could be done using this tech. If you want to  see another battle scene I've made an unreal engine using a lot of the same medieval clothing  assets and metahumans, I highly suggest checking out this video I made of a historic naval battle in  the 1500s. Alright, so before ending this video, which has gotten way longer than I expected,

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_011.jpg

### Trying to Recreate the Shot with Sora [16:17]
**Transcript:** I wanted to see if it was possible to get a similar shot using generative AI.  So I upgraded to ChatGPT Pro to really get more familiar with these video generating tools.  This gives the best access to OpenAI's newest video model, Sora. Anyway, let's see if we can prompt  something similar into existence. Okay, and admittedly, if there was a subreddit for prompt  this would be a top post, but I tried to be as descriptive as possible. So I did a few different  lengths of the video qualities. I started with 480p since that allowed for the longest generation,  which is 20 seconds, and I got these. So obviously it didn't get the memo on a continuous tracking shot  or adhering to our perceptions of 3D space kind of all over the place. I do love this surfing  debris shot and how he morphs into several of himself. And this one, there are definitely some  interesting things happening. It actually looks a bit like our shot, but for some reason he's running  backwards, probably because I mentioned running backwards in the prompt. It seems to have a hard time  with spatial continuity, but I love the part where he turns around and we see his face. Here is where  things start to surprise me a l...

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_012.jpg

### My Thoughts on Generative AI [18:16]
**Transcript:** that my thoughts don't actually matter at all. AI is going to do its thing regardless of how I feel  about it. And as someone who works in media and art and content creation, it is extremely important  to stay up to date on these tools in order to stay relevant and to leverage them in the best ways  possible. And since you're watching this channel, I assume you see Unreal Engine as a means to an end,  which is to create the visions you have in your head for storytelling, educating,  reenacting history, etc. So I think it's important to stay agnostic to the tool that is doing the  actual rendering of your visions. So I plan to keep this channel fully focused on Unreal Engine,  especially as a filmmaking and storytelling tool, and especially focused on  meta-humans and performance capture. But I do plan to see how these AI tools can be incorporated  into the workflow. Okay, thanks for watching to the end. If you found this interesting or entertaining  or helpful, please consider liking and subscribing. We also have a Discord community link in the  description. So come on by to discuss filmmaking and Unreal Engine. And we even have people using  Quick Magic already. Here's an animatio...

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_013.jpg


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
