---
title: Cheap AI Mocap that Actually Works - QuickMagic.Ai, Chaos Destruction, and Metahumans in UE5
source: YouTube
url: https://www.youtube.com/watch?v=7xYyfWeAHiA
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-23
ue_version: "UE5"
tags: [mocap, quickmagic, metahuman, retargeting, chaos-destruction, sequencer, battle-scene, niagara, medieval, filmmaking, intermediate]
extraction_status: complete
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
**Transcript:** the multi-camera solution from Move AI, which yields great results.  However, this comes with a few major caveats. For one, it's expensive,  costing $7,000 per year for a license. And the other is that your performances will always  be limited to what you can do inside the volume that you set up.  So, if you wanted to capture a really long running animation, maybe someone running through a battle,  or two people walking and talking through a complex environment like my last project,  you don't have a lot of options other than to run back and forth in your space and chop the  animation up. Or use a treadmill, or use an inertial suit, all of which come with their own  limitations. What would be amazing is if you could track with your actor with a camera,  and it would track your movement across the ground in 3D space, giving you basically an unlimited  volume size and decent fidelity of the animation, because the camera can stay close to the actor  the whole time. And that's where Quick Magic AI enters the picture. Now, this is easily the best  single camera mo cap solution I have used or seen. I've tried Move One from Move AI,  and the results were pretty good when it came to the general spatial accuracy of the capture.  However, it seemed to suffer from jitteriness and foot sliding. I've also tried radical motion,  which was really good and really mitigated the jitters, but still had pretty bad foot sliding,  and kind of weird posture. The free Rokoko vision solution was pretty terrible, although I  haven't really tested it that much. Quick Magic, however, seemed to be decently smooth,  and most importantly, had great foot locking, meaning the feet stayed firm on the ground and didn't  slide when they weren't supposed to. And what really caught my eye was that it could compensate  for a moving camera, keeping the subject anchored in space accurately. This made me think that  this could be a potential solution to capturing big movements over large distances that couldn't  be captured easily in a stationary volume. I wanted to make a video that I could only make if I

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
**Transcript:** So, when you import, just make sure you have the skeleton set to none, and it will bring it right in.  I want to show really quickly the entire raw animation and video side by side,  so you can see how good the capture was. I mean, this looks really good. It's not perfect.  There are a few moments where it looks like I'm shuffling a little, but I'm also kind of running  weird. It was a little slow since it was icy out, and I was hamming up the exaggerated movements.  I'm pretty sure the actual distance covered isn't accurately captured by the animation,  but it is good enough for a starting point. So, really quickly, I'll show you how to get this  animation retargeted into a sequence and onto a medicumin, so we can make any adjustments to the  animation, and add cameras, and everything else. So, just right click on your animation,  and go up here to Retarget Animation, which will bring up this window. Double-click on the animation  over here in the list, and then select the target skeletal mesh, which can be any of the  metahuman skeletons. In our case, I'll just select the male tall normal weight, then just click  export animation, select a folder, and it's retargeted, as easy as that. Now, we want to create a new  level sequence up here, and then assuming you've added a metahuman to your project, you drag them  into your level, and with the metahuman selected, go to your sequence, click the add menu, go to  actor to sequence, and select the metahuman you have selected. Now the metahuman is in your sequence,  but before we do anything, we want to make sure the LOD isn't going to change on us. So,  with your metahuman selected, go to its details panel, and in the hierarchy, scroll down to the  LOD sync, and under forced LED, change it from negative 1 to 0, which will lock your metahuman  into the highest LOD, no matter where your camera is. This is important for using things like  custom clothing, which you will see in a bit. Now, to apply the animation, you will want to delete  the control rigs from the body and face tracks, then just click the plus sign, and go to animation,  and find the animation you want to apply. And there you go, you now have the animation fully  retargeted and applied to a metahuman. Now, I went pretty quickly here, and didn't do a very deep

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_005.jpg

