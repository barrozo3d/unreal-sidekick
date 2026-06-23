---
title: Create a Lightsaber Battle in Unreal 5 (in 10 minutes!)
source: YouTube
url: https://www.youtube.com/watch?v=MWFpt3ZQ0zE
author: Josh Toonen
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
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
**Transcript:** If you wanna create films that you have to have characters,  I mean, a one single movie that you love  that doesn't have characters, it's impossible.  It doesn't exist, so it's impossible to avoid characters  when learning Unreal Engine for filmmaking.  And when you're first starting,  characters can be really daunting  because it puts all of the different disciplines together  for modeling, texturing, rigging, and animation.  And if you're not good at every single one of those steps,  you might be afraid to jump in.  Well, I'll show you where you can find characters of your own,  but also how to give them life and performance  without having to know animation.  What's up?  My name's Josh Tuner, and I'm a director and visual effects  supervisor, and I've spent the last eight years  working on Hollywood visual effects on movies  like Star Wars, Shazam, and Deadpool.  And last year, I was an on-set Unreal operator  at the world's largest LED volume working  on Avatar, the last Airbender.  So every single day I was using Unreal,  and then after that, I would spend my nights  and weekends trying to understand how to use Unreal Engine  to make films of my own without a huge budget  and without a huge crew.  And I make these videos because making films in Unreal  is still really, really hard.  But if you know the workflows and you know the techniques,  you can repeat them over and over again on films of your own.  So today I'm going to show you step-by-step  how I import characters, bring them into sequencer,  and string together many different motion capture

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_000.jpg

### Importing characters [1:13]
**Transcript:** animations together to create a performance  with characters in Unreal.  All right, let's show you the fastest way  for you to get 3D characters directly  into your Unreal scene so you can start animating them  right away.  And the best place to find that is mixmo.com.  So here they have a selection of a bunch of characters.

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_001.jpg

### Downloading Mixamo animations [1:30]
**Transcript:** They're not amazing, but they will absolutely do the trick  so we can just get our hands dirty with the animation system.  And here you can even upload your own 3D models and rig them.  So just go to mixmo.com, sign in, and go to the character  section.  So we have this big list of characters,  and then we're going to pick this character that's  Vanguard by T. Tune Young.  He's just on page one.  And so now that we have our character,  we can go over to the animations tab.  And we can start to see exactly what the animations  are going to look like transferred to this character.  The best tip I have here is just try  to find a pack of different animations.  So you can string many animations together  that are supposed to be working in the same timeline.  So to get this started, I'm going to start with the sword  and shield pack.  And all we have to do is hit download,  and all of the defaults are good.  And the best way to learn is not by watching,  but it's by doing it yourself.  So either start a brand new U project,  or I've included the project files I'm using here  as a free download down in the description.

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_002.jpg

### Importing characters [2:24]
**Transcript:** So download that if you're a beginner,  or if you just want to follow step by step.  So I've loaded up this project here,  and let's just import our character first and foremost.  So there should be an object called the name of the character,  Vanguard.  And then this is the FBX import box.  And the important things to know here  are the difference between a skeletal mesh and a skeleton.  So a skeletal mesh is what a character is called  inside of Unreal.  It's the mesh associated to the character.  The skeleton is the actual bones and the rig underneath.  So in this case, we need to create a brand new skeletal mesh  and a brand new skeleton because it's a new character.  So to start this, we're just going to go to skeletal mesh,  import mesh, we'll leave skeletal blank,  and we'll hit import.  And once this is imported, we should have our character.  So we have our skeletal mesh, we have our skeleton,  and now we need to start importing our animations.  So just to keep this organized,  I'm going to take all these textures and the materials  and put them in another folder,  and then we'll create a new folder called animations.  So now let's just select everything and drag this in and import it.  And then now we'll just need to assign our skeletons.  So we'll type in Vanguard, and we have our Vanguard skeleton.  And then we'll just set the animation length  to exported time and press import.  All right, now the animations are imported.  We can open up any of these and we'll  have our animation editor here.  Just so you know, you don't really modify any animations  here in terms of the actual keyframes.  Although it is possible to do like many changes.  But here we can preview all of our different animations.  So pick a few here that we kind of like.

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_003.jpg

