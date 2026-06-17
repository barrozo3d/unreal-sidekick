---
title: EASIEST VFX pipeline EVER with Composite Mesh Actors in Unreal Engine 5.7 (Composure EP1)
source: YouTube
url: https://www.youtube.com/watch?v=6he5ag3nLjs
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-17
ue_version: "5.7"
tags: ["Composure", "composite mesh actor", "camera projection", "virtual production", "media profile", "live feed", "image sequence", "green screen", "blue screen", "3D compositing", "filmmaking"]
extraction_status: complete
frames_dir: tutorials/frames/easiest-vfx-pipeline-ever-with-composite-mesh-actors-in-unreal-engine-57-composu/
frame_count: 10
---

# EASIEST VFX pipeline EVER with Composite Mesh Actors in Unreal Engine 5.7 (Composure EP1)

**Source:** [YouTube](https://www.youtube.com/watch?v=6he5ag3nLjs)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 33m1s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en So, since my last video, I've got a new pet. [music] And uh his name's Rover, and uh he's a bit bitey, so be careful. All right. I haven't. Um we're in Unreal Engine 5.7, and I'm using the new composure feature, which is basically 3D camera projections in the viewport. So, you take the feed from the camera and you project it into a representation of this environment, and it lands on those surfaces, and you can put objects in between them. And it's really fun. And I'm going to give you a breakdown of how I do that. Um, it'll also work with it. Right now it's live, so this is um using a live feed, but it will work with image sequences and you can also do the blue screen and green [music] screen extractions with it and put that into environments as well. That'll be on the second video. But on this first one, I just wanted to kind of get on with it and show you a basic setup using a locked off camera. If you've got lots of money and you're a studio and you can afford like a Mars system, then you can hook all this up, too. Um but um I can't. All right, so let's get on with the video. So I'm going to come out of the main camera, which is you, and just show you...

**Frame:** tutorials\frames\easiest-vfx-pipeline-ever-with-composite-mesh-actors-in-unreal-engine-57-composu\frame_000.jpg


---

## Structured Notes

### Core Technique
Using UE 5.7's Composure plugin with a Composite Actor and camera projection to place live or pre-recorded footage onto curved 3D mesh geometry inside an Unreal scene — replacing the old flat "green screen card" approach with a depth-aware, shadow-casting, fog-interactive projection surface.

### Summary
This is Composure Episode 1 from Dean Yurke's virtual production series. He introduces the Composure workflow in UE 5.7 where a camera feed (live USB or pre-recorded image sequence) is projected from the scene's cine camera onto a curved Composite Mesh Actor, rather than placed on a flat card. This lets the subject's projected image interact with the scene's depth of field, exponential height fog, and other volumetric effects since it sits at a real position in 3D space. For a locked-off camera, the setup is straightforward: place the Composite Mesh Actor where the subject stands, associate it with the scene camera via the Composite Actor, and the footage maps naturally. He also covers using a Media Profile for swappable live sources, demonstrates projecting onto arbitrary mesh shapes (including a wolf character), and notes that the second episode will cover green/blue screen extractions. This episode focuses on using a raw live feed without keying.

### Key Steps
1. Ensure Composure plugin is enabled (Edit > Plugins > Composure).
2. Open Window > Virtual Production > Composure; Place a Composite Actor in the scene.
3. In the Composite Actor details, associate it with the scene camera (Camera Component selection).
4. For live feeds: create a Media Profile (media source URL or USB device) and assign it to the plate layer's signal input.
5. Go to the Plate Layer on the Composite Actor; set signal input to the active Media Profile.
6. Place a Composite Mesh Actor in the scene at the location/scale where the subject stands.
7. Drag the Composite Mesh Actor into the Composite Actor's plate layer composite mesh content slot; right-click → Apply Unlit Material.
8. Look through the scene camera — the footage now projects onto the mesh geometry with correct perspective.
9. To project onto custom shapes: select any scene object → right-click → Apply Unlit Material; assign it as the composite mesh content.
10. For offline/pre-recorded workflows: swap the live Media Profile for an Image Media Source pointing to an EXR sequence folder.

### UE Systems / Blueprints / Settings
- Composure Plugin (Window > Virtual Production > Composure)
- Composite Actor (Plate Layer, Shadow/Reflection Layer)
- Composite Mesh Actor (curved default surface, or any custom mesh)
- Media Profile (swappable live vs. recorded source)
- Image Media Source / File Media Source
- Unlit Alpha Material (applied to composite mesh geometry)
- Cine Camera Actor (associated with Composite Actor for projection origin)

### Difficulty
Intermediate

### UE Version
5.7

### Tags
Composure, composite mesh actor, camera projection, virtual production, media profile, live feed, image sequence, green screen, blue screen, 3D compositing, filmmaking

---

## Related Entries
- `green-screen-cards-are-dead-camera-projections-in-unreal-engine-change-everythin.md` — Episode 2: adds blue screen keying to this same Composure setup
- `green-screen-integration-in-unreal-engine-57-virtual-production-got-even-better-.md` — Episode 3: lit composite mesh material improvements and DaVinci Fusion extraction pipeline
- `green-screen-edge-wrap-secrets-and-a-lie---advanced-davinci-to-unreal-engine-wor.md` — advanced companion: edge wrap utility pass and camera tracking for moving shots
