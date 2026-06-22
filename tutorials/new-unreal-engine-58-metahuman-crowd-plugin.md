---
title: New Unreal Engine 5.8 Metahuman Crowd Plugin
source: YouTube
url: https://www.youtube.com/watch?v=bJIPlvmoTVw
author: Smart Poly
ingested: 2026-06-22
ue_version: "5.8"
tags: [metahuman, mass, optimization, lod, overview]
extraction_status: complete
frames_dir: tutorials/frames/new-unreal-engine-58-metahuman-crowd-plugin/
frame_count: 0
---

# New Unreal Engine 5.8 Metahuman Crowd Plugin

**Source:** [YouTube](https://www.youtube.com/watch?v=bJIPlvmoTVw)
**Author:** Smart Poly
**Duration:** 9m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello guys, welcome back to another video. Epic Games just officially dropped on religion 5.8, and along with it they introduced a brand new feature called the MetaHuman crowd plugin. The MetaHuman crowd plugin allows you to assemble optimized instances of MetaHuman characters to create crowds simulated by mass, scaling from the tens to thousands of characters. The new experimental plugin provides a complete assembly pipeline with seamless transitions between high fidelity actors and low fidelity instance skeletal meshes based on camera distance. And in this video we'll be checking out the new MetaHuman crowd plugin, the sample project, which is currently free to download on fab, and I'll actually show you guys how to get your hands on it. Also before we get into the video, I just released my new Unreligion masterclass course bundle. I just launched a brand new Unreligion masterclass course, this bundles together all of my courses showing you how to make games inside of Unreligion. This masterclass course has over 150 plus hours of learning content, and I will show you how to make eight different games from complete scratch. You'll master multiplayer networking, survival mechanics,...



---

## Structured Notes

### Core Technique
Overview of UE 5.8's new experimental MetaHuman Crowd plugin, which uses Mass (Unreal's data-oriented crowd/AI framework) to simulate optimized crowds of MetaHuman characters scaling from tens to thousands, with automatic high-fidelity-to-low-fidelity LOD transitions based on camera distance.

### Summary
Smart Poly covers Epic's new MetaHuman Crowd plugin, released alongside UE 5.8. The plugin assembles optimized instances of MetaHuman characters into Mass-simulated crowds ranging from a handful of characters to thousands. Its core feature is a complete assembly pipeline that seamlessly transitions each character between a high-fidelity full actor and a low-fidelity instanced skeletal mesh depending on distance from the camera, keeping large crowds performant without an obvious quality drop up close. The video walks through the free sample project available on Fab and shows how to download and access it. (Transcript truncated by ingestion at ~1200 characters; the hands-on setup/configuration steps shown later in the video were not captured here and would need a follow-up pass for full step-by-step detail.)

### Key Steps
1. [Context] Understand the MetaHuman Crowd plugin's purpose: Mass-simulated crowds of MetaHuman characters from tens to thousands
2. [LOD pipeline] Recognize the automatic high-fidelity-actor to low-fidelity-instanced-mesh transition driven by camera distance
3. [Sample project] Download the free MetaHuman Crowd sample project from Fab
4. [Explore] Open the sample project to see the assembly pipeline and crowd setup in practice (exact configuration steps not captured in available transcript)

### UE Systems / Blueprints / Settings
- MetaHuman Crowd plugin (experimental, UE 5.8) — assembles optimized MetaHuman character instances into Mass-simulated crowds
- Mass framework — Unreal's data-oriented entity/crowd simulation system underlying the plugin's scaling to thousands of characters
- Distance-based LOD transition — seamless swap between high-fidelity actors and low-fidelity instanced skeletal meshes based on camera distance
- Fab marketplace — source of the free MetaHuman Crowd sample project

### Difficulty
Beginner

### UE Version
5.8

### Tags
metahuman, mass, optimization, lod, overview

---

## Related Entries
- [Unreal Engine 5.8 NEW Markerless Motion Capture Tutorial](unreal-engine-58-new-markerless-motion-capture-tutorial.md) — another MetaHuman-related UE 5.8 feature, covering markerless mocap rather than crowd simulation
- [How Unreal 5.8 Changed Filmmaking](how-unreal-58-changed-filmmaking.md) — broader UE 5.8 feature roundup mentioning Megalights and other crowd/performance-relevant updates
