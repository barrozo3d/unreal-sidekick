---
title: Why Modern VFX Suck (And How to Make Yours Not Suck)
source: YouTube
url: https://www.youtube.com/watch?v=qPVS75PM5eU
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 5.x"
tags: [vfx, filmmaking, compositing, cinematography, beginner]
extraction_status: complete
frames_dir: tutorials/frames/why-modern-vfx-suck-and-how-to-make-yours-not-suck/
frame_count: 6
---

# Why Modern vfx Suck (And How to Make Yours Not Suck)

**Source:** [YouTube](https://www.youtube.com/watch?v=qPVS75PM5eU)
**Author:** Boundless Entertainment
**Duration:** 7m49s | 6 section(s)

---

## Structured Notes

### Core Technique
Part 1 of the modern VFX quality series. Root cause diagnosis: modern VFX fail because studios use CGI as a crutch for poor filmmaking decisions — fully digital shots with no practical grounding. Sam's own short film "Gemini" demonstrates the solution: shoot on real locations, make real elements the dominant visual, composite in only what is physically impossible to shoot.

### Summary
8-minute series opener diagnosing why modern VFX quality has declined. Core argument: the problem isn't VFX technology — it's lazy filmmaking decisions in the director's chair and studio boardrooms. Over-reliance on CGI means: impossible timetables for artists, green-screen-only shoots that lack grounding in reality, and missing cinematographic craft (lighting motivation, composition). Sam demonstrates his own approach from short film "Gemini": shot at a real destroyed dairy farm; only the buildings/city in the background are CG; all foreground — rubble, debris, landscape — is real; adds fog at the practical-to-digital boundary to smoothly blend the transition. Key insight: matching CGI to real footage raises the quality bar because the CGI must be accurate enough to pass as real; fully CGI has no reference to fail against.

### Key Principles
1. **VFX serve story, not replace production design** — CGI as a crutch leads to VFX that announce themselves; good VFX blend in and serve the story beat
2. **Shoot on a real location** — real environment provides: accurate lighting reference for CG elements, real foreground/midground to anchor CG, visual complexity impossible to fake cheaply
3. **Make real elements the main focus** — CGI should be supporting cast, not the hero; the eye forgives imperfect CG when real elements are dominant in the frame
4. **Fog/haze blends practical-to-digital boundary** — adding fog where real and CG meet allows a soft, light-based transition that hides the seam; atmospheric perspective also adds depth
5. **Real footage raises CG quality bar** — when CG must match real footage, any inaccuracy is visible; this forces better CG; fully digital has no failure mode because there's nothing to compare against

### Sam's Gemini Workflow (Applied Example)
- Shot at destroyed dairy farm (real location with post-apocalyptic look)
- Only CG elements: buildings, city background
- Real elements: rubble, debris, landscape, foreground props — all in camera
- Added fog cards at the practical-to-CG transition zone
- Composited in AE/Resolve; buildings matched to real sky/lighting reference captured on set

### UE Relevance
- When compositing with UE5 + Genesis: always have real foreground/midground elements in camera
- Fog Cards in UE5 (or Exponential Height Fog) can add blending haze at scene boundaries
- Real HDRI captured on set → UE Sky Light → accurate CG lighting match

### Difficulty
Beginner (filmmaking philosophy + personal case study, no technical steps)

### UE Version
UE 5.x

### Tags
`#vfx` `#filmmaking` `#compositing` `#cinematography` `#beginner`

---

## Related Entries
- [[why-modern-vfx-suck-and-how-to-make-yours-not-suck-part-2---transformers-vs-marv]] — Part 2: Transformers vs Marvel case studies
- [[why-modern-vfx-dont-suck---low-budget-virtual-production-everything-everywhere-a]] — Part 3: EEAAO positive case study
- [[these-simple-mistakes-are-ruining-your-vfx]] — extended VFX philosophy (mistakes series)
- [[the-5-secrets-to-hollywood-level-visual-effects-with-no-budget]] — positive version: 5 principles from Oscar winners