### Deep-dive Metahuman Performance Capture Tutorial [7:37]
**Transcript:** dive on this process, and that's because I have a very comprehensive step-by-step tutorial  right here on this channel that will show you in great detail the workflow for doing full face,  and body performance capture with metahumans. It is designed to be as accessible as possible,  and uses the cheapest tools available. Now, the tutorial uses Move 1 for the body capture,  but you can really swap that part of the tutorial out with this one and use Quick Magic instead.  Once you have the animation captured and imported into Unreal, the process is exactly the same  for cleaning up the animation, using metahuman animator for the face, building the environment, etc.  So, stay tuned for an updated version of the tutorial, which will likely feature Quick Magic.

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_006.jpg

### Rokoko Headrig with Quickmagic [8:27]
**Transcript:** Now, as you can see, I recorded this wearing a Rococo head rig to see if Quick Magic would work  while doing face capture as well. I didn't see too much of a problem with the head tracking,  which is great, and means you could probably use this for full performance capture.  I won't go over the process for using metahuman animator since that is covered in the tutorial I  mentioned, but I wanted to show that it is possible. Okay, so on to building the scene itself.

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_007.jpg

### Building the Scene and Destroying it with Chaos Destruction [8:53]
**Transcript:** I decided to go with a medieval battle scene since the assets I had on hand seemed to fit  this idea the best. I used this awesome castle, which has this great bridge I could have the guy  running on. I also used the medieval armor pack from Polyphoria, which I have used multiple times  in my past videos, as well as the modular medieval NPC version 2, which has all these amazing,  high quality outfits, which all fit metahuman's right out of the box. And I decided to use the  King outfit since I just love the cloth physics on the cape and the tunic, all of which just work  and really added to the animation itself. I decided having giant explosions in the background  all around would be really cool. And since this castle is this large stone structure, I figured I  could get away with some basic destruction without having to get too detailed. Now, I just want to say  this is definitely not meant to be a tutorial on Unreal Engine's Chaos physics engine. Chaos is  super powerful and you can get some amazing results if you know what you're doing, but you're  definitely opening up a can of worms that will add a lot of complexity to the shot. I have tried a  few times to do a video on Chaos destruction, including using the vehicles from the Matrix demo,  but I always seem to run into some bugs or hiccups in the workflow, and it ends up costing me days  trying to figure it out. By the way, if anyone has had success using the vehicle destruction from  the Matrix demo in the sequencer, I really want to hear from you. So please consider stopping by  the discord or commenting below. I will definitely be making a comprehensive tutorial in the future  that shows how to use Chaos physics and destruction in cinematics. For now, I will show you the really  basic destruction I used for this scene. And if you want to know more about how to do Chaos destruction  like this properly, I found this one tutorial by Praj Prad, unfortunately after I had done a lot  of the work in the scene already, which explains how to do this in a much more detailed and comprehensive way.  But if you want to just mess around and have some fun, what I explain here should get you started  quickly and easily. So you start by selecting the static mesh you want to destroy, and up here in  this drop down you want to change from selection mode to fracture mode. Then you select the type of  fracture you want. In my case, I chose cluster, then click new, and select a folder to save your new  geometry collection to. You can play with the settings to change how many fragments you want,  and then just click fracture. You can then play with the explode amount to see the different fragments.  And I just did that to a few different sections of the castle. Then you can see here I am moving  these yellow volumes around, which are called anchor fields, which you can find by searching your  engine content. And these are adding constraints to the fractured sections. So the entire thing  doesn't just break apart as soon as it receives any impact or damage. I'm then assigning the anchor  fields to their respective geometry collections over in the geometry collection details panel under  initialization field. Now, in order to specify when and where exactly I want the explosions to happen,  I add these pink orbs, which are called bomb fields, and are also found by searching your engine  content folder. I then place them intersecting with the meshes I want destroyed. And to hear you can  see I am cross referencing a renderer of the shot in Adobe Premiere, where I'm checking the timing  of the camera to see where it is pointing at what time. So I know when the explosion is supposed to  happen. Then I set the delay in the field's detail panel so it will activate exactly when I want.  Also, it seems that the scale of the field is one factor that determines how powerful the effect  actually is. So I'm setting the minimum and maximum scale to a certain number and making them the  same. So there is no variation when I run the simulation. The fields are then added to the  sequencers just so I can make them hidden in the render. Now, the way I did this, the engine runs  a new simulation every time I do a render. And even though I have set the physics to have as little  variation as possible, the pieces will still move a little differently every time. This makes such a  long and complex shot very difficult. Since in one render it might look great, but in the next  a huge piece lands right in front of the camera and ruins the shot. And of course every time you add a  new element, like a character, a prop or another explosion, it can cause unpredictable effects which  can make it hard to art director scenes. So you can see that I didn't even assign a material for  the interior of the rubble. So it just has this broken stretch texture over it. There are even some  weird inside out normals or something and you can see through the backs of some of the geometry.  But the tutorial by Projprod I mentioned earlier seems to cover all this in detail.  So then I just added some Niagara particle explosions to the impact areas and set their  activation time in the sequencer. My attempt at creating cannonball controls really just ended up  looking like rockets, but I figured whatever, it looks awesome. Maybe it's a trailer for King  Makers 2 cruise missile crusade to add some more production value and make it feel a little more

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
**Transcript:** I wanted to see if it was possible to get a similar shot using generative AI.  So I upgraded to ChatGPT Pro to really get more familiar with these video generating tools.  This gives the best access to OpenAI's newest video model, Sora. Anyway, let's see if we can prompt  something similar into existence. Okay, and admittedly, if there was a subreddit for prompt  this would be a top post, but I tried to be as descriptive as possible. So I did a few different  lengths of the video qualities. I started with 480p since that allowed for the longest generation,  which is 20 seconds, and I got these. So obviously it didn't get the memo on a continuous tracking shot  or adhering to our perceptions of 3D space kind of all over the place. I do love this surfing  debris shot and how he morphs into several of himself. And this one, there are definitely some  interesting things happening. It actually looks a bit like our shot, but for some reason he's running  backwards, probably because I mentioned running backwards in the prompt. It seems to have a hard time  with spatial continuity, but I love the part where he turns around and we see his face. Here is where  things start to surprise me a little. I mean, this obviously looks like a game of some kind,  and I end up getting a few generations that looked like this. Here the debris looks a lot like  unreal engine 3 destruction physics or something. I tried shortening and simplifying the prompt,  and this is what I got, which really isn't much better. I can't really say that I'm impressed,  but admittedly, text to video will never be as precise as actually building your own animation.  Not for now. So my thoughts on AI and art and the ethics of how the models are trained are

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_012.jpg

