---
title: How to Create Cinematic Environments in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=Cp7sWfiHcJg
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [cinematics, sequencer, geometry, animation, materials, lighting, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-to-create-cinematic-environments-in-unreal-engine-5/
frame_count: 10
---

# How to Create Cinematic Environments in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=Cp7sWfiHcJg)
**Author:** Josh Toonen
**Duration:** 15m9s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** If you're creating environments in Unreal, a lot of beginners fall for this simple mistake.  They don't add animation into their environments.  So I want to take you behind the scenes of the samurai sword fight we made for War of Being.  I made it entirely inside Unreal Engine 5.  Building the characters, animations, and environments from scratch,  and I want to share all the lessons we learned along the way.  So if you want to prove your environments today,  I'm going to share nine of my favorite techniques that you can apply to your scenes right away.  To create depth, animation, and movement,  and stick around to the end because I'm going to show you two methods to create cloth simulations,  to add flowing wind, to flags, banners, and costumes.  What's up, my name's Josh Tune, and I've spent the last eight years working on Hollywood  Visual Effects as an artist and supervisor on movies like Star Wars, Deadpool, and across the Spider-Rex.  And I've started using Unreal Engine Onset to create animated films in my own.  So let's hop into Unreal and pull back the curtain on War of Being.  Whenever I'm starting an environment build, I always go through these three stages.

**Frame:** tutorials\frames\how-to-create-cinematic-environments-in-unreal-engine-5\frame_000.jpg

### How I Start Every Environment [0:56]
**Transcript:** The block out, the camera, and then the build.  Step one is the block out, so in this case, we were under some pretty tight deadlines,  so I started with an asset pack first, so I could start using high-quality models to start our  first assembly of this environment. But usually, I'll block out a scene using primitive shapes,  like cubes, spheres, and cylinders, just to get a simple layout of the scene.  I'll also include a human scale reference and import motion capture data as early as possible,  to see how the characters look inside of the environment.  Step two is creating cameras. Now, these don't have to be final shots, but you should try to mimic  the overall look and vibe of your scene and make sure that your environment works shot through  the camera lens. If your compositions don't work at this block out stage, no amount of high-res,  geometry, or particle effects is going to save your scene. You want to view your environment through  as many camera angles as possible at this stage, so once the camera is set up, I'll use that to tweak  our block out and make sure that the layout of the overall environment makes sense for the scene  we're trying to shoot. And then the thir...

**Frame:** tutorials\frames\how-to-create-cinematic-environments-in-unreal-engine-5\frame_001.jpg

### Finish the Build [2:08]
**Transcript:** add decals, up-res any assets that aren't working close to camera, and then add in any lighting  and movement through particle effects and find ways to add life and animation into the environment  itself. And you don't have to over-complicate this. If I look at our floating rocks here,  you can see that they're constantly spinning, and if I look from a top-down view,  you can see that the volumetrics and shadows are moving along with our floating rocks here.  And if I go into sequencer to see how this is set up, all I'm doing is I'm taking these two  arch-quixel assets, and then parenting them to a basic actor. This is just an empty actor that we can  animate. But when we apply animation to the parent, then we can start adding in decals and have them  parented and move correctly with our arches. So we can save some time on texturing these arches,  since we never really see them up close. We can easily move these around, and then they'll stay  in the same place as they animate throughout our sequence. But I'm just using two rotation keyframes  here, and in the curve editor, I've selected them and changed their pre-infinity and post-infinity  settings to linear. So they continue on b...

**Frame:** tutorials\frames\how-to-create-cinematic-environments-in-unreal-engine-5\frame_002.jpg

### Lighting Blockout [3:47]
**Transcript:** block out lighting as early as possible is that it's our way to show off our work and show off  our environment. So if I just disable all the lights in the scene here, you'll see how big of a  difference this makes. And one of our environment is black. We don't actually read any of the geometry  or detail in our environment. So typically, if I was just going to start this from scratch, I like to  start off by backlighting environments, especially hallways like this. So I would just start off by  making a spotlight, increasing the intonuation radius, and then pushing it back in our scene so that  we can backlight our environment. And because our surfaces are reflective, the position of the light  has a big effect on how it reflects across our surfaces. And then to add some fill light, I would just  add some additional spot lights. In this way, we can be really selective about what parts of our  environment we choose to reveal. And this is why I like to block out the camera moves early on,  because from here, we can tell right away if something's working or not, and we can easily change  the position of our light in context, previewing one of our final shots. We can do the same thing...

**Frame:** tutorials\frames\how-to-create-cinematic-environments-in-unreal-engine-5\frame_003.jpg

### Cloud Cards [5:19]
**Transcript:** techniques to build this environment that you can start applying right away. Now one of the key  things that we added in early on were cloud cards. These are just simple planes that we would hide  in the background to add depth and atmosphere to our shot. Now one of the first movies I ever  worked on was Alien Covenant. And one of the locations they shot at in real life is Milford Sound  in New Zealand. Now if you look up images of this place, it looks larger than life and has real life  clouds intersecting with mountains. Now it's really important when you're trying to add in  stylized clouds to ground your work in reality and use real life reference like you could find at  Milford Sound and let real life influence the design and placement of your cloud cards. So if I just  select these, you can see that they're just really big cards that are one sided that we can start  to move around and place shot by shot. You can even add in simple animation to move them left and  right to give us some drifting movement. And the material is super easy to make if I select this  fake fog material. All that we're doing is we're changing the blend mode over to translucent  and then we're taking th...

**Frame:** tutorials\frames\how-to-create-cinematic-environments-in-unreal-engine-5\frame_004.jpg

### Only Build What You See [7:17]
**Transcript:** only build what you see. One thing we did with our mountains in the background, if we get up close  here, you'll start to see that these are actually just really simple cards and planes as well.  If you look from the top down, it becomes more obvious. But ever since Unreal 5 and Nanite has been  released, I think a lot of people default to using 3D models and 3D trees. But when we're seeing  the trees from this far away, there's no clear advantage to using 3D models. So instead, we opted  to use tree cards. And that way we can paint a bunch of these anywhere we want across the landscape.  And that way far away in the distance, our trees will still hold up and add some rough edges to our  landscapes without taking down our render time. And if we see an area that we want to paint on  some more trees, it's really easy to make those adjustments on the fly and to add in trees  shot by shot. Now, another thing we did, which helped the overall team, was separating our environment

**Frame:** tutorials\frames\how-to-create-cinematic-environments-in-unreal-engine-5\frame_005.jpg

### How to Use Levels for Cinematics [8:08]
**Transcript:** into levels. Now, how does this work? Levels are just another way to organize all of the actors  in your outliner into separate groups. So not everyone on our animation team had great work  stations where they could show all the lights, particles, and effects. So we just made these  effects and geometry levels. So we can still adjust the animation of our actors, but we don't have  to load in our entire scene in the background. And later on, we could easily swap out our lighting  levels and change it for different times of day. And you can fully control your levels inside of  sequencer by creating a level visibility track. That way, we can keep our characters and geometry  exactly the same in this wide shot, but just change the lighting in time of day.  Which brings us to our last environment, the graveyard and the location of our last battle

**Frame:** tutorials\frames\how-to-create-cinematic-environments-in-unreal-engine-5\frame_006.jpg

### Landscape Tools [8:59]
**Transcript:** between the sunrise.  First, we use Unreal's landscape tools to create depth and sculpt a custom landscape. And there's  a few methods we use to add movement and animation into our environment. First, let's talk about  how we use the landscape tool. So we just created a small landscape around the center of our scene.  We have a separate water plane that makes up the water itself. And then we're just taking the sculpting  tool of our landscape to brush. When you're sculpting, just click anywhere to raise that surface up,  or shift click to push it further down. And this way, we can block in something that looks  fairly complex, but was actually quite simple to set up. But one thing that's not as well known  is using landscape grass in your material. Landscape grass is a way for us to populate  foliage across our entire ground. And this way, we can add a lot of high detail geometry and  fidelity up close and also help hide our character's deep in the ground, but we don't have to place  anything by hand. And if we wanted to change our landscape and paint in different areas in the  background, this foliage will automatically populate and it'll go on top of any surface it's  supposed to...

**Frame:** tutorials\frames\how-to-create-cinematic-environments-in-unreal-engine-5\frame_007.jpg

### Background Birds [11:22]
**Transcript:** And lastly, here's a few methods that you can use to add movement and animation into your own  environments. My favorite way is to add birds into the background. These help create scale by showing  the movement and speed of the birds. But it also adds that animation and randomness from real life.  I tested out all the birds on the Unreal marketplace and I wasn't really happy with any one  particular system. So we went ahead and built our own background birds, which is now available  at Unreal for VFX.com slash birds. We created six drag and drop systems that you can easily bring  into any project you use in the future. And within two clicks, you can drag in your birds,  change their speed, flight path color and animation. And then you never have to mess with it again.  You can instantly upgrade your scenes and make them feel bigger, more complicated and more photo  realistic by adding in background birds into any shot. And personally, I have not made an environment  without using these since they were created. You might be surprised how something so small can  make such a big impact. So go and download these other on sale this week only now available at  Unreal for VFX.com slash bi...

**Frame:** tutorials\frames\how-to-create-cinematic-environments-in-unreal-engine-5\frame_008.jpg

### Cloth Simulations [12:31]
**Transcript:** to our flags and banners here. Let's go up close to this flag and take a closer look.  Now to preview a cloth simulation, usually you'll have to start simulating your game.  And now we can see the results of this blowing in the wind. Now how do you set up cloth for flags?  So that they simulate at render time. What all you need to do is that you have to set this up as a  skeletal mesh actor. So create your flag mesh in a software like blender, make sure to  testulate it before you bring it in. Having extra geometry here will help our simulation.  So create a simple cloth card, then just export this as an FBX file. And then just click and drag  the file into the content browser to import it. And then we want to import this as a skeletal mesh.  Now open it up and we have our skeletal mesh editor. And now we have to add in our cloth.  So you can right click on your asset and create clothing data from this section and create.  This will add clothing data. But we're not done yet. Just right click on your mesh again and  apply the clothing data. The last step is activating our cloth paint. And here we can paint anything  that's simulated white and anything we don't want to simulate to be...

**Frame:** tutorials\frames\how-to-create-cinematic-environments-in-unreal-engine-5\frame_009.jpg


---

## Structured Notes

### Core Technique
Nine environment animation techniques for the War of Being cinematic in UE5: 3-stage blockout workflow, cloud cards, floating rock animation via empty actor, level sub-layers in Sequencer, landscape sculpting, landscape grass, and cloth simulation on flags using Skeletal Mesh + Clothing Data.

### Summary
Josh Toonen demonstrates nine practical techniques used in the War of Being cinematic to make a static environment feel alive in UE5. Viewers learn the professional 3-stage environment workflow (blockout cameras before detailing), cloud card materials, how to animate floating rocks via a parent empty actor with looping rotation, organize the scene with sub-levels controlled by Sequencer's Level Visibility track, sculpt landscape terrain, use landscape grass nodes for automatic foliage placement, and set up cloth simulation on flag meshes using UE5's built-in Clothing Data system — all without external plugins.

### Key Steps
1. **3-stage workflow**: (1) Blockout rough geometry; (2) block camera angles in Sequencer before adding detail; (3) build only what the camera sees.
2. **Cloud cards**: Create plane meshes with a translucent material (Blend Mode = Translucent); use a noise texture as Opacity with Two-Sided = true; set a fake fog material for atmospheric blending.
3. **Floating rocks (looping)**: Select rock meshes, create empty actor parent, parent rocks to it; add Transform track in Sequencer; keyframe rotation at frame 0 and at sequence end (same rotation value); set Pre-Infinity and Post-Infinity = Linear for endless looping rotation.
4. **Level sub-layers**: Create separate levels for effects, geometry, and lighting (File → New Level → Empty Level; World Settings → Persistent Level); use Sequencer Level Visibility track to toggle per-level visibility per shot.
5. **Landscape sculpt**: Modes → Landscape → Sculpt; click to raise, Shift+click to lower; use the Smooth brush after sculpting.
6. **Landscape grass**: In the Landscape Material, add a Landscape Grass Output node; assign a Grass Type asset with a static mesh; UE5 auto-populates the landscape with the foliage.
7. **Cloth simulation on flags**: (a) Model the flag as a standard mesh in your DCC; (b) export as Skeletal Mesh FBX with a simple bone chain; (c) import to UE5 as Skeletal Mesh; (d) right-click in Content Browser → Create Clothing Data; (e) open the Skeletal Mesh, go to Clothing tab → Apply Clothing Data; (f) use Cloth Paint tool to paint influence: white = fully simulated, black = pinned.

### UE Systems / Blueprints / Settings
- **Cloud card material**: Plane mesh; Blend Mode = Translucent; Opacity = noise texture; Two-Sided = true; no lighting (Unlit or Lit with emissive)
- **Looping rotation**: Parent empty actor; Sequencer Transform track; keyframe rotation 0° at start and end; Pre/Post Infinity = Linear
- **Level Visibility track**: Sequencer → + Track → Level Visibility; assign sub-level; keyframe visible/hidden per shot
- **Landscape Grass**: Landscape Material → Landscape Grass Output node → assign Grass Type asset; grass density and scale set in Grass Type asset
- **Clothing Data**: Right-click Skeletal Mesh → Create Clothing Data; Skeletal Mesh Editor → Clothing tab → Apply Clothing Data; Cloth Paint = white (simulated) / black (pinned)

### Difficulty
Intermediate

### UE Version
UE 5.x

### Tags
cinematics, sequencer, geometry, animation, materials, lighting, intermediate

---

## Related Entries
- [[unreal-engine-masterclass-animate-environments-the-easy-way]] — 8 animation techniques including ship animation and Niagara user parameters
- [[how-to-make-a-samurai-film-in-unreal-5]] — War of Being production context and stage actor pattern
- [[master-cinematic-fog-volumetric-god-rays-in-ue5]] — fog and volumetric lighting to enhance environment depth
