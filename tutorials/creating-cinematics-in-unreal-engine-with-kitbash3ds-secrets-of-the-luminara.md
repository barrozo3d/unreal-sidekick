---
title: Creating Cinematics in Unreal Engine with KitBash3D's Secrets of the Luminara
source: YouTube
url: https://www.youtube.com/watch?v=f2YLWIvs6F8
author: The Gnomon Workshop
ingested: 2026-06-17
ue_version: "5.4"
tags: [cinematics, kitbash3d, sequencer, volumetric-lighting, god-rays, character-animation, asset-migration, blueprints, cargo-plugin, electric-dreams, environment, ue5, gnomon-workshop]
extraction_status: complete
frames_dir: tutorials/frames/creating-cinematics-in-unreal-engine-with-kitbash3ds-secrets-of-the-luminara/
frame_count: 8
---

# Creating Cinematics in Unreal Engine with KitBash3D's Secrets of the Luminara

**Source:** [YouTube](https://www.youtube.com/watch?v=f2YLWIvs6F8)
**Author:** The Gnomon Workshop
**Duration:** 42m32s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hello everyone, my name is Koskyo Saki, I am an Unreal Engine journalist in the CZNVFX industry  and I have a course called Creating Cinematics in Unreal Engine 5 at the No-1 Workshop.  Today, with this free mini-course, I am guiding you how to make a cinematic shot very quickly with the collaboration of KitBush3D and Unreal Engine.  We'll start from the basics, including how to bring KitBush3D assets into your project using cargo.  We will craft natural environments, set up cinematic lighting, and add a character to your scene,  and finally we'll render your masterpiece using Unreal Engine sequencer.  By the end, you will have the tools to unlock the secrets of the Lumina and share your story with the world.  Ready to dive in? Let's get started!

**Frame:** tutorials\frames\creating-cinematics-in-unreal-engine-with-kitbash3ds-secrets-of-the-luminara\frame_000.jpg

### Kickstarting Unreal [1:07]
**Transcript:** So let's start creating Unreal Project and disclaimer. By the time you're watching this tutorial,  the workflow might be a little bit different. From mid-October 24, Epic Games is intending to migrate the content into this platform called Fab.  You're going to download Unreal Engine, Mega Scan, all the assets through Fab, not from Epic Games Launcher.  But I don't know how it's going to look like right now, but the workflow must be similar.  So for now, let me just go with the Epic Games Launcher.  Navigate yourself to Unreal Engine tab, go to library, and you can click this plus icon bottom to download new Unreal Engine instance.  Select the latest version, I already have it. As of right now, 5.4.4, and install. Once it's installed, let's launch Unreal Engine.  Let's navigate to games, hit blank, and turn on ray tracing for this project, and let's do the project location.  For now, I'm going to select desktop, but make sure you have plenty of disk space.  Select folder, and I have to create the project name. So I'm going to call this, get my secret of luminon, and hit create.  When first I'm launching, it has to compile shaders. It might take a little bit of time, but let's wait f...

**Frame:** tutorials\frames\creating-cinematics-in-unreal-engine-with-kitbash3ds-secrets-of-the-luminara\frame_001.jpg

### Importing Kitbash3D [6:57]
**Transcript:** Okay, now let's start adding those Kipash 3D Premium asset for this project to get going.  In order to utilize Kipash 3D assets, you need cargo. So now we get to the Kipash 3D website, and you have to download cargo.  Download the cargo software for your computer. Once it's downloaded and loans your cargo, it asks you to sign in, sign up if you haven't, and use a potential to sign in.  Once you sign in, what I would do is go to Account tab. By the way, you need to have Unreal install on your computer beforehand.  Please make sure to add Unreal Engine to your computer first, and choose the software settings to be Unreal Engine 5.4.  If you haven't seen it, hit Add New Software, select Unreal, version 5.4, and make sure to close your Unreal if it's still open, and hit Install.  Activate your plugin, hit Next. So it automatically adds the cargo plugin to your Unreal Engine.  It's nicely automated, and so let's close this tab.  Reload Unreal Engine by just going to Library, and you should be able to see your project somewhere in my project section, or you can launch Unreal Engine 5.4.4.  And instead of creating new project, you can select from here, or browse, in my case Desktop, click...

**Frame:** tutorials\frames\creating-cinematics-in-unreal-engine-with-kitbash3ds-secrets-of-the-luminara\frame_002.jpg

### Creating Natural Environment [16:06]
**Transcript:** Okay, now let's start adding terrain to the scene.  I would love to save some time by utilizing the free sample kit from Epic Games.  So let's navigate to Launcher.  Let's go samples.  And here we have Electric Dreams Environment.  Download this environment and let's create a project.  And make sure your local drive has enough storage because this project is pre-vik at least 60 YG.  Once you created a project, launch the project.  And we're going to try this thing called Migration.  You can migrate entire project or target specific assets.  For this specific project, navigate yourself to assembly, turn on filter,  blue print class, control A to select everything, right click, asset action, migrate.  So it's going to grab all the necessary files, texture, materials, and meshes and everything.  Associate it with these blue print class.  So hit OK.  And we have to navigate ourself to the project folder that we want to migrate to.  Under project, just select content and select folder.  So it's going to duplicate all these necessary files and paste onto our secrets of the Ruminera Unreal project.  It might take some time, so make some coffee and relax and come back.  So it took me like ...

**Frame:** tutorials\frames\creating-cinematics-in-unreal-engine-with-kitbash3ds-secrets-of-the-luminara\frame_003.jpg

### KitBashing Assets [23:12]
**Transcript:** So from here let's start adjusting the kit bash model and go into more details.  The kit bash asset is provided as blueprint actor.  Blueprint is the most versatile format that you can have in Unreal Engine.  You can contain anything inside.  In fact, if you expand this section, you see bunch of stuff inside.  Select Blueprint, hit Ctrl B to show in the content browser and double click to go inside, hit Viewport.  And in fact, as you can see, these are consisted of bunch of different static meshes.  So this asset is treated as kind of like a group.  And if you want to modify this asset, there are many ways to modify it.  Let's say if I wanted to move this stage right here, I will try to aim it here in a double click and then you can move it around.  Also you can go back to Blueprint Editor and you can move things around and hit Compile and it will update the original Blueprint itself.  But this double click and moving method will not override the original Blueprint.  So I think this is more versatile.  And let's say if you wanted to delete one particular static mesh, you can just simply hit Delete button.  Instead, what you can do is go into the Detail panel in static mesh and you ...

**Frame:** tutorials\frames\creating-cinematics-in-unreal-engine-with-kitbash3ds-secrets-of-the-luminara\frame_004.jpg

### Cinematic Lighting [33:06]
**Transcript:** To make the scene look more like a cinematic, it's cheesy but got right always works.  I moved all my lighting related stuff into this lighting sublabel.  You want to make this one work, I have to enable exponential height fog down there.  There is a tick box says volumetric fog, so I'm going to tick it.  Let's add light, red light in the scene.  Just like camera, you can control light by its point of view.  So right click, pilot, red light, so you can control the light for its perspective.  So I'm going to like place it outside of the cave here like M2 inside, go back to perspective,  and then search volumetric and add volumetric scattering intensity like crazy, 100,000.  And then make things like bigger, 100 by 100, attenuation radius to be a lot bigger.  Change the barn to angle, smaller lengths to be a lot longer.  Okay, a lot more longer.  So make sure this light is covering the scene.  Lastly, tick, cast volumetric shadow.  So you will start to see the crazy got rays happening, I'll reduce the intensity quite a bit.  In a content browser search euro, and there are a lot of trees named the European tree,  and just get one of them.  I'm going to use this as a fake light blocker...

**Frame:** tutorials\frames\creating-cinematics-in-unreal-engine-with-kitbash3ds-secrets-of-the-luminara\frame_005.jpg

### Character Animation & Render [35:50]
**Transcript:** So the last missing piece is to add a character to make it more alive.  For this example, we're going to use Epic Games, one of the samples.  Go to Launcher, Samples, and there is Slay Animation Sample.  You know the drill, download is, create a project, and then we're going to migrate this one.  Okay, once you open a project, we go Slay and Assets, Character, Echo.  That's the character we're going to use, the right click, Migrate, and Hit OK.  Like always, select Content and select Fulder.  Okay, and also we need that character to be moving.  So we need to migrate things called Animation Sequence.  So again, in Content, Slay, Sequences, and Under Sequences, put the Filter, Animation Sequence,  it's going to only show Animation files only, and we're going to filter through by typing Echo,  that's the name of the character, right click, Migrate.  It's going to grab the Assets already exported as well, but don't worry, just say, okay, select the destination.  So he asks you, hey, this Assets already exists on the destination, what do you want to do?  We'll say no to that one, it already exists.  So he only going to export the Animation Sequence.  Cool, let's go back to the main proj...

**Frame:** tutorials\frames\creating-cinematics-in-unreal-engine-with-kitbash3ds-secrets-of-the-luminara\frame_006.jpg

### Outro [41:36]
**Transcript:** Thank you so much for staying until very end.  Feel like to dive deeper into Unreal Engine Cinematics journey.  I would like to recommend to take a look at my course,  creating Cinematics in Unreal Engine.  At the normal workshop.  From common practice to our theory to all the components of Cinematics creation in Unreal Engine.  I specifically designed the course so that everybody would be ready to work in production environment.  I would like to see all your work.  Until next time, stay Unreal.  Thanks for watching.

**Frame:** tutorials\frames\creating-cinematics-in-unreal-engine-with-kitbash3ds-secrets-of-the-luminara\frame_007.jpg


---

## Structured Notes

### Core Technique
End-to-end cinematic shot workflow in UE5.4 using KitBash3D assets: project setup → Cargo plugin import → environment assembly via asset migration → volumetric god-ray lighting → character animation → Sequencer render.

### Summary
Mini-course by Koskyo Saki (Gnomon Workshop) walking through a full cinematic pipeline using KitBash3D's "Secrets of the Luminara" kit. Covers UE5.4 project creation with ray tracing, installing the KitBash3D Cargo plugin, migrating terrain from Epic's Electric Dreams sample, editing KitBash Blueprint Actors per-instance, building volumetric god-ray lighting with Rect Lights and Exponential Height Fog, migrating the Echo character + animations from the Slay sample, and compositing the final shot in Sequencer.

### Key Steps
1. Create blank UE5.4 project with **Ray Tracing enabled**
2. Download KitBash3D **Cargo** app → Settings → Add Unreal 5.4 → Install plugin (auto-injects into UE)
3. Import KitBash3D assets via Cargo into the project
4. Migrate terrain from **Electric Dreams Environment** sample (Content Browser → Blueprint Class filter → Select All → Right-click → Asset Actions → Migrate → target project's /Content folder)
5. Place KitBash Blueprint Actors; double-click individual static meshes inside the BP for non-destructive per-instance edits (doesn't overwrite source Blueprint)
6. **Volumetric god rays**: Add Exponential Height Fog → tick Volumetric Fog → Add Rect Light → Pilot from its POV → set Volumetric Scattering Intensity (100,000), large Attenuation Radius, narrow Barn Door angle, long Source Length → tick **Cast Volumetric Shadow** → reduce Intensity to taste → place European tree mesh as fake light blocker
7. Migrate **Echo character** from Slay Animation Sample (Content/Slay/Character/Echo → Migrate)
8. Migrate **Echo Animation Sequences** (Content/Slay/Sequences → filter Animation Sequence → filter "Echo" → Migrate; skip existing assets)
9. Add character to scene with animation in Sequencer → render with Movie Render Queue

### UE Systems / Blueprints / Settings
- **Sequencer** — cinematic assembly and render
- **Blueprint Actor** — KitBash3D assets arrive as BPs; per-instance mesh editing via viewport double-click
- **Exponential Height Fog** — Volumetric Fog checkbox required for god rays
- **Rect Light** — Pilot mode (right-click → Pilot) for light-POV placement; Cast Volumetric Shadow
- **Content Migration** — cross-project asset transfer; handles dependency gathering automatically
- **KitBash3D Cargo Plugin** — auto-installs into UE; requires UE closed during plugin install
- **Fab / Epic Games Launcher** — asset acquisition (note: Epic migrating to Fab from mid-Oct 2024)
- **Ray Tracing** — enabled at project creation

### Difficulty
Beginner–Intermediate

### UE Version
5.4.4 (UE5)

### Tags
cinematics, kitbash3d, sequencer, volumetric-lighting, god-rays, character-animation, asset-migration, blueprints, cargo-plugin, electric-dreams, environment, ue5, gnomon-workshop

---

## Related Entries
- Sequencer / cinematics tutorials (Black Eye Cameras v2, Dean Yurke series)
- Volumetric lighting / Lumen entries in Rendering docs
