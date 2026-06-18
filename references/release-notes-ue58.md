# Unreal Engine 5.8 — Release Notes Reference

**Released:** June 2026 (general public)  
**Status:** Current stable as of 2026-06-17  
**Note:** UE 5.8 is the last planned major UE5 release. Epic is ramping toward UE6; UE5 receives bug fixes only after this.

---

## Cinematics & Rendering Highlights (Most Relevant)

### Movie Render Graph — Now Production Ready `[5.8]`
- Fully production-ready (was Early Access in 5.4, prod-ready in 5.6 with caveats, fully stable in 5.8)
- Supports all major preset features with graph-based configuration
- **Light Modifier node**: per-render-layer property overrides for lights, Light Actor Type Condition, variable exposure control
- **Accumulation Depth of Field**: filmic DOF via accumulated deferred renders — eliminates parallax artifacts on hair/groom
- **nDisplay integration**: Movie Render Graph now works with nDisplay collections, modifiers, render layers, deferred and path tracer rendering

### MegaLights — Now Production Ready `[5.8]`
- Was Experimental in 5.5, still Experimental in 5.6/5.7 — **now production-ready in 5.8**
- Reduced noise, improved performance targeting 60fps
- Enhanced debugging tools
- Added transmission support (subsurface scattering through thin geometry)
- Froxel-based translucency support
- IES volumetric light profile support

### Lumen Lite (Beta) `[5.8]`
- New medium-quality GI tier — 2× faster than Lumen High Quality
- Targets 60fps on PS5; uses irradiance fields + probe occlusion
- Good for previz and lower-end platforms while keeping Lumen look

### Fog Screen Space Scattering — FSSS (Experimental) `[5.8]`
- On Exponential Height Fog component
- Approximates multiple light scattering in participating media (fog, smoke, dust)
- Makes dense fog appear blurrier and more physically integrated with scene lighting

### Substrate NPR / Toon Shading (Experimental) `[5.8]`
- Stylized non-photorealistic rendering on Substrate Blendable GBuffer mode
- Supports all light types: local lights, sky lights, Lumen GI
- Ramp-based shading control, dithering, hatching patterns

---

## Character & Animation

### Animation Mixer (Experimental) `[5.8]`
- Layer and mask character animations **directly within Sequencer** — no separate AnimBP or slots needed
- Supports bone matching, offset root motion, transitions between clips
- Major workflow win for mocap polish: layer additive corrections on top of imported mocap

### Sequencer Improvements `[5.8]`
- **Synchronized selection**: selecting in Sequencer also selects in Curve Editor and Viewport (and vice versa)
- **Simplified view mode**: cleaner track layout
- **AutoBaking workflows**: streamlined animation baking directly from Sequencer
- **Audio in Sequencer**: Control Bus and Control Bus Mix tracks for timeline animation; improved MRQ audio support

### Skeletal Editor Blendshape Tools `[5.8]`
- Joint locking during sculpt
- Mesh element selection
- **Morph target mirroring** — critical for facial rigging
- Lattice deformer
- Improved brush behaviors
- Extended Control Rig to support sculpt-driven facial workflows and custom skeletal meshes

### Control Rig Improvements `[5.8]`
- **Control Rig Dynamics**: lightweight particle-based solver for cosmetic physics (hair, cloth secondary motion) — **5× faster** than existing solutions
- **Control Rig Physics (Beta)**: force-based functionality as layered rigs with runtime improvements; new physics modules for Modular Control Rig
- **Direct Mesh Controls (Experimental)**: rig controls rendered directly on skeletal mesh sections for viewport-driven manipulation
- Modular Control Rig: improved hierarchy management, module authoring, connector workflows, new hotkeys, visibility options, mirroring refinements
- **RigMapper (Beta)**: improved node graph for facial animation transfers with expanded remap curves stack

### Retargeting `[5.8]`
- **Foot Definition for Retargeting**: define foot planes and toes for better animation transfers across character types
- **Retarget Override Sets**: single IK Retargeter asset handles different retarget relationships without creating additional assets

---

## MetaHuman `[5.8]`

### MetaHuman Crowd (Experimental)
- New plugin providing **optimized instanced MetaHumans** scaling from tens to thousands of characters
- Seamless LOD transitions — significant upgrade over OverCrowd's MetaHuman-per-agent approach for ultra-large crowds
- Complements OverCrowd for hero/mid-ground agents; can replace Niagara crowd sims for better visual fidelity at scale

