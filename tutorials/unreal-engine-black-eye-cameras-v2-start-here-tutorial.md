---
title: Unreal Engine Black Eye Cameras v2: START HERE Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=vs6yjL-l_FQ
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "UE5"
tags: [black-eye-cameras, v2, gameplay, orbit-camera, camera-manager, blend-list, trigger-volume, save-and-play, cross-camera, dead-zone, dynamic-zoom, adaptive-cutscene, hybrid-workflow, modifiers, blueprints]
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
**Transcript:** easy to set up. We put a trigger volume. We give it a tag called aim. We create a camera.  A new one. It's often a copy of the gameplay camera. Set that to be on aim. And this camera  has got the recentering to point to a world interaction. So you blend to this camera and  it's looking at this one direction. You can pick the heading and you can pick the pitch.  And in this example, we've given the user the ability to have orbit control, but it  springs back pretty fast. You have a full control over that. It can be full orbit, no orbit  or this sort of dampened orbit. And then because I've got saving play turned on, let's  just tune this. Like a stringing a little bit. Let's change the pitch a little bit.  Okay, save and plays on. We're good. We go back out. Okay, let's run around. How does this feel  coming into it now? Okay, that's cool. A little low. Let's try it from the side. And instead of  typing a number and hitting compile and hoping it works, your iteration loop is insanely fast.  Because it has to be. So let's forget goes. We're going to change the lens. We're going to go  a little more telephoto. Let's see what that looks like. We come in. Blinder the telephoto lens.  We're going to just change this heading a little bit more. Change the pitch.  I don't know what I'm doing. I'm just framing this thing better. But you get where this is going.  You can set up a trigger volume and have the camera look somewhere specific and control how the  user orbit input feels. Very powerful. Tight spaces. You know, places where you want to change

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_003.jpg

### Tight Spaces [3:56]
**Transcript:** your over camera because of a world thing. Here's how to do it. Duplicate your gameplay camera.  Call it tight space. Create a trigger volume. Add a tight space tag. Or whatever you want to call it, of  course. Put that tag on your camera. Now we're going to use a default blend to go to that. We'll  talk more about blends in a bit and make this camera have a smaller orbit. You're done. It's that fast.  Boom. You want your camera to be higher, lower. Look to the left. Different input speed,  whatever. Trigger volume tag. And you go just like tweaking this a little bit. Let's just make it go a little  bit higher. Notice too, the collision will still look at the bone when you collide. So you're not  just like looking at the center of the character. You can control where the camera looks on the collision.  In a note, so fast to set up world relative camera behaviors. Look at that. And we're back to  gameplay. Easy. The interesting cube demo. This uses something called the Black Eyed Cross Camera.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_004.jpg

### Interesting Cube [5:10]
**Transcript:** And what it does is the cross camera can look at and follow two different things. And it gives you  a control over the heading and the height between those two different things.  The interesting cube demo here uses a direct camera reference. So you can use tags or you can  have a trigger volume like directly call a camera by putting it in the camera reference option.  Because we've got the auto activate on the player and I usually suggest keeping that as your subject  one. We're looking at the player and we're looking at the cube.  And just this can be another player. This could be anything in the world.  And then we've got a dynamic FOV on there, which is just seeing  frame these two things. Do some dynamic zooming. You can see the little white box. Look at that.  Now we're framing those two things. And because we've got save and play turned on,  we can tune this while we're going. So this is the follow distance. And because we get dynamic zoom,  it's effectively doing a Zolly. All there is. I'm pick the heading, pick the distance,  pick your height. And this is a camera, the cross camera is relative to the two different things.  Super powerful. Really good for dialogue.  Now you can play with the weights. So we're just going to look at the character. We're going to look at the  cube or mix a both. And then just play your game. Run into that spot. How does that feel?  And look at that. You can see the white target go from targeting both. Boom.  And now we're considering both cameras at a fixed heading.  I'll just tune that a little bit. We believe in Black Eye that you work through the lens.  We don't think you should type in a bunch of numbers in a blueprint and hope you get there.  You work through the lens. You get the shot that you want for any given moment.  It's like how a real DP works. It's like how cinemas work forever. Not a bunch of numbers.  It's about what the frame does.  Boom. We're back to gameplay. We've got a lot more examples of this stuff. Check out the demo scene.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_005.jpg

