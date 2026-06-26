---
title: How I Use Move.AI and Metahumans to Achieve AAA Character Animation in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=-GQWj_20J0g
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-23
ue_version: "UE5"
tags: [mocap, metahuman, move-ai, animation, sequencer, character, performance-capture, butterworth-filter, two-actor, cinematics]
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
**Transcript:** For this project, we're using some custom metahuman assets.  The medieval armor and the guards uniform come from the medieval armor pack by Polyphoria,  which provides high-quality modular armor that's easy to use.  You simply drag different parts over the skeletal mesh slots on the metahuman  and apply the appropriate materials.  The orc character is also from Polyphoria.  Although it's not a metahuman initially, it has detailed face rigging and blend shapes.  I hired an artist on Upwork to convert it to a metahuman using the metapype conversion pipeline.  This is a very in-depth process on its own, and remains one of the hardest parts of bringing  these metahuman creatures to life. The castle in our scene was also from the Unreal Engine marketplace.  I adjusted the angle of the sun to act as a cross-key light for our scene,  and added some easy fog by William Fauci.  We didn't have a specific script or story we wanted to tell.  Our main goal was to test the pipeline in essence, so forgive us our terrible writing.  I promise there is much better coming soon.  That is the worst poetry I've ever heard in my entire life!  Put you smile, let's go account for something I might.  We start in the motion capture stage, which in this case is an empty garage.

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
Two-actor simultaneous Move AI + MetaHuman Animator pipeline: 6 GoPros in ring → both actors perform scene in one take with iPhone head rigs → upload to Move AI Cloud → download per-actor files → import Move AI pre-retarget skeleton → UE5.4 built-in retarget to MetaHuman → transfer iPhone face data → create MetaHuman Identity → process performance → sync face+body in Sequencer → bake body to Control Rig → Curves Editor Butterworth low-pass filter for jitter cleanup.

### Summary
Charlie Driscoll tests simultaneous two-actor Move AI capture in a garage with 6 GoPros covering ~100 sq ft. Each actor wears Rokoko head rig (iPhone) for face capture. Sync method: hand clap + mouth pop to align face and body timecodes. Performances uploaded to Move AI Cloud → few hours processing → per-actor animation files downloaded. Import pipeline in UE5.4: import Move AI pre-retarget skeleton → import body animation files → use built-in Retarget (UE5.4) to remap to MetaHuman skeleton. Face: transfer recordings from Live Link app on iPhone to PC → import → create MetaHuman Identity → Process Performance → AAA face animation in minutes. Sequencer: sync face + body animation tracks; head rig recording simultaneously avoids eyeline mismatch that causes uncanny valley when face is recorded separately. Cleanup: bake body tracks to MetaHuman Control Rig → Curves Editor → low-pass Butterworth filter to remove high-frequency jitter (especially head + arms). Cost: $7,000/year Move AI license for 2-actor capture; comparable to or cheaper than two Xsens suits. Limitation: hands still hit-or-miss.

### Key Steps

**Capture stage:**
1. Set up 6 GoPro cameras in 360° ring covering ~100 sq ft capture area
2. Each actor: mount iPhone in Rokoko adjustable head rig
3. Sync method: hand clap (body timecode sync) + mouth pop (face timecode sync) at start of each take
4. Perform scene in one continuous take
5. Upload footage to Move AI Cloud → label files per actor → wait few hours for processing

**Import to UE5 (body):**
1. Download processed animation files from Move AI platform (per actor)
2. UE5: Import Move AI pre-retarget skeleton FBX
3. Import body animation for each actor (FBX)
4. UE5.4 Retarget: Assets → Retarget → map Move AI skeleton → MetaHuman skeleton → bake retargeted animation

**MetaHuman Animator (face):**
1. iPhone Live Link app: transfer face recordings to PC
2. UE5: import face performance files
3. Create MetaHuman Identity for each actor (matches face mesh to performance)
4. Process MetaHuman Performance → face animation generates automatically (few minutes)

**Sequencer assembly:**
1. Place MetaHuman characters in scene
2. Add body animation track → assign retargeted body animation
3. Add face animation track → assign processed face animation
4. Sync face + body using clap/pop markers → offset tracks to align

**Jitter cleanup:**
1. Select body animation track in Sequencer → Bake to Control Rig
2. Open Curves Editor
3. Select jittery curves (head, arms)
4. Apply Filters → Butterworth Low-Pass filter → reduces high-frequency jitter without destroying motion integrity

**Assets used:**
- Medieval armor (Polyphoria): drag armor parts onto MetaHuman skeletal mesh slots
- Orc character (Polyphoria): non-MetaHuman initially → converted via Metapipe pipeline (hired Upwork artist)
- Castle: UE Marketplace asset
- Easy Fog (William Faucher): Marketplace fog system

### UE Systems / Blueprints / Settings
- **Move AI MovePro**: 6-camera markerless mocap; $7,000/year; 2-actor simultaneous; cloud processing (few hours/clip); provides pre-retarget skeleton for UE import
- **UE5.4 Built-in Retarget**: Retarget Asset tool; maps Move AI skeleton → MetaHuman skeleton; no third-party plugin needed in UE5.4+
- **MetaHuman Animator**: UE5 built-in tool; requires iPhone 12+; imports Live Link face recordings → create MetaHuman Identity → Process Performance; corrects eye movements for uncanny valley prevention
- **Live Link (iPhone)**: records face animation during capture; transfer to PC after session; sync with body via clap/pop markers
- **Rokoko head rig**: adjustable iPhone mount; keeps phone stable on actor's head during physical performance; enables simultaneous body+face capture
- **Bake to Control Rig (Sequencer)**: converts animation track keyframes to Control Rig poses → makes curves editable in Curves Editor
- **Butterworth Low-Pass Filter (Curves Editor)**: smoothing filter in UE5 Curves Editor; removes high-frequency jitter from mocap data while preserving large-arc motion; particularly effective on head + arm curves
- **Metapipe**: MetaHuman conversion pipeline; converts third-party character meshes to MetaHuman format; complex process; suitable for outsourcing on Upwork

### Difficulty
Advanced (full dual-actor mocap pipeline + jitter cleanup)

### UE Version
UE5

### Tags
[mocap, metahuman, move-ai, animation, sequencer, character, performance-capture, butterworth-filter, two-actor, cinematics]

---

## Related Entries
- how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator.md (same author, solo actor Move AI breakdown with 3D Scan Store heads)
- how-i-made-this-aaa-battle-scene-in-unreal-engine-5.md (same author, Move AI naval battle + Dramatic Deaths pack)
- how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal.md (same author, OverCrowd for large crowds)
