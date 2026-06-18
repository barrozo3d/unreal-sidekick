---
title: MetaHuman Realtime Animator Best Practices | Unreal Engine Animation Hub
source: YouTube
url: https://www.youtube.com/watch?v=PgzSGQnWVcU
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["metahuman", "animation", "mocap", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/metahuman-realtime-animator-best-practices-unreal-engine-animation-hub/
frame_count: 4
---

# MetaHuman Realtime Animator Best Practices | Unreal Engine Animation Hub

**Source:** [YouTube](https://www.youtube.com/watch?v=PgzSGQnWVcU)
**Author:** Unreal Engine
**Duration:** 9m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome to Animation Hub. Today we're going to be looking at best practices for using a webcam for metahuman animator. So before we can use the metahuman animator face it's important to make sure the plug-ins are enabled so I'll go to plug-ins here. So I don't know exactly which ones of these you need, imagine you need most of them but certainly for the live link aspect of this you'll need the metahuman live link plug-in enabled. So in my case I'm using a Logitech Brieo which is a nice little accessible web camera. And to get that set up on this metahuman which by the way is a very standard preset metahuman nothing special here and then I'm just going to go to add source in my live link window and then choose metahuman video. As you can see I've got my Brieo there and also you'll notice it's capable of doing the 12 AE by 720 90 FPS. There's a lot of options here but there's 90 FPS one we found is ideal. The extra frame rate that you get over resolution because as you can see I could do 60 at 1080p here but this 90 at 720p is considerably better for visual fidelity and fine kind of facial movements. Now if your frame rate is at 30 FPS you'll probably find that's capturing the face a...

**Frame:** tutorials\frames\metahuman-realtime-animator-best-practices-unreal-engine-animation-hub\frame_000.jpg


---

## Structured Notes

### Core Technique
Webcam-based MetaHuman Animator facial capture — setting up a USB webcam via Live Link for real-time performance capture with best practices for frame rate, resolution, and environment.

### Summary
Practical best practices for using MetaHuman Animator with a webcam source via Live Link. Covers enabling the MetaHuman Live Link plugin, configuring the source (`Add Source → MetaHuman Video`), optimal camera settings (720p/90fps preferred over 1080p/60fps for facial capture quality), lighting environment requirements, and recording workflow. Uses a Logitech Brio as the test camera.

### Key Steps
1. Enable plugins: `Edit → Plugins → MetaHuman Live Link` (+ Face AR Streaming, Live Link)
2. Open **Live Link** window (`Window → Live Link`)
3. `Add Source → MetaHuman Video` → select your webcam from the device list
4. Set camera resolution: **720p @ 90fps** preferred over 1080p @ 60fps (better fine facial motion fidelity)
5. Position webcam at eye level, ~50–60cm from face; even frontal lighting with no harsh shadows
6. In the Sequencer MetaHuman track: `Add → Live Link Control Rig → Live Link Face` (or ARKit)
7. Preview the live capture in the MetaHuman face; adjust `Strength` per blend shape as needed
8. Hit **Record** in Live Link Sequencer integration to bake the performance to an Animation Sequence
9. Review and clean up the captured curves in the Curve Editor

### UE Systems / Blueprints / Settings
`MetaHuman Live Link Plugin` → enables webcam/iPhone face capture via Live Link
`Live Link Window → Add Source → MetaHuman Video` → webcam source setup
Optimal settings: 720p @ 90fps (Logitech Brio or equivalent USB webcam)
`Live Link Face Track` (Sequencer) → real-time MetaHuman face control from Live Link stream
`Record` in Live Link Recorder → bakes to Animation Sequence
Lighting: even, frontal; avoid harsh shadows or backlight for accurate blend shape detection

### Difficulty
Intermediate

### UE Version
UE5

### Tags
metahuman, animation, mocap, intermediate

---

## Related Entries
- `references/metahuman-reference.md` — MetaHuman setup and animation methods
- `tutorials/metahumans-for-mocap-unreal-engine-animation-hub.md` — CaptureCharacter setup for Mocap Manager
- `tutorials/live-link-hub-tips-unreal-engine-animation-hub.md` — Live Link Hub multi-source management
- `references/lip-sync.md` — audio-driven facial animation