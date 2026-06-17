---
title: The best real-time mocap I have ever seen - Captury, Captive Devices, and Metahuman Animator - UE5
source: YouTube
url: https://www.youtube.com/watch?v=h5QzOjs8418
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.6"
tags: [mocap, real-time-mocap, captury, captive-devices, metahuman-animator, overcrowd, markerless, performance-capture, unreal-fest, ue5]
extraction_status: complete
frames_dir: tutorials/frames/the-best-real-time-mocap-i-have-ever-seen---captury-captive-devices-and-metahuma/
frame_count: 7
---

# The best real-time mocap I have ever seen - Captury, Captive Devices, and Metahuman Animator - UE5

**Source:** [YouTube](https://www.youtube.com/watch?v=h5QzOjs8418)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 5m46s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Just two weeks ago, I was at Unreal Fest, and what I saw there absolutely blew my mind.  And no, that's not just YouTube hyperbole. Check this out.  I got to test a completely markerless, real-time, full performance capture setup  for both body and face, streaming directly into Unreal Engine onto a medical note.  This was demoed to thousands of people throughout the course of the convention,  and was even done live during this state of Unreal keynote.  Now I'm going to do it. I'm going to do it like a giant and like looking up at like myself as a  giant or whatever. Yep. And honestly, this is hands down the best real-time performance capture  I have ever seen. And it had no suits, no markers, and no depth sensors.  The freedom that that gives actors and filmmakers or anyone doing performance capture for that matter  is a total game changer. And in this video, I'm going to show you why.  We're going to take a really close look at the accuracy of these real-time captures,  as well as breakdown the costs, as well as what this tech might be best suited for.

**Frame:** tutorials\frames\the-best-real-time-mocap-i-have-ever-seen---captury-captive-devices-and-metahuma\frame_000.jpg

### Equipment Used [1:10]
**Transcript:** So here's the gear that I was using. For body capture, I stepped into the capture  relive setup, which is a fully-markerless mocap system that tracks everything from head to  fingers with AI and machine vision cameras. At the same time, I wore the Core HMC facial rig  by captive devices. Its lightweight has a single, monocular camera and was comfortable enough to  honestly forget I even had it on. Yeah, wow, this is super comfortable and very, very light.  It's like wearing nothing. It really makes a difference compared to a head rig with a phone,  and not having that weight impeding the motion of your neck. That's really important.  The captive devices and metacuman teams running the demo were awesome and generously shared

**Frame:** tutorials\frames\the-best-real-time-mocap-i-have-ever-seen---captury-captive-devices-and-metahuma\frame_001.jpg

### Capturing the Performance [1:57]
**Transcript:** the actual data from my session. How is it recording? Oh, awesome, awesome.  Just me rolling. All right. So although I was just goofing around, you can see how incredible  the raw output is. No cleanup was done to this animation. Here, I've applied that raw data to  a few of the new 5.6 stock metacumans with some custom clothing from Polyphoria.  The facial expression's detail is absolutely insane. And again, this performance capture is  all in real time, and this looks as good as the previous offline version of metacuman animator.  Of course, I have rendered these shots out in movie render queue, but the animation for both  body and face is completely raw. Even the hands were extremely impressive. I didn't really  stress test them, and they won't get really complex interactions, but other than that,  they were some of the best hand captures I've ever seen. Certainly from a camera-based system,  and certainly in real time. Also, here's footage from Ken showing our crowd simulation plug-in

**Frame:** tutorials\frames\the-best-real-time-mocap-i-have-ever-seen---captury-captive-devices-and-metahuma\frame_002.jpg

### OverCrowd Integration [3:05]
**Transcript:** overcrowd using the same performance capture data and the new 5.6 metacumans.  So notice the cloth physics appearing on the guy with the blue and white tunic as Ken scrubs  through the sequencer switching from vats to blueprint actors with cloth simulation.  So there's like a pop there. We're still refining that transition, but you get the idea that  is an extremely useful feature and a very powerful core feature of overcrowd.  And if you're interested in trying out overcrowd, you can actually pick it up now on Patreon for  a reduced price while it's still in beta, and you'll get it on fabs for free when it's fully released.  All right, let's do some quick numbers. The capture live setup with 10 cameras that you see in this

**Frame:** tutorials\frames\the-best-real-time-mocap-i-have-ever-seen---captury-captive-devices-and-metahuma\frame_003.jpg

### Cost and Tech Specs [3:50]
**Transcript:** video runs about $50,000 total, including hardware. The software itself is 24,000,  with an annual $7,000 renewal. So obviously this is a studio solution, but it really might not be  that far out of reach for some indie creators if you were a real power user. The core HMC facial rig  by captive devices is about $30,000, using a 4K global shutter camera, dual LEDs, built-in timecode  sync, and is fully integrated with metacumans animator at 60 frames per second. The battery lasts  six hours comfortably for full day shoots. So real-time performance capture has been around for a while

**Frame:** tutorials\frames\the-best-real-time-mocap-i-have-ever-seen---captury-captive-devices-and-metahuma\frame_004.jpg

### Significance [4:36]
**Transcript:** with optical systems like Vidcon or suits like Xsense, but having it works seamlessly using just  cameras with no markers, no calibration, and wearing my normal clothes feels revolutionary.  The raw MoCAP turned out very usable, honestly better than some of my polished capture sessions.  So this instant feedback allows actors and filmmakers to fine tune expressions and emotional beats,  and you can use virtual cameras on an iPad, and you could really just crank out shots or scenes all day.  And honestly having a giant screen nearby to like look at my performance was way better than  just being in an empty room with cameras. Thanks again to the Capture Captive Devices and

**Frame:** tutorials\frames\the-best-real-time-mocap-i-have-ever-seen---captury-captive-devices-and-metahuma\frame_005.jpg

### 05:48 Outro [5:24]
**Transcript:** Metacumans teams for letting me demo this incredible tech. If you're working with metacumans or  any characters in Unreal Engine, this workflow is a truly magical experience. So if you found  anything useful or entertaining, please consider leaving a like and subscribing. All right, thanks for  watching. Peace.

**Frame:** tutorials\frames\the-best-real-time-mocap-i-have-ever-seen---captury-captive-devices-and-metahuma\frame_006.jpg


---

## Structured Notes

### Core Technique
Real-time markerless full-body + face performance capture streamed directly into Unreal Engine 5.6 using Captury CaptureLive (10 AI machine vision cameras, ~$50K system) for body and the Captive Devices Core HMC lightweight monocular facial rig ($30K) — no suits, no markers, no depth sensors — with raw uncleaned output applied to new UE 5.6 MetaHumans and rendered via Movie Render Queue, showcased at Unreal Fest.

### Summary
Charlie Driscoll reports from Unreal Fest where he demoed the Captury CaptureLive + Captive Devices Core HMC system — a fully markerless, real-time performance capture setup (body and face) streaming directly into Unreal Engine 5.6 onto MetaHumans. No suits, no markers, no depth sensors. The body system uses 10 AI machine-vision cameras; the face rig is a lightweight monocular camera head mount weighing almost nothing. Output is real-time on a large monitor providing immediate feedback to performers. Raw uncleaned animation is applied to UE 5.6 stock MetaHumans with Polyphoria clothing and rendered with Movie Render Queue. Also briefly shown: OverCrowd integration with the same performance data for crowd simulation, including VAT-to-blueprint-actor cloth physics transition. Cost breakdown: CaptureLive ~$50K total hardware + $24K software + $7K/year renewal; Core HMC ~$30K.

### Key Steps
1. Set up Captury CaptureLive system (10 AI machine vision cameras, ~$50K total); configure for performer tracking in volume.
2. Performer wears Captive Devices Core HMC lightweight facial rig (monocular 4K camera, dual LEDs, built-in timecode sync, 60fps, 6hr battery).
3. System streams real-time body + face animation directly into Unreal Engine 5.6 onto MetaHumans — no processing delay.
4. Use large monitor nearby for immediate performance feedback; iterate on expressions and emotional beats in real time.
5. Raw data applied to UE 5.6 stock MetaHumans with Polyphoria custom clothing; render via Movie Render Queue.
6. (Optional) Feed same performance capture data into OverCrowd for crowd simulation with VAT/cloth-physics blueprint actor swapping.

### UE Systems / Blueprints / Settings
- Captury CaptureLive (10 AI machine vision cameras; markerless body + finger tracking; real-time streaming to UE; ~$50K hardware + $24K software + $7K/year renewal)
- Captive Devices Core HMC facial rig (monocular 4K global shutter camera, dual LEDs, timecode sync, 60fps, 6hr battery, integrated with MetaHuman Animator; ~$30K)
- MetaHuman Animator (face animation, real-time offline version quality)
- UE 5.6 stock MetaHumans (new 5.6 characters with cloth physics)
- Movie Render Queue (final render output)
- OverCrowd plugin (crowd simulation using same performance data; VAT → blueprint actor cloth physics swap demo)
- Polyphoria clothing (MetaHuman costume)

### Difficulty
Advanced

### UE Version
5.6

### Tags
mocap, real-time-mocap, captury, captive-devices, metahuman-animator, overcrowd, markerless, performance-capture, unreal-fest, ue5

---

## Related Entries
- `how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-.md` — OverCrowd tutorial referenced in this video's crowd sim demo
- `how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng.md` — Move.AI Pro pipeline for comparison (the non-real-time alternative)
- `cinematic-motion-capture-with-move-one-and-metahuman-animator---unreal-engine-54.md` — budget version of the same performance capture goal
