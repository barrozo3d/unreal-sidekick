---
title: Unreal Engine Masterclass: Animate Environments The Easy Way
source: YouTube
url: https://www.youtube.com/watch?v=4-_mXW1Vwuo
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5"
tags: [environment-animation, sequencer, niagara, camera-shake, character-animation, mixamo, ultra-dynamic-sky, sprite-sheets, user-parameters, movie-render-queue, cinematics, workflow]
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
**Transcript:** I think a lot of people misunderstand why Unreal Engine is so powerful for visual effects and filmmaking.  Look, there is no reason to use Unreal Engine if you're just gonna render out still images.  The biggest advantage of using Unreal is that you can render entire sequences in minutes  when the same thing would take you hours or days in a different 3D software.  And there's been some incredible environment art coming out of Unreal 5.  But when you see sequences, there's nothing moving inside of it.  And if you want to use Unreal to make movies just like I do,  you need to make your images move.  So if you were to transform your renders from still images and static scenes into something with life,  animation, and movement, then stick around to the end because I'm gonna go over eight different  techniques that are simple and repeatable in all your projects going forward.  What's up, my name's Josh Tunin and for the last eight years I've been working as an artist and  supervisor on Hollywood films. And I've been using Unreal Engine on set and to make movies of my own.  And right now, filmmaking is still really hard and complicated and unreal, but I want to take what I've  learned over the last year and a half and make it as simple as possible. So let's just jump right into it.  So starting off, we got this awesome scene. This was actually created by Justin Coulan,  who was someone I worked with over in the VAD department at Pixamundo.  And we were a part of the team building the underground temple environment for LED walls.  He made this as a personal piece and was kind enough to let me use it as an example for this lesson.  So shout outs to him. So if we wanted to start animating an outdoor scene,

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_000.jpg

### What are we going to animate? [1:19]
**Transcript:** usually you'd start with blowing grass or trees, something moving in the wind.  But because everything in the scene is hard surface, we have to start getting creative right away.  So what can we add movement and animation to inside our scene? Well, the first thing that I can see  are the ships in the background. We can have those flying through the air. Next, we have our character  here, which characters can be kind of daunting, but I'll show you a really simple way to add animation  to our character. We can also animate our camera so we can add a little bit of camera shake and a  simple dolly in. But by giving it some handheld movement, it'll really ground our shot in reality.  The next thing we can do is add movement to the clouds, just so everything in the scene is moving  and it's dynamic. And stick around if you want to learn some of my best tricks with Niagara  particle systems. So we can create some steam elements that we can populate throughout our scene,  where we can take one master system and give it a couple of user parameters so we can change the  size and speed as we populate it around. First off, let's create a new level sequence and we'll

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_001.jpg

