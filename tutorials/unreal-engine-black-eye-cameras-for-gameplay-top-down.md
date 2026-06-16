---
title: Unreal Engine Black Eye Cameras for Gameplay: Top Down
source: YouTube
url: https://www.youtube.com/watch?v=MFrmcgQHGJk
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v2
ue_version: "UE 5.3+"
tags: [blackeye-v2, camera, gameplay, top-down, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-for-gameplay-top-down/
frame_count: 4
---

# Unreal Engine Black Eye Cameras for Gameplay: Top Down

**Source:** [YouTube](https://www.youtube.com/watch?v=MFrmcgQHGJk)
**Author:** Black Eye Technologies
**Duration:** 3m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey everybody, this is Adam. Let's get into some gameplay cameras. In this video, we're gonna get into the top down gameplay cameras. It's so cool how Epic has created all these test scenes for us to deconstruct. Let's get into the top down one. Have you ever noticed? Top down, first person, third person. Video game genres. Our camera descriptions. The Delta between a good project and a great one is often the camera. Okay, let's get into it. So here's the camera that's in there and it's great. Stampin, it's following, but you can see without much look ahead, the character can get pretty close to the edge of the screen. So what we're gonna do is we're gonna show you how quickly you can do some velocity look ahead stuff on the black eye. So let's get some black eye mode out into the scene. So look at this. This is where we're gonna get to. You're running, but the camera is giving you some leading composition. You can see the center of the screen is in front of the character. But as you go slower, it comes back and as you go faster, it goes forward. When you've got powerful camera controls like this, you can experiment, you can iterate, you can try out ideas like look at this. We got ...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-for-gameplay-top-down\frame_000.jpg


---

## Structured Notes

### Core Technique
Top-down gameplay camera with velocity-based look-ahead using Black Eye Cameras: camera composition leads in the direction of movement, scales with speed, and springs back to center when the character slows.

### Summary
3.5-minute tutorial showing how to upgrade Epic's built-in top-down template camera with Black Eye's velocity look-ahead system. Drop in a Black Eye camera, activate it, and the camera automatically shifts its framing so the character leads toward the center-ahead of the screen proportionally to movement speed. Demonstrates rapid iteration via Save-in-Play for dialing in the look-ahead feel and spring-back.

### Key Steps
1. **Open Epic's top-down template scene** — note the default camera lacks look-ahead; character can drift to screen edge.
2. **Drop a Black Eye Orbit Camera into the scene** — set Auto-Activate on the player.
3. **Enable velocity look-ahead** — in the camera settings, enable the look-ahead option; this offsets the composition target in the velocity direction.
4. **Tune look-ahead scale** — controls how far ahead the composition leads at max speed vs. idle (center frame).
5. **Spring-back** — when character decelerates, composition drifts back to center using dampening. Tune the return speed.
6. **Iterate with Save-in-Play** — enable the Save-and-Play toggle; adjust look-ahead amount and spring feel while the game runs.
7. **Experiment with extreme values** — e.g., push look-ahead far for high-speed feel; pull back for slower tactical games.

### UE Systems / Blueprints / Settings
- **Velocity look-ahead** — Black Eye orbit camera setting; offsets composition target proportionally to velocity vector
- **Look-ahead scale** — magnitude of the composition offset at full speed
- **Return dampening** — spring speed when velocity drops (spring-back to centered composition)
- **Save-and-Play** — live iteration while PIE is running
- **Epic Top-Down Template** — `TopDown` map; uses a CameraActor spring arm by default; Black Eye replaces it

### Difficulty
Beginner

### UE Version
UE 5.3+ (Black Eye v2; Epic top-down template shown)

### Tags
`#blackeye-v2` `#camera` `#gameplay` `#top-down` `#beginner`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-v2-start-here-tutorial]] — full v2 system; gameplay camera section covers trigger-based camera switching
- [[unreal-engine-black-eye-cameras-2-person-combat-side-camera-tutorial]] — another gameplay camera archetype (side camera)
