---
title: MetaHumans for Mocap | Unreal Engine Animation Hub
source: YouTube
url: https://www.youtube.com/watch?v=myxrzJiLc6I
author: Unreal Engine
ingested: 2026-06-23
ue_version: "UE5"
tags: [metahuman, mocap, motion-capture, live-link, capture-character, virtual-production, facial-animation, blueprint, construction-script, leader-pose]
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
**Transcript:** Welcome to Animation Hub. Today we're going to be looking at how to set up a meta-human for MoCAP manager. So we can't just use them straight out the box. We do need to make a new version of them basically. It needs to be inheriting from their Capture Character class. So I've got my meta-human here and let's just open that up. As you can see we've got the various components and so we're going to create a new blueprint. We're going to make it of Capture Character. There we go. You can call this what you want but I quite like Capture Character MH character. So I want just copying the original name. So I'm going to open these both up. We're going to transfer some assets between them. So let's go full screen. First things first, if we get hold of the body and we copy paste or you can shift the right mouse button. Let's go and paste that onto the Skeletal Mesh asset top slot there. So we've got our arms and legs in. Next let's go and get the rest of the Skeletal Mesh and the groom. So let's select these controls C and then let's paste these over. And so there we go. So we've basically copied that blueprint but it's of a different inherited class. It's parent class is different I should say. So let's close these both down and then in MoCat Manager let's create a new character. Let's call it for now. Capture because that's going to be the data that we the underlying Skeletal data that we're going to use and then MH01. That's going to be the name. The source is going to be our Catery Skeletal and we've already got this set up. And I'm going to in the character class, I'm going to choose the one the class that we just created. And then character mesh you're going to want to add the body for that character. So character 01 body mesh and then create the character asset and then we can spawn it. So as you can see we've already got some anime already had some animation coming in and that's mapped but you will notice I'm sure that the short city shirt isn't lining up. It isn't is an anime. Now we can fix this temporarily by going to the character section on the asset and just toggling this but that's pretty annoying to do every time. And this is something we can fix on the construction. So if I just edit this class, go to the construction script and off of construction, let's just set the leader pose component. And we're going to use, it's only the body and the shorts that's the issue. The face doesn't need this because it gets its animation from a different source which we're going to look into in a sec. So there we go. If you had a meta human with more components than this then you would just build one of these for each mesh. And what we're going to want to do is set it basically say is this mesh, this shorts and t-shirt has a new leader which is the body and we're going to want to tick these two. And what this is doing is basically saying all of your animation is inherited from this component. Hit compile and save. And then just to prove that this is going to work every time we spawn this character, let's just delete these and spawn it again. So it was that one and hit spawn. That's what you can see that's worked great. So, but what about face? Let's sort face out. So we can use webcam for this. So if I go over to the live link tab and add source, go to meta human video. This is available in the meta human live link again. And it can detect our webcam and I quite like the default settings so I'm just going to hit connect. First thing you're going to want to do is go in and disable head orientation, translation and stabilization. The reason being is that we're already getting the head orientation, translation and stabilization off of the capture data. If we had these on, we would get double transforms on the neck which are pretty wacky, pretty fun, but not really what we need. So in order to apply this to the meta human, we do need to combine these sources which is what we're going to use the virtual live link subject for. So we're just going to go to add source again, add a virtual subject. I'm going to call this body and face. Add and then I'm just going to go and add those two subjects. Then back in MoCat Manager, I'm just going to apply, instead of the body data that's coming in on unknown, let's apply the new virtual live link subject where they're combined. And you should now see that she's animating to my facial pose. So if we just want to isolate that to take a closer look, let's just give the source as the webcam. And now you can see it's matching my lips and my eye blinks and my facial expressions. So if we now switch that back to the virtual live link subject, we've combined a two. And that's it and that's how we set up meta humans for MoCat Manager.

**Frame:** tutorials\frames\metahumans-for-mocap-unreal-engine-animation-hub\frame_000.jpg


---

## Structured Notes

### Core Technique
MetaHumans cannot be used directly with MoCap Manager — they must be wrapped in a new Blueprint that inherits from the **Capture Character** class. Skeletal mesh components and grooms are copied from the original MH Blueprint. Clothing meshes require a **Set Leader Pose Component** in the Construction Script to follow body animation. Face capture is handled separately via Live Link MetaHuman Video source; head orientation/translation must be disabled to avoid double transforms; a **Virtual Live Link Subject** combines body + face into a single stream.

