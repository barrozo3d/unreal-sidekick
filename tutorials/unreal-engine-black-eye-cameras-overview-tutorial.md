---
title: Unreal Engine Black Eye Cameras: Overview Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=JGnNpbWiT_0
author: Black Eye Technologies
ingested: 2026-06-23
ue_version: "UE5"
tags: [black-eye-cameras, overview, look-at, follow, dynamic-fov, damping, bone-tracking, sequencer, hybrid-workflow, cinematics]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-black-eye-cameras-overview-tutorial/
frame_count: 11
---

# Unreal Engine Black Eye Cameras: Overview Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=JGnNpbWiT_0)
**Author:** Black Eye Technologies
**Duration:** 20m10s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey, welcome to this Black Eye Camera tutorial. We covered a lot of stuff in this one. My name is Adam. Let's go  So thank you for

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_000.jpg

### Installation [0:11]
**Transcript:** Purchasing Black Eye if you did here it is at the buy button  It goes into your library folder and you pick which project you'd like to edit to which version of Unreal  Open your plugins folder  There it is. We've got documentation. We've got a discord server super active go there lots of questions and help

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_001.jpg

### LookAt [0:33]
**Transcript:** Okay, let's jump in the basic look at this is one of the most powerful features in Black Eye  This is responsible for camera rotation what it's looking at and what's unique about this is is it looks through the lens and it gives you compositional controls  Okay, so let's put a camera in the scene. So open up your drawer  Go to your plugins folder. Make sure you've got that turned on  right here  You'll see the  You'll see the black eye folder and you'll see cameras and we've got a few different ones and  Just grab the basic look at the cine one drop in the scene  Okay, so you can see it's not looking at anything. It's just a zombie camera in the world  With the real zombie in the world  Okay, let's set up a look at shot. So here's how it goes. You select the camera  Let's make a bit more room here select the camera and you'll see there's follow look at the camera. We're gonna pick look at  so  It's simple you find your subject you hit the eyedropper you click on a subject now the camera is looking at this thing  And by default it's looking at the entire thing the bounding box. That's the  blue cube that's there  What's cool is you can move the camera around and it'll still look at the thing  Okay, so we're gonna make a little sequence here. We're gonna create a camera cut track  and we're gonna drag the black eye camera onto the track and  There it is. So the white cube is how the camera is seeing  The subject moving in screen space if now got a camera looking at something  So let's play it  You know center composition not that great and now we're cutting the guys head off. So maybe we should do some dynamic  Epi

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_002.jpg

### Dynamic FoV [2:30]
**Transcript:** So let's turn it on go to enable dynamic epi and the desired subject viewport size is how big you want that thing on screen  We're gonna change the damping. This is the zoom damping. So how aggressively it'll zoom  To keep the subject on the screen and you can see now as you get closer to the camera  The camera's widening the calculated FOV value there is showing what the FOV is and it'll  dynamically zoom between the two limits the telephoto limit and the wide limit  So now you've got a camera that's dynamically looking at something and  dynamically zooming in order to keep it in frame  So this is I mean, this is just super powerful for creating cutscenes and cinematics  When you've got variable sized objects or you just don't do the work of keyframing all this zoom  These are the composition presets are kind of handy  You can just hit them and it'll put the subject at all the standard rule of thirds. So let's just put it at the bottom left  And with the damping control  The camera will  Are very aggressively or very like thick viscous lots of camera weight  Move to track and to rotate and to zoom to keep the subject in the same spot  So super quickly no keyframes  We've got a camera that's  That's probably too wide. This is a bit crazy. Let's zoom in a bit  Okay, this toes off  Look at that we got a shot. It's not bad  Super quick. Okay, let's make a new viewport window  Again, you can check this out look at the Zollies you get because we're moving and zooming  You just try out different shots grab the camera move it around  Does this feel good here  Let's just move a little  It's so fast to prototype shot ideas because  You know you're not putting keyframes down the cameras now what you want. Let's shoot it from the other side shoot it from the front  You can see that bounding box is moving around quite a bit with this motion. So  Depending on what you're tracking the bounding box might not be the best way to do it  And a sec we'll show you that you can track bones  Let's just move this to the side  Okay

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_003.jpg