### Black Eye Demo Scene [7:33]
**Transcript:** It's under engine plugins. Black Eye, demos, fire it up. Look at all this stuff.  We've tried to make one of everything in here. And if you're not seeing this, remember you  got to turn on the hours. It turn on the plugin content. And that shows you all the content.  Lots of fun stuff to play with here. Okay, let's get into the camera manager.  This is going to control how all the cameras work together.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_006.jpg

### Camera Manager Setup [7:59]
**Transcript:** So let's make a third person one of the demos. Thank you for making this epic. Here it is.  We're going to drop in the orbit camera.  And we're going to set it to auto activate on the player and to look at to follow them.  And just a little sidebar check out the panel. I'm going to talk about this more. And  utilities preview selected cameras. Turn that off. Okay, so now the orbit is in there.  You're going to have to set the look to be whatever the projects look is.  In our demo scene, we use our look file. But because this project set up with this look,  you need to add this controller look profile. So I'm going to drop that in. That's just what's  consistent with this project. Save because save. Now play boom. There's our orbit camera.  And you can see there's no camera manager here. So I'm going to start a new clean project here.  Let's go back to the start clean project. Open the blackout window. Go to the manage tab.  And we can create. I'm doing it for the entire project, but you can do it for the level too.  I'm going to go back and create that camera. Just drop an orbit in project. And you know, turn off that  preview again. Set it to be auto activate and look at the player. Oh yes, the inputs of course.  Now there's an override on that. This is something you need to mention here. Now there's an override  because we set this up to be the entire project. The levels got an override. If you do a level,  you don't need to do this. But this is a difference if you've got an entire project or a level.  The level might have an override. So that was why did that? You can see the camera manager is running.  And if you don't see it for some reason, go to the blackeye panel and you can enable the debug.  And that will fire that debug up.  Gameplay camera setups. Let's do some cool world-based camera stuff. So let's create a blackeye trigger volume.

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
**Transcript:** So if you create an orbit camera and you attach it to a character, you can see what it does.  There's the orbit rings. You can see it move. We recommend attaching it to the root bone because  it tends to be the most stable. But practically, you're going to have a spawn character.  So in our demo scene, we've got a welcome camera, which is the one that activates.  And then as soon as you leave this trigger volume, we go to the default camera.  And it's set up to not auto-activate, just it activates on that trigger.  So we're in the welcome camera right now. You can see up here welcome.  And then the second you leave this little area, blend to default.  Then you can see as you go to different things where the camera managers  showing the blend between all the different cameras.  So input speed controls are here. We expose them because there's a lot of mojo. You like to tune the  stuff. Slow cameras, fast cameras. That's where you control the input speed.  The auto-recentering means if it's off, you orbit. It'll stay there. If you turn it on,  after the given time, based on the speed, it's going to return the camera to whatever your  pitch and heading centers are. You can have it be, you know, absurdly slow like this,  whatever you want. An interesting little side effect. If you get your recentering to zero  in a short time, the camera does a follow. Like it's always recentering back to that heading  echo. So you can see how the camera follow behind. But if I crank this up,  the recentering speed to something big and put a delay on, then you can run around  and the camera will not recenter to behind you. So the recentering is more than just recentering.  It's also a, it controls how your orbit camera feels as you run around. Not a lot of controls,  but a lot of different, you know, behavior possibilities. Okay, so radius makes sense.  And this is how far you want the orbit to be. And then you've got clamps on your pitch.  So you can limit it. So you can have the orbit only go up and down so far.  If you set it lower than the floor, the camera will go lower than the floor. And if there's a  collision on your floor, guess what? The camera will collide and hit the floor and slide along the floor.  And note, we're looking at this point. So the collision works on wherever you're looking. Also note,  if you set it over 90 or 290, gimbal lock hits. That's just hard math right there. So  straight down shots are not desirable. Okay, so the heading center.  The heading center is you can have it return to behind the character, but you can also have it  return to some other angle. And that's how we did the aim example here. And basically you're just  forcing the camera to return to a particular angle on the character or pitch. Now here, we're looking  the root, but let's look at the head bone. You can look at any bone. And because we don't have  much damping, you see there's little bounce on that. It's because the character's animation is  coming into the camera system. And that could be cool or it could be annoying. Maybe you want to  do a little rodeo run. Actually, if you really want to do a rodeo run, look at this, look at the hand.  We're tracking the hand on this gear. So I don't think this is what they did it, but it's, you know,  I don't know if this is what you would want to do it actually, but it's kind of fun to see. You can  look at any bone. Most of the time we recommend a root with an offset because the root is the  most stable. So do a root and then do a look at offset and push that up. So we're not actually  looking at the head. We're looking at an offset root bone. That's approximately where the character's  head is. This gives you the cleanest, you know, behavior. And we got damping. I would stay away from  these. We've got a trace amount on pitch just to decouple that. If it's at zero, the camera is hard  pinned looking at that thing, which in this case is the root with a vertical offset. If we do the head  with a hard pin, let me just fix that offset. It's cool. We're looking at the head hard pin to  the middle of the screen, but we're also going to inherit all of the motion that's on that, which,  depending on what you want, me or me, not be one, you want. So just for gagels, we're going to put  a ton of pitch damping in. The cool thing is is that you've got a vertical decoupling of the  character. But the tricky thing is, is on hard input controls, you're squishing against that  damping. Look at this. And you probably don't want this. So our recommendation is to leave the  look damping controls. Here's it on the side, side to side. So yes, the character's decoupled,  pitch wise, but you're also your orbit's going to fight with it.  So this is me showing you, hey, don't do this stuff, probably. That's what this controls do,  though, useful in other areas. Screen space position is cool, though. Look at this.  All of your orbit is looking through the lens. These aren't world offsets. This is through the lens.  And now we're orbiting around something that's not in the middle of the screen. So this is crazy  for aim modes, peering around corners, like places where you want the orbit to not be  in the center of the screen. Or if it is the center of the screen, you can buy a set up a little bit.  So it's, you know, horizontally centered, but vertically, you've got an offset. Pretty cool.  You probably don't want to do this, but just to show that all our math works, congratulations  Gerald, you're a genius. Look at, we've got a role. But the free look all still works, the orbit's  still works. Okay, so collision, usual suspect controls. You look at, you're looking down the lens.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_011.jpg

