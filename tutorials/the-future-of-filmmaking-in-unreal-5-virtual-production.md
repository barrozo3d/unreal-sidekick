---
title: The Future of Filmmaking in Unreal 5 (Virtual Production)
source: YouTube
url: https://www.youtube.com/watch?v=56RMmZlDVw4
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [cinematics, pipeline, rendering, beginner]
extraction_status: complete
frames_dir: tutorials/frames/the-future-of-filmmaking-in-unreal-5-virtual-production/
frame_count: 4
---

# The Future of Filmmaking in Unreal 5 (Virtual Production)

**Source:** [YouTube](https://www.youtube.com/watch?v=56RMmZlDVw4)
**Author:** Josh Toonen
**Duration:** 11m56s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** What you're seeing isn't real. This is virtual production. Today, if you're not learning about virtual production, then you're getting left behind. Using Unreal Engine 5, anyone can create virtual environments that can be used on set, even you. But most people misunderstand why virtual production is such a powerful tool. By now, everyone accuses Marvel and other blockbusters of overusing green screen and visual effects. But the problem isn't visual effects or virtual production. It's how they're being used. Make no mistake, virtual production is the future of visual effects in filmmaking. That's why today I'm going to take you behind the scenes of the horror short film I made using virtual production in Unreal Engine 5. So if you want to learn all the secrets and everything I've learned from using Unreal Engine on set, stick around to the end and I'll show you exactly how it's done. And this video is sponsored by me and Unreal Fundamentals. This is the playbook for creating real-time visual effects and films inside of Unreal Engine 5. We'll talk about that more later. What's up? My name's Josh Tunin and for the last eight years I've worked as an artist and supervisor on Hollywood v...

**Frame:** tutorials\frames\the-future-of-filmmaking-in-unreal-5-virtual-production\frame_000.jpg


---

## Structured Notes

### Core Technique
Overview of virtual production on LED volumes using Unreal Engine 5, covering how real-time rendering on physical LED walls replaces green screen for immersive in-camera VFX, demonstrated through a horror short film production.

### Summary
Josh Toonen provides an overview of LED volume virtual production, explaining how UE5's real-time rendering drives physical LED wall stages where actors perform in front of an interactive, real-light-emitting environment. Viewers learn the fundamental concept of in-camera VFX (ICVFX), how the LED wall replaces green screen and adds practical interactive lighting on actors, and the implications for small indie filmmakers who might access VP stages. Content is conceptual and inspirational with limited technical depth.

### Key Steps
1. Understand LED volume concept: UE5 renders the environment in real time onto a curved LED wall; actors perform in front of the wall; cameras capture both actor and environment in-camera.
2. The LED wall emits real colored light onto actors — interactive lighting that matches the virtual environment without additional practical lights.
3. UE5 nDisplay plugin drives the LED wall rendering: manages frustum tracking (inner frustum = what the camera sees; outer frustum = rest of the LED wall for fill light).
4. Camera tracking data (from optical or mechanical tracking systems) feeds into UE5 nDisplay to correct the perspective of the inner frustum in real time.
5. For indie access: seek VP stage rental facilities that offer day rates, or look for VP education programs at film schools.

### UE Systems / Blueprints / Settings
- **nDisplay plugin**: Drives LED volume rendering; manages inner/outer frustum; requires camera tracking input
- **Inner frustum**: Region of LED wall rendered with correct perspective for the tracked camera
- **Outer frustum**: Surrounding LED wall area rendered for ambient fill light onto set
- **Camera tracking**: Mechanical or optical tracking system feeds position/rotation to UE5 nDisplay for perspective correction
- **Interactive lighting**: LED wall light output replaces traditional practical lights; actors receive colored interactive illumination from the virtual environment

### Difficulty
Beginner

### UE Version
UE 5.x

### Tags
cinematics, pipeline, rendering, beginner

---

## Related Entries
- [[how-this-unreal-engine-5-film-won-an-oscar]] — UE5 as a complete film production platform
- [[how-ue5-created-the-most-realistic-game-ever---unrecord-trailer-breakdown]] — real-time rendering capabilities that enable VP quality