### Animate Ships in Sequencer [2:15]
**Transcript:** call this LS animation. And I'm just going to add my camera into the level sequence. So you can do  that. And if there isn't a camera already, it'll automatically create a camera cut track as well.  That way we can view this camera without worrying about moving it when we click this little camera  icon here, otherwise you can use the shift C hot key. So the first thing that we can see here is the  two ships flying in the distance. So let's start off by animating those flying through the air.  So I'm just going to select one of the ships and I'm going to press the F key so that I'll teleport  towards these objects. We can see that there's two different objects here. They're not grouped  together. They're not the same mesh. So one thing I'm going to do right off the bat is I'm going to  create an empty actor and I'm just going to drag it on top of our ship here. Now I want to take the  two objects that create the ship and just parent them to our actor. So I'm just going to click and  drag them in the outliner. You can see it won't let me do it at first because they're set to static.  So I'm just going to change these objects to movable empty actors are movable by default. And then  we'll just do the same for the other ship and we'll just call these ship one and ship two. Now if I  click on the camera cut we'll see our original camera angle. Now let's add our empty actors into  sequencer. So I'm going to select these in the outliner and hit the add track button to the sequence  and then hit add current selection. So now that we have these in our timeline let's talk about how  sequencer works. Every object in an unreal scene has so much data all these different variables  in parameters associated to each one. So to change anything in sequencer we have to manually tell  to define and expose a certain parameter before we can change it. So let's create a simple flying  animation. Let's click the plus icon to create a keyframe on our first frame and then let's jump  to frame 150. We'll actually want to set our sequence to 24 frames a second and we also want to press  this snapping button. This makes it so wherever I drag in the scene I'm snapping to a frame as  opposed to the sub frames that would exist in a game engine. So I want both of these ships to move  forward at the same exact speed. So if I select my empty actor I can see they're moving in the  positive x axis because the red arrow of the transformation gizmo is pointing forward there.  So in sequencer let's add plus 40,000 units and set a new keyframe. So I want to do the same thing  to ship to and because it's so much further away even though we'll add the same amount of distance  it should appear to be moving slower which will help the scene feel bigger. But when we play this  one problem that we have is the ships ease in and ease out at the beginning and end of our shot  because by default unreal creates auto-bezzier keyframes. So in order for these to animate perfectly  straight like a ship would we just need to convert these to linear keyframe and we can do this by  selecting our keyframes and pressing the four key. Now when I look in the curve editor you can see  we have a perfectly straight animation. Awesome. Now we have our ships moving. Next up let's add some  movement to our character. But one thing that we can see here is that our character here is a static

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_002.jpg

### Quickly animate characters [5:04]
**Transcript:** mesh. It's not a skeletal mesh in order to apply animation it has to be a skeletal mesh. We do  have a skeletal mesh version of our character here but we don't have any animations. And I go more  in depth about character animation in my last video so make sure to check that out if you want to  learn more. And in that video I took a model that already existed from miximote.com and imported  into Unreal. But here we have a character that has a rig but it doesn't have the same rig as miximote.  So we could just import our character into miximote. It'll create a brand new rig and then apply  that animation to the rig or we can retarget that animation to our existing skeleton. So I'm going  to very briefly show you how to do that and what I'm going to do is right click it go to asset  actions and I'm going to export this as an FBX. I like creating a round trick folder if I'm going  in out of Unreal and on select level of detail we don't need collision or morph targets or anything.  And in fact we're going to lose all of our rig data. So what I'm going to do is I'm just going to  import our worker rig into blender and I'm going to remove that rig. So we have our worker rig.FBX  going to import this and because it's blender this will be brought in as an armature. So we'll just  take our worker rig and we'll just drag it off and then we want to just delete our armature modifier.  And now we can just export this again as an FBX. Now we'll have our mesh that we can import right  into miximote.com. So we're going to select our rig list version of it and because we've removed our  rig we're going to have a new auto-rigger that we'll need to add to our character. So now it's  going to compute and we'll have a rig version of our asset that we can now apply any miximote  animation to. All right now this is complete and I know there's a couple animations where we can  have our guy standing and doing some keep alive animation. We want to export this with skin at 24  frames a second. So now we can hop right back into Unreal. Let's import this as a brand new skeleton  and a brand new skeletal mesh. So we're going to select skeletal mesh, import the mesh,  leave the skeleton blank so Unreal knows to create a brand new one. And we're going to change the  material import method to do not create materials and import all. And now you can see we already have  an animation applied to our character. We can add our skeletal mesh into the scene by just  clicking a dragging or rotate him into place. And now that he's a skeletal mesh instead of a  static mesh we can add him into our sequencer. So add actor to sequencer and then it'll know to create  an animation track. So from here you can see we already have our animation assigned because it'll  automatically generate that list. And now when we press play we have our character animated inside  the scene. And now you can see it's looping and very quickly we already have our character animated.  We have these ships animated. But now let's add different environmental effects like the clouds  moving, birds and smoke and atmosphere in the easiest way possible. So to start adding cloud movement

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_003.jpg

