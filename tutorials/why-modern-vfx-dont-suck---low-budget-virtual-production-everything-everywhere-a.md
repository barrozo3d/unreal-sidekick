---
title: Why Modern VFX DON'T Suck - Low Budget Virtual Production & Everything Everywhere All at Once
source: YouTube
url: https://www.youtube.com/watch?v=6w8cEVgikrg
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 5.x"
tags: [vfx, filmmaking, virtual-production, compositing, cinematography, beginner]
extraction_status: complete
frames_dir: tutorials/frames/why-modern-vfx-dont-suck---low-budget-virtual-production-everything-everywhere-a/
frame_count: 4
---

# Why Modern VFX DON'T Suck - Low Budget Virtual Production & Everything Everywhere All at Once

**Source:** [YouTube](https://www.youtube.com/watch?v=6w8cEVgikrg)
**Author:** Boundless Entertainment
**Duration:** 8m48s | 4 section(s)

---

## Structured Notes

### Core Technique
Part 3 of the modern VFX series (positive counterpart to Parts 1 and 2). Case study: Everything Everywhere All at Once — how creative practical-first thinking and DIY virtual production principles produce superior results to big-budget fully-digital approaches.

### Summary
8-minute positive counterpart to the "why VFX suck" series. Sam analyzes Everything Everywhere All at Once (low budget, acclaim) as a model for creative VFX filmmaking. Key multiverse-jump shot breakdown: actress in a wheelchair (not green screen) moving backwards + low shutter speed + low frame rate + leaf blower = natural motion blur and wind effect; played at 24fps produces the correct amount of motion for a "slow motion" appearance. For shots that couldn't be done practically: green screen + two LED screens as environmental fill light on either side of the actress — budget virtual production. Also explains professional virtual production (LED volume + camera tracking + Unreal Engine) and how indie filmmakers can approximate it. Shows that the right creative solution is often cheaper and more convincing than a large-budget CG approach.

### Key Techniques Covered
1. **Practical camera speed manipulation** — low shutter speed + reduced frame rate + real movement = natural motion blur; playback at 24fps makes normal-speed movement appear faster/stylized; the film grain and blur are real, not added in post
2. **Prop + environmental physics** — actress in a wheelbarrow pushed backwards + leaf blower = authentic hair/clothing movement + realistic interaction physics; far more convincing than keyed green screen + digital wind
3. **DIY virtual production with LED screens** — place TVs or LED screens beside subject during green screen shoot; they cast environmental light that color-matches the background being composited; eliminates the "floating in a void" look of pure green screen
4. **Professional virtual production** — LED volume (modular LED panels, 360-degree or partial); camera tracking (position sensors on camera + set); computer feeds real-time tracked position to UE engine; engine renders correct parallax/perspective to LED in real-time; result: environment in camera, no post compositing needed for background
5. **Indie approximation of VP** — TVs, projection screens, or projector directly on subject; works for color/light matching even without true parallax-correct rendering

### UE Relevance
- Virtual production uses Unreal Engine as the real-time background renderer on LED volumes
- Genesis (Boundless's own plugin) provides the camera tracking layer for affordable virtual production setups
- For post-composite workflow (without LED volume): see compositing tutorial series

### Difficulty
Beginner (filmmaking philosophy + technique context, no UE steps)

### UE Version
UE 5.x

### Tags
`#vfx` `#filmmaking` `#virtual-production` `#compositing` `#cinematography` `#beginner`

---

## Related Entries
- [[why-modern-vfx-suck-and-how-to-make-yours-not-suck]] — Part 1 of the series (critiques)
- [[why-modern-vfx-suck-and-how-to-make-yours-not-suck-part-2---transformers-vs-marv]] — Part 2: Transformers vs Marvel case studies
- [[no-cost-virtual-production-is-here---and-its-changing-filmmaking]] — virtual production accessibility manifesto
- [[the-5-secrets-to-hollywood-level-visual-effects-with-no-budget]] — 5 principles from low-budget winners
- [[3d-tracking-natively-in-unreal-engine---full-tutorial]] — Genesis camera tracking for virtual production