### Bone Tracking [5:20]
**Transcript:** So  Let's not track the that let's track bones. So when I turn that off it shows it is root who's back there  But if you type in his head  Now we're tracking his head bone  And that size that you get you can change the size of  Basically the cube the volume of the head and what I'm doing now is I'm changing the screen size position to  Adjust the composition slightly  So this is a different shot now  It's a bit more consistent framing because we're not framing this dynamic  You know the outer shape of something we're just tracking its head  I'm just messing with ideas. Let's move the camera around  Let's try to focus the length effectively different focal lengths because it's dynamically zooming to keep that head that size on screen  So I'm going to decouple the damping here

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_004.jpg

### Damping [6:25]
**Transcript:** Or link them but look at this. This is with no damping  I'm gonna zoom in a bit  You can see we're just like hard pinned and this is horrible or maybe useful but  That's up, you know very hard pin camera and then just by opening that up the damping where we've added a bunch of weight to the camera  And this is obviously crazy like a number of five you can almost think of this is like seconds like how many seconds  It takes the camera to catch up  So anything over one is a lot depending on the speed of what you're tracking like look at this. This is so goopy and heavy now  We change the  Screen size a little bit  And this is you know probably too much. Let's move that up there  Change the telephoto limit you can see that we were banging on the limit of the lens and I had to go down to you know 2.4 whatever  very telephoto  The dynamic zoom will only work inside the ranges of  The lens limits  So I've decoupled the damping here. What's cool about this is you can  Damp more aggressively left to right than up to down or vice versa  So  Because he's got like a lot of up and down motion. We've got  More pitch damping and less yaw damping pitch being up and down  And these are only two controls, but they're very powerful and they can give you a lot of different camera behaviors where you want to  Be sensitive to motion and one axis and less sensitive to motion on the other  Okay, so let's just  dial in a shot that's  reasonably well composed  And here's buddy pigeon toad zombie  With a little skipping is an animation cycle  But you get the idea how quickly you could move here  It's so fast and then you know what if like well, let's just try from the side  Compositions preserved the object in screen sizes preserved  Look how fast you can try out different shot ideas

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_005.jpg

### Multiple Subjects [8:48]
**Transcript:** Multiple subjects you can track more than one thing it's super useful. So pick your look at  Open a subject add more little plus  So we got two subjects now, and I'm gonna make the second one  Also looking at the character. We're gonna track two things on the same character  So we'll turn off actor bounds and look at this pelvis. So we're tracking the head and  The pelvis you can see top left the two little blue boxes one on the head and one on the pelvis  And what's really powerful about this?  Let's just adjust the  composition here with a screen space position and  Make them a little bigger in the screen  So  What's powerful about this is you can get very specific character framing like a cowboy shot or a midshot  But the characters can be different sizes. Let's say you got a cutscene and  There's some small characters and some big characters. You can have a single camera handle them  So right now because we're tracking you can see up on the top left we're tracking his pelvis and his head  Combining to make the white box in the viewport, which is containing both of those volumes  The camera is gonna zoom to always keep his pelvis and his head in the frame  And that's really powerful. You can have put ahead in a foot or multiple characters  And then the same thing goes you can drag the camera and move it around  You're always gonna get that shot with the head and the pelvis that size on the screen  Super useful

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_006.jpg

### Plate + Pedestal [10:22]
**Transcript:** Plate and pedestal it's these little things they add up to make the camera feel more realistic  So the camera plate distance and the pedestal height give you a pivot point that's not on the camera sensor  Which is the default and unreal you can see now that we're  mimicking the pivot point of where this thing would be if it was on a fluid head tripod  So like that's what it normally is and the camera very unrealistically rotates around this pivot point  Now that on its own it's not the most amazing thing of course, but  When you combine that with the dynamic look at and the fact that the camera is  Moving from this position, which is far more realistic like this is how we've seen a camera rotate and twist and turn and all the movies and  TV and when you get that  Automatically framing and you get the pivot point right just feels right and that's big

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_007.jpg

