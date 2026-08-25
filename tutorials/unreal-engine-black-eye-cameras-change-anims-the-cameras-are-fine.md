---
title: Unreal Engine Black Eye Cameras: Change Anims (the cameras are fine)
source: YouTube
url: https://www.youtube.com/watch?v=VADulk2Gao4
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, animation, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-change-anims-the-cameras-are-fine/
frame_count: 4
---

# Unreal Engine Black Eye Cameras: Change Anims (the cameras are fine)

**Source:** [YouTube](https://www.youtube.com/watch?v=VADulk2Gao4)
**Author:** Black Eye Technologies
**Duration:** 1m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey, I'm Adam from Black Eye. Let's set up one camera and then change some animations. Okay, so we've got a camera looking at the zombie. We can just grab the camera and move it around. It's composing on his head. So the camera's always going to rotate to get the head. At that point on the screen, you can see here I'm moving that, so let's compose that up a little higher. There's a bit of damping there. We're gonna change how big that is on screen and the camera's gonna get that shot no matter what the player does. So you can see he's lumbering the camera's following his head to loosely, the camera's following his position. Now watch this, we're gonna change the animation. Now he's running. He's going super fast. We didn't touch the camera because the camera knows I want to be this far away. I want to look at his head. And you can set shots up, change things around. The shots are still gonna work. So let's just go back set it to the walk. It's all the same. Still composing, still following. Let all works, change animations, shots still work. And there it is, thanks for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-change-anims-the-cameras-are-fine\frame_000.jpg


---

## Structured Notes

### Core Technique
Black Eye cameras remain valid when character animations change — bone-based tracking (head + follow) is animation-agnostic, so the same camera setup works for walk, run, or any other animation.

### Summary
1-minute concept demo. Sets up a Black Eye camera following a character's position + looking at its head, then swaps the character's animation from walk to run. The camera adapts automatically to the new speed and movement rhythm because it tracks the head bone, not the animation clip. The camera is always oriented toward the head and maintains the desired follow distance — "the cameras are fine" when animations change.

### Key Steps
1. **Set up LookAt on head bone** — camera looks at the head, not actor bounds.
2. **Set Follow on character** — camera follows position with follow distance and loose damping.
3. **Adjust composition** — set screen size, composition placement while character is in default anim.
4. **Swap animation** — change the character's running animation to another (walk→run or vice versa).
5. **No camera changes needed** — camera still correctly frames the head and follows at the same distance. Works with any animation speed.

### UE Systems / Blueprints / Settings
- **LookAt (head bone)** — targets the head bone; animation-agnostic; always finds the bone regardless of animation playing
- **Follow** — world-space follow at set distance; adjusts to new movement speed automatically via damping
- **Follow damping** — loose/small value; camera follows loosely, giving it some weight

### Difficulty
Beginner

### UE Version
UE 5.x (Black Eye v1)

### Tags
`#blackeye-v1` `#camera` `#animation` `#beginner`

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:07] tutorials/frames/unreal-engine-black-eye-cameras-change-anims-the-cameras-are-fine/frame_000.jpg
- [0:21] tutorials/frames/unreal-engine-black-eye-cameras-change-anims-the-cameras-are-fine/frame_001.jpg
- [0:38] tutorials/frames/unreal-engine-black-eye-cameras-change-anims-the-cameras-are-fine/frame_002.jpg
- [0:55] tutorials/frames/unreal-engine-black-eye-cameras-change-anims-the-cameras-are-fine/frame_003.jpg

## Related Entries
- [[unreal-engine-black-eye-cameras-overview-tutorial]] — full LookAt + Follow system explanation
- [[unreal-engine-black-eye-cameras-look-around-tutorial]] — bone-targeting + damping in more detail
