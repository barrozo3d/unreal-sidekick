---
class: operational
verified: n/a
sources:
  - https://www.unrealengine.com/en-US/release-notes
  - https://dev.epicgames.com/documentation/unreal-engine/whats-new
last_verified: never
version_basis: "unknown"
---
# Unreal Engine Version Tracker

**last_checked:** 2026-06-18
**current_stable:** UE 5.8

## Known Versions

| Version | Release | Release Notes File | Status | Key Features |
|---------|---------|-------------------|--------|--------------|
| UE 5.8 | 2026-06-17 | `references/release-notes-ue58.md` | Ingested (synthesized) | MegaLights prod-ready, MRG fully prod-ready, Accumulation DOF prod-ready, Animation Mixer Experimental, MetaHuman Crowd Experimental, Control Rig Dynamics prod-ready, MCP Server plugin Experimental, Skeletal Editor blendshape tools, Audio Subtitles Beta, MetaSound Pages, WASAPI. **Last planned major UE5 release before UE6.** |
| UE 5.7 | 2026 | (current docs — no separate page) | Previous stable | All docs on dev.epicgames.com are 5.7 |
| UE 5.6 | 2025 | `tutorials/unreal-engine-57-release-notes.md` | Ingested (sparse) | Movie Render Graph prod-ready, Substrate prod-ready, Modular Control Rig prod-ready, MegaLights improvements |
| UE 5.5 | 2024 | `tutorials/unreal-engine-55-release-notes.md` | Ingested (full) | Dynamic Sequencer, Animation Layers, Optimized MetaHumans + MetaHuman Component, MegaLights Experimental, Path Tracer prod-ready, Modular Control Rig Beta |
| UE 5.4 | 2024 | `tutorials/unreal-engine-5-4-release-notes.md` | Ingested (sparse) | Motion Design module, PCG v2, Nanite Displacement Experimental, Movie Render Graph Early Access, Modular Control Rig Experimental |
| UE 5.3 | 2023 | (not yet ingested) | — | Substrate materials Experimental, GPU Lightmass improvements, Lumen improvements |
| UE 5.2 | 2023 | (not yet ingested) | — | PCG framework (first introduction), Procedural Content Generation |
| UE 5.1 | 2022 | (not yet ingested) | — | Lumen hardware raytracing, Nanite tessellation preview |
| UE 5.0 | 2022 | (not yet ingested) | — | Lumen, Nanite, MetaHuman, World Partition, Chaos Physics stable |

## Feature Version Matrix

| Feature | Introduced | Production Ready | Notes |
|---------|-----------|-----------------|-------|
| Lumen | UE 5.0 | UE 5.0 | HWRT improvements in 5.5 |
| Nanite | UE 5.0 | UE 5.0 | Displacement Experimental in 5.4 |
| World Partition | UE 5.0 | UE 5.0 | HLOD improvements in 5.2+ |
| MetaHuman | UE 5.0 | UE 5.0 | Optimized pipeline in 5.5; MetaHuman Component in 5.5 |
| Control Rig | UE 4.26 | UE 5.0 | Modular Control Rig Experimental 5.4, Beta 5.5, Prod 5.6 |
| PCG | UE 5.2 | UE 5.3 | v2 in 5.4; GPU Processing Beta in 5.7 |
| Substrate Materials | UE 5.2 (Exp) | UE 5.6 | Replaces legacy material model |
| Path Tracer | UE 5.0 | UE 5.5 | Spatio-Temporal denoiser in 5.5 |
| Movie Render Graph | UE 5.4 (EA) | UE 5.8 | Fully prod-ready in 5.8; audio export improved 5.8 |
| Accumulation DOF | UE 5.5 (Exp) | UE 5.8 | Filmic depth-of-field via accumulated renders |
| Animation Mixer | UE 5.8 (Exp) | — | Layer/mask animations in Sequencer without AnimBP |
| MetaHuman Crowd | UE 5.8 (Exp) | — | Optimized instanced MetaHumans at scale |
| Control Rig Dynamics | UE 5.6 | UE 5.8 | Cosmetic secondary motion; 5× faster in 5.8 |
| MetaHuman Animator Audio-Driven | UE 5.8 | UE 5.8 | Audio-only facial animation without face capture session |
| MCP Server Plugin | UE 5.8 (Exp) | — | AI model ↔ UE editor integration |
| Audio Subtitles | UE 5.8 (Beta) | — | Native subtitle system in Sequencer |
| MegaLights | UE 5.5 (Exp) | UE 5.8 | Production ready as of 5.8 |
| Motion Design | UE 5.4 | UE 5.4 | Cloners, effectors, Rundown graph |
| ML Deformer | UE 5.1 | UE 5.3 | Mask painting added 5.5 |
| Modular Control Rig | UE 5.4 (Exp) | UE 5.6 | Module Variants in 5.5 |
| Chaos Cloth | UE 5.0 | UE 5.1 | ML Cloth added 5.3 |
| Hair Strands (Groom) | UE 4.26 | UE 5.0 | Art Directability added 5.x |
| nDisplay / ICVFX | UE 4.x | UE 5.0 | Ongoing improvements each release |

## URL Patterns for Auto-Update
- Release notes: `https://www.unrealengine.com/en-US/release-notes`
- Documentation: `https://dev.epicgames.com/documentation/unreal-engine/whats-new`
