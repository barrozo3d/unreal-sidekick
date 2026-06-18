---
title: Pose Library ADDITIVE MODE: Layer Animation Poses in Unreal Engine
source: YouTube
url: https://www.youtube.com/watch?v=YSrYqx19_Y0
author: Unreal Engine
ingested: 2026-06-18
ue_version: "UE5"
tags: ["animation", "control-rig", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/pose-library-additive-mode-layer-animation-poses-in-unreal-engine/
frame_count: 4
---

# Pose Library ADDITIVE MODE: Layer Animation Poses in Unreal Engine

**Source:** [YouTube](https://www.youtube.com/watch?v=YSrYqx19_Y0)
**Author:** Unreal Engine
**Duration:** 8m43s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** In this video, I'm going to show you how to use the Pose Library tool to not only apply poses or blend between them, but also use the new additive mode, and I'll also show you how to use it as more or less a selection set button. Another great set of tools you have access to is the Pose Library. So when you're in animation mode, if you go up to poses and hit this button, it will pull up a little window for controlling poses. Now you can go ahead and dock this somewhere if you'd like, and what it will allow you to do is save and refer back to different preset poses for your selected rig. So what I can do is I can grab, for example, all of the right hand bone controls. So if I come over here to my anim outliner, I can grab all of these, like, right meta, pinky, all the different hand controls. So I'll just shift click, all of those different hand controls, they're all selected. And I can save this particular pose as a fist. So with all that selected, I'll go up here to my pose. I'll say create pose, and I'll call this fist underscore R. Great asset. I can redo the thumbnail if I don't like the frame that has got here. I can just say capture thumbnail, and that'll give me a new pictur...

**Frame:** tutorials\frames\pose-library-additive-mode-layer-animation-poses-in-unreal-engine\frame_000.jpg


---

## Structured Notes

### Core Technique
Pose Library in Animation Mode — saving, recalling, and blending between rig poses; using Additive Mode to layer corrective poses on top of existing animation.

### Summary
Official UE guide to the Pose Library tool available in Animation Mode. Covers creating pose assets from selected controls (e.g. fist shape for right hand), using the blend slider to apply poses partially, the Additive Mode which adds a pose delta on top of existing keyframe data, and using saved poses as one-click selection sets for complex rig controls.

### Key Steps
1. In Animation Mode, go to **Poses** panel (`Window → Poses` or the toolbar Poses button)
2. Select the rig controls you want to save (e.g. all right hand controls via Anim Outliner shift-click)
3. Click **Create Pose** → name it (e.g. `fist_R`) → asset saved to Content Browser
4. To apply: select destination controls → click pose thumbnail in the Poses panel
5. Use the **Blend** slider (0–1) to partially apply the pose
6. Enable **Additive Mode** toggle → pose is now applied as a delta on top of the current animation curve data
7. Use Additive Mode to layer corrective shapes (subtle fist tightening, shoulder adjustment) without destroying base animation
8. **Selection Set trick:** save a pose with multiple controls selected → clicking it re-selects those controls (acts as a selection set button)

### UE Systems / Blueprints / Settings
`Poses Panel` (Animation Mode → Window → Poses) → UI for creating/applying/managing poses
`Create Pose` → saves current selected control transforms as a reusable asset
`Blend Slider` (0–1) → partial pose application
`Additive Mode` → pose applied as delta on top of existing keyframe data (non-destructive overlay)
`Capture Thumbnail` → update pose preview icon to current frame

### Difficulty
Intermediate

### UE Version
UE5

### Tags
animation, control-rig, intermediate

---

## Related Entries
- `references/control-rig-animation.md` — Control Rig animation tools
- `tutorials/non-destructive-animation-in-ue5-layered-control-rigs-explained.md` — layered control rigs