### Creating our Level Sequence [3:54]
**Transcript:** First we're going to create a level sequence called LS  underscore character and then we can just press enter  to open up sequencer because it's already selected.  And now we'll navigate back to our Vanguard soldier  in the content browser and just click and drag him into the viewport.  We still need to add him into our sequencer.  So we'll add a new track with the green plus sign.  And then at the very top of this menu,  we can add our selected actor.  And now if you hit the add animation button,  we'll see all of the different animations  that share the same skeleton.  Really quick, I prepared this before.  We're just going to take a lightsaber.  But it's literally just cylinders together  and I'm using an emissive material combined together  to just make a really simple lightsaber.  So we'll bring this in.  And it's actually really easy to parent things to objects  in Unreal and within sequencer.  If I show everything that's only in this level,  we'll have our red lightsaber in our Vanguard person.  And we'll just make sure both of them are set to movable.  And then we'll parent this to the right hand.  So we have this, the lightsaber shouldn't move.  And then when we add our first animation,  let's just add a slash animation.  I'll just go on the animation track and pick this slash.  We'll see that it should just automatically stick  and move to the path of our hand.

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_004.jpg

### Assembling our animation [5:08]
**Transcript:** Let's add a death animation.  So we'll add this death to.  And this is a cool thing.  You can just overlap these and they will start to blend  in between.  They'll do like a soft blend.  And then you could even change the easing between those two.  I'll just give it a default for now.  You can see we can have a seamless blend  between our two animations on our guy right here.  So just to fill out the beginning here,  let's add in just a simple idle animation.  And we'll intersect that at the end.  All right, cool.  So we have our first character.  Now let's bring in our second one.  So now I'm going to control and drag this into here.  And this will automatically add our actor into sequencer.  And let's have him run up and do a couple  hack and slash things.  Let's give him his own lightsaber.  So right now we'll just duplicate that from the original one.  Let's go to the original red lightsaber.  Let's hit detach and let's add it to our Vanguard character.  We know we'll want it on his right hand.  So we'll grab that.  And then we can just zero out this transformation.  And it should snap right to his hand.  Just do a really simple 90 degree rotation  and slot that right into place.  I'm hitting shift and drag here.  Can move our camera with the object.  And now let's add some character animation.  Let's say we want to combine one, two, three,  different attack animations together

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_005.jpg

### How to use Motion Blending [6:24]
**Transcript:** and have our character travel forward into the world.  Well, we're going to have a problem.  Every time a new animation starts,  the character is going to teleport back to where it started.  So if we want our character to travel correctly  through the world, we want to right click our animation  and use the motion blending options.  This is how we can have our new animation start  where our last animation ended.  All we have to do is select what bone we want to match  in the previous animation.  And we just want to set ourselves  to the hips of the previous clip.  So now we've got our motion blending working.  And this is the key technique that we'll use  to string all of our different attack animations together.  So now we've blended sort of attack two and sort of attack three.  And we'll keep adding animations here.  Just remember at any point,  if you want to add in different animations,  use the animation editor to preview  all the different animations we've downloaded.  So now let's reposition our attacking character  so he slices right through the enemy.  We want to add a transformation track.  We have one here.  But now we can actually keyframe in the position.  So let's move ourselves.  Cool.  So we're starting to have this slash going through.  And now we just want to align the timing between our slash  and the death impact on our enemy character.  So we'll just slide around our animation clips here.  We can see we're a little bit early there.  And now we can see boom, he slices right through.  And so we want these two to clash at the same time.  And once they clash, we want that death hit tab  and afterwards.  So now we can see we kind of have an awkward timing here  where they're not getting their lightsabers at the same time.  So one thing that we can do for any of these animation clips,  we can actually just change how fast they play back.  So if you right click, go to the properties  and then go to play rate.  If we go to two, it'll be twice as fast.

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_006.jpg

