---
title: 3D Tracking Natively in Unreal Engine - FULL TUTORIAL
source: YouTube
url: https://www.youtube.com/watch?v=z9t4XIoNsHY
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: genesis
ue_version: "UE 5.x"
tags: [genesis, camera-tracking, vfx, compositing, distortion, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/3d-tracking-natively-in-unreal-engine---full-tutorial/
frame_count: 7
---

# 3D Tracking Natively in Unreal Engine - FULL TUTORIAL

**Source:** [YouTube](https://www.youtube.com/watch?v=z9t4XIoNsHY)
**Author:** Boundless Entertainment
**Duration:** ~14m | 7 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted - see ingested file...]

---

## Structured Notes

### Core Technique
Full end-to-end walkthrough of Genesis (Boundless Entertainment 3D camera-tracking plugin): automated tracking from masked footage, 3D reconstruction import, scene scale/orientation calibration via two-point measurement, and automatic distortion compensation via Lens Component - all done natively inside Unreal Engine with zero manual tracking work.

### Summary
14-minute full tutorial covering all three Genesis processes. Workflow: mask subject in AE/DaVinci/fusion (gray solid fill) to eliminate moving actors from tracking footage → Genesis window: Choose Footage → automated tracking (no manual work) → import tracking scene (Choose Directory from Genesis output folder) → set frame rate (e.g. 23.976) + sensor width (e.g. 27.03mm from RED camera) → activate Set Scale Mode (two-point click on mesh, enter measured distance) → set orientation → review camera + distortion: Genesis auto-creates Lens Component with distortion parameters; toggling Apply Distortion shows the alignment difference. Genesis Perpetual License option available (buy outright + 1 year updates).

### Key Steps
1. **Mask subject** - in AE/DaVinci/fusion: create mask around moving subject, fill with gray solid, render; eliminates moving actors from tracker
2. **Enable Genesis** - Edit > Plugins > search Genesis > enable > restart; open Genesis window (dock it)
3. **Choose Footage** - Click Choose Footage in Genesis panel; select the masked tracking footage
4. **Automated tracking** - Genesis tracks automatically; wait for completion (point cloud + dense mesh reconstructed)
5. **Import tracking scene** - Click OK when prompted; or Choose Directory to navigate to Genesis output folder; import any tracking scene into any UE project
6. **Set frame rate + sensor width** - Frame rate must match footage (e.g. 23.976); sensor width from camera specs (e.g. 27.03mm for RED); Genesis calculates focal length from sensor width + tracking data; critical for correct depth of field
7. **Set scene scale** - Genesis > Scene Setup > select tracking scene > Scale > Activate Set Scale Mode > click two points on mesh > enter known real-world distance between them
8. **Set orientation** - Align scene to world up/forward in Scene Setup
9. **Review background plate** - Select camera > Background Plate Preview > set opacity=1, fade range=0; scrub timeline to verify tracking alignment
10. **Distortion compensation** - Genesis auto-creates Lens Component on tracked camera with distortion parameters; toggle Apply Distortion to see/verify alignment; leave enabled for final composite

### UE Systems / Blueprints / Settings
- **Genesis plugin** - Boundless Entertainment proprietary; install via Epic Marketplace or Fab; enables Genesis panel (dock in editor)
- **Lens Component** - UE native lens distortion system; Genesis populates it automatically from tracking data; controls Apply Distortion toggle
- **Background Plate Preview** - Overlays footage on camera view in editor; opacity + fade range controls; use to verify CGI alignment in real-time
- **Scene Setup > Scale Mode** - Two-point click on reconstructed mesh; enter real-world distance; Genesis rescales scene to match reality (critical for correct depth of field + CGI integration)
- **Sensor width requirement** - Must match actual camera; used to calculate focal length from tracking data; incorrect value = wrong DOF

### Difficulty
Intermediate

### UE Version
UE 5.x (Genesis plugin)

### Tags
`#genesis` `#camera-tracking` `#vfx` `#compositing` `#distortion` `#intermediate`

---

## Related Entries
- [[i-built-the-camera-tracking-tool-i-always-wished-unreal-had]] - Genesis announcement + feature overview
- [[unreal-engine-5-compositing-tutorial---composite-any-scene-fully-inside-of-ue5]] - compositing workflow using Genesis tracking
- [[3d-tracked-camera-from-after-effects-to-unreal-engine-tutorial]] - AE-to-UE tracking (non-Genesis approach)
