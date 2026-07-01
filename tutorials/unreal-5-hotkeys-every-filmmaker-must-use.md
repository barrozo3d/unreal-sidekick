---
title: Unreal 5 Hotkeys Every Filmmaker Must Use
source: YouTube
url: https://www.youtube.com/watch?v=HU7qHi6bn9A
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5"
tags: [sequencer, hotkeys, workflow, cinematics, camera, animation, filmmaking, tips, rendering, slow-motion]
extraction_status: complete
frames_dir: tutorials/frames/unreal-5-hotkeys-every-filmmaker-must-use/
frame_count: 14
---

# Unreal 5 Hotkeys Every Filmmaker Must Use

**Source:** [YouTube](https://www.youtube.com/watch?v=HU7qHi6bn9A)
**Author:** Josh Toonen
**Duration:** 20m29s | 14 section(s)

---

## Raw Data (for Claude Code extraction)


### Unreal 5 Filmmaking Starts with Sequencer [0:00]
**Transcript:** You can't make films and unreal if you haven't mastered sequencer.  This is the timeline where you can add animations to characters, lights and effects,  whether you're completely new to Unreal filmmaking or you just want to speed up your workflow,  this is for you.  To make it easy to get up and running inside of sequencer and take everything I've learned from last eight years,  I worked as an artist and supervisor on Hollywood Visual Effects.  I'm movies like Star Wars 9, Fantastic Beasts, and Across the Spider-Verse.  And I started using Unreal Engine as an on-set operator in virtual-production on Netflix's Avatar, The Last Airbender.  And when you use Unreal on set, you have to be ready to make any change at the last minute.  And when the whole crew around you is waiting, you have to make those changes in seconds.  That's why you have to be fast, nimble, and smarter inside of sequencer.  So I put together a list of 20 of my favorite sequencer hotkeys and tips  to make your workflows even faster inside of sequencer.  We're going to move quick, select this video so you can jump back to it later and stick around until the end,  because I'll share my favorite tip on how to add slow motion or bullet time all inside of sequencer.  You're going to want to hear this.  Let's jump right in to 20 of my favorite tips inside of sequencer.

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_000.jpg

### Sequencer Hotkeys You'll Use Everyday [1:08]
**Transcript:** So here I am in the project file for War of Being,  and I'm going to open up one of these level sequences and let's start with the basics.  So pressing play will play through your sequence.  This thing in the middle is our time indicator that we can scrub along and decide on a frame.  A really important note for visual effects is you need to have this magnet icon enabled.  D is the hot key here, and this will snap your time indicator to a whole frame.  If I zoom in here and I disable this magnet, you can see I can scrub in between our frames here,  but this will add stuttering and jitteriness to your renders if you create key frames in between any whole frames.  So make sure that's enabled.  The next hot key to know is jackal.  So jk and l j will reverse your timeline.  K will pause it and l will play it forward.  So just remember jackal, and if you don't want to use hot keys,  you can do the same thing with these buttons down here.  We have play forward, play in reverse, and then we can step forward by one frame.  You can also use your arrow keys to step forward by one frame,  or you can press shift and then the left and right arrow keys to jump ahead.  Or backwards by five frames.  Now you can change the amount of frames that we jump forward here instead of five by going  into your playback options and just changing this jump frame increment to something like 15.  And now you can make much bigger jumps throughout your scene.  Then if you want to snap back to the first frame in our output range,  you can just press the up key, and that will jump to the first frame.  And the down key actually will just playback your sequence.  So if you want to jump to that last frame, just press control and the up key,  and that will snap to our last frame.  I can right click in sequencer to drag around up and down throughout the menu.  I can press the minus key to zoom out or the plus key to zoom in.  I can also control that with these little sliders here.  Our green in and out points are our active frame range.  So you can drag these around or press the left or right bracket key to move those in and out.  And this is the frame range that movie render queue will render by default.  And if you just want to preview your active timeline,  you can press the F key to frame up on your sequencer timeline.  And that will make your in and out points be the center of your sequence.  Now the entire reason we're using sequencer is to add animations and key frames into our timeline  here. So if you want to jump to any key frame, just click on that key frame and your time indicator  will jump right to it. And if you just want to jump forward or backwards across our key frames,  it's really simple as well. Just select a track and then use the comma and period keys to jump  forward and backwards between any key frames. Now this example already has a lot of key frames in  it. So to keep it simple, let's set up a scene completely from scratch. So here we are in our

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_001.jpg

### Must-Use Settings when Starting from Scratch [3:57]
**Transcript:** graveyard sequence. And I've taken our two characters and we've imported them in the scene.  So from here, all we'd have to do is right click in our content browser, go to Cinematics and  create a new level sequence. So now we have an empty level sequence. Now you'll also want to change  over your frames per second here from 30 frames per second over to 24, which is the standard  frame rate for movies. And the first thing to do is start to add our characters and cameras into  sequencer. So there's a couple ways we can do this. The first and easiest is just to drag that  reference from the outliner into sequencer and it'll automatically add it. The other way,  I'll click on our other samurai is to add this actor to sequencer through the add track button.  And this will be the same exact thing. And the last way, the hot key that I try to use is you have  to select your object in the viewport and then press Control A. And you'll see that pops into our  sequencer here. And if this isn't working for you, just make sure you right click inside of sequencer  before pressing any hot keys to make sure you're communicating with sequencer. Now with characters,  the first thing to do is to add an animation. So I'm going to import our motion capture animation  here. And now we can see our motion capture is imported. Now the next thing we want to do is add  in a camera and start keyframing the animations. So you need two things to render a camera out of

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_002.jpg

### Animating Cine Cameras in Unreal 5 [5:12]
**Transcript:** sequencer. One is a cine camera and the other is a camera cut track. So there's two methods for  that. The easiest by far is just to click on this create a new camera icon. And this will create a  camera from your specific view. But you should also know it's easy to create custom hot keys for any

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_003.jpg

### Create Customized Hotkeys in Unreal 5 [5:30]
**Transcript:** option inside of sequencer to make that even faster. So let's make a hot key for creating a new camera.  If I go to edit editor preferences, I'm going to type in camera and scroll down to the sequencer hot  keys here. And you can see that the create camera currently doesn't have a hot key. So one that I  like to use so that I don't press it on accent is Control Shift Alt C. I still like to use the C  for the camera icon. But obviously with Control C it's a widely used hot key. But now I can go  around in the scene, find a nice spot and just press Control Shift Alt C and it will create a new  camera. Now this camera came in with this little lightning bolt icon and that just means that this  is a spawned actor. Meaning if I close this level sequence, there's no camera inside of our 3D  world. And now I can even search for a cine camera and it won't show up. For cameras, I almost  always convert these to possessible because I just want them to live inside of the scene.  And now it'll exist regardless if I close sequencer or not. Now this isn't a hot key, but this is my  most useful tip in terms of animating characters and cameras. And that's using a stage actor.  I like to parent both my characters and my camera to the same parent actor. So I'll take my cine camera  actor and parent it to this empty actor, this mocap stage. And then we can start to rotate it around  our scene. And you'll notice our composition stays exactly the same. By the way, if you want to  download all of these hot keys and more all in one place, you can get that for free when you sign up  for Unreal Fundamentals. Start as a complete beginner and unreal to making your own action scenes  in just 30 minutes a day. Check it out at unrealforvfx.com slash Fundamentals. But the real power of

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_004.jpg

### Animating the Easy Way [7:16]
**Transcript:** sequencer is animating different details of any actor inside of sequencer. Now you'll notice by  just looking through the camera options here that we have a couple little keyframe icons inside  of the details panel. And this is by far the fastest way to add keyframes for things like focal  length and aperture. Now we have these three keyframes set. And if I enable auto keyframe, this icon here,  I can scrub later on and adjust something like the zoom. And it'll automatically animate between  our two keyframes. But one thing that can be really confusing early on is that you don't see any of  these ad keyframes next to our location and rotation option. But obviously the most common thing to do  is to animate the transform. So to create any property inside of sequencer, we need to add a track.  So for our Cine camera actor, let's add in a transform track. And this will give us location,  rotation and scale and allow us to set two keyframes and animate between them. Now I can see that the  animation is a little offset here. So I'm just going to select all of these keyframes and then press  control and write arrow key. And that will just nudge these keyframes by one frame until I like the  animation. Now I'm going to delete this entire transform track here and show you the hot key in  this case. All you have to do is select your actor and press the S key. And we can see we've  automatically created keyframes on our location and rotation settings. Now we've selected this actor  and if you look at the gizmo in the center of the frame here, I press the W, E and R keys that  will go from transform rotation and scale. By just adding the shift key to those same exact hot  keys, we can quickly create transform rotation and scale keyframes. And that's the fastest way to add  those in. But a lot of times it's nice to look through the camera lens and adjust the composition  intuitively. So to do that, all you have to do is click on this little pilot icon next to our

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_005.jpg

### Piloting Cameras in Sequencer [9:15]
**Transcript:** cine camera actor. The hot key here is shift P to pilot your camera. You can see whether we're  piloting on the top left. And now we can pilot this around. And because we have auto keyframe enabled,  this will automatically update and we can quickly change our animation. So that's piloting your  camera. But the first track of any sequencer should be this camera cuts track. This is what movie  render queue will decide to render. And when you view this camera instead of piloting it,  which is shift C for the hot key, if you're viewing your camera cut, you can't adjust this camera  at all. I'm right clicking in the viewport, but I'm not able to actually change the transform.  So when you're ready to lock down your camera, this is the best option is don't pilot your camera.  View the camera cut and then you'll never have to worry about changing your animation.  Another way to set this up is you can right click on any actor and lock this actor. You'll see that  all of our tracks turn red. And this means that we can't adjust any keyframes inside of sequencer.  Just make sure to right click and unlock it when you want to make any changes. You can also pin  any actor to the top of sequencer. So now I'll always have this cine camera actor at the top of  our sequence. So if you only want to adjust one thing and oftentimes that will be the camera,  you can just pin it to the top of sequencer. But I can't stress enough that you can really animate

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_006.jpg

### Animating Materials + Blueprints in Sequencer [10:36]
**Transcript:** any property inside of sequencer even down to the materials. So what if I wanted to change the color  or intensity of our gold samurai's eyes here? Well that exists in this element zero material.  Well we could adjust that in this first material here by changing the emissive strength,  brighter or lower by setting it to zero. It turns off. But what if I only wanted to change it  inside of this one shot and not for our entire project file? Well I can't drag this emissive  strength into sequencer. But I can keep adding in tracks until I can find this emissive strength.  So let's go to add a track. And here we can see this skeletal mesh component. Now if I look on the  right side of our details panel, we can see that it's the skeletal mesh component is inside of this  actor that has all of these details underneath it. So we need to add in the skeletal mesh component  track in order to animate anything inside of here. Once this is added, we can add another track  to adjust the material parameters of any one of our materials. So let's select element zero  and add a parameter here. And now we can easily find that emissive strength. And it'll automatically  create a keyframe. So now if I set this to zero, you can see that it updates inside a sequencer.  But again, when I close sequencer and I look back at our yellow samurai, you can see that his  eyes have returned to normal. So if you're not finding the property that you want to animate,  keep diving in to the tracks and go deeper and deeper into this hierarchy inside of your details  panel to find what you're looking for. Another thing you should know about is the camera preview.

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_007.jpg

### Camera Preview (and when to use it) [12:14]
**Transcript:** I personally like to disable this, but people have different preferences. So if you go to the  editor preferences and type in camera preview, I'll toggle back on preview selected camera. And this  will give us an additional viewport that we can pin at any time. Let me change this down to a size  of three and minimize this window. And how this works is you'll just press on this little pin icon.  And now you'll have this little preview window docked to the side of your viewport at any time.  And this can make it easier to adjust your scene while still previewing your camera. All you have  to do is unpin this preview and as soon as you select anything else in your scene, that preview will  go away. Now I tend to always just use the shift to see hot key to view the camera cut, but use  whatever is easier. Now if you ever want to hide the details of any object and sequencer, just select

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_008.jpg

### Organize Sequencer in Seconds [13:00]
**Transcript:** it and press the V key and that will hide everything below it. Or if you want to expand any detail that  can be key framed, press shift V to reveal it. And that will show you every single object and  expand any of these hidden drop downs. Now as soon as you start to add a lot of things in,  your sequencer can get pretty messy. So to organize it, you can just press control F to search for  anything inside the sequencer. I'm just going to search for the samurai. And now I can select both  of these and press control G. This will create a new folder and add these actors into that folder.  So now I can just rename this as characters and now it's really easy to hide these or show them  whenever they're needed. Oftentimes I'll make anywhere from 20 to 40 cameras for a single shot.  So when I find something I'm happy with, I'll take all of the old cameras and throw them into  a folder so they still exist, but they're hidden from the rest of sequencer. Now if you have character

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_009.jpg

### Character Animation (FK Control Rigs) [13:58]
**Transcript:** animation and you want to modify it further inside of sequencer, you have two options for that.  You can either edit this with an FK control rig. Now this will not give you the controls you're  probably looking for if you have a humanoid character, but this will convert your skeleton into an  FK control rig so you can modify any bone. But the way we did this on War of Being was we created  control rigs for all of our characters so we could bake our animation onto this control rig that  makes it very easy for us to go back and add any modifications to certain keyframes. But in this  case we have an IK rig, so our hands and feet will stay in the same exact place but we can still  move around at the rest of the body. Now you can also add in additive tracks so you don't have to  modify every single keyframe. You can just identify a single bone that you want to adjust like these  hips. So as an example, I'll just tilt him over to do something really obvious and awkward and  just create a single keyframe. And now for the entire rest of the animation will have that offset.  So you can do this for the hands, feet or anything else inside of your scene to make quick adjustments  to your animation. Lastly, let's talk about slow motions and how to add bullet time all inside of

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_010.jpg

### The Best Method for Slow Motion (Bullet Time) [15:05]
**Transcript:** sequencer. Now if you want to stretch and squash or just re-time your keyframes, you have a couple  options here which make it pretty easy. The first if I want to change these transform keyframes would  be to grab this gray track at the top of any property that's keyframe and you can simply drag  these in and out points and you'll see that they scale in re-time correctly. But let's say you just  wanted to re-time the end and not the entire sequence that could get a little tricky but they  built a tool for that as well. If you press control M you'll get this hidden transform menu here  and this will let you offset your keyframes forwards or backwards by 10 units or you can make this twice  as long or you can divide these by two so they'll go twice as fast. So you can quickly double or  half any amount of keyframe animation but with this transform menu you just select the keyframes  you want so you don't affect your entire frame range. But in my opinion the best way to add slow  motion is to create a time dilation track. Just look through this drop down here and add it into  your scene and this will give us a time multiplier we can apply across our entire world. So if I set  this down to something really low like 0.25 you'll see that even the birds and the animated water  texture on our ground are all moving at one fourth the speed of our original scene. So this is  the most universal way to apply this to your scene and when I play back our sequence you'll see  that our actors are also moving in slow motion. You can even animate these so I can start slow and  get faster at the end. So you have a lot of control once you add in this time dilation track.  Lastly I think a lot of beginners can be confused by the rendering process inside of Unreal and I

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_011.jpg

### Preview Your Render in the Viewport [16:51]
**Transcript:** totally get it. This was definitely the hardest thing to comprehend at the very beginning but the  real important thing that you have to know which will hopefully demystify this entire thing is that  whenever you go to render local out of movie render queue what happens is our game starts to play  and our physics begin to simulate. Now this can be very confusing because we're not really  playing a video game inside of Unreal Engine. We really just want to play back sequencer but we  can't preview our final render because this is not through our camera but even if we did and look  through our camera cut here we could start on the first frame but the timing is not exact here  it's not correct and our render would actually look slightly different than what we're seeing here.  So how can we fix that? Well the way to preview your render exactly inside of your viewport  is actually really simple so let's browse to our level sequence here. All we have to do is click  and drag this level sequence and add it into our scene. Now this is an actor just like anything else  just like our camera or our particles or our lights there's actors inside of the scene and all we  have to do is set this to auto play and I'll set the loop to loop indefinitely. Now the next time  that we go to press play we'll automatically snap into this level sequence and we'll be able to  preview exactly what we'll see out of movie render. Now something's not looking right at this stage  you should expect it to not look right in your final render so go back and make any adjustments  at this stage here and to swap this out for another level sequence all you have to do is either drag  that other level sequence in or you can select any other level sequence from the dropdown and from  here you can use the hot key alt key to play your game or you can also simulate your game which is  playing your game without controlling upon and now when you simulate your level sequence will play  back but you won't be looking through the camera so you can view your 3d scene from an outside  perspective so you can press alt s to simulate your game you can press escape to stop game mode  or you can go back and play your selected report here and if you ever want to get your mouse cursor

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_012.jpg

### Join our Unreal Filmmaking Bootcamp [19:00]
**Transcript:** back you can press shift and f1 and now you can select anything inside of your scene and start making  adjustments while your game is playing. Now this took me just a couple seconds to explain but  honestly it took me months to learn how this entire system works together so leave a like down  below if you learned something new now did you know you can master all the skills to make your own  films inside of Unreal 5 and be job ready in just 21 days and no you don't need to know how to  model how to animate or how to code you can go from a complete beginner to creating Hollywood level  visuals in just 30 minutes a day we've helped complete beginners and industry pros just like you  learn the skills to be job ready at visual effects in virtual-production studios all you have to do  is go to on real for vfx.com slash fundamentals I've taken every lesson every template and every  cheat sheet that I use on my own commercial projects and I'm giving them away for free when you  join unreal fundamentals this is filmmaker focused training so you can create your own action scenes  entirely in unreal 5 these are battle tested on real world productions and I'm giving all of my  best secrets away so sign up today at on real for vfx.com slash fundamentals grab it on sale before  the end of this week and make sure to subscribe if you want to see more unreal visual effects and  filmmaking videos just like this and you can check out this playlist of all of the unreal 5 tutorials  I've already made so far thanks for watching and I'll see you next time peace

**Frame:** tutorials\frames\unreal-5-hotkeys-every-filmmaker-must-use\frame_013.jpg


---

## Structured Notes

### Core Technique
20 Sequencer hotkeys and workflow tips for filmmakers, from Josh Toonen's 8-year VP/vfx career. Covers: time navigation (J/K/L, arrow keys, Up/Ctrl+Up, D for snap), actor import into Sequencer (Ctrl+A), keyframing (S key, Shift+W/E/R), camera piloting (Shift+P) vs. viewing (Shift+C), stage actor parent workflow, material parameter animation (deep track hierarchy), Time Dilation track for slow motion, and preview-render-in-viewport workflow (add level sequence as actor → AutoPlay → Simulate with Alt+S).

### Summary
20m29s Josh Toonen crash course on Sequencer hotkeys and filmmaker workflow. Structured as 20 tips. Key hotkeys documented below. Additional workflows: custom hotkey creation (Editor Prefs → search action); spawnable vs possessable actor conversion; stage actor (parent camera + characters to empty actor for orbit composition); animating any material parameter via nested track hierarchy (Skeletal Mesh Component → Material Parameters → Element N → find param); FK Control Rig bake for animation editing; additive track for single-bone offset; Ctrl+M retime menu; Time Dilation track (add from dropdown, animate from 0–1+); level sequence actor for viewport preview render (drag sequence into scene → AutoPlay → Loop → Alt+S to simulate → Shift+F1 for cursor back).

### Key Steps
**Time navigation:**
- **J** — play in reverse; **K** — pause; **L** — play forward
- **D** — toggle time snap to whole frames (magnet icon); must be ON to avoid sub-frame keyframes (which cause stuttering renders)
- **Arrow keys** — step forward/backward 1 frame
- **Shift + Arrow keys** — jump forward/backward by N frames (default 5; change in Playback Options → Jump Frame Increment)
- **Up** — jump to first frame (in/out range start)
- **Ctrl + Up** — jump to last frame (in/out range end)
- **Down** — play sequence
- **Minus / Plus** — zoom out / zoom in on Sequencer timeline
- **[ / ]** — move in/out range markers (green endpoints)
- **F** — frame/fit the active in/out range in the Sequencer view
- **Comma / Period** — (with track selected) jump backward/forward between keyframes

**Adding actors to Sequencer:**
- Drag from Outliner into Sequencer → easiest
- Add Track button → select actor
- Select actor in viewport → right-click inside Sequencer → **Ctrl+A** → fastest hotkey

**Camera setup:**
- Create Camera button → creates CineCameraActor from current view + Camera Cuts track
- Custom hotkey: Edit → Editor Preferences → search "camera" → Sequencer → Create Camera → assign (e.g., Ctrl+Shift+Alt+C)
- Spawnable (default) — camera only exists while sequence is open; convert to **Possessable** to persist in scene

**Stage actor workflow:**
- Create empty actor → parent CineCameraActor + characters to it
- Rotate the parent → composition stays locked; everything orbits together

**Keyframing:**
- **S** — set keyframe on Location + Rotation of selected actor
- **W / E / R** — switch gizmo (translate/rotate/scale); **Shift+W/E/R** — set keyframe for that transform type
- Auto keyframe icon — scrub to frame → adjust property → key added automatically
- Add **Transform track** manually if S key doesn't work on a specific actor

**Nudge keyframes:**
- Select keyframes → **Ctrl + Right Arrow** — nudge right 1 frame

**Camera piloting vs viewing:**
- **Shift+P** — pilot camera (freehand camera control; auto-keyframe updates camera position)
- **Shift+C** — view camera cut (locked read-only; camera cannot be moved accidentally)
- Right-click actor → **Lock** — all tracks go red; nothing can be keyed; right-click → Unlock to resume

**Pin track:**
- Right-click track → **Pin** — keeps it at top of Sequencer regardless of scroll

**Material parameter animation:**
- Add Track → Skeletal Mesh Component → (find component) → Material Parameters → Element N → search param name → adds animatable float track
- Changes only apply within this sequence; original material unchanged when sequence closed

**Camera preview panel:**
- Editor Prefs → search "camera preview" → enable Preview Selected Camera
- Click **pin icon** in camera preview → docks to viewport side; persists while active; unpin to dismiss
- Shift+C alternative for most use cases

**Organize Sequencer:**
- **V** — collapse/hide all sub-tracks of selected item; **Shift+V** — expand all keyframeable properties
- **Ctrl+F** — search tracks in Sequencer
- Select multiple tracks → **Ctrl+G** → creates folder; rename folder to organize

**Retiming animation:**
- Drag gray bar at top of property track → stretches/compresses keyframes
- **Ctrl+M** — Transform menu (offset keyframes ±10; multiply ×2; divide ÷2); select only desired keyframes first

**Slow motion / bullet time:**
- Add Track dropdown → **Time Dilation** → adds global time multiplier for entire world (characters, particles, water textures, etc.)
- 1.0 = normal; 0.25 = 25% speed (quarter time); animate the value for variable-speed bullet time

**Preview render in viewport:**
- Drag Level Sequence from Content Browser into scene viewport (as an actor)
- Set actor: **Auto Play = true**; **Loop = Loop Indefinitely**
- **Alt+S** — Simulate game (without player controller) → sequence plays back exactly as rendered; view 3D scene from outside camera
- **Shift+F1** — recover cursor while game is running (can now select/edit scene while game plays)

### UE Systems / Blueprints / Settings
- **J/K/L transport** — industry-standard edit software navigation; works in Sequencer and viewport
- **Time snap (D)** — locks time indicator to whole frames; essential for clean renders
- **Spawnable vs Possessable** — spawnable actor lives only in sequence; possessable is a scene actor referenced by sequence; right-click → Convert to Possessable
- **Stage actor** — empty actor as parent for camera + characters; orbit/composition trick
- **Ctrl+A in Sequencer** — adds selected viewport actor to Sequencer; requires focus inside Sequencer window
- **S keyframe shortcut** — sets Location + Rotation keyframe; Shift+W/E/R sets per-component
- **Auto Keyframe** — record icon in Sequencer toolbar; any property change while moving playhead creates a key
- **Ctrl+M retime** — Transform Keyframes dialog; select keyframes first; offset/multiply/divide
- **Time Dilation track** — added from track dropdown; animatable 0–1+ float; affects all physics, particles, animations globally; keyframeable for variable speed
- **Level Sequence as actor** — drag sequence asset into viewport → Actor in scene; set Auto Play + Loop → simulates exact render timing without MRQ
- **Alt+S** — Simulate (Play in Editor without spawning player); level sequence actor auto-plays; exact render preview
- **Shift+F1** — recover cursor during Play/Simulate; enables viewport editing while game runs
- **FK Control Rig bake** — right-click Skeletal Mesh in Sequencer → bake FK control rig; full bone rotation edit; for IK need custom control rig
- **Additive track** — add on top of existing animation; key single bone for whole-shot offset without touching base keys

### Difficulty
Beginner-Intermediate. Essential reference for any UE5 filmmaker. Start here.

### UE Version
UE5 (also applicable to UE4 in most cases)

### Tags
sequencer, hotkeys, workflow, cinematics, camera, animation, filmmaking, tips, rendering, slow-motion

---

## Related Entries
- `unreal-5-secrets-every-filmmaker-must-know.md` — companion Josh Toonen tutorial; lighting, DOF, compositing secrets
- `the-2025-guide-to-rendering-in-unreal-engine-5.md` — MRQ rendering guide; Movie Render Queue setup
- `the-1-skill-you-need-for-lighting-in-ue5.md` — companion character lighting tutorial by Josh Toonen
- `ue5-animation-layers-non-destructive-camera-shake-character-tweaks.md` — Sequencer animation layers; non-destructive approach to the additive track mentioned here
