---
title: How to Make Blade Runner in Unreal 5 (Step-by-step)
source: YouTube
url: https://www.youtube.com/watch?v=ncjHJQPyzto
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [cinematics, sequencer, lighting, post-process, animation, mrq, beginner]
extraction_status: complete
frames_dir: tutorials/frames/how-to-make-blade-runner-in-unreal-5-step-by-step/
frame_count: 14
---

# How to Make Blade Runner in Unreal 5 (Step-by-step)

**Source:** [YouTube](https://www.youtube.com/watch?v=ncjHJQPyzto)
**Author:** Josh Toonen
**Duration:** 24m45s | 14 section(s)

---

## Raw Data (for Claude Code extraction)


### How to make Blade Runner 2049 in Unreal Engine 5 [0:00]
**Transcript:** This isn't Blade Runner, it's Unreal Engine 5.  You don't need 8 hours of tutorials to get started.  Most people overcomplicate Unreal Engine, so today we're going to keep it really simple  and together we'll recreate this shot from Blade Runner 2049 as fast as possible.  What's up, my name's Josh Tuner and I've spent the last 9 years working as a visual effects  artist and supervisor on movies like Dungeons & Dragons and A Process Spider-Verse.  And now I make my own animated films.  So today I'm going to give you the roadmap to render your very first shot in Unreal Engine 5.  Now your first film isn't going to be perfect, so don't worry.  Just follow the steps once and you'll know the exact process to make your very own films

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_000.jpg

### Building your Blade Runner scene step by step [0:39]
**Transcript:** forever.  So let's start building our scene step by step.  I downloaded some stills from the original movie so I could constantly go back and forth  and compare my 3D scene to the original reference.  To get started, if you don't have Unreal Engine downloaded already, just download the  Epic Games Launcher and download the latest version.  What we're starting with here is the third person example project.  So when you go to make a brand new project, just click on Games and then select the third  person example project and we'll use this template to kick off our project.  Just press Create.  Now the thing about Unreal is the longest wait times are when you're creating your project  at the very start.  But after all that waiting, we get to render in real time and have an interactive viewport  where we can add our lights, camera and action right here in front of us.  For example, if we go up and press the Play button at the very top, we'll start playing  our game and now we can move around in the 3D world using the WAST controls and the  space bar.  But how do you go from this example project to the world of Blade Runner?  Well the first thing you'll do every time to start off a proje...

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_001.jpg

### Download free 3D models to jumpstart your project [2:24]
**Transcript:** So for this example I found some really inexpensive models of K from Blade Runner 2049 and his  spinner, both from CGTrader.com.  If you want to follow along exactly I'll just leave a link for both of these below.  But just know you can use any character you want and you can even use the characters  included with our sample project.  Because the third person template will come preloaded with 4 different characters that  you can simply drag right into your scene.  By the way if you want to learn how to make your own films in Unreal 5 then you should  join my Unreal 5 filmmaking bootcamp, Unreal Fundamentals.  This is my entire filmmaking tool kit.  You'll get my render presets, templates and everything I've learned so any one of you  can go from a complete beginner to mastering Unreal 5 for filmmaking.  It's on sale right now so check it out down below or go to unrealforvfx.com slash fundamentals.  Let's get back to the video.

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_002.jpg

### Import any vehicle into Unreal Engine 5 [3:09]
**Transcript:** So let's start out by adding in our vehicle, the spinner.  We can create a brand new folder in our content browser.  Let's create a new folder and let's call it spinner.  Then we can press enter to open it up and then importing your objects is really simple.  You just need a .fbx or .obj file and then you can click and drag that directly into our  content browser.  Now any 3D objects can be saved in Blender and imported into Unreal.  Just select all the objects you want to export and then go to file and export this as a .fbx  file.  Then we'll limit this to the selected objects and press export.  Then just drag and drop this fbx file right into your content browser.  And now we have our import options.  Now Unreal has two different names for 3D objects inside of Unreal.  The first is a static mesh, just like a statue that stands still.  And the second is a skeletal mesh that has a rig and skeleton with bones that you can  puppeteer.  Now if your object has a rig, Unreal is smart enough to detect it and import it with all  the settings you need.  All we need to do is press import on the bottom.  And so now we have our 3D object imported.  Now the way that this was imported is that w...

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_003.jpg

### Add realistic materials and textures to your objects [5:16]
**Transcript:** And whenever you import an object into Unreal, odds are you're going to have to recreate  the materials completely from scratch.  So in our case, I'm going to grab all the textures that were included with our object  and just drag them into Unreal.  And now we should have five imported textures.  So from here, we need to take our textures and turn them into a material that we can  assign to our 3D object.  So to do that, let's right click on our content browser and make a new material.  And we'll call this M-M underscore spinner and press Enter.  So I have our material on top and our textures underneath.  So let's just drag in each one of these and then we can assign them to the right material  slot.  In this case, if I read here, I can see that this is the base color texture.  So when I drag this in, I'll just plug this directly into our base color.  And then we'll do the same for our metallic, our roughness and our normal map.  Then just make sure to press Save.  And then all we need to do to apply it to our objects is to click our objects in the  outliner, scroll down until you see the material slot, and then we can just click and drag  our spinner material into the empty materi...

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_004.jpg

### Rig any character for free with the Mixamo + the One Click Control Rig [7:02]
**Transcript:** Squid.  You know, no problem at all because you can rig and animate your characters completely  for free using one of our free plugins, the one click control rig.  With the one click rig, you can take any 3D character and quickly add animations directly  inside of Unreal 5.  Just go to Unreal for VFX.com slash rig to download this yourself.  Now the way this works is we're going to take our 3D model and we're going to use the  auto rigging tools on Miximo.com.  Just go to Miximo.com and make a free account, and then you can upload your 3D characters.  In our case, I'm going to drag our 3D model and then I'll get the auto rigging tools.  You just need to assign the chin, wrists, elbows, knees, and growing.  And then press next.  And Miximo will go through and auto generate a rig for your character.  Then we can preview it to make sure everything's working at first glance.  And from here, we have a huge library of animation clips that we can directly apply to our  character.  So we can find some fun combat animations, but in our case, in the movie, he's mostly  brooding and walking slowly through the desert.  So we can just type in walk and find some nice simple walking animations th...

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_005.jpg

### Import your rigged character into Unreal Engine [8:22]
**Transcript:** So we'll go to our content folder and we can make a new folder called K. And we can take  our new downloaded file and just import it right into our content browser.  Then we can pick our asset name and I'm going to call this SKMK.  And SKM just stands for skeletal mesh and press import.  And then in our content browser, we have everything we need to get started.  We have our skeletal mesh.  We have our first animation file and we have our other skeleton asset.  Now the first thing I always do is assign the materials onto our character and the best  place to do this is inside of the skeletal mesh editor.  So just double click on that pink skeletal mesh and if you reassign the materials that  you see right here, this will always be the default material when you drag this into  any scene.  So let's create a new material and we can do this by clicking on this drop down here  and at the very top, let's create a brand new material.  We can go to our K folder and call this M-M-K.  Let's open this up and we'll do the same thing we did before.  We need to import our textures and assign those in the material.  In our case, we just have one image texture that will drag that into our content b...

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_006.jpg

### Create massive landscapes like AAA games [10:27]
**Transcript:** Looking back at our reference, let's create this rocky ground and build up all this fog  and atmosphere in our scene.  So for now, let's delete every object that's not K or the spinner.  One thing that's really important is if you just hide these objects in your outliner,  as soon as you go to play your game or render out your 3D movie, all of that geometry  will reappear.  So it's not good enough just to hide your objects in the outliner, we need to delete them  from the 3D world.  So next to create that sandy rocky landscape, we can use the landscape tool in Unreal Engine.  At the very top of your screen, we can jump out of selection mode and jump into landscape  mode.  And this will allow us to create a vast landscape just like in a game like Far Cry or  Red Dead Redemption.  But we don't need all that flexibility or complexity, we're going to create a really  simple one for our film.  So let's just go to the Managed tab and then we can create a new landscape.  And if you look in your 3D scene, you can see exactly how big our previewed landscape  will be.  Now, there's two different ways you can create a landscape.  I could just select all the default options here and press Crea...

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_007.jpg

### Add photorealistic sand textures from Quixel Megascans [12:55]
**Transcript:** To do this, you can click on the fab icon and from here we can download some free sand  textures from Quixel Megascans, which is a great free and high quality resource that's  created by the team behind Unreal Engine.  Just type in Quixel and find any asset that's been created by the Quixel team and then  you can click on their creator icon to jump to all the assets created by Quixel.  Now just make sure to include all 3D compatible formats here and this will show you all of  the Quixel Megascans library.  So let's type in sand and we can search for only assets that are created from Quixel  and then you can also filter by price.  So this way you can only find the free assets if that's what you want to do.  So I'm going to grab this free rippled sand material and we'll use this and scatter  it across our entire landscape.  Let's make sure this is set to high quality and then we can add this into our project  and it will automatically download and import into Unreal.  Now in your content folder you'll see a new folder called fab and inside we'll have  a new Megascans folder.  We can go to our surfaces and click on rippled sand.  Now here our textures are automatically imported and a ...

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_008.jpg

### Create cinematic fog and volumetric lighting effects [15:28]
**Transcript:** Now all we need to do if we want to adjust our fog or our atmosphere is let's just  type that in the outliner.  And search for something called exponential height fog.  If I adjust the details here we have full control over the density of our fog and we can  even add in some cool rendering features like volumetrics.  To start out let's increase this fog density to something really dense and thick like a  value of 1.  Just to get things started.  Now this is probably too extreme but it's alright for now.  We also have some controls for start distance so you can also make sure that the fog doesn't  start until a certain point which you might want so that doesn't start until right behind  your characters.  Now let's keep scrolling down until you find volumetric fog and let's set this to true.  This will totally change the behavior of our fog because now our sunlight also known  as our directional light inside of Unreal will directly impact our volumetric fog.  You'll really start to notice this if I search for my directional light.  Let's just move the sun closer to our characters.  You'll see now depending on where our sun is in our scene it has a really dramatic effect  on our lands...

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_009.jpg

### Color grade your shots directly in Unreal Engine 5 [17:00]
**Transcript:** post process volume.  Now this might sound stranger intimidating but don't worry.  Post processing is just all of the work you do after you render out your image.  So if you do any work in Photoshop or After Effects or Nuke all of that would be considered  post processing but we can just do it directly inside of Unreal Engine.  So in your outliner just type in post process volume and this is all of the different render  settings in our scene.  We have control for things like chromatic aberration, exposure, lens flares, depth of  field but what we want to adjust is the global color grading.  If we go down to this global tab and we go to the gain settings we'll have this little  color wheel and from here we can just click the center and drag this until we're getting  the yellow orange colors that you're seeing in Blade Runner 2049.  This is a cool start but we always need to go back to our reference and one thing that's  kind of cool that they did in the original movie was adding some reds into the shadows.  Which just makes it feel a little bit more otherworldly or like it's on this alien planet.  So to do that just scroll up to find the gamma controls right above the gain controls ...

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_010.jpg

### Set up cameras and create your first animated sequence [18:35]
**Transcript:** By the way because we're using the real time rendering side of Unreal Engine we'll get  some splotchy shadows from certain angles but you can also switch over to path tracing  mode at any point and you'll get a fully realistic and path traced version of your  scene.  For now let's jump back to lit mode.  But right now we just have our 3D viewport.  Let's create a camera so we can actually film our first scene.  So to create any animations or to create our first timeline just go up to this clapperboard  image at the top and let's add in a new level sequence.  We can go to our content folder and type in ls underscore 01 for our very first shot.  This will create a brand new level sequence which is our animation timeline where we can  add in keyframes and animate any single property that you see in the details panel.  First things first I always set this to 24 frames per second and I'll enable snapping.  Then if we want to add our characters into sequencer we can just drag them from the outliner  and literally just drop them right into our sequencer timeline.  From here we can add in our animation tracks.  And if you expand this it'll just keep looping the same animation.  Now we can ...

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_011.jpg

### Render your film and drag + drop into any editing software [21:45]
**Transcript:** Keep going.  Now that we have our entire environment and film set created you can spend time working  on set acting like a director and designing your own shots and sequences by plotting out  your cameras just like this.  And now if you want to render out your shot and throw it directly into an editing timeline  just go to edit plugins and then we'll enable one plugin apple pro res media then just make  sure to enable this and you'll need to restart Unreal engine but before you do that just  go back to save all in your content browser and save everything in your scene so you don't  lose your progress.  Then let's restart Unreal and we'll finish up by rendering this out.  So now with Unreal Engine reloaded just open up that level sequence one more time and then  we can look through our camera cut track by pressing this little camera cut icon right  here and this will allow us to look through our camera.  At any point you can also press shift C and hop out of your camera cut view and you can  see exactly how your camera is moving through 3D space.  And this is a good way to test out your camera and see if it's looking too artificial or  too perfect versus what would actually happen i...

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_012.jpg

### Master Unreal Engine 5 filmmaking with my complete course [24:03]
**Transcript:** Now if you want to speed run all of Unreal Engine and learn all my advanced workflows  and techniques as well as get my exact templates and render presets I have an all in one  filmmaking bootcamp called Unreal Fundamentals.  We're all taking you from a complete beginner to making your own blockbuster films in Unreal  Engine 5.  Together we'll build four environments step by step and learn exactly what it takes to make  your own films look like your favorite Hollywood movies.  It's on sale right now so click the link below or go to unrealforvfx.com slash fundamentals.  And if you want to upgrade and improve your 3D renders then watch part two of this tutorial  right here where we'll add map paintings and lens flares using all the same techniques  I use every day on Hollywood films.  Otherwise subscribe down below and I'll see you in the next video.  Peace.

**Frame:** tutorials\frames\how-to-make-blade-runner-in-unreal-5-step-by-step\frame_013.jpg


---

## Structured Notes

### Core Technique
Complete beginner-to-finished-cinematic walkthrough using UE5: Third Person template → FBX import → Mixamo auto-rig → landscape creation → Megascans textures → Exponential Height Fog → Post Process color grade → Sequencer → Movie Render Queue ProRes output.

### Summary
Josh Toonen provides an end-to-end beginner tutorial recreating the Blade Runner neon-noir aesthetic in UE5 using entirely free assets. Viewers follow every step from opening a Third Person template and importing a Mixamo character through building a desert landscape with Quixel sand textures, adding volumetric fog and dramatic color grading, animating the scene in Sequencer, and rendering a final cinematic in Apple ProRes. By the end, beginners have a complete understanding of the core UE5 filmmaking pipeline.

### Key Steps
1. Start a Third Person template project; open the Content Browser (Ctrl+Space) for asset navigation.
2. Import character FBX: Content Browser → Import → select FBX → FBX Import Options: Skeletal Mesh = true, Skeleton = none (create new skeleton).
3. Upload character to Mixamo.com for auto-rigging: on Mixamo, place markers on chin, left/right wrists, left/right elbows, left/right knees, and groin; download the rigged character as FBX.
4. Create landscape: Modes → Landscape → Managed tab → Create New Landscape; set desired size and resolution.
5. Import Quixel Megascans sand textures from Fab/Bridge and paint them onto the landscape using the Landscape Paint tool.
6. Add Exponential Height Fog (Quick Add → Visual Effects): Volumetric Fog = true, Fog Density = 1.0, Start Distance = set to push fog away from camera.
7. Add Post Process Volume (Infinite Extent); in Color Grading: boost Gain for orange/yellow highlights; push Gamma for red shadow tones.
8. Create a Level Sequence at 24fps; add Camera Cut track with Cine Camera actor; add character animation tracks.
9. Open Movie Render Queue; enable Apple ProRes Media plugin (Edit → Plugins → Pro Res); set output format to Apple ProRes.

### UE Systems / Blueprints / Settings
- **FBX Import**: Import Options: Skeletal Mesh = true; Skeleton = new; Import Mesh = true; no morph targets needed
- **Mixamo markers**: Chin, left/right wrists, left/right elbows, left/right knees, groin (7 points)
- **Landscape Mode**: Modes → Landscape → Managed tab; Scale and resolution set at creation; painted with Quixel sand materials
- **Exponential Height Fog**: Volumetric Fog = true; Fog Density = 1.0; Start Distance = push from camera; Fog Height Falloff controls layer thickness
- **Post Process Volume**: Infinite Extent (Unbound) = true; Color Grading → Gain (orange/yellow highlights); Gamma (shadow red push)
- **Sequencer**: 24fps; Camera Cut track; Animation track per character
- **Movie Render Queue + Apple ProRes**: Edit → Plugins → "Apple ProRes Media" → enable; MRQ output format = Apple ProRes 4444

### Difficulty
Beginner

### UE Version
UE 5.x

### Tags
cinematics, sequencer, lighting, post-process, animation, mrq, beginner

---

## Related Entries
- [[how-i-remade-the-backrooms-using-vfx.md]] — same beginner pipeline (Third Person template, fog, post-process)
- [[this-free-plugin-changes-filmmaking-forever-unreal-5]] — OneClick Control Rig for the Mixamo rig step
- [[unreal-engine-masterclass-animate-environments-the-easy-way]] — next-level environment animation building on this foundation
