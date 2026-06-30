---
title: Unreal Engine Black Eye Cameras: Version 1.1 New Features: Cross Camera
source: YouTube
url: https://www.youtube.com/watch?v=uUxE0gaOvnQ
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "UE5"
tags: [black-eye-cameras, cross-camera, dialogue, over-the-shoulder, follow, look-at, damping, orientation-damping, location-damping, v1-1]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-version-11-new-features-cross-camera/
frame_count: 4
---

# Unreal Engine Black Eye Cameras: Version 1.1 New Features: Cross Camera

**Source:** [YouTube](https://www.youtube.com/watch?v=uUxE0gaOvnQ)
**Author:** Black Eye Technologies
**Duration:** 4m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** BlackI version 1.1 has some cool new features and this video is about one of them called the Crosscam. And this is a brand new camera. And what it does is it sets a relationship between a camera and two subjects. So if you look at these two people here, there's a ray between their palvuses and there's an angle heading in the camera goes at the end. And you've got controls over distance. Which you can see aggressively done here. And you've got controls over the height. And then you've got a control for the heading. So look at this. This guy picks up the other one. And the camera is always maintaining this heading between the two characters. You can change the heading, move it behind, and always keep that relationship. So here's a good example. Look at when the one guy pulls forward, the camera swings. So it always maintains that angle between those two objects. And those two objects can be anything. They can be bones on a character. They can be two different things. So look at this example. It's like a dialogue shot we're doing over the shoulder. Adjusting the look at to get the composition right. You can see it made one head have a larger bounding volume. Now this camera is always going to do an over the shoulder no matter what these two people do. And you can see if someone, the far guy pulls forward, the camera will swing behind. So you can set up dialogue shots where you're always getting the perfect amount of overlap. Okay, here's how to set it up. Go to place actor, drop a cross camera in the scene. There is. And you can see into the perpendicular follow. There's two subjects, one and two, A and B. So we're going to pick A, the left person, be the right person, and boom, automatically default to 90. So we're doing a perpendicular shot on the two. You can adjust the distance. You can adjust the height. You can see the composition is not great yet. We're going to fix that and here's the heading. Okay, so let's change it instead of off the root. We're going to do it off the pelvis. Just gets a little bit of a cleaner angle sometimes depending on how the character is animated. And let's fix our look at. So I'm going to add another look at subjects we're tracking too. So we're now composing on both. Let's do a little dynamic F OV. Let's adjust the size. And watch this. We spin the heading around in the distance. And we're just always going to get that shot. Let's frame a little bit here, move it in. And there's the heading. You can see we're spinning. And we're going to add a little bit of location damping. That's the damping of the camera. I'm going to talk about that a bit more. Here we go. We got a shot. Let's fix the look at pumping a little bit. The F OV damping needs to be a bit higher. Boom. It's always going to maintain that heading. It's following those two people. It's done. This is important. It's a little bit more complicated. So look at this. I've turned all the damping off. There's no orientation damping. There's no location damping. And look how brittle the camera is. It's like hard pin to the angle. Hard pin to positionally. And if we put in rotation damping, the camera is still positionally constrained. But the angular damping is there. So you can see it's rotating in a very goopy viscous manner. That's orientation damping. And they're decoupled from positional damping. And there's a lot of reasons for this. You'll see you need both. So let's fix that. Turn that damping down. You can see though the position is still locked. Just the angular damping is there. Okay. So now let's put in. Let's just make that a bit smaller. And let's add some location damping. One's a lot. So now you can see that little orange angle. That's the arm. Now we've got a damping between the camera and the arm. So you've got two. You've got a angular rotation damping. And then you've got a position damping, which is how the camera is being dampened to the end of that arm. So with both of these, you can create a lot of different behaviors. You can have a little bit of angular damping and a lot of positional damping or vice versa. Depending on what you're tracking and how much it's spinning around, you'll need both. It's a little bit of a balancing act though. So we're just going to dial in these numbers a little bit more. Less is more very often on damping, especially if it's active. Look at that. Worked pretty well. New black eye, 1.1. Thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-version-11-new-features-cross-camera\frame_000.jpg


---

## Structured Notes

### Core Technique
BEC v1.1 Cross Camera introduction. Creates a camera that maintains a fixed angular relationship (heading) between two subjects. A "ray" is drawn between the subjects' pelvis/root bones; camera sits at the end of the ray at a configurable heading and height. As either subject moves, the camera swings to maintain the heading angle — perfect for over-the-shoulder dialogue shots that work regardless of character world position. Key two-damping distinction: **Orientation Damping** (angular, how smoothly camera rotates) and **Location Damping** (positional, lag along the ray arm) are fully independent.

### Summary
4m46s BEC v1.1 Cross Camera feature reveal. Shows a camera locked to the angular relationship between two characters. Heading control: spin camera around both people; always maintains configured over-the-shoulder angle. Even when one character moves forward, the camera swings to maintain heading. Setup: Place → Cross Camera actor → Perpendicular Follow Subject A + B → heading/distance/height dials → Look At one or both subjects + Dynamic FOV. Two damping systems: Orientation Damping (angular rotation viscosity) + Location Damping (positional arm-end lag) — both needed, independently tunable. Less is more on damping for active shots.

### Key Steps
1. Place → Place Actors → search "Cross Camera" → drag into level
2. Select Cross Camera → Details: **Perpendicular Follow**: Subject A → eyedropper → left character; Subject B → eyedropper → right character
3. Camera auto-positions perpendicular to the two subjects (default heading = 90°)
4. Adjust **heading** dial → spin camera around both subjects (0° = front; 90° = side; 180° = back)
5. Adjust **distance** → camera moves closer or farther from subjects while maintaining heading
6. Adjust **height** → camera rises or lowers
7. Change Follow from root to **pelvis** bone → sometimes gives cleaner angle depending on character animation
8. Enable **Look At** → pick one character head bone → adjust bounding radius to head size → adjust Focus Distance Offset to compensate for bone being inside geometry
9. Optionally add second Look At subject for combined framing + Dynamic FOV
10. Add to Sequencer Camera Cuts track → cut between this and other cameras
11. Tune **Orientation Damping** (angular: how smoothly camera rotates when subjects move) → start low
12. Tune **Location Damping** (positional: lag at end of arm between camera and target position) → start low
13. Both damps needed: zero orientation = hard-pinned rotation (brittle on movement); zero location = hard-pinned position; combined = organic feel

### UE Systems / Blueprints / Settings
- **Cross Camera actor** — distinct from Look At/Follow camera; maintains heading angle between two subjects
- **Perpendicular Follow: Subject A/B** — two subject slots; "ray" drawn between them; camera at configurable end point
- **Heading** — angle of camera around the two-subject ray (0–360°); 90° = perpendicular; 180° = behind
- **Distance** — how far camera sits at end of ray
- **Height** — vertical offset of camera from ray midpoint
- **Orientation Damping** — angular viscosity: how smoothly camera rotates to follow subjects; zero = hard-pin rotation (rigid); high = very goopy rotation
- **Location Damping** — positional viscosity: lag between camera's target position and actual position; creates weight in following arm end; independent from orientation
- **Two damping systems** — critical distinction: you need BOTH; one controls rotation, other controls position; tune separately; "less is more for active shots"
- **Look At + bone targeting** — usual BEC look at on Cross Camera; set Focus Distance Offset to compensate for bone depth inside geometry
- **Bounding Radius** — cube size around targeted bone; affects how camera frames partial subjects

### Difficulty
Beginner to intermediate. Setup is fast; damping system requires understanding of two-component model.

### UE Version
UE5 (Black Eye Cameras v1.1+)

### Tags
black-eye-cameras, cross-camera, dialogue, over-the-shoulder, follow, look-at, damping, orientation-damping, location-damping, v1-1

---

## Related Entries
- `unreal-engine-black-eye-cameras-start-here-tutorial.md` — Cross Camera used in dialogue system context (full workflow)
- `unreal-engine-black-eye-cameras-overview-tutorial.md` — BEC overview including cross camera
- `unreal-engine-black-eye-cameras-v2-start-here-tutorial.md` — v2 Cross Camera usage for gameplay (Interesting Cube demo)
