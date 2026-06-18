---
title: MetaHumans for Mocap | Unreal Engine Animation Hub
source: YouTube
url: https://www.youtube.com/watch?v=myxrzJiLc6I
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["metahuman", "animation", "mocap", "blueprint", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/metahumans-for-mocap-unreal-engine-animation-hub/
frame_count: 4
---

# MetaHumans for Mocap | Unreal Engine Animation Hub

**Source:** [YouTube](https://www.youtube.com/watch?v=myxrzJiLc6I)
**Author:** Unreal Engine
**Duration:** 6m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome to Animation Hub. Today we're going to be looking at how to set up a meta-human for MoCAP manager. So we can't just use them straight out the box. We do need to make a new version of them basically. It needs to be inheriting from their Capture Character class. So I've got my meta-human here and let's just open that up. As you can see we've got the various components and so we're going to create a new blueprint. We're going to make it of Capture Character. There we go. You can call this what you want but I quite like Capture Character MH character. So I want just copying the original name. So I'm going to open these both up. We're going to transfer some assets between them. So let's go full screen. First things first, if we get hold of the body and we copy paste or you can shift the right mouse button. Let's go and paste that onto the Skeletal Mesh asset top slot there. So we've got our arms and legs in. Next let's go and get the rest of the Skeletal Mesh and the groom. So let's select these controls C and then let's paste these over. And so there we go. So we've basically copied that blueprint but it's of a different inherited class. It's parent class is different I should ...

**Frame:** tutorials\frames\metahumans-for-mocap-unreal-engine-animation-hub\frame_000.jpg


---

## Structured Notes

### Core Technique
Setting up a MetaHuman for Mocap Manager — creating a `CaptureCharacter`-derived Blueprint that inherits the MetaHuman's skeletal mesh components, enabling real-time mocap streaming.

### Summary
Animation Hub tutorial on adapting a MetaHuman for use with Mocap Manager live capture. The standard MetaHuman Blueprint cannot be used directly — a new Blueprint inheriting from `CaptureCharacter` must be created, and the Skeletal Mesh components (body, head, groom, clothing) manually copied over. The resulting actor can then receive Live Link data from Mocap Manager for real-time face and body capture.

### Key Steps
1. Open your MetaHuman Blueprint in the editor
2. Create a **New Blueprint Class** → parent class: `CaptureCharacter` (search for it in the class picker)
3. Name the new BP (e.g. `CaptureCharacter_MH_[CharacterName]`)
4. Open both the original MetaHuman BP and the new CaptureCharacter BP side-by-side
5. From the MetaHuman BP: **copy** the `Body` Skeletal Mesh component → paste into the new BP's component hierarchy
6. Copy all remaining Skeletal Mesh components (face, torso accessories, groom) → paste into new BP
7. Verify all mesh assets are correctly assigned in the Details panel of each component
8. Set the **LOD Sync** and **Animation Blueprint** references to match the original MetaHuman
9. Place the new `CaptureCharacter` BP in the level → point Live Link source at it for mocap streaming

### UE Systems / Blueprints / Settings
`CaptureCharacter` class → base class for MetaHumans used with Mocap Manager; enables Live Link body/face
`Blueprint Class → Reparent` or new → inherit from CaptureCharacter
Skeletal Mesh components (Body, Face, Torso, Groom) → must be manually copied from original MetaHuman BP
`Live Link` → connects Mocap Manager capture data to the CaptureCharacter BP
`LOD Sync` → synchronize LOD levels across all MetaHuman mesh components

### Difficulty
Intermediate

### UE Version
UE5

### Tags
metahuman, animation, mocap, blueprint, intermediate

---

## Related Entries
- `references/metahuman-reference.md` — MetaHuman setup, LOD, animation
- `tutorials/metahuman-realtime-animator-best-practices-unreal-engine-animation-hub.md` — webcam MetaHuman Animator
- `tutorials/live-link-hub-tips-unreal-engine-animation-hub.md` — Live Link Hub setup