### Playrate of Animations [8:10]
**Transcript:** If we go to 0.5, it'll go half the speed.  So we'll probably want to slow down this sword  and shield attack by about 0.7.  So now by slowing that one down and kind of moving it around,  we can see that we've got these two guys  clashing their lightsabers together.  It's not perfect, but very quickly,  we can start to block in motions like that.  Just to finish this off, let's have him  running up at the beginning of this shot.  And then one thing that we want to do here  on our run animations, because this loops  and starts at one place and ends in another,  it makes it very difficult to string these animations together.  So one thing that we can do in the animation editor  is enable root motion.  So we do this, we'll lock our entire animation to the hips  and then we'll want to change this from reference pose  to animation first frame and that'll kind of fix  the angle that he's at.  We'll just make sure this force root lock  is checked as true.  We'll save that.  And now when we're back in our sequencer,  we'll just add this and we'll choose our root animation.  So what we're gonna do right here  is at the very beginning of this transition,  we're gonna make a transform key frame.

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_007.jpg

### Dealing with Run Animations [9:16]
**Transcript:** We really just need the location here.  And we're gonna hover over these, click and drag over these  and press the four key.  This is going to make it a linear key frame.  And again, you will understand exactly why in just a second.  So we have our foot here  and we can see that our foot shouldn't be dragging  across the ground like that.  So we're gonna move him back and X just a little bit.  We're gonna go and hit four again  and we'll see how this looks.  We can see the foot is still kind of sliding  and traveling around.  So one thing that we can do is let's just select  both of these key frames.  Let's go and hit our curve editor.  The X location yet again, so it shows up in our curve editor.  So we're gonna select our key frame here  and we're gonna hit this double right arrow here  and pick our pre-infinity options and go to linear.  And this is gonna make it so the curve  between our two key frames here gets extended  into infinity before our first key frame.  So this looks a little weird because our animation  is too slow.  We can see that he's like sliding backwards  as he's running forward.  He's kind of moonwalking.  So what we can do is we can just select this key frame here.  And if you control and hit the left arrow key,  we can move the key frames back by one frame.  So if we move the key frames closer together,  our character will move faster  and if we move them further apart,  the character will move slower.  So we can see here we're moving them faster  and I think we can just have him be  some Captain America superhuman.  So our guys coming in, they clashed their lightsabers.  He slices right through them  and then let's add one last piece of animation here.  And we have this superhero pose  and he smashes these drones into the ground.  That's the original shot.  So we'll come through here.  We'll overlap these just at the very beginning  and let's take this, right click our sword  and shield casting match with this bone  in previous clip and match to the hips.  This should transport him back to where he should be.  Even without blending any animation,  we actually get a pretty seamless transition  between those two pieces of animation.  And there we go in just a couple of minutes  we've already finished creating a performance  out of these animations.  And this is what it looks like  when the entire shot is put together  with effects, blasters, light interaction,  all that good stuff.  If you follow along, render it out  and share your work in the comments down below  would love to see what you put together,  especially if you use your own animations.  So like and subscribe if you learned something  it helps trick the algorithm to promote this video  to people just like you.  And stay tuned to learn more Unreal filmmaking techniques.  I'm gonna break down all of the demo projects  I've done over the last year.  And I'm in the middle of a production  on this samurai sword fight.  We did the motion capture when I was back home  over the holidays.  And I'm really excited to show you exactly how we did it.  So stick around and I'll see you in the next video.  Peace.

**Frame:** tutorials\frames\create-a-lightsaber-battle-in-unreal-5-in-10-minutes\frame_008.jpg


---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### UE Systems / Blueprints / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### UE Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Entries
[PENDING EXTRACTION]
