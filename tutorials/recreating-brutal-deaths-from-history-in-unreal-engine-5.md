---
title: Recreating BRUTAL Deaths from History in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=2t3c1KJbBe8
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.x"
tags: [production-breakdown, cinematics, metahuman, move-pro, overcrowd, niagara, sequencer, historical-drama, client-work, mocap, metahuman-animator, voice-ai, ue5]
extraction_status: complete
frames_dir: tutorials/frames/recreating-brutal-deaths-from-history-in-unreal-engine-5/
frame_count: 9
---

# Recreating BRUTAL Deaths from History in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=2t3c1KJbBe8)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 6m49s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Building historical reenactments in Unreal [0:00]
**Transcript:** I've always wondered how Unreal Engine and Metihuman filmmaking would hold up if they were used to create the dramatic reenactments you see in big epic historical documentaries.  So, needless to say, I was extremely interested when a client reached out to me to create exactly that.  The project focused on one of the most brutal deaths in Roman history, the execution of Emperor Valerian by pouring molten gold down his throat.  And because this moment takes place at the height of Rome's conflict with the Persian Empire under King Shaper, the story demanded scale, drama, and a lot of brutal action.  The challenge was to rebuild the entire reenactment inside Unreal Engine and see how cinematic we could make it in just one month.

**Frame:** tutorials\frames\recreating-brutal-deaths-from-history-in-unreal-engine-5\frame_000.jpg

### Collaborating with Sharp Entertainment [0:43]
**Transcript:** I was contacted by Sharp Entertainment, the team behind Doomsday Preppers, 90 Day Fiance, and some of the biggest unscripted shows on TV.  They were developing a proof of concept for a new series called Die Like a Legend, which mixes narration, expert interviews, and stylized reenactments.  Each episode covers a different badass moment in history through the lens of one epic death.  What he does not yet know is that he will soon die one of the most horrific deaths of all time.  So they had actually already shot their reenactments on a green screen stage, so those scenes served as a roadmap for my Unreal Engine animation.  And because of the time constraints, Sharp let me mostly do my own thing and apply my own style and direction to the performances and cinematography, knowing I had a well-defined story and structure to work within.  The Larian's Army was sickened by a plague, immensely high fever, diarrhea, and post-rolls on the skin leading to death.

**Frame:** tutorials\frames\recreating-brutal-deaths-from-history-in-unreal-engine-5\frame_001.jpg

### Adding dialogue and facial capture [1:49]
**Transcript:** The first week was mostly pre-production, and that's when we made the decision to add dialogue.  I'm still Caesar. Let me go, and you can have all the gold in law.  The green screen versions had no spoken lines, but since MetaHuman Animator does such a good job capturing facial performances, and since I'd be using 11 labs to morph my voice into multiple characters,  giving Valarian and Shaper actual dialogue was a great way to add production value and emotional beats, even while working with a single performer.  Take it, and let's end this. Gold is what old men offer when they can no longer raise a sword.

**Frame:** tutorials\frames\recreating-brutal-deaths-from-history-in-unreal-engine-5\frame_002.jpg

### Environments and wardrobe assets [2:33]
**Transcript:** Now, one cornerstone of a great historical drama is always the sets and the wardrobes, and so another big part of pre-production was finding high quality environments and clothing assets.  When you're working alone, great environments can be a huge shortcut to making your scene look more professional, especially if they are already lit well.  Of course, you will likely end up tweaking the lighting, but it shows the environment artist at least had lighting in mind when they created it.  And Valarian's Villa is a perfect example. I found it on Fab, switched the sun to Moonlight for an edge light, and added a few flickering point lights near the lamps and torches.  Of course, daytime exterior scenes are great for speed, since you can really make everything work by adjusting the angle of the sun from shot to shot.  Wardrobes followed the same philosophy. Now, there are very few Roman outfits made natively for MetaHumans, surprisingly, but I had access to Polyphoria's medieval Oriental Armor pack, and it was a great fit for the Persian characters.  The craftsmanship is gorgeous on this armor, a lot of which I used totally out of historical context, but proof of concept.  For the Romans,...

**Frame:** tutorials\frames\recreating-brutal-deaths-from-history-in-unreal-engine-5\frame_003.jpg

### Full-performance capture with Move Pro [3:52]
**Transcript:** Once the world and characters were set, I moved into performance capture. For the body animation, I used MovePro, the Extremely Robust Multicam solution from MoveAI, which uses 6 GoPro Tens recording at 4K60FPS.  For the face, I used an iPhone 13 and a Rococo head rig.  I performed Valarian, Shaper, the Guards, the Mobs, everyone. Most of the swordfighting came from Mocap I Shot here in my studio with two stuntmen.  And those animations are actually available on Fab if you want to use them. They drop straight onto two MetaHumans in Sequencer, which let me build super intense action scenes incredibly quickly.  And this story is violent, so I leaned into that energy every chance I got. After capture, everything went into Unreal Engine.  Once the scenes were assembled, I finally moved into cinematography, and this is the most fun part.

**Frame:** tutorials\frames\recreating-brutal-deaths-from-history-in-unreal-engine-5\frame_004.jpg

### Cinematography in Unreal Engine 5 [4:57]
**Transcript:** Some of the shots were planned, but some of the best ones came from just exploring the scene once it was built.  Crowds were crucial for scale, and that's where my Overcrowd plugin became especially handy.  I was actually using an early internal build and wasn't using any advanced crowd behavior, but it was still perfect for filling scenes with Persian warriors, Roman formations, Angry Mobs, and background fighters.

