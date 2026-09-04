---
title: Recreating BRUTAL Deaths from History in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=2t3c1KJbBe8
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-23
ue_version: "UE5"
tags: [metahuman, mocap, move-ai, eleven-labs, short-film, cinematics, crowds, fab, production-pipeline, virtual-production]
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
**Transcript:** I was contacted by Sharp Entertainment, the team behind Doomsday Preppers, 90 Day Fiance, and some of the biggest unscripted shows on TV.  They were developing a proof of concept for a new series called Die Like a Legend, which mixes narration, expert interviews, and stylized reenactments.  Each episode covers a different badass moment in history through the lens of one epic death.  What he does not yet know is that he will soon die one of the most horrific deaths of all time.  So they had actually already shot their reenactments on a green-screen stage, so those scenes served as a roadmap for my Unreal Engine animation.  And because of the time constraints, Sharp let me mostly do my own thing and apply my own style and direction to the performances and cinematography, knowing I had a well-defined story and structure to work within.  The Larian's Army was sickened by a plague, immensely high fever, diarrhea, and post-rolls on the skin leading to death.

**Frame:** tutorials\frames\recreating-brutal-deaths-from-history-in-unreal-engine-5\frame_001.jpg

### Adding dialogue and facial capture [1:49]
**Transcript:** The first week was mostly pre-production, and that's when we made the decision to add dialogue.  I'm still Caesar. Let me go, and you can have all the gold in law.  The green-screen versions had no spoken lines, but since MetaHuman Animator does such a good job capturing facial performances, and since I'd be using 11 labs to morph my voice into multiple characters,  giving Valarian and Shaper actual dialogue was a great way to add production value and emotional beats, even while working with a single performer.  Take it, and let's end this. Gold is what old men offer when they can no longer raise a sword.

**Frame:** tutorials\frames\recreating-brutal-deaths-from-history-in-unreal-engine-5\frame_002.jpg

### Environments and wardrobe assets [2:33]
**Transcript:** Now, one cornerstone of a great historical drama is always the sets and the wardrobes, and so another big part of pre-production was finding high quality environments and clothing assets.  When you're working alone, great environments can be a huge shortcut to making your scene look more professional, especially if they are already lit well.  Of course, you will likely end up tweaking the lighting, but it shows the environment artist at least had lighting in mind when they created it.  And Valarian's Villa is a perfect example. I found it on Fab, switched the sun to Moonlight for an edge light, and added a few flickering point lights near the lamps and torches.  Of course, daytime exterior scenes are great for speed, since you can really make everything work by adjusting the angle of the sun from shot to shot.  Wardrobes followed the same philosophy. Now, there are very few Roman outfits made natively for MetaHumans, surprisingly, but I had access to Polyphoria's medieval Oriental Armor pack, and it was a great fit for the Persian characters.  The craftsmanship is gorgeous on this armor, a lot of which I used totally out of historical context, but proof of concept.  For the Romans, I pulled armor from Fab and CG Trader, and used MetaTailer to fit everything onto the MetaHumans bodies.

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
End-to-end professional UE5 filmmaking pipeline for a commercial historical reenactment project (Sharp Entertainment "Die Like a Legend" proof of concept). Stack: Move Pro (6× GoPro 4K60 multicam markerless body mocap) + Rococo head rig (facial) + iPhone 13 MetaHuman Animator + ElevenLabs voice morphing + Fab environment/wardrobe assets + MetaTailor (clothing fit) + OverCrowd plugin (crowd) + Niagara (VFX).

### Summary
7-minute Charlie Driscoll production breakdown for a paid commercial client (Sharp Entertainment). Historical reenactment of Emperor Valerian's execution in Roman/Persian setting. Primarily a showcase + tool inventory. Key elements: (1) green-screen reference from client served as story roadmap; (2) dialogue added via MetaHuman Animator + ElevenLabs voice morph for multiple characters from single performer; (3) Fab environments (Valarian's Villa) + wardrobe from multiple sources (Polyphoria/Fab/CG Trader) fit with MetaTailor; (4) Move Pro (6-GoPro multicam) for body mocap, single performer playing all roles; (5) stuntman swordfighting mocap sold as Fab assets; (6) OverCrowd plugin for crowd background; (7) Olympic meshes (boiling crucible) + Niagara (gold stream) for execution VFX. Commercial-grade result achieved in 1 month solo.

