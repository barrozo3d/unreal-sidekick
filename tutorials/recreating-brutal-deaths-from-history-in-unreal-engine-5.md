---
title: Recreating BRUTAL Deaths from History in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=2t3c1KJbBe8
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
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
