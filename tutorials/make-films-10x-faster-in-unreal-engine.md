---
title: Make Films 10x Faster in Unreal Engine
source: YouTube
url: https://www.youtube.com/watch?v=RBtlrRP2fvs
author: Josh Toonen
ingested: 2026-06-17
ue_version: "5.x"
tags: [decals, materials, environment, virtual-production, sequencer, cinematics, quixel, fab, caustics, flipbook, character-attachment, animation, ue5]
extraction_status: complete
frames_dir: tutorials/frames/make-films-10x-faster-in-unreal-engine/
frame_count: 6
---

# Make Films 10x Faster in Unreal Engine

**Source:** [YouTube](https://www.youtube.com/watch?v=RBtlrRP2fvs)
**Author:** Josh Toonen
**Duration:** 20m45s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### What Unreal does that Blender doesn't - Decals! [0:00]
**Transcript:** Why is building environments so much faster in Unreal Engine?  It's because Unreal can do something that blender in Maya can't.  You can save hours and start making better looking environments  with a simple drag and drop.  All you need is this one technique, decals.  If you can drag and drop, you can text your any 3D model in seconds  using the methods I'm about to show you.  So you can go from a beginner, advanced to pro  by the end of this video.  I'll show you three easy ways to use decals  to build your own virtual film sets and environments  that I learned on set on the virtual production of Star Trek Discovery  and Avatar the Last Airbender.

**Frame:** tutorials\frames\make-films-10x-faster-in-unreal-engine\frame_000.jpg

### Level 1: Free Decals for Cinematic Environments [0:30]
**Transcript:** Starting out with level one, downloading high-quality decals  for free and texturing any scene in seconds.  But first off, what is a decal?  Well, if you've ever played Call of Duty  and seen a bullet hole in the wall, that's a decal.  It's a texture that you can apply over any surface instantly.  And they're great to arch-direct any scene  and tie together different 3D objects in your environment.  And the best part about Unreal is that you can download  high-quality decals for free by just opening up your content  browser by pressing Control-Space and opening up FAP.  From here, just find any asset created by Quixel  and then we can navigate to all the assets that are published  by Quixel and we can download any of these high-quality  assets for free.  Just make sure to sort by price and only show the free assets.  And then on the left hand side, you'll  see a separate menu just for decals.  Some of my favorite ones are under the damage  and grunge drop down.  We can use these for storytelling with bloody handprints  or just add grunge and leakage to any surface.  You can even fake some three-dimensional details  with these concrete cracked decals, which  will look like they're c...

**Frame:** tutorials\frames\make-films-10x-faster-in-unreal-engine\frame_001.jpg

### Level 3: Making Bullet hole Decals in Photoshop [2:50]
**Transcript:** Let's take this to the next level and let me show you how  to make your own custom decals yourself.  Let me show you how we can make these bullet hole decals  from scratch.  So let's kick this off in Photoshop.  I found this bullet hole image off of Google images.  And from here, let's process this to turn it into a decal.  Now in order for this to work correctly,  we need to make sure our background is transparent  so we can move that image around and it'll be isolated  against the background.  Now in Photoshop, you can see transparency.  But what I'm real is looking for is the alpha channel,  which is just a black and white mask,  which is telling unreal what's transparent and what's opaque.  Now this works as a white value will be completely opaque  so nothing will be seen through it.  Where a black value is completely transparent  so it won't show up in your final decal.  Then everything in between all these gray values  on blurry edges will be semi-transparent.  So the easiest way to do this is just to use  the object select tool and click and drag over the object  you wanna punch out.  This will create a selection around our object  and then in your layers panel,  just press ...

**Frame:** tutorials\frames\make-films-10x-faster-in-unreal-engine\frame_002.jpg

### Level 5: Attach Decals to Characters [6:45]
**Transcript:** We're not done yet.  Let's take this to the next level  by attaching our decals to characters and animate them.  In this example, let me show you how we can make  this lightsaber impact streak across this character's back  by breaking down this project file  that's included in Unreal Fundamentals.  But the way this birdmark is created is actually  with a decal that we could drag up and down  and art direct just like our bullet impacts.  First off, to create this birdmark texture,  I just used the brush tool and painted this rough jagged shape  to imitate the birdmark of a lightsaber  that I exported it with a transparent background  and set up the material in the same way we did earlier.  But where this gets interesting  is how we can apply a decal onto a character.  Let me just drag and drop this decal into our scene  and I'll scale it down and rotate it towards our character  and we can line it up here.  But right now it's not sticking to our character  and we need to animate it so it only appears  after he slices through the enemy.  So to attach this to a character,  all we need to do is in our outliner,  we'll select our decal and then we can click and drag it  onto any charact...

**Frame:** tutorials\frames\make-films-10x-faster-in-unreal-engine\frame_003.jpg

### Level 7: Add Caustics Animations to Decals (Blade Runner example) [9:11]
**Transcript:** So now you know some advanced techniques  to add impacts like this into your cinematics.  But let's take this to another level  and let me show you some more ways to animate your decals.  Like in this example from Blade Runner.  Decals don't just have to be static textures.  We can add animation into our materials  to create water caustics just like this effect  from Blade Runner 2049.  And because it's a decal,  we can move these around left or right  and art direct them along with any other part of our lighting.  So let me show you two simple but super effective techniques  to add animation into materials just like this.  Now for the texture,  I created this caustics material inside of Nuke,  which is just a simple noise pattern.  And I adjusted the edges so that it tiles perfectly.  And this is super important later on.  So let me open up this new material.  And before we change it into a decal,  let's keep it as a standard opaque surface for now.  And then I'll press control space  and drag in our texture.  Then I'm gonna drag off the RGB channel  and we're gonna multiply this by a color,  which will allow us to tint it to that cool orange color.  Then we'll plug it into the ba...

**Frame:** tutorials\frames\make-films-10x-faster-in-unreal-engine\frame_004.jpg

### Level 10: Secret Trick to Animate Decals with Motion Graphics + Footage [14:31]
**Transcript:** But there's one more technique you have to learn  if you want to start using decals just like the pros.  Let me show you this awesome material setup  to add animations like this into your decals.  I learned this back on War of Being  when we were working on this idea  where the scribe character was casting spells from her temple  and out on the battlefield,  I was trying out this idea of visualizing these spells  cast into the middle of their arena.  So I found a great method to create a decal  that we can move anywhere across the arena  that's animated all in real time.  Plus once you understand how all these systems work together,  we can actually keyframe the animation of this spell  directly inside of sequencer.  So we can adjust the timing at the start.  And by the end, we'll see a draw now  and stick to the final animation.  So let me show you how this works.  Here's a look at the entire material setup  and I think you'd be surprised that it's actually pretty simple.  All of the animation is actually driven by a single node,  this flip book material function.  You can make this yourself by right clicking  in any material graph and just typing in flip book.  Flip books are rea...

**Frame:** tutorials\frames\make-films-10x-faster-in-unreal-engine\frame_005.jpg


---

## Structured Notes

### Core Technique
Decals as the primary speed-up tool for UE cinematic environments — three escalating levels: free Quixel/FAB decals → custom Photoshop alpha decals → animated decals (caustics, flipbooks) attached to characters and keyed in Sequencer.

### Summary
Josh Toonen (virtual production veteran — Star Trek Discovery, Avatar: The Last Airbender) teaches a progressive 3-level decal workflow to drastically speed up environment building and VFX in UE. Level 1: drag-and-drop free Quixel decals from FAB (grunge, damage, cracks). Level 3: create custom decals in Photoshop using alpha/transparency. Level 5: parent decals to characters in the Outliner and keyframe visibility in Sequencer (e.g. lightsaber burn mark). Level 7: animate decals with tiling Panner-driven caustics material (Blade Runner 2049 reference). Level 10: drive decal animation from video footage / texture atlases via the Flipbook material function, timed in Sequencer (spell casting effect from War of Being virtual production).

### Key Steps
1. **Free decals**: Ctrl+Space → FAB → filter Quixel + free + Decals category → drag onto any surface; best categories: damage, grunge, cracks
2. **Custom Photoshop decal**: find/paint image with transparent BG → use Object Select to isolate → export PNG with alpha → import to UE → create Material with Blend Mode: Deferred Decal → Texture Sample RGB → Base Color; Alpha → Opacity Mask
3. **Attach decal to character**: drag decal actor onto character in Outliner to parent it → scale/rotate to fit → add Sequencer track → keyframe visibility to match action timing
4. **Animated caustics**: create tiling caustic texture (Nuke or PS) → Material Graph: Texture Sample + **Panner** (UV animation speed) → multiply by color → plug into Emissive on Deferred Decal material; set material to Translucent + Deferred Decal
5. **Flipbook decal**: right-click Material Graph → search "Flip Book" material function → connect sprite sheet texture atlas → set playback rate → export from Nuke/After Effects as sprite sheet → keyframe start frame in Sequencer to sync spell/impact animation

### UE Systems / Blueprints / Settings
- **Deferred Decal** — material Blend Mode that projects texture onto any underlying surface
- **FAB / Quixel Bridge** — free high-quality decal library accessible via Content Browser (Ctrl+Space)
- **Material Graph nodes**: Panner (UV animation), Flipbook material function, Multiply, Texture Sample, Emissive/Base Color/Opacity Mask inputs
- **Sequencer** — keyframe decal visibility, material parameter animation, flipbook start frame
- **Outliner parenting** — drag-drop decal actor onto character to attach/follow skeleton

### Difficulty
Beginner → Advanced (leveled 1/3/5/7/10 structure)

### UE Version
UE5 (FAB integration indicates UE 5.4+)

### Tags
decals, materials, environment, virtual-production, sequencer, cinematics, quixel, fab, caustics, flipbook, character-attachment, animation, panner, ue5

---

## Related Entries
- Materials / rendering doc entries (Panner, material functions)
- Sequencer animation tutorials (keyframing, cinematics)
- Boundless Entertainment Lighting / VFX tutorials