### Key Steps
- **Pre-production** (week 1): green-screen reference from client → story structure + shot list
- **Decision: add dialogue** — MetaHuman Animator captures facial performance; ElevenLabs morphs voice for Valerian and Shapur from single performer's voice
- **Assets**:
  - Environments: Fab (Valerian's Villa) — switch Directional Light to moonlight for edge; add point lights at lamps/torches
  - Wardrobe: Polyphoria Medieval Oriental Armor Pack (Fab) for Persians; additional armor from Fab + CG Trader for Romans; **MetaTailor** to fit clothing to MetaHuman bodies
- **Performance capture**:
  - Body: **Move Pro** (MoveAI multicam solution) — 6× GoPro 10 at 4K60FPS; single performer plays all characters (Valarian, Shapur, guards, mob)
  - Face: iPhone 13 + **Rococo head rig** → MetaHuman Animator
  - Stuntmen: swordfighting mocap purchased separately; available on Fab; drops directly onto two MetaHumans in Sequencer
- **Crowd**: **OverCrowd plugin** (Charlie's own plugin, on Fab) — quick crowd background for battles (early internal build; basic placement, no advanced AI behavior)
- **VFX**: execution scene — Olympic meshes (boiling crucible); Niagara waterfall effect (molten gold stream); combined with lighting + smoke
- **Cinematography**: explored shots after scene assembly; camera placement informed by story beat and action energy

### UE Systems / Blueprints / Settings
- **Move Pro (MoveAI)** — 6× GoPro 10, 4K60FPS multicam markerless body mocap; more robust than single-cam Move.AI; professional-tier solution
- **Rococo head rig** — head-mounted iPhone for facial reference during body capture; synced with MetaHuman Animator
- **MetaHuman Animator** — facial capture from iPhone reference; lip sync driven by performer; ElevenLabs voice used post-facto
- **ElevenLabs** — AI voice morphing/cloning; single performer voice morphed into two distinct character voices (Valerian + Shapur)
- **MetaTailor** — third-party plugin; fits marketplace clothing assets to MetaHuman bodies without manual rigging
- **OverCrowd plugin** — Charlie Driscoll's crowd system plugin; fast background crowd placement (on Fab); used for Roman formations, Persian warriors, angry mobs, background fighters
- **Fab** — all environments, wardrobe, and mocap assets sourced here; includes stuntman swordfighting animation packs (two-MetaHuman Sequencer ready)
- **Olympic meshes** — used for boiling crucible (presumably third-party mesh pack from Fab)
- **Niagara** — waterfall effect for molten gold stream; combined with lighting/smoke for execution VFX

**Production context:**
- 1-month timeline, solo production (Charlie)
- Client: Sharp Entertainment (Doomsday Preppers, 90 Day Fiance creators)
- One performer played ALL roles (Valarian, Shapur, all guards, mob)
- Green screen reference from client served as story roadmap
- Completed POC on Sharp's YouTube channel

### Difficulty
Advanced (Production). This is a professional pipeline showcasing multiple integrated tools. Understanding the stack requires familiarity with MetaHuman, mocap, VFX, and Sequencer. No step-by-step technical instruction — production breakdown format.

### UE Version
UE5 (no specific minor version; MetaHuman Animator + Move Pro ecosystem)

### Tags
metahuman, mocap, move-ai, eleven-labs, short-film, cinematics, crowd, fab, production-pipeline, virtual-production

---

## Related Entries
- `moveai-and-unreal-engine-5-metahuman-short-film---gigantic-joe.md` — Charlie Driscoll; same pipeline (Move.AI + MetaHuman Animator + ElevenLabs); Gigantic Joe showcase
- `motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma.md` — Charlie Driscoll; Move.AI sword fight breakdown (more technical detail)
- `metahuman-realtime-animator-best-practices-unreal-engine-animation-hub.md` — MetaHuman Animator webcam best practices
- `new-unreal-engine-58-metahuman-crowd-plugin.md` — MetaHuman Crowd Plugin (alternative crowd solution for UE5.8)