### Animate clouds (Ultra Dynamic Sky) [8:02]
**Transcript:** into our scene. This is using a plugin called ultra dynamic sky which I also used on that  samurai sword fight. I can't recommend it enough. It's a great sun and sky system. It has some  really awesome features. It can be pretty complicated but a lot of the basic settings are up here  at the top. And we don't want to do animate time of day. We want to animate our clouds only.  So if we go to cloud movement we can very quickly set this to one. And by default this randomized  cloud formation on Rondas checked to true. We want to set this to false. So every time when we preview  our animation it'll start at the same exact spot. So a really important note here we're going to  render through movie render queue. In order to get an accurate understanding of what Unreal is going  to render you actually need to play or simulate your game. This causes a lot of issues when rendering  but this is what's happening under the hood. If you're simulating and you're trying to dial in  your settings like I'm adjusting the ultra dynamic sky. And if you right click here you can keep  your simulation changes or just press K as a hotkey. And this means when I press stop here  it's going to keep that cloud speed that I changed while simulating. So now I want to briefly go

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_004.jpg

### Niagara Smoke and Steam [9:10]
**Transcript:** over Niagara particle systems and the different ways that we can create smoke. So I'm not going to  go through and create these smoke elements from scratch. But I want to cover the techniques that  you can apply to any Niagara system that will still keep them very simple and lightweight  but allow you to move them around and customize them so that you can have these dynamic elements  that you can move around. So there's two different techniques going on here and both of them are  using sprite sheets. One of the biggest limitations of real-time render engines are the texture memory.  So a lot of times it can be difficult to bring in raw video into a game engine. So typically you have  to find some way to optimize them and bake these things down into images and that's where sprite  sheets come into place. So what's going on in this system here is every particle that's spawning is  randomly picking one of these images. We have a four by four grid here so we have 16 total images  and because our smoke is spawning so quickly you don't perceive that we're just picking random  sprites out of this contact sheet. So in our Niagara editor all that we're using to drive this  is this sub-image index and we're setting a random value per particle between 0 and 15 or  between 1 and 16. We're just starting at 0 instead of 1. And then if we go into our master  material to see how this works the specific thing that we need to use here is this particle sub-uv.  So this looks just like a texture sample except it's a specific node used to talk to our Niagara  particle system. So if I type in particle sub-uv you can see it's under the particles menu which  also could just be known as Niagara. And because we're using this node here in our material graph  Niagara knows to look for this and knows that it can modify this data where it can't do that  from a texture sample alone. So we're just taking this texture sample and then bringing that into  Niagara we're setting the sub-image index between 0 and 16 and then lastly in our sprite renderer  we're setting our sub-image size to 4 by 4. And with these four things in a row you need every  single one of them but when they're working together we get this pretty natural feeling particle  system. And now we can use these to dress them throughout our scene. The other method is to have  animated sprites. So this is a similar idea but the execution is just a little bit different.  So instead of picking a single random image out of a sprite sheet I've actually converted a video  clip into an 8 by 8 sprite sheet. And instead of picking a random image per particle it's actually  animating through here and playing it back. So each particle is animating they are the same exact  sprite but because they're evolving and they're moving and getting bigger over time you know  quite see where one particle starts and the other one finishes. And the only difference here is we  have our sub-image size set to 8 by 8. And instead of using the sub-image index there's another  particle update node that we can use called sub-uv animation. And this will tell it not to pick a  random image but to animate through the entire sprite sheet in a row so it'll emulate the idea of  video playback. But when it comes to texture memory this is still just a 2K image. So we're not  overloading our GPU. We're not loading in a 2K image for every single frame. We're loading in  one single 2K image and then we can populate this anywhere in our scene and there's almost no  limit to how many particles we could have in our scene now because we prepared it in this way.  And now that we have these prepared it's very easy for us to drag these around anywhere in our scene  and start to add different clouds and steam and smoke. And depending on how fast and large the

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_005.jpg

