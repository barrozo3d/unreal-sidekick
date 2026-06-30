---
title: Motion Capture isn't just for Hollywood any more...
source: YouTube
url: https://www.youtube.com/watch?v=hoCoa8gMP-M
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5"
tags: [mocap, motion-capture, rococo, workflow, sequencer, retargeting, control-rig, filmmaking, cinematics, indie-production]
extraction_status: complete
frames_dir: tutorials/frames/motion-capture-isnt-just-for-hollywood-any-more/
frame_count: 10
---

# Motion Capture isn't just for Hollywood any more...

**Source:** [YouTube](https://www.youtube.com/watch?v=hoCoa8gMP-M)
**Author:** Josh Toonen
**Duration:** 18m26s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Motion Capture for Indie Filmmaking [0:00]
**Transcript:** What if you could start making your own sci-fi films and action scenes at a fraction of the time?  Well now you can, using motion capture. Believe it or not, any one of you can start using motion  capture and start making Hollywood-level films just like this from home, saving you hundreds of  hours and getting better results than having to painstakingly keyframe everything yourself.  I spent the last decade working in Hollywood visual effects, and the last two years making animated  films an unreal engine. But it wasn't until I made this samurai sword fight that I was able to  brew my own sci-fi action scenes to life faster than ever. So in this video, you'll learn all the  shortcuts in my exact process to go from an idea to final animation, even if you're not an  animator yourself. You'll see just how streamlined this workflow is, and why motion capture isn't just  for big studios anymore. It's now a tool that all of us filmmakers can actually use.  Now the traditional way of making animated films is you start with a storyboard,  then you make your pre-vis, and then you make the final result. In each step it uses a different  software. But with Unreal Engine 5 we can go from storyboard to pre-vis to final result while  working in real time, and that's what we're going to cover today. So before we dive in, let's watch  this breakdown of how Halon Entertainment approaches pre-vis with filmmaking in mind.  Basically it's like watching a movie before you actually make the movie. Pre-vis is really just  a way for the director and everybody that's involved in a production to come up with an agreement  on what they would like to do. The great thing about using Unreal is that it looks so good that  it gives them a really good sense of what the eventual movie is going to be like.  There's a reason that I love pre-vis, and I love this development process. This is where  the movies get made. We really have to concentrate more on the story and your composition. Those are  the things that are going to hold your audience. Does the emotion work? And are you engaged? And if  you're engaged when it looks like a video game, it's only going to be that much better when it's live action.

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_000.jpg

### Four stages to bring any film to life [1:50]
**Transcript:** So in this lesson we'll cover the four stages that every motion capture production goes through.  We'll start with an overview and then dive into each step, and it all starts with the build.  Start out by collecting inspiration and building your film sets and environments along with your  3D characters. The second step is motion capture, where you'll work with actors together on set to  create a real performance, and then you'll need to clean up your motion capture data to get a clean  animation. Then we'll start the filmmaking cycle. This is when you set up your cameras,  assemble your first edit, and then improve the animations through the camera lens. Then you can  decide what parts of your motion capture you need to improve and upgrade, which is super easy when  you have a control rig. And lastly, when your edit is locked, we'll move on to lighting and effects,  and we'll add in the finishing touches and composite our renders to make them look photo real.  Let's talk about building and sourcing your 3D characters. In our case, we started from an

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_001.jpg

### Build - 3D characters and environments [2:44]
**Transcript:** existing 3D model to save us some time on the first version and start right away with a rig.  But we did make some major changes to the 3D model by creating a custom helmet to match the  original concepts and references, and we completely replaced the materials and textures and created  our own in Substance Painter. Now most people skip over this super important step. Look development.  Once you've created your textures in Substance Painter, your character isn't done just yet.  You need to preview your characters under real lighting conditions, and we want to stress test  the materials to make sure they'll hold up under any situation. The easiest way to do this is to  create a turntable. Put your character in the middle and set up some lights, and rotate your asset  around by 360 degrees, so you see every side of your object. Then do a second pass where you  rotate the lights. This will start to reveal if anything looks artificial or fake in your materials.  And if there's anything not looking right, just continue adjusting your textures and materials  until it looks true to life. Next, let's talk about motion capture and what it takes to get great

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_002.jpg

### Budget friendly Mocap options [3:44]
**Transcript:** results yourself. Now there's many different options for motion capture, ranging from completely  free by just using your webcam or your iPhone, all the way to dedicated motion capture studios,  which are tens of thousands of dollars per day. But if you're on an indie budget,  I would recommend Rococo. It's what we use to shoot the motion capture for this short,  and we use Rococo smart suits and smart gloves to capture the performance for our sword fight.  Now, why I went with Rococo is that we could capture two suits at the same time,  and by using their smart gloves we could actually get hand animation, which can be pretty tricky  and time consuming to do yourself, especially with characters holding swords and weapons.  Now if you want to jump into the action and make your own sci-fi films yourself, Rococo is awesome  enough to give every one of you watching this video a discount store wide. Just use coupon code  unreal vaffx at checkout, and you'll get an extra 5% off your entire order. I'll leave a link  down below for the bundle we used on this exact project. Now if you're using a Rococo system on set,

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_003.jpg

### The perfect motion capture workflow [4:42]
**Transcript:** all of the data is transmitted from the suits directly into Rococo studio, and it's connected  by using a Wi-Fi router. Now we're not using that for internet, modern day routers are insanely  fast at sending data between devices. The easy way to get started in Rococo studio is by creating an  actor profile for each actor wearing a smart suit. Here you can enter in the height for your actors,  and pick whether they're male or female body types, and you can specify any measurement so your  skeleton perfectly matches your actor. We created our two actor profiles, and then when we created  a new project, you simply add these actors into your scene, and you connect your smart suit and  smart gloves. We started every single take by having one of our actors clap their hands so we could  align the motion capture data with the video and audio tracks. And to keep things organized,  we created a folder for each setup and a take number for each attempt. In between each take, we would  recalibrate our motion capture suits to get the best results possible. Just press the recalibrate  button at the top of Rococo studio, and your actors just need to stand still with their hands  by their side for three seconds. So here's some raw behind-the-scenes footage to take a look at how  every take would start. Yeah, we're on a take four. Okay, and recalibrating.  And mocap rolling.  And then we would start recording each performance.  And you get a immediate result, and you can tell whether it's going to work or not.  This simple naming process really kept things organized and simple at the same time.  On set, we also had a live action camera capturing reference footage at all times.  This way, we always had footage to look back at so we know what was really happening in real life  in case there were any errors in our motion capture. Now, if you want your shoot to go smoothly,  you need to anticipate all the problems that could happen beforehand. One issue we faced is after  one hour or so of recording, Rococo studio would slow down and our characters would stutter.  It says, no time to panic. The easy fix for most of these issues is simply restarting every part  of your workflow. In our case, I just had to restart my laptop itself, but I went through the  entire chain by restarting my laptop, the router, and all the Rococo suits to make sure everything  was working correctly. When troubleshooting, you're really just trying to find that one broken  link in the chain. And another pro tip is to bring batteries. You want an external battery to  make sure the suits last as long as possible so you can keep recording throughout an entire day.  Now, before we export this data out of Rococo studio, there's one step that most people skip over  which totally ruins their motion capture data. And that's because you need to do a pass of motion  capture cleanup before we export our animation. Here in the timeline, if you look on the very right  side, you can add filters onto the animation data. And we use these three filters every single time.  The first one is locomotion. Now, this filter isn't just important. I would say it's  absolutely necessary. And to see this in action, I'm going to press on this little gizmo button  so I can preview these filters in the viewport. If I zoom in closer here, these green and blue bars  are telling Rococo when our actors' feet are planted on the ground. If I zoom in here a little  bit closer by expanding on this timeline, let me press play and you can see the different feet  activate when they're planting on the ground. Now, the more accurate you can be with this,  the more accurate your motion capture will be. This green bar right here is signaling that our left  foot is planted on the ground. If I scrub back and forth here, I can actually see that our left foot  begins to drift left and right. And that's because we don't have the blue bar active when it should be.  So if I drag this blue bar to the right and then I press on process changes, that reduces the  drift on our back foot. Now, don't worry, this isn't a fully manual process. Rococo will do its  best guess and do a first pass at placing the left and right feet. You just want to go through  the entire timeline and make sure it's accurate and adjust each step by dragging these bars left  and right. If you don't do this, your feet won't be firmly planted on the ground and your characters  will be slipping left and right like they're on an ice rink. And it's totally unconvincing when  you bring that data into Unreal. If I want to switch between characters, I can just use these tabs  on the bottom left by switching between HPW, which is our yellow character or our blue character.  And we can preview the gizmos for our filters there. Now, the next most helpful filter is Drift Fix.  If I preview this gizmo, this tool is really easy to set up. You're just going to define the start  and end position of your character to help nudge our characters into the right world space.  Now, Rococo suits are using sensors inside of the motion capture suit to capture the speed and  rotation of each joint. High-end motion capture systems will use cameras so that all the data and  characters it's capturing all share the same exact 3D world. Now, we don't get that advantage with  Rococo and that's why we can adjust the start and end positions to change the trajectory of our  character. Now, in our case, the way we made this super simple is that we started each take with  our characters standing left and right of one another. And we use our reference footage to make  sure we're starting our Rococo models in the right 3D space. Again, if you need to adjust this,  you can just change that start position by dragging it left and right and pressing Process Changes.  The rest of the filters are helpful for smoothing out your data, like reducing the toe bend  with the toe bend filter or by using the foot iK system to recalculate your legs, which might  give you a better result. Then, once you've processed all your changes and you've watched through and  have some great motion capture data, that's when we can start to export our animations. To do that,  just go on the bottom right and we can use the X-Porter. And we'll export our data as an FBX file  with all the data included and we can select what skeleton we want. Now, if you use the mix-of-most  skeleton, you can automatically use the one-click control rig with your character. Otherwise, you can  use the Rococo Newton skeleton and your frames per second is set by your project. Then, just press  export. Then, you just have to go through every single take, which it does add up, it can take a while,  but it's totally worth it because we'll get clean, accurate motion capture data ready to use inside  of Unreal. Then, you can import your animations and the Rococo character itself into Unreal. The first

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_004.jpg

### Copy your animation to new characters [11:03]
**Transcript:** thing I did was I took the Rococo animations and I put them inside of the environment. Then,  I would add a sword onto the character and set up a camera so I could start thinking of new  angles and interesting shots even with this basic character. But, if you want to transfer your  Rococo animations onto your character, the next step is retargeting. We need to retarget the  animations from our Rococo rig to our character rig. So, I imported all of my characters and  animations into Unreal, including the Rococo skeleton character, and then I created retargeting  assets for both characters. This way, I could preview all those animations on our samurai characters,  and even before we had our finished model and our finished textures, I could preview the animations  on the final rig. Now, once our motion capture is imported and we've done our first pass of retargeting

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_005.jpg

### Filmmaking cycle on Unreal Engine 5 [11:52]
**Transcript:** animations, that's when the filmmaking cycle begins. We'll start creating cameras and rendering  our shots, then dropping those into our edit, and then jumping right back into Unreal to adjust and  animate our characters in camera. And we'll do this for every single take that has an interesting  performance. Now, the goal at this stage isn't just to look at your motion capture data, it's to  assemble your first edit. In filmmaking, if you don't have an edit, you don't have anything.  We need to build a timeline with video and audio, and the way to do that is to render out our motion  capture data through a camera. So, the typical setup is I would add both characters into sequencer,  then I would find motion capture performances that are interesting and assign those takes onto each  character and align them in the center of my environment. Then I would create multiple cameras  with different focal lengths. Typically, I'll create at least one wide shot, which would have a focal  length of 20 to 40 millimeters, and then I would create a close-up for each character, and for the lens,  you something between 50 and 150 millimeters. Then, I'd try to find one special moment and create a  camera just for that. Maybe there's a sword swing with lots of weight in momentum, and when you're  zooming around in your 3D world as you let your animations play, it's really easy to get inspired  and find new camera compositions and ideas on the fly. Then, I would use look at tracking, so your  camera can always follow the action. The goal here isn't to have a perfect camera move right away.  It's to get your first camera move, so you can make your first render and block in your movie  in your editing timeline. But one pro tip is I always try to picture what it would take for a  real camera person to hold a heavy camera on set, and I try to imagine how you would have to pull  this off in real life. As soon as you start moving your camera too fast or in unrealistic ways,  it's the fastest way to take your audience out of your film. Then, I would load all these up into  movie render queue and render out all of these sequences using the Playblast QuickTime preset.  To make fast renders, that render out as a .mov file that I can drop directly into an editing timeline.  With this preset, you can render long takes that are 30 seconds or a few minutes long,  and it shouldn't take that long to render. You can always lower your output resolution as well,  if you want it even faster render too. Another pro tip is you can add a burn-in, which is just  some text that you'll include in your render. That would include data like the frame number or the  name of your sequence. This will make it really easy to jump back and forth between your edit and  your level sequences in Unreal. All you need to do is add this burn-in option to your render  configs, and this will automatically be added to your renders. Then once you've rendered out a couple  of takes, we can take all those renders into your editing software, like Adobe Premiere or Resolve.  Now again, the reality is you don't have a film until you have a timeline with video and audio

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_006.jpg

### Editing your Animated Film [14:48]
**Transcript:** together, and that's why our goal is to get there as fast as possible. Now because we rendered out  these really long takes, when we drag in our renders, it's just like getting footage from onset.  You can bring in each take, watch through the footage, and clip out any selects or highlights  from the cool moments that you see, and assemble the best ones together. And it's super important to  bring in basic music and sound effects as early as possible too. In our case, we were making a  music video, so we had a soundtrack that we could start pacing our shots to. Now I never expect this  first version to be perfect. It's just your first draft, but once you find some camera movement that

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_007.jpg

### How to Edit + Improve Your animations [15:21]
**Transcript:** you're happy with, and you find a nice flow and pace to your film, you can jump back into Unreal and  make adjustments. Where we'll improve our animation, or come up with new ideas and adjust our animation.  Once you've decided on the right camera moves and frame ranges, we can lock our edit and improve  our animation and motion capture inside of Unreal by using control rigs. Using the same exact  workflow we used before. We'll start out with our animation clips, and then we would right click  on our asset, and bake this animation onto a control rig. Then we'll use additive tracks and the  curve graph editor to perfect our animation. And then the cycle continues. Keep watching your edit,  and update your cameras, and character animation until you have a version of your edit that has the  right pace and flow between each shot. At this stage, just focus on the composition and the flow  across your entire film. Once everything is locked, only then should you move on to the next step,

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_008.jpg

### Adding Lighting + FX in cinematics [16:16]
**Transcript:** lighting and effects. It's important to save this step until the end, and I honestly wouldn't  worry about lighting or effects whatsoever until you have a first draft of your edit.  Lighting will change the mood of your film, but ultimately it won't change the story. So there's  no point in lighting before the camera and animation has a great first pass. Because if you end up  moving the camera, your lighting will look totally different. At any point, you can press play and drag  your lights across your scene, and I really like this method of finding new ideas and new lights  in a really interactive way. And from this point forward, filmmaking in Unreal is a very iterative  process. Keep improving your shots and improving your film one version at a time. On War of Being,  we didn't finish our character assets until the very end. We continued updating the cloth,  the helmet, and physics assets as we went. And anytime there was an error in our render, we would  update that physics assets, and now we have the improved version for the next shot too.  And when you go to make your final renders, the only thing that changes in the end is you'll  increase your render settings and use a higher quality render preset, and finish off your visual  effects shots by compositing your final image by using the one click compositing template.  So that's the entire workflow when making films and animations with motion capture.  Even if you use another MoCAP system other than Rococo, the workflow will stay the same once you  load all your animations into Unreal. So keep these steps in mind and use this workflow as you're  planning your next film. If you want to jump into the action and make your own sci-fi films like  this yourself, Rococo is awesome enough to give every one of you watching this video a discount  store wide. Just use coupon code Unreal VFX at checkout and you'll get an extra 5% off your entire  order. So if you're new to Unreal or you've struggled learning it in the past, don't worry. I'll give  you my entire filmmaking toolkit inside of Unreal Fundamentals. My course that'll take you from a  complete beginner to making your own sci-fi films and action scenes in Unreal 5. It's on sale right  now at Unreal for VFX.com slash fundamentals. Otherwise, press subscribe down below and click here  to go behind the scenes and see how we tackle the lighting and environments for the Samurai sword fight  that by step. I'll see you next time. Peace!

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_009.jpg


---

## Structured Notes

### Core Technique
End-to-end indie filmmaking pipeline using Rococo inertial mocap suits → UE5 Sequencer → editing → iterative camera/animation refinement. Four stages: Build (characters + environments + look dev turntable) → Mocap (shoot + Rococo Studio cleanup: Locomotion filter + Drift Fix) → Filmmaking Cycle (cameras + MRQ Playblast renders + editing → Control Rig improvements) → Lighting/FX. Key philosophy: get to a rough edit ASAP; never light until camera/animation is locked.

### Summary
18-minute Josh Toonen tutorial documenting the full mocap filmmaking workflow used to produce a samurai sword fight short (two actors, Rococo suits + gloves). Covers: Look Dev turntable method for stress-testing materials; Rococo smart suit setup (actor profiles, WiFi, recalibration between takes, clap-sync); Rococo Studio cleanup (Locomotion filter for foot planting — CRITICAL, Drift Fix for world-space trajectory); FBX export; UE5 import + IK retargeting to custom characters; Sequencer filmmaking cycle (cameras + MRQ Playblast renders + editing timeline); baking mocap to Control Rig for cleanup; iterative lock-then-light workflow.

### Key Steps
**Stage 1 — Build:**
1. Source/create 3D character model → custom materials in Substance Painter
2. **Look Dev Turntable** (critical step most skip):
   - Place character center scene; add lights; rotate character 360° (see every side)
   - Second pass: rotate the lights instead (reveals artificial-looking areas under different lighting angles)
   - Fix any materials/textures that look fake; repeat until fully photorealistic

**Stage 2 — Mocap (Rococo):**
1. **Actor setup** in Rococo Studio: create actor profile per actor (height + male/female + measurements)
2. Create project → add actors → connect smart suit + smart gloves for each
3. Folder per camera setup + take number naming (keeps data organized)
4. Start every take with a **clap** (audio-visual sync reference for matching mocap to video)
5. **Recalibrate** between takes: press Recalibrate → actors stand still, hands by sides, 3 seconds
6. Reference camera rolling at all times on set (fallback if mocap has errors)
7. **Troubleshoot stuttering** (1hr+ sessions): restart laptop → router → all suits in chain order

**Stage 2b — Rococo Studio Cleanup (DO NOT SKIP):**
1. **Locomotion filter** (NECESSARY):
   - Green = left foot planted; Blue = right foot planted
   - Drag bars to correct timing; press Process Changes
   - Prevents ice-rink foot-drift sliding
   - Rococo does a first-pass guess; manually verify throughout full timeline
2. **Drift Fix filter**:
   - Set start/end world position for character (reference footage helps)
   - Corrects trajectory drift (inertial sensors don't share a 3D world like camera-based mocap)
3. Optional: Toe Bend filter; Foot IK (recalculates legs — may give better result)
4. Export as FBX via X-Porter:
   - Skeleton: **Mixamo skeleton** (enables one-click Control Rig in UE) OR Rococo Newton skeleton
   - FPS: match project
   - Export all takes individually

**Stage 3 — Import + Retargeting in UE5:**
1. Import Rococo skeleton + all animation FBX files into UE
2. Place Rococo character in environment → add props (sword) → set up basic camera → start framing shots immediately
3. Create **IK Retargeter assets** for source rig (Rococo/Mixamo) → target rig (custom character)
4. Preview all takes on final character rig (can do this before final textures are done)

**Stage 3b — Filmmaking Cycle (iterative):**
1. Add both characters to Sequencer → assign mocap takes → align in environment center
2. **Camera setup**:
   - Wide shot: 20–40mm focal length
   - Close-up per character: 50–150mm
   - One "special moment" camera for key action
   - Enable **Look At Tracking** → camera always follows action
3. **MRQ → Playblast QuickTime preset** (.mov): fast renders of full takes (30s–few minutes); lower resolution if needed; add **Burn-In** (frame number + sequence name → makes NLE sync easy)
4. Import renders into **Premiere or Resolve**: assemble edit with music/SFX ASAP; cut selects from long takes
5. Iterate: camera adjustments → re-render → edit refinement → loop until flow is right
6. **Animation improvement** (after edit is locked on frame ranges):
   - Right-click animation clip → **Bake to Control Rig**
   - Use additive tracks + Curve Editor to refine specific moments
   - Keep cycling until animation and cameras are perfect

**Stage 4 — Lighting + FX (LAST, after edit is locked):**
1. Press play → drag lights around scene interactively to find moods
2. Iterative per-shot lighting improvement
3. **Final render**: increase MRQ quality settings + high-quality preset + one-click compositing template for VFX shots

### UE Systems / Blueprints / Settings
- **Sequencer** — add characters as actors; assign animation takes per character; align in scene center; multi-camera setup
- **Level Sequences + Camera Cuts track** — per-shot camera setups with Look At Tracking enabled
- **Look At Tracking** — camera component constraint; follows target actor automatically; keeps action in frame during early filmmaking cycle
- **MRQ → Playblast QuickTime preset** — fast .mov renders for editing pipeline; long take output; Burn-In overlay (frame number + sequence name)
- **MRQ Burn-In** — add burn-in option in render config; displays frame number + sequence name on render; enables fast jumping between NLE and UE sequences
- **Bake to Control Rig** — Sequencer right-click animation clip → Bake to Control Rig → select rig type; converts mocap take to editable Control Rig keyframes
- **Additive tracks** — Sequencer animation layers; add bone overrides on top of baked animation
- **IK Retargeter** — source rig (Rococo/Mixamo) → target rig (custom character); create retargeting assets in UE; preview animations on final character before textures are done
- **Look Dev Turntable** — character center scene, rotate asset 360° under fixed lights, then rotate lights under fixed character; stress-tests material authenticity
- **Rococo Studio** — Rococo's capture software; WiFi data routing; actor profiles; Locomotion filter; Drift Fix; FBX X-Porter export; real-time preview per take
- **Locomotion filter** (Rococo) — foot-plant detection; green = left, blue = right; manual bar adjustment; REQUIRED to prevent foot drift/sliding
- **Drift Fix filter** (Rococo) — world-space start/end position correction; compensates for inertial sensor drift over time; use reference footage for placement

### Difficulty
Intermediate. Requires Rococo mocap hardware + Substance Painter for full pipeline. UE portion (Sequencer, MRQ, IK retargeting, Control Rig) is documented elsewhere; this tutorial provides the production philosophy and mocap-specific workflow.

### UE Version
UE5 (UE5 Sequencer, MRQ, Control Rig, IK Retargeting — no specific minor version mentioned)

### Tags
mocap, motion-capture, rococo, workflow, sequencer, retargeting, control-rig, filmmaking, cinematics, indie-production

---

## Related Entries
- `motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter.md` — Dean Yurke bone matching for root-motion blending; Layered FK Control Rig
- `make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta.md` — beginner filmmaking pipeline; Sequencer + MRQ + camera; no mocap hardware required
- `motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahua.md` — Move.AI-based mocap cinematic (if present)
- `metahuman-realtime-animator-best-practices-unreal-engine-animation-hub.md` — webcam face capture; alternative to mocap suits for facial animation
- `live-link-hub-tips-unreal-engine-animation-hub.md` — mocap streaming via Live Link Hub; body + face combined; recording
