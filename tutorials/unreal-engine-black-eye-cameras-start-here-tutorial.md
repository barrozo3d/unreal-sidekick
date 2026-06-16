---
title: Unreal Engine Black Eye Cameras | START HERE Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=3KxVyOQwTRo
author: Black Eye Technologies
ingested: 2026-06-16
plugin_version: blackeye-v1
ue_version: "UE 5.x"
tags: [blackeye-v1, camera, cinematics, sequencer, blueprints, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-start-here-tutorial/
frame_count: 15
---

# Unreal Engine Black Eye Cameras | START HERE Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=3KxVyOQwTRo)
**Author:** Black Eye Technologies
**Duration:** 54m57s | 15 section(s)

---

## Raw Data (for Claude Code extraction)


### Why Black Eye [0:00]
**Transcript:** Hey, this is Adam. Thank you for your interest in Black Eyed Cameras. Let us tell you why we built this thing.  It's really fascinating because we've watched so much TV, so many movies.  Subconsciously, we have a very surprisingly deep understanding of how cameras move.  How they frame things, the weight, that little acceleration and deceleration, the leg between the camera operator and the subject moving around.  We know when this feels right. And the reason we built Black Eyed is because we believe in CG the camera should have a relationship with the subject.  And when you get this mojo right, things feel good. And when the cameras are good in a project, it elevates the quality of everything.  Black Eyed is a very powerful camera system for Unreal Engine that makes virtual cinematography feel more like real cinematography.  You can keyframe the camera's position like here, but dynamically do the composition.  Or you can have setups and we've been here before.  Hey, let's do this track shot of something flying over top. And then the director says, you know what? Let's make it go a little bit faster.  So what I'm doing here is changing two keyframes of where I want this composed on...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_000.jpg

### Plugin install [2:36]
**Transcript:** So let's get going.  Installing Black Eye. Go to the Fab tab inside you in and type Black Eye cameras.  And there we are.  So when you click on it, buy it. Mine says View and Launcher because I've already bought it.  Build it. But once you buy it, it'll show up in here.  And then you say where you'd like to install it, which project and then boom, it's in the project.  Once your project's open, go to Edit, Plugins, click on Black Eye and you're going to have to turn it on.  And it'll make you reboot. And just note here we get support, which is our discord and the documentation.  Use read the documentation for real.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_001.jpg

### Debug and CVARs [3:15]
**Transcript:** Debug and Cvars. So you can go to the little eyeball and click on Black Eye.  It'll show all of our stuff. And then in the Cvars area, just type Black Eye or Black and you can see our stuff.  So if you want it off, type zero. There I just turn the guides off.  And this will be the master. So under the eyeball, it'll show everything or nothing, whatever you've got configured.  And you could sub configure things in here like guides or camera names or frustums, all sorts of stuff.  Camera names are pretty wild. I mean, if you got a lot of cameras in the scene, this could be a bit of a mess.  Or it can really help you debug before 5.6. It's under this little show button top left.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_002.jpg

### LookAt [3:51]
**Transcript:** And right here is where it all started. Many years ago, we thought, why can't we just have a camera that dynamically composed on moving subjects?  We don't have to keyframe all this. And that's where we got this idea.  So let's make one of those simple, but very powerful camera. So go to the top, click Black Eye Create.  Look at camera. You can see this is a zombie camera. It's not doing anything yet.  It's just in the world.  Not paying any attention to people walking by. So let's click Look at.  Right now we're just going to do one subject. Hit the eyedropper.  Pick a character.  That's it. I mean, that's not it. There's more, but that's it to make a camera start to dynamically compose a moving subject.  You can see this shot's not great for a few reasons. I'm going to drag it onto the timeline.  So when we click it and we turn it on, we can see our guides.  So because we just click, click the character.  We're targeting the whole actor bounds.  And for some things that's great, sometimes it's problematic.  You can see that that outside shape changes.  So we're going to put on some dynamic FOV.  And what's cool about this is it lights the camera automatically zoom to keep that on...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_003.jpg

### Plate and Pedestal [9:24]
**Transcript:** This is such an unassuming feature, but it actually brings an incredible amount of realism because in real life cameras don't rotate around their sensor.  So what the plate pedestal lets you do is it lets you create the pivot point to mimic real life pivot points like in steady cams and fluid heads.  It lets you adjust the camera up and down and forward and back.  And that's where the camera will rotate from and it turns out we've watched a lot of it.  So look at this. No cameras ever rotates in real life around the middle of the sensor.  No camera does that.  So plate and pedestal lets you adjust the camera offset to mimic real life rigs.  Like look at where that's pivoting around. It's you know lower and further back.  We've seen so many movies like these steady cams that pivot point and so low.  But like look what the motion looks like like this. We've seen this. This is what movies look like.  So we need to emulate this. It's very important.  So here I'm putting the camera. I'm going to far this to far, but look at this. It's way up top.  And it's pivoting around that pivot point that's below the camera.  And it's subtle, but the way that the camera moves now.  It's going to sw...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_004.jpg

### Follow [11:38]
**Transcript:** Let's do it for character. So where look at handles the rotations.  Follow handles translation. So let's click the follow and then let's click a subject.  Boom. We're following that subject. Now you see the camera pops. We just assume 300 units off to the side.  Of course, you can adjust that. And if we hit play, you can see the camera's following, but see it's pumping.  It's not great. And we're going to show you why.  So there's no damping. It's all set to zero. This is positional damping. So if you crank this up, you can see the camera.  It's actually going to fall behind a little bit because it's like traveling through some viscous honey.  Trying to keep up the subject. Look at this. If I go back on forth, you can see the camera.  If I go back on forth, you can see that the camera is going wiggle, wiggle. That's the damping working.  So that's better. So you can grab the camera and move it forward.  And just offset for that damping amount. You can move it anywhere.  Part of the magic and those transforms will back propagate into the follow offset.  There you go. You're going to side shot.  Still not perfect.  There a bit of damping there. You can see and we'll just tweak it and...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_005.jpg

### Follow Vehicles [15:09]
**Transcript:** Okay, let's do the next flavor on vehicles.  Maybe at this super cool big medium small. Thank you so much for these environments are beautiful.  So we're dropping a new camera in.  It's going to be a follow camera, of course.  And just like with the character, just click the car.  Dink, we go off 300 units to one side.  We got a really rigid camera constrained to the car.  Not a lot of life yet, but you can just grab the camera.  Move the shot. Now we're going to set. Here's the offset.  You can punch the numbers in manually too, of course.  Okay, and we're going to get look at the car too.  So click, look at, click the car. You can see the blue box.  Now we're looking at the car.  And of course, because we're now looking at the entire car, we can do some line stuff.  So we'll just do dynamic FOV.  You might think I love dynamic of FOV in every shot. I don't.  It can be too much, but sometimes it can also be really fast just to try out ideas.  Look at the Zolly.  Where's Hitchcock? Automatic Zolly. No rigs.  Okay, side shot, tracking the car. Pretty basic.  Let's bring in a sequencer. Let's look at the debugs.  So we're following the car.  It's locked to the side.  Really basic. Fo...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_006.jpg

### Follow Keyframes [18:48]
**Transcript:** Procedural camera behaviors, but then they'll let you key frame and craft some other things.  So I just grab this camera and set this sort of over the shoulder shot up.  But look at this.  We're going to now look at that other ballerina.  The camera is following the walker, but looking at the ballerina.  And you can set these up in any combination.  Follow this. Look at that and switch.  What I'm doing here now is I've got the camera on sequence.  We're just key frames from follow offset.  So I want to say start with it here. Let's just keep frame that.  And then go to the somewhere else.  Here.  You can see when we get here.  We lost the composition of the character because the camera is now behind.  So we can adjust the relationship between what the camera and what it's following here through key frames on follow offset.  Let's dump a key here.  And then the camera is still going to follow, but we're keyframing the relationship between the two.  And you can do that on anything here. We're going to do it on a Norbit.  So look at this follow camera dynamically moving with the ballerina also dynamically composing.  Really basic shot just took a second to set up.  Let's adjust the vi...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_007.jpg

### Multiple Subjects [23:21]
**Transcript:** Multiple subjects.  Let's get a camera to track two people, common scenario.  So we've got the camera in the scene.  We're going to select the subject mode to be multiple subjects.  And then let's click subject one to be the left and collect subject two to be the right.  You can see now I'm just going to grab the camera and move it around.  The camera is tracking those two people.  You can see the blue box.  It's going around their whole, their bounding box effectively.  These two guys have a little disagreement of sorts and they get closer and further back.  Let's move this camera to a better shot.  Okay, and then to really show it off, we'll do some automatic FOV because these guys get close to each other and they get further apart.  So we'll show how this works on all the systems.  Okay, let's get on to sequencer and we can see what's going on.  So the camera is framing.  So the white box is going around.  The two blue boxes, the white box is the product of everything.  And we're following subject on the left, subject on the right.  And camera is not doing a lot because they're not really moving too much.  But watch, we throw.  The camera moves back.  Look at that.  Let's see ho...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_008.jpg

### Keyframe Weights [29:27]
**Transcript:** Multiple subjects and keyframing weights.  This is a powerful config for more complicated shots.  Big ups to big mediums.  Small for these environments.  Beautiful.  Okay. So we're going to just make a camera and drop a black eye camera in the scene.  And we're going to say look at, but we're going to multiple subjects.  And in this case, we're going to target like different components on this little space contraption.  So here we are.  We're going to open it up and say, let's target.  And I don't know the bone name. So let's go in and check out what are the bones on this thing.  We're targeting the camera on the camera.  Camera target in the camera.  So we type in the bone name, which is camera three for this thing.  Turn off use component bounds.  Component bounds will target the whole entire object, the bounding box, the object.  But we want to target sub things like bones.  And you can see sometimes where you want it looking is an exactly lined up with where the bone is.  Just due to the way it's weighted, rigged.  So we're going to change the bounding radius, which is a box, a cube that we draw around to the bone.  You can make that different sizes.  And we're going to use the...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_009.jpg

### Cross Camera [37:57]
**Transcript:** The blackhead cross camera, you know, we see a world where maybe the dialogue is synthetic.  You don't know how long a scene is going to last.  You don't know what they're going to say.  You need a camera system that can handle like a variable length dialogue section.  So here we got these two guys.  We're going to drop a camera in.  We're going to drop the cross camera in.  We're going to click perpendicular follow two subjects on the left and the one on the right.  So let's subject left, left character, subject right, right character.  The camera moves over to the side.  Let's target the root.  Roots are often more stable for camera position than the other bone.  Okay, so we're going to lift the camera up on the camera height.  And here we go.  The camera is, but it's not looking at them.  It's looking, it's pointing at them, but it's not looking at them.  You can look at multiple subjects, but for this, we're just going to look at one character.  Okay, we're going to tape in the head bone.  And turn off user-bound.  So we're not framing their entire character.  So this camera is relative to both people, but we're just looking at the head of the one.  And if I adjust the heading,...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_010.jpg

### Camera Switcher [47:41]
**Transcript:** Easily switch between your army of cameras,  which are dynamically following and framing and composing whatever's happening.  Incredibly powerful for MoCAP, live events, eSports.  Okay, here's how to do it.  This is our scene.  Well, these guys look like they just came back from the open pasta bar at lunch.  And we got a rando singer.  Perfect.  So drag the camera switch actor into your project.  To your level.  And then you can see here under cameras,  we've got this array that you generate.  So you pick a button, you pick a camera.  You can even click that keyboard button and then actually just tap the keyboard  and you bind them.  So these are some cameras that have already gotten the scene set up.  But let's make another one.  So I'm just going to drop a Black Eye Camera into scene.  We'll make it look at the character.  Just the positioning a little bit.  Let's make this one look at the head.  So we hit the look at, type in the head bone, turn off the actor bound.  So it's looking now just at the head bone.  And you know, we can put it wherever we want.  Just a composition.  Sure.  Fix that.  Just, there we go.  Okay, let's duplicate this.  And we're going to make another came...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_011.jpg

### Keyframe Composition [50:26]
**Transcript:** A key framing composition.  If you're a layout artist in games or CG, this is the juice right here, because this is such a powerful combination of procedural cameras, which we don't take your talent away from you.  But we're allowing black eyes letting you drive the composition like a camera operator.  So you can see when you look at something, black eye will always look at it no matter where the camera is or what the subject does.  But this is not great composition because the composition is right in the middle of the screen.  So let's move the camera.  Let's move the composition.  We're looking through the lens.  We wind it on the right side of the screen.  So you can see now the camera, all the rotations, all the buttery math.  To keep the car on the right side of the screen.  But I want to change the composition over the course of the shot.  And this is just so powerful.  What you do is you add a look at channel.  And then you add your screen space position.  And then just open that up and set a keyframe for how you were looking through the lens, what the composition you want.  And then go to some other position in your shot.  And adjust your composition.  And keyframe those.  ...

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_012.jpg

### Baking Cameras [53:53]
**Transcript:** You want keys on every frame.  We get it.  Lots of reasons why.  Let's pick it up a little bit near the end of this video.  Okay, so you got a crazy shot.  Look at this like, my body cam.  Let's bake it down.  So you create a cine camera actor.  Let's rename it.  Clear names are great.  Good habits.  So you drag it down into sequencer.  And then you pick the black eye camera you want to bake.  You go to linked cameras.  You punch the camera in.  The actor that you want to bake it down to.  You hit record.  That's it.  Baking down it goes.  And look at this.  Look at all those juicy keyframes.  Keyframes on everything.  There you go.  Bake it down.  DCC round trip.  You want to knew G it.  We understand.  There it is.  Boom.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_013.jpg

### End [54:44]
**Transcript:** Thank you for watching.  We're here for you.  Join our Discord.  Reach out to us.  Let's talk about shots.  Let's build some really cool stuff.  Thanks.

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-start-here-tutorial\frame_014.jpg


---

## Structured Notes

### Core Technique
Black Eye Cameras v1 complete system tutorial: LookAt (single and multiple subjects), Plate & Pedestal rig pivot, Follow with damping, Follow Vehicles, Keyframe Weights, Cross Camera, Camera Switcher, Sequencer hybrid keyframing of composition, and baking camera animations to CineCameraActor.

### Summary
55-minute original (v1) Black Eye START HERE tutorial. Covers why the plugin exists (cinema-accurate camera behavior in CG), all core camera types (LookAt, Follow, Cross Camera), multi-subject tracking with keyframeable weights, the Camera Switcher actor for live switching between an army of cameras, hybrid Sequencer mode (procedural tracking + manual position/composition keyframes), and baking the result to a standard CineCameraActor for export/round-trip. Installs via Fab tab inside UE. Includes CVARs/debug overlay.

### Key Steps
1. **Install** — Fab tab inside UE, search Black Eye Cameras. Enable plugin under Edit → Plugins. Debug overlay: Eyeball → Black Eye; CVARs: type `black` to filter. Note: before UE 5.6, show button is top-left.
2. **LookAt camera** — Black Eye Create → LookAt Camera. Click Look At → eyedropper → pick subject. By default tracks actor bounds; switch to bone targeting for characters (type bone name, disable use component bounds). Dynamic FOV auto-zooms to keep subject at constant screen size.
3. **Plate and Pedestal** — Offsets the camera's rotation pivot point to emulate real-world steady cam / fluid head geometry (pivot below/behind the sensor). Adjust plate offset X/Z to mimic specific rigs. Subtle but critical for cinematic realism.
4. **Follow (character)** — Click Follow → pick subject (camera jumps 300 units to side). Add positional damping to decouple camera from subject jitter. Drag camera to adjust spatial relationship; offset back-propagates to follow offset automatically.
5. **Follow (vehicles)** — Same flow as characters. Add Look At on the car for dynamic FOV Zolly effect. Combine with Sequencer to keyframe relative position changes while tracking continues.
6. **Multiple Subjects** — Set subject mode to Multiple Subjects. Pick subject one + two. Camera frames both actors' combined bounding box. Add Dynamic FOV to handle variable distances (subjects approach/diverge).
7. **Keyframe Weights** — With multiple subjects, keyframe individual subject weights (0–1) in Sequencer. Cut between subjects by ramping one weight down and another up. Can target specific bones (type bone name, disable actor bounds, set bounding radius). Useful for detailed setups like space vehicles with multiple camera target points.
8. **Cross Camera** — Drop Cross Camera actor. Assign Subject Left + Subject Right (e.g., two dialogue characters). Camera positions itself relative to both. Adjust heading, camera height, follow distance. Look At targets one character's head bone. Cross Camera is relative to the two subjects' midpoint.
9. **Camera Switcher** — Drag Camera Switch Actor into level. In Cameras array, bind cameras to keyboard keys. Live-switch during playback. Extremely powerful for MoCap, eSports, live events — an army of Black Eye cameras all tracking dynamically.
10. **Keyframe Composition in Sequencer** — Add LookAt channel → Screen Space Position. Keyframe subject position on screen (e.g., move from left third to right third over the shot). Black Eye handles all rotation math while you control what appears where on screen.
11. **Bake to CineCameraActor** — Create CineCameraActor, drag to Sequencer. Select the Black Eye camera → Linked Cameras → set target CineCameraActor → hit Record. Bakes all procedural animation to dense keyframes on every channel. Ready for DCC export / NukeX round-trip.

### UE Systems / Blueprints / Settings
- **Black Eye LookAt** — core camera type; params: subject, bone name, use component bounds, bounding radius, Dynamic FOV
- **Black Eye Follow** — translation component; params: subject, follow offset (spatial relationship, keyframeable), positional damping
- **Plate and Pedestal** — pivot point offset; X (forward/back), Z (up/down) mimic real-world rig geometry
- **Multiple Subjects** — subject mode; adds subject array; white bounding box = combined frame of all subjects
- **Keyframe Weights** — per-subject weight in multi-subject mode; keyframeable 0→1 in Sequencer
- **Cross Camera** — two-subject follow+look-at; params: heading, camera height, follow distance; look-at targets one bone
- **Camera Switcher** — actor with camera array bound to keyboard keys; enable Camera Manager for blends
- **Screen Space Position** — Sequencer channel under LookAt; keyframe where the subject appears on screen (0,0 = center)
- **Linked Cameras** — bake target for recording Black Eye output to CineCameraActor keyframes
- **CVARs** — `blackeye.guides 0/1`, `blackeye.cameranames`, `blackeye.frustums`; exposed under Eyeball → Black Eye

### Difficulty
Advanced

### UE Version
UE 5.x (Fab install method = UE 5.4+; "before 5.6 it's under show button" confirms tutorial spans multiple versions)

### Tags
`#blackeye-v1` `#camera` `#cinematics` `#sequencer` `#blueprints` `#intermediate` `#advanced`

---

## Related Entries
- [[unreal-engine-black-eye-cameras-v2-start-here-tutorial]] — v2 version; adds Orbit Camera, Camera Manager, gameplay system, Save-in-Play
- [[unreal-engine-black-eye-cameras-version-11-new-features-cross-camera]] — Cross Camera feature detail
- [[unreal-engine-black-eye-cameras-cam-switcher-tutorial]] — Camera Switcher dedicated tutorial
- [[unreal-engine-black-eye-cameras-bake-down-cam-anims]] — Baking cameras dedicated tutorial
- [[unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics]] — car-specific applications
- [[plugin-blackeye-versions]] — version history and compatibility
