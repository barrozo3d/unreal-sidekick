---
title: Unreal Engine Black Eye Cameras: Version 1.1 New Features: Cross Camera
source: YouTube
url: https://www.youtube.com/watch?v=uUxE0gaOvnQ
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1.1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, cinematics, dialogue, beginner, intermediate]
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
**Transcript:** BlackI version 1.1 has some cool new features and this video is about one of them called the Crosscam. And this is a brand new camera. And what it does is it sets a relationship between a camera and two subjects. So if you look at these two people here, there's a ray between their palvuses and there's an angle heading in the camera goes at the end. And you've got controls over distance. Which you can see aggressively done here. And you've got controls over the height. And then you've got a control for the heading. So look at this. This guy picks up the other one. And the camera is always maintaining this heading between the two characters. You can change the heading, move it behind, and always keep that relationship. So here's a good example. Look at when the one guy pulls forward, the camera swings. So it always maintains that angle between those two objects. And those two objects can be anything. They can be bones on a character. They can be two different things. So look at this example. It's like a dialogue shot we're doing over the shoulder. Adjusting the look at to get the composition right. You can see it made one head have a larger bounding volume. Now this camera is always ...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-version-11-new-features-cross-camera\frame_000.jpg


---

## Structured Notes

### Core Technique
Black Eye v1.1 Cross Camera: a new camera type that positions itself based on the spatial relationship between two subjects (heading angle, distance, height), always maintaining its configured angle between them regardless of how they move.

### Summary
4.75-minute feature overview for the Cross Camera introduced in v1.1. The Cross Camera draws a conceptual ray between two subjects (e.g., their pelvises) and positions the camera at the end of that ray at a configurable heading angle, distance, and height. When one character moves or picks up the other, the camera swings to maintain the heading relationship. Ideal for dialogue, combat two-shots, and any scenario where you need a consistent spatial relationship between two moving targets. Subjects can be bones on a single character, two different actors, or any two scene objects.

### Key Steps
1. **Drop Cross Camera actor** — Black Eye v1.1+; new camera type in the plugin.
2. **Assign Subject Left and Subject Right** — pick two characters (or bones, or objects). A ray is established between their positions (defaulting to pelvis/root).
3. **Set heading** — the angle around the two-subject ray where the camera sits. Adjust to move camera behind, to the side, or for an over-the-shoulder position.
4. **Set camera height** — vertical offset of the camera from the midpoint between the two subjects.
5. **Set distance** — how far the camera sits along the heading from the midpoint.
6. **Configure LookAt** — for dialogue over-the-shoulder shots, set LookAt to one character's head bone. Adjust bounding volume on that head for correct framing.
7. **Dynamic behavior** — when one subject moves relative to the other (e.g., one pulls forward), the camera maintains the heading angle and swings accordingly. No keyframing needed for the tracking behavior.

### UE Systems / Blueprints / Settings
- **Cross Camera** — Black Eye v1.1+ camera type; establishes a 3D relationship between two subjects
- **Subject Left / Subject Right** — the two subjects; can be actors, bones, or any scene objects
- **Heading** — angle around the subject-pair axis where the camera positions (0 = beside, 180 = behind)
- **Camera Height** — vertical offset from subject midpoint
- **Distance** — camera distance along the heading from the subject midpoint
- **Bounding Volume / Bone targeting** — set LookAt to a specific bone (head) for over-the-shoulder framing

### Difficulty
Beginner / Intermediate

### UE Version
UE 5.x (Black Eye v1.1)

### Tags
`#blackeye-v1` `#camera` `#cinematics` `#dialogue` `#beginner` `#intermediate`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-start-here-tutorial]] — Cross Camera section in v1 START HERE
- [[unreal-engine-black-eye-cameras-v2-start-here-tutorial]] — v2 Cross Camera (updated; same concept)
- [[unreal-engine-black-eye-cameras-dynamic-dialog-intro]] — Dynamic Dialog (extends Cross Camera for multi-person variable dialogue)
- [[plugin-blackeye-versions]] — v1.1 changelog
