---
title: Unreal Engine Black Eye Cameras: Look Around Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=oZ_0JPrN-hE
author: Black Eye Technologies
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-look-around-tutorial/
frame_count: 8
---

# Unreal Engine Black Eye Cameras: Look Around Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=oZ_0JPrN-hE)
**Author:** Black Eye Technologies
**Duration:** 2m52s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey this is Adam, is your character how the user controlled head motion?  Let's set up a cool little black eye rig called the look around.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-look-around-tutorial\frame_000.jpg

### Character Binding [0:07]
**Transcript:** Okay, drop a black eye camera in the scene, rename it because you're not a monster.  We're gonna click follow, click the character and we're gonna follow the root bone.  Then we're gonna click look at, click the character and we're gonna look at the head bone.  If your character is already in the scene, just look at it.  But if you're spawning it in, set auto assigned to the player ID, and then turn on look at and follow.  Set this up to a character that's in the scene and then you can hide it.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-look-around-tutorial\frame_001.jpg

### Save in Play! [0:34]
**Transcript:** Supergirl features, this one, save and play.  Save all your changes, game changer.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-look-around-tutorial\frame_002.jpg

### Look Distance [0:39]
**Transcript:** Alright, here's the juice right here. Select the look at, see the offset, it's in local space.  Set that to a number down why, that's the orientation of the head bone.  Now you're looking at a spot that's 80 units down from the head bone.  This nice weight, this damping, you can follow very loosely, you can recompose where you're following.  See this, we're gonna like move the composition of where we would like to follow, subject to be a little higher, lower in the frame.  You still get that nice weight to it.  Okay, let's move that back down a little bit, get it more centered.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-look-around-tutorial\frame_003.jpg

### Damping [1:17]
**Transcript:** And let's play with the damping. So you've got per act of stamping.  So here we're gonna go zero, you can see very brittle, just hard pinned.  But you can also decouple the vertical from the horizontal, the pitch and the yacht.  So we're gonna go with more horizontally and less vertically and look at this.  The camera's gonna more lazily follow left to right because of the screen ratio.  Of course, and then it's gonna be more aggressively following up and down.  Pretty cool.  That nice weight we spent so long getting that mouth right.  The camera will follow with weight and damping in a sense of mass.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-look-around-tutorial\frame_004.jpg

### Dead Zones [2:05]
**Transcript:** Dead zones.  So you can create a dead zone and all the motion inside it will be disregarded.  This is too big, just make an example.  And as soon as the target goes outside the dead zone, then the damping kicks in.  Let's make this little smaller so it's a bit more appropriate.  Dead zones are adjustable for their horizontal vertical size.  And those handful of controls you can get so much behavior.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-look-around-tutorial\frame_005.jpg

### Wrap Up [2:35]
**Transcript:** Thank you for watching.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-look-around-tutorial\frame_006.jpg

### Sneak Peek [2:40]
**Transcript:** So, little sneak peek.  We've got a pretty cool free look orbit, their person camera system coming.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-look-around-tutorial\frame_007.jpg


---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### UE Systems / Blueprints / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### UE Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Entries
[PENDING EXTRACTION]
