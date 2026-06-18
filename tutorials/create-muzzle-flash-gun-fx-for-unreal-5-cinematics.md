---
title: Create MUZZLE FLASH Gun FX for Unreal 5 Cinematics
source: YouTube
url: https://www.youtube.com/watch?v=wFhZxRJZN8E
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [niagara, vfx, particles, sequencer, cinematics, intermediate]
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
**Transcript:** where we can set the lifetime and particle size. So let's change the sprite size over to a uniform  value and let's make that a value of 60 and now let's reduce our lifetime. So let's change this  to direct set and give an exact lifetime and we want to set this to something really, really short  in a movie of muzzle flash is only visible for one single frame. So we want to recreate that  in our own cinematics. So instead of having our lifetime set to one second in that particle  disappearing after one entire second, let's set it to 0.05 and this will make that particle flash  on and off. And there we go. Now it's crude but we do have our first muzzle flash. All we have to  do is swap out this sprite so that it's a picture of a real muzzle flash instead of this circle.  So to change that out, let's go to the bottom at our render tab and select sprite render and we  need to create a new material to replace our sprite. So I've already imported in a mature,  but let's make a simple material for this sprite. I'm going to create a new material called  underscore muzzle flash. Now let's drag in our muzzle flash image. Let's plug that into the  emissive color and then to get rid of this bl...

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_005.jpg

### Bullets and tracer fire [5:45]
**Transcript:** So let's create a new bullet. I'm going to select our directional burst here. Let's actually rename it.  So I'm just going to press on the F2 key and call this our muzzle flash. And now we can  right click here, copy and paste. And now let's call this bullet. The only difference is under  particle spawn will need to add in velocity. So let's type in velocity. And with Niagara,  the order really matters here. But they do a great job of telling you when something's broken. So  you can just press on these fix issue buttons to fix any problems with the order there. And now in  our add velocity menu, let's change this from linear to in cone. Now a big problem here though is  our lifetime is super short. So we need to lengthen that so that bullet can cast off and travel  through space. So let's go to initialize particle, which has all of our default settings.  And let's change that lifetime over to a value of two seconds. Now obviously our velocity is super  slow. So we'll need to add a lot of velocity here. I'm going to add about 1500 units. And I'm  going to change the cone angle down to zero so that there's no randomness in the direction of our  bullets. Now obviously the particle is ...

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_006.jpg

### Add collisions in Niagara [7:29]
**Transcript:** you can see that the bullets are literally bouncing off that wall and traveling backwards. And if  we moved our rifle around here, you can see that it dynamically collides with any part of our  environment. Now this is cool, I guess, but we need to make sure that that bullet impacts that wall  and then creates a burst of spark launching off in the opposite direction. So let's handle that  next. So first off, let's make sure we kill that particle after it bounces off the wall. To do  that under particle update, let's add in a new module called kill particles. And we want to set this  kill particles to true after our particle has collided. So we can do this by pressing on the down  arrow and literally just type in has collided. And this makes it so every time a bullet collides,  that it dies on impact. But now we need to spawn another particle emitter for our spark impact.  So let's right click in our Niagara graph and create a new emitter. And let's start from one of

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_007.jpg

### Creating impact sparks [8:27]
**Transcript:** their presets. And this time, let's pick a directional burst. So we're starting from the same thing,  except remember, it's spawning from the original location, not from the impact of our collided  particle. So to fix this directional burst, let's just go to the sprite render and change this  alignment over to velocity aligned. And that's going to give us a much better looking impact.  But how can we spawn this as soon as a particle collides? Well, to do this, we need to use something  called an event handler. All this does is let the Niagara system know every time a particle collides  where it happened. So to set this up, let's open up that Niagara system. So in our bullet that's  firing through our environment under particle update, let's press on the plus button and type in  generate collision event. And in order for this to work, you just need to go to the top of your  emitter and make sure to enable persistent ID and press compile. Now this system will know  every time there's a collision. But we need to make sure to transfer that information and spawn  particles from the impact. So to do that in our new spark burst setup, let's press on this small  stage button and add in our...

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_008.jpg

### Interactive Light with Niagara [11:03]
**Transcript:** of our environment. But it's really easy to add in under our muzzle flash system. Let's get this  setup first and under our render tab, let's add in a new light render. Now there are some weird  particular settings that you need to use here. They're not so photorealistic as the rest of the  lighting system in Unreal, but it can still be really effective. What I normally do is I'll change  this radius scale to something big like 64. And then in this case, I'm not going to use the  inverse square falloff. This is going to cast a ton of light into the scene, which is not exactly  what we want here. So let's change our default exponent to something like 800. So it just appears  around the gun itself. Now we can also change the color by adding a little bit of red  into this light. So it starts to cast bright light into our scene. But you're probably wondering,  can we add this to the bullet flying through the scene? And the answer is yes. You can literally  copy this light render and paste it in our bullet system. And now we have a light attached to each  bullet. Now we're going to make these a bit darker because I want those muzzle flashes to be the  brightest thing in our scene. So I'...

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_009.jpg

