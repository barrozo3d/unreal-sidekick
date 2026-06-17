---
title: Roger Deakins Lighting Tutorial - BLADE RUNNER 2049
source: YouTube
url: https://www.youtube.com/watch?v=S8nDuuIucCc
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 5.x"
tags: [cinematography, lighting, filmmaking, beginner]
extraction_status: complete
frames_dir: tutorials/frames/roger-deakins-lighting-tutorial---blade-runner-2049/
frame_count: 4
---

# Roger Deakins Lighting Tutorial - BLADE RUNNER 2049

**Source:** [YouTube](https://www.youtube.com/watch?v=S8nDuuIucCc)
**Author:** Boundless Entertainment
**Duration:** 4m34s | 1 section(s)

---

## Structured Notes

### Core Technique
4-minute analysis of Roger Deakins' cinematographic philosophy on Blade Runner 2049: 1-3 light sources per scene maximum; motivate every light through the story/environment (practical lights, water, windows, open doors); let non-essential areas fall to darkness; the lighting builds the world and contributes to the story's mood.

### Summary
4.5-minute intro to Roger Deakins' lighting philosophy applied to Blade Runner 2049. Key insight: the film uses very few light sources per scene (1-3) but each source is motivated by the environment (a window, a practical light fixture, a hologram, water reflection) rather than being a fill rig. Deakins uses practicals (neon signs, desk lamps, holographic projections, candles, water-reflected light) as primary sources and builds character around what naturally exists in the scene. The lighting builds the Blade Runner world — dystopian neon vs. cold industrial blue — and this contrast is part of the storytelling. Sam's takeaway: instead of adding lighting to show everything, allow most of the frame to fall to darkness and use one motivated source to carve out shape. Transcript is partially cut off but covers the foundational philosophy.

### Key Principles (Roger Deakins / Blade Runner 2049)
1. **Minimum sources** — 1-3 light sources per scene; additional fixtures may cover a large set but the lighting theory stays simple
2. **Story-motivated lighting** — every source has a narrative reason: window, practical lamp, neon sign, water reflection, hologram; no unmotivated fill lights
3. **Let darkness work** — not everything needs to be visible; shadow is as important as light; non-essential areas fall to black without apology
4. **Environment as set dressing + lighting** — uses water reflections, holographic projections, city lights through windows as free environmental accent sources
5. **Simplicity is resourcefulness** — complex cinematic looks achieved with fewer resources; more light ≠ better; motivated restraint = character

### Comparison: Deakins vs Greig Fraser
- Both use atmospheric depth (haze/rain/fog) — see dune-breakdown
- Deakins: more neon/practical motivated; cooler color temperatures; allows deep shadow
- Fraser (Dune): soft natural light style; overhead large sources; warm sandy palette
- Both: shoot from shadow side, use minimal but deliberate sources, let backgrounds breathe

### UE Application
- **Practical-motivated lighting**: use Point Lights / Rect Lights placed at neon sign locations; IES profiles for realistic lamp fall-off; Emissive materials on sign geometry
- **Water reflections**: add Puddle Blend Material (see Dash puddles tutorial) or a reflective plane material; picks up all scene lights
- **Hologram accent**: Emissive material on translucent mesh; use a Rect Light with gobo (LightForge) to project patterns
- **Contrast ratio**: expose for the highlights; let shadow areas fall — PPV > Min Luminance = 0; no excessive Lumen indirect that fills shadows uniformly
- **Color temperature**: Blade Runner 2049 has orange/amber neon vs. cool steel blue — set Point Lights to warm (3200K) + Directional to cool blue (6500K)

### Difficulty
Beginner (cinematography philosophy; 4.5 min overview)

### UE Version
UE 5.x

### Tags
`#cinematography` `#lighting` `#filmmaking` `#beginner`

---

## Related Entries
- [[dune-cinematography-breakdown-how-to-get-the-dune-look]] — Greig Fraser (related DoP analysis)
- [[unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic]] — practical night scene lighting implementation
- [[unreal-engines-secret-weapon-for-cinematic-lighting]] — LightForge 2.0 gobo texture projection for motivated lighting
