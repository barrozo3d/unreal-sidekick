---
title: Why Modern VFX Suck (And How to Make Yours Not Suck) PART 2 - Transformers vs Marvel
source: YouTube
url: https://www.youtube.com/watch?v=zOcXC-imA5U
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 5.x"
tags: [vfx, filmmaking, compositing, cinematography, beginner]
extraction_status: complete
frames_dir: tutorials/frames/why-modern-vfx-suck-and-how-to-make-yours-not-suck-part-2---transformers-vs-marv/
frame_count: 6
---

# Why Modern vfx Suck (And How to Make Yours Not Suck) PART 2 - Transformers vs Marvel

**Source:** [YouTube](https://www.youtube.com/watch?v=zOcXC-imA5U)
**Author:** Boundless Entertainment
**Duration:** 6m48s | 6 section(s)

---

## Structured Notes

### Core Technique
Part 2 of the modern VFX quality analysis series. Case study comparison: Transformers (ILM, on-location, practical-CG blend) vs. Marvel (studio, blue/green-screen, fully digital) — the practical-digital blend in Transformers produces far more convincing VFX despite lower per-shot VFX budget than Marvel's all-digital approach.

### Summary
7-minute case study comparison of Transformers and Marvel VFX philosophies. Transformers (Michael Bay / ILM): shot on real locations with practical effects; only the CG robots are digital — everything else (bus, fire, environment) is real; the CG robot interacting with real objects makes the digital element impossible to dismiss; ILM VFX supervisor describes capturing 360-degree HDR reference of every location so robot reflections match exactly ("the secret is keep it dark and out of focus" — they prefer having controllable lighting conditions). Marvel Black Widow counter-example: actress on blue-screen, fully digital background, flat overcast lighting, unconvincing composition — every bad VFX practice in one shot. Conclusion: always anchor digital elements in practical reality; never let the digital be the only real thing in the frame; good cinematography makes VFX more convincing, bad cinematography exposes every VFX flaw.

### Key Principles Demonstrated
1. **On-location = built-in realism** — shooting in a real environment grounds all CG elements; reflections, shadows, lighting all come from reality not from guessing; Transformers principle: the CG robot is the only thing that isn't real
2. **Real objects anchor CG** — using a real bus, real fire, real stunts in the same shot as CG robots; anything real in the frame makes the viewer question what is and isn't CG in the rest of the frame
3. **ILM HDRI capture workflow** — on every location: crew member captures 360-degree HDRI/photographic reference from exact camera position; in CG: apply that HDRI as reflection/lighting reference on the CG element; result = exact lighting match
4. **The "dark and out of focus" rule** — ILM VFX supervisor quote: "the secret to visual effects is keep it dark and out of focus" — controllable/moody lighting is easier to match in CG than bright flat overcast; helps hide integration seams
5. **Bad cinematography exposes VFX** — Black Widow shot: flat overcast lighting + straight-on camera angle + no practical elements = every VFX seam is visible; good composition + motivated lighting + real elements in frame = CG seams disappear

### UE / Filmmaker Application
- When compositing with Genesis/UE5: always shoot on a real location with reference HDRIs captured on set
- Apply HDRI as lighting reference in UE5 (Sky Light > HDRI) for accurate CG-to-footage integration
- Avoid blue/green-screen unless absolutely necessary; add practical elements at the shoot (real props, practical lights, real foreground elements)
- Motivated lighting (direction + color from a logical source) is easier to match in UE5 than flat ambience
- Keep CG camera angles dynamic and constrained by real-world lens choices — avoid the "floating camera" look of fully CG shots

### Difficulty
Beginner (filmmaking analysis, no technical steps)

### UE Version
UE 5.x

### Tags
`#vfx` `#filmmaking` `#compositing` `#cinematography` `#beginner`

---

## Captured Frames

<!-- Timestamps RECOVERED 2026-08-25 by recover_moments.py, not chosen.
     ingest.py before c4decae picked blind-era moments deterministically;
     re-derived from the source's own chapter/duration metadata and
     accepted only because the count matched frame_count exactly.
     These are blind-era moments: legible and citable now, but not
     content-anchored. Re-selecting them is still a human call. -->

- [0:05] tutorials/frames/why-modern-vfx-suck-and-how-to-make-yours-not-suck-part-2---transformers-vs-marv/frame_000.jpg
- [1:18] tutorials/frames/why-modern-vfx-suck-and-how-to-make-yours-not-suck-part-2---transformers-vs-marv/frame_001.jpg
- [2:13] tutorials/frames/why-modern-vfx-suck-and-how-to-make-yours-not-suck-part-2---transformers-vs-marv/frame_002.jpg
- [3:16] tutorials/frames/why-modern-vfx-suck-and-how-to-make-yours-not-suck-part-2---transformers-vs-marv/frame_003.jpg
- [3:47] tutorials/frames/why-modern-vfx-suck-and-how-to-make-yours-not-suck-part-2---transformers-vs-marv/frame_004.jpg
- [5:58] tutorials/frames/why-modern-vfx-suck-and-how-to-make-yours-not-suck-part-2---transformers-vs-marv/frame_005.jpg

## Related Entries
- [[why-modern-vfx-suck-and-how-to-make-yours-not-suck]] — Part 1 of this series
- [[why-modern-vfx-dont-suck---low-budget-virtual-production-everything-everywhere-a]] — Part 3 (positive counterpart)
- [[these-simple-mistakes-are-ruining-your-vfx]] — VFX mistakes Part 1 (related philosophy)
- [[3d-tracking-natively-in-unreal-engine---full-tutorial]] — Genesis: UE5 camera-tracking for compositing