### Follow [11:16]
**Transcript:** Follow camera movement a big topic. Let's go to the follow module pick the eyedropper pick the character  By default, we just throw the camera back 300 units  So that's probably not what you want so you can either punch it in  In the transform inspector or just grab the camera and move it to where you'd like  I'm gonna put a little damping in here. So we've got a bit of positional damping  And you can see now in seconds we've created a track shot  Set the camera to follow the subject move the camera to where you want it put a little bit of damping on it  And the camera will automatically follow  Different damping settings are gonna change the behavior of the camera drastically. So going from point one to one  The camera's now really heavy and you can see as I move this back and forth and look at that slow heavy  Maybe that's too much. Maybe that's what you want and check it out with zero  100% right camera is following locked not realistic probably not useful  But give the camera just a little kiss of damping small values point to here  And you now have this nice weight feels like somebody's carrying it the camera's got mass  It's more believable and in no time at all  You've created this camera that is following looking at the subject  believable weight and it'll do that no matter where the character is what the subject is

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_008.jpg

### Sequencer [12:40]
**Transcript:** Sequencer all right, let's get some cameras on a timeline and do some cuts and blends. I'm gonna throw another camera in the scene  And then you take that camera and call it something and  You drag that on to the camera cuts track  You can obviously do this with as many cameras as you want. Let me just clean up this naming a little bit. We got a medium  We've got a wide  And I'm gonna drag the wide onto the timeline and because it's a brand new camera. It's  Not doing anything yet just staring  Off into a direction. So click look at click  Mr. Zombie now it's looking at Mr. Zombie  We'll just clean up the composition a little bit  And we're gonna move this back. This is gonna be like a big wide shot  Let's push him down the frame kind of rule of thirds him  I could have just hit the rule of thirds button  Okay, there's some there's a little bit of damping on there and we've got this wide side shot  Cool  Okay  What am I doing?  Um, I'm gonna pick the lens here could use a dynamic f ove but  Just gonna set an f ove  All right, so buddies moving along  There's that shot. Okay, we're gonna duplicate the medium shot. We're gonna make that a follow shot  We use a how to set up a follow shot just in the  I mean it a few minutes ago  So uh, this is now follow shot. We're gonna pull it behind  Let me just make a little bit more room and uh, just drag it onto the cut track. So we've now got the follow shot there  thought number three  And um, let's put it behind so you can drag the camera around of course and position it that way  Which is usually the way to go but if you want to have like really something super lined up  you can also go into  here and just uh  Set hard numbers to your follow offsets. So I want it, you know, zero right right down the line  And let's center punch the composition  Okay, so we've got this  Follow shot that's  Behind the guy and we're just gonna move it back a little bit more. Let's just clean the shot up and just take a sec to  Make it composed a little bit better a little better framing  Too wide  Okay, there and then let's lift it up a little bit  Okay, follow shot  Don't cut his feet off  Okay, so we got this side track shot  Then we cut to this wide  Side and then we get this follow and  That's fast. We got all these things set up really quickly and what's cool about this is the character can move  It could be somewhere else or you could say speed the animations up and all goodness still work  Okay, you know what for this side shot? Let's not make it a track. So I'm gonna go to the subject on follow and clear it  We now aren't following  The character anymore. So we basically  Turn it into a tripod shot and let's change the order you can right click on a on a clip and change the order  So here we are change the order a little bit now. We're gonna turn on can blend just right click the camera cut track turn on can blend  Look at this  If I overlap those two clips we go from a cut to a blend  Let's just give it a bit more room  So that cross fate there is blending the cameras together  So instead of going from a cut we have this  Hain shot and it just turns into the follow shot. Okay, do dramatically. We get a where's this fixes a little bit  Make a little bit more room for ourselves. Open this up  Smooth or softer blinds tried it a little bit earlier. Okay, look at this  Try chat track shot into this follow shot could use a bit more work  But like a fast we're working and let's go full rapid prototyping try out crazy ideas. Let's go from that mid shot to a wide in a blend  kind of weird kind of fun

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_009.jpg

