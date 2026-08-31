---
title: I BUILT The Camera Tracking Tool I Always Wished Unreal Had
source: YouTube
url: https://www.youtube.com/watch?v=uMJXtDJf6VQ
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: genesis
ue_version: "UE 5.x"
tags: [genesis, camera-tracking, vfx, beginner]
extraction_status: complete
frames_dir: tutorials/frames/i-built-the-camera-tracking-tool-i-always-wished-unreal-had/
frame_count: 4
---

# I BUILT The Camera Tracking Tool I Always Wished Unreal Had

**Source:** [YouTube](https://www.youtube.com/watch?v=uMJXtDJf6VQ)
**Author:** Boundless Entertainment
**Duration:** ~3m | 1 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted - see ingested file...]

---

## Captured Frames

⚠️ **Listed 2026-08-31 without timestamps, and not usable for grounding.**
These frames were captured at ingest but never recorded in the file — no
`## Captured Frames` section was written, so the entry claimed frames it never
listed (`validate.py` check #17, population A). The paths below are the frames
that actually exist, listed so the record is true.

Two limits, stated rather than worked around:

- **No timestamps.** No moment was ever recorded for these. None is given here,
  because inventing one is the moment-*choosing* D0 rules out — and it would also
  make the set look re-groundable when it is not.
- **256×144.** Blind-era captures at the resolution D0b identified as unreadable.
  Panel layout is discernible; node names, parameter values and menu text are not.
  **They are cited nowhere in the Structured Notes, because they ground nothing.**

- tutorials/frames/i-built-the-camera-tracking-tool-i-always-wished-unreal-had/frame_000.jpg
- tutorials/frames/i-built-the-camera-tracking-tool-i-always-wished-unreal-had/frame_001.jpg
- tutorials/frames/i-built-the-camera-tracking-tool-i-always-wished-unreal-had/frame_002.jpg
- tutorials/frames/i-built-the-camera-tracking-tool-i-always-wished-unreal-had/frame_003.jpg

---

## Structured Notes

### Core Technique
Genesis plugin announcement and capability overview: the first 3D camera-tracking tool built directly into Unreal Engine, providing sub-pixel accurate camera match-move, textured 3D reconstruction, distortion compensation, in-engine preview, and scale/orientation tools - all fully automated with zero manual tracking setup.

### Summary
Short announcement video introducing Genesis by Boundless Entertainment. Sam explains the problem (UE has no native 3D camera tracker; integrating CGI with live action is the hardest part of vfx) and presents Genesis as the solution: a UE plugin that automates camera-tracking, 3D reconstruction, and distortion compensation. Key Genesis capabilities: sub-pixel accurate match move, detailed textured reconstructed mesh, distortion compensation, in-engine preview, scale/orientation tools, zero manual work required. Philosophy: shoot in real environments, use vfx to enhance (not replace).

### Key Steps
N/A - announcement video. For implementation see [[3d-tracking-natively-in-unreal-engine---full-tutorial]].

### UE Systems / Blueprints / Settings
- **Genesis (overview)** - Plugin features: (1) sub-pixel camera match move, (2) textured reconstructed mesh, (3) distortion compensation, (4) in-engine preview, (5) scale+orientation tools; 100% automated
- **Filmmaking philosophy** - Shoot real environments, add VFX on top; Genesis enables this by removing the complexity barrier of camera-tracking

### Difficulty
Beginner

### UE Version
UE 5.x (Genesis plugin)

### Tags
`#genesis` `#camera-tracking` `#vfx` `#beginner`

---

## Related Entries
- [[3d-tracking-natively-in-unreal-engine---full-tutorial]] - full Genesis step-by-step tutorial
- [[unreal-engine-5-compositing-tutorial---composite-any-scene-fully-inside-of-ue5]] - compositing follow-up