### Bird Particle Systems [13:00]
**Transcript:** size of the smoke is it'll give us a sense of scale in our scene. So the next thing that we can add  are birds. But birds are a great thing in any naturalistic scene which will just give you a sense  of scale. The smaller the birds are in the frame the larger your scene is going to look. So we have  these these are from the legacy system. You can get packs like these from the marketplace or build  your own. But essentially they're just swarming particles with a simple bird model that's just  flapping its wings and you can see here it's a it's a small thing but you can now drag these around  inside your scene. And I'm just going to change their color to lack here so they really start to  cut out against the sky and we could even slow these down. So I wouldn't recommend trying to dig in  and learn the legacy particle system cascade. Definitely just focus on Niagara. It's just much better.  So now by populating these around throughout the scene now our sky is already feeling extremely  active compared to where it was just a few minutes ago. And now if we want to take that steam system  one step further we can actually parent this to our ship actors. So we're going to drag this in  so it's by our ship. We'll probably have to make these a lot bigger. And one last I'll call it a  secret with Niagara just because I haven't seen it too much but it's by far the most useful feature

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_006.jpg

### Niagara User Parameters [14:20]
**Transcript:** is setting up different user parameters. So there's this little user parameter section in every  Niagara system where you can add in custom variables. Most of them just are float variables which  is just any number. And then you can set up you know things like opacity, size, spawn rate,  and link them up anywhere here by just dragging down here and typing in any user variable that you've  created. And one thing that we can do is change the lifetime but I don't have a custom parameter  so all you have to do is we'll create a new float we'll call this lifetime. And initialize  particle is where the lifetime settings are. So you can see right now it's set to 16 so I'm  going to set this to 16 by default so it doesn't mess up any of my other existing smoke systems.  And now I'll set this to lifetime. So now the lifetime variable is linked here we know it's 16 by  default but now if I hit save and I go back into my scene we have this we have the smoke emitter here  we'll now have this new variable call lifetime and let's change this to something way different like  35. So now all of our other systems are exactly as they were before but now we can have custom variables  for this one single system. Now let's parent this to our ship actor. All right well this is looking  cool we have a lot more movement and life inside of our scene but the one thing that isn't moving

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_007.jpg

