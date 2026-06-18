---
title: Learning Unreal 5 in One Year (Progression + Lessons)
source: YouTube
url: https://www.youtube.com/watch?v=9rRiExTYrpE
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [cinematics, pipeline, animation, niagara, beginner]
extraction_status: complete
frames_dir: tutorials/frames/learning-unreal-5-in-one-year-progression-lessons/
frame_count: 16
---

# Learning Unreal 5 in One Year (Progression + Lessons)

**Source:** [YouTube](https://www.youtube.com/watch?v=9rRiExTYrpE)
**Author:** Josh Toonen
**Duration:** 26m1s | 16 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Learning Unreal is hard, like really hard.  It's the steepest learning curve I've had  learning any visual effects software yet.  Over the last year, I've been on a mission  to learn Unreal Engine to create films of my own.  And today I want to share the entire process with you.  What's up?  My name's Josh Tunin, and I'm a director and visual  effects supervisor.  And I've spent the last eight years  working on Hollywood visual effects.  But everything changed last year when Unreal 5 dropped.  On limited polygons, real-time global illumination,  in short, CG became real-time.  Around that time last year, I was hired at Pixamondo  to join their virtual production team,  and operate on the world's largest LED volume  event, Cooper, where I've gone avatar the last airbender.  So today, I'll be walking you through my journey  of learning Unreal Engine and teach you  the most important lessons I learned along the way.  And hopefully, leave a roadmap for myself  from one year ago to speed up the learning process.  The first project I ended up doing  is very traditional, like many others before me.  Sometimes the best way to start

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_000.jpg

### My First Project [1:15]
**Transcript:** is to take a bunch of quicksale assets,  some of these great free assets that Epic has supplied,  and just start throwing them into a scene  to really start understanding how all of the systems work  together.  And during these early projects, follow the fun.  Follow what is actually enjoyable to learn.  I was messing around with the fracturing tools,  a lot of the landscape tools, and just flying around,  getting comfortable with Nanite, and really trying  to push geometry detail, a really high-dense geometry  in the foreground.  At this stage, I think it's really important just  to focus on setting up a single camera,  focusing on making a nice composition,  and playing around without the lighting and geometry  systems.  Don't worry about animation, anything like that.  Just worry about creating a still scene with static objects.  And one fun thing I learned on this one too  was using Go-Bos.  You can see on the right side here, basically large dark shapes  that you can use to cover the sun and really art direct  some of your shadows.  I just made a very large plane with a noise texture on it,

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_001.jpg

### Drone Lightsaber Battle [2:15]
**Transcript:** and start easily breaking up the harsh sunlight.  And then I took this level and started  using it to learn the animation systems.  So this was the first shot that I assembled together,  and there's a lot of stuff going on,  so I'll start to break down what the layers are.  First one is Miximo Motion Capture Animations.  This is a model straight from Miximo.  Things like the drones and the lightsaber  were just very quickly assembled, taking assets off  of online stores like CG Trader and Turbo Squid,  and quickly assigning those, bring those into the scene,  doing basic textures, and really just trying to focus  on getting everything working together.  Another key piece of advice at this stage  is don't waste time modeling.  Find pre-existing assets.  There's enough to learn without tackling modeling  at the same time.  This was also a deep dive into the Niagara system  and trying to make these different chains of events  that work together, and I'll go into more detail  on that later.

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_002.jpg

### Lesson One [3:15]
**Transcript:** But lesson number one is you're learning a game engine,  not a render engine, or a visual effects engine.  You are learning a game engine first,  and really understanding that at a fundamental level  from the beginning is very, very useful.  You can't avoid learning the game engine side of Unreal.  If you ignore it, troubleshooting becomes insanely difficult  and frustrating, and to be honest,  when I first started on this project,  there were several times where I had to stop dead  of my tracks, and I didn't understand  how to even render some of these things.  This is the reason why the LearnAker is so steep,  and why it can feel really intimidating,  and any point in the chain of processes  that you're trying to understand,  from lighting, scene assembly, into animation,  and sequencer, and then rendering through movie render queue.  In between each of these steps, something can go wrong,  and when you're first starting, it will go wrong.  But Unreal is at its best when all of these systems  are interacting together, and have a great example  with the Niagara system that I set up in the last scene.  This is a fairly basic setup here,  but it kind of illustrates the power of Unre...

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_003.jpg

### Niagara Muzzle Tracers [4:20]
**Transcript:** versus some of the traditional VFX packages  where you really are hand-animating every single step.  So if I go to Game Mode, we can see this.  These are just two simple Niagara particle systems here  that I call muzzle tracers,  and this is a dynamic effect system  where there are a chain of events going on.  We have the muzzle flash spawning,  we have a bullet moving from this system.  We have a light trail following the tracers themselves.  And if we look a bit closer,  I also designed these bursts that will explode on impact,  and based on the angle of the impact,  will actually spawn the particle system  in the opposite direction so that we get the correct impact.  And as we move this, the base particle system here,  and we take this drone, and we move through the scene,  we can really quickly see that the entire system  will start to move with them.  And right here, I'll just take shift and drag along here,  and you can see that the particles and the impacts  and everything start to move with it.  I want to take this one step further  in the finish shot itself.  So if we go down here to shot 20,  and I view the camera cut here, I'll just press play.  We can see that all of th...

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_004.jpg

### International Space Station [6:45]
**Transcript:** So the next project I did was taking  this international space station model  and trying to design a simple world around it  and really trying to understand  Lumen and the lighting system at a very fundamental level.  These are some of the shots that came out of it.  And this was taking it from a full round trip,  from Unreal, from movie render queue,  and then rendering it in Nuke.  Again, very basic animations here,  but really just focusing on every step of the chain  working together before going to complex.  Again, keep in mind that I wasn't able  to render out the previous shot  because I didn't understand how the simulation  part of Unreal was working.  So this was a great practice just to focus  on camera animation specifically  and rendering it out and doing a full round trip into Nuke  in aces, in linear color, and getting  those crisp highlights, lens flares, things like that,  all interacting and working together  so that ideally you could render directly out of Unreal  into a Nuke template that does all of these interesting lens

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_005.jpg

### Niagara + Flipbooks [7:50]
**Transcript:** effects, all in one step.  This next project was a very simple,  pair-down idea just to really focus on art direction  and Niagara systems.  On this one specifically, you can see some of these emitters  for the different smoke, this little pot emitter here.  I found a really interesting clip from Gladiator,  the Ridley Scott movie, and I wanted to recreate something  that had a bit more depth and just to match something  that was completely photoreal and try to understand  what that would take inside of Unreal,  basically taking different images of smoke  that are chosen at random, that will make up  and break up the smoke texture that's being emitted,  and then finding interesting ways with curl noise  to break up the look of the smoke here.  I also was playing around with fire and sub-UV flipbooks,  so these are flipbooks that are in the material themselves,  basically 64 frames baked into a 2K texture  that will loop forever so that you can place these elements  in your scene and they will just continue to animate  and you set it and forget it, and now you just worry  about the cameras and the characters in your scene after that.  And if you haven't noticed, there are so many  d...

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_006.jpg

### Lesson Two [9:08]
**Transcript:** Each menu in Unreal is basically its own plug in,  its own separate program within Unreal,  the material graph is its own editor,  the static mesh editor is its own editor.  This has completely different settings than our materials do,  and you have to learn the entire pipeline  for each of these editors one at a time.  There are different careers that spend their entire time  in just one of these editors within Unreal.  So as a VFX artist and as a generalist trying to use Unreal  for VFX, it's really important to have  a fundamental understanding of each of these.  And I've laid out a very simple learning path  for what you should learn first.  I would definitely start with the material graph.  Very quickly you can bring in quicks and assets,  import those directly into your scene,  and start playing with the material instances  that come with quicks and mega scan assets automatically,  as well as understanding the master material editor.  The next step is lighting.  This can get over complicated very quickly.  The main building blocks of a good scene,  a good exterior lighting scene,  is a directional light, which is your sun,  a sky atmosphere, and your sky light.  By each of th...

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_007.jpg

### At-home Virtual Production [11:05]
**Transcript:** So the next project was the first time  where I was putting all of these lessons  that I put together into one piece  of previous animation, characters, crowd,  and this time, even using a virtual camera.  This was taking the virtual production techniques  that have been used on films like James Cameron's Avatar,  and Ready Player One, and starting to put all of the pieces  together to really tell a story,  figuring out how to take these clips  in different small sequences,  and bring them into a timeline in order to tell a story.  Eventually, I will release this,  but this was a huge learning opportunity  on how to take all of these different pieces of animation,  go through retargeting and IK retargeting,  which is new in Unreal 5,  and putting all of this together in a timeline,  and funny enough, things like crowds actually become  much easier when doing them inside of Unreal,  especially when you're reusing a lot of the same character rigs.  It adds a lot of simplicity to what would otherwise  be a complex issue.  This is another topic.  I will do a full on-depth video on how to take  Mixamo, motion capture animations,  and apply them to different character rigs,  whether they...

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_008.jpg

### Sample Projects You Should Download [13:47]
**Transcript:** Epic Games has released so many triple A quality projects  for free.  You may have heard of the Matrix demo and some other ones,  but I made a list of some of my favorites  that I found really help speed up my workflow  and you can use to speed up yours  and understand how these complex systems work together.  The first one was the Miracat demo  where you get to see how wetta effects  is thinking about constructing a cinematic out of Unreal 4.  In this case, you may have to download Unreal 4  just to open the project, but it is absolutely worth it.  And I actually got started using Unreal 4  before Unreal 5 had launched.  The second one is the Medieval project.  This was put out by the Quixel team,  and they really brought photorealism and art direction,  like something you'd see on the PlayStation 5  or any other modern title.  They really pushed both the quality of the assets  and the lighting, but also optimization and performance,  which was really helpful when working  on the virtual production LED volume stage.  The third project is Slay, the animation sample.  This really helped me understand how you can nest  sub sequences inside of sequencer  to make complex shot work quit...

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_009.jpg

### Getting Started with Vehicles [16:00]
**Transcript:** This is another example of the vehicle starter content  example that I started bringing in to understand  how I could take gameplay elements  and incorporate them into scenes of my own.  Here I was able to drive around a car  and start modifying that blueprint.  And here, funny enough, I'm just pressing the M key  to flip the car.  So it would add a physics force to start flipping the car.  And very quickly, you can see how you can take  the small events and different simple blueprints  and start chaining them together  to do way more complex animations.  This brought me into my next film project,  which I'm calling Heatseeker.  I was starting to get obsessed with this idea

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_010.jpg

### Heatseeker [16:40]
**Transcript:** of this windsurfing racing league,  almost a Saturday morning cartoon  that you could create as a cinematic and unreal.  So I took what I learned from the car configurator  and started to take these really simple models  and start to create a controller based off of them  that would dynamically interact based on how you're driving it.  From there, I tried to see what it would take  to bring a character and parent them  and parent different IK rigs to different parts  of the windsurfing controller.  Here, I literally took the mixamo girl,  the character right off the home screen of mixamo  just as a way to assemble this as fast as I could  and suss out the concepts.  And very quickly, was able to have this drifting racer  that dynamically moved and shifted based on how the physics  of the vehicle was interacting with the world.  Where you press a key and she'll bounce  with a little extra weight just to add impact to the driving.  I added another control to the sail  so it would shake with intensity the faster the vehicle was moving.  From here, I started building out this little world.  To be honest, again, it does not always work.  Some things just break and a lot of it is hard to...

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_011.jpg

### Horror ICVFX [19:30]
**Transcript:** I had been working on some horror projects on the side  and trying to figure out interesting ways  to play with the depth that you could have inside of a scene.  And I wanted to see what animation would look like  on an LED volume.  So this test was really to see what this animation looks like  when shot through a camera,  what sort of lighting and interaction could we cast  onto the actors in the scene?  And how could we make this mind bending twisting,  turning tunnel and make it as cool as possible?  And an interesting test here was seeing what it would take  to have a virtual foreground.  So even though everything is shot with an LED screen  behind Nick here, we were cheating some of the depth  so you could actually have the environment look like  it's coming in the foreground and defocused

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_012.jpg

### Lesson Four [20:15]
**Transcript:** like it would look like through a camera lens.  All right, lesson four, documentation.  But I think Unreal's documentation is notorious  for being difficult to follow.  This has probably happened to you  where you think you know what you need to find,  but you just simply can't find what you're looking for.  Now that Unreal is in 5.1,  and I'm sure we'll update more throughout the year,  you're kind of backtracking through all these different  documentation and also different forum posts  that may or may not apply to the conversion of Unreal.  So I want to make a simple slide here.  It's simple, but very, very effective, I believe,  of how to actually get the most use out of the documentation  that Epic has given for Unreal 5 and beyond.  And that is two very simple things.  One, are you trying to learn a workflow  or are you trying to learn a feature or a plugin?  The first thing you should always try to understand  is the workflow of how do these systems work together?  And once you know how these things work together,  it's much easier to go into the feature or the plugin itself  where you can use F11 and it'll just pop up  the documentation that you need for the editor  that is...

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_013.jpg

### Photoreal Renders + Lesson 5 [22:35]
**Transcript:** And now for the rest of the year,  I wanted to take a closer look at what it takes  to achieve photorealism out of these game-edgin renders  and really work on lighting and attempting  many different lighting scenarios in the same scene.  So the last lesson here is to start and finish your small projects.  This is absolutely the best way to learn Unreal  is not spending a bunch of time on one really long project  when you're first learning this software in particular,  especially when you look through the game dev side  and the tutorials that will bring you down  that path of Unreal.  It is very, very clear that the first month,  two months, even three months of work  that you're doing in this,  it really is just to learn how all of these things work together.  There are just so many small things that you'll end up  discovering when you're playing that is just much better  to make 30 small projects one a day for an entire month  than one really long big project over 30 days.  You'll get much more out of working on these smaller projects.  It is not enough to just watch tutorials.  You have to do it for yourself.  You have to think of unique problems  and figure out solutions and no...

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_014.jpg

### Mr. Freeze Project [24:05]
**Transcript:** Thank you for sticking around this far.  To wrap this up, I want to show you test renders  that I was doing for a Mr. Freeze project  in this Batman Beyond World.  Testing again, the full pipeline from rendering  all the way into Nuke and giving it that final polish pass  that I'm used to in the Visual Effects world.  And by this time, because I've kind of gone  through the whole character pipeline  and done all these steps so many times,  it was just a much faster process to start from scratch,  take a model, rig it, do IK retargeting  with Mix-A-Mount animations, stick it in a scene,  put it in sequencer, and you can quickly start to see  how what was once a very complex process to set up,  now that I've gone through the ringer  and done it a few times, it becomes much faster,  and you just know exactly how these systems work together.  And do not get me wrong, there are always problems,  it will never stop happening.  That is the painful part, but also the fun and rewarding aspect  of Unreal is beating your head against the wall  until you finally find the right answer.  In this case, it usually is just a simple checkbox  hidden somewhere deep inside Unreal,  but I hope this was...

**Frame:** tutorials\frames\learning-unreal-5-in-one-year-progression-lessons\frame_015.jpg


---

## Structured Notes

### Core Technique
A one-year UE5 learning progression retrospective covering 5 key lessons, including a Niagara event chain muzzle-tracer system, flipbook sub-UV fire textures, and IK retargeting as the three core technical milestones.

### Summary
Josh Toonen reflects on one year of learning Unreal Engine 5 for filmmaking, distilling the experience into 5 lessons that accelerate the learning curve. Viewers learn his recommended approach: start with the game engine fundamentals before filmmaking, master one editor at a time (starting with Materials), use virtual camera and previs, rely on F1/F11 for context-sensitive documentation, and finish small projects. Three technical milestones are showcased: a complete Niagara muzzle-flash-to-bullet-impact event chain, flipbook sub-UV fire textures (64 frames in a 2K atlas), and IK retargeting for cross-character animation transfer.

### Key Steps
1. **Lesson 1 — Learn the game engine first**: UE5 is a game engine; spend time understanding actors, components, blueprints, and the editor before focusing on filmmaking tools.
2. **Lesson 2 — One editor at a time**: Each UE5 editor (Material Editor, Animation Editor, Niagara Editor, Sequencer) is its own sub-program; start with Materials because it underlies everything.
3. **Lesson 3 — Virtual camera and previs**: Use UE5's virtual camera system to previs shots in 3D before committing to final animation; iterates quickly.
4. **Lesson 4 — F11 for documentation**: Press F11 on any node or property for context-sensitive UE documentation (or search UE docs directly).
5. **Lesson 5 — Finish small projects**: Complete small films before moving to bigger ones; every finished project teaches pipeline lessons no tutorial can.
6. **Niagara event chain**: Muzzle flash Niagara emitter → generates collision event → bullet tracer emitter reads event → on bullet collision → triggers impact burst emitter; full chain with persistent IDs.
7. **Flipbook sub-UV fire**: 64 fire frames arranged in a 2K texture atlas (8×8 grid); Niagara Sub-Image UV module picks frames in sequence for animated fire; lightweight alternative to video texture.
8. **IK Retargeting**: Use IK Rig + IK Retargeter to transfer any animation from one skeleton to any other without Mixamo; supports complex rigs.

### UE Systems / Blueprints / Settings
- **Niagara event chain**: Emitter 1 (muzzle flash) → Generate Collision Event + Persistent ID; Emitter 2 (bullet) reads Collision Event → fire on event; Emitter 3 (impact burst) reads bullet Collision Event; all three emitters in one Niagara System
- **Flipbook sub-UV**: 64 frames, 2K texture atlas (8×8 grid); Niagara Sub-Image UV module → Num Tiles X=8, Num Tiles Y=8; animation mode = Sequential for fire, Random for smoke
- **IK Retargeter**: Window → IK Retargeting → IK Rig (source) + IK Rig (target) → map bone chains → Export Retargeted Animation

### Difficulty
Beginner

### UE Version
UE 5.x

### Tags
cinematics, pipeline, animation, niagara, beginner

---

## Related Entries
- [[create-muzzle-flash-gun-fx-for-unreal-5-cinematics]] — detailed Niagara gunfire system building toward the event chain shown here
- [[this-free-plugin-changes-filmmaking-forever-unreal-5]] — OneClick Control Rig and Mixamo pipeline covered in early learning
- [[motion-capture-isnt-just-for-hollywood-any-more]] — IK Retargeting in production use