### Orbit Collision [19:36]
**Transcript:** So that orbit push in will be kind of wherever you want. I've got it at the neck here. But you  could have this be, you know, whatever you want. And right here, we're doing the recenter time.  This is way too slow. So this is like how quickly the camera comes back. It's almost like a rebound  setting on a shock. So you push in and then come straight back. You probably want this fast,  but that's what that control is. And then the probe size, this is the sphere around the camera  that's doing the collisions. So 30 is huge, bigger than the camera. But if you set this really small,  you'll see that you can even kind of have the camera clad through the wall a little bit. Like,  this is too small. You can like see, you know, behind the wall. So let's just crank this up a little  bit. And this is the size of this sphere around the camera that's doing the collisions.  And look at this just to compare the UE spring arm. You know, it's, it's colliding. It's looking  down the spring arm. But with our collision system, you get to assign where the camera's looking.  So I'm just going to switch this over to run our camera. And then when you, um, clad against stuff.  And then it pushes in and you have control over what that framing is on that, which, uh, you're probably  what? Modifiers and customization. This is an entire video on its own. I'm going to just touch

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_012.jpg

### Modifiers + Customization [21:09]
**Transcript:** on it here. Orbit cameras. We've got customization on your commonly used things. And what this  lets you do is it lets you put in graphs to modify these different, um, attributes based on another  attribute. So here's a interesting example. We are going to change the FOV based on the orbit  height. So as you're low, we're wider. And as you get higher in the orbit, you're more telephoto.  I'm just going to turn it for centering because it's getting in the way. So look at this.  This, this graph is controlling the FOV. So this is your overhead angle and this is your lower angle.  And this is where let's flip around. Now your telephoto when you're down low and you're  wide angle when you're up high. Um, this is an extreme example, but these are useful and there's  so many different ways to configure it. Uh, so you can get some very sophisticated graph controls.  Um, this is definitely level two. More advanced stuff. We'll do a video that gets into this in detail.  Um, but that's where these things are. Look at this camera. So wide. Let me get telephoto. Hey,  guys, this is a unusable orbit camera. Here's uh, showing the modifiers. We've got a little demo  here, the velocity sensitive area. So if you open the level blueprint, you can see that we've got

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
**Transcript:** bones. They've got the lenses set up. And you can adjust the composition through the lens  right in the panel. The preview modes, this performance thing, frames a super fast,  full as looks dreamy. It's whatever your scene is doing. But obviously more expensive.  It's flat to get compromised. You can still see what's going on, but it's really light.  So these cameras are set up. They're tracking the character. They're moving. It's a very simple  follow. But it's all configured. And this is a whole bunch of mouse clicks that we've turned into  what to. So dragging the composition of the window and these little white dots show the pitch  damping. So I'm just sitting it to zero. And this camera is hard pinned looking at the character.  Probably don't want that, but there it is. And if I crank these up,  you can see the white dots give a preview of the damping speed,  how aggressively the camera is going to work or not to keep that in frame.  Now the subject's going to move around the frame. But not as much as you might think. And the  reason why is because the camera's also moving with the character. So let's go to the follow.  And let's increase the positional damping. This is the camera's follow damping and it's  per axis. So you can listen to xy a lot that's movement, but decouple from its up and down or  anything, any combo in there. So now this camera is following the character, but with  much more damping. I'm just going to go big numbers too. So this is like a really smooth  steady cam operator following. And you can see the characters moving a lot on the screen a lot  because we've got a lot of look damping. So if we go back to that, we can now tune that a little bit  and get this shot dialed up. And of course all of this stuff's key frameable. But the jam here  is this camera now knows the shot that you want and it's going to do it even if things change.  So it's super fast to prototype stuff. Here I am just moving it around and it still figures it out.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_017.jpg

