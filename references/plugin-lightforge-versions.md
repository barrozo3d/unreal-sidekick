# LightForge — Version History & Compatibility Reference

**Plugin:** LightForge (Cinematic Lighting & Filmmaking Plugin for UE5)
**Developer:** Boundless Entertainment
**Website:** https://boundless-resource.com
**Resource Hub:** https://boundless-resource.com/lightforgehub/
**Store:** Boundless Entertainment website (not on Fab)
**Platform:** Windows only (Mac/Linux "on its way" as of 2026)

> **Context:** Boundless Entertainment's YouTube channel (@BoundlessEntertainmentFilms) covers both LightForge tutorials AND general UE5 filmmaking techniques. Not every video from this channel is LightForge-specific — many cover path tracing, compositing, VFX in standard UE5.

---

## Version Compatibility Matrix

| Version | UE Support | Notes |
|---|---|---|
| LightForge 1.x (original) | UE 5.2, 5.3, 5.4, 5.5 | Windows only |
| LightForge 2.0 (current) | **UE 5.6, 5.7** | Windows only; NOT backward-compatible with UE 5.5 and earlier |

> **Breaking compatibility:** LightForge 2.0 **drops support for UE 5.5 and earlier**. Tutorials recorded on LightForge 1.x in UE 5.2–5.5 will show a different UI and feature set. Always check the UE + LightForge version combination shown in a video.

---

## LightForge 2.0 (Current — 2026)
**Theme:** Comprehensive centralized filmmaking console

**Supported UE:** 5.6, 5.7 (Windows only)

### Core Features
**Lighting System:**
- 30+ Lighting Presets — instant cinematic lighting setups
- 100+ static and looping Gobo Textures with customizable master material
- Dynamic lighting, sky, clouds, and look control from a centralized console
- Save, export, and share custom lighting setups between projects

**Camera System:**
- 30+ industry-standard camera presets (easy matching to real cameras)
- 20+ LUTs for in-engine color grading; includes `.cube` files for DaVinci Resolve
- Cinematic render presets with built-in rendering guide

**Optimization Tools:**
- One-click scene optimization for Nanite, Lumen, Path Tracing, Volumetric Fog
- One-click project setup for Path Tracing and Hardware Ray Tracing
- "Highest quality in 3 clicks" render preset workflow
- Compatible with existing Unreal Engine projects (non-destructive)

**Central Console:**
- Control scenes, cameras, and Post Process Volumes from single unified interface
- Designed for filmmakers who want to work without deep UE knowledge

### Included Resources
- Step-by-step guides
- Full training course
- Rendering guide
- Priority email support

---

## LightForge 1.x (Legacy)
**Supported UE:** 5.2, 5.3, 5.4, 5.5 (Windows only)

The original LightForge established the core concept: a centralized filmmaking UI to streamline UE5 lighting, cameras, and rendering. Specific feature list for v1.x is not publicly documented, but includes:
- Basic lighting presets
- Camera presets
- LUTs
- Render optimization shortcuts

Tutorials from the early Boundless channel (2022–2024) typically show LightForge 1.x.

---

## Plugin Identification in Tutorials

Look for these UI cues to identify the LightForge version in a video:
- **UE version shown in title bar** — 5.6/5.7 = almost certainly LightForge 2.0; 5.2–5.5 = LightForge 1.x
- **"LightForge 2.0" mentioned explicitly** in title or transcript
- **UI panel style** — 2.0 has a more unified console layout

Tutorials NOT using LightForge at all: path tracer tutorials, compositing tutorials, general rendering tips from this channel can apply to standard UE5 without any plugin.

---

## How to Cross-Reference Tutorials

When extracting a Boundless/LightForge tutorial:
1. Check if LightForge is actually used (many Boundless videos are pure UE5 technique)
2. If LightForge is used, identify 1.x vs. 2.0 from the UE version and UI
3. Note specific LightForge features shown (presets used, LUTs, optimization buttons)
4. Flag UE version compatibility clearly — 2.0 users on UE 5.5 cannot use 2.0 features

**Key flags:**
- `lightforge-1x` — UE 5.2–5.5 era tutorials
- `lightforge-2x` — UE 5.6–5.7 era tutorials; centralized console shown
- `ue5-filmmaking` — Boundless tutorials with no LightForge dependency (pure UE5)
