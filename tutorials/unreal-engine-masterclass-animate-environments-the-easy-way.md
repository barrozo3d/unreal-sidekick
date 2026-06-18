---
title: Unreal Engine Masterclass: Animate Environments The Easy Way
source: YouTube
url: https://www.youtube.com/watch?v=4-_mXW1Vwuo
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [cinematics, animation, niagara, sequencer, mrq, tsr, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-masterclass-animate-environments-the-easy-way/
frame_count: 10
---

# Unreal Engine Masterclass: Animate Environments The Easy Way

**Source:** [YouTube](https://www.youtube.com/watch?v=4-_mXW1Vwuo)
**Author:** Josh Toonen
**Duration:** 22m52s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** I think a lot of people misunderstand why Unreal Engine is so powerful for visual effects and filmmaking.  Look, there is no reason to use Unreal Engine if you're just gonna render out still images.  The biggest advantage of using Unreal is that you can render entire sequences in minutes  when the same thing would take you hours or days in a different 3D software.  And there's been some incredible environment art coming out of Unreal 5.  But when you see sequences, there's nothing moving inside of it.  And if you want to use Unreal to make movies just like I do,  you need to make your images move.  So if you were to transform your renders from still images and static scenes into something with life,  animation, and movement, then stick around to the end because I'm gonna go over eight different  techniques that are simple and repeatable in all your projects going forward.  What's up, my name's Josh Tunin and for the last eight years I've been working as an artist and  supervisor on Hollywood films. And I've been using Unreal Engine on set and to make movies of my own.  And right now, filmmaking is still really hard and complicated and unreal, but I want to take what I've  learned o...

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_000.jpg

### What are we going to animate? [1:19]
**Transcript:** usually you'd start with blowing grass or trees, something moving in the wind.  But because everything in the scene is hard surface, we have to start getting creative right away.  So what can we add movement and animation to inside our scene? Well, the first thing that I can see  are the ships in the background. We can have those flying through the air. Next, we have our character  here, which characters can be kind of daunting, but I'll show you a really simple way to add animation  to our character. We can also animate our camera so we can add a little bit of camera shake and a  simple dolly in. But by giving it some handheld movement, it'll really ground our shot in reality.  The next thing we can do is add movement to the clouds, just so everything in the scene is moving  and it's dynamic. And stick around if you want to learn some of my best tricks with Niagara  particle systems. So we can create some steam elements that we can populate throughout our scene,  where we can take one master system and give it a couple of user parameters so we can change the  size and speed as we populate it around. First off, let's create a new level sequence and we'll

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_001.jpg

### Animate Ships in Sequencer [2:15]
**Transcript:** call this LS animation. And I'm just going to add my camera into the level sequence. So you can do  that. And if there isn't a camera already, it'll automatically create a camera cut track as well.  That way we can view this camera without worrying about moving it when we click this little camera  icon here, otherwise you can use the shift C hot key. So the first thing that we can see here is the  two ships flying in the distance. So let's start off by animating those flying through the air.  So I'm just going to select one of the ships and I'm going to press the F key so that I'll teleport  towards these objects. We can see that there's two different objects here. They're not grouped  together. They're not the same mesh. So one thing I'm going to do right off the bat is I'm going to  create an empty actor and I'm just going to drag it on top of our ship here. Now I want to take the  two objects that create the ship and just parent them to our actor. So I'm just going to click and  drag them in the outliner. You can see it won't let me do it at first because they're set to static.  So I'm just going to change these objects to movable empty actors are movable by default. And then  w...

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_002.jpg

### Quickly animate characters [5:04]
**Transcript:** mesh. It's not a skeletal mesh in order to apply animation it has to be a skeletal mesh. We do  have a skeletal mesh version of our character here but we don't have any animations. And I go more  in depth about character animation in my last video so make sure to check that out if you want to  learn more. And in that video I took a model that already existed from miximote.com and imported  into Unreal. But here we have a character that has a rig but it doesn't have the same rig as miximote.  So we could just import our character into miximote. It'll create a brand new rig and then apply  that animation to the rig or we can retarget that animation to our existing skeleton. So I'm going  to very briefly show you how to do that and what I'm going to do is right click it go to asset  actions and I'm going to export this as an FBX. I like creating a round trick folder if I'm going  in out of Unreal and on select level of detail we don't need collision or morph targets or anything.  And in fact we're going to lose all of our rig data. So what I'm going to do is I'm just going to  import our worker rig into blender and I'm going to remove that rig. So we have our worker rig.FBX  going to ...

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_003.jpg

### Animate clouds (Ultra Dynamic Sky) [8:02]
**Transcript:** into our scene. This is using a plugin called ultra dynamic sky which I also used on that  samurai sword fight. I can't recommend it enough. It's a great sun and sky system. It has some  really awesome features. It can be pretty complicated but a lot of the basic settings are up here  at the top. And we don't want to do animate time of day. We want to animate our clouds only.  So if we go to cloud movement we can very quickly set this to one. And by default this randomized  cloud formation on Rondas checked to true. We want to set this to false. So every time when we preview  our animation it'll start at the same exact spot. So a really important note here we're going to  render through movie render queue. In order to get an accurate understanding of what Unreal is going  to render you actually need to play or simulate your game. This causes a lot of issues when rendering  but this is what's happening under the hood. If you're simulating and you're trying to dial in  your settings like I'm adjusting the ultra dynamic sky. And if you right click here you can keep  your simulation changes or just press K as a hotkey. And this means when I press stop here  it's going to keep that clou...

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_004.jpg

### Niagara Smoke and Steam [9:10]
**Transcript:** over Niagara particle systems and the different ways that we can create smoke. So I'm not going to  go through and create these smoke elements from scratch. But I want to cover the techniques that  you can apply to any Niagara system that will still keep them very simple and lightweight  but allow you to move them around and customize them so that you can have these dynamic elements  that you can move around. So there's two different techniques going on here and both of them are  using sprite sheets. One of the biggest limitations of real-time render engines are the texture memory.  So a lot of times it can be difficult to bring in raw video into a game engine. So typically you have  to find some way to optimize them and bake these things down into images and that's where sprite  sheets come into place. So what's going on in this system here is every particle that's spawning is  randomly picking one of these images. We have a four by four grid here so we have 16 total images  and because our smoke is spawning so quickly you don't perceive that we're just picking random  sprites out of this contact sheet. So in our Niagara editor all that we're using to drive this  is this sub-image...

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_005.jpg

### Bird Particle Systems [13:00]
**Transcript:** size of the smoke is it'll give us a sense of scale in our scene. So the next thing that we can add  are birds. But birds are a great thing in any naturalistic scene which will just give you a sense  of scale. The smaller the birds are in the frame the larger your scene is going to look. So we have  these these are from the legacy system. You can get packs like these from the marketplace or build  your own. But essentially they're just swarming particles with a simple bird model that's just  flapping its wings and you can see here it's a it's a small thing but you can now drag these around  inside your scene. And I'm just going to change their color to lack here so they really start to  cut out against the sky and we could even slow these down. So I wouldn't recommend trying to dig in  and learn the legacy particle system cascade. Definitely just focus on Niagara. It's just much better.  So now by populating these around throughout the scene now our sky is already feeling extremely  active compared to where it was just a few minutes ago. And now if we want to take that steam system  one step further we can actually parent this to our ship actors. So we're going to drag this in  so ...

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_006.jpg

### Niagara User Parameters [14:20]
**Transcript:** is setting up different user parameters. So there's this little user parameter section in every  Niagara system where you can add in custom variables. Most of them just are float variables which  is just any number. And then you can set up you know things like opacity, size, spawn rate,  and link them up anywhere here by just dragging down here and typing in any user variable that you've  created. And one thing that we can do is change the lifetime but I don't have a custom parameter  so all you have to do is we'll create a new float we'll call this lifetime. And initialize  particle is where the lifetime settings are. So you can see right now it's set to 16 so I'm  going to set this to 16 by default so it doesn't mess up any of my other existing smoke systems.  And now I'll set this to lifetime. So now the lifetime variable is linked here we know it's 16 by  default but now if I hit save and I go back into my scene we have this we have the smoke emitter here  we'll now have this new variable call lifetime and let's change this to something way different like  35. So now all of our other systems are exactly as they were before but now we can have custom variables  for this one sing...

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_007.jpg

### Camera Shake [15:50]
**Transcript:** is our camera. So let's go through how to set up camera shake for our cameras. So unreal does include  a camera shake system so if I want to add a camera shake track you can see that's here but there's  nothing created by default. So this can kind of be hidden at first but it's just a couple clicks here  all we have to do to create a camera shake blueprint is we want to create a new blueprint class  and then we don't want any of these common ones we want to type in camera shake and we'll scroll  down here to default camera shake base. So let's call this VP camera shake medium and now when you  open this up you'll see that we have this Perlin noise camera shake pattern if this doesn't show up  sometimes when you first open it it'll look like this and it's a little confusing because you're  thinking where are all the settings they're just under this little tab here. Essentially what we  have is we have location and rotation settings. So let's add this camera shake blueprint into our  sequencer so we can start seeing the results. Now in our sequencer let's add a camera shake track  we can see now we do have this blueprint class and if we expand here we'll see by default it comes  in r...

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_008.jpg

### Movie Render Queue [20:40]
**Transcript:** clapper board if you don't see movie render queue and you just see movie scene capture it's because  we need to enable the plugin so just go to the plugins menu and type in movie render queue  and let's turn on both of these and then just save your project and reboot it so now with movie  render queue enabled let's press our clapper board and let's go into our config settings for most  situations especially just getting started we can just render this as a png sequence otherwise you  would be rendering this as an exr sequence but I think for most people this is going to be the most  common way to do this and then we can override our anti aliasing and set this to temporal super  resolution you typically want to change your temporal sample count to something like eight or 16  but one thing worth noting with our camera shake that we've added camera shake happens on every  tick that movie render queue is going to render so what that means is that if we're rendering 16  samples for every one frame our camera shake is actually going to go crazy it's going to play 16  times faster than what we would expect so if you do want to use that as your render settings you  just need to open up the...

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_009.jpg


---

## Structured Notes

### Core Technique
Eight environment animation techniques for static UE5 scenes: empty actor ship animation, character retargeting via Mixamo, Ultra Dynamic Sky cloud movement, Niagara sprite sheet smoke, bird flock particles, Niagara user parameters for modular control, Blueprint camera shake with MRQ compensation, and TSR anti-aliasing render settings.

### Summary
Josh Toonen delivers eight practical techniques to add life and movement to any UE5 environment scene for filmmaking. Starting from a completely static scene, viewers learn to animate hard-surface ships via empty actor parents, retarget characters through the Blender→Mixamo pipeline, animate clouds with Ultra Dynamic Sky's simulation system, build Niagara smoke using sprite sheets for performance-friendly particles, expose Niagara user parameters for scene-wide modular control, create a Blueprint camera shake class, and configure MRQ with TSR anti-aliasing while compensating for the camera shake temporal sampling problem.

### Key Steps
1. **Animate ships**: Select ship meshes → change to Movable → create Empty Actor parent → parent all ship sub-meshes → add Transform track in Sequencer → keyframe position/rotation for flight path.
2. **Character retargeting**: Export character FBX from UE5 → import to Blender → remove rig (select armature → X → Delete) → upload to Mixamo → auto-rig → import back to UE5 as new Skeletal Mesh → use IK Retargeter to transfer animations OR use Mixamo rig directly.
3. **Ultra Dynamic Sky clouds**: Set Cloud Movement Speed = 1; set Randomize Cloud Formation on Start = false (so render always starts from the same cloud position); use right-click → K shortcut to keep simulation state changes.
4. **Niagara sprite sheets**: In a Niagara sprite emitter, add Sub-Image UV module; set a 4×4 grid (16 images total); particles randomly pick one image per spawn for visual variety with a single texture.
5. **Niagara user parameters**: Niagara System editor → User Parameters section → + float variable (name: "Lifetime"); in Initialize Particle module, link Lifetime = User.Lifetime; set default = 16; in scene instances, the Lifetime override appears in Details panel.
6. **Blueprint camera shake**: Content Browser → New Blueprint Class → Default Camera Shake Base → name it VP_Camera_Shake_Medium; open → Perlin Noise Camera Shake Pattern → configure Location (X/Y/Z amplitude, frequency) and Rotation settings.
7. **MRQ TSR anti-aliasing**: MRQ settings → Anti-Aliasing → Method = Temporal Super Resolution; Temporal Sample Count = 8–16; camera shake fix: in the Blueprint Camera Shake class, increase Camera Shake Update Interval to compensate for faster temporal sampling.

### UE Systems / Blueprints / Settings
- **Empty Actor animation**: Create Empty Actor; parent sub-meshes; set all to Movable; Sequencer Transform track; keyframe position/rotation for movement
- **IK Retargeter**: For character retargeting; source = Mixamo skeleton, target = existing custom skeleton
- **Ultra Dynamic Sky**: Cloud Movement = 1; Randomize Cloud Formation on Start = false; press K (right-click → Keep Simulation Changes) to persist cloud position after Stop
- **Niagara Sub-Image UV**: Module in Sprite Renderer or Particle Spawn; Grid X = 4, Grid Y = 4; Random Row = true for variety
- **Niagara User Parameters**: Section in Niagara editor header; + float variable; linked to any module parameter; exposed in scene instance Details panel
- **Default Camera Shake Base Blueprint**: New Blueprint Class → DefaultCameraShakeBase; Perlin Noise Camera Shake Pattern; Location: Amplitude (X/Y/Z), Frequency; Rotation: Pitch/Yaw/Roll Amplitude, Frequency
- **MRQ TSR settings**: Anti-Aliasing Override → Temporal Sample Count = 8–16; Camera Shake Update Interval = increase to match sample count

### Difficulty
Intermediate

### UE Version
UE 5.x

### Tags
cinematics, animation, niagara, sequencer, mrq, tsr, intermediate

---

## Related Entries
- [[how-to-create-cinematic-environments-in-unreal-engine-5]] — 9 environment animation techniques including cloth sim and landscape grass
- [[create-muzzle-flash-gun-fx-for-unreal-5-cinematics]] — Niagara user parameters and system construction in detail
- [[unreal-5-hotkeys-every-filmmaker-must-use]] — Sequencer workflow and camera management hotkeys