### How to Animate our Gunfire On/Off [12:30]
**Transcript:** and decide when to fire and when not to? Well, let's talk about that next. If you want to learn how I'm  a big budget action sequences from home, it's all using Unreal Engine 5. And this week, I'm going  to share all my secrets in the live Godzilla masterclass. Sign up today at unreal for VFX.com slash  Godzilla. And I'll show you how to recreate all the on set filmmaking techniques that go into  your favorite plotbuster movies, even if you're not an animator yourself. You don't want to miss out  so make sure to register today at unreal for VFX.com slash Godzilla. Now let's add this intense gunfire  into a real action scene shooting down Godzilla. So let's add in some muzzle flashes onto our helicopters  in this shot. To do that, I'm just going to click and drag our gunfire into our scene. And you can  see right away it'll start shooting some bullets at Godzilla. Now if we want to animate anything,  we have to add it into sequencer. So let's add our Niagara system into sequencer. And let's create

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_010.jpg

### Using Niagara in Sequencer [13:27]
**Transcript:** a new attached track and attach it to our helicopter. And now you can see we already have our particle  system shooting down Godzilla. But how do we change the timing of our gunfire? What if we wanted  to start it intense and stop halfway through? Well, if you didn't know already, we can build some  custom controls and menus into any Niagara system. Let's double click on our gunfire system  and create something known as a user parameter. Just like in materials, we can create customizable  parameters that we can change on the fly and even add animation and keyframes to. Let's start  animating our spawn rate first. So to do that, I'm going to click on the spawn rate of our muzzle  flash and click on this down arrow and you type in user, which will let us create a new user parameter.  Now we need the spawn rate of our muzzle flash and our bullets to be exactly the same. We can have  some faster than others. So let's go to the spawn rate of our bullets and change our spawn rate  here over to a user parameter. But now we can select the one we just created called spawn rate.  Now these two are linked together. And when I jump back into our viewport, if I look on the right  side, I can se...

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_011.jpg

### How to get consistent renders with Niagara and Sequencer [15:25]
**Transcript:** especially with Niagara. But if you follow this, you'll get the same results every single time.  All you need to do is go to edit plugins and enable the Niagara SimCash plugin.  If you enable this inside of sequencer, we can click on that Niagara component and add a Niagara  Cash Track. What this will do is give us a little record icon here. And if we press on the record  button, it'll go through our sequence and create an exact position for every single particle in our  shot. And this will make it identical if we ever go back to re-render this later. Now we could  render this out as is and just render this out of movie render queue. But I like to isolate each

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_012.jpg

### Rendering with Movie Render Queue [16:05]
**Transcript:** layer of my scene and composite them together. Now most people over complicate isolating render layers  inside of Unreal. Basically, all we need to do is just disable or hide everything that we don't need.  So hide any extra levels or geometry that is not being used. Once your viewport matches what you  want with everything turned off, then you can go to render. Once we have a render where our  muzzle flashes and impacts are isolated, then we can start combining it together. But how do you  go from particle system to Hollywood level visual effects? Well, that's where the next most important

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_013.jpg

### Compositing your Gunfire in Nuke [16:40]
**Transcript:** step comes in and that's compositing. Compositing is just Photoshop for video. But for us, it's where we're  going to add in lens flares, lens dirt, and anything that makes it look better. By adding this layer  on top of our original render, I want to share a couple extra techniques I used to take these shots  even further. I also rendered out a couple of extra spotlights that mimic the same position and  lighting of our muzzle flash. By combining this custom light with the other muzzle flashes,  I was able to art direct that lighting while still getting custom dynamic particle effects  from the system without animating anything myself. And now our scene feels more intense.  And you can make these look even better by having these muzzle flashes interact with smoke and  rain. You'll notice in this shot where we're firing from the cockpit of a helicopter,  that if I pause on any dynamic frame here, that the muzzle flash is lighting up all the surrounding  rain. Now how do we do that? Well, first it was by laying out real stock footage of rain that I could  place in my 3d scene. But then it's by isolating that muzzle flash layer, blurring it out,  and multiplying it against that rain ...

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_014.jpg