### Rig [27:57]
**Transcript:** And you might wonder why is it transformed down there?  Well, because  I'll just just add a little bit more. See that pivot point?  That pivot point's there because in real life cameras don't rotate around their sensors. So we've  got a control so you can set that rig up. When a steady cam, my camera's up high. So when it looks  down, it doesn't pivot around the center. Pivots are around the guy's hand on the pole  on the steady cam arm. And this might think like we're being, you know, this might sound like we're  being, you know, really fussy. It's not this is a real thing we have subconsciously  seen so much content that this pivot point thing is real. I'm just going to just the weight here  a little bit. The camera's target multiple bones on the character and I'm just bicing to target the  head a bit more than pelvis because I've moved the shot in. So we're procedurally moving the  camera. We're procedurally aiming it. We can grab the camera and move it around of course.  And that rotation is emulating the steady cam offset.  This needs a bit more. Let's correct that damping now.  And we like to think of it as your guiding this camera operator to do what you want, but it's  doing it in a very authentic to reality way. The camera's pivoting. The camera's looking through  the lens. It's doing the damping through the lens. And it's following a character like how a real  person would on a steady cam. Let's see what it looks down. Let's see that like down look.  It's a steady cam down look. Not a video game. The camera pivots from the middle of the sensor  down look. We're going to go to a shoulder rig. And the pivot point is going to be like a person  standing there. See that pivot point is not on the sensor. Look at that one.  This is not new G stuff. This is how you make cameras feel believable. And that's a camera pivoting  on its sensor. And we've never seen that in real life. I mean you'd have to make a complicated  rig in real life to do that. Nobody does. Okay, so we're going to go back to shoulder rig.  I'm going to set this to just track the head.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_018.jpg

