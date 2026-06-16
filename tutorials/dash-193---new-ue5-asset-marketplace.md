---
title: DASH 1.9.3 - NEW UE5 ASSET MARKETPLACE
source: YouTube
url: https://www.youtube.com/watch?v=YHmNyyI998k
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.9
ue_version: "UE 5.x"
tags: [dash-1.9, release-notes, marketplace, content-library, dekogon, ambientcg, scatter, beginner]
extraction_status: complete
frames_dir: tutorials/frames/dash-193---new-ue5-asset-marketplace/
frame_count: 7
---

# DASH 1.9.3 - NEW UE5 ASSET MARKETPLACE

**Source:** [YouTube](https://www.youtube.com/watch?v=YHmNyyI998k)
**Author:** Polygonflow Dash
**Duration:** 8m19s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

[...raw data omitted — see ingested file...]

---

## Structured Notes

### Core Technique
Dash 1.9.3 release overview — major additions: Dash Marketplace (individual asset purchasing directly in Content Browser), Dekogon Library integration (first marketplace seller; individual assets at 4 license tiers), Sierra Division (Explorer's Room Pack free for limited time), ambientCG integration (free textures/atlases/HDRIs), per-instance size in scatter table, Mesh Convex Hull Tool upgrade for game collision.

### Summary
8-minute release video for Dash 1.9.3. Key additions: (1) Dash Marketplace — browse and buy individual assets from third-party vendors directly in Dash Content Browser; free Content Browser license also grants Marketplace access. (2) Dekogon Library — first seller; thousands of individual high-quality assets; add to cart → 4 license tiers (Personal/Indie/Studio/Enterprise) → purchase → import; avoids expensive bulk packs. (3) Sierra Division — Explorer's Room Pack offered free for limited time via Sierra Division tab. (4) ambientCG Library — free PBR textures, tileable atlases, and HDRIs integrated; download → Ctrl+drag 3 textures → Apply Blend Material; drag HDRIs; scatter atlases. (5) Scatter Improvements — per-instance scale control now available directly in scatter table for surface scatters. (6) Mesh Convex Hull Tool — create and control convex hulls around static meshes and scatter instances for game collision; params: count, height; Compute → test in Play Mode → enable Hide to hide hulls.

### Key Steps
1. **Dash Marketplace access** — open Dash Content Browser → Marketplace button → browse vendor tabs (Dekogon, Sierra Division, etc.); free Content Browser license also grants Marketplace access
2. **Dekogon asset purchase** — open Dekogon tab → scroll/search → select assets → Add Selected to Cart → view cart total → Purchase → License Selection (Personal/Indie/Studio/Enterprise) → Confirm → assets download and import automatically
3. **Sierra Division free pack** — switch to Sierra Division tab → download Explorer's Room Pack for free (limited time)
4. **ambientCG Library** — open Dash Content Browser → ambientCG tab → browse/download textures/atlases/HDRIs → for Blend Material: Ctrl+drag 3 textures onto surface → Apply Blend Material; drag HDRI to scene; scatter atlases like any other asset
5. **Per-instance size in scatter table** — select scatter tool → Scatter Table → individual rows have Size column; adjust per-instance to create natural variety
6. **Mesh Convex Hull Tool** — search `convex hull` → assign scatter instance → set Count + Height → Compute → test in Play Mode (blocks character from entering scattered meshes) → Enable Hide Adoption when happy

### UE Systems / Blueprints / Settings
- **Dash Marketplace** — accessible from Content Browser Marketplace button; individual asset purchases; free CB license = free marketplace access; in-app purchase flow with cart + license selection
- **Dekogon integration** — 4 license tiers: Personal/Indie/Studio/Enterprise; individual asset pricing; auto-download + import on purchase
- **Sierra Division tab** — Explorer's Room Pack free (limited time); premium asset vendor
- **ambientCG Library** — free PBR textures, atluses, HDRIs; download icon in CB; Ctrl+drag 3 → Apply Blend Material; HDRI drag-to-scene supported; atlas scatter supported
- **Scatter Table per-instance size** — individual scale override per instance row in surface scatter table
- **Mesh Convex Hull Tool** — count + height params; Compute → generates hulls around selected scatter instances; Play Mode collision test; Enable Hide Adoption to hide hulls after verification

### Difficulty
Beginner

### UE Version
UE 5.x (Dash 1.9.3)

### Tags
`#dash-1.9` `#release-notes` `#marketplace` `#content-library` `#dekogon` `#ambientcg` `#scatter` `#beginner`

---

## Related Entries
- [[dash-192---new-ue5-tools-amazon-3d-library-integration]] — 1.9.2 ABO + Mesh Pattern + rainfall
- [[best-free-unreal-engine-5-asset-management-plugin-in-2025]] — Full Dash 1.9 Content Browser overview
- [[dash-19---managing-assets-in-ue5-just-got-a-lot-easier]] — 1.9 base release
- [[creating-a-blend-material-in-unreal-engine-5-just-got-easier]] — Blend Material tool detail
