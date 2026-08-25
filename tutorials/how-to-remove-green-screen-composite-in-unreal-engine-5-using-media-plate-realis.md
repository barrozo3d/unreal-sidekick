---
title: How to Remove Green Screen & Composite in Unreal Engine 5 Using Media Plate (Realistic Shadows)
source: YouTube
url: https://www.youtube.com/watch?v=771myWapQ_s
author: World Of VFX
ingested: 2026-06-23
ue_version: "UE5.7"
tags: [green-screen, compositing, media-plate, chroma-key, shadows, virtual-production, materials, sequencer]
extraction_status: complete
frames_dir: tutorials/frames/how-to-remove-green-screen-composite-in-unreal-engine-5-using-media-plate-realis/
frame_count: 4
---

# How to Remove Green Screen & Composite in Unreal Engine 5 Using Media Plate (Realistic Shadows)

**Source:** [YouTube](https://www.youtube.com/watch?v=771myWapQ_s)
**Author:** World Of vfx
**Duration:** 9m3s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey what's up guys welcome back to another Unreal Engine 5 video. Today we'll talk about how you can use the green-screen footage instead of Unreal Engine with the shadow. And it will be a very easy technique. So let's get started. All right, so I have downloaded a project file from Epic Games Fab. And now we need to add a plugin that is named Media Plate. And you can find this called Media Plate Beta. Make sure you turn down and restart your Unreal Engine. After that, simply click here. You can find Media Plate. Click the Media Plate here. So this will create a media plate kind of a pain in front of you. Just scale it up. Now in it to browse your footage. So first of all, I just rotate it something like this. And let's make it to 90 degree. And after that, going down, you can find this file option. Click here, browse your green-screen footage. Once you browse it successfully, going up, just simply click this, open the current media. And now, boom, you can see your green-screen footage. Also, the light is interacting with the environment. This is the newly launched update. You can easily use it. After that, going down, you have this option called main element. Just double-click in it. So this is a main material. And now you have this called parent material as well. Click this search bar. And you have this newly launched media plate. So you have this media plate CC translucent. Just right-click and duplicate so that original will not get changed or hampered. So now let's rename it to let's say key out. Let's make it to key and press enter. And after that, simply drag and drop under this parent material. And just double-click in this parent material. And you have this lot of new materials. OK, so no need to worry about. We are going to use very simple things. So first of all, just press tab and type key. And you have this MF Chroma here. Just click it. We'll have to connect this before this media-texture. So what you're going to do, simply click this RGB, connect with this input color and click this emission color to this e-multiplier. And opacity should connect with this opacity tab. That's it. Just press apply. And now you have this semi-transparent effect. No need to worry about. Simply save it and close this. So now we have this media-texture palette. Just double-click and it will open a new browser. Just drag and drop this to outside. And you have this key color option. Just click this on. Select this color, open this drop-up, and pick your green color. And after that press OK. So if you notice, we have this spherical mode. You can change it to plain. So now you can see how exactly it will look like after the key out. Now, here you can do a lot of things. You can actually modify your mask. So if you want, you can increase it. You can also alpha change like this. But there is a most important option called spill correction. And now you have this key spill display option. Just simply turn this on. So it will automatically display your edges. Now, going down, you can do anything like color correction, brightness, contrast, and all. But before doing anything, you just need to turn on this color correction amount, change it to one. And now if you want, you can change it to brightness as well, contrast, whatever you want to do. So it will automatically impact on your main output. Now, make sure save it. And you have to close this. Close this as well. So now we have this transparent green-screen removed character. Now you need to adjust the character where you want to place it as per your scene. So let's do it. So I placed the character somewhere here. This looks pretty good. And I just used the cam 02. And let's change something on the camera so that the angle will get fixed. Now this is a long shot. So what I'm going to do, I'm change it from digital film to DSLR. So it's clicking white. Now go to universal zoom, change it to 85 millimeter. All let's say 50 millimeter is pretty enough. Good. And now you can see pretty good depth in it. So now let's place the camera as per your scene. So let's say this one is pretty good. Now make sure your focus should be always on this character. You have this called manual option, change it to tracking. And from the auto track option, type media palette or plate. Simply click this. So now always this character is in focus. Wherever you go, the character should be always in focus. If you go closer, the background will blur. If you go far, the automatically the blur will get updated. Now we don't have any shadow in it. So to get the shadows, it's a very simple technique. What I'm going to do, I'm just select this media plate and go to edit and duplicate it. So we have both the media plates exactly in the same space. Now turn off the first one because we are going to use the second one for the shadow. Now click this so that we can use this material. Now going down, you have the same material, just double click in it. So now you can't see anything because we are going to do some changes right over here. Now double click on the parent material. We have to add one single parameter. So simply click and right click, change it to parameter and let's say change it to opacity. And then multiply it to MU just like this. And after that, add a node called multiply or multiply and simply default value should connect with B. This opacity connect with A and this one will connect to our opacity over right and make sure the default value should one. Yep, that's it. And after that, simply place apply save it. Now close this. Now we have the character. Now what happened? We can see the character and the shadows exactly in the same space. Now going up, you can type Unlit and simply click this one to default lit. So now it will exactly generate the shadows. But you can't see the shadow right now. So to see the shadow, simply type shadow sorry, simply type shadow and you have this option called cast dynamic shadow. Simply turn this on. Now boom, you can see the shadow cast is generating. Also in this global scale parameter, we have already used this opacity multiplier. So now we have to turn this on and change it to 0.001. So that exactly the shadow will create. Also going down, you can find this option called opacity mask clip value. Change it to same 0.001 and simply press save. So now whatever shadow you are seeing, it's actually applying from the main character. Now you just need to close this. Now inside of the media plate, you can type cast press enter and going up, you can find this cast shadow, make sure the dynamic shadow should turn on. And in the light settings, you can change the shadow cache in validation behavior should always turn on. So automatically the shadow will get updated. So now if you play, you can exactly see the shadow is going here. And if you just turn on the media plate here, you can exactly see both the media plates are connected. Now you need to play both simultaneously. So what you can do, you can create a new level sequence and name it to, let's say green and press enter. And we have this. Now I'm just selecting the cam 0 to just drag and drop, select the camera and now use this media plate both. So first of all, select the first media plate, just drag and drop and press yes. Click the second media plate, just drag and drop and press yes. So now both the media plates are connected to each other. Now if you play, you can see the shadow right over here. Now you can actually change the lighting to see how exactly it will look like to go to the light settings, light source. And now you can exactly change the light directions and automatically the shadow will update. If you notice this area, the shadow is visible. Now one more thing, if you want to change the position of the character, make sure you need to do one more thing. Select the camera, move it wherever you want to move. For example, this is my current position. Now we need to rotate this one. So select both the media plates because both are exactly in the same space and then you can rotate. So what happened the shadow and the main media plate will get update, simultaneously, something like this. Now once you play, you can see on the background, the shadow is moving and then foreground, the character is moving. In the same way, you can do your green-screen footage composition inside of one religion. So yes, that's it for today. I hope you really understand how you can create your green-screen composition inside of one religion. This is 5.7 by the way. And if you really feel this video is helpful for you, comment down below and subscribe for more amazing content like this. See you in my next video. Till then keep watching keep rocking world of effects.

**Frame:** tutorials\frames\how-to-remove-green-screen-composite-in-unreal-engine-5-using-media-plate-realis\frame_000.jpg


---

## Structured Notes

### Core Technique
Green screen chroma key composite in UE5 using the Media Plate Beta plugin. Two Media Plate actors stacked in the same position: one for the keyed footage (MF Chroma node), one for shadow casting (opacity-controlled duplicate material). Both driven in Sequencer for synchronized playback with real-time dynamic shadows from scene lighting.

### Summary
9-minute tutorial by World Of VFX showing how to composite green-screen footage into a UE5.7 scene using the Media Plate plugin. Chroma key is achieved by adding an MF Chroma node to a duplicated Media Plate CC Translucent material. Realistic dynamic shadows require a second duplicate Media Plate actor with a custom opacity parameter, cast shadow enabled, and opacity mask clip value = 0.001. Both plates are added to a Level Sequence for synchronized playback. Camera uses tracking auto-focus locked to the media plate.

### Key Steps
1. **Enable plugin** — Plugins → search "Media Plate Beta" → enable → restart UE5
2. **Place Media Plate** — click Media Plate button in toolbar → plane appears; scale up; rotate 90° to face camera
3. **Load footage** — Media Plate Details → File → browse green-screen footage → Open Current Media → footage plays with UE lighting interaction
4. **Duplicate material for keying**:
   - Main Element → double-click material → parent material slot → search "media plate CC translucent" → right-click → Duplicate → rename (e.g., "key") → drag onto parent material slot → double-click parent material
5. **Add MF Chroma node** — press Tab → type "key" → select MF Chroma → connect: RGB → Input Color; Emission Color → e-Multiplier; Opacity → Opacity → Apply
6. **Key out green** — save and close material; double-click media-texture palette (opens browser); drag "Key Color" out → enable it → select color → pick green → OK
7. **Plane mode** — change from Spherical to Plain to see flat composite view
8. **Spill correction** — enable "Key Spill Display" toggle to visualize edges
9. **Color correction** — enable Color Correction Amount → set to 1; adjust brightness, contrast, etc.
10. **Create shadow plate (duplicate)**:
    - Select Media Plate actor → Edit → Duplicate
    - Turn off original (visibility toggle)
    - On duplicate: double-click material → double-click parent material
    - Right-click inside material → Convert To Parameter → rename "Opacity"
    - Add Multiply node: Opacity → A; default value → B; output → Opacity Override; default value = 1 → Apply → Save
11. **Enable shadow visibility**:
    - Set viewport to Default Lit (type "Unlit" in outliner → click Default Lit)
    - Re-enable first (original) Media Plate; now both plates occupy same position
    - On shadow duplicate: enable Cast Dynamic Shadow
    - Global scale parameter: enable Opacity Multiplier → set to 0.001
    - Opacity Mask Clip Value → 0.001 → Save
12. **Media Plate shadow settings** — inside shadow Media Plate: Cast Shadow → enable; Shadow Cache Invalidation Behavior → Always
13. **Level Sequence playback**:
    - New Level Sequence → drag camera → drag both Media Plates (press Yes to each) → play sequence to sync both plates
14. **Camera setup** — camera: Digital Film → DSLR; focal length 50-85mm; Focus: Manual → Tracking → type "media plate" in auto-track search → select → auto-focus locks on plate
15. **Reposition character** — select BOTH media plates simultaneously → rotate/move together to keep shadow aligned; adjust camera independently

### UE Systems / Blueprints / Settings
- **Media Plate Beta plugin** — UE5 plugin; adds Media Plate actor type; supports video playback with UE lighting interaction; enable in Plugins panel
- **Media Plate actor** — placed in scene as a plane; accepts video file via File → Browse; plays with real-time light interaction from scene directional light
- **Media Plate CC Translucent material** — built-in Media Plate material; duplicate before modifying to preserve original
- **MF Chroma node** — chroma key material function; input: color + emission color + opacity outputs from media-texture; connects before the main media-texture in material graph
- **Key Color parameter** — in Media Texture palette browser; enable → color picker → select green; drives chroma key matte
- **Plain mode** — media plate projection mode; use instead of Spherical for flat footage compositing
- **Spill Correction / Key Spill Display** — shows edge mask for spill cleanup; toggle in texture palette browser
- **Color Correction Amount** — must be enabled (set to 1) before brightness/contrast adjustments take effect
- **Shadow plate technique** — duplicate Media Plate + custom Opacity parameter (multiplied down to 0.001) creates invisible plate that casts shadows from scene lighting
- **Opacity Mask Clip Value** — set to 0.001 on shadow plate material; allows shadow geometry to exist without visible surface
- **Cast Dynamic Shadow** — enable on shadow Media Plate actor; Shadow Cache Invalidation Behavior = Always for real-time shadow updates
- **Level Sequence** — add both media plates + camera; play syncs footage playback with Sequencer timeline
- **Camera tracking auto-focus** — camera focus mode: Tracking → Auto Track field → search "media plate" → selects Media Plate as focus target; DoF follows character movement
- **UE version** — UE5.7 (specified in tutorial)

### Difficulty
Intermediate. Shadow setup requires custom material parameter and specific opacity clip values. Two-plate workflow is the non-obvious part that enables dynamic shadows.

### UE Version
UE5.7

### Tags
green-screen, compositing, media-plate, chroma-key, shadows, virtual-production, materials, sequencer

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:54] tutorials/frames/how-to-remove-green-screen-composite-in-unreal-engine-5-using-media-plate-realis/frame_000.jpg
- [2:43] tutorials/frames/how-to-remove-green-screen-composite-in-unreal-engine-5-using-media-plate-realis/frame_001.jpg
- [4:59] tutorials/frames/how-to-remove-green-screen-composite-in-unreal-engine-5-using-media-plate-realis/frame_002.jpg
- [7:14] tutorials/frames/how-to-remove-green-screen-composite-in-unreal-engine-5-using-media-plate-realis/frame_003.jpg

## Related Entries
- `how-to-make-blade-runner-in-unreal-5-step-by-step.md` — introduces camera, sequencer, and material basics for context
- `how-to-make-unreal-look-more-cinematic.md` — focal length, DoF, and cinematic camera settings applicable to composited shots
- `the-future-of-filmmaking-in-unreal-5-virtual-production.md` — virtual-production context for live compositing workflows
