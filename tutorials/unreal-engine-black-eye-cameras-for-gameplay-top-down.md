---
title: Unreal Engine Black Eye Cameras for Gameplay: Top Down
source: YouTube
url: https://www.youtube.com/watch?v=MFrmcgQHGJk
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "UE5"
tags: [black-eye-cameras, gameplay, top-down, velocity-lookahead, follow, damping, workflow, installation]
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
**Transcript:** Hey everybody, this is Adam. Let's get into some gameplay cameras. In this video, we're gonna get into the top down gameplay cameras. It's so cool how Epic has created all these test scenes for us to deconstruct. Let's get into the top down one. Have you ever noticed? Top down, first person, third person. Video game genres. Our camera descriptions. The Delta between a good project and a great one is often the camera. Okay, let's get into it. So here's the camera that's in there and it's great. Stampin, it's following, but you can see without much look ahead, the character can get pretty close to the edge of the screen. So what we're gonna do is we're gonna show you how quickly you can do some velocity look ahead stuff on the black eye. So let's get some black eye mode out into the scene. So look at this. This is where we're gonna get to. You're running, but the camera is giving you some leading composition. You can see the center of the screen is in front of the character. But as you go slower, it comes back and as you go faster, it goes forward. When you've got powerful camera controls like this, you can experiment, you can iterate, you can try out ideas like look at this. We got a camera up high. Nope, let's put it in closer. Let's have the orientation damping low. One number change. It's a completely different feel. You can iterate, you can tune, you can move fast. Okay, let's install this. We go to edit plugins, go to black eye, turn it on. You might have to reboot. Once you get it in, let's go to black eye, drop a camera in the scene and we're gonna set it to target player zero and look at and follow it. Click the look at and set it to world space center. And then click save and play so all your changes are saved and let's run it. The default camera position is not ideal. So let's punch in some offsets. We're gonna mimic the camera that was in there slightly just so you can see the differences with the look ahead, change the lens. Okay, and let's turn on the debug so you can see what's going on. Okay, so now we got a camera. Similar. Let's put a little follow damping on there. One is quite a bit. And we turned off the look damping so the camera's get the car, the caratress can be pinned to this end of the screen and the camera is going to follow dampened. You can still see we get kind of close to each the frame. You know, smooth and buttery in one regard, but it's not really a sophisticated camera yet. And it kind of packs up a little bit when you're on towards the camera. So let's fix that. So the look at, there's an offset. And if it's in local space, you can change where you're looking on the character. So we just pushed it forward a little bit. And that's cool sometimes, but look, it's a little C-Sick E-in. For some things that's amazing, but for this, we wanted to look at the character, but not always. So let's move it back. We're gonna use velocity look ahead. So I'm gonna just punch some numbers in there. Too much. Now when we start to move the velocity, we're looking ahead based on the character's velocity. Let's make these numbers a little less crazy. So you can see that dot, it moves forward. And the camera is now composing on the that velocity position that's ahead. But as you slow down, it comes back. You can see that look ahead. Now just to compare with the original camera with no look ahead, look at this, you're packing in. So just a couple of seconds under a minute, you've got velocity look ahead on a top-down camera. Good cameras make great projects. Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-for-gameplay-top-down\frame_000.jpg


---

## Structured Notes

### Core Technique
Black Eye top-down gameplay camera with **Velocity Look Ahead** — prevents character from packing to screen edge by moving the camera's look-at point forward in the direction of movement. Key insight: default Epic top-down camera has no look ahead; BEC adds it in under a minute.

### Summary
3m25s Adam (Black Eye Technologies) top-down gameplay camera tutorial using the Epic top-down example scene. Compares default Epic camera (character packs to screen edge) vs. BEC camera with velocity look ahead (camera leads composition ahead of character). Steps: install BEC plugin → drop camera → Target Player 0 → Look At (World Space Center) + Follow → Save and Play → tune offsets + lens. Add Follow Damping (1 = significant weight). Velocity Look Ahead: punch in values; debug shows dot moving forward as character speeds up, centering when slowing down. Look At Offset in local space to move look-at point forward (warning: can feel nausea-inducing at high offset). Works for any top-down genre; iterates in seconds.

### Key Steps
**Install:**
1. Edit → Plugins → search "Black Eye" → enable → restart UE

**Camera setup:**
2. Black Eye content folder → drag camera into scene
3. Details: **Auto Assign: Player 0** → binds to player character automatically at runtime
4. Enable **Look At** → set mode: **World Space Center** (looks at character's world-space center)
5. Enable **Follow** → camera follows character position
6. **Save and Play** → settings persist through PIE sessions; tune while game runs

**Tune:**
7. Default position not ideal → punch in offsets (X/Y/Z) and change lens to match scene scale
8. Enable **Debug** to see look-ahead dot and composition markers
9. Add **Follow Damping** (start ~1 = quite a bit of weight; adjust to feel)

**Velocity Look Ahead:**
10. Look At module → **Velocity Look Ahead**: set a value → look-at point moves forward in character's movement direction based on speed
11. As character speeds up: dot moves ahead of character (leading composition)
12. As character slows/stops: dot returns to character center
13. Tune the value: too much = nauseating camera swing; find the sweet spot

**Optional: Look At Offset (local space):**
14. Look At Offset in local space → push look-at forward of character center → alternative to velocity look ahead for simpler offset; can feel motion-sick-inducing at high values

### UE Systems / Blueprints / Settings
- **Auto Assign: Player 0** — automatically targets the player-controlled character; no manual subject assignment needed in gameplay
- **Look At: World Space Center** — targets the character's world-space center point for rotation; stable for top-down
- **Save and Play** — preserves BEC settings made during PIE back to the asset; enables live iteration
- **Follow Damping** — positional decoupling; adds weight/lag to camera follow; "1" is quite a lot; tune to game feel
- **Velocity Look Ahead** — moves look-at pivot forward proportional to character velocity; prevents character packing to screen edge; centers at rest; tune amount carefully
- **Look At Offset (local space)** — static offset of look-at point relative to subject; simpler than velocity look ahead but less responsive to speed changes
- **Debug mode** — shows look-ahead dot, composition markers, tracking lines in viewport during PIE

### Difficulty
Beginner. Plugin install + 5 settings = top-down camera in under 1 minute.

### UE Version
UE5 (Black Eye Cameras)

### Tags
black-eye-cameras, gameplay, top-down, velocity-lookahead, follow, damping, workflow, installation

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:20] tutorials/frames/unreal-engine-black-eye-cameras-for-gameplay-top-down/frame_000.jpg
- [1:02] tutorials/frames/unreal-engine-black-eye-cameras-for-gameplay-top-down/frame_001.jpg
- [1:53] tutorials/frames/unreal-engine-black-eye-cameras-for-gameplay-top-down/frame_002.jpg
- [2:44] tutorials/frames/unreal-engine-black-eye-cameras-for-gameplay-top-down/frame_003.jpg

## Related Entries
- `unreal-engine-black-eye-cameras-overview-tutorial.md` — full BEC plugin overview; all follow modes
- `unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics.md` — velocity look ahead used extensively for car cameras
- `unreal-engine-black-eye-cameras-start-here-tutorial.md` — BEC beginner intro