### Dead Zones [30:56]
**Transcript:** So the dead zones, what this does is this creates a region through the lens where it disregards  all motion inside. And I'm doing kind of a weird setup here just to show it. But I'm turning  off the damping and making a big dead zone. And you can see that the little triangles the bone  and the camera won't move until it hits the edge of the box. And this is good for things like where  you're maybe you've got like an animation cycle that's got some high frequency noise in it.  Or you just want to decouple the camera from the subject a little bit.  And then there's the damping control. So I'm just made into smaller and increasing the damping.  And now we've got a little more. It's still a little bit robotic. But you can see that this  control is nice to decouple. And we have one on follow two we call that the dwell radius.  Remember we're still tracking the root bone. So look at this.  The character has to leave the character's root bone needs to leave that sphere in order for the camera  to care. And I'm going to switch this to the pelvis just for giggles because we'll see it a bit more.  Of course the camera moves up now because we've moved the whole follow operation to this new bone.  So I'm just going to move that shot back. And let's just fix that shot.  What you'll see now is the camera's not going to move until the character hits the edge of that.  We were inspired by like Dolly cam operators that aren't moving the camera on a Dolly back  and forth high frequency when the character moves in inch or two. They just move it when the  character moves past a certain limit. So you can create these like bubbles around what you're  following. The camera will like stay put until the things really on the move and then okay let's  follow now. So that's what the follow 12 radius does. See the camera's just sitting now on nice.  And then okay now they're on the move okay yeah let's move now.  But it's staying still until the camera until the character does move sufficiently in any direction.  The look enable button it just turns the look on and off. So if it's on you're going to have the  dynamic look and if it's off you won't. So the FOV control here this is the lens field of view.  Let me just put a little bit more pelvis into this shot or spinal three.  And you'll see why because we're going to do some dynamic zooming based on multiple bones.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_019.jpg

### Dynamic Zoom [33:50]
**Transcript:** So when you set it to lens pack mode if you've got a lens pack selected that lens pack you know just  click between them. Whatever lenses are in your lens pack that setting I'll go between it. So if  you've got a lens pack for your project that's cool. And dynamic zoom turns this into subject size.  So what you're saying is I want this thing to be this big on screen.  This is really powerful you actually can see when I move the camera it's all these a little bit  because it's zooming to keep that thing that size on screen.  And this is really powerful when you want to make cinematics, cutscenes, sequences but you  have variable things going on. So here we are dynamically zooming. Following when the thing hits the  edge of the follow radius and we're targeting we're looking at the head and the spine bone.  You know pretty sophisticated camera animation when I'm not really doing anything.  So let's torture test this. Let's keyframe the character and then at this gale and then let's  make the character huge. This is weird of course it's weird but what we're showing you is you can  have one cutscene set up and you can have multiple different characters and the camera is going to  figure it out. You know we see a world where singular camera systems can handle multiple different  scenarios. So look at this the characters like scaling up. We're dynamically framing. We're  dynamically zooming. We're moving. We didn't touch the camera. We changed the character skill  by you know one and a half percent whatever it is. Times it by 1.5 and look at this the camera just  it's going to figure it out. We know that you might not want to ship this if this is a cutscene  so bake it down. This is the rig is where the role is obviously all the rotations

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_020.jpg

### Manage and Utilities [36:03]
**Transcript:** for the plate and pedestal rig emulation work with the role.  That's a pretty crazy math going on there.  Yeah this is the managed tab we already talked about that and this is utilities. This is where you  can turn on names your frustums, priority stack and the preview selected of course this is  as a virus this is unreal but it's you know it's buried in a couple of menus and it's really  nicer to expose that so I'm going to make three cameras right now and look there they are.  Those preview windows are handy depending on what you're doing so we just expose them so they're  really easy to find in the utilities tab. Adaptive cutscenes you know I've done different cutscenes

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_021.jpg