### My Thoughts on Generative AI [18:16]
**Transcript:** that my thoughts don't actually matter at all. AI is going to do its thing regardless of how I feel  about it. And as someone who works in media and art and content creation, it is extremely important  to stay up to date on these tools in order to stay relevant and to leverage them in the best ways  possible. And since you're watching this channel, I assume you see Unreal Engine as a means to an end,  which is to create the visions you have in your head for storytelling, educating,  reenacting history, etc. So I think it's important to stay agnostic to the tool that is doing the  actual rendering of your visions. So I plan to keep this channel fully focused on Unreal Engine,  especially as a filmmaking and storytelling tool, and especially focused on  meta-humans and performance capture. But I do plan to see how these AI tools can be incorporated  into the workflow. Okay, thanks for watching to the end. If you found this interesting or entertaining  or helpful, please consider liking and subscribing. We also have a Discord community link in the  description. So come on by to discuss filmmaking and Unreal Engine. And we even have people using  Quick Magic already. Here's an animation from one of our community members, Ally.  All right, my name is Charlie, and I will see you in the next one.

**Frame:** tutorials\frames\cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma\frame_013.jpg


---

## Structured Notes

### Core Technique
QuickMagic AI for continuous tracking-shot body mocap (moving camera, ~50m run, $1.86): import to UE5, retarget to MetaHuman; Chaos destruction for set pieces: fracture mode → cluster fracture → geometry collection → anchor fields (limit collapse) + bomb fields (timed explosions); LOD forced to 0 on MetaHuman for custom clothing; background characters use asset-pack mocap animations.

