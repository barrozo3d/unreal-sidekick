---
title: How I Use Move.AI and Metahumans to Achieve AAA Character Animation in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=-GQWj_20J0g
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.4"
tags: [mocap, metahuman, metahuman-animator, move-ai, two-actor-capture, animation-cleanup, butterworth-filter, performance-capture, ue5]
extraction_status: complete
frames_dir: tutorials/frames/how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng/
frame_count: 10
---

# How I Use Move.AI and Metahumans to Achieve AAA Character Animation in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=-GQWj_20J0g)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 7m49s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In this video, we're going to show you how we made this Unreal Engine short film in a weekend.  We're using Move AI, a camera-based, markerless,

**Frame:** tutorials\frames\how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng\frame_000.jpg

### Goal of this Test [0:22]
**Transcript:** and a suitless motion capture system combined with Unreal Engine's metahuman animator face animation pipeline.  The idea behind this test was to capture two actors' body and face performances simultaneously,  to achieve genuine interactions,  islands, and timing between the actors.  We aim to create a pipeline with minimal friction for the actors and director,  allowing them to walk into a motion capture session, put on head rigs,  and jump right into the scene with as little discomfort and hassle as possible.  Watch to the end of the video to see the final film,  and how we think this technology is causing a paradigm shift in how we produce movies.

**Frame:** tutorials\frames\how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng\frame_001.jpg

### Assets Used [1:04]
**Transcript:** For this project, we're using some custom metahuman assets.  The medieval armor and the guards uniform come from the medieval armor pack by Polyphoria,  which provides high-quality modular armor that's easy to use.  You simply drag different parts over the skeletal mesh slots on the metahuman  and apply the appropriate materials.  The orc character is also from Polyphoria.  Although it's not a metahuman initially, it has detailed face rigging and blend shapes.  I hired an artist on Upwork to convert it to a metahuman using the metapype conversion pipeline.  This is a very in-depth process on its own, and remains one of the hardest parts of bringing  these metahuman creatures to life. The castle in our scene was also from the Unreal Engine marketplace.  I adjusted the angle of the sun to act as a cross-key light for our scene,  and added some easy fog by William Fauci.  We didn't have a specific script or story we wanted to tell.  Our main goal was to test the pipeline in essence, so forgive us our terrible writing.  I promise there is much better coming soon.  That is the worst poetry I've ever heard in my entire life!  Put you smile, let's go account for something I might.  We sta...

**Frame:** tutorials\frames\how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng\frame_002.jpg

### Capturing the Performances with Move.AI [2:15]
**Transcript:** We have six GoPro cameras set up in a ring to cover an area of around a hundred square feet,  or 9.2 square meters.  Each actor wore a head rig with an iPhone to capture facial animations simultaneously with body  animation. After sinking the face and body animations with a hand clap and mouth pop technique,  we perform the scene in one take.  Once we had our best take, we uploaded the footage to the Moove AI Cloud Processing platform.  We labeled the files and uploaded them for processing, which took a few hours.

**Frame:** tutorials\frames\how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng\frame_003.jpg

### Bringing Animations into Unreal Engine [2:53]
**Transcript:** After processing, we previewed the animations and downloaded the files for each actor.  We imported the animation files into Unreal Engine, starting with the Moove AI  pre-retarget skeleton. Then we imported body animations for each actor,  and using Unreal Engine 5.4's built-in retargeting function,  mapped the animations to our MetaHumans.

**Frame:** tutorials\frames\how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng\frame_004.jpg

### Metahuman Animator [3:13]
**Transcript:** Next, we transferred the face animations from the live link app on our iPhones to the computer,  imported them into our project and created a new MetaHuman identity.  We then processed the MetaHuman performance, and this is where the real magic happens.  In just a few clicks and a few minutes of processing,  we have AAA quality facial animation right out of the box.  We place our MetaHuman characters in the map where we're going to be filming our scene.

**Frame:** tutorials\frames\how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng\frame_005.jpg

### Assembling the Scene in Sequencer [3:48]
**Transcript:** We synced the face animations with the body animations.  I highly recommend getting a head rig to record the face animations at the same time as the body  animations. While you can record the face animations separately, little subtleties and the  eye movements will not be correct, and this is a leading contributor to the uncanny valley.  All you...  We reset, we reset.  So, now we have all the raw animations synced and on our characters.  As you can see, the raw Moove AI animation is pretty jittery.

**Frame:** tutorials\frames\how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng\frame_006.jpg

### Cleaning up Jittery Animation [4:16]
**Transcript:** I've found this to be a bit worse when capturing two actors simultaneously versus just one.  To smooth out jittery body animations, we baked the body tracks to the MetaHuman control rig,  and used the Curves Editor to apply a low-pass Butterworth filter.  This reduced high-frequency jitters, especially in the head and arms, without compromising the  animations integrity.

**Frame:** tutorials\frames\how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng\frame_007.jpg