### Summary
6-minute Epic Animation Hub tutorial showing how to integrate a MetaHuman into MoCap Manager for full-body + face performance capture (Captury body + webcam face). Covers: creating a Capture Character Blueprint wrapper by copying MH components; setting up the character in MoCap Manager (source + class + mesh); fixing clothing follower meshes via Set Leader Pose Component in the Construction Script; adding MetaHuman Video Live Link source for face; disabling head orientation/translation (prevents double neck transforms when body capture already drives head); creating a Virtual Live Link Subject that combines body + face; switching MoCap Manager to use the combined virtual subject.

### Key Steps
1. **Create Capture Character Blueprint**:
   - Content Browser → New Blueprint → Parent Class: **Capture Character**
   - Name it (e.g., `CaptureCharacter_MH_CharacterName`)
   - Open both the new BP and the original MH Blueprint side by side
   - From original MH BP → copy Body Skeletal Mesh → paste into new BP's top Skeletal Mesh slot (arms/legs)
   - Select remaining Skeletal Meshes + Grooms from original MH BP → Ctrl+C → paste into new BP

2. **Set up character in MoCap Manager**:
   - MoCap Manager → Create New Character
   - Name: give it a capture name (e.g., `Capture_MH01`)
   - Source: set to Captury Skeletal (pre-configured source)
   - **Character Class**: select the new Capture Character BP created in step 1
   - **Character Mesh**: select the character's body mesh
   - Create Character Asset → Spawn

3. **Fix clothing follower (Construction Script)**:
   - Problem: clothing meshes (shorts, t-shirt) don't follow body animation automatically
   - Open the Capture Character BP → Construction Script
   - From Construction node: add **Set Leader Pose Component**
   - Target: shorts mesh; Leader: body mesh; check both tick boxes
   - Add a second Set Leader Pose Component node for each additional clothing mesh
   - Compile + Save → delete and re-spawn character to verify fix

4. **Add face capture via webcam**:
   - Window → Live Link → Add Source → **MetaHuman Video** (requires MetaHuman Live Link plugin)
   - Select webcam → Connect
   - **CRITICAL**: Disable **Head Orientation**, **Translation**, and **Stabilization** from the face Live Link source — body capture already drives head/neck; leaving these on causes double transforms

5. **Combine body + face via Virtual Subject**:
   - Live Link → Add Source → **Virtual Subject** → name it (e.g., `body and face`)
   - Add both subjects: body capture subject + webcam face subject → combine

6. **Apply to MoCap Manager**:
   - In MoCap Manager, switch character's source from plain body capture → select the **Virtual Live Link Subject**
   - Character now drives body from Captury + facial expressions from webcam simultaneously

### UE Systems / Blueprints / Settings
- **MoCap Manager** — Epic plugin for real-time performance capture management; requires Captury or similar body system as source; spawns Capture Character Blueprints in level
- **Capture Character class** — parent class required for MoCap Manager characters; MetaHuman must be wrapped in a BP inheriting this class (not the default MH parent)
- **Set Leader Pose Component** — Blueprint node (Construction Script); sets a clothing/secondary mesh to follow another mesh's animation; prevents de-sync between body and clothing; both boxes must be checked; add one node per secondary mesh
- **Live Link → MetaHuman Video** — Live Link source type for webcam face capture; requires MetaHuman Live Link plugin; outputs head orientation + translation + facial expression data
- **Head Orientation / Translation / Stabilization** — disable all three on the face Live Link source when body capture system already drives neck/head bones; otherwise neck gets double transforms
- **Virtual Live Link Subject** — combines multiple Live Link sources (body + face) into a single subject; enables MoCap Manager to receive combined stream; equivalent to virtual subject in Live Link Hub
- **Captury Skeletal** — body mocap source type in MoCap Manager; full-body skeleton streaming from Captury system

### Difficulty
Intermediate. Requires MoCap Manager + Captury hardware setup. Blueprint skills needed for Construction Script fix. Core workflow is procedural once hardware is configured.

### UE Version
UE5 (MoCap Manager + MetaHuman + Live Link Hub ecosystem — UE5 era)

### Tags
metahuman, mocap, motion-capture, live-link, capture-character, virtual-production, facial-animation, blueprint, construction-script, leader-pose

---

## Related Entries
- `live-link-hub-tips-unreal-engine-animation-hub.md` — Live Link Hub for multi-source mocap routing; Virtual Subject setup; recording
- `metahuman-realtime-animator-best-practices-unreal-engine-animation-hub.md` — webcam face capture best practices; camera FPS/exposure settings; two-machine offload
- `metahumans-in-unreal-engine.md` — complete MetaHuman Blueprint structure, LODs, animation pipeline, Control Rig
