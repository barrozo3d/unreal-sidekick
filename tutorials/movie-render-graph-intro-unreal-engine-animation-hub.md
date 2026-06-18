---
title: Movie Render Graph Intro | Unreal Engine Animation Hub
source: YouTube
url: https://www.youtube.com/watch?v=0c8-8NSarDI
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE 5.8"
tags: ["rendering", "movie-render-graph", "sequencer", "cinematics", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/movie-render-graph-intro-unreal-engine-animation-hub/
frame_count: 4
---

# Movie Render Graph Intro | Unreal Engine Animation Hub

**Source:** [YouTube](https://www.youtube.com/watch?v=0c8-8NSarDI)
**Author:** Unreal Engine
**Duration:** 11m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hi, welcome to the animation hub. My name is Sean and today we're going to have a look at how to use movie render graph to render out. Shots and layers. We got this cool, a go our project here. We're going to grab a shot of this big guy kind of ripping the doors apart and then it's this cat looking at. Jumping out of the way here. So let's go over here and if you right click and go to cinematic. Movie render graph, you can name it whatever you want. Here and let's double click and let's have a look real quick in movie render graph. So a lot of these nodes and things to look pretty familiar. If you're used to the movie render graph kind of legacy config. The stuff is in here in movie render graph. We just kind of exposed a lot of the more common settings that people are going to want to use. Like warm up settings game overrides game output settings, you know where you can change where where you render to which sort of resolution. Just for any interest of time we're not going to go over every single one. You can find a lot of videos and documentation out there on that. So movie render graph itself. You have your render blobels and then you have your actual layers here. So here is one...

**Frame:** tutorials\frames\movie-render-graph-intro-unreal-engine-animation-hub\frame_000.jpg


---

## Structured Notes

### Core Technique
Movie Render Graph (MRG) node-based render pipeline intro — setting up render globals, defining shot layers, and configuring output — the preferred replacement for legacy Movie Render Queue.

### Summary
Practical intro to Movie Render Graph from the Animation Hub series, using the ACOM sample project. Shows right-clicking a Level Sequence to create an MRG asset, the node graph interface (Render Globals → Output → Layers), configuring warm-up settings and game overrides, setting up per-layer render passes (beauty, cryptomatte, depth), and triggering a render. MRG is fully production-ready from UE 5.8.

### Key Steps
1. In Content Browser, right-click a Level Sequence → `Cinematic → Movie Render Graph` → name and save the asset
2. Double-click the MRG asset to open the node graph
3. The graph has: `Render Globals` node (warm-up, resolution, frame range) → connected to output layers
4. Configure `Render Globals`: set `Warm Up Frame Count` (30–60 for physics/Niagara), `Resolution`, `Output Directory`
5. Add a **Render Layer** node for the Beauty pass; connect to an **EXR Output** or **PNG Output** node
6. Add additional Render Layer nodes for compositing passes: `Cryptomatte`, `Depth`, `Motion Vectors`
7. Set `Game Overrides` node: disable LOD bias, enable high-quality shadows, disable streaming textures
8. Right-click the graph → **Render** or queue multiple sequences
9. Monitor output in `Output Log` → renders save to specified directory

### UE Systems / Blueprints / Settings
`Movie Render Graph` (Content Browser → Cinematic → Movie Render Graph) → node-based render pipeline
`Render Globals` node → warm-up, resolution, frame rate, output path
`Render Layer` node → per-pass render configuration (beauty, depth, cryptomatte)
`Game Overrides` node → disables streaming, enables high-quality settings for render
`EXR Output` / `PNG Output` nodes → file format selection per layer
Fully production-ready from UE 5.8; replaces linear Movie Render Queue

### Difficulty
Intermediate

### UE Version
UE 5.8

### Tags
rendering, movie-render-graph, sequencer, cinematics, intermediate

---

## Related Entries
- `references/sequencer-cinematics.md` — MRQ/MRG settings reference
- `recipes/mrq-multipass-exr.md` — multi-pass EXR setup
- `recipes/cinematics-pipeline.md` — full pipeline Stage 7: render