### Camera Shake [15:50]
**Transcript:** is our camera. So let's go through how to set up camera shake for our cameras. So unreal does include  a camera shake system so if I want to add a camera shake track you can see that's here but there's  nothing created by default. So this can kind of be hidden at first but it's just a couple clicks here  all we have to do to create a camera shake blueprint is we want to create a new blueprint class  and then we don't want any of these common ones we want to type in camera shake and we'll scroll  down here to default camera shake base. So let's call this VP camera shake medium and now when you  open this up you'll see that we have this Perlin noise camera shake pattern if this doesn't show up  sometimes when you first open it it'll look like this and it's a little confusing because you're  thinking where are all the settings they're just under this little tab here. Essentially what we  have is we have location and rotation settings. So let's add this camera shake blueprint into our  sequencer so we can start seeing the results. Now in our sequencer let's add a camera shake track  we can see now we do have this blueprint class and if we expand here we'll see by default it comes  in really short this is just because the timing the duration is set to one and this is set in seconds  not in frames so you can just set this to a very long time like 150 seconds and now if we click on  this little camera in our camera cut section now we're previewing the camera we can see there's  still not much movement but if I change this location amplitude to something huge like 20 we can  see that you know what actually our camera is moving it's just our scene is so big that we're  not really seeing that movement. So it's nice to have a little bit of location movement but the big  thing that people associate with camera shake is actually rotation so if I set this to even one rotation  is a lot more sensitive than location because it's one degree of rotation our camera's already a lot  more bouncy if I set this to five we'd have this in five degrees and we're getting some intense  shake here and then frequency is what it sounds like it's the speeds. If I set it higher it will go  faster if I set it lower to point one it'll go slower so now we're at 10% of our speed if we're at  point one as opposed to the default of one. The biggest thing you should be aware of and what makes  the camera shake the most distracting is the amount of roll so the roll if you think of a plane  doing a barrel roll twirling around typically this is what's gonna make you feel most uneasy this is  still very intense obviously but just by removing that at least everything is framed up as it was  before so let me set this back down to one I'm gonna change the frequency to point five so we have  a bit of floatiness but it's nothing too crazy and now you can see we already have some pretty  naturalistic movement it's very easy to go overboard here but if you don't get any depth and parallax  by translating your camera through the scene it's still gonna feel pretty static like right now it's  just a person standing here with maybe a shoulder rig a handheld camera but the camera itself isn't  adding any depth into the scene so what we can do here is just set some transformation keyframes  so I'll just set a location and rotation and then I'll go to the last frame and instead of  looking through our camera cut if I click the camera icon next to the actor in the scene this will  make it so we can pilot our camera and now if I right click in the viewport and I move slowly  through the scene we can start to reframe our camera in a way that still looks good and makes sense  and a quick tip you can increase or decrease the speed of your camera through the mouse field  going up or down or you can use the camera speed on the top right of your viewport and then lastly  we'll just create one more keyframe for location and rotation and now we have a nice simple but believable  camera movement and then one last thing I would do here just to give us a little something extra  it's always nice to have something extremely close to the camera we don't have anything in between  our character and the camera so as a last step I'm just going to take some smoke let's duplicate that  and move it close to camera especially if it's something that we can kind of pass through and if  you scrub you can see exactly what that camera is going to do which will also help us reframe  where we want that smoke to be and now we just have a little bit of extra movement and life in  our extreme foreground nice and subtle but believable so let's do one last check just by  simulating our game and seeing how it looks and everything seems to be working as intended as you  can see the smoke particles take some time to boot up so let's go into movie render queue and set  up our final render settings so the way you'll normally do this is you would go and click this

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_008.jpg

### Movie Render Queue [20:40]
**Transcript:** clapper board if you don't see movie render queue and you just see movie scene capture it's because  we need to enable the plugin so just go to the plugins menu and type in movie render queue  and let's turn on both of these and then just save your project and reboot it so now with movie  render queue enabled let's press our clapper board and let's go into our config settings for most  situations especially just getting started we can just render this as a png sequence otherwise you  would be rendering this as an exr sequence but I think for most people this is going to be the most  common way to do this and then we can override our anti aliasing and set this to temporal super  resolution you typically want to change your temporal sample count to something like eight or 16  but one thing worth noting with our camera shake that we've added camera shake happens on every  tick that movie render queue is going to render so what that means is that if we're rendering 16  samples for every one frame our camera shake is actually going to go crazy it's going to play 16  times faster than what we would expect so if you do want to use that as your render settings you  just need to open up the camera shake and you'll just want to change the frequency of everything so  if you just do one divided by 16 this is how fast you'd want that playback to go and the one thing we  want to do is we want to include some warm up frames so in our case we just need our engine warmup  count so our ships require quite a bit so I'm going to change this to a high number like 512  anything in the engine warmup count it's not actually rendering these frames so it's fairly quick  we'll just take a few extra seconds and a lot of times I'll just add this game override so that we  force cinematic quality settings and then from here all we have to do is hit render local  and we're set and here's a look at the final renders for these shots so leave a like if you  learned something new and subscribe if you want to stick around because I'm breaking down the entire  behind the scenes of the animated film I made for Tesseract's music video for War of Being with  over five minutes of animation completely made inside of Unreal I'll see you next time

**Frame:** tutorials\frames\unreal-engine-masterclass-animate-environments-the-easy-way\frame_009.jpg


---

## Structured Notes

