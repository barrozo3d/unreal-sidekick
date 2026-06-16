# Black Eye Cameras — Version History & Compatibility Reference

**Plugin:** Black Eye Cameras (Procedural & Dynamic Camera System for UE5)
**Developer:** Black Eye Technologies
**Contact:** info@blackeyetechnologies.com
**Website:** https://blackeyetechnologies.com
**Store:** Fab.com (paid)
**Platform:** Windows (primary); UE 5.1–5.7+

---

## Version Compatibility Matrix

| Version | UE Support | Key New System | Notes |
|---|---|---|---|
| 1.0 | UE 5.x | Core camera system | Initial release — follow, look-at, orbit modules |
| 1.1 | UE 5.x | Cross Camera, Multi-Subject LookAt | Keyable weights in Sequencer; version 1.1 was major update |
| 1.1.1 | UE 5.x | Keyable Weights in Sequencer | Bug fixes + Sequencer weight keyframing |
| 1.1.7 | UE 5.x | Cam Switcher + Pilot mode | Camera switching system |
| 1.2 | UE 5.x | Shot List module | Preview/plan shots before executing |
| v2.0 | UE 5.4+ (estimated) | Full gameplay camera system | Complete rewrite; adds high-level blending, orbit cameras, aim methods, priorities, collision, Camera Manager |
| v2.x (current) | UE 5.6–5.7 | Full system (gameplay + cinematics) | Includes car cameras, dynamic dialog, top-down, etc. |

> **Critical note:** v2.0 is a significant architectural rewrite — tutorials from v1.x cover a different API. Features like Camera Manager, gameplay camera priorities, and collision handling are v2 exclusive. Always check which version is shown.

---

## Version Notes

### Black Eye v2.x (Current — 2025/2026)
**Theme:** Full gameplay + cinematic camera unification

**What's New vs. v1.x:**
- **High-level camera blending** — smooth transitions between any camera state
- **Orbit cameras** — planetary-style orbit with configurable radius/speed
- **Aim methods** — multiple targeting strategies (soft lock, hard lock, free aim)
- **Camera priorities** — priority system determines which camera is active at any moment
- **Collision avoidance** — cameras respond to world geometry automatically
- **Camera Manager** — centralized manager for multi-camera setups
- **Gameplay camera presets:**
  - **Dynamic Dialog** — conversational camera switching between characters
  - **Top Down** — isometric/top-down perspective camera
  - **Car Camera** — vehicle-following with gameplay and cinematic modes
  - **Follow Component: Dwell Radius** — camera lingers/orbits at a set distance
  - **2-person combat side camera** — side-scrolling fighter-style
- **Gameplay cameras milestone** — new in v2, allowing complete camera control for games (not just cinematics)

---

### Black Eye v1.2
**New:** Shot List module — preview and plan shots before camera setup; visible in v1.2 Preview tutorials

---

### Black Eye v1.1.7
**New:** Cam Switcher + Pilot mode — switch between multiple camera setups; Pilot mode for direct control

---

### Black Eye v1.1.1
**New:** Keyable Weights in Sequencer — animate camera blend weights directly on Sequencer tracks

---

### Black Eye v1.1
**Theme:** Major feature expansion

**New Features:**
- **Cross Camera** — blend across multiple camera setups simultaneously
- **Multi-Subject LookAt Weights** — per-subject weight controls when tracking multiple actors
- **Version 1.1 New Features HYPE** video = announcement of 1.1 feature batch

---

### Black Eye v1.0 (Initial Release)
**Core modules:**
- Follow module — camera follows a target with configurable offset
- LookAt module — camera always points at a subject
- Orbit module (basic) — camera orbits around a point
- Bake down cam anims — export camera animations to standard Sequencer tracks
- Multiple targets on a character — track different bones/components
- Multiple follow + look-at modules on one camera

---

## Core Concepts (All Versions)

**Modules system:** Black Eye cameras are built from stackable modules (Follow, LookAt, Orbit, etc.) rather than a monolithic camera actor. Each module has a Weight parameter — you can blend between behaviors by keyframing weights in Sequencer.

**Bake workflow:** After prototyping a shot with Black Eye cameras, use "Bake down cam anims" to convert the result to standard Sequencer camera animation tracks — makes it portable without the plugin.

**Speed of Thought philosophy:** The plugin is designed for rapid shot prototyping — get a complex shot (like the "Millennium Falcon shot" example) in 7 keyframes. Iteration speed is the core value proposition.

---

## How to Cross-Reference Tutorials

When extracting a Black Eye tutorial:
1. Identify the plugin version from video title, UI appearance, or transcript
2. Note which modules/features are shown
3. Flag if a feature is v1-only (now replaced in v2) or v2-only
4. Note the UE version used in the tutorial

**Key flags:**
- `blackeye-v1` — Follow, LookAt, Orbit, Bake; Shot List (1.2); Switcher (1.1.7)
- `blackeye-v2` — Gameplay cameras, Camera Manager, Collision, Car/Dialog/TopDown presets
- `blackeye-v1-sequencer` — Keyable Weights (1.1.1+), Cam Switcher (1.1.7+)
