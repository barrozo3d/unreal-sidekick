---
title: Unreal Engine | Black Eye Cameras: 2 person combat side camera tutorial
source: YouTube
url: https://www.youtube.com/watch?v=W4UZ4-vLxxw
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, gameplay, combat, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-2-person-combat-side-camera-tutorial/
frame_count: 4
---

# Unreal Engine | Black Eye Cameras: 2 person combat side camera tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=W4UZ4-vLxxw)
**Author:** Black Eye Technologies
**Duration:** 4m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey, I'm Adam from Black Eye. Let's do a quick two-character camera. That's going to attract them from the side. Ooh, looks like one guy's is on me. Alright, let's jump into it. So you're going to want to open your content browser. Make sure your engine plug-ins folders turned on so you can see everything. You can come down to the Black Eye folder. You can see we've got a bunch of cameras there. Grab the simple look at. Jump it in your scene. Now when you select that, you can see there's a few things going on. We've got a follow and a look at. We want to follow. So pick that. We're going to pick multiple subjects. I'll turn that on and let's add a subject. Here's ready for one. Now we get two. Open them up. You just get the eyedropper and you just pick them left person, right person, cameras now. In between those two, you can see the red line. That's the showing that we're tracking those two people. And you can punch in offset values or you can just grab the camera and move it to wherever you want. So we're going to do the latter. So we're just going to pick it up and move it back. Now you can see the camera is not looking at the character. So let's fix that. So open the look at. A...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-2-person-combat-side-camera-tutorial\frame_000.jpg


---

## Structured Notes

### Core Technique
2-person combat side camera using Black Eye: multi-subject Follow (two characters) + multi-subject LookAt with bone targeting + Dynamic FOV to keep both fighters framed from the side, like a fighting game camera.

### Summary
4-minute tutorial for a fighting-game-style side camera that follows two characters and keeps them both framed. Simple LookAt + Follow in multi-subject mode. Camera positions itself between and beside the two characters (side view). Dynamic FOV zooms to maintain both fighters in frame as they move apart or together. Dynamic compositional damping ensures smooth framing.

### Key Steps
1. **Drop Simple LookAt camera** — find under Plugins → Black Eye → Cameras.
2. **Set Follow, Multiple Subjects** — enable Follow, set mode to Multiple Subjects. Add two subjects, eyedropper left + right characters. Red line between them confirms tracking.
3. **Reposition camera** — grab camera, move it to the side of the action (perpendicular to the fight plane). Black Eye maintains the offset relationship.
4. **Set LookAt, Multiple Subjects** — same as Follow: add subjects array, pick both characters for LookAt.
5. **Enable Dynamic FOV** — keeps both fighters in frame as they approach or separate. Adjust screen size for desired framing margins.
6. **Tune composition damping** — adjust LookAt damping for smooth framing during fast movement.
7. **Test with movement** — fighters running toward/away from each other; camera maintains side framing and zooms accordingly.

### UE Systems / Blueprints / Settings
- **Simple LookAt** — Black Eye v1 camera type with Follow + LookAt modules
- **Multiple Subjects (Follow)** — camera position = average of two characters; Red debug line confirms tracking
- **Multiple Subjects (LookAt)** — camera rotates to compose on both characters
- **Dynamic FOV** — auto-zooms to keep both subjects in frame; set screen size for framing margins
- **Composition damping** — smooths camera framing during fast motion

### Difficulty
Beginner

### UE Version
UE 5.x (Black Eye v1)

### Tags
`#blackeye-v1` `#camera` `#gameplay` `#combat` `#beginner`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-overview-tutorial]] — Multiple Subjects section
- [[unreal-engine-black-eye-cameras-v2-start-here-tutorial]] — Cross Camera (v2) for two-subject relationship camera
- [[unreal-engine-black-eye-cameras-version-11-new-features-cross-camera]] — Cross Camera (v1.1) — alternative for two-subject framing with heading control