### The Fun Part + Cost of Move.AI [4:47]
**Transcript:** Now comes the fun part.  With all the animations imported, synced, cleaned up, and assigned to their characters,  we have the scene playing out right in front of us, just like a play.  We can fly around in real time, looking at the scene from every possible angle.  There are a lot of trade-offs to creating films like this, but this process has just brought  a crazy amount of production value to a fairly low-budget production.  The Moove AI license costs roughly $7,000 per year to capture two actors at the same time,  but this is cheaper than using two X-Sense suits.  The hands are still pretty hit or miss, but the face animations from MetaHuman Animator are incredible.  If you enjoyed this video, please consider subscribing and liking.  Please leave a comment to let me know if you would like me to go into any of the processes  and more depth in future videos. Now, please enjoy the film.

**Frame:** tutorials\frames\how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng\frame_008.jpg

### Full Short Film [5:46]
**Transcript:** Not raid.  What could you possibly have the dream with us?  How about a bit of this fine Orkish jelly?  It's a hit among me, people, I?  Orkish jelly.  Oh, this sounds revolting.  But I could sing you some Melodies, I mean?  Melodies?  What about some poetry?  Well, mate, that's a fine idea.  I have some Orkish poetry.  Oh, Castle, big and strong.  That may end you ding ding dong.  That is the worst poetry I've ever heard in my entire life!  Put you smiled, I just got a account for something I might.  Maybe.  What else you got?  Uh, wisdom inside.  An Orkish perspective on Raiden Castle's, after all, who better to consult on keeping Ork's out?  Then and all, that won't seem.  Fair point, I guess.  Well, shall we then discuss this over a fine point of me?  Well, no Ork has ever asked me politely for anything in my entire life, to be honest with you.  And, uh, not that I think about it, I think about jelly.  I gotta get some of that in my belly.  Come on.  Orchial fomal is dochial, is a lamb.  Gonna get so much trouble for this.

**Frame:** tutorials\frames\how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng\frame_009.jpg


---

## Structured Notes

### Core Technique
Two-actor simultaneous performance capture using Move.AI Pro (6 GoPros in a ring, ~100 sq ft volume) with MetaHuman Animator face capture via head rigs — both actors perform the scene in one take, animations imported into UE 5.4, retargeted to custom MetaHumans, and jitter reduced via low-pass Butterworth filter on the Control Rig curves.

### Summary
Charlie Driscoll demonstrates his team's pipeline for capturing two actors simultaneously using Move.AI Pro and MetaHuman Animator. Six GoPro cameras in a ring cover ~100 sq ft; each actor wears a head rig with an iPhone for face capture. After a single performance take, footage is uploaded to Move.AI cloud, processed, and downloaded as per-actor FBXs. These are imported into UE 5.4, retargeted to custom MetaHumans (including a Polyphoria orc converted to MetaHuman via Metapype), synced in Sequencer, then smoothed using a Butterworth low-pass filter baked through the Control Rig. The resulting "play" can be explored in real time by flying camera through the scene. Honest assessment of cost ($7,000/year for MovePro) versus quality trade-offs.

### Key Steps
1. Set up 6 GoPro cameras in a ring covering ~100 sq ft capture volume; each actor wears head rig with iPhone for MetaHuman Animator face capture.
2. Perform scene in one take; upload all camera footage to Move.AI cloud for processing (few hours).
3. Preview and download per-actor FBX animation files.
4. Import FBXs into UE; use UE 5.4 built-in retargeting to map animations to MetaHuman skeletons.
5. Transfer face capture from iPhone to PC via LiveLink archives; import into Unreal; create MetaHuman Identity; process face performance.
6. Sync face + body animations in Sequencer using clap/mouth-pop sync marker.
7. Bake body animation to MetaHuman Control Rig; open Curves Editor; apply low-pass Butterworth filter to head/arm/body controls to reduce high-frequency jitters.
8. Fly camera in real time to discover shot angles; set up cameras in Sequencer.

### UE Systems / Blueprints / Settings
- Move.AI Pro multi-cam (6 GoPros, ~100 sq ft volume, $7,000/year, 2-actor simultaneous)
- MetaHuman Animator (face capture, LiveLink Archive import)
- UE 5.4 Animation Retargeter (Move.AI FBX → MetaHuman skeleton)
- Level Sequencer (face + body sync, camera animation)
- MetaHuman Control Rig (bake + edit)
- Curves Editor: low-pass Butterworth filter (head/arm/body controls)
- Polyphoria Medieval Armor Pack + Orc character (converted to MetaHuman via Metapype pipeline)
- Easy Fog by William Fauci (environment atmosphere)
- Directional Light (cross-key lighting setup)

### Difficulty
Intermediate

### UE Version
5.4

### Tags
mocap, metahuman, metahuman-animator, move-ai, two-actor-capture, animation-cleanup, butterworth-filter, performance-capture, ue5

---

## Related Entries
- `cinematic-motion-capture-with-move-one-and-metahuman-animator---unreal-engine-54.md` — full beginner tutorial for budget version of this pipeline using Move One
- `how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator.md` — production breakdown of mafia cinematic using the same Move.AI Pro setup
- `motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma.md` — two-actor sword fight using this same two-person capture approach
