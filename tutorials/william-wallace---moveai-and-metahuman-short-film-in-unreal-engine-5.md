---
title: William Wallace - Move.AI and Metahuman short film in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=PYTu-rLyPro
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.x"
tags: [mocap, metahuman, move-ai, short-film, historical, performance-capture, elevenlabs, ue5]
extraction_status: complete
frames_dir: tutorials/frames/william-wallace---moveai-and-metahuman-short-film-in-unreal-engine-5/
frame_count: 4
---

# William Wallace - Move.AI and Metahuman short film in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=PYTu-rLyPro)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 1m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Sons of Scotland. I am William Wallace. William Wallace was seven feet tall. I am so at heart. Kills men by the hundreds. If you were here, you'd consume the English. Fireballs from his eyes. Bults of whiping from his eyes. But I am William Wallace. Nice sea before me. A whole army of my countrymen. Here, in defiance, tyranny, will you fight? Against that? No. We'll run. And you will live. Odd. Fight. And you may die. Run. And you'll live. Always to want. But bang in your beds. Many years from now. Would you be willing to train all the days from this day to that for one chance, just one chance, to come back here and kill our enemies? They may take our lives, but they will never take our freedom.

**Frame:** tutorials\frames\william-wallace---moveai-and-metahuman-short-film-in-unreal-engine-5\frame_000.jpg


---

## Structured Notes

### Core Technique
Short historical short film recreating William Wallace's famous "Freedom" speech using a custom MetaHuman in Unreal Engine 5, driven by Move.AI body mocap and MetaHuman Animator face capture — pure showcase film with virtually no technical narration in the transcript.

### Summary
"William Wallace" is a very short (1m25s) period CGI short film by Charlie Driscoll recreating the iconic Braveheart "Freedom" speech with a custom William Wallace MetaHuman in a medieval Scottish battlefield environment. The transcript contains only the film's Braveheart dialogue with no behind-the-scenes narration, making this a pure portfolio/showcase entry. The technical pipeline follows Driscoll's established approach: a custom period-appropriate MetaHuman character driven by Move.AI body capture and MetaHuman Animator face performance, assembled in Sequencer with environment assets and cinematic camera work. ElevenLabs voice morphing is likely used to give the character an appropriate Scottish accent. This entry demonstrates the channel's broader goal of creating cinematic short films using UE5 performance capture tools.

### Key Steps
1. Source or commission a William Wallace period-appropriate MetaHuman (Scottish warrior costume, facial features).
2. Capture actor performance delivering the speech using Move.AI body mocap.
3. Record face performance via MetaHuman Animator iPhone or lightweight head rig.
4. Apply ElevenLabs voice morphing for Scottish accent character voice.
5. Set up medieval Scottish battlefield environment in UE5 (Fab/Marketplace assets or Quixel).
6. Assemble in Sequencer with cinematic cameras; render via Movie Render Queue.

### UE Systems / Blueprints / Settings
- Move.AI body capture (single or multi-cam)
- MetaHuman Animator (face performance capture)
- Level Sequencer (animation + camera assembly)
- Custom period MetaHuman (William Wallace character)
- Environment assets (medieval Scottish battlefield)
- ElevenLabs (voice morphing for character-appropriate accent)
- Movie Render Queue (final render output)

### Difficulty
Intermediate

### UE Version
5.x

### Tags
mocap, metahuman, move-ai, short-film, historical, performance-capture, elevenlabs, ue5

---

## Related Entries
- `moveai-and-unreal-engine-5-metahuman-short-film---gigantic-joe.md` — comparable short film showcasing the Move.AI + MetaHuman pipeline as a creative vehicle
- `moveai-unreal-engine-54-motion-capture-short-film-using-custom-orc-metahumans---.md` — similar short-film format using custom historical/fantasy MetaHumans
- `cinematic-motion-capture-with-move-one-and-metahuman-animator---unreal-engine-54.md` — full beginner tutorial for the Move.AI + MetaHuman Animator pipeline used here