### Core Technique
8 repeatable environment animation techniques for UE5 cinematics: (1) Object animation via empty actor parents + linear Sequencer keyframes; (2) Static → Skeletal mesh character via Blender rig removal + Mixamo auto-rig; (3) Cloud movement via Ultra Dynamic Sky plugin; (4) Niagara sprite-sheet smoke (random selection vs animated playback); (5) Niagara User Parameters for per-instance customization; (6) Bird swarm particles; (7) Parenting Niagara systems to moving actors; (8) Camera shake via Blueprint + Sequencer track; plus Movie Render Queue camera shake frequency fix.

### Summary
22m52s Josh Toonen masterclass on adding animation and life to UE5 environments. Uses an underground temple scene (hard-surface). 8 techniques: (1) Ships — empty actor parent + Movable + Sequencer location keyframes + linear conversion (press 4); (2) Characters — static→skeletal via Mixamo (Blender strip rig → Mixamo auto-rig → UE import new skeleton + animation); (3) Ultra Dynamic Sky clouds (Cloud Movement = 1; Randomize = false; Simulate mode + K key to keep changes); (4) Niagara smoke sprites — method A: random sprite from 4×4 sheet (sub-image index 0–15 + Particle Sub-UV material node); method B: animated through 8×8 sheet (Sub-UV Animation node); (5) User Parameters — float variables in Niagara + link to attributes → per-instance control without editing system; (6) Bird particles from Marketplace (Cascade OK here); (7) Parent Niagara to ship actor; (8) Camera shake — Blueprint DefaultCameraShakeBase + Perlin noise; Sequencer Camera Shake track; duration 150s; tune rotation amplitude (1° = visible); avoid roll; add dolly translation + foreground smoke; Movie Render Queue frequency fix for multi-sample renders.

### Key Steps

**1. Animate rigid objects:**
1. Select mesh objects → change mobility to **Movable**
2. Create empty actor → parent both ship meshes to it → rename ("ship one", "ship two")
3. Select empty actors → Sequencer → Add Track → Add Current Selection
4. Frame 0 → plus icon = keyframe; frame 150 → move in Sequencer value field (+40,000 X units) → keyframe
5. Select keyframes → press **4** to convert to Linear (removes auto-Bezier ease in/out)

**2. Animate characters (no existing animation):**
6. Export static mesh as FBX → import into Blender → delete armature → re-export FBX (mesh only)
7. Upload to Mixamo.com → auto-rig → pick animation → export with skin at 24 fps
8. Import into UE5: Skeletal Mesh → new skeleton → Don't Create Materials → Import All
9. Drag skeletal mesh into scene → add to Sequencer → animation track auto-assigns animation

**3. Animate clouds (Ultra Dynamic Sky):**
10. Select Ultra Dynamic Sky actor → Cloud Movement = **1** (or desired speed)
11. Disable **Randomize Cloud Formation** → clouds start from same position every preview
12. Press **Simulate** (not Play) to see correct cloud animation; adjust settings live
13. Press **K** during Simulate to keep setting changes when stopping simulation

**4. Niagara smoke — sprite sheet (random):**
14. Material: use **Particle Sub-UV** node (not regular Texture Sample) with sprite sheet texture
15. Niagara: set **Sub-Image Index** = random float 0–15 per particle
16. Sprite Renderer: **Sub-Image Size** = 4×4 (must match sprite sheet grid)
17. → Each particle picks one random image; fast spawn rate obscures repetition

**4b. Niagara smoke — animated sprite sheet:**
18. Same setup but use **Sub-UV Animation** node instead of Sub-Image Index → animates through sheet in order
19. Set Sub-Image Size = 8×8 (for converted video clip); result = video playback feel at 2K memory cost

**5. Niagara User Parameters:**
20. Niagara editor → User Parameters section → add Float parameter (e.g., "lifetime")
21. In Initialize Particle module → change Lifetime setting to use the new User Parameter
22. Back in scene: each placed emitter now shows "lifetime" property → override per-instance without editing system

