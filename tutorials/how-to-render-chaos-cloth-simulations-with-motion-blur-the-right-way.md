---
title: How to Render Chaos Cloth Simulations with Motion Blur [The RIGHT Way]
source: YouTube
url: https://www.youtube.com/watch?v=f4izPHpbfZI
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: lightforge-v2
ue_version: "UE 5.x"
tags: [lightforge-v2, simulation, cloth, rendering, mrq, sequencer, take-recorder, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way/
frame_count: 10
---

# How to Render Chaos Cloth Simulations with Motion Blur [The RIGHT Way]

**Source:** [YouTube](https://www.youtube.com/watch?v=f4izPHpbfZI)
**Author:** Boundless Entertainment
**Duration:** ~14m | 10 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted - see ingested file...]

---

## Structured Notes

### Core Technique
Chaos Cloth simulations break when rendered with MRQ temporal subsampling (the cloth re-simulates per subframe causing chaos). The fix: cache the simulation via Take Recorder + Chaos Cache Manager into a saved animation track, then render using temporal sub-sampling with AA Method=None, spatial=1, temporal=21. Critical bug: delete and re-add the Chaos Cache track in Sequencer after recording, or UE will re-simulate instead of using the cache during render.

### Summary
14-minute tutorial on the only correct way to render Chaos Cloth with high-quality motion blur in MRQ. Problem: temporal subsampling (needed for motion blur) causes Chaos Cloth to re-simulate for each subframe, producing chaotic/corrupted results. Solution: cache the cloth animation using Take Recorder, then render from cache. Workflow: add Wind Directional Source to scene → simulate to verify cloth movement → open Take Recorder > Source > Actor > select character with cloth → open sequence to record into → hit Record (countdown to 1 then starts) → play simulation through timeline → stop Take Recorder → File > Save All. Bug fix: delete the Chaos Cache track in Sequencer, then re-add by dragging Chaos Cache Manager and adding Chaos Cache track via +Track, or UE re-simulates during render and overwrites the cache. Render settings: MRQ > AA Method=None, Spatial Samples=1, Temporal Samples=21, EXR 16-bit, deferred or path trace, Game Overrides enabled.

### Key Steps
1. **Verify cloth sim** - Place actors > Wind > Wind Directional Source; hit Simulate to preview cloth in viewport
2. **Open Take Recorder** - Window > Take Recorder (or Cinematics > Take Recorder)
3. **Set source** - Take Recorder > Source > + > Actor (not Live Link or Chaos Cache); select character with cloth sim
4. **Open sequence** - Click arrow in Take Recorder > open the shot sequence to record into
5. **Record** - Hit Record in Take Recorder; countdown from 3 to 1; simulation plays and cloth animation is captured
6. **Stop and save** - Let simulation run to end (auto-stops) or hit Stop; File > Save All
7. **Bug fix (critical)** - In Sequencer: find Chaos Cache Manager track > DELETE it; then drag Chaos Cache Manager actor from Outliner into Sequencer > click +Track on it > Chaos Cache > chaos cache track re-appears with saved animation; without this, UE will re-simulate during render
8. **Render settings** - MRQ > Anti Aliasing: Method=None, Spatial Samples=1, Temporal Samples=21 (higher=better blur quality); EXR Sequence 16-bit; Deferred or Path Tracing; Game Overrides=ON; OCIO config optional

### UE Systems / Blueprints / Settings
- **Temporal Subsampling** - MRQ Anti Aliasing > Temporal Sample Count; each frame split into N subframes; captures incremental movement for smooth motion blur; breaks Chaos sims unless cached
- **Take Recorder** - Captures live simulation data as animation tracks; source=Actor captures cloth; records while simulation plays in editor; creates animation asset
- **Chaos Cache Manager** - UE system for caching Chaos cloth/destruction simulations; drag into scene based on specific actor; captures cloth frames as replayable data
- **Chaos Cache bug** - After recording: Sequencer Chaos Cache track must be deleted and re-added or render will trigger live re-simulation and overwrite cache work
- **AA Method=None** - Required for temporal subsampling to work correctly for motion blur; spatial=1, temporal=N where N controls blur quality
- **Wind Directional Source** - Place Actors > Wind > adds wind force field to scene; good starting point for cloth wind effects

### Difficulty
Intermediate

### UE Version
UE 5.x

### Tags
`#lightforge-v2` `#simulation` `#cloth` `#rendering` `#mrq` `#sequencer` `#take-recorder` `#intermediate`

---

## Captured Frames

<!-- Timestamps RECOVERED 2026-08-25 by recover_moments.py, not chosen.
     ingest.py before c4decae picked blind-era moments deterministically;
     re-derived from the source's own chapter/duration metadata and
     accepted only because the count matched frame_count exactly.
     These are blind-era moments: legible and citable now, but not
     content-anchored. Re-selecting them is still a human call. -->

- [0:05] tutorials/frames/how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way/frame_000.jpg
- [1:31] tutorials/frames/how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way/frame_001.jpg
- [2:05] tutorials/frames/how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way/frame_002.jpg
- [3:28] tutorials/frames/how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way/frame_003.jpg
- [5:53] tutorials/frames/how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way/frame_004.jpg
- [9:08] tutorials/frames/how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way/frame_005.jpg
- [10:02] tutorials/frames/how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way/frame_006.jpg
- [11:48] tutorials/frames/how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way/frame_007.jpg
- [12:56] tutorials/frames/how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way/frame_008.jpg
- [13:41] tutorials/frames/how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way/frame_009.jpg

## Related Entries
- [[best-settings-for-unreal-engine-56---perfect-renders-every-time]] - MRQ render settings deep-dive
- [[fastest-way-to-optimize-unreal-engine-56-for-cinematic-renders---path-tracer-pro]] - Path Tracer render optimization
- [[unreal-engine-54-cinematic-previs-course]] - full filmmaking workflow context
