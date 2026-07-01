---
title: Create MUZZLE FLASH Gun FX for Unreal 5 Cinematics
source: YouTube
url: https://www.youtube.com/watch?v=wFhZxRJZN8E
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5"
tags: [niagara, vfx, gunfire, muzzle-flash, particle-system, cinematics, collision, sequencer, compositing, filmmaking, simcache, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/create-muzzle-flash-gun-fx-for-unreal-5-cinematics/
frame_count: 16
---

# Create MUZZLE FLASH Gun FX for Unreal 5 Cinematics

**Source:** [YouTube](https://www.youtube.com/watch?v=wFhZxRJZN8E)
**Author:** Josh Toonen
**Duration:** 19m12s | 16 section(s)

---

## Raw Data (for Claude Code extraction)


### How to Create Gunfire and Muzzle Flashes in UE5 [0:00]
**Transcript:** If you want to make action films, it's never been easier with Unreal 5.  Today, you'll learn how I created these explosive gunfire and muzzle flashes for my Godzilla  short film made entirely inside of Unreal Engine 5.  And the best part, you set up the system once and Unreal 5 does all the work for you.  What's up, my name's Josh Tunin, and for the last 8 years of work in Hollywood Visual  Effects on movies like Dungeons & Dragons, Across the Spiderverse, and Godzilla vs.  Calm. And I want to share some of the biggest lessons I learned making a Godzilla short of my  own in Unreal 5. Whether you're making movies, games, or you just want to blow stuff up for fun,  by the end of this video, you'll have all the skills to bring your own action sequences to life.  Subscribe to the channel and let's get started.  So let's break down each layer of our gunfire system and create it step by step.  So here are the three main components. We need our muzzle flash, we need our tracer

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_000.jpg

### Breaking down our Gunfire system [0:54]
**Transcript:** fire, and we need our impact spark explosion. So first, we need our muzzle flash, which is just  a picture of a real muzzle flash, then we need a light to cast light onto objects and into our scene.  Then we need to shoot out a bullet that will collide with our environment. We want to spark  impact to collide in the opposite direction. So let's create this interactive procedural system  so that we can move around our gun and have dynamic impacts every single time. And to follow  along, all you need is a picture of a muzzle flash. So let's start building. Let's right click

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_001.jpg

### Start from a Niagara template [1:26]
**Transcript:** in our content browser and create a new Niagara system. And let's create a new system from a  pre-existing emitter. There's a couple templates that are included with Unreal that we can start from.  A muzzle flash is literally a small explosion at the front of a gun. So to recreate this,  let's start from a directional burst. Just click on directional burst and press on the green  plus arrow and then press on finish. Now let's name this and start with NS for Niagara System and  call it NS Gunfire. And now we can see our Niagara editor. This lets us create and modify particle  effects in Unreal. Now we have this little preview window on the left, but it's a little limited,  so I like to just click and drag this directly into the scene and use that to start building.  I'm just going to take this system, parent it to our rifle and reset the transform. And I want to  align this system to the very front of the gun. But the default behaviors here are a little messed up.  So let's dive in. Now Niagara is definitely a tool by game developers for game developers. So here's

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_002.jpg

### How Niagara works (for cinematics) [2:26]
**Transcript:** a quick run through for the rest of us using Unreal Engine for filmmaking. Niagara graphs are being  executed from the top of each system all the way down. So we start by spawning and modifying the  attributes of our spawn particle. And then in our particle update, we add in different effects and  forces before rendering it out as a sprite. And a sprite just means each particle is an image. So  first off, we need to create that muzzle flash of an automatic rifle firing over and over and over  again at a concentrated speed. So to do that, let's go to the very top of our system and start  making some changes. Now this default system only bursts one single time. And I can tell this  by recompiling this particle system, and you'll notice that it restarts it every single time.

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_003.jpg

### Creating automatic gunfire - spawn rate [3:10]
**Transcript:** So that's not what we want. We want constant, consistent, automatic fire. So instead of spawning a  burst instantaneously, let's click on this module and delete it and instead replace it with a  spawn rate node. This will give us a consistent spawn rate and let's set this to a value of three.  This will get us started, but we need to do one more thing and that's changed this loop behavior  to only play one single time and instead play it infinitely. And now we have a stream of particles.  Now this is super basic, but let's dive in and make it look like a muzzle flash. Now we need to  get rid of all the other effects like gravity, drag and all of the randomness here. We just want  that pop of the first explosion coming out of the gun. So let's take things like drag, gravity,  and forces and velocity and even scaling the sprite size by the speed and delete all of that.  So now we're responding a few small particles at the front of the gun that aren't moving anywhere  and to make them a bit bigger in the size of a muzzle flash, let's go into initialize particle

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_004.jpg

### Adding your first Muzzle Flash [4:07]
**Transcript:** where we can set the lifetime and particle size. So let's change the sprite size over to a uniform  value and let's make that a value of 60 and now let's reduce our lifetime. So let's change this  to direct set and give an exact lifetime and we want to set this to something really, really short  in a movie of muzzle flash is only visible for one single frame. So we want to recreate that  in our own cinematics. So instead of having our lifetime set to one second in that particle  disappearing after one entire second, let's set it to 0.05 and this will make that particle flash  on and off. And there we go. Now it's crude but we do have our first muzzle flash. All we have to  do is swap out this sprite so that it's a picture of a real muzzle flash instead of this circle.  So to change that out, let's go to the bottom at our render tab and select sprite render and we  need to create a new material to replace our sprite. So I've already imported in a mature,  but let's make a simple material for this sprite. I'm going to create a new material called  underscore muzzle flash. Now let's drag in our muzzle flash image. Let's plug that into the  emissive color and then to get rid of this black outline, I'm going to change this from an opaque  blend mode over to an additive blend mode. So that muzzle flash adds on top of our scene. I'll also  build in a simple multiply control that we can plug in and modify later on. And let's just call that  brightness. And now let's apply our new material. And there we go. Now we have the beginnings of our  muzzle flash. But now it's time to add our bullet and have it dynamically collide with our environment.

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_005.jpg

### Bullets and tracer fire [5:45]
**Transcript:** So let's create a new bullet. I'm going to select our directional burst here. Let's actually rename it.  So I'm just going to press on the F2 key and call this our muzzle flash. And now we can  right click here, copy and paste. And now let's call this bullet. The only difference is under  particle spawn will need to add in velocity. So let's type in velocity. And with Niagara,  the order really matters here. But they do a great job of telling you when something's broken. So  you can just press on these fix issue buttons to fix any problems with the order there. And now in  our add velocity menu, let's change this from linear to in cone. Now a big problem here though is  our lifetime is super short. So we need to lengthen that so that bullet can cast off and travel  through space. So let's go to initialize particle, which has all of our default settings.  And let's change that lifetime over to a value of two seconds. Now obviously our velocity is super  slow. So we'll need to add a lot of velocity here. I'm going to add about 1500 units. And I'm  going to change the cone angle down to zero so that there's no randomness in the direction of our  bullets. Now obviously the particle is too big, but we can change that as well. And a great module  here is scale sprite size by the speed, which means that we can scale our bullet to be longer  in the direction that it's already traveling, which is great for bullet tracers. And if we scale  this in Y, that means our bullet will stretch out in the direction that it's traveling. And as a  last thing under your sprite render, you want to change over your alignment from automatic to  velocity align. Now this is great, but we need to make sure that our bullets collide with the  environment. So under particle update, let's add in a collision note. Now with this collision here,

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_006.jpg

### Add collisions in Niagara [7:29]
**Transcript:** you can see that the bullets are literally bouncing off that wall and traveling backwards. And if  we moved our rifle around here, you can see that it dynamically collides with any part of our  environment. Now this is cool, I guess, but we need to make sure that that bullet impacts that wall  and then creates a burst of spark launching off in the opposite direction. So let's handle that  next. So first off, let's make sure we kill that particle after it bounces off the wall. To do  that under particle update, let's add in a new module called kill particles. And we want to set this  kill particles to true after our particle has collided. So we can do this by pressing on the down  arrow and literally just type in has collided. And this makes it so every time a bullet collides,  that it dies on impact. But now we need to spawn another particle emitter for our spark impact.  So let's right click in our Niagara graph and create a new emitter. And let's start from one of

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_007.jpg

### Creating impact sparks [8:27]
**Transcript:** their presets. And this time, let's pick a directional burst. So we're starting from the same thing,  except remember, it's spawning from the original location, not from the impact of our collided  particle. So to fix this directional burst, let's just go to the sprite render and change this  alignment over to velocity aligned. And that's going to give us a much better looking impact.  But how can we spawn this as soon as a particle collides? Well, to do this, we need to use something  called an event handler. All this does is let the Niagara system know every time a particle collides  where it happened. So to set this up, let's open up that Niagara system. So in our bullet that's  firing through our environment under particle update, let's press on the plus button and type in  generate collision event. And in order for this to work, you just need to go to the top of your  emitter and make sure to enable persistent ID and press compile. Now this system will know  every time there's a collision. But we need to make sure to transfer that information and spawn  particles from the impact. So to do that in our new spark burst setup, let's press on this small  stage button and add in our event handler. The important thing here is that we're looking for  an event source, which we just created in our other emitter. So let's change the source over to  a collision event. Let's spawn 20 particles every time there's a collision event. And let's change  the execution mode to spawn particles. Now we just need to do one last thing under the event handler.  Type in collision so that we can receive a collision event. Now if you follow it along, you should have  a particle system that shoots out bullets and creates a new particle system where that impact  happens. But our impact is flipped. We needed to shoot in the opposite direction. That's super,  super simple. As a last step, just go to your ad velocity in cone and change that cone axis  instead of being in the forward x axis. Let's invert it and change that to negative one. And that'll  just flip it around so it shoots off in the opposite direction. And now every bullet has the  right impact regardless of what angle you're shooting from. Now to refine this and clean some things  up, we can also add some collision to our spark impact. So now that we have everything working here,  if we want them to bounce and collide with the rest of the environment, let's just go to the  particle update and add in another collision node. And now not only do we have great impacts,  we also have them colliding and interacting with our environment even further. I like changing the  advanced aging rate after collision. So we can have that lifetime evolve twice as fast after that  first collision. We're missing one key ingredient and that's adding light interacting with the rest

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_008.jpg

### Interactive Light with Niagara [11:03]
**Transcript:** of our environment. But it's really easy to add in under our muzzle flash system. Let's get this  setup first and under our render tab, let's add in a new light render. Now there are some weird  particular settings that you need to use here. They're not so photorealistic as the rest of the  lighting system in Unreal, but it can still be really effective. What I normally do is I'll change  this radius scale to something big like 64. And then in this case, I'm not going to use the  inverse square falloff. This is going to cast a ton of light into the scene, which is not exactly  what we want here. So let's change our default exponent to something like 800. So it just appears  around the gun itself. Now we can also change the color by adding a little bit of red  into this light. So it starts to cast bright light into our scene. But you're probably wondering,  can we add this to the bullet flying through the scene? And the answer is yes. You can literally  copy this light render and paste it in our bullet system. And now we have a light attached to each  bullet. Now we're going to make these a bit darker because I want those muzzle flashes to be the  brightest thing in our scene. So I'll change that default exponent to a higher value.  And now we can add interactive lights to every layer of our scene. You can also change the  particle color in that initialized particle tab so that we can tint everything to be a bit more  orange instead of perfectly white. So there is our particle system, but how can we add it into our shot

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_009.jpg

### How to Animate our Gunfire On/Off [12:30]
**Transcript:** and decide when to fire and when not to? Well, let's talk about that next. If you want to learn how I'm  a big budget action sequences from home, it's all using Unreal Engine 5. And this week, I'm going  to share all my secrets in the live Godzilla masterclass. Sign up today at unreal for vfx.com slash  Godzilla. And I'll show you how to recreate all the on set filmmaking techniques that go into  your favorite plotbuster movies, even if you're not an animator yourself. You don't want to miss out  so make sure to register today at unreal for vfx.com slash Godzilla. Now let's add this intense gunfire  into a real action scene shooting down Godzilla. So let's add in some muzzle flashes onto our helicopters  in this shot. To do that, I'm just going to click and drag our gunfire into our scene. And you can  see right away it'll start shooting some bullets at Godzilla. Now if we want to animate anything,  we have to add it into sequencer. So let's add our Niagara system into sequencer. And let's create

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_010.jpg

### Using Niagara in Sequencer [13:27]
**Transcript:** a new attached track and attach it to our helicopter. And now you can see we already have our particle  system shooting down Godzilla. But how do we change the timing of our gunfire? What if we wanted  to start it intense and stop halfway through? Well, if you didn't know already, we can build some  custom controls and menus into any Niagara system. Let's double click on our gunfire system  and create something known as a user parameter. Just like in materials, we can create customizable  parameters that we can change on the fly and even add animation and keyframes to. Let's start  animating our spawn rate first. So to do that, I'm going to click on the spawn rate of our muzzle  flash and click on this down arrow and you type in user, which will let us create a new user parameter.  Now we need the spawn rate of our muzzle flash and our bullets to be exactly the same. We can have  some faster than others. So let's go to the spawn rate of our bullets and change our spawn rate  here over to a user parameter. But now we can select the one we just created called spawn rate.  Now these two are linked together. And when I jump back into our viewport, if I look on the right  side, I can see we have a new user parameters area here. So let's change this over to a value of  three. So we're firing off three at all times. But if I wanted to keyframe this on or off,  I'll just go to the gunfire inside of sequencer and let me add in a Niagara component track.  This will let us modify anything inside of Niagara. So I'll add another track inside here.  And now you'll see we can create a track for our spawn rate. What this means is we can start with  a spawn rate of three and then halfway through our shot. We can change that to a spawn rate of zero,  which would turn off our gunfire halfway through. Let's slide this to the right. And now we can see  that gunfire stops halfway through. And now we're ready to render out our scene. Now a big roadlock  a lot of people face is that they can't get the same result every time they render out of Unreal,

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_011.jpg

### How to get consistent renders with Niagara and Sequencer [15:25]
**Transcript:** especially with Niagara. But if you follow this, you'll get the same results every single time.  All you need to do is go to edit plugins and enable the Niagara SimCash plugin.  If you enable this inside of sequencer, we can click on that Niagara component and add a Niagara  Cash Track. What this will do is give us a little record icon here. And if we press on the record  button, it'll go through our sequence and create an exact position for every single particle in our  shot. And this will make it identical if we ever go back to re-render this later. Now we could  render this out as is and just render this out of movie render queue. But I like to isolate each

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_012.jpg

### Rendering with Movie Render Queue [16:05]
**Transcript:** layer of my scene and composite them together. Now most people over complicate isolating render layers  inside of Unreal. Basically, all we need to do is just disable or hide everything that we don't need.  So hide any extra levels or geometry that is not being used. Once your viewport matches what you  want with everything turned off, then you can go to render. Once we have a render where our  muzzle flashes and impacts are isolated, then we can start combining it together. But how do you  go from particle system to Hollywood level visual effects? Well, that's where the next most important

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_013.jpg

### Compositing your Gunfire in Nuke [16:40]
**Transcript:** step comes in and that's compositing. Compositing is just Photoshop for video. But for us, it's where we're  going to add in lens flares, lens dirt, and anything that makes it look better. By adding this layer  on top of our original render, I want to share a couple extra techniques I used to take these shots  even further. I also rendered out a couple of extra spotlights that mimic the same position and  lighting of our muzzle flash. By combining this custom light with the other muzzle flashes,  I was able to art direct that lighting while still getting custom dynamic particle effects  from the system without animating anything myself. And now our scene feels more intense.  And you can make these look even better by having these muzzle flashes interact with smoke and  rain. You'll notice in this shot where we're firing from the cockpit of a helicopter,  that if I pause on any dynamic frame here, that the muzzle flash is lighting up all the surrounding  rain. Now how do we do that? Well, first it was by laying out real stock footage of rain that I could  place in my 3d scene. But then it's by isolating that muzzle flash layer, blurring it out,  and multiplying it against that rain stock footage. And by multiplying these two layers together,  we get the dynamic interaction frame by frame without putting in a bunch of extra work. And again,  I created extra layers of dynamic interactive light so we can feel all the sparks and muzzle flashes  bouncing and trickling past Godzilla. And in the end, I was able to bust out this shot in less  than a day by combining all these different elements together. So I hope you can use these to

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_014.jpg

### Master Unreal 5 Filmmaking in 21 Days [18:15]
**Transcript:** level up your own cinematics and action scenes right after this video. And now it's your turn.  If you follow a long step by step, you can add gunfire and interactive effects into your own  cinematics and action scenes. But look, if you're new to Unreal or you've struggled learning in the  past, it doesn't have to take six months or a year to master Unreal. In fact, you can learn  everything you need to know in just 21 days when you join Unreal Fundamentals. We'll take you  from a complete beginner to an Unreal filmmaker by creating environments and films step by step.  I'll give you every cheat sheet and template I've ever created so you can use my own templates  on your own freelance and professional work. Get the shortcuts and start learning today for just  99 bucks over at Unreal for VFX.com slash Fundamentals. Subscribe to the channel for more  unreal and filmmaking videos just like this and I'll make sure to see you in the next video. Peace.

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_015.jpg


---

## Structured Notes

### Core Technique
Procedural Niagara gunfire system for cinematics: three layered emitters (muzzle flash, tracer bullet, impact spark) with inter-emitter collision events, light renders, Sequencer user parameters for on/off animation, and SimCache for deterministic re-renders.

### Summary
Hollywood VFX veteran Josh Toonen (Dungeons & Dragons, Across the Spider-Verse) walks through building a complete interactive gunfire system from scratch in Niagara. The system uses a Directional Burst template as the starting point, then builds three emitters: a muzzle flash sprite with an additive material and ~0.05s lifetime, a tracer bullet with velocity-aligned scaling and collision, and a spark impact spawned via collision event handlers. Interactive light renders attach to each emitter. Spawn rate is exposed as a User Parameter and animated in Sequencer via Niagara Component Track. SimCache plugin locks particle positions for identical re-renders. Final shot is composite-friendly: isolate each layer and combine in Nuke.

### Key Steps
1. Content Browser → RMB → New Niagara System → New System From Emitter → Directional Burst → name NS_Gunfire
2. **Muzzle Flash emitter:**
   - Delete default burst spawn module; add Spawn Rate (value=3); set Loop Behavior=Infinite
   - Delete Drag, Gravity, Forces, Velocity, Scale Sprite Size By Speed modules
   - Initialize Particle: Sprite Size=Uniform value=60; Lifetime=Direct Set value=0.05
   - Create material: muzzle flash image → Emissive Color; Blend Mode=Additive; add Multiply node named "brightness"
   - Sprite Render: assign new material
3. **Bullet emitter:**
   - Copy muzzle flash emitter, rename "bullet"; Lifetime=2s
   - Add Velocity (In Cone); Cone Angle=0; speed=1500 units
   - Add Scale Sprite Size By Speed (Y axis) for tracer stretch
   - Sprite Render: Alignment=Velocity Align
   - Particle Update: add Collision module; add Kill Particles → set Has Collided=true
   - Enable Persistent ID at emitter top; add Generate Collision Event
4. **Impact Spark emitter:**
   - New emitter from Directional Burst; Sprite Render Alignment=Velocity Align
   - Add Event Handler stage; Source=Collision Event; Spawn 20 particles; Execution Mode=Spawn Particles; receive Collision Event
   - Add Velocity (In Cone): change cone axis to -X (negative) to invert direction
   - Add Collision module; set Advanced aging rate after collision=2
5. **Light Renders:**
   - Muzzle flash: Add Light Render; Radius Scale=64; uncheck Inverse Square Falloff; Default Exponent=800; tint orange
   - Bullet: copy same Light Render; increase exponent (dimmer)
6. **Sequencer animation:**
   - Muzzle flash spawn rate → click Spawn Rate field down arrow → type "user" → create User Parameter; repeat for bullet emitter, assign same parameter
   - In Sequencer: select Niagara actor → Add Niagara Component Track → Add Spawn Rate sub-track → keyframe (3=fire, 0=stop)
7. **Consistent renders:**
   - Edit → Plugins → enable Niagara SimCache Plugin
   - Sequencer: Niagara component → Add Niagara Cache Track → press Record → bakes per-frame particle positions
8. **Layer isolation:** hide unused levels/geometry to isolate muzzle flash pass; composite in Nuke with lens flares, dirt, extra spotlights for art-directed light

### UE Systems / Blueprints / Settings
- **Niagara System**: Directional Burst template as base; three emitters chained via Event Handlers
- **Collision Event / Generate Collision Event**: inter-emitter communication for impact spawning
- **Persistent ID**: required on source emitter for collision events to work
- **Sprite Render**: Additive blend mode for muzzle flash overlay; Velocity Align for bullets/sparks
- **Light Render** (Niagara): Radius Scale, Default Exponent (non-inverse-square falloff), color tint
- **User Parameters**: expose Spawn Rate as Niagara user param; keyframe via Niagara Component Track in Sequencer
- **Kill Particles module**: condition on `Has Collided` to terminate bullets on impact
- **Scale Sprite Size By Speed** (Y axis): stretches bullet sprite into tracer shape proportional to velocity
- **Niagara SimCache Plugin**: deterministic per-frame particle baking for re-render consistency
- **Movie Render Queue**: render isolated layers; composite in Nuke

### Difficulty
Intermediate — requires Niagara fundamentals but clearly walked through from template

### UE Version
UE5

### Tags
[niagara, vfx, gunfire, muzzle-flash, particle-system, cinematics, collision, sequencer, compositing, filmmaking, simcache, intermediate]

---

## Related Entries
- cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma.md (action scenes, Chaos)
- cinematography-deepdive-for-beginners---camera-and-render-settings-tutorial---un.md (Movie Render Queue, compositing)
- beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in.md (Sequencer filmmaking techniques)
