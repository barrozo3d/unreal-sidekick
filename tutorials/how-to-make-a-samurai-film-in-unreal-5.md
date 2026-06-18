---
title: How to Make a Samurai Film in Unreal 5
source: YouTube
url: https://www.youtube.com/watch?v=ixnoglWzwBw
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [cinematics, mocap, animation, sequencer, pipeline, control-rig, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-to-make-a-samurai-film-in-unreal-5/
frame_count: 9
---

# How to Make a Samurai Film in Unreal 5

**Source:** [YouTube](https://www.youtube.com/watch?v=ixnoglWzwBw)
**Author:** Josh Toonen
**Duration:** 12m39s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### <Untitled Chapter 1> [0:00]
**Transcript:** If you're like me, you've always wanted to create massive sci-fi movies without a giant budget.  Not just watching films anymore, but creating a story of your own.  Building your own world and your own characters and putting yourself in the middle of the action  to start recording and creating movies that you want to watch.  Using Unreal Engine 5, you can start crafting your film,  placing the characters, environments, and pointing the camera yourself to start creating your vision.  Seen by scene, shot by shot.  Not with million dollar budgets, but using free software in the computer you have at home.  Look, two years ago, this wouldn't be possible,  but today anyone can create visual effects in films using Unreal Engine 5.  And to prove it, I want to pull back the curtain and show you exactly how we created War of Being.  And the samurai sword fight behind Tesseract's latest music video.  What's up, my name's Josh Tunin, and for the last eight years I've worked as an artist and supervisor on Hollywood films.  On movies like Star Wars, Dungeons and Dragons, and across the Spider-Verse.  I first started learning visual effects because I wanted to make my films look like my favorite ...

**Frame:** tutorials\frames\how-to-make-a-samurai-film-in-unreal-5\frame_000.jpg

### MOTION CAPTURE CLEANUP [3:10]
**Transcript:** There's no skipping over this last step.  When you see a movie like an avatar way of the water, every single shot in that three hour movie was hand touched and reanimated by a senior level artist,  some of the best in the world.  And you should fully expect that you'll have to do lots of cleanup on this data after the fact.  Rocco lets you do a lot of this in their own software where you can get a first pass that we could immediately start importing into Unreal Engine and start framing up our shots.  So we took that motion capture data and created some test shots inside of Unreal.  So we could start blocking out our environment and a crucial step design our characters starting out.  It was all about the characters, the camera, and the environment.  What are the compositions we're going to make between the poses of our characters and their place inside of the environment?  The first step was creating the edit.  So I would lay out the performance, get our two samarises in the scene.  We would retarget the animations from the Rocco rig onto our samurai rig.  And then I would take six or seven different camera angles and render out the entire frame range.  I would export playblasts of ...

**Frame:** tutorials\frames\how-to-make-a-samurai-film-in-unreal-5\frame_001.jpg

### ENVIRONMENTS [4:34]
**Transcript:** Well the first CG artist to jump on board was Flora Ville-Bare.  Not only can he build environments in Unreal, he's a concept artist first.  So we got to be really creative and try out lots of ideas and design this world for the first time.  And early on it's all about iterating fast, not trying to get something completely perfect.  At first we tried different floating mountains, submerging the entire landscape in the clouds, trying out different graphic compositions.  That's why I love using Unreal is you can discover and try out these ideas without committing to them or spending too long on any one idea.  So after a few weeks of going back and forth and trying to capture the concepts that the band sent over, we landed on this foggy landscape in this old world filled with decaying buildings and robots spread across the vistas.  And we used lots of fog and clouds to create depth through our mountainscapes.  We created three different environments.  The first was our cliff scape, which we did two different lighting scenarios as the sun dips below our two planets.  And then our samurais fall down into the graveyard filled with the bodies of their past duels.  So we tried to tell the ...

**Frame:** tutorials\frames\how-to-make-a-samurai-film-in-unreal-5\frame_002.jpg

### MARKERLESS [6:39]
**Transcript:** They can approximate the movement of the character in 3D.  But this usually falls apart when you need two hands connected together to hold a sword.  We knew this was a limitation going in and that's why it was so instrumental to have a great robust rig inside of Unreal so that we take our two separated hands and attach them to a sword and have them all moving around together.  And this is why we needed our animation team to go in and re-animate nearly every single shot.  Matt Ringo came in to create the control rigs for these characters.

**Frame:** tutorials\frames\how-to-make-a-samurai-film-in-unreal-5\frame_003.jpg

### CONTROL RIGS [7:15]
**Transcript:** Yeah, you have no idea how satisfying that is.  To save the day to get our control rigs prepped perfectly for animation.  That way we could do all the motion capture cleanup entirely in Engine.  Andrea Lim, Tyler Lindsay, and Yorzloff of Bone Studios came together to re-animate some of the pivotal moments in the fight scene.  Some of the sandoffs or any moments where you see the swords collide.  We had to go back in and re-animate those moments to make sure they had the impact and the weight that we felt when we recorded it on set.  We collaborated on this project by using a GitHub repository.  And our entire team connected into one project.  We all worked in separate levels and pushed our updates at the end of each day.  And that way we could all be working out of the same project file on our local machines,  but contributing to a shared project file together.  Now a pro tip, and this is something pretty cool if you parent your characters and your cameras to the same parent actor that we're just using as our reference point for our stage.

**Frame:** tutorials\frames\how-to-make-a-samurai-film-in-unreal-5\frame_004.jpg

### STAGE ACTOR [8:05]
**Transcript:** We can move or rotate our stage anywhere around the world, but the compositions will look exactly the same.  And this can really help when blocking out your shots.  And once we had our characters polished, and our environments finished, we could put them in the scene and start making our final compositions.  And then to finish off the entire project, I stepped in to do the final lighting, compositing, and effects.  By the end we had over 120 final shots.  A lot of this film actually ended up on the cutting room.  Floor for various reasons.  It's just part of the process.  Most everything is rendered directly out of Unreal and given a really simple lens effect treatment to get realistic glows and diffusion that will happen coming through a camera lens.  But all of the lighting, elements, and effects were created inside of Unreal using Unreal Engine's tools.  Not add it in after the fact.  Achieving any level of mastery in visual effects or filmmaking takes one thing.  And that's practice.  You have to practice over and over again.  And that's why in Unreal, you can drag around lights, reframe the shot, rotate the background, or just change the camera animation entirely.  It allows f...

**Frame:** tutorials\frames\how-to-make-a-samurai-film-in-unreal-5\frame_005.jpg

### MY 3 BIGGEST MISTAKES [9:45]
**Transcript:** And I'd love to pass forward for anyone else making films for the first time.  First off, characters are the biggest bottleneck.

**Frame:** tutorials\frames\how-to-make-a-samurai-film-in-unreal-5\frame_006.jpg

### CHARACTERS ARE THE BOTTLENECK [9:51]
**Transcript:** Make sure that you have your character and your rig completely finished before you go into your motion capture.  We still made it work in the end.  But this caused a lot of scheduling and pipeline issues because we didn't have our finished characters  when we really needed to start animating to finish the entire film.  And one of the biggest struggles on this was the hardware limitations.  The graphics card we used to render this entire short was an RTX 3080.  We had a hard limitation of only 8 gigs of VRAM that we could put inside of a single scene.  If you're taking this seriously, you definitely want at least a 3090 GPU.  Instead of 8 gigs, you have 24 to work with.  And that gives you three times the resources of what you can add into your scene.  And lastly, the obstacle is the path.

**Frame:** tutorials\frames\how-to-make-a-samurai-film-in-unreal-5\frame_007.jpg

### THE OBSTACLE IS THE PATH [10:33]
**Transcript:** There's lots of errors that you're going to run into along the way.  It's part of the process.  But if you learn how to do it once, you never have to learn how to do it again.  So you can replace your render times with learning and teaching yourself for the first time.  And that allows you to make the entire film in real time.  Now, if you want to make your own films and you've struggled learning on real in the past,  then you'll want to know about Unreal Fundamentals.  This is the playbook for creating real-time visual effects in films inside of Unreal 5.  Together, we'll create four different environments step by step to go from a complete,  unreal beginner to someone who can create visual effects in films in real time.  In a matter of days, not months or years.  This was compressing all the lessons I've learned from the last two years of using Unreal Engine  on set, creating animated films on my own to create a single, simplified learning path.  So anyone can go from a complete beginner to mastering Unreal's workflows and tools,  focusing on what matters most for visual effects and filmmaking.  This is the exact training I wish I had when I was first starting out,  and I've incl...

**Frame:** tutorials\frames\how-to-make-a-samurai-film-in-unreal-5\frame_008.jpg


---

## Structured Notes

### Core Technique
Production breakdown of the War of Being samurai film: Rococo mocap cleanup, retargeting to samurai character rig, Control Rig final pass, stage actor pattern for consistent shot compositions, and GitHub-based team collaboration via separate sub-levels.

### Summary
Josh Toonen breaks down the production workflow for his War of Being samurai film, focusing on the practical pipeline for getting clean mocap data onto a samurai character and collaborating with a team. Viewers learn the Rococo mocap cleanup process, how to retarget the Rococo skeleton to a custom samurai rig, use Control Rig for final animation polish, apply the stage actor pattern to manage consistent character and camera relationships across shots, and use GitHub with separate sub-levels to enable multiple team members to work in parallel without conflicts.

### Key Steps
1. Capture mocap data with Rococo suits; clean up artifacts in Rococo Studio before exporting FBX.
2. Import Rococo FBX animation into UE5; create an IK Rig for the Rococo source skeleton and a separate IK Rig for the samurai target skeleton in the IK Retargeting editor.
3. Map bone chains between the two IK Rigs; run the retarget to produce a new animation asset on the samurai skeleton.
4. Apply Control Rig to the samurai skeleton (bake retargeted animation to Control Rig); use Control Rig editor for per-bone performance cleanup and hero pose adjustments.
5. Apply the stage actor pattern: create an empty actor, parent the samurai character and all cameras for that shot to it; reposition the root actor to change composition without breaking relative relationships.
6. Set up GitHub collaboration: each team member works in a separate sub-level (see [[how-to-create-cinematic-environments-in-unreal-engine-5]]); push updates at end of each day; pull main level to see combined result.

### UE Systems / Blueprints / Settings
- **Rococo FBX export**: Standard skeleton FBX; exported after cleanup in Rococo Studio
- **IK Retargeter**: IK Rig for Rococo source skeleton + IK Rig for samurai target; bone chain mapping; retarget produces new animation asset
- **Control Rig bake**: Right-click animation in Sequencer → Bake to Control Rig; per-bone curve editing
- **Stage actor pattern**: Empty Actor root; characters + cameras parented as children; Movable; reposition root to change entire shot layout
- **GitHub + sub-levels**: Each team member assigned a sub-level (effects/geometry/lighting); committed independently; pulled into master level for review

### Difficulty
Intermediate

### UE Version
UE 5.x

### Tags
cinematics, mocap, animation, sequencer, pipeline, control-rig, intermediate

---

## Related Entries
- [[motion-capture-isnt-just-for-hollywood-any-more]] — detailed Rococo mocap pipeline used in this production
- [[how-to-create-cinematic-environments-in-unreal-engine-5]] — sub-level organization and cloth simulation for the War of Being environment
- [[unreal-5-hotkeys-every-filmmaker-must-use]] — stage actor pattern and Sequencer workflow
