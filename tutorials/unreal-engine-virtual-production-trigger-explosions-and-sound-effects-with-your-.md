---
title: Unreal Engine Virtual Production: Trigger Explosions and Sound Effects with your Keyboard (Tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=5cpjK7kKASU
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-06-23
ue_version: "UE5"
tags: [level-blueprint, keyboard-trigger, niagara, vfx, sound, virtual-production, live-streaming, blueprint]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-virtual-production-trigger-explosions-and-sound-effects-with-your-/
frame_count: 5
---

# Unreal Engine Virtual Production: Trigger Explosions and Sound Effects with your Keyboard (Tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=5cpjK7kKASU)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 6m37s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro: Interactive Live Streaming in Unreal Engine [0:00]
**Transcript:** I wonder what will happen if I press this button.  Ah!  If you're into live streaming with Unreal Engine and you want to trigger events with your  keyboard, then look no further because I've got the video view where we go over level  blueprints.  Yeah!  So here we are in Unreal Engine and I'm going to go over this in more detail in a minute,  but here's quick overview for people that are familiar with Unreal Engine and level blueprints  just so you can see what I was using.  So I'm just going to go into the level blueprint editor, open level blueprints and then this

**Frame:** tutorials\frames\unreal-engine-virtual-production-trigger-explosions-and-sound-effects-with-your-\frame_000.jpg

### Overview of Level Blueprints for VFX Triggers [0:34]
**Transcript:** is the one that I made and so it's very simple.  So we've got a trigger.  So we get a keyboard here, keyboard input and then we go and activate something and we're  going to activate a Niagara component and we're going to grab this Niagara explosion  from our outliner so you just navigate to it and then just drag it in and then turn on  reset so that you can press the button multiple times and then right at the end we've got  a little sound spawner there.  So there's a quick overview so make sure you give it a good like and see you next time.  In the meantime, I'm going to show you how we're going to create one of these from scratch.  So I'm going to just close this window and pretend that here we are, hi, here we are

**Frame:** tutorials\frames\unreal-engine-virtual-production-trigger-explosions-and-sound-effects-with-your-\frame_001.jpg

### Setting up a New Level Blueprint from Scratch [1:17]
**Transcript:** in the Unreal Engine and I'm going to create a level blueprint.  So all of the levels come with a level blueprint and they're just basically emptied to begin  with and you access it by going over here to these three little dots and then you say,  open that up and they say open level blueprint and here's what I made earlier but we'll pretend  it's over here so it will kind of look like this.  But so you don't actually have to do anything, you just go over here, I'm going to recreate  this.  So we go over here and we hit the right mouse button and then we look for keyboard, oh here

**Frame:** tutorials\frames\unreal-engine-virtual-production-trigger-explosions-and-sound-effects-with-your-\frame_002.jpg

### Mapping Keyboard Events to Niagara Particle Systems [1:45]
**Transcript:** it is, keyboard events.  And then so you pick any of these so it's like any of the keyboard buttons and then we're  going to pick this one here.  Let's go for number four.  So there's our keyboard event and then from here we're going to drag this little pin  out and you pull that open and then in here you search for it's called an activate but  watch this if I try and go activate and I'm looking for activate.  It's not actually, this will list you everything that's available but by default I think context  sensitive is on.  So turn that off otherwise you wouldn't be able to find what you're looking for and this  is what I want, activate you see in context sensitive sensitive, I don't know why it won't  list it.  So turn that off and then you click on activate and that activates an activate node and then  here it's looking for a target and the target we want is a Niagara component system so  you click on there, drag this out and then look for get Niagara component.  There it is.  And then we want to add in our Niagara system so whatever particle system you've made,  put it into your environment and then find it in the outliner and then you basically  took me ages to wear this out but you find it, you grab it and then you drag it into here.  So here it is inside your event graph and then you connect it by just dragging it onto  the target like that and then at this point you can actually, we could actually make this  work but like I said in the quick overview, if you turn a reset on then that will let you  do multiple key press.  If you don't have that on you've got to wait for the Niagara event to finish and then  you can hit the keyboard again so it's not as exciting.  So turn that on and at this point I'm just going to, I haven't got the sound yet but  I'm just going to say compile and then what have we got?  We've got a keyboard for, I'm going to move my window over a little bit and open this  up just so we can see if I click on here and so we're on keyboard number four and you  can change this by clicking under that and then going into keyboard and then picking  your favorite key so let's go for D for D in it, well there they are.  So if you press D now it'll trigger this, that's kind of a boring one the engine so let  me find one of the explosions.  Let me just go and lower this and then go to confetti, there we are, let's put confetti  there instead.  So I'm just going to select that one, delete it, take my confetti, put it into the target,  hit compile, hit save and now if I go into play mode it'll kill my video but if I go  into play mode there we are and now I have to activate my video camera, I know.  So these are things to know if you're doing that.  If you're using, I'm going to go over this in a different video, I had to use your webcam  for live streaming but if you are in there and when you press play and engine it turns  off so you have to go and reactivate it like this and then it'll work again.  Anyway let's go and make this big screen, press in here and then press F11 right now,  click in here so this window is now active and I'm going to press D.  Hooray!  Now I had to make the sound myself because we haven't connected the sound yet so we're  going to come out of here.  So we're back in Unreal and I've come out of play in engine mode and I'm just playing  my sequencer and I'm going to go and open up our level blueprint and then over here

**Frame:** tutorials\frames\unreal-engine-virtual-production-trigger-explosions-and-sound-effects-with-your-\frame_003.jpg

### How to Spawn Sound Effects at Location [5:13]
**Transcript:** now we're back in here I'm going to go and look for a spawn sound at location.  Spawn sound at location and so this now will look for a sound asset so we're going to  open this up and then look for a bang sound.  What's that sound like?  We'll find out and then again compile this then go back into play in engine and I'll  have to reset my camera but it's be worth it.  Alright so we're full screen mode and we're going to now press our keyboard.  Are you ready?  3, 2, 1.  It's a bit loud for confetti but it's super confetti and that's what you get with  Unreal.  Alright so that's a lot for now and I will go over another video how to set up this  live virtual production system using your webcam so you can have some fun and I'm going  to make it simple, simple in Unreal.  As simple as I can so that you can kind of get you into playing around with virtual  production in Unreal Engine so make sure you subscribe so that you won't miss that  video and in the meantime I'm going to have some fun.  Good egg.

**Frame:** tutorials\frames\unreal-engine-virtual-production-trigger-explosions-and-sound-effects-with-your-\frame_004.jpg


---

## Structured Notes

### Core Technique
Level Blueprint keyboard trigger → activate Niagara VFX + spawn sound. No Sequencer, no animation tracks — pure runtime Blueprint triggering. Designed for live virtual production / live streaming where operator hits a key to fire a practical-style VFX event. Niagara Reset = true allows repeated triggering from same key without waiting for system to finish.

### Summary
6m37s Dean Yurke casual Level Blueprint tutorial. Goal: press a keyboard key during Play in Engine to trigger a Niagara explosion/confetti effect + play a sound. Setup: Level Blueprint → Keyboard Event node → Activate node (turn off Context Sensitive to find it) → Get Niagara Component → drag Niagara actor from outliner into BP graph → connect; enable Reset. Add sound: Spawn Sound at Location node → pick sound asset. Compile + Save → Play in Engine → press key → VFX + sound fires. Notes: in PIE mode webcam turns off (live streaming concern); F11 for fullscreen PIE.

### Key Steps
1. Place Niagara VFX actor in scene (explosion, confetti, etc.) and note its name in Outliner
2. Toolbar → Blueprint menu (three dots icon) → **Open Level Blueprint**
3. In event graph: **right-click → Keyboard Events → pick key** (e.g., "4", "D") → Keyboard Event node placed
4. Drag from Pressed pin → release → search for **Activate** → ⚠️ disable **Context Sensitive** if not found → click Activate
5. From Target pin on Activate node → drag → search **Get Niagara Component** → connect
6. In Outliner: find Niagara actor → drag into Blueprint graph → connect to Get Niagara Component's Object pin
7. On Activate node: set **Reset = true** → allows repeated key presses without waiting for VFX to finish
8. Hit **Compile** → **Save**
9. To add sound: after Activate → drag from Exec out → search **Spawn Sound at Location** → connect; set Sound = desired SoundAsset
10. Compile + Save → **Play in Engine (PIE)** → click inside viewport to make window active → press bound key → VFX fires
11. Fullscreen PIE: press **F11** while PIE is active

### UE Systems / Blueprints / Settings
- **Level Blueprint** — world-scoped Blueprint; accessed via toolbar → three-dot menu → Open Level Blueprint; one per level
- **Keyboard Event node** — fires on key press/release/hold; find via right-click → Keyboard Events → pick key
- **Context Sensitive toggle** — must be disabled to find some nodes like Activate in Blueprint search
- **Activate node** — activates a component (including Niagara particle systems); Reset=true re-triggers without waiting
- **Get Niagara Component** — gets reference to Niagara component; drag Niagara actor from Outliner into graph to provide Object pin
- **Reset = true** — on Activate node; allows keyboard mashing without waiting for previous VFX to complete
- **Spawn Sound at Location** — Blueprint node; takes Sound asset + Location vector; plays 2D or 3D sound at world position
- **Play in Engine (PIE)** — required to test keyboard triggers; click viewport to focus window first; F11 for fullscreen

### Difficulty
Beginner. Minimal nodes; visual production entry-point.

### UE Version
UE5 (compatible with UE4 as well)

### Tags
level-blueprint, keyboard-trigger, niagara, vfx, sound, virtual-production, live-streaming, blueprint

---

## Related Entries
- `niagara-magic-effects-with-geometry-trails.md` — Niagara VFX systems
- `unreal-engine-masterclass-animate-environments-the-easy-way.md` — Niagara user parameters and environment VFX placement