### Adaptive Cutscenes [36:54]
**Transcript:** which are the same cutscene but they're different because the players involved could be different  or you're working on a scenario where you don't exactly know what the characters are going to do  so I'm going to set this shot up we're looking at this character we're targeting the head and  the palis bones we're going to put this onto a sequencer and we're going to show hybrid mode where  you can keyframe some things and then use the power of black eye to fill in the gaps in a  authentic to reality way so here's a shot can remove follows great but I want it to look over  the right side of the screen here so look at this subject screen position keyframe  characters on the left side of the screen that start and then I move to the right hand side of  the screen at the end let's tell you work in films you know what's my A what's my B here's  your frame for the A here's your frame for the B so keyframe how black eyes looking through the lens  and it fills it all in the middle it's using the ray gets using all of that math to keep you  the right rotations but you're looking through the lens the next one we're going to do is this follow  offset so we're following the character but you can keyframe the offset on that follow  so I want to land somewhere around here so I'm going to put some keyframes and I'm going to go to  just a fixed FOV and here's my shot with this lens this framing but at the start let's put the  camera somewhere crazy oh hi and just like in real life let's work through the lens let's define what  we want our A to B and then keyframe that offset and here's the B and look at this shot we've got  this like huge truck in I'm still framing I'm still moving I took what seconds right to try this idea  out and what's crazy about this now that that camera is set up you can do you can do wacky things  like let's change this character scale and I know in your project you're probably not changing your  character scale like this but this is to show that once you inform these cameras of your intent these  are the shots this is the framing this is what I want you to do at this moment in time they can  handle the changes so this becomes a super fast way of working so look at that I just put some keyframes  on the character I'm just moving these down here and here's that shot again coming in from up high  hit play you're a distracting person walking far away hide you  there we go and the camera is going to fall come in from up high  and it's framing this character that's doing something different  with all that like organic key motion that would take forever to keyframe and your director's like  I like the shot but what if what if the super scary what ifs let's just look at this here what if  we did this shot but we wanted to do it somewhere else what if we had a different character  what if we shot it from a different angle it just figures it out yeah well what if the characters  somewhere else  just fix this in a  you can just new G this screen space composition and go to the graph editor  and this is how you're working you're working through the lens so this is where on the frame  the character is in just a couple of keyframes I'll just fix that and I want it to go from the right  but then to end in the middle so see we're on the left hand side of the screen  the character does this strange gross thing but you know you get what I'm saying it's  we're handling this variable situation now we're looking on the right hand side of the screen  but I want to end let's end with it in the middle I don't like that we're cutting off the arms  not great so we're just going to throw another keyframe in there and have the character in the middle  of the screen at the end and we'll check it out run the left we've got three keyframes controlling  wear on the screen go from the right the end of the middle and then look at this we go from the right  and then we end in the middle but let's let's get kind of crazy let's just grab the character  let's do it over here we still get all that heavy positional damping on that's why the camera is  taking a second to catch up that's what the goopy right now but I'll just move it somewhere else  those cameras know the shot you know what you want  they're still figuring it out we hope that you can try out new ideas you can work faster

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_022.jpg

### End [42:27]
**Transcript:** what if it's not scary and create beautiful amazing shots for cutscenes cinematics for gameplay  we're helping to make Unreal Engine one of the best places in 3D to work with cameras  thank you for your interest this is BlackI2 we hope you like it  you  fine  you

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-v2-start-here-tutorial\frame_023.jpg


---

## Structured Notes

### Core Technique
BEC v2 comprehensive start-here. Major new systems: (1) **Camera Manager** — project-level or level-level controller that manages all camera blending, blend lists, and trigger volume camera transitions; (2) **Orbit Camera** — full-featured gameplay third-person camera with input speed, auto-recentering, pitch/radius clamps, collision, modifiers, and blueprint piping; (3) **Save and Play** — tune cameras live while game is running; settings persist back to asset; (4) **Adaptive Cutscenes** — hybrid mode: subject screen position + follow offset keyframes; camera adapts to character changes and "what ifs." Philosophy: work through the lens, not through numbers.

