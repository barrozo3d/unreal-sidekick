---
title: Unreal Engine Black Eye Cameras: Car camera INTRO
source: YouTube
url: https://www.youtube.com/watch?v=Wh-QAH49C70
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v2
ue_version: "UE 5.3+"
tags: [blackeye-v2, camera, gameplay, cinematics, vehicles, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-car-camera-intro/
frame_count: 4
---

# Unreal Engine Black Eye Cameras: Car camera INTRO

**Source:** [YouTube](https://www.youtube.com/watch?v=Wh-QAH49C70)
**Author:** Black Eye Technologies
**Duration:** 1m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey, this is Adam. We just released a new Black Eye tutorial video for driving cameras. So for gameplay, look at this. You can feel the weight of the car. It's not stuck to the middle of the screen. It's moving. Like, it's not 1996 anymore. Having a car stuck to the middle of the screen, you can't feel the physics. But with Black Eye, you can feel the acceleration, the deceleration, the braking, the how the tires are sticking to the road. And I'll show you how fast it is to set up. Controls for rotational damping, lots. Here's hardly any. So you can fine-tune your camera. We show you the effects of like variable pivot points. See how it's far in front. And as you slow down, it comes further back. You can create crazy drone cameras. And for cinematics shooting cars, I'll break down how you can do sweeping flybys, how you can lean into Black Eye's procedural composition, and easy off-sets, follow modes. So you can, in a handful of keyframes, create these beautiful sweeping buttery smooth sequences. Look at this. As the car speeds up, we're looking at the front of the car. As it slows down, we're looking at the whole thing. Magic. Come check it out. It's on YouTube. Thanks for watchin...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-car-camera-intro\frame_000.jpg


---

## Structured Notes

### Core Technique
Teaser/preview for Black Eye Cameras car camera tutorial: rotational damping, variable pivot points, speed-dependent composition framing, and cinematic sweeping flyby setups.

### Summary
1.5-minute promo for the full car camera tutorial. Previews four key features: rotational damping (camera feels the weight/physics of the car rather than being rigidly attached), variable pivot points (camera pivots shift as the car accelerates/decelerates — front of car at speed, whole car at rest), cinematic drone cameras, and Sequencer-based sweeping flybys using Black Eye's procedural composition with minimal keyframes. No technical steps shown — see [[unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics]] for full detail.

### Key Steps
N/A — preview only. Key concepts teased:
- **Rotational damping** — dial for how much the camera physically "feels" the car's acceleration/braking
- **Variable pivot point** — pivot position shifts from front-of-car (speed) to whole-car (slow)
- **Dynamic framing with speed** — at speed: front of car in frame; slowing: full car visible
- **Cinematic sweeping flybys** — procedural composition + few keyframes in Sequencer

### UE Systems / Blueprints / Settings
- **Rotational damping** — Black Eye camera param; controls physical lag in camera rotation relative to car
- **Variable pivot point** — pivot target shifts with speed (front vs. center of vehicle)
- **Black Eye procedural composition** — auto-frames based on subject + speed state
- **Sequencer integration** — buttery smooth sweeping shots with handful of keyframes

### Difficulty
Beginner (teaser; see full tutorial for intermediate content)

### UE Version
UE 5.3+ (Black Eye v2)

### Tags
`#blackeye-v2` `#camera` `#gameplay` `#cinematics` `#vehicles` `#beginner`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics]] — full car camera tutorial this video previews
- [[unreal-engine-black-eye-cameras-v2-start-here-tutorial]] — complete v2 system overview