### Mesh to MetaHuman
- Convert arbitrary-topology meshes into fully-rigged MetaHumans in a single workflow
- Automatic results — no manual retopo or wrapping required (was previously YVO3D/Faceform Wrap territory)

### Unbaked Textures
- Full control over MetaHuman textures and materials without performance loss
- Custom visual fidelity — override any MetaHuman texture directly

### Body Animation Capture
- **Single camera monocular body capture** for performance inside MetaHuman Animator
- Available standalone and integrated into MetaHuman Animator workflow
- Lower barrier than Move.AI for quick takes

### Improved Solve Quality
- New animation models for better quality across varied capture conditions
- **Audio-driven animation** support in MetaHuman Animator

### Batch Processing
- Improved API for processing large volumes of performance capture data end-to-end

### Platform
- MetaHuman Animator now supports **Linux and macOS**

### Live Link Face Video Streaming
- Real-time video streaming to the engine on iOS/Android
- Simultaneous animation solving on newer devices

---

## Audio `[5.8]`

### Audio Insights — Production Ready
- Loudness metering, signal flow visualization, live monitoring, event logging, plots
- Standalone cache improvements

### Audio Subtitles (Beta)
- Per-platform overrides
- Level Sequence preview without PIE
- Locale-specific duration
- New Blueprint functions

### MetaSound Updates
- **Node Configuration (Experimental)**: dynamic interface configuration, node update transform API, sub-interface layout serialization
- **MetaSound Templates (Experimental)**: property-driven graph generation, custom UMG widget support
- **Format/Channel Agnostic Types (Experimental)**: full pipeline integration, Ambisonics, Wave Player 2.0, CAT Mixer, Grain Player
- Audio in Sequencer: Control Bus/Control Bus Mix tracks

### WASAPI
- New default Windows audio backend replacing XAudio2
- Improved latency, device handling, robustness

---

## AI & MCP `[5.8]`

### MCP Server Plugin (Experimental)
- **Model Context Protocol plugin** — enables Claude (and other AI models) to connect directly to UE projects
- AI can become an active collaborator operating within specific UE workflows
- This skill (Unreal Sidekick) can leverage this in Mode 4 when MCP is enabled

---

## World Building `[5.8]`

### Mesh Terrain (Experimental)
- Next-generation mesh-based terrain system
- Supports overhangs, floating islands, tunnels (not possible with Landscape)
- Interoperable with PCG, World Partition, OFPA
- Nanite + virtual textures + variable tessellation

### PCG Improvements
- Manual editing of PCG data (non-destructive selection/exclusion/modification)
- Complex attributes: arrays, structures, sets, maps
- Embedded subgraphs (like Blueprint functions)
- GPU runtime scatter (matches landscape grass system performance)
- New nodes: align points, scene capture transforms, actor teleport, class extraction

---

## Editor & Workflow `[5.8]`

### Editor Gizmo System
- Unified gizmo framework replacing legacy implementations
- Refined design, improved feedback, expanded screen-space handles
- Rotation delta lines, snapping indicators, interaction presets

### FBX Import Performance
- Experimental uFBX library — faster imports especially on large files with multi-core benefits

### Interchange Import
- USD Import now production-ready for asset import
- Improved Nanite settings, groom attributes on USD import

### Sandboxes
- Isolated workspaces for experimentation
- Changes persist only what you choose, without affecting the main project

### Shortcut Manager
- Refreshed UI, scoped search, keybind search, advanced syntax filtering

### Details Panel Favorites
- Favorite entire categories; optional section filter bar for modified properties

---

## Feature Status Changes Summary

| Feature | Before 5.8 | UE 5.8 |
|---------|------------|--------|
| MegaLights | Experimental (5.5–5.7) | **Production Ready** |
| Movie Render Graph | Prod-ready (5.6) with gaps | **Fully Production Ready** |
| Accumulation DOF | Experimental (5.8 EA) | **Production Ready** |
| Animation Mixer | — | **Experimental** |
| MetaHuman Crowd | — | **Experimental** |
| Mesh Terrain | — | **Experimental** |
| Control Rig Dynamics | — | **Production Ready** |
| Control Rig Physics | — | **Beta** |
| Lumen Lite | — | **Beta** |
| Audio Insights | Beta | **Production Ready** |
| USD Import (Interchange) | Beta | **Production Ready** |
| Mutable | Beta | **Production Ready** |
| Iris Replication | Beta | **Production Ready** |
| MetaSound Templates | — | **Experimental** |
