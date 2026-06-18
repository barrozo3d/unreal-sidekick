---
title: Live Link Hub Tips | Unreal Engine Animation Hub
source: YouTube
url: https://www.youtube.com/watch?v=JdaXti950vg
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["animation", "mocap", "pipeline", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/live-link-hub-tips-unreal-engine-animation-hub/
frame_count: 4
---

# Live Link Hub Tips | Unreal Engine Animation Hub

**Source:** [YouTube](https://www.youtube.com/watch?v=JdaXti950vg)
**Author:** Unreal Engine
**Duration:** 6m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome to the Animation Hub. Today I'm going to show you some tips for setting up and using the Live Link Hub to manage Live Link data. This includes recording data, as well as managing the Live Link streams that can be sent to multiple work sessions. Live Link Hub is a standalone app, as long as you have the plugin enabled, you can go under the Tools menu and launch Live Link Hub. Set it to come up here. So looking at left and right, I can add a source, add my Captury Body. As soon as I do that, I have the subject that is being streamed from my Captury system. This will appear in the Editor menu. You can see on the right I have clients. The clients are the workstations that are on the subnet. These two workstations that are currently on the same subnet that have the Editor launched. This is the one that I'm working with. This is another one. It will also tell you what level the other workstation is launched into. So let's add some more sources. I'm going to add the OptiTrac. I can have multiple systems come in at the same time. OptiTrac here, you can see that appears and immediately Live Link and Editor updates. Now we're going to add I have linked face. So in the face, see it lo...

**Frame:** tutorials\frames\live-link-hub-tips-unreal-engine-animation-hub\frame_000.jpg


---

## Structured Notes

### Core Technique
Live Link Hub standalone app — routing multiple mocap streams (body + face + props) from different systems to multiple UE editor workstations simultaneously over a subnet.

### Summary
Covers Live Link Hub as a centralized routing app for professional mocap setups. Demonstrates adding multiple sources (Captury body, OptiTrack, iLinked face) simultaneously, routing streams to multiple UE editor instances on the same subnet, recording all streams together, and managing which clients receive which data. Enables team-based mocap sessions where multiple animators work on different characters from the same live data.

### Key Steps
1. Enable **Live Link Hub Plugin** in UE (`Edit → Plugins → Live Link Hub`)
2. Launch Hub: `Tools → Live Link Hub` (standalone window; can run on a dedicated machine)
3. In Live Link Hub: `Add Source` → choose your mocap system (Captury, OptiTrack, iLinked, MetaHuman Video, etc.)
4. Sources appear in the left panel; subject list populates automatically
5. **Clients** panel (right) shows all UE editor instances on the same subnet — verify correct workstation is listed
6. Assign subjects to clients (optional; default: all subjects broadcast to all clients)
7. Hit **Record All** to capture all streams simultaneously to a single session
8. In each UE editor, open Live Link window → subjects from Hub appear automatically (no local source setup needed)
9. Useful for multi-character scenes: different team members animate different characters from same live data

### UE Systems / Blueprints / Settings
`Live Link Hub` (standalone app) → centralized Live Link routing; Tools → Live Link Hub
`Add Source` → Captury Body, OptiTrack, iLinked Face, MetaHuman Video, etc.
`Clients Panel` → shows all UE editor instances on subnet; assign subjects per client
`Record All` → simultaneous multi-source recording
`Subnet discovery` → automatic; all editors on same network segment see Live Link Hub

### Difficulty
Intermediate

### UE Version
UE5

### Tags
animation, mocap, pipeline, intermediate

---

## Related Entries
- `tutorials/metahumans-for-mocap-unreal-engine-animation-hub.md` — CaptureCharacter setup
- `tutorials/metahuman-realtime-animator-best-practices-unreal-engine-animation-hub.md` — webcam face capture
- `references/metahuman-reference.md` — MetaHuman animation pipeline