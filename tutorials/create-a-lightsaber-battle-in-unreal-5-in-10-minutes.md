---
title: Create a Lightsaber Battle in Unreal 5 (in 10 minutes!)
source: YouTube
url: https://www.youtube.com/watch?v=MWFpt3ZQ0zE
author: Josh Toonen
ingested: 2026-06-18
ue_version: "5.x"
tags: [animation, sequencer, cinematics, beginner]
extraction_status: complete
frames_dir: tutorials/frames/create-a-lightsaber-battle-in-unreal-5-in-10-minutes/
frame_count: 9
---

# Create a Lightsaber Battle in Unreal 5 (in 10 minutes!)

**Source:** [YouTube](https://www.youtube.com/watch?v=MWFpt3ZQ0zE)
**Author:** Josh Toonen
**Duration:** 11m52s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### You need characters in your film [0:00]
**Transcript:** If you wanna create films that you have to have characters,  I mean, a one single movie that you love  that doesn't have characters, it's impossible.  It doesn't exist, so it's impossible to avoid characters  when learning Unreal Engine for filmmaking.  And when you're first starting,  characters can be really daunting  because it puts all of the different disciplines together  for modeling, texturing, rigging, and animation.  And if you're not good at every single one of those steps,  you might be afraid to jump in.  Well, I'll show you where you can find characters of your own,  but also how to give them life and performance  without having to know animation.  What's up?  My name's Josh Tuner, and I'm a director and visual effects  supervisor, and I've spent the last eight years  working on Hollywood visual effects on movies  like Star Wars, Shazam, and Deadpool.  And last year, I was an on-set Unreal operator  at the world's largest LED volume working  on Avatar, the last Airbender.  So every single day I was using Unreal,  and then after that, I would spend my nights  and weekends trying to understand how to use Unreal Engine  to make films of my own without a huge budget  and ...

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_000.jpg

### Importing characters [1:13]
**Transcript:** animations together to create a performance  with characters in Unreal.  All right, let's show you the fastest way  for you to get 3D characters directly  into your Unreal scene so you can start animating them  right away.  And the best place to find that is mixmo.com.  So here they have a selection of a bunch of characters.

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_001.jpg

### Downloading Mixamo animations [1:30]
**Transcript:** They're not amazing, but they will absolutely do the trick  so we can just get our hands dirty with the animation system.  And here you can even upload your own 3D models and rig them.  So just go to mixmo.com, sign in, and go to the character  section.  So we have this big list of characters,  and then we're going to pick this character that's  Vanguard by T. Tune Young.  He's just on page one.  And so now that we have our character,  we can go over to the animations tab.  And we can start to see exactly what the animations  are going to look like transferred to this character.  The best tip I have here is just try  to find a pack of different animations.  So you can string many animations together  that are supposed to be working in the same timeline.  So to get this started, I'm going to start with the sword  and shield pack.  And all we have to do is hit download,  and all of the defaults are good.  And the best way to learn is not by watching,  but it's by doing it yourself.  So either start a brand new U project,  or I've included the project files I'm using here  as a free download down in the description.

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_002.jpg

### Importing characters [2:24]
**Transcript:** So download that if you're a beginner,  or if you just want to follow step by step.  So I've loaded up this project here,  and let's just import our character first and foremost.  So there should be an object called the name of the character,  Vanguard.  And then this is the FBX import box.  And the important things to know here  are the difference between a skeletal mesh and a skeleton.  So a skeletal mesh is what a character is called  inside of Unreal.  It's the mesh associated to the character.  The skeleton is the actual bones and the rig underneath.  So in this case, we need to create a brand new skeletal mesh  and a brand new skeleton because it's a new character.  So to start this, we're just going to go to skeletal mesh,  import mesh, we'll leave skeletal blank,  and we'll hit import.  And once this is imported, we should have our character.  So we have our skeletal mesh, we have our skeleton,  and now we need to start importing our animations.  So just to keep this organized,  I'm going to take all these textures and the materials  and put them in another folder,  and then we'll create a new folder called animations.  So now let's just select everything and drag this in a...

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_003.jpg

### Creating our Level Sequence [3:54]
**Transcript:** First we're going to create a level sequence called LS  underscore character and then we can just press enter  to open up sequencer because it's already selected.  And now we'll navigate back to our Vanguard soldier  in the content browser and just click and drag him into the viewport.  We still need to add him into our sequencer.  So we'll add a new track with the green plus sign.  And then at the very top of this menu,  we can add our selected actor.  And now if you hit the add animation button,  we'll see all of the different animations  that share the same skeleton.  Really quick, I prepared this before.  We're just going to take a lightsaber.  But it's literally just cylinders together  and I'm using an emissive material combined together  to just make a really simple lightsaber.  So we'll bring this in.  And it's actually really easy to parent things to objects  in Unreal and within sequencer.  If I show everything that's only in this level,  we'll have our red lightsaber in our Vanguard person.  And we'll just make sure both of them are set to movable.  And then we'll parent this to the right hand.  So we have this, the lightsaber shouldn't move.  And then when we add our fi...

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_004.jpg

### Assembling our animation [5:08]
**Transcript:** Let's add a death animation.  So we'll add this death to.  And this is a cool thing.  You can just overlap these and they will start to blend  in between.  They'll do like a soft blend.  And then you could even change the easing between those two.  I'll just give it a default for now.  You can see we can have a seamless blend  between our two animations on our guy right here.  So just to fill out the beginning here,  let's add in just a simple idle animation.  And we'll intersect that at the end.  All right, cool.  So we have our first character.  Now let's bring in our second one.  So now I'm going to control and drag this into here.  And this will automatically add our actor into sequencer.  And let's have him run up and do a couple  hack and slash things.  Let's give him his own lightsaber.  So right now we'll just duplicate that from the original one.  Let's go to the original red lightsaber.  Let's hit detach and let's add it to our Vanguard character.  We know we'll want it on his right hand.  So we'll grab that.  And then we can just zero out this transformation.  And it should snap right to his hand.  Just do a really simple 90 degree rotation  and slot that right into plac...

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_005.jpg

### How to use Motion Blending [6:24]
**Transcript:** and have our character travel forward into the world.  Well, we're going to have a problem.  Every time a new animation starts,  the character is going to teleport back to where it started.  So if we want our character to travel correctly  through the world, we want to right click our animation  and use the motion blending options.  This is how we can have our new animation start  where our last animation ended.  All we have to do is select what bone we want to match  in the previous animation.  And we just want to set ourselves  to the hips of the previous clip.  So now we've got our motion blending working.  And this is the key technique that we'll use  to string all of our different attack animations together.  So now we've blended sort of attack two and sort of attack three.  And we'll keep adding animations here.  Just remember at any point,  if you want to add in different animations,  use the animation editor to preview  all the different animations we've downloaded.  So now let's reposition our attacking character  so he slices right through the enemy.  We want to add a transformation track.  We have one here.  But now we can actually keyframe in the position.  So let's mov...

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_006.jpg

### Playrate of Animations [8:10]
**Transcript:** If we go to 0.5, it'll go half the speed.  So we'll probably want to slow down this sword  and shield attack by about 0.7.  So now by slowing that one down and kind of moving it around,  we can see that we've got these two guys  clashing their lightsabers together.  It's not perfect, but very quickly,  we can start to block in motions like that.  Just to finish this off, let's have him  running up at the beginning of this shot.  And then one thing that we want to do here  on our run animations, because this loops  and starts at one place and ends in another,  it makes it very difficult to string these animations together.  So one thing that we can do in the animation editor  is enable root motion.  So we do this, we'll lock our entire animation to the hips  and then we'll want to change this from reference pose  to animation first frame and that'll kind of fix  the angle that he's at.  We'll just make sure this force root lock  is checked as true.  We'll save that.  And now when we're back in our sequencer,  we'll just add this and we'll choose our root animation.  So what we're gonna do right here  is at the very beginning of this transition,  we're gonna make a transform key fram...

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_007.jpg

### Dealing with Run Animations [9:16]
**Transcript:** We really just need the location here.  And we're gonna hover over these, click and drag over these  and press the four key.  This is going to make it a linear key frame.  And again, you will understand exactly why in just a second.  So we have our foot here  and we can see that our foot shouldn't be dragging  across the ground like that.  So we're gonna move him back and X just a little bit.  We're gonna go and hit four again  and we'll see how this looks.  We can see the foot is still kind of sliding  and traveling around.  So one thing that we can do is let's just select  both of these key frames.  Let's go and hit our curve editor.  The X location yet again, so it shows up in our curve editor.  So we're gonna select our key frame here  and we're gonna hit this double right arrow here  and pick our pre-infinity options and go to linear.  And this is gonna make it so the curve  between our two key frames here gets extended  into infinity before our first key frame.  So this looks a little weird because our animation  is too slow.  We can see that he's like sliding backwards  as he's running forward.  He's kind of moonwalking.  So what we can do is we can just select this key fram...

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_008.jpg


---

## Structured Notes

### Core Technique
Beginner Mixamo character animation in UE5: importing and rigging characters via Mixamo, building a Level Sequence with motion-blended sword animations, using playrate to slow down attacks, enabling root motion, and attaching an emissive lightsaber prop to a hand bone.

### Summary
Josh Toonen shows complete beginners how to get a believable lightsaber battle into UE5 in roughly ten minutes using only free assets. Viewers learn to select and download Mixamo character packs, import them to UE5 with a new skeleton, create a Level Sequence, assemble sword and shield animation clips, use motion blending to chain attacks seamlessly, adjust playrate for dramatic slow-motion, enable root motion for locomotion animations, and parent a simple emissive lightsaber mesh to the character's hand bone. By the end, beginners have their first complete character animation sequence.

### Key Steps
1. Go to Mixamo.com → Characters tab → select "Vanguard by T. Chiu Young" → Animations tab → find the Sword and Shield pack → Download (FBX, default settings).
2. In UE5, import the FBX: Import Options → Skeletal Mesh = true; Skeleton = none (create new); Import = all assets.
3. Create a Level Sequence (right-click Content Browser → Cinematics → Level Sequence → LS_Character); drag the Vanguard character into the viewport; drag into Sequencer with + (Add Selected Actor).
4. Add animation track via the green + → Add Animation; select sword animations to build an attack combo sequence.
5. Parent lightsaber prop: duplicate a simple emissive cylinder mesh → set to Movable → drag onto character in Outliner → "Attach to Bone" → right_hand bone → zero transform.
6. Chain animations with Motion Blend: right-click animation clip → Motion Blend Options → Match Bone = pelvis/hips; the new animation starts where the previous one ended.
7. Slow attacks with Playrate: right-click animation clip → Properties → Play Rate = 0.7 (70% speed for sword attacks) or 0.5 (50% for extra dramatic moments).
8. Fix run animation with Root Motion: double-click run animation → Animation Editor → Enable Root Motion = true; Root Motion Root Lock = Force Root Lock = true; save. Back in Sequencer, add transform keyframes to manually drive root position.
9. Use Curve Editor to set keyframe interpolation on transform keys: select keyframe → press 4 = Linear for smooth root travel; pre/post infinity = Linear for looping.

### UE Systems / Blueprints / Settings
- **Mixamo FBX import**: Skeletal Mesh = true; Skeleton = new; Import Mesh = true; import all textures/materials
- **Level Sequence**: Right-click Content Browser → Cinematics → Level Sequence; 24fps; Camera Cut track optional
- **Motion Blend**: Right-click animation clip → Motion Blend Options → Match Bone = pelvis; aligns new clip to end pose of previous clip
- **Play Rate**: Right-click clip → Properties → Play Rate; 1.0 = normal, 0.7 = slow, 0.5 = half speed
- **Root Motion**: Animation Asset Editor → Enable Root Motion = true; Root Motion Lock = Force Root Lock = true
- **Bone attachment**: Outliner → drag prop onto character → Attach to Bone → right_hand bone; set Transform to zero after attach
- **Curve Editor**: Sequencer → Curve Editor button; select key → press 4 = Linear tangent; right-click → Pre-Infinity = Linear for loop extrapolation

### Difficulty
Beginner

### UE Version
UE 5.x

### Tags
animation, sequencer, cinematics, beginner

---

## Related Entries
- [[this-free-plugin-changes-filmmaking-forever-unreal-5]] — deeper Mixamo pipeline with Blender prep and OneClick Control Rig
- [[how-to-animate-spider-man-in-unreal-engine-5-for-beginners]] — next step: Control Rig baking, additive tracks, Pose Library
- [[unreal-5-hotkeys-every-filmmaker-must-use]] — Sequencer workflow shortcuts for efficient animation editing
