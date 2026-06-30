---
title: Move.AI and Unreal Engine 5 Metahuman Short Film - GIGANTIC JOE
source: YouTube
url: https://www.youtube.com/watch?v=I3GzRdnFEIw
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-23
ue_version: "UE5"
tags: [metahuman, move-ai, mocap, short-film, virtual-production, metahuman-animator, eleven-labs, scale, indie-studio, cinematics]
extraction_status: complete
frames_dir: tutorials/frames/moveai-and-unreal-engine-5-metahuman-short-film---gigantic-joe/
frame_count: 2
---

# Move.AI and Unreal Engine 5 Metahuman Short Film - GIGANTIC JOE

**Source:** [YouTube](https://www.youtube.com/watch?v=I3GzRdnFEIw)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 5m5s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en stick around to see some behind the scenes at the [Music] end Marvin Marvin come in are you seeing this yep I got visual looks like he got you came from he looks huge I think that's why they call him gigantic Joe yeah thanks figured that part out I didn't know they made him this big he's been gentically altered to serve a specific purpose just like the rest of us he's probably just intelligent enough to do his job hey what are you doing the plan was to leave the wa on the [Music] floor Mother of [Applause] God you're are not alow why come I know I'm looking for you I have something important to discuss why see Jo what what I know what they've done to you and to others like you it's wrong deeply wrong wrong you say here we work we survive this life what else exists just surviving isn't living Joe they've made you intelligent capable of so much more just to use you as a tool intelligence they a gift I say curse see much change little but it doesn't have to be like this together we can fight and you can be free free they're strong we just tools I'll fight I'll win why you help you show him the P show him what you brought him because I r you this okay uh never mind mind that was a stupid idea look I see you Joe not just your strength but your wisdom there's so much more that you could teach us if only we listen not all humans are the same show me these others need see more no more understand more [Music] oh boy hold on to your butts all right thanks for watching when you combine Unreal Engine 5 with a suitless motion capture system like move Ai and voice morphing technology like 11 Labs the amount of Leverage that an indie Studio or even just one person can get from these tools in a few days is mind-blowing the quality of these custom metahumans and metahuman animator make it so it really feels like I'm just puppeting these characters with my performance and once you get over the initial technical hurdles of the software and the pipeline it becomes very intuitive to create films in this way so what we're trying to do with this channel is to create short films and serialized content and to learn something new each time or play with some element that this medium en aables more easily than if we were to do it practically in this case the scene is fairly simple it's just three characters talking what we get out of it is scaling up one of the characters to be gigantic and now we get to play with scale in a way you just don't really get to in other mediums as a cinematographer who shoots mostly commercials and documentaries I don't often get to frame up and light a giant talking Sasquatch dude so follow along for more in-depth breakdowns on this film and others in the very near future all right catch you in the next one

**Frame:** tutorials\frames\moveai-and-unreal-engine-5-metahuman-short-film---gigantic-joe\frame_000.jpg


---

## Structured Notes

### Core Technique
Move.AI (suitless markerless mocap) + MetaHuman Animator (face) + ElevenLabs (AI voice) + UE5 MetaHuman scale manipulation — three-character dialogue scene where one character is scaled to giant size. Demonstrates creative use of UE5's real-time scale flexibility (a feature impractical in live-action production). Primarily a short film showcase with brief production commentary.

### Summary
5-minute Charlie Driscoll short film "Gigantic Joe" — a sci-fi/fantasy dialogue scene between two normal-sized characters and one gigantic genetically-altered character. Minimal technical instruction (mostly the film itself). Post-film commentary confirms stack: UE5 + Move.AI (suitless mocap) + ElevenLabs voice morphing + MetaHuman Animator. Author notes that after initial technical hurdles the pipeline becomes intuitive; key advantage is "puppeting" characters with your own performance via MetaHuman Animator. Creative learning goal: playing with scale (giant character framing/lighting) — something impractical in live action. One-person or small indie studio production; made in a few days.

### Key Steps
- Source/create custom MetaHumans (includes a giant-scaled version)
- Move.AI capture for body performance → import animation to UE5
- MetaHuman Animator for facial capture (driven by performer's own performance)
- ElevenLabs for AI voice morphing to give giant character a distinctive voice
- Scale one MetaHuman character to giant size in UE5 (standard Actor Scale property)
- Film the three-character dialogue scene in Sequencer with appropriate camera framing for scale contrast

### UE Systems / Blueprints / Settings
- **Move.AI** — markerless suitless mocap system; body capture; no suit required for performers
- **MetaHuman Animator** — facial capture using performer's own facial expressions; driven via Live Link
- **MetaHuman scaling** — scale Actor Transform to make MetaHuman giant; UE5 handles lighting/shadow/physics at any scale; useful for characters impractical to do in live action
- **ElevenLabs** — AI voice morphing/synthesis; used to create distinct character voice separate from performer's real voice
- **UE5 real-time lighting** — lighting a giant character requires no special workflow; Lumen handles global illumination automatically at any character scale

### Difficulty
Intermediate-Advanced. Requires Move.AI hardware and familiarity with MetaHuman Animator pipeline. The technical stack (Move.AI + MetaHuman Animator + ElevenLabs) involves multiple software integrations. Content is mostly a film showcase rather than a step-by-step tutorial.

### UE Version
UE5 (no specific minor version; MetaHuman Animator + Move.AI ecosystem)

### Tags
metahuman, move-ai, mocap, short-film, virtual-production, metahuman-animator, eleven-labs, scale, indie-studio, cinematics

---

## Related Entries
- `motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma.md` — Charlie Driscoll Move.AI sword fight breakdown (more technical detail)
- `moveai-and-unreal-engine-5-metahuman-cinematic---hacker.md` — Charlie Driscoll Move.AI + MetaHuman Animator cinematic (same pipeline, more breakdown)
- `metahuman-realtime-animator-best-practices-unreal-engine-animation-hub.md` — MetaHuman Animator webcam best practices; FPS/exposure settings
- `metahumans-in-unreal-engine.md` — MetaHuman Blueprint structure, LODs, Control Rig animation