**Frame:** tutorials\frames\recreating-brutal-deaths-from-history-in-unreal-engine-5\frame_005.jpg

### Using OverCrowd for large battles [5:23]
**Transcript:** I used Overcrowd in almost every scene to quickly add background characters for more production value.  And if you're interested in adding massive crowds to your movies or games, you can pick it up now on Fab, link in the description.  And finally onto the molten gold execution, which was the most intense moment in the project.

**Frame:** tutorials\frames\recreating-brutal-deaths-from-history-in-unreal-engine-5\frame_006.jpg

### Recreating the execution scene [5:43]
**Transcript:** You were, Cesar. Now you are my spectra.  I used Olympic meshes for the boiling gold in the Crucible, and an Niagara waterfall effect for the stream pouring down Valarians throughout.  Combined with the lighting, the smoke, and the metahuman performance, the scene came together in a way that felt brutal and cinematic, and it was just what I was going for. It was perfect.

**Frame:** tutorials\frames\recreating-brutal-deaths-from-history-in-unreal-engine-5\frame_007.jpg

### Final thoughts and call to action [6:14]
**Transcript:** Of course, a massive thank you to Sharp Entertainment. They have the completed proof of concept on their YouTube channel, so go check it out. It's a ton of fun.  If you could see yourself watching a show like this on YouTube or elsewhere, make sure to like and subscribe to their channel so we can keep making more.  Let them know in their comments what famous deaths from history you would like to see on the show.  And if you want more Unreal Engine filmmaking content, mocap breakdowns, or behind the scenes videos like this, please like and subscribe.  I'm Charlie, and I will see you in the next one.

**Frame:** tutorials\frames\recreating-brutal-deaths-from-history-in-unreal-engine-5\frame_008.jpg


---

## Structured Notes

### Core Technique
Full solo UE5 historical drama production pipeline for a real client (Sharp Entertainment "Die Like a Legend"): FAB environment + wardrobe assets → Move Pro 6-cam body mocap + iPhone face cap + MetaHuman Animator → 11 Labs voice morphing → OverCrowd crowds → Niagara waterfall VFX → Sequencer cinematography. One-month turnaround.

### Summary
Production breakdown of Charlie Driscoll's client project for Sharp Entertainment (Doomsday Preppers, 90 Day Fiance producers) — a proof-of-concept for "Die Like a Legend," an historical drama series recreating famous deaths in UE5. The project (Emperor Valerian vs. Persian King Shapur) was completed solo in one month. Key workflow decisions: source pre-lit FAB environments and modify lighting (sun angle + flickering point lights), use FAB wardrobe packs (Polyphoria Oriental Armor for Persians), Move Pro 6-cam 4K60 for body + Rococo head rig + iPhone for face, MetaHuman Animator for facial performance, 11 Labs to morph one performer's voice into multiple characters, pre-made FAB sword fighting mocap packs for action scenes, OverCrowd for crowd/army fills, Niagara waterfall + custom mesh crucible for molten gold VFX.

### Key Steps
1. **Pre-production**: source and evaluate FAB environments that are already well-lit (shortcuts production time); plan character lineup and voice strategy
2. **Environment lighting**: take FAB environment → switch Directional Light to moonlight for edge lighting; add flickering Point Lights near practical lamp/torch actors; lean on sun angle for daytime exterior shots
3. **Wardrobe**: FAB wardrobe packs — Polyphoria Medieval Oriental Armor (Persians); adapt period assets out of strict historical accuracy for visual quality
4. **Body mocap**: Move Pro (6 GoPro 10s, 4K60fps); solo performer plays all characters (Valerian, Shapur, guards, mobs)
5. **Face cap**: iPhone 13 + Rococo head rig → process in MetaHuman Animator
6. **Voice**: 11 Labs voice morphing → one performer produces multiple character voices
7. **Pre-made action animations**: use FAB 2-actor MetaHuman sword fighting animation pack (drag-drop onto two MetaHumans in Sequencer)
8. **Crowds**: OverCrowd plugin for Persian warriors, Roman formations, angry mobs, background fighters
9. **Molten gold VFX**: custom mesh crucible (Olympic meshes) + **Niagara waterfall effect** for molten gold stream pouring down throat + complementary lighting and smoke
10. **Cinematography**: explore assembled scene freely in Sequencer; some of the best shots discovered by wandering the built environment

### UE Systems / Blueprints / Settings
- **Sequencer** — full scene assembly, animation, cinematography, 2-actor animation drop-in
- **MetaHuman Animator** — facial performance capture from iPhone 13 + Rococo head rig
- **OverCrowd plugin** (FAB) — crowd/army fills; used without advanced behavior features
- **Niagara** — waterfall effect repurposed as molten gold stream
- **Directional Light** — Ctrl+L sun angle control, moonlight for edge lighting
- **Point Lights** — flickering practicals near torches/lamps (Light Function or keyframe-animated intensity)
- **FAB assets** — pre-lit environments, Polyphoria armor packs, 2-actor sword fight mocap packs

### Difficulty
Advanced (full production pipeline; client work; solo 1-month turnaround)

### UE Version
UE5 (MetaHuman Animator, OverCrowd, FAB marketplace)

### Tags
production-breakdown, cinematics, metahuman, move-pro, overcrowd, niagara, sequencer, historical-drama, client-work, mocap, metahuman-animator, voice-ai, 11-labs, ue5

---

## Related Entries
- Other Charlie Driscoll tutorials (Move.AI, OverCrowd, mocap pipeline)
- Move Pro mocap tutorials
- OverCrowd crowd simulation tutorials
- Niagara VFX documentation
