---
title: Unreal Engine 5.4: Take Recoder Driven Cinematics
source: YouTube
url: https://www.youtube.com/watch?v=h2aL7jEg_xw
author: Reality Forge
ingested: 2026-07-20
ue_version: "UE 5.4"
tags: [sequencer, cinematics, camera, mrq, movie-render-graph, blueprint, animation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-54-take-recoder-driven-cinematics/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Unreal Engine 5.4: Take Recoder Driven Cinematics

**Source:** [YouTube](https://www.youtube.com/watch?v=h2aL7jEg_xw)
**Author:** Reality Forge
**Duration:** 12m15s | 14 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone, Sean here with RealityForge. In this tutorial, we're going to learn how to use
[0:03] stake recorder to capture in-game actors like the off-road vehicle from the template.
[0:08] We'll start with driving over a landscape and then learn how to use the camera crane
[0:11] with auto key framing to quickly create our shot. We will then learn how to apply this animation
[0:17] to a proxy vehicle and fix things like motion blur on our wheels before rendering out.


### Project Recap / Setup [0:22]
**Transcript (timestamped):**
[0:22] In this video, I'm going to be using the environment we created in the erupting volcano video. In this
[0:26] project, I'm going to navigate to the maps folder and then open the canyon map. If you've seen
[0:30] that video, this is probably what you have. If you haven't, in that video, I show you how to set
[0:34] up the materials and give you the source files to get exactly this landscape. To start things off,
[0:39] we're going to zoom into this section over here. In the description of this video, you'll find a


### Recreating my drive path with rings [0:41]
**Transcript (timestamped):**
[0:43] text file, copy all of its contents, don't make any changes and paste it on your landscape. You'll
[0:48] end up with a tunnel of rings. A small note here of this isn't working for you. Make sure the
[0:52] landscape is created at the same height I created mine. The reason we're doing this is because
[0:56] if you are following along and you drive your off road car through these rings, you'll end up with
[1:00] a cinematic very similar to mine. On the upper right, we're going to click on settings and then


### Setting up game mode for offroad vehicle [1:03]
**Transcript (timestamped):**
[1:04] world settings and then override our game mode to the off road game mode. Now when you press play
[1:09] and editor, the off road car will spawn, but you can then drive using the WS and D keys. A second
[1:14] note here, the only reason we can see these game modes or have them in our project is because in
[1:18] the previous video, we started off with the vehicle template. After pressing escape to exit,
[1:22] play and editor, we're going to locate the player start actor and move it all the way back here to
[1:27] the start of our tunnel. With everything now set up, we're going to go ahead and save our map.


### Using Take Recorder to capture gameplay [1:30]
**Transcript (timestamped):**
[1:31] Once that's done, we're going to click on window, cinematics and then choose take recorder. Once
[1:36] take recorder opens, we're going to play and editor once again. Don't click on the viewport as you
[1:40] lose your mouse, but if you've done this already by accident, you can use shift F1 to get it back
[1:44] again. With our game running, we're going to add a source and take recorder and you're looking for
[1:47] this off road car pond over here. With the source added, we can now click on the record button,
[1:52] which is going to capture everything our off road car pond does. Now you can click on the viewport
[1:56] and as you drive your car around, take recorder is capturing all of this to a sequence. Once again,
[2:01] if you are following along, keep your car in the center of these rings and you'll end up with a
[2:05] cinematic very similar to mine. That said, you don't have to drive your car here. You can drive it
[2:09] anywhere on this landscape and take recorder will capture that gameplay. Once you're done, you can
[2:13] press the escape key to stop recording. Next, we're going to open our content drawer and navigate to
[2:17] the content folder. Here we're going to double click to go into cinematics, then takes and then
[2:21] there'll be a folder with today's date. Inside this folder, you'll find a cinematic called scene1
[2:26] or one that you can double click to open and then play. You can also lock the viewport to any cameras
[2:30] by clicking on this button over here. As you can see, it's playing back what it captured as we drove
[2:34] the car through the tunnel. From the quickly added project, we're going to open the place


### Adding CineCamera and Camera Crane [2:36]
**Transcript (timestamped):**
[2:38] actors panel and up here on the search bar, we're going to search for camera drag out a camera
[2:42] crane and place it anywhere on the left of your car and move it slightly higher. Press F to focus
[2:47] on the crane and then while holding Alt and your left mouse button, you can orbit around it. Now,
[2:51] drag and drop a cine camera actor into the scene and to get this to work with the crane, we need to
[2:55] drag and drop it on top of the crane in the outliner to make it a child of the crane. Then when you
[3:01] reset its location, it'll be in the right place. Now, when you make changes to your crane, you're the
[3:05] camera stays where it should be. And we're going to set this at 90. We're also going to set the Z
[3:09] value on our camera to 90 so that it's pointed towards the car. Let's now position our crane so
[3:14] that the car is in the center of the frame. And we're also going to go to the front orthographic
[3:18] view and move our crane just above the landscape. Back in our perspective view, we're going to change
[3:23] this over to the cine camera actor. And in the details panel, we're going to set our field of
[3:27] view to 18 just so that it's a little wider sequences created by take recorder are going to be read
[3:32] only. So you'll have to click this lock over here. And then you'll be able to add tracks as the crane
[3:36] is already selected. It will show up over here. And then we can add a transform subtract by clicking
[3:42] on this plus and then selecting transform. The transform track is going to store keyframes as we
[3:46] animate our crane moving alongside our car. Move your sequence to where the cars passing the first


### Animating The Crane and setting up sequence [3:48]
**Transcript (timestamped):**
[3:50] string right click and choose set start time. Then go to the point where the car passes the final
[3:55] ring and then right click and choose set end time with our start and end defined, we can press the
[4:00] F key to focus on this region. Now let's begin animating our crane. We're going to go to the
[4:04] beginning of our sequence, move the crane forward so that the cars in the center of the frame like
[4:08] this and then I'm going to add a keyframe on the transform track. Let's now go to the middle of our
[4:13] sequence. And once again, line up the car so that it's in the center of the frame and then add a
[4:17] keyframe. Let's not move this to the end of our sequence. And once again, line up that car so that
[4:21] it's in the center of the frame, and then we're going to add a keyframe, move your playback
[4:25] head between the first two keyframe oil justice position of the crane so that the cars in the
[4:29] center of the frame. Then we're going to go ahead and add a keyframe repeat the same process for
[4:33] the middle to the final keyframe go to this area in between them. Adjust that the car in the
[4:38] the center of the frame and then add a keyframe. With 6 keyframes you should have a decent
[4:42] track of the car except at the end as the car slows down. So move your playback head
[4:46] between the final 2 keyframes, center the car and then add a keyframe. We're still losing
[4:50] a little bit of track towards the end as the car slows down. So repeat the same process
[4:55] again. Go to the point between the final 2 keyframes, center the car and then add a keyframe.
[4:59] Once you're done animating your crane, select the cine camera actor and your outliner.
[5:03] Click on the add button in sequencer, actor to sequencer and then add cine camera actor.
[5:07] If you're new to sequencer, the camera cut track up here is very important. This is the
[5:11] active camera that's being rendered. So we're going to delete the existing binding and add
[5:14] our cine camera actor that we just added over here and stretch it out for the entire length
[5:19] of the sequence. Let's lock our viewport to the camera cut
[5:22] track and play our sequence. So in about 5 minutes we've captured the offered vehicle
[5:26] from the template using take recorder and animated a camera crane alongside it. Now
[5:30] we're going to set up some animation for our crane pitch, yaw and arm length. Let's add


### Animating The Camera with Automatic Keyframing [5:31]
**Transcript (timestamped):**
[5:34] keyframes for all 3 of these and if you try to make changes to this with your mouse, it
[5:38] may be a little too fast. So if you hold control you can get more precise movements.
[5:42] Now I'm going to change the viewport to the cine camera actor by clicking on perspective
[5:46] and then cine camera actor. Then I'm going to add a keyframe track to only the rotation
[5:50] under transforms of our cine camera actor. I'm doing this because now when I enable auto
[5:54] key by clicking on this button, our crane pitch, yaw, arm length and the direction our
[5:59] camera is facing will automatically be keyed when I make a change.
[6:02] So to begin I'm increasing my crane arm length and pitching it downwards so that the camera
[6:07] is just underneath this jump here. After getting it into a position that I like, I then orient
[6:11] the camera towards the car. Because we're using automatic keyframes, I can move a second
[6:15] into my cinematic and simply point the camera back at the car and Unreal will record this
[6:20] keyframe. So now our camera tracks the car as it's coming over that first jump. We're
[6:24] also going to move our camera backwards by reducing the arm length and yawing to the
[6:28] left. Like we did earlier, we're going to go to the middle of the cinematic roughly
[6:31] about here and reduce our camera arm length. So we're pulling back. I'm also going to
[6:36] set the yaw to 90 so it's pointed right at the car and I'm going to then orient the camera
[6:40] like this. Now as we're starting at the base of that first jump, your camera may clip into
[6:45] the landscape. So just increase your crane pitch and automatic keyframes will record
[6:49] it for you. On the way to our next keyframe, we are losing tracking of the car. So we'll
[6:52] just frame it a little bit more in the center and that should look a lot better. Alright,
[6:56] this is what we have so far. So we start off with this jump and then the camera slowly
[7:00] pulls back to this side profile view of our off road vehicle roughly at the middle point
[7:05] of our cinematic. At the end of the cinematic, I want the camera to move back and focus on
[7:09] the volcano. I'll start by reducing the crane arm length and setting the pitch to zero because
[7:13] we need the volcano and the car in the frame. We need to move back a little bit more. So
[7:17] I'm just going to reset this to 500, which is its starting value. While we're at it,
[7:21] we'll also make some minor adjustments to the framing. So that covers the basics of this
[7:25] cinematic, but I had an idea while recording this video. What if the camera panned up and
[7:30] went to the right of the volcano? So I added a keyframe four seconds before the end and
[7:34] then readjusted my camera's final position like this. So that negative space to the right
[7:38] of the volcano can be used for something like a title. To animate the smoke, I'm going to


### Setting up VDB (Smoke) Animation In Sequencer [7:41]
**Transcript (timestamped):**
[7:42] select the VDB volume, which has 249 frames. Then from our current end frame number, we're
[7:48] going to subtract 249. With our volume actor selected, we're going to add a track for it
[7:52] in sequencer. And we're also going to add its volume component by clicking on this cross
[7:57] and selecting this option over here. Then on the volume component, you're going to add a frame
[8:01] track and set the current frame value to zero. We're also going to add a keyframe. Then we're
[8:06] going to go to the end of our sequence and set this value to 249. Now when you play a sequence,
[8:11] the smoke is going to be animated and won't be static. However, before concluding, we need to
[8:15] remove the easing that gets added by default to any keyframes in Unreal. So select both of your
[8:20] keyframes, right-click and choose linear instead. Now as we're going to be using the movie render
[8:25] queue, make sure it's enabled in your project. So in the plugins menu up here, search for movie
[8:29] render queue, and it's this plugin right here. Click on these three dots to make sure you are
[8:33] using movie render queue, then open it up and click on unsaved config. Up here, you can specify
[8:38] where your files are going to get saved. So create an empty folder and select it. After this, click
[8:42] on accept and then render local. Once this starts rendering, you'll notice there's no suspension


### Example of problem (No Wheels / Suspension) [8:43]
**Transcript (timestamped):**
[8:46] or wheels and our body's just floating in space. Fixing this is pretty easy. But before we fix it,
[8:51] let's understand what we're going to do. We're going to create our own version of the car
[8:55] blueprint. Just add the mesh, suspension, tires, and play the captured animation on the suspension.


### Creating Proxy Offroad Car Actor [9:01]
**Transcript (timestamped):**
[9:01] Open your content drawer, navigate to the vehicles folder, and then inside this,
[9:04] you're looking for an off-road car folder. Here, you're going to right-click and select
[9:08] blueprint class, and your parent class is going to be an actor. We're going to name this blueprint
[9:12] BP underscore off-road proxy, and then double-click to open it. Once the blueprint opens in the same
[9:17] folder, you'll find the off-road body and the suspension. We're also going to drag four copies
[9:22] of the off-road tires. So one, two, three, and four. Then on the left, double-click to rename
[9:27] your tires. So I'm using tire underscore FR, meaning front right. I'm doing the same for the other
[9:33] three. So FL, BR, and then BL. Shift select all four tires and drag and drop them on SKM off-road,
[9:39] which is our suspension. On the left, select a tire, and then on the right, specify what socket
[9:44] it's getting attached to. Here, we're searching for Viz, and then wheel underscore whatever tire
[9:49] you've selected. So for example, tire FL is getting attached to Viz wheel FL. Repeat the same process
[9:55] for all four tires. We're also going to go ahead and add a red light here so that we have some
[9:59] illumination coming out of the front of the car. Back in the environment, you're going to double-click


### Adding our Proxy Offroad Car to the sequence [10:02]
**Transcript (timestamped):**
[10:03] on the sub-sequence and drag and drop the blueprint we just created. With the actor selected,
[10:07] we're going to click on the add button, actor to sequencer, and this button over here. Then we're
[10:12] going to add a transform track. Unfold off-road PON zero and scroll all the way down to the
[10:17] transform track. This is the data that was captured by Take Recorder. So Ctrl C, scroll all the way
[10:22] back up, go to the beginning of your sequence, and paste it on the newly created transform track.
[10:27] Now you should see both cars in identical positions. The suspension on the blueprint we
[10:32] created is called SKM underscore off-road. So we're going to add a track for this in-sequencer by
[10:37] clicking on this plus and then SKM off-road. The suspension on the PON we drove and captured
[10:42] with Take Recorder is called Vehicle Mesh. So we're going to go back to sequencer and look for
[10:46] the Vehicle Mesh track. Right-click and choose create linked animation sequence. Name this
[10:51] something you can easily identify. In my case, this is going to be off-road suspension. Then
[10:56] click on add and then export to linked animation sequence. Add the animation to the SKM off-road
[11:00] track by going up to animation and then choosing it in the list of options here. We're going to
[11:05] move this animation sequence back here so it's playing at the right time and disable the off-road
[11:09] car PON 0. Now when you exit your sub-sequence, lock your viewport to the camera and play it. It'll
[11:14] look exactly like it did before and renders out as well. Motion blur on the wheels is going to be a


### High Quality Motion Blur For Wheels [11:18]
**Transcript (timestamped):**
[11:20] problem and you can fix this by adding two settings to your render configuration. The first
[11:24] setting is anti-aliasing. Here we're going to override anti-aliasing to none. Set the spatial
[11:30] samples to 2 and the temporal samples to 4. I do encourage you to play around with these values
[11:34] to find a look that you're going for. The next setting we're going to add is console variables.
[11:38] We're going to add two here. The first one is going to be motion blur quality. So as you type
[11:43] here, it's going to suggest options. We're going to select motion blur quality and set this to a
[11:47] value of 4. We're also going to add motion blur separable. So it's this setting right here and
[11:53] set this to a value of 1. Click accept and then render local. And with that, you now have a cinematic


### Outro [11:57]
**Transcript (timestamped):**
[12:00] cover car you drove over our terrain. Let us know in the comments what you thought about this video
[12:04] or what you would like to see next on the channel. Give us a like, give us a sub and I'll see you
[12:09] in the next one.



---

## Captured Frames

- [1:47] tutorials/frames/unreal-engine-54-take-recoder-driven-cinematics/frame_000.jpg
- [2:26] tutorials/frames/unreal-engine-54-take-recoder-driven-cinematics/frame_001.jpg
- [2:51] tutorials/frames/unreal-engine-54-take-recoder-driven-cinematics/frame_002.jpg
- [4:04] tutorials/frames/unreal-engine-54-take-recoder-driven-cinematics/frame_003.jpg
- [6:02] tutorials/frames/unreal-engine-54-take-recoder-driven-cinematics/frame_004.jpg
- [8:29] tutorials/frames/unreal-engine-54-take-recoder-driven-cinematics/frame_005.jpg
- [8:46] tutorials/frames/unreal-engine-54-take-recoder-driven-cinematics/frame_006.jpg
- [11:24] tutorials/frames/unreal-engine-54-take-recoder-driven-cinematics/frame_007.jpg

---

## Structured Notes

### Core Technique
Use **Take Recorder** to capture live gameplay (an off-road vehicle driving a track) straight into a Level Sequence, then build a hand-keyframed **Camera Crane + Cine Camera** shot around that captured motion using **Auto Key**, swap the captured vehicle for a rigged **proxy Blueprint** (so wheels/suspension animate instead of floating), and finish with Movie Render Queue + console-variable tweaks for correct wheel motion blur.

### Summary
Sean (RealityForge) reuses a canyon/volcano environment from an earlier video and has the viewer paste in a pre-made ring path (a text-file "spline of rings") to drive an off-road vehicle through as a repeatable, camera-friendly path. He records that drive with **Take Recorder** (Window -> Cinematics -> Take Recorder -> add the vehicle Pawn as a source -> Record -> drive -> Escape to stop), producing a Level Sequence under `Content/Cinematics/Takes/<date>/Scene1`. He then builds a camera move by parenting a **Cine Camera Actor** to a **Camera Crane**, keyframing the crane's Transform track by eye at several points along the timeline, then refining pitch/yaw/arm-length framing using **Auto Key** so every manual adjustment is captured as a keyframe automatically. A VDB volcano-smoke actor gets its own Frame track animated from 0 to its frame count (249), with eased keyframes switched to **Linear**. Because Take Recorder only captures the *vehicle Pawn's* root transform (not its suspension/wheel animation), the video shows building a separate proxy Blueprint actor (body + suspension + 4 named tires socketed to the suspension mesh) and re-targeting the captured transform + suspension animation onto it via **Create Linked Animation Sequence**, so the render shows working suspension instead of a floating car body. Finishes with Movie Render Queue setup and two settings needed for clean wheel motion blur: Anti-Aliasing override (Spatial Samples 2, Temporal Samples 4) and console variables `r.MotionBlurQuality=4` + `r.MotionBlurSeparable=1`.

### Key Steps
1. **Prep a repeatable drive path**: paste a provided text-file spline/ring-path onto the landscape (must be created at the same landscape height as the source project) so a driven vehicle produces a consistent, camera-blockable path through a "tunnel of rings."
2. Override the map's **Game Mode** (World Settings -> Game Mode Override) to the off-road vehicle Game Mode so PIE spawns the drivable car (WASD); move the **Player Start** to the beginning of the ring tunnel.
3. **Record with Take Recorder**: Window -> Cinematics -> Take Recorder -> Play In Editor -> in Take Recorder, **Add Source -> From Actor** -> select the off-road car Pawn -> **Record** -> click into the viewport (Shift+F1 recovers the mouse if lost) -> drive through the rings -> **Escape** to stop. Result lands in `Content/Cinematics/Takes/<today's date>/Scene1`, playable/lockable to its camera immediately.
4. **Build the camera rig**: Place Actors panel -> search "camera" -> drag a **Camera Crane** next to the car -> drag a **Cine Camera Actor** onto the crane in the Outliner (parents it) -> reset the camera's location -> set crane arm/rotation (e.g. arm length 90, camera Z rotation 90 to face the car) -> position the crane in front-orthographic view just above the landscape -> switch viewport to the Cine Camera -> set **Field of View to 18** for a wider frame.
5. Take-Recorder sequences are **read-only** by default — click the lock icon in Sequencer to unlock before adding tracks. With the crane selected, **Add Track -> Transform** on the crane.
6. **Manual crane keyframing**: set sequence Start/End time (right-click the playhead at the point the car enters/exits frame -> Set Start/End Time) -> press **F** to frame that range -> move to several points along the range (start, 1/4, middle, 3/4, near-end, end — roughly 6+ keyframes), each time repositioning the crane so the car stays centered, then manually add a Transform keyframe at each.
7. Add the Cine Camera Actor to Sequencer (**Add -> Actor to Sequencer**) and make sure it replaces the existing binding on the **Camera Cuts** track, stretched across the whole sequence length — this is the track that determines what actually renders.
8. **Auto Key refinement pass**: add a keyframe track for only the camera's **Rotation** (under Transform) -> enable **Auto Key** (toolbar button) -> every manual pitch/yaw/crane-arm-length change while scrubbing is now recorded as a keyframe automatically — hold **Ctrl** while dragging gizmo values for finer precision. Used to: track the car over a jump (increase arm length, pitch down, aim at car), pull back to a side-profile shot at mid-sequence (reduce arm length, yaw ~90), and finish on a wide shot with the volcano and car both in frame (arm length back to its starting value ~500, pitch to 0) — plus a late "pan up and right of the volcano" flourish keyframed ~4 seconds before the end to leave negative space for a title.
9. **Animate the VDB smoke volume**: select the VDB actor (in this case 249 frames long) -> compute `end_frame - 249` as its start point in the main sequence -> Add Track for the actor, then add its **Volume Component** track -> add a **Frame** track -> keyframe Frame=0 at the volume's start and Frame=249 at the sequence's end -> select both keyframes -> right-click -> set interpolation to **Linear** (removes Unreal's default eased-in/out keyframe behavior, which would make the smoke loop-sync incorrectly).
10. **Enable Movie Render Queue** (Edit -> Plugins -> search "movie render queue" -> confirm enabled) -> open MRQ -> **Unsaved Config** -> set an output folder -> **Accept** -> **Render (Local)**.
11. **Fix the floating-car problem** (Take Recorder only captured the Pawn's root transform, not wheel/suspension animation): create a new Blueprint (parent class **Actor**) named e.g. `BP_OffroadProxy` in the vehicle's content folder -> add the off-road body + suspension mesh + 4 copies of the tire mesh, renamed FR/FL/BR/BL -> socket each tire to the suspension's matching `Viz_Wheel_<FR/FL/BR/BL>` socket -> optionally add a headlight.
12. **Re-target the captured motion onto the proxy**: drag the proxy Blueprint into the sub-sequence -> Add to Sequencer with a Transform track -> copy the Transform keyframes from the original captured Pawn's track and paste them onto the proxy's Transform track at sequence start (both actors now move identically) -> add a track for the proxy's suspension mesh (`SKM_OffRoad`) -> on the original captured Pawn's **Vehicle Mesh** track, right-click -> **Create Linked Animation Sequence** -> export it -> assign that generated Animation Sequence to the proxy's suspension track (Animation property) -> nudge its start offset to sync timing -> disable/hide the original captured Pawn -> lock viewport to camera and play to confirm the proxy now drives with animated wheels/suspension in place of the original floating body.
13. **Fix wheel motion blur** in the MRQ render config: add **Anti-Aliasing** setting -> override, Spatial Samples = 2, Temporal Samples = 4 (adjust to taste); add **Console Variables** setting -> `r.MotionBlurQuality = 4` and `r.MotionBlurSeparable = 1` -> Accept -> Render (Local).

### UE Systems / Blueprints / Settings
- Take Recorder (Window -> Cinematics -> Take Recorder): Add Source -> From Actor, Record/Stop, output to `Content/Cinematics/Takes/<date>/`
- Camera Crane + Cine Camera Actor (parented in Outliner), Field of View, crane Pitch/Yaw/Arm Length properties
- Sequencer: read-only lock on Take-Recorder-generated sequences, Transform track, Camera Cuts track (defines the actually-rendered camera), Set Start/End Time, Auto Key toggle, keyframe interpolation (Linear vs default eased)
- Volume Component **Frame** track for VDB volumetric smoke animation
- Blueprint proxy actor: Actor parent class, socket-based tire attachment (`Viz_Wheel_FL/FR/BL/BR`), **Create Linked Animation Sequence** (right-click a Sequencer skeletal mesh track) to convert captured motion into a reusable Animation Sequence
- Movie Render Queue: Unsaved Config, output folder, Render (Local)
- MRQ render settings for motion-blurred wheels: Anti-Aliasing (Spatial Samples 2 / Temporal Samples 4), Console Variables `r.MotionBlurQuality=4`, `r.MotionBlurSeparable=1`

### Difficulty
Intermediate

### UE Version
UE 5.4

### Tags
#sequencer #cinematics #camera #mrq #movie-render-graph #blueprint #animation #intermediate

---

## Related Entries
- [How to Render Chaos Cloth Simulations with Motion Blur \[The RIGHT Way\]](how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way.md) — shares `#take-recorder` `#mrq` `#sequencer`; the only prior Take Recorder mention in this library, used there just to cache a cloth sim before MRQ render. This tutorial is the first dedicated Take Recorder-for-cinematics walkthrough (confirmed gap before this ingest).
- Burn Clip Names onto DaVinci Resolve and Fusion (`tutorials/burn-clip-names-onto-davinci-resolve-and-fusion-video-quick-fusion-tip.md`) — downstream compositing step that would follow an MRQ render like the one this tutorial produces.
- `references/sequencer-cinematics.md` — general Sequencer/Cine Camera/MRQ reference this tutorial's steps plug directly into.