### Summary
19m43s production diary by Charlie Driscoll. Tests QuickMagic AI for tracking-shot mocap — key feature: compensates for moving camera while keeping subject anchored in 3D space, enabling captures over large distances (50m run). Process: film from behind/front with handheld camera, neutral lens, keep camera pointed same direction (no orbiting); upload to QuickMagic browser → AI MoCap → select UE4 mannequin skeleton, enable "moving camera" + "on-real-floor" → export FBX. Retarget to MetaHuman: RMB animation > Retarget > select MetaHuman skeleton > export. MetaHuman setup: force LOD=0 (for custom clothing); delete control rigs; add retargeted animation. Scene: medieval castle (Fab), custom clothing (Polyphoria), background MetaHuman characters with asset-pack animations. Chaos destruction: fracture mode > cluster > fracture settings > geometry collection; anchor fields (engine content) for structural constraints; bomb fields (engine content) for timed explosions; delay set in field details; explosions added as Niagara particles; caveat — simulation randomness makes complex shots difficult to art-direct consistently. Also compared with Sora AI video generation — couldn't achieve spatial continuity.

### Key Steps
1. **QuickMagic capture**: film subject from behind or front (NOT side, NOT orbiting); handheld camera; ~50m run; neutral main lens (no wide angle); Samsung Note 23 Ultra; keep camera pointed same direction throughout
2. **QuickMagic upload**: browser platform > AI MoCap > drag clip; trim; T-pose at start; drag UE4 mannequin skeleton; enable: full body + hands, T-pose, moving camera, on-real-floor export; 28 credits (~$1.86); download FBX
3. **Import to UE5**: import FBX with skeleton = None
4. **Retarget to MetaHuman**: RMB animation > Retarget Animations > select MetaHuman target skeletal mesh > Export Animation
5. **MetaHuman sequence setup**: add MetaHuman to level; actor to sequence; set forced LOD = 0 (prevents LOD changes with custom clothing); delete default control rigs; add animation track with retargeted animation
6. **Chaos destruction**:
   - Select static mesh → change viewport to Fracture Mode
   - Choose fracture type (Cluster); click New → save geometry collection; adjust fragment count; click Fracture
   - Place Anchor Fields (search engine content) → constrain geometry collection from immediately collapsing; assign in geometry collection details > Initialization Field
   - Place Bomb Fields (search engine content) → intersect with meshes to destroy; set delay in field details; make bomb fields invisible in sequencer
   - Set minimum = maximum scale for consistent results (reduces variation)
   - Add Niagara particle explosions at impact points; keyframe activation in sequencer
7. **Background characters**: MetaHumans with asset pack animations (pirate mocap, Reallusion "Run for Your Life" pack); custom medieval clothing (Polyphoria)
8. **Chaos caveats**: simulation runs fresh per render (some variation even with fixed settings); complex scenes need baking or careful art-direction; interior fracture normals/materials need manual fix

### UE Systems / Blueprints / Settings
- **QuickMagic AI**: browser-based; UE4 mannequin export; moving camera mode; on-real-floor mode
- **Fracture Mode**: viewport mode (selection mode dropdown); Cluster fracture type; geometry collection asset
- **Anchor Fields** (engine content search): constraints to prevent full collapse; assigned to geometry collection > Initialization Field
- **Bomb Fields** (engine content search): timed destruction trigger; delay parameter; scale = explosion power
- **LOD sync forced=0**: MetaHuman details > LOD Sync > Forced LOD: 0 (locks highest LOD for custom clothing)
- **Retarget Animations**: RMB animation > Retarget Animations > MetaHuman skeletal mesh

### Difficulty
Intermediate

### UE Version
UE5

### Tags
[mocap, quickmagic, metahuman, retargeting, chaos-destruction, sequencer, battle-scene, niagara, medieval, filmmaking, intermediate]

---

## Related Entries
- budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-.md (same author: QuickMagic + face capture)
- how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat.md (crowd simulation)
- recreating-brutal-deaths-from-history-in-unreal-engine-5.md (destruction cinematics)
