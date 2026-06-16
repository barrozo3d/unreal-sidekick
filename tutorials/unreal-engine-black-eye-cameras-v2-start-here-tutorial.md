---
title: Unreal Engine Black Eye Cameras v2: START HERE Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=vs6yjL-l_FQ
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v2
ue_version: "UE 5.3+"
tags: [blackeye-v2, camera, gameplay, cinematics, blueprints, sequencer, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-v2-start-here-tutorial/
frame_count: 24
---

# Unreal Engine Black Eye Cameras v2: START HERE Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=vs6yjL-l_FQ)
**Author:** Black Eye Technologies
**Duration:** 43m5s | 24 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Thanks for your interest in Black Eyed 2. We've been working really hard on this second  version. And why are we doing it? Because cameras are important. We've watched so much  TV, so many movies, that we have a really deep, subconscious understanding of how cameras  move and what they do in real life. And it's important to get that stiff right. Black Eyed  helps you emulate those real life camera behaviors. You'll bring a lot of realism and believability  to your camera work. And our new gameplay system for version 2, Weezing is going to transform  how people work with gameplay cameras. Let's get into the gameplay cameras because that's

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_000.jpg

### Gameplay System [0:46]
**Transcript:** a really big part of Black Eyed 2. We see this world where if you want to push in the  camera for a tunnel or look at something as you walk by, do camera cuts, or frame it over  a bit to one side because there's a boss battle. We see a world where you're tuning the  cameras while you're playing. That's this button, save and play. So if you run to a bridge,  you have it go to a camera that's higher and you tune the shot. Let's go higher. Let's  change the composition. The game's running. You go back and forth and you like, okay, let's  try that transition. Is that smooth? Does the camera go up high enough? Does it go fast  enough? And you're creating this stuff while it's happening. Okay, let's get you set up.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_001.jpg

### Plugin Install [1:30]
**Transcript:** Install. Release Report. Go to your Fab page. If you've bought us, we're there. Go to Fab  to buy Black Eyed, of course. And then you can add it to your project. And then when you're  in the project, go to plugins, you're going to have to turn it on. You'll have to restart.  And then we strongly recommend going to our demo level. Fire that up. That's all this  stuff and it shows you how to do a ton of gameplay things. So here's some examples in the  demo. This is an aim where we blend to looking at a certain world heading. So this is so

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_002.jpg

### Aim [1:57]
**Transcript:** easy to set up. We put a trigger volume. We give it a tag called aim. We create a camera.  A new one. It's often a copy of the gameplay camera. Set that to be on aim. And this camera  has got the recentering to point to a world interaction. So you blend to this camera and  it's looking at this one direction. You can pick the heading and you can pick the pitch.  And in this example, we've given the user the ability to have orbit control, but it  springs back pretty fast. You have a full control over that. It can be full orbit, no orbit  or this sort of dampened orbit. And then because I've got saving play turned on, let's  just tune this. Like a stringing a little bit. Let's change the pitch a little bit.  Okay, save and plays on. We're good. We go back out. Okay, let's run around. How does this feel  coming into it now? Okay, that's cool. A little low. Let's try it from the side. And instead of  typing a number and hitting compile and hoping it works, your iteration loop is insanely fast.  Because it has to be. So let's forget goes. We're going to change the lens. We're going to go  a little more telephoto. Let's see what that looks like. We come in. Blinder the telephoto lens.  We...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_003.jpg

### Tight Spaces [3:56]
**Transcript:** your over camera because of a world thing. Here's how to do it. Duplicate your gameplay camera.  Call it tight space. Create a trigger volume. Add a tight space tag. Or whatever you want to call it, of  course. Put that tag on your camera. Now we're going to use a default blend to go to that. We'll  talk more about blends in a bit and make this camera have a smaller orbit. You're done. It's that fast.  Boom. You want your camera to be higher, lower. Look to the left. Different input speed,  whatever. Trigger volume tag. And you go just like tweaking this a little bit. Let's just make it go a little  bit higher. Notice too, the collision will still look at the bone when you collide. So you're not  just like looking at the center of the character. You can control where the camera looks on the collision.  In a note, so fast to set up world relative camera behaviors. Look at that. And we're back to  gameplay. Easy. The interesting cube demo. This uses something called the Black Eyed Cross Camera.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_004.jpg

### Interesting Cube [5:10]
**Transcript:** And what it does is the cross camera can look at and follow two different things. And it gives you  a control over the heading and the height between those two different things.  The interesting cube demo here uses a direct camera reference. So you can use tags or you can  have a trigger volume like directly call a camera by putting it in the camera reference option.  Because we've got the auto activate on the player and I usually suggest keeping that as your subject  one. We're looking at the player and we're looking at the cube.  And just this can be another player. This could be anything in the world.  And then we've got a dynamic FOV on there, which is just seeing  frame these two things. Do some dynamic zooming. You can see the little white box. Look at that.  Now we're framing those two things. And because we've got save and play turned on,  we can tune this while we're going. So this is the follow distance. And because we get dynamic zoom,  it's effectively doing a Zolly. All there is. I'm pick the heading, pick the distance,  pick your height. And this is a camera, the cross camera is relative to the two different things.  Super powerful. Really good for dialogue.  Now you ...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_005.jpg

### Black Eye Demo Scene [7:33]
**Transcript:** It's under engine plugins. Black Eye, demos, fire it up. Look at all this stuff.  We've tried to make one of everything in here. And if you're not seeing this, remember you  got to turn on the hours. It turn on the plugin content. And that shows you all the content.  Lots of fun stuff to play with here. Okay, let's get into the camera manager.  This is going to control how all the cameras work together.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_006.jpg

### Camera Manager Setup [7:59]
**Transcript:** So let's make a third person one of the demos. Thank you for making this epic. Here it is.  We're going to drop in the orbit camera.  And we're going to set it to auto activate on the player and to look at to follow them.  And just a little sidebar check out the panel. I'm going to talk about this more. And  utilities preview selected cameras. Turn that off. Okay, so now the orbit is in there.  You're going to have to set the look to be whatever the projects look is.  In our demo scene, we use our look file. But because this project set up with this look,  you need to add this controller look profile. So I'm going to drop that in. That's just what's  consistent with this project. Save because save. Now play boom. There's our orbit camera.  And you can see there's no camera manager here. So I'm going to start a new clean project here.  Let's go back to the start clean project. Open the blackout window. Go to the manage tab.  And we can create. I'm doing it for the entire project, but you can do it for the level too.  I'm going to go back and create that camera. Just drop an orbit in project. And you know, turn off that  preview again. Set it to be auto activate and look at the playe...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_007.jpg

### Gameplay Camera Setups [9:59]
**Transcript:** And put it here. Make it big.  And we're going to give it a tag. And we're going to call this. We're going to create a tag.  I'm putting it all with its prefix. So it goes in the subfolder. But you can obviously organize  this however you want. We're going to call it high. We're going to turn that on for the trigger volume.  I'm going to duplicate the gameplay camera. And I'm going to call it high.  And then we're going to turn off the auto-activate for the player because we don't want this camera to be first.  We want the default camera to be first. We want this one to go when we trigger it on the high.  Then let's go to this camera. We'll let's make a huge radius. Let's move it up high.  Follow up high. And see the level. And hit play. How much this we run into the trigger volume.  We use the default blend to blend to the high camera.  Now, when we blend back, I go fast at what's. Now if I had that little save and play turned on,

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_008.jpg

### Save in Play [11:15]
**Transcript:** which I'm doing right now, we can hit play, run into this trigger volume, and then  turn the camera to be what it wants. I don't want it that high. I want it higher.  So select shot. What am I doing? Here we go. Orbit radius. Let's make it. I know. We're just,  I'm going, we're doing whatever. We're making this huge.  Let's feel that out. Everything still works. Collisions to there. And then we blend back down.  We want to create this world for you where it's super fast to create sophisticated camera  behaviors based on world locations, animations, whatever. So how do all the cameras know how to

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_009.jpg

### Blend Lists [12:07]
**Transcript:** blend and cut together? Well, that's with the blend list. So let's go to the demo scene because  it has a whole bunch already set up. If you go to the black eye panel and go to the manage tab,  it shows the project's blend list and you can hit the button and it shows them. Okay, let's go  through this default. If no blend is defined, this is what it does. How long? The whole time,  the blend type in the exponent. And the whole time is just like a buffer.  It needs an event needs to be on a certain amount, that amount of time before it triggers.  And then here's all your custom blends. So if I want to go from camera A to camera B,  it's this long. If I want to go from camera B back to camera A, you can do it differently.  You can define all of your camera to camera blends here. And then we've got wild cards,  like the security camera. No matter what, we want to cut. So anything from this camera,  whatever, anything to this camera, whatever. It's not easy. Very powerful.  Okay, let's get into the orbit camera. The orbit camera is a lot, a lot in here.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_010.jpg

### Black Eye Orbit [13:13]
**Transcript:** So if you create an orbit camera and you attach it to a character, you can see what it does.  There's the orbit rings. You can see it move. We recommend attaching it to the root bone because  it tends to be the most stable. But practically, you're going to have a spawn character.  So in our demo scene, we've got a welcome camera, which is the one that activates.  And then as soon as you leave this trigger volume, we go to the default camera.  And it's set up to not auto-activate, just it activates on that trigger.  So we're in the welcome camera right now. You can see up here welcome.  And then the second you leave this little area, blend to default.  Then you can see as you go to different things where the camera managers  showing the blend between all the different cameras.  So input speed controls are here. We expose them because there's a lot of mojo. You like to tune the  stuff. Slow cameras, fast cameras. That's where you control the input speed.  The auto-recentering means if it's off, you orbit. It'll stay there. If you turn it on,  after the given time, based on the speed, it's going to return the camera to whatever your  pitch and heading centers are. You can have it be, ...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_011.jpg

### Orbit Collision [19:36]
**Transcript:** So that orbit push in will be kind of wherever you want. I've got it at the neck here. But you  could have this be, you know, whatever you want. And right here, we're doing the recenter time.  This is way too slow. So this is like how quickly the camera comes back. It's almost like a rebound  setting on a shock. So you push in and then come straight back. You probably want this fast,  but that's what that control is. And then the probe size, this is the sphere around the camera  that's doing the collisions. So 30 is huge, bigger than the camera. But if you set this really small,  you'll see that you can even kind of have the camera clad through the wall a little bit. Like,  this is too small. You can like see, you know, behind the wall. So let's just crank this up a little  bit. And this is the size of this sphere around the camera that's doing the collisions.  And look at this just to compare the UE spring arm. You know, it's, it's colliding. It's looking  down the spring arm. But with our collision system, you get to assign where the camera's looking.  So I'm just going to switch this over to run our camera. And then when you, um, clad against stuff.  And then it pushes in and yo...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_012.jpg

### Modifiers + Customization [21:09]
**Transcript:** on it here. Orbit cameras. We've got customization on your commonly used things. And what this  lets you do is it lets you put in graphs to modify these different, um, attributes based on another  attribute. So here's a interesting example. We are going to change the FOV based on the orbit  height. So as you're low, we're wider. And as you get higher in the orbit, you're more telephoto.  I'm just going to turn it for centering because it's getting in the way. So look at this.  This, this graph is controlling the FOV. So this is your overhead angle and this is your lower angle.  And this is where let's flip around. Now your telephoto when you're down low and you're  wide angle when you're up high. Um, this is an extreme example, but these are useful and there's  so many different ways to configure it. Uh, so you can get some very sophisticated graph controls.  Um, this is definitely level two. More advanced stuff. We'll do a video that gets into this in detail.  Um, but that's where these things are. Look at this camera. So wide. Let me get telephoto. Hey,  guys, this is a unusable orbit camera. Here's uh, showing the modifiers. We've got a little demo  here, the velocity sensitive ...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_013.jpg

### Blueprint Customization [22:49]
**Transcript:** a little rig here where we change the recentering time speed based on the players speed.  So that's using these, and we get tons of modifiers. You can push these with blueprints.  Um, I would consider this more of an old school way of working because you're pushing numbers and  hoping you get there, but it's obviously very powerful. So we've got both. We've got the work through  the lens way or hey, I want to push it through blueprints way. So let's just run over here.  So when you're running the recentering time is very quick, but when you're stopped, it's very  slow. So what you effectively get is a camera that follows when you're running, but running,  but then you've got full orbit controls when you stopped. Obviously, this guy is the limit for  what you want to do here with the modifiers and blueprints. But this is a slightly overblown.  Look at all these things. All the usual suspect controls for piping blueprints into camera  attributes go crazy. The black eye panel man, we worked on this thing for a long time.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_014.jpg

### Black Eye Panel [24:07]
**Transcript:** Corey and you guys killed it on this. We went, we went nuts on it. Like the knobs actually  are lit. Did we have to go this far? Like look at this, the button, the lights on the buttons  actually cast light. Why did we do this? Well, because when your UI feels good, everything  feels good. When you hold a really nice camera, there's just something about it. Okay, so you can  open it, go to Window, open Black Eye Camera. Let's go through it. You can just dock it over here.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_015.jpg

### Create Camera [24:49]
**Transcript:** You can see the black eye viewport matches the, you know, the perspective viewport. And if I select  some garbage and pick a few lenses, that's the framing on those things based on that distance.  So you can preview framing. If I pick a character, that's the framing. I actually even track the  head. We get the right bones. We've, we identify the bones and we do the framing appropriate to  the character based on those shots. So you can preview what the framing looks like,  which is cool. And you've got different lens packs. If you want to create your own,  that's fine. I've made a whole bunch. But you can craft your own lens packs.  And then when you create the camera, hit the button. There they are. There's all your cameras.  Created at that view, that at the angle. And they're all set up. They're all tracking the right

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_016.jpg

### Composition Editing [25:40]
**Transcript:** bones. They've got the lenses set up. And you can adjust the composition through the lens  right in the panel. The preview modes, this performance thing, frames a super fast,  full as looks dreamy. It's whatever your scene is doing. But obviously more expensive.  It's flat to get compromised. You can still see what's going on, but it's really light.  So these cameras are set up. They're tracking the character. They're moving. It's a very simple  follow. But it's all configured. And this is a whole bunch of mouse clicks that we've turned into  what to. So dragging the composition of the window and these little white dots show the pitch  damping. So I'm just sitting it to zero. And this camera is hard pinned looking at the character.  Probably don't want that, but there it is. And if I crank these up,  you can see the white dots give a preview of the damping speed,  how aggressively the camera is going to work or not to keep that in frame.  Now the subject's going to move around the frame. But not as much as you might think. And the  reason why is because the camera's also moving with the character. So let's go to the follow.  And let's increase the positional damping. This is the ca...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_017.jpg

### Rig [27:57]
**Transcript:** And you might wonder why is it transformed down there?  Well, because  I'll just just add a little bit more. See that pivot point?  That pivot point's there because in real life cameras don't rotate around their sensors. So we've  got a control so you can set that rig up. When a steady cam, my camera's up high. So when it looks  down, it doesn't pivot around the center. Pivots are around the guy's hand on the pole  on the steady cam arm. And this might think like we're being, you know, this might sound like we're  being, you know, really fussy. It's not this is a real thing we have subconsciously  seen so much content that this pivot point thing is real. I'm just going to just the weight here  a little bit. The camera's target multiple bones on the character and I'm just bicing to target the  head a bit more than pelvis because I've moved the shot in. So we're procedurally moving the  camera. We're procedurally aiming it. We can grab the camera and move it around of course.  And that rotation is emulating the steady cam offset.  This needs a bit more. Let's correct that damping now.  And we like to think of it as your guiding this camera operator to do what you want, but it's  doin...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_018.jpg

### Dead Zones [30:56]
**Transcript:** So the dead zones, what this does is this creates a region through the lens where it disregards  all motion inside. And I'm doing kind of a weird setup here just to show it. But I'm turning  off the damping and making a big dead zone. And you can see that the little triangles the bone  and the camera won't move until it hits the edge of the box. And this is good for things like where  you're maybe you've got like an animation cycle that's got some high frequency noise in it.  Or you just want to decouple the camera from the subject a little bit.  And then there's the damping control. So I'm just made into smaller and increasing the damping.  And now we've got a little more. It's still a little bit robotic. But you can see that this  control is nice to decouple. And we have one on follow two we call that the dwell radius.  Remember we're still tracking the root bone. So look at this.  The character has to leave the character's root bone needs to leave that sphere in order for the camera  to care. And I'm going to switch this to the pelvis just for giggles because we'll see it a bit more.  Of course the camera moves up now because we've moved the whole follow operation to this new bo...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_019.jpg

### Dynamic Zoom [33:50]
**Transcript:** So when you set it to lens pack mode if you've got a lens pack selected that lens pack you know just  click between them. Whatever lenses are in your lens pack that setting I'll go between it. So if  you've got a lens pack for your project that's cool. And dynamic zoom turns this into subject size.  So what you're saying is I want this thing to be this big on screen.  This is really powerful you actually can see when I move the camera it's all these a little bit  because it's zooming to keep that thing that size on screen.  And this is really powerful when you want to make cinematics, cutscenes, sequences but you  have variable things going on. So here we are dynamically zooming. Following when the thing hits the  edge of the follow radius and we're targeting we're looking at the head and the spine bone.  You know pretty sophisticated camera animation when I'm not really doing anything.  So let's torture test this. Let's keyframe the character and then at this gale and then let's  make the character huge. This is weird of course it's weird but what we're showing you is you can  have one cutscene set up and you can have multiple different characters and the camera is going to  figur...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_020.jpg

### Manage and Utilities [36:03]
**Transcript:** for the plate and pedestal rig emulation work with the role.  That's a pretty crazy math going on there.  Yeah this is the managed tab we already talked about that and this is utilities. This is where you  can turn on names your frustums, priority stack and the preview selected of course this is  as a virus this is unreal but it's you know it's buried in a couple of menus and it's really  nicer to expose that so I'm going to make three cameras right now and look there they are.  Those preview windows are handy depending on what you're doing so we just expose them so they're  really easy to find in the utilities tab. Adaptive cutscenes you know I've done different cutscenes

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_021.jpg

### Adaptive Cutscenes [36:54]
**Transcript:** which are the same cutscene but they're different because the players involved could be different  or you're working on a scenario where you don't exactly know what the characters are going to do  so I'm going to set this shot up we're looking at this character we're targeting the head and  the palis bones we're going to put this onto a sequencer and we're going to show hybrid mode where  you can keyframe some things and then use the power of black eye to fill in the gaps in a  authentic to reality way so here's a shot can remove follows great but I want it to look over  the right side of the screen here so look at this subject screen position keyframe  characters on the left side of the screen that start and then I move to the right hand side of  the screen at the end let's tell you work in films you know what's my A what's my B here's  your frame for the A here's your frame for the B so keyframe how black eyes looking through the lens  and it fills it all in the middle it's using the ray gets using all of that math to keep you  the right rotations but you're looking through the lens the next one we're going to do is this follow  offset so we're following the character but you can...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_022.jpg

### End [42:27]
**Transcript:** what if it's not scary and create beautiful amazing shots for cutscenes cinematics for gameplay  we're helping to make Unreal Engine one of the best places in 3D to work with cameras  thank you for your interest this is BlackI2 we hope you like it  so

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_023.jpg


---

## Structured Notes

### Core Technique
Black Eye Cameras v2 complete system overview: gameplay camera setup (orbit, trigger volumes, Camera Manager), Save-in-Play real-time iteration, Blend Lists, Black Eye Panel, and adaptive cinematic camera tools.

### Summary
Full walkthrough of Black Eye v2's new gameplay camera system. Covers installing the plugin from Fab, setting up the Camera Manager, creating trigger-volume-based camera behaviors (aim, tight spaces, cross-camera, top-down), and the "Save-in-Play" workflow for iterating on cameras while the game runs. Also covers the Black Eye Panel UI for composition editing, lens packs, Dead Zones, Modifiers/Blueprints integration, Dynamic Zoom, and Adaptive Cutscenes for Sequencer.

### Key Steps
1. **Install** — Acquire from Fab, add to project, enable plugin under Plugins, restart editor. Open Demo Level (`Engine/Plugins/Black Eye/demos/`).
2. **Camera Manager** — Open Black Eye Panel → Manage tab → Create manager (project-wide or per-level). Required for all blend routing.
3. **Orbit Camera setup** — Drop in Orbit Camera actor, set Auto-Activate on player, assign Look/Follow target (root bone recommended). Set Look Profile to match project input.
4. **Save-in-Play** — Enable "Save and Play" toggle in Black Eye Panel. Edit camera properties live while game is running; changes persist after stopping PIE.
5. **Trigger volume behaviors** — Duplicate the gameplay camera, rename (e.g., "High" / "TightSpace"), set unique tag, disable Auto-Activate, place trigger volume with matching tag. Camera Manager uses default blend automatically.
6. **Aim camera** — Duplicate camera, set to Aim mode, configure world heading + pitch. Set orbit control mode (full / dampened / none). Blend in via trigger tag.
7. **Cross Camera** — Looks at and follows two different subjects (player + cube / two characters). Exposes heading, distance, height controls. Supports Dynamic FOV (procedural Zolly). Ideal for dialogue.
8. **Blend Lists** — Manage tab → Blend List. Define default blend (duration + easing). Add custom blends per camera-to-camera pair. Wild-card blends (e.g., always cut from security cam).
9. **Black Eye Panel — Composition** — Full panel mode. Preview camera framing with bone tracking + lens packs. Drag composition target on-screen. White dots visualize pitch damping.
10. **Modifiers + Blueprints** — Orbit cameras expose graph-based modifiers (FOV vs orbit height, recentering time vs player speed). Push any camera attribute from Blueprints via exposed node list.
11. **Dead Zones** — Define an on-screen region where subject motion is ignored. Combine with Dwell Radius (follow only when root bone exits sphere) to decouple camera from character noise.
12. **Dynamic Zoom** — Switch lens mode to "subject size" — camera zooms to keep subject at constant screen size regardless of distance.
13. **Adaptive Cutscenes (Sequencer)** — Keyframe subject screen position (A→B) in Sequencer; Black Eye fills the intermediate camera motion using its procedural composition math. Works with variable characters/scales.
14. **Orbit Collision** — Assign specific bone as collision look target (neck, spine). Tune Probe Size (sphere radius around camera). Compare to UE Spring Arm: Black Eye lets you assign the aim bone independently from collision direction.
15. **Rig pivot** — Steady cam rig pivot emulation: camera rotates around a virtual rig point (like a cameraperson's hand on pole), not the sensor. Configurable weight + pivot offset.

### UE Systems / Blueprints / Settings
- **Black Eye Camera Manager** — project-wide or level-scoped, controls all blend routing
- **Orbit Camera actor** — primary gameplay camera; key params: orbit radius, input speed, auto-recentering time, recentering speed, probe size
- **Cross Camera** — two-subject follow/look; params: heading, distance, height, dynamic FOV toggle
- **Aim camera** — world heading + pitch, orbit mode (full / dampened spring / none)
- **Trigger Volume** — tag-based. Camera tag = trigger tag → Camera Manager switches on entry/exit
- **Blend List** — duration, blend type (linear/ease/custom curve), exponent, whole-time buffer; wild-card support
- **Save and Play** — button in Black Eye Panel; edits during PIE are committed on stop
- **Black Eye Panel** — `Window → Black Eye Camera`; tabs: Create Camera, Composition, Rig, Manage, Utilities
- **Modifiers** — graph curves mapping one attribute to another (e.g., `orbit pitch → FOV`, `player speed → recentering time`)
- **Dead Zone** — screen-space region; motion inside region ignored by look-at
- **Dwell Radius** — world-space sphere around bone; follow only triggers when subject exits sphere
- **Dynamic Zoom** — subject-size mode: maintains constant screen-space size via FOV adjustment
- **Adaptive Cutscenes** — Sequencer keyframe on `subject screen position`; Black Eye interpolates procedurally between keyframes
- **Plugin content path** — `Engine/Plugins/Black Eye/demos/` (requires "Show Plugin Content" enabled in Content Browser)

### Difficulty
Advanced

### UE Version
UE 5.3+ (Black Eye v2 minimum; UE5 UI confirmed in frames)

### Tags
`#blackeye-v2` `#camera` `#gameplay` `#cinematics` `#blueprints` `#sequencer` `#intermediate` `#advanced`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-start-here-tutorial]] — v1 START HERE for comparison (v1 system, pre-gameplay cameras)
- [[unreal-engine-black-eye-cameras-overview-tutorial]] — v1 overview, same plugin earlier version
- [[unreal-engine-black-eye-cameras-dynamic-dialog-intro]] — Dynamic Dialog feature expanded
- [[unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics]] — car camera detailed tutorial
- [[unreal-engine-black-eye-cameras-for-gameplay-top-down]] — top-down velocity look-ahead
- [[plugin-blackeye-versions]] — version compatibility reference