**6. Birds:**
23. Marketplace → bird particle packs (Cascade/legacy is fine) → drag into scene
24. Adjust color (dark to cut against sky), slow speed; populate in different scene areas

**7. Parent Niagara to moving actor:**
25. Drag Niagara emitter in Outliner onto ship actor → parented → smoke travels with ship

**8. Camera shake:**
26. Content Browser → right-click → Blueprint Class → DefaultCameraShakeBase → name "VP_CameraShake_Medium"
27. Open BP → PerlinNoiseCameraShakePattern → set Location Amplitude (20+ for large scenes) + Rotation Amplitude (~1° = visible, 5° = intense) + Frequency (0.5 = floaty, 1 = default)
28. ⚠️ Remove or set Roll to 0 — roll makes shake most nauseating
29. Sequencer: camera track → right-click → Add → Camera Shake track → pick the BP class → expand clip → set Duration = 150 seconds
30. Add translation keyframes (dolly in) for depth/parallax
31. Add foreground smoke near camera for extra depth

**Movie Render Queue — camera shake fix:**
32. Enable plugin: Plugins → search "Movie Render Queue" → enable both → restart
33. MRQ settings: Anti-aliasing → Temporal Super Resolution → Temporal Sample Count = 8–16
34. ⚠️ Camera shake plays at sample rate speed: open shake BP → Frequency ÷ sample count (e.g., 1÷16 = 0.0625) → set all frequency values to that
35. Engine Warmup Count = 512+ (particles need frames to boot up; not rendered, just fast)
36. Add Game Overrides → Force Cinematic Quality → Render Local

### UE Systems / Blueprints / Settings
- **Movable mobility** — required before adding any object to Sequencer for animation
- **Empty Actor as parent** — group multiple meshes for single transform keyframe; standard UE grouping technique
- **Linear keyframe (press 4)** — overrides auto-Bezier; use for mechanical/constant-speed motion like vehicles
- **Sequencer Add Current Selection** — add selected Outliner objects to timeline at once
- **Ultra Dynamic Sky** — third-party plugin; Cloud Movement float + Randomize Cloud Formation bool; preview requires Simulate mode
- **K key during Simulate** — keep changes made during Simulate back to object; avoids losing live edits
- **Particle Sub-UV node** (material) — required for Niagara to control sprite sheet sampling; Texture Sample alone won't work
- **Sub-Image Index** (Niagara) — set to random float per particle; picks single frame from sprite sheet
- **Sub-UV Animation** (Niagara) — animates through sprite sheet sequentially; emulates video without video texture overhead
- **Sub-Image Size** (Sprite Renderer) — must match sprite sheet grid (4×4, 8×8)
- **Niagara User Parameters** — float (or other) variables at system level; exposes per-instance overrides in scene Details panel; link via parameter name
- **DefaultCameraShakeBase** (Blueprint) → PerlinNoiseCameraShakePattern — built-in UE camera shake class; Location/Rotation/Roll amplitude + Frequency
- **Camera Shake track** (Sequencer) — add to camera track; Duration field in seconds not frames; must be long enough to cover shot
- **MRQ camera shake frequency fix** — multi-sample AA runs game ticks per sample → shake plays N× faster; compensate by setting Frequency = 1÷N in shake BP
- **Engine Warmup Count** (MRQ) — pre-simulate ticks before first render frame; essential for Niagara particles to reach correct state; free (not rendered)

### Difficulty
Intermediate. Multiple techniques combined; most individually beginner-level.

### UE Version
UE5

### Tags
environment-animation, sequencer, niagara, camera-shake, character-animation, mixamo, ultra-dynamic-sky, sprite-sheets, user-parameters, movie-render-queue, cinematics, workflow

---

## Related Entries
- `this-free-plugin-changes-filmmaking-forever-unreal-5.md` — OneClick Control Rig for character animation
- `unreal-5-secrets-every-filmmaker-must-know.md` — camera shake + DOF + Niagara bokeh techniques
