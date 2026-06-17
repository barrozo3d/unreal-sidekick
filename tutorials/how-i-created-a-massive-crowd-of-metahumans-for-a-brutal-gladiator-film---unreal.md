---
title: How I created a MASSIVE crowd of Metahumans for a BRUTAL Gladiator film - Unreal Engine 5, OverCrowd
source: YouTube
url: https://www.youtube.com/watch?v=y-6aiWvh_GY
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.x"
tags: [overcrowd, crowd-simulation, metahuman, mocap, move-ai, gladiator, battle-scene, vat, elevenlabs, ue5]
extraction_status: complete
frames_dir: tutorials/frames/how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal/
frame_count: 9
---

# How I created a MASSIVE crowd of Metahumans for a BRUTAL Gladiator film - Unreal Engine 5, OverCrowd

**Source:** [YouTube](https://www.youtube.com/watch?v=y-6aiWvh_GY)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 9m8s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In this video, I'll show you how I made this gladiator themed short film in just one week with Unreal Engine 5.  Using a powerful asset called Overcrowd, I was able to set these brutal combat sequences and detailed performances against an epic backdrop of thousands of modular characters with metahuman faces and facial animations.  But first, enjoy the film.

**Frame:** tutorials\frames\how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal\frame_000.jpg

### CINEMATIC [0:23]
**Transcript:** Look upon the glory before you.  This, this is the strength that is built out of blood and steel, forging men into weapons sharper than any blade.  Soon, all of our enemies will face the same fate, the barbarians of Germania, the rebels of his spaniard.  They will all bend knee or bleed into the sand like these slaves before us.  People love you, season.  And their eyes, you can do no wrong.  And it's sick as hell.  Empire cannot exist without subjugation.  Every province I conquer brings more slaves for your entertainment.  More warriors to die in the sand for your slaughter.  The Eagle standards will fly over land. You cannot even imagine.  Alright, thanks for watching.

**Frame:** tutorials\frames\how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal\frame_001.jpg

### Creating a massive crowd with OverCrowd [2:50]
**Transcript:** So, for this gladiator project, I teamed up with Kenneth McLean, the developer of Overcrowd, who's been building this incredibly powerful crowd simulation asset for Unreal Engine 5.  And full disclosure, I am now a partner in this asset and will be helping in its development moving forward.  So, for this scene specifically, I placed dozens of overcrowd instantiors around the stadium, each spawning roughly 300 modular crowd members.  Each instant ser lets you define exactly which characters, wardrobes, and animation sets spawn in each crowd section.  And once spawned, you can actually manually reposition individual crowd members, which is perfect for art directing or figuring out the exact composition of your shot.  Now, Overcrowd works similarly to the already powerful anima texture plugin by Epic, but it adds a lot of functionality.  Modular metahumans with facial animation, advanced vat animation sequencing, automatic LOD generation for optimization, precise art direction control, and dynamic mesh and ragdoll swapping capabilities.  Now, because Overcrowd is currently undergoing an overhaul in its UI and feature set, it's not available for sale right now.  But if you go to my bra...

**Frame:** tutorials\frames\how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal\frame_002.jpg

### Sword fighting choreography Mocap [4:41]
**Transcript:** Alright, let's dive into the Gladiator Pights themselves.  Every Sword Combat sequence here uses custom mocap animations I captured myself using Move AI's Markylist Multi-Camp system.  So these animations are actually part of a paired Sword Fighting animation pack I'm developing, which is specifically targeted to the metahumanskeleton and designed for cinematic use.  This pack was directly inspired by the Kung Fu Fighting animation set I showcased in one of my earlier videos, but this time around I wanted something focused on realistic Sword Combat that filmmakers and cinematic artists could easily drop into their projects.  So having these animations pre-made made it incredibly easy to block out my fight scenes in Sequencer.  For each Gladiator pair, I set up their animations in their own dedicated folder in the Sequencer, allowing me to slide the entire choreography sequences around on the timeline.  So if I needed to adjust what a pair was doing in the background of a different character shot, it was as simple as just shifting the animation group.  Plus, since some of these animations included longer choreographed sequences, I was able to easily get wide establishing shots of th...

**Frame:** tutorials\frames\how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal\frame_003.jpg

### High Quality Metahumans from 3D Scan Store [6:44]
**Transcript:** Alright, let's dive into the characters themselves.  So I decided to integrate some high quality heads from the 3D scan store into my MetaHumans.  So these heads come directly from real world 3D scans, and they feature insanely detailed 8K textures.  So up close, the skin details like pores, wrinkles, and blemishes just look ridiculously realistic, especially compared to standard MetaHumans.  Now, as for the performances themselves, I actually did all the acting myself using MOVE AI's MovePro Markerless Multicam System for capturing body animations and MetaHumans animator for facial capture.

**Frame:** tutorials\frames\how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal\frame_004.jpg

### Capturing Performances with Move.Ai and Metahuman Animator [7:14]
**Transcript:** I wore the same head rig from FaceMotionCapture.com that I've shown in some previous videos, and it's honestly one of the most affordable and effective options out there.  Costs only 100 bucks, which is pretty good considering what it's up against.  And then finally for the voices, I used 11 Labs Voice Changing Technology to morph the recorded audio.

**Frame:** tutorials\frames\how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal\frame_005.jpg

### Voice Morphing using Elevenlabs [7:46]
**Transcript:** This is the strength that has built our empire. Blood and steel. Forging men into weapons, sharper than any blade.

**Frame:** tutorials\frames\how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal\frame_006.jpg

### Zombie Tutorial Part 2 Update [8:03]
**Transcript:** So a lot of you are wondering about my Part 2 on my Zombie Tutorial. I promise it's coming soon, but actually Overcrowd, the CrowdSIM asset I'm using here, is highly relevant to that.  It basically has all the features you guys asked for after the first Zombie Tutorial.  And so I'll be using Overcrowd extensively in that upcoming Part 2, where we'll do some crazy stuff.  Like shooting the zombies, communicating between Niagara and the VATs to have more realistic animations and behavior, modular zombies, and much more.  Okay, thanks so much for watching. If you found any of this useful or entertaining, please consider leaving a like and subscribing.

**Frame:** tutorials\frames\how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal\frame_007.jpg

### Outro [8:39]
**Transcript:** If you want to chat about anything and everything on Real Engine filmmaking, come on by the Discord. There's a link in the description.  And if you want to see more cinematic scenes made in Unreal Engine and how I made them, check out any of the videos in the breakdowns playlist right here on this channel.  Alright, I'm Charlie and I will see you in the next one.

**Frame:** tutorials\frames\how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal\frame_008.jpg


---

## Structured Notes

### Core Technique
OverCrowd crowd simulation plugin fills a Roman gladiatorial stadium with thousands of modular MetaHuman characters (facial animations included), while Move.AI Pro multi-cam mocap and MetaHuman Animator drive the foreground gladiator combat sequences, creating a week-long production of a cinematic short film.

### Summary
Charlie Driscoll breaks down his gladiator-themed short film made in one week using Unreal Engine 5. The stadium crowd of thousands is powered by OverCrowd, a custom crowd simulation plugin he co-developed, which places modular MetaHuman characters (with facial animations) using population instantiators around the stadium. Foreground combat uses custom paired sword-fighting mocap animations captured with Move.AI's MovePro multi-cam system, developed as part of a planned animation pack. Performers use 3D Scan Store premium heads for photo-realistic skin detail, with all acting performed by Driscoll himself using a FaceMotionCapture.com head rig. ElevenLabs handles voice morphing for multiple characters.

### Key Steps
1. Set up OverCrowd instantiators around stadium; configure each instantiator with character/wardrobe/animation sets for crowd sections (~300 characters per instantiator).
2. Manually reposition individual crowd members for art-directed shots.
3. Capture paired sword-fighting choreography with Move.AI MovePro multi-cam system; apply animations in Sequencer organized by gladiator pair folder.
4. Import 3D Scan Store high-detail heads; integrate with MetaHuman (8K textures for realistic skin pores/wrinkles).
5. Capture performances with Move.AI body mocap + MetaHuman Animator face capture via FaceMotionCapture.com head rig.
6. Morph recorded dialogue audio using ElevenLabs voice changing.
7. Organize each gladiator pair's animation group in Sequencer folders for easy repositioning.

### UE Systems / Blueprints / Settings
- OverCrowd plugin (crowd simulation, modular MetaHuman characters, VAT animation, facial animation, LOD generation, mesh/ragdoll swapping)
- Move.AI MovePro multi-cam system (6 GoPros for body mocap)
- MetaHuman Animator (face capture, FaceMotionCapture.com head rig)
- Level Sequencer (animation groups by character pair, grouped for repositioning)
- 3D Scan Store heads (8K texture MetaHuman integration)
- ElevenLabs voice morphing
- Niagara / AnimToTexture (underlying VAT system powering OverCrowd)

### Difficulty
Intermediate

### UE Version
5.x

### Tags
overcrowd, crowd-simulation, metahuman, mocap, move-ai, gladiator, battle-scene, vat, elevenlabs, ue5

---

## Related Entries
- `how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-.md` — full tutorial on using OverCrowd plugin step by step
- `how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat.md` — manual Niagara + AnimToTexture zombie crowd tutorial (precursor approach)
- `motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma.md` — dedicated breakdown of the paired sword-fighting mocap capture process
