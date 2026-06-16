---
title: Unreal Engine Black Eye Cameras: Follow Component: Dwell Radius
source: YouTube
url: https://www.youtube.com/watch?v=oYYxZc2jO2c
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, gameplay, cinematics, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-follow-component-dwell-radius/
frame_count: 4
---

# Unreal Engine Black Eye Cameras: Follow Component: Dwell Radius

**Source:** [YouTube](https://www.youtube.com/watch?v=oYYxZc2jO2c)
**Author:** Black Eye Technologies
**Duration:** 1m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey, this is Adam. Let's talk about follow cameras. It's a big topic. What better movie than 1917? I think they used every camera, transport, mechanism, rig, dolly, humans holding things, handing it to arms on cars. One continuous shot. So when we built the follow control in black eye, we want to give you controls which can emulate all these kinds of behaviors. So we've got our injured zombie walking, the camera's following. That red sphere that you see, that's called the follow dole radius. And basically it's going to disregard motion from the subject that you're following inside that sphere. So look at this. When it's big, if the camera's inside that, the camera's not going to move. It's going to ignore the zombie motion. Here's when it's small. And then that little line that comes off it, that's how much damping you have to give you this heavy, soft weight. You can adjust that. And with these two controls, you can create a lot of different follow behaviors.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-follow-component-dwell-radius\frame_000.jpg


---

## Structured Notes

### Core Technique
Black Eye Follow Dwell Radius: a sphere around the subject within which camera follow motion is ignored; combine with positional damping to emulate human camera operator behaviors like the 1917 continuous-shot follow rig.

### Summary
1-minute tutorial on the Follow Dwell Radius feature. Inspired by 1917's complex follow-camera choreography (dollies, arms on cars, human operators passing the camera). The dwell radius (red sphere around subject) creates a "dead zone" for positional follow — camera ignores all subject motion inside the sphere. Outside the sphere, positional damping adds heavy organic weight. Adjusting dwell radius + damping creates a wide range of follow personalities from rigid to floaty.

### Key Steps
1. **Set Follow on character** — standard Follow setup.
2. **Enable Dwell Radius** — sets a red sphere around the follow subject. Visible in viewport.
3. **Adjust dwell radius size** — large sphere: camera stays still until subject travels far outside the center; small sphere: camera follows very tightly.
4. **Add positional damping** — the "line" off the sphere visualizes damping; controls how slowly the camera "catches up" after the subject exits the dwell radius. Heavy values = soft, organic, weighted feel.
5. **Combine for personality** — large radius + high damping = very loose, human-operator feel; small radius + low damping = tight follow.

### UE Systems / Blueprints / Settings
- **Follow Dwell Radius** — sphere around follow subject; camera ignores motion within the sphere
- **Red sphere debug visualizer** — visible in viewport; size matches dwell radius
- **Positional damping** — how quickly camera catches up after subject exits dwell radius; "line" off sphere indicates amount
- **Combination** — dwell radius + damping = complete follow personality control

### Difficulty
Beginner

### UE Version
UE 5.x (Black Eye v1)

### Tags
`#blackeye-v1` `#camera` `#gameplay` `#cinematics` `#beginner`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-v2-start-here-tutorial]] — Dwell Radius section in v2 START HERE (same concept, more detail)
- [[unreal-engine-black-eye-cameras-overview-tutorial]] — Follow damping system context
