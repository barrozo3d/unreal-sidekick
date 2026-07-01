---
title: Unreal Engine Compositing Tutorial - UNREAL ENGINE FOR FILMMAKERS [Course Link in Description]
source: YouTube
url: https://www.youtube.com/watch?v=39nmue2lIdA
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 5.x"
tags: [compositing, fog-cards, media-player, sequencer, materials, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-compositing-tutorial---unreal-engine-for-filmmakers-course-link-in/
frame_count: 8
---

# Unreal Engine Compositing Tutorial - UNREAL ENGINE FOR FILMMAKERS [Course Link in Description]

**Source:** [YouTube](https://www.youtube.com/watch?v=39nmue2lIdA)
**Author:** Boundless Entertainment
**Duration:** 8m46s | 8 section(s)

---

## Structured Notes

### Core Technique
Fog cards and media-texture compositing in UE5 using Media Player + Media Texture + translucent plane material. Media Track in Sequencer handles playback timing. Technique works for fog overlays, green-screen plates, or any video layer composited in-engine.

### Summary
9-minute tutorial on compositing video media as fog cards or overlay layers inside UE5. The technique: import an MP4 as a Media Player (with Media Texture output); create a plane scaled to match aspect ratio; drag the Media Texture onto the plane to auto-create a material; open the material and set up RGB + Multiply (scalar "strength") → Emissive Color + Opacity scalar (Translucent blend mode); disable Cast Shadow on the plane mesh; in Sequencer: add Media Track > + > select the media player > drag clip to fill timeline > right-click > Edit Section > assign Media Texture. Applicable to: fog cards (atmospheric density layers), green-screen footage plates, lens flare overlays, any 2D video element.

### Key Steps
1. **Import video** — right-click in Content Browser > Media > Media Player; check "Video Output Media Texture Asset" = ON; click OK; name the media player; double-click to open > browse to MP4 file > double-click > Save; close
2. **Create plane** — place a Plane from Place Actors; scale X=16, Y=9 (matches 16:9 aspect ratio); rotate so it faces the camera direction
3. **Create material** — drag the Media Texture from Content Browser onto the plane; auto-creates a basic material; double-click the material to open Material Editor
4. **Material setup** — Material > General > Blend Mode = Translucent; Texture Sample > RGB output → Multiply node > multiply by Scalar Parameter ("strength": default=1) → Emissive Color output; create separate Scalar Parameter ("opacity") → Opacity output; this allows independent brightness and opacity control per instance
5. **Disable shadow** — select the plane > Details > Rendering > Cast Shadow = OFF (otherwise the plane casts a flat rectangle shadow on ground)
6. **Sequencer Media Track** — open Level Sequence; Sequencer toolbar > +Track > Media Track; on the Media Track: click + > select your media player; drag the section to the desired start/end frames; right-click section > Edit Section > Media Texture: assign the media-texture asset; clip now plays in sync with Sequencer
7. **Adjust look** — select plane > Details > material override instance > adjust Strength (emissive brightness) and Opacity per shot

### UE Systems / Settings
- **Media Player** — UE media playback asset; links to external video file; controls play/pause/loop; requires Media Texture companion for rendering
- **Media Texture** — texture asset that reads from Media Player; use as Texture Sample in material for video-driven material; created automatically when "Video Output Media Texture Asset" is checked
- **Translucent Blend Mode** — required for transparent fog/overlay planes; exposes Opacity input; allows alpha compositing in viewport and renders
- **Emissive Color for fog** — using Emissive instead of Base Color allows the plane to self-illuminate and ignore scene lighting; matches the "glow" behavior of real atmospheric fog
- **Media Track in Sequencer** — Level Sequence track type that drives Media Player playback; clip start = media playback start; drag to trim or extend

### Difficulty
Intermediate

### UE Version
UE 5.x (early era)

### Tags
`#compositing` `#fog-cards` `#media-player` `#sequencer` `#materials` `#intermediate`

---

## Related Entries
- [[unreal-engine-5-compositing-tutorial---composite-any-scene-fully-inside-of-ue5]] — full compositing workflow (camera-tracking + image plate)
- [[unreal-engine-depth-fog-tutorial-path-traced]] — depth fog for Path Tracer (PPV material method)
- [[unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic]] — fog cards + night scene lighting companion
- [[unreal-engines-secret-weapon-for-cinematic-lighting]] — LightForge 2.0 uses File Media Source for gobo videos (same Media Player system)