### Master Unreal 5 Filmmaking in 21 Days [18:15]
**Transcript:** level up your own cinematics and action scenes right after this video. And now it's your turn.  If you follow a long step by step, you can add gunfire and interactive effects into your own  cinematics and action scenes. But look, if you're new to Unreal or you've struggled learning in the  past, it doesn't have to take six months or a year to master Unreal. In fact, you can learn  everything you need to know in just 21 days when you join Unreal Fundamentals. We'll take you  from a complete beginner to an Unreal filmmaker by creating environments and films step by step.  I'll give you every cheat sheet and template I've ever created so you can use my own templates  on your own freelance and professional work. Get the shortcuts and start learning today for just  99 bucks over at Unreal for VFX.com slash Fundamentals. Subscribe to the channel for more  unreal and filmmaking videos just like this and I'll make sure to see you in the next video. Peace.

**Frame:** tutorials\frames\create-muzzle-flash-gun-fx-for-unreal-5-cinematics\frame_015.jpg


---

## Structured Notes

### Core Technique
Building a complete Niagara gunfire FX system from scratch in UE5: muzzle flash sprite, bullet tracer with collision, spark directional burst, light render, and Niagara user parameters — with SimCache for frame-perfect cinematic renders.

### Summary
Josh Toonen walks through building a production-ready Niagara gunfire system entirely from first principles in UE5. Viewers learn to create the muzzle flash (directional burst with emissive sprite material), bullet tracer (velocity cone emitter with collision events), spark burst (event handler responding to bullet impact), and dynamic light render (radius/exponent scale). Niagara user parameters expose spawn rate and intensity for per-shot customization, and the Niagara SimCache plugin bakes the stochastic simulation for consistent multi-sample MRQ renders.

### Key Steps
1. Create a new Niagara System from the Directional Burst template; rename to NS_Gunfire.
2. Set Spawn Rate module value = 3; Loop Behavior = Infinite so it fires as long as triggered.
3. Initialize Particle module: Lifetime = 0.05 seconds; Sprite Size = 60 (uniform) for a compact muzzle flash.
4. Create a muzzle flash sprite material: Blend Mode = Masked; Emissive Color input (bright orange/white); Opacity Mask input connected to a radial gradient texture; set Two-Sided = true.
5. Add a second emitter for the bullet tracer: set Velocity in Cone module with Cone Angle = 0 (straight forward), Lifetime = 2, Speed = 1500 units/frame for supersonic feel.
6. Add Kill Particles module: condition = Has Collided = true so tracers disappear on impact.
7. Add an Event Handler: Generate Collision Event (from bullet emitter) + Persistent ID enabled; create a third spark emitter that reads this collision event to spawn the impact burst.
8. Add a Light Renderer module in the muzzle flash emitter: Radius Scale = 64, Light Exponent = 800 for a brief intense flash.
9. Create Niagara User Parameters (float variables) for Spawn Rate and other exposed values so instances can be customized per character.
10. Install the Niagara SimCache plugin (Edit → Plugins → Niagara SimCache); bake the simulation to SimCache before MRQ render so every temporal sample uses identical particle positions.

### UE Systems / Blueprints / Settings
- **Niagara System**: Directional Burst template → renamed NS_Gunfire; Spawn Rate = 3; Loop Behavior = Infinite
- **Initialize Particle**: Lifetime = 0.05; Sprite Size = 60 (uniform)
- **Muzzle flash material**: Blend Mode = Masked; Emissive + Opacity Mask; Two-Sided = true
- **Bullet emitter**: Velocity in Cone; Cone Angle = 0; Lifetime = 2; Speed = 1500
- **Kill Particles module**: Has Collided condition = true
- **Event Handler**: Generate Collision Event; Persistent ID = enabled; triggers spark burst emitter
- **Spark emitter**: Velocity Aligned Sprite (sprites align to travel direction)
- **Light Renderer**: Radius Scale = 64; Light Exponent = 800
- **Niagara User Parameters**: Float variables in User Parameters section; linked to Spawn Rate, Lifetime, etc. via drag-connect
- **Niagara SimCache plugin**: Edit → Plugins → "Niagara SimCache"; bake before MRQ for deterministic multi-sample renders

### Difficulty
Intermediate

### UE Version
UE 5.x

### Tags
niagara, vfx, particles, sequencer, cinematics, intermediate

---

## Related Entries
- [[ragdoll-physics-are-insanely-easy-in-unreal-5]] — Niagara system lifecycle track in Sequencer for explosion timing
- [[learning-unreal-5-in-one-year-progression-lessons]] — Niagara event chain muzzle tracer system as learning milestone
- [[how-i-made-a-godzilla-cinematic-in-unreal-engine-5]] — rain Niagara particles and lighting in a full production context
