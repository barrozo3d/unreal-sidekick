---
title: Unreal Engine for Filmmakers - How to Make your Lighting CINEMATIC
source: YouTube
url: https://www.youtube.com/watch?v=SMCTeoj9YaA
author: Boundless Entertainment
ingested: 2026-06-16
plugin_version: none
ue_version: "UE 5.x"
tags: [lighting, lumen, fog, atmospherics, sequencer, cinematography, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic/
frame_count: 9
---

# Unreal Engine for Filmmakers - How to Make your Lighting CINEMATIC

**Source:** [YouTube](https://www.youtube.com/watch?v=SMCTeoj9YaA)
**Author:** Boundless Entertainment
**Duration:** 10m55s | 9 section(s)

---

## Structured Notes

### Core Technique
Night scene cinematographic lighting in UE5: "full moon" hard directional key light placed from the shadow side of camera; Exponential Height Fog with volumetric fog; Light Shaft Occlusion for god rays visible when camera faces toward the light. Lumen indirect lighting bounce control via Indirect Lighting Intensity parameter.

### Summary
11-minute lighting tutorial covering cinematic night scene setup with god rays/light shafts. Two lighting styles for night scenes are mentioned — soft overcast and hard full-moon (this video covers full-moon). Steps: HDRI night sky texture on Sky Light (low intensity) for skybox; Directional Light for the key (moonlight); rotate using E (rotation gizmo); lighting theory: shoot from the shadow side (camera faces light direction for rim lighting on scene geometry); Source Angle on directional light controls shadow softness (2.5 = soft); Indirect Lighting Intensity = Lumen bounce amount (0 = no bounce, higher = more GI fill); Exponential Height Fog > Volumetric Fog ON; Scattering Color = white; Fog Height FOG = 2 (keeps fog out of sky); Light Shaft Occlusion ON on directional light = god rays appear when objects block direct light path from light to camera.

### Key Steps
1. **Sky setup** — Sky Light > Cubemap > assign HDRI night sky texture; reduce Intensity to 0.1–0.3 (dim star field only; don't overpower the moonlight key)
2. **Directional light (moonlight)** — Place Actor > Directional Light; drag into scene; white to cool blue tint; Intensity ~10–15
3. **Position key light** — hit E (rotation gizmo) on directional light; rotate to desired angle; lighting theory: position so camera is shooting from the shadow side — the lit side of objects is away from camera, creating rim/edge light on geometry edges
4. **Source Angle** — Directional Light > Source Angle = 2.5 (slightly soft moonlight shadows vs. razor-sharp sun)
5. **Lumen bounce** — Directional Light > Indirect Lighting Intensity: 0 = no GI bounce; 0.3–0.5 = subtle ambient fill in shadow areas (Lumen calculates; more bounce = brighter shadow fill)
6. **Exponential Height Fog** — Place Actor > Exponential Height Fog; Fog Inscattering Color = white; Fog Density = adjust to taste; Fog Height Falloff = ~2 (keeps fog near ground, clear sky)
7. **Volumetric Fog ON** — Exponential Height Fog > Volumetric Fog = true; Scattering Distribution controls density of light response in fog
8. **God rays (Light Shaft Occlusion)** — Directional Light > Light Shaft Occlusion = ON; camera must face toward the light with a dark area (shadow) behind the lit zone; objects that block the directional light path create occlusion zones; fog scatters around them = god rays
9. **Camera angle for god rays** — point cine camera toward light source; dark background (shadowed area) is required; direct line of sight to light source = peak visibility of rays

### UE Systems / Blueprints / Settings
- **Sky Light** — Place Actors > Lights > Sky Light; Cubemap mode: assign HDRI texture for skybox; controls ambient environment illumination
- **Directional Light** — Intensity (lux): ~13; Source Angle: shadow softness (2.5 = soft moon); Indirect Lighting Intensity: Lumen bounce multiplier; Light Shaft Occlusion: ON for god rays
- **Indirect Lighting Intensity** — Lumen global illumination multiplier on this light; 0 = direct lighting only; higher = more light bounced off surfaces
- **Exponential Height Fog** — height-based atmospheric fog; Volumetric Fog ON = enables light scattering in fog for god rays + volumetric depth
- **Light Shaft Occlusion** — Directional Light feature; requires camera to face light source + dark background; occlusion from objects between camera and light creates volumetric crepuscular rays through fog

### Difficulty
Intermediate

### UE Version
UE 5.x (Lumen GI era)

### Tags
`#lighting` `#lumen` `#fog` `#atmospherics` `#sequencer` `#cinematography` `#intermediate`

---

## Related Entries
- [[unreal-engines-secret-weapon-for-cinematic-lighting]] — LightForge 2.0 gobo lighting setup
- [[unreal-engine-depth-fog-tutorial-path-traced]] — depth fog and fog cards in Path Tracer
- [[unreal-engine-for-filmmakers---cinematic-camera-settings-setting-up-virtual-came]] — camera settings companion
- [[dune-cinematography-breakdown-how-to-get-the-dune-look]] — cinematic lighting reference (Dune atmosphere)