### Summary
43m5s Adam (Black Eye Technologies) v2 start-here covering all major new BEC2 features. Gameplay-focused first: gameplay camera + trigger volumes + tags → smooth world-relative camera changes during play; Save and Play = tune while game is running, changes persist. Camera Manager (BEC Panel → Manage): project vs level scope; blend lists (default, custom per-pair, wildcards). Demo scene = everything pre-built to study. Orbit Camera (deep-dive): input speed, auto-recentering (doubles as follow-camera behavior at high speed), pitch clamps, heading center, bone targeting, screen-space position for off-center orbit, collision (probe size + recenter time), dead zones (look + dwell radius), dynamic zoom (keep subject size on screen). Modifiers: graph-based (e.g., FOV vs orbit height) + Blueprint piping (recentering speed vs velocity). BEC Panel: Create tab (preview framing on selected character, lens packs, one-click create cameras); composition editing through lens; damping preview dots. Rig (plate/pedestal): pivot point offset for real-rig feel. Adaptive cutscenes: keyframe subject screen position + follow offset → camera adapts to character scale/position changes; "what if" shots are free.

### Key Steps

**Install + Demo:**
1. Fab → buy Black Eye Cameras → add to project → Edit→Plugins→Black Eye → enable → restart
2. Open demo scene: Engine Plugins content → Black Eye → Demos (turn on Show Plugin Content)

**Save and Play:**
3. BEC camera details → **Save and Play** toggle ON → Play → tune camera settings live → settings persist back to asset when stopped

**Camera Manager Setup:**
4. BEC Panel (Window → Black Eye Camera) → Manage tab → Create (project-scope or level-scope)
5. Place an Orbit Camera in scene → set Auto Activate for player → set look-at bone
6. Set project's look profile to match project visual settings (or load BEC demo look file)

**Trigger Volume Camera Blending:**
7. Place → Black Eye Trigger Volume → set Tag (e.g., "high", "tight_space", "aim")
8. Duplicate gameplay camera → rename → turn off Auto Activate → configure differently (e.g., higher orbit, tighter lens)
9. Set the duplicate camera's tag to match the trigger volume tag → on enter: blend to that camera; on exit: blend back
10. With Save and Play: run into trigger, tune camera settings live until correct

**Blend Lists:**
11. BEC Panel → Manage tab → Blend List → Default blend (whole duration + blend type + exponent)
12. Add custom blends: Camera A → Camera B (specific duration/type); Camera B → Camera A (different)
13. Wildcards: any camera → this camera = always cut (e.g., security camera)

**Orbit Camera:**
14. Place orbit camera → attach to character root bone → set **Auto Activate for player**
15. **Input Speed** — controls how fast player can orbit; tune in panel
16. **Auto Recentering** — ON: camera springs back to heading center after input; OFF: stays where orbited; at high recenter speed + short delay = camera functions as a follow camera
17. **Heading Center** — default: behind character; can set to any heading (used for "aim" → world direction)
18. **Radius** — orbit distance; pairs with pitch clamps (min/max pitch to prevent gimbal at ±90°)
19. **Look at bone** — recommend: root bone + Look At vertical offset (most stable); head bone = inherits animation bounce
20. **Screen Space Position** — off-center orbit (e.g., for aim modes, peeking corners); compositional offset that the orbit rotates around
21. **Collision**: Probe Size = sphere around camera; Recenter Time = spring-back speed after push-in; tune probe to avoid clipping without being too large
22. **Look Dead Zone** — disregards subject motion within rectangular screen zone; good for high-frequency animation noise
23. **Dwell Radius** (Follow) — sphere around camera; subject must leave sphere before camera follows; "dolly operator bubble"

**Dynamic Zoom:**
24. **Lens Pack mode** → automatically cycles between fixed lenses in pack based on subject
25. **Dynamic Zoom mode** → subject size mode: camera adjusts FOV to maintain subject at desired screen size; adapts to subject scale changes

**Modifiers + Blueprint Customization:**
26. Orbit camera → Customization → add modifier graph: e.g., FOV controlled by orbit pitch (low=telephoto, high=wide)
27. Level Blueprint → get BEC camera reference → push values into attributes; e.g., velocity → recentering time (fast running = camera follows; stopped = full orbit)