### Hybrid Workflows [17:10]
**Transcript:** Hybrid setups. This is my favorite and one of the most powerful ways of working  So what we're gonna do is we're gonna add a transform track to this side camera  So it's the why shot  And we're gonna just keyframe that camera position and  There he goes he walks the cameras  Still with that same position  Let's drop a keyframe though. Let's  Move that camera you can see it's still doing the dynamic gaming with a look at module  And let's put that camera right here. Okay, so that's  Great the cameras pushing in  Okay, so let's add another layer to this we need to  We need to fix the composition. This isn't great composition. So select the camera  Let's go back to the start  Select the camera  Hit plus go to look at because we're gonna keyframe some look at attributes and then  Let's add a channel for subject screen position  So this is where the subject is in the screen position. So  We've got a key here and you can see I just moved the composition over  I just fix it damping a little bit  Now that subjects of the bottom left rule of thirds, but that's not great for here. That doesn't look so good  So let's center it and let's push it up  And  What that's doing now is we're keyframing the composition and this is such a great way of working  Because at each different beat you can adjust the composition and then black. I will fill the middle in  So you can say I want the composition here at the start and I want the composition like this in the middle and  It'll completely figure it out and not only will it figure it out  But it'll still figure it out with variable scenario things if subjects are moving characters change. It's great  And so the next layer on top of this is to not compose on the whole subject  You could see before like the framing when we went up close wasn't great. So we want to track the head so  And just pick the look at took off use a whole actor bounds  typed in head  And so now we're we're targeting the head so we can actually  Get a we can craft this shot better because  Well, I want to have the camera push in and actually go into being this wide shot and push right in and going to being this head shot  So I'm adjusting the camera position. It's just auto keyframing because we got auto keys set on  We get the framing we want and look at this  And no time at all we go from this wide shot  The camera pushes in and we land perfectly on the guy's head  Thanks so much for watching  Black guy a super powerful camera system for the Unreal Engine on fab.com

**Frame:** tutorials\frames\unreal-engine-black-eye-cameras-overview-tutorial\frame_010.jpg


---

## Structured Notes

### Core Technique
Comprehensive Black Eye Cameras overview covering all major systems: **Look At** (compositional camera rotation with bone targeting, Dynamic FOV, damping per-axis, multiple subjects), **Follow** (positional tracking with damping), **Plate + Pedestal** (realistic pivot point for tripod-like rotation), **Sequencer integration** (multi-camera timeline, cross-blend with Can Blend), and **Hybrid Workflow** (Transform keyframes + Look At auto-rotation + Subject Screen Position track for compositional keyframing).

### Summary
20m10s Adam (Black Eye Technologies) comprehensive overview tutorial. Seven major sections: (1) Installation — Fab → project Plugins folder → enable. (2) Look At — eyedropper → actor/bone; blue cube = tracking volume; Dynamic FOV auto-zooms to keep subject at desired % of screen; damping controls; composition presets (rule of thirds buttons). (3) Bone Tracking — type bone name instead of using actor bounds for stable head tracking. (4) Damping — "think in seconds"; pitch/yaw axes separate; 0 = hard pin; high values = very slow/viscous. (5) Multiple Subjects — add multiple Look At targets; each gets blue cube; white cube = combined frame; great for dialogue/cowboy shots with variable-size characters. (6) Plate + Pedestal — sets camera pivot off sensor to fluid-head tripod position; more realistic rotation behavior. (7) Follow — eyedropper → character; default 300 units back; drag camera to position; positional damping for mass/weight. Sequencer: multi-camera timeline; Can Blend for cross-fades (right-click Camera Cuts track); clip order adjustment (right-click clip). Hybrid workflow: Transform track for camera position keys + Look At auto-rotation + Subject Screen Position track for composition keys; bone targeting for zoom-in head shot.

### Key Steps
**Installation:**
1. Fab.com → Buy Black Eye → Library → Add to project; open UE → Edit → Plugins → Black Eye → enable → restart

**Basic Look At:**
2. Content Browser → Enable Show Plugin Content → Black Eye folder → Cameras → drag **Simple Look At** (or "Basic Cine") into scene
3. Select camera → Details panel → **Look At** → enable → eyedropper → click subject
4. Blue cube = tracking volume (actor bounding box by default); camera always rotates to keep subject in frame
5. Drag Camera Cuts track in Sequencer → drag BEC camera onto it

**Dynamic FOV:**
6. Look At → **Enable Dynamic FOV** → set **Desired Subject Viewport Size** (% of screen) → camera auto-zooms to maintain that size
7. **Zoom Damping** — how aggressively camera zooms; higher = slower/heavier zoom response
8. **Telephoto Limit / Wide Limit** — min/max FOV range for auto-zoom
9. **Composition presets** — rule-of-thirds buttons; click to place subject at standard positions

