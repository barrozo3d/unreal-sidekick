---
title: Motion Capture Sword Fighting Cinematic in Unreal Engine 5 - Move.AI and Metahumans
source: YouTube
url: https://www.youtube.com/watch?v=ukk4vw-bIpA
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.x"
tags: [mocap, metahuman, move-ai, sword-fighting, two-actor-capture, animation-pack, fight-choreography, control-rig, ue5]
extraction_status: complete
frames_dir: tutorials/frames/motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma/
frame_count: 5
---

# Motion Capture Sword Fighting Cinematic in Unreal Engine 5 - Move.AI and Metahumans

**Source:** [YouTube](https://www.youtube.com/watch?v=ukk4vw-bIpA)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 8m1s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In this video, I'll show you how I made this choreographed sword fighting scene in Unreal Engine 5.

**Frame:** tutorials\frames\motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma\frame_000.jpg

### SHORT FILM [0:06]
**Transcript:** So this was one of the funnest videos I've done in a long time.

**Frame:** tutorials\frames\motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma\frame_001.jpg

### Choreography with Professional Stuntmen [0:51]
**Transcript:** And that's because I was finally able to do something that I wanted to do since I got my hands on this motion capture technology in the first place.  I was finally able to get two actors at the same time into the motion capture volume to do some fight choreography.  I made a fight scene video recently that was a Kung Fu fight.  And the whole inspiration for that film was that I'd found a way around needing to do choreography.  That's because there was this animation pack from real illusion of hand-to-hand combat.  And it had paired animations that were 5, 10 seconds long.  And it showed the two characters interacting and fighting.  And the choreography was so good. The animations were awesome.  And it was so easy to just take two of these animations and put them into a scene and then start setting up the cameras.  And I wanted to do the same thing with a sword fight.  But the problem is there's not a lot of great paired animations out there.  There are paired animations where you might have one or two moves or something.  But everything that's out there would be so tedious to stitch together into an actual fight scene.  It's almost not really worth it.  And as far as I've gotten ma...

**Frame:** tutorials\frames\motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma\frame_002.jpg

### Assembling the Scene in Unreal Engine [3:50]
**Transcript:** I just found a scene that I had had in my library for a while.  This is really awesome, sort of broken down cathedral.  And it had just amazing lighting already.  I did very little to change the lighting here.  And then I just dropped in two metahumans.  And I used the Medieval Armor pack from Polyphoria for the clothing.  And then got the animations that I wanted to use, chopped up and into the sequencer and applied to each metahuman.  Once that was in place, I baked the animations to the control rig.  And that allowed me to go in and actually fine-tune the animations.  Honestly, there was not a lot of cleanup done to these animations.  You know, I did go in and just remove the hand tracking because one hand is literally just holding a sword.  So no need for hand animation.  And then the main thing that I was doing was going through and making sure the swords were actually connecting.  Because the swords are just attached to the hand bone.  And so, you know, you can see when I just put the animations in, the swords aren't really lining up because like the actual angle of the wrist isn't being tracked accurately.  So that was the one thing I had to go in and manually adjust.  And I...

**Frame:** tutorials\frames\motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma\frame_003.jpg

### Ideas for more Battle Scene Mocap [6:33]
**Transcript:** And then you can, you know, you can set it in any setting you want, use any camera angles, you know, make it any style.  And the idea is that I'm building enough Lego pieces and I'm building blocks to eventually make a whole battle scene, you know, of any kind of scale.  So in this case, it's just a generic short sword because that was the easiest to do.  And also because I think it has a lot of uses.  But, you know, we want to do, you know, other types of swords, maybe katanas or samurai sword style stuff.  You know, broad sword, pikes spears.  Also all the sorts of things you might see in a medieval battle scene.  So let me know in the comments, you know, what other kinds of choreography you'd like to see.  You know, what could you imagine using this to create yourself?  Alright, that's enough for this video.  If you found it interesting or valuable in any way, please consider leaving a like and subscribing.  Come by the discord, show off what you're making, you know, and we love to just talk all things unrelentient filmmaking.  It's a great, really helpful supportive community and it's awesome.  I think it's turning into one of the best, you know, online resources for this kind ...

**Frame:** tutorials\frames\motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma\frame_004.jpg


---

## Structured Notes

### Core Technique
Two professional stunt performers captured simultaneously in Move.AI Pro multi-cam volume for choreographed sword fighting, with the main cleanup challenge being sword alignment to hand bones via Control Rig additive layer and wrist rotation correction — building reusable "Lego piece" sword-fight animation assets for future battle scenes.

### Summary
Charlie Driscoll captures two actors doing choreographed sword fighting using Move.AI Pro (multi-camera system). The key challenge motivating this video is the lack of quality paired sword-fight animations on the market — most available paired animations are limited (1-2 moves) and too tedious to stitch together. Using Move.AI Pro he captures continuous choreographed sequences with professional stunt performers, then assembles them in UE5 Sequencer over a ready-made cathedral environment with Polyphoria Medieval Armor clothing. The main cleanup work involves the hand tracking being inaccurate for wrist angles when holding swords — fixed by removing hand tracking entirely and manually correcting sword-to-wrist rotation in the Control Rig. The resulting animations are designed as a reusable animation pack/library for future medieval battle scenes.

### Key Steps
1. Hire professional stunt performers; capture extended choreographed sword fighting sequences with Move.AI Pro multi-cam setup.
2. Import FBX animations; retarget to MetaHuman skeletons; apply Polyphoria Medieval Armor clothing.
3. Place MetaHumans in cathedral environment (Fab) in Sequencer; apply animations; attach sword static meshes to hand bones.
4. Bake animations to MetaHuman Control Rig.
5. Remove hand tracking data entirely (one hand holds sword, no hand animation needed); correct wrist/arm rotation so swords align properly during contact moments.
6. Add additive animation layer; use Control Rig to manually correct sword alignment frame by frame at contact moments.
7. Fly camera around live scene to find interesting shot angles; set up cameras in Sequencer.

### UE Systems / Blueprints / Settings
- Move.AI Pro multi-cam (two-actor simultaneous sword-fight capture)
- MetaHuman Animator (face capture, referenced as part of full pipeline)
- Level Sequencer (animation layering, camera cuts, sword attachment to hand bones)
- MetaHuman Control Rig (bake + additive layer for sword alignment corrections)
- Polyphoria Medieval Armor Pack (MetaHuman clothing)
- Cathedral environment (Fab asset)
- Static mesh swords (attached to hand bones in Sequencer)

### Difficulty
Intermediate

### UE Version
5.x

### Tags
mocap, metahuman, move-ai, sword-fighting, two-actor-capture, animation-pack, fight-choreography, control-rig, ue5

---

## Related Entries
- `how-to-create-a-fight-scene-cinematic-in-unreal-engine-55.md` — similar fight scene using Reallusion animation pack instead of custom mocap
- `how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng.md` — two-actor simultaneous capture pipeline overview
- `how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal.md` — gladiator film that uses these sword-fight animation assets in background OverCrowd crowd
