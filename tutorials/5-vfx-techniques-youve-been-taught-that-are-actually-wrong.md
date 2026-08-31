---
title: 5 VFX Techniques You've Been Taught That Are ACTUALLY Wrong
source: YouTube
url: https://www.youtube.com/watch?v=rUZxS3IwZhQ
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 5.x"
tags: [vfx, filmmaking, cinematography, compositing, beginner]
extraction_status: complete
frames_dir: tutorials/frames/5-vfx-techniques-youve-been-taught-that-are-actually-wrong/
frame_count: 4
---

# 5 vfx Techniques You've Been Taught That Are ACTUALLY Wrong

**Source:** [YouTube](https://www.youtube.com/watch?v=rUZxS3IwZhQ)
**Author:** Boundless Entertainment
**Duration:** ~8m | 5 section(s)

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

- tutorials/frames/5-vfx-techniques-youve-been-taught-that-are-actually-wrong/frame_000.jpg
- tutorials/frames/5-vfx-techniques-youve-been-taught-that-are-actually-wrong/frame_001.jpg
- tutorials/frames/5-vfx-techniques-youve-been-taught-that-are-actually-wrong/frame_002.jpg
- tutorials/frames/5-vfx-techniques-youve-been-taught-that-are-actually-wrong/frame_003.jpg

---

## Structured Notes

### Core Technique
Part 2 of the VFX philosophy series. Critiques five commonly-taught VFX techniques that are counterproductive or stylistically incorrect: overuse of camera shake, improper motion blur application, excessive color grading, incorrect depth of field usage, and over-reliance on lens flares.

### Summary
8-minute critique of five VFX techniques widely promoted in tutorials that actually hurt production quality. Sam argues these techniques are over-used as shortcuts that signal "we tried" rather than genuinely serving the story. Each technique is shown in before/after examples. Companion to Part 1 (these-simple-mistakes-are-ruining-your-vfx). Core philosophy: every visual tool exists to serve the story, not to demonstrate technical skill.

### Key Steps / Mistakes Covered
1. **Camera shake overuse** — handheld-style shake applied uniformly regardless of story context; creates nausea without narrative purpose; rule: shake should respond to story events, not be a constant filter
2. **Motion blur application** — incorrect shutter angle settings producing either too much blur (dreamlike) or too little (strobing); 180-degree shutter rule (shutter speed = 2x frame rate) as starting baseline
3. **Color grading as correction** — extreme teal-and-orange or desaturated grades applied without understanding why films use those palettes; correct approach = grade serves the emotional arc of the scene
4. **Depth of field** — extremely shallow DOF used on everything as a "cinematic" signal; over-use disconnects viewer from environment; rule: DOF choice should match the lens language of the story
5. **Lens flares** — added in post as decoration; real lens flares occur only when a light source enters frame; fake flares positioned incorrectly break immersion

### UE Relevance
- Sequencer camera settings: Shutter Speed = 2x frame rate; DOF Aperture tied to story intent
- MRQ: Motion Blur settings (temporal samples, shutter angle)
- Post Process Volume: color grading via color curves, not global teal-orange crush
- LightForge or PPV: lens flare control (add only when light source is in frame)

### Difficulty
Beginner

### UE Version
UE 5.x

### Tags
`#vfx` `#filmmaking` `#cinematography` `#compositing` `#beginner`

---

## Related Entries
- [[these-simple-mistakes-are-ruining-your-vfx]] — Part 1 of the VFX mistakes series
- [[unreal-engines-secret-weapon-for-cinematic-lighting]] — LightForge gobo/lighting philosophy
- [[the-simplest-rendering-trick-90-of-unreal-artists-miss]] — chromatic aberration, vignette, lens imperfections
- [[how-to-make-your-unreal-engine-renders-look-real]] — cinematic realism principles