**BEC Panel Create Tab:**
28. BEC Panel → Create tab → select character in viewport → panel previews framing on character per lens
29. Pick lens pack → click "Create Cameras" → cameras created at current view angle, targeting correct bones, lenses pre-set
30. Adjust composition through lens in panel (drag to reposition subject on screen); white dots = damping preview

**Rig (Plate/Pedestal in v2):**
31. BEC camera → Rig section → adjust offset (forward/back, up/down) → moves camera pivot point away from sensor center → mimics steadicam/shoulder rig pivot

**Adaptive Cutscenes (Hybrid Mode):**
32. Place camera → Follow + Look At → drag to Sequencer
33. Add **Subject Screen Position** track → keyframe composition A→B (where on screen at start vs end)
34. Add **Follow Offset** track → keyframe offset A→B (start position vs end position; e.g., high → close)
35. BEC handles all rotation math; camera produces correct shot even if character changes position or scale
36. Move character anywhere → shot still works → "what if" shots are instant

### UE Systems / Blueprints / Settings
- **Camera Manager** — project or level scope; manages all camera priority, blending, and trigger transitions; required for gameplay camera system
- **Save and Play** — camera detail setting; persist parameter changes made during PIE; essential for rapid gameplay camera iteration
- **Trigger Volume + Tag** — Black Eye Trigger Volume actor; tag string matches camera tag string; no blueprint wiring needed; enter=blend to camera, exit=blend back
- **Blend List** (Manage tab) — default blend + per-camera-pair custom + wildcard (any→camera or camera→any); each entry: duration, blend type, exponent
- **Orbit Camera** — full gameplay third-person camera; auto-recentering + heading center + input speed; at extreme settings: functions as automated follow or aim camera
- **Look at bone targeting** (Orbit) — recommend root + vertical offset for stability; head bone = inherits anim wobble
- **Screen Space Position** (Orbit) — orbital center is offset from screen center; useful for aim modes and edge-peek compositions
- **Collision** — probe sphere + recenter time; BEC camera targets selected look-at bone, not spring arm center; more control over framing during collision
- **Look Dead Zone** (Look At) — rectangular screen-space dead zone; camera ignores subject motion inside it
- **Dwell Radius** (Follow) — follow sphere; camera only follows when subject exits sphere; prevents micro-jitter following
- **Dynamic Zoom** — subject size mode; FOV adapts to maintain constant screen size regardless of subject distance/scale
- **Modifiers** (Customization) — curve-based attribute overrides: axis is orbit angle/speed/etc; output is any camera attribute (FOV, radius, etc.)
- **Blueprint Modifier** — all camera attributes exposed for BP piping; old-school but very powerful; combine with Save and Play for tuned behavior
- **Subject Screen Position** (Sequencer track) — keyframe where subject appears on screen; BEC computes all rotations; adaptive to changes in character animation/scale/position
- **Follow Offset** (Sequencer track) — keyframe camera position relative to subject at different shot moments; combine with screen position for full hybrid cinematics

### Difficulty
Intermediate. V2 introduces camera manager and orbit camera; hybrid mode and adaptive cutscenes are more advanced.

### UE Version
UE5 (Black Eye Cameras v2)

### Tags
black-eye-cameras, v2, gameplay, orbit-camera, camera-manager, blend-list, trigger-volume, save-and-play, cross-camera, dead-zone, dynamic-zoom, adaptive-cutscene, hybrid-workflow, modifiers, blueprints

---

## Related Entries
- `unreal-engine-black-eye-cameras-start-here-tutorial.md` — v1 start-here; covers Look At, Follow, Cross Camera, Switcher, Bake
- `unreal-engine-black-eye-cameras-v2-gameplay-cameras-are-here.md` — BEC v2 gameplay cameras deep-dive
- `unreal-engine-black-eye-cameras-version-11-new-features-cross-camera.md` — Cross Camera detailed setup
- `unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics.md` — Save and Play tuning workflow for vehicles
- `unreal-engine-black-eye-cameras-bake-down-cam-anims.md` — baking cinematic cameras for pipeline export
