---
title: Unreal Engine Black Eye Cameras: Look Around Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=oZ_0JPrN-hE
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, gameplay, beginner]
extraction_status: complete
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
Black Eye "Look Around" camera rig: camera follows character's root bone and looks at head bone with per-axis damping and dead zone, emulating a human head-tracking camera operator.

### Summary
3-minute tutorial for the Look Around rig — a camera that follows the character's root bone (translation) while dynamically composing on the head bone (rotation), with adjustable pitch/yaw damping and a dead zone. Ideal for over-shoulder or face-tracking gameplay cameras. Teases an upcoming free-look orbit third-person system at the end.

### Key Steps
1. **Drop Black Eye camera + rename** — add actor to scene, rename it (good naming habit).
2. **Follow on root bone** — click Follow → pick character → set follow bone to root bone (most stable for translation).
3. **LookAt on head bone** — click Look At → pick character → type head bone name → disable "use actor bounds" (targets bone, not bounding box).
4. **Spawned characters** — if character isn't in scene yet, enable Auto-Assign to player ID + enable Look At and Follow; configure on a scene-placed reference then hide it.
5. **Save-in-Play** — enable save-and-play to iterate camera feel while game runs.
6. **LookAt offset in local space** — select Look At → set local offset (e.g., Y = -80 to aim 80 units in front of head bone). Adjust offset to re-compose subject position in frame.
7. **Damping** — set per-axis damping: `pitch damping` (vertical response) and `yaw damping` (horizontal response). Adjust independently to get natural weight — e.g., more horizontal lag for cinematic feel on wide aspect ratios.
8. **Dead Zone** — create a dead zone region; motion inside the zone is ignored. Camera only reacts when the target exits the zone. Adjust horizontal and vertical dead zone size independently.

### UE Systems / Blueprints / Settings
- **Follow (root bone)** — translational follow target set to root bone for stability
- **LookAt (head bone)** — rotational tracking; bone name typed manually; disable actor bounds
- **Auto-Assign** — player ID; enables automatic binding on spawn
- **LookAt local offset** — spatial offset from bone in local space; controls subject placement in frame
- **Pitch / Yaw damping** — per-axis; adjust vertical vs horizontal response independently
- **Dead Zone** — screen-space ignore region; independent horizontal and vertical size controls
- **Save-in-Play** — iterate camera feel while game is running

### Difficulty
Beginner

### UE Version
UE 5.x (Black Eye v1)

### Tags
`#blackeye-v1` `#camera` `#gameplay` `#beginner`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-start-here-tutorial]] — full v1 system; Follow + LookAt covered in detail
- [[unreal-engine-black-eye-cameras-v2-start-here-tutorial]] — Dead Zones section in v2 START HERE covers the same concept in depth