**Bone Tracking (vs bounding box):**
10. Look At → disable Actor Bounds → type bone name (e.g., "head") → camera tracks specific bone position; more stable for head shots vs. body motion

**Damping:**
11. Separate **Pitch Damping** (up/down) and **Yaw Damping** (left/right); 0 = hard-pinned; values ~1 = significant weight; 5 = extremely slow/viscous; think of values as "seconds to catch up"
12. Decouple axes: more pitch damping than yaw (or vice versa) for specific tracking behaviors

**Multiple Subjects:**
13. Look At → Add (+) → eyedropper → second subject; repeat for more subjects
14. Each subject gets a blue cube; white cube = combined frame encompassing all subjects
15. Dynamic FOV zooms to keep all subjects' combined frame at desired screen size

**Plate + Pedestal:**
16. Enables realistic camera pivot point (off-sensor, at fluid head tripod position); makes camera rotation feel more cinematic vs. rotating around sensor

**Follow:**
17. Follow → enable → eyedropper → character; camera snaps to default 300 units behind; drag camera to desired position
18. **Positional Damping** — 0 = hard-locked; 0.2 = slight weight/mass; 1.0 = very heavy; choose based on desired feel

**Sequencer multi-camera:**
19. Drop multiple BEC cameras in scene; configure each differently (wide, medium, follow)
20. Drag each onto Camera Cuts track as separate clip sections
21. Right-click Camera Cuts track → **Can Blend** → overlap clip boundaries = cross-fade blend between cameras
22. Right-click clip → change clip order

**Hybrid workflow (composition keyframing):**
23. Add **Transform track** to camera → set 2-3 position keyframes for the camera's physical path (push in, pull back, etc.)
24. Look At handles all rotation automatically (camera always looks at subject)
25. Add **Subject Screen Position track** → key frame X/Y where subject should appear on screen at each beat → BEC recalculates camera rotation to hit exact composition at each keyframe
26. Enable **Auto Keys** in BEC → position camera in viewport → BEC auto-records the desired shot as keyframes

### UE Systems / Blueprints / Settings
- **Look At module** — core rotation system; eyedropper to pick subject; bone name targeting; composition presets; Dynamic FOV; pitch/yaw damping per-axis
- **Dynamic FOV** — auto-zoom; Desired Subject Viewport Size (% screen); Zoom Damping; Telephoto/Wide limits
- **Actor Bounds** — default tracking volume (whole actor's bounding box); disable to use bone targeting instead
- **Bone targeting** — type bone name in Look At target field; more stable for character shots
- **Multiple Subjects** (Look At) — add multiple targets; combined frame = white cube; Dynamic FOV fits all subjects simultaneously
- **Plate + Pedestal** — camera pivot offset from sensor to fluid-head-tripod position; more cinematic rotation behavior
- **Follow module** — positional follow; eyedropper → subject; Positional Damping; default offset 300 units
- **Can Blend** (Camera Cuts track, right-click) — enables cross-fade blending when clips overlap on the cut track
- **Subject Screen Position track** (Sequencer) — X/Y keyframes for desired subject position on screen; BEC recalculates rotation to match
- **Auto Keys** — BEC setting; viewport camera adjustments auto-recorded as keyframes; "work through the lens"
- **Hybrid workflow** = Transform keys (camera position) + Look At auto-rotation + Screen Position keys (composition)

### Difficulty
Beginner-Intermediate. Start here for BEC; full system reference.

### UE Version
UE5 (Black Eye Cameras, Fab.com)

### Tags
black-eye-cameras, overview, look-at, follow, dynamic-fov, damping, bone-tracking, sequencer, hybrid-workflow, cinematics

---

## Related Entries
- `unreal-engine-black-eye-cameras-start-here-tutorial.md` — BEC beginner "Start Here" tutorial (companion)
- `unreal-engine-black-eye-cameras-v2-start-here-tutorial.md` — v2 Start Here with updated features
- `unreal-engine-black-eye-cameras-car-cameras-gameplay-and-cinematics.md` — Subject Screen Position track and damping in depth for vehicle shots
- `unreal-engine-black-eye-cameras-2-person-combat-side-camera-tutorial.md` — Multiple Subjects in practice; automatic zoom for 2-character shots
