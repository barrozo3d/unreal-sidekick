---
title: How to Create A Massive Zombie Horde in Unreal Engine 5.5 - Niagara Crowd Simulation, AnimToTexture
source: YouTube
url: https://www.youtube.com/watch?v=h6FEW4Kz_Kk
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat/
frame_count: 28
---

# How to Create A Massive Zombie Horde in Unreal Engine 5.5 - Niagara Crowd Simulation, AnimToTexture

**Source:** [YouTube](https://www.youtube.com/watch?v=h6FEW4Kz_Kk)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 64m38s | 28 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Have you ever wanted to create massive crowds of thousands of stampeding zombies in Unreal Engine?  Well, in this video, I'll show you step by step how to use an IAGRA particle emitter for crowd simulation  and some free plugins and tools to create static meshes that are animated by their material instances.  This will allow for thousands of animated meshes on screen at once, all running in real time.  So grab a drink, grab a chainsaw, because where we're going, there's a lot of zombies.  But first, let's watch a short cinematic that will showcase the effect we're creating.

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_000.jpg

### CINEMATIC [0:35]
**Transcript:** Okay, thanks for watching.

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_001.jpg

### Overview of Effect [1:21]
**Transcript:** Before we jump into the actual tutorial, I just want to go over a couple of the limitations of this effect, how it's put together, and what's going on, as well as make sure to shout out the tutorials that I followed and have borrowed from in order to make this tutorial.  Okay, so I have some of my settings turned down here, so I can actually record and look at this stuff at the same time.  But what is actually going on with this effect? Well, we have an IAGRA emitter and a bunch of static mesh particles that are animated through vertex animation textures.  So their animations have been baked into their material instances, which are then animating their skeletal meshes.  So let's go ahead and open up the actual Niagara emitter here.  And let's take a look. So we have a fountain emitter and you'll see up here, let's see, we can come down here and you'll see there's seven individual static meshes here.  So we can just go ahead and open one of these up and we've got a zombie dude and yeah, this is a static mesh.  And as you can see up here and he's being animated through his material instance.  So we're going to learn how to actually make these in this tutorial.  And you'll see we made...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_002.jpg

### Limitations [4:21]
**Transcript:** You know, there's no inter particle collisions.  So if you look closely, you'll see the zombies are just running through each other.  I did try to add inter particle collisions using neighbor grids and it just got a little too complicated for this.  I would love to see someone else build on top of this and add that in.  But that is one of the limitations. I also figured it doesn't really matter that much for, you know, the actual shots I was trying to create.  So another limitation is it's you can't really control the direction that they're running in by just rotating the particle emitter.  Let's see, we just select that.  So if I were to try and like rotate this emitter, for example, it'll rotate, you know, the shape that they're spawned in, but like they're going to keep, once they hit the ground, they're going to keep running in that direction.  And so in order to actually change the direction that they're running in, you need to go into the emitter.  And I've set up a way to kind of change, easily change their direction this way.  So you can kind of change, right now they're running on the x axis.  So if you wanted them to run in the opposite direction, you would just change th...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_003.jpg

### Benefits [7:14]
**Transcript:** So I mean, just knowing how to bake these static meshes and animate them using vertex animation textures and to do that all in Unreal Engine without leaving and going to some other software like blender or Maya.  That's all super valuable and can absolutely come in, you know, it will be useful in the future. If you ever need to create large crowd simulations or you want large amounts of instance static meshes that are animated.  And likewise, you know, just learning a little bit about the particle emitters and how they work and how to kind of use you can turn, you know, a basic particle emitter into something that can be, you know, like a crowd simulation.  This is all, this is all really cool and like I said, can be useful into the future.  And so before we get started, I just want to shout out the two of the main tutorials that I sort of combined to create this effect. I really watched a lot of tutorials to try and figure out all of this stuff, but there's two main ones that I'm drawing from very, very much so.

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_004.jpg

### Main Tutorials Used [8:14]
**Transcript:** And the first one is this tutorial by trash praxis on YouTube Unreal Engine 5, anima texture plugin, how to use it to make vertex animation textures for crowds.  And he has developed this tool that you see here, docked in his editor and that is what allows you to actually bake the animations into these static mesh materials.  And we're going to go over how to do that and how to install his tool here. And the other is from code like me on YouTube Unreal Engine 5 swarm of rats with Niagara.  And as you can see, this is where I got the lot of the particle logic from it's basically this effect that he created with some modifications.  And then I've combined trash praxis vertex to animation texture tutorial.  So I just wanted to make sure I shout out those two creators and I put links to both of their tutorials in the description as well as a link to trash practices tool on GitHub that we will be using.  And I will show how to install that in the tutorial coming up. But yeah, make sure to give them a like and subscribe and all that with all that said, let's dive in and start making zombies.

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_005.jpg

### Project and Plugin Setup [9:58]
**Transcript:** Okay, so here we are in the Epic Games launcher and the first thing we're going to do is we're going to launch Unreal Engine 5.5 in my case 5.5.1.  All right, and the first thing you're going to do is come over to the games tab over here and we're just going to create a blank and we'll call this zombie.  All right, so we have our project open and the first thing we're going to do is just go and create a new level.  Just do a basic create that.  Okay, and while we're here, why don't we just go ahead and save and we'll call this zombie setup.  Great.  And while we're at it, why don't we just go up to edit our project settings and we'll make sure this is our boot up map and in case we crash and anytime we start up the game.  So I'll just go to start up map and just select zombie setup.  Okay, that's good.  And the next thing we want to do is actually enable the plugin, which is the anem to texture plugin.  So just go up to here, edit plugins and you can just search anem to texture.  Great.  We'll just go ahead and enable that and you can just go ahead and restart now.  Okay, so now that our project is booted back up, we need to go over to get hub to download the tool that was made by ...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_006.jpg

### Download and Install Vertex Animation Texture Tool from Github [11:30]
**Transcript:** And I'll put a link in the description as well as you can click it up in the corner of the screen.  Okay, and now we're over at get hub and you can see the tools that are over here.  And this is the latest version of the tool and you can see it was 5.4.4.  However, it seemed to work just fine for 5.5.1.  So just go ahead and click that and then just go right over here and download the raw file.  Okay, now that you have that downloaded, go to your project folder and open up your content folder.  And then you're going to drag the US that you just downloaded, drag it into your content folder and it'll show up right inside your project.  Alright, so just go right over to the tool here and it's an editor utility widget, by the way.  So just right click and go up to run editor utility widget and that'll just pop up right here.  And here you can see this contains all the functionality that we're going to need to make our instance static meshes and our vertex animation textures.  And it's all very easy and it's super convenient that trash praxis is built this and given this away for free.  And so we're going to go through all of this in a minute. So let's just go ahead and dock that over h...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_007.jpg

### Adding Zombie Characters and Animations [13:03]
**Transcript:** So some zombies and some zombie animations and I'm going to be using ones from fab from the marketplace, but you could totally use them from Mixemile or some other website.  And here's one of the packs that I used that I have pulled up already just called zombie pack by undead shop.  I'll put a link in the description and I think it was like $50 for these three characters.  Anyway, go ahead and add that to your project.  Let's see.  It doesn't have 5.5, but that's okay. Just add it anyway.  And then I used this 73 zombie animations pack from gem games for the animations and they work pretty well.  I've had them for a while. I can't remember how much I paid for them. Anyway, go to add project.  And then here we'll just take a quick look at the animations here.  These ones are great because it came with nine different running animations.  So that gave me a lot of variety, which is really important to really selling the effect.  You want a lot of variety and the animations in the crowd that you're showing.  So some of these are pretty goofy. This one's pretty cool.  And then why don't we really quickly look at the zombies we pulled in too.  So let's go over to our zombie pack here.  A...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_008.jpg

### Retargeting Zombie Animations [15:26]
**Transcript:** Go back to our zombie runs.  And we'll do this one or the guy kind of plotting forward.  So just right click on the animation.  Go up here, retarget animations.  And it looks like we have to re-select it from over here.  Run 7, double click.  And that'll start playing there.  And then the target skeletal mesh.  We will find that right here.  And it's actually right here already.  We're going to select a SK Army Mutant.  And you should see them running together.  And we're going to go to export animations.  And let's actually...  Let's make a new folder here really quickly.  For the retargeted animations.  So we'll select that and just export it to there.  Great.  Okay.  And now we have the animation all set up and retargeted.  And before we go any further, I actually want to just add another folder to our content folder.

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_009.jpg

### Organizing Meshes [16:34]
**Transcript:** And we'll just call this zombie meshes.  And this is just going to help us stay a tiny bit more organized here.  And let's just move our zombie skeletal mesh.  Let's just move that into here for now.  And great.  So now he's sitting in there.  And this will just help keep us a little bit more organized as we start to get our static meshes built out.  So before we start to convert the skeletal mesh into the static mesh and bake the animations into that material,

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_010.jpg

### Modifying Materials wtih AnimToTexture Blueprint Code [17:11]
**Transcript:** we need to modify his material a little bit and create a material instance before we run through all of these buttons.  And the easiest way to do that is to look at the examples from the anima texture plugin that we installed.  And just copy some of that blueprint into this guy's material.  So make sure you can see your plugin content.  So come over here to settings and just make sure you see show plugin content there.  Then you can come over here and come down to your engine folder.  And you'll see there's plugins.  And we're looking for, there we go, anima texture content.  That's the plugin we installed.  And you can just open up characters and we'll look at the mannequin.  And in here you'll see you can just click on this blueprint here.  We'll look at the viewport and you can see these are instant static meshes that are being animated by their materials.  So this is exactly what we are going to do next.  So what we're going to do is we're going to look at this guy's material, copy some of that to our other guys to our zombies material.  Okay.  So if you come over here and click on the instance static mesh component, you'll see here's the static mesh.  And here are its two mate...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_011.jpg

### Baking the Vertex Animation Textures and Generating Static Meshes with Trash Praxis' Tool [24:20]
**Transcript:** We have everything set up and ready to go.  So let's just go ahead and minimize this.  And the first thing we can do is we can just take our skeletal mesh and add it to the slot here.  And now we can go to create static mesh from selected.  So just click that.  And boom, we now have the static mesh created.  And let's go ahead and add our animation to this array up here.  So you click the little plus to add a slot.  Let's go to our animations folder with the animation that we retargeted.  Let's go ahead and plop that in there.  And in trash practice tutorial, he adds a bunch of animations,  a bunch of idle animations to the static mesh.  And you could do that here too.  But the way he ends up setting up his crowd is different from the way we're doing ours.  We're using a Niagara particle effect to create our zombie horde.  And he uses a blueprint to sort of distribute the static meshes in a crowd  and vary their animations and stagger them and so on.  And I highly recommend if you want to do that, check out his tutorial for that.  And I'll put the link up here again or down in the description.  But as I mentioned in the intro, it's hard to get the material blueprints  to communicat...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_012.jpg

### Setting Up More Zombies [34:05]
**Transcript:** So I'm just going to do that and I might just speed it up and but keep in mind it's doing the exact same thing as we just did.  And before we go any further, let's just keep this all organized and tidy.  So we'll just go ahead and make a new folder and we'll call this guys zombie 01.  And we'll just go ahead and select all of these and we'll just move all of those assets into there.  And so that's just keeping our zombie meshes folder a little bit more organized.  Okay. So we can just go to the zombie cop from the same zombie pack and we'll find a skeletal mesh and move it into our zombie mesh folder.  Let's open that up and let's find his material and move that into the zombie folder as well, just consolidating that.  And now let's go back to the parent material that we set up and we'll copy that stuff over into our new zombies material.  And this is just like what we did before.  We're just relinking these materials, use material attributes, move that note over, reconnect it.  And that's all set up.  And then remember to make it a material instance.  And now we can go over to our tool here and we can clear all of these fields.  And we can move our...  Oh, I realized that for the ...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_013.jpg

### IMPORTANT Do Not Apply LOD If Prompted When Closing Static Mesh Window [38:14]
**Transcript:** I actually had to revert to a save here.  I had all of those static meshes open and I went to close and it a message popped up saying, you know, do you want to apply the level of detail to the static meshes.  And just click no.  And yeah, click, click no and it will because if you apply the level of details, it's going to break the UVs and they'll look like a ball of spiky things.  And that's not what you want.

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_014.jpg

### Setting Up Niagara Emitter and Adding Meshes, Initial Spawn Velocity, and Collision [38:51]
**Transcript:** Alright, so before we continue, just make sure you have your Niagara plugin enabled.  It should be on by default, but just make sure that's on.  Alright, and now we'll go ahead and we are going to create a new Niagara system.  And we are going to use a fountain.  And we'll call this an S for Niagara system.  Zombie.  Or.  Ah, great. So let's go ahead and open that up.  And.  Okay, so the first thing we want to do is we can just go ahead and delete this sprite renderer.  And because we want to have meshes, so we're going to add a mesh render down there.  And over here, you can see under the meshes, there's an array.  And there's just this thing in here for now, but we're going to actually add some to that.  And great.  Now we have ones for all four of our zombies here.  So let's go to our zombie meshes.  And let's pull our static meshes into here right now.  And it's already starting to look weird.  Particles are cool.  Great.  Just grabbing all our zones.  Or Z buddies.  Okay, great.  Now we have all four of our meshes in this array.  And you know, you'll remember that, you know, in the one that I used for the cinematics, I showed at the beginning, I had seven different static mesh...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_015.jpg

### Changing Particle Lifetime and Randomizing Initial Scale [43:14]
**Transcript:** So they're not just disappearing so quickly.  So let's go over to initialize particle.  And you'll see lifetime mode random.  And it gives a minimum and maximum.  That's good.  I already know the.  The lifetimes that I want in there because I've set this up before.  So you can of course play around with all of these variables to get the desired effect.  But we're going to go with that for now.  You hear you can also change the.  The scale as well.  So we can change the.  Scale to be a random uniform mode.  And here you can.  And so this will just make you know them a little bit bigger or smaller.  I like to do one as the biggest.  And then I think I said it to point eight.  You know, so there's maybe like a 20% variation between their actual size.  And go ahead and save that.  It's already compiled though.  All right.

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_016.jpg

### Applying Linear Force to Particles [44:24]
**Transcript:** So now we want to give them some linear force to actually move them across the ground and through the world.  So we're we're going to do that under particle update.  So let's go over here.  We're going to add a linear force.  And let's change the coordinate space to world.  And let's go ahead and make it like a hundred.  Right.  You see they're starting to start and to scoot out that way.  And they're they're slowing down.  So let's go ahead and turn off drag.  Okay.  So that is that's helping a lot.  And so yeah, you can see how they're you know they're starting and they're getting their their initial amount of force and they're moving out and and slowing down.  And right now that's because we have you know we don't have a strong enough force to overcome the gravity.  So we could lower the gravity if you want.  You know, just like this would you know kind of lower it to like half.  And you'll see they'll start to move more and further.  But I want the gravity to be normal.  Like I really want the effect of them.  You know falling properly as they like go over the ledge.  So I'm going to keep it there.  And go over and you'll kind of just have to play with the amount of force.  And...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_017.jpg

### Setting Up Variation in Linear Force and Adding Sine Wave Movement [47:36]
**Transcript:** But before we move on from the linear force I kind of just want to I want to actually change some stuff here to add some more randomization into this.  So what we're going to do is actually change this from a random range vector.  We're going to do it make.  Make vector great.  And so now we get all three of these vectors and we'll do random range float.  And now we can change this back to what we had.  What was it 150 200 something like that.  And what we're what we can do now that we made this whole thing a vector we can now change the Y force.  We can give it a little bit of wiggle and randomized that wiggle by turning the Y vector into a sign.  So we're just clicking on these little side arrows and make sign and then the scale we can change to we can make that random float as well a random range float.  So we can add let's do and we'll actually randomize the period as well change that to a random range float.  And I'm just going to I already have this figured out just kind of through trial and error.  But so I'm copying this from my original one.  But just so I did a scale of minus 200 and a maximum of 200 and a period of minus 10 and a maximum of 10 and you know really feel fr...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_018.jpg

### Changing Spawn Volume Shape [49:59]
**Transcript:** And that's under particle spawn you'll see shape location and set to sphere.  So if we go over that over that we can change that to a box slash plane and we can then change the box size to I don't know a thousand by a thousand.  All right, and that's starting to spread them out that's spreading out the area we don't you know we don't need a vertical one we're just doing spreading them out over a horizontal area.  And you can see that's starting to spread them out a little bit and of course you can change this to whatever you want as well whatever suits your your purposes, but let's just see.  Let's keep that out of thousand let's do 3000 okay so now we're getting a little bit more of like a of a crowd running running in that direction.  Starting to look pretty cool.  And really quickly before we go any further I just want to show how you can you can change the spawn rate.

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_019.jpg

### Changing Spawn Rate of Particle Emitter [51:24]
**Transcript:** If you go over to the emitter update over here you'll see there's emitter state and spawn rate and those will both show up over here.  And okay so you can see we have like our loop behavior and the loop duration and then the spawn rate so if you wanted you know more more zombies to be appearing right here you could say I don't know change this to 300 and now we're going to get a lot more zombies a lot faster.  And as you can see here it's it's in a loop but you could change it to just spawn once for example so you just switch it to once and boom it's just going to poop out a bunch of like 300 zombies right there and that could be useful for something else if you wanted but I like the you know for example if you wanted to distribute them.  In a little bit more controlled way over an environment you could say you know change your shape location to something like you know really big.  And then it's going to spawn 300 zombies over you know just once over that whole size so that might be useful for you.  So I'm doing you know depending on what you're doing but for now we're going to I'm going to change that back and I'm going to go back to my spawn rate.  We just have the emitter update...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_020.jpg

### Adding Another Linear Force to Give More Directional Control to Horde [53:40]
**Transcript:** And then another thing before we go any further you know as I mentioned you know before the tutorial started there's there's not a great way to like rotate the emitter and you know change the direction of the zombies.  So the best way that I've found to to give me some control over that is you know you go to your linear force and you know see we're sending them in this direction and so say you wanted to like you know send them in the other direction you just you just change these to a negative force.  And they'll start running in the other direction the opposite direction and then you know if you wanted them to move along the y axis and have the x axis be you know they're they're sort of sign sign wave you would switch these around now the easiest way to do that is I feel like is to just copy this and give yourself to limit this.  So you can have two linear forces and you know make sure you disable one because you now you can have two linear forces and you can have one setup to be like your movement along the x axis and then one to be set up for movement along the y axis.  Now that we have this duplicated we can actually switch these around so we can just go up to the x here and ma...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_021.jpg

### Making Zombies Face the Proper Direction, Aligning them to Direction of Velocity [56:41]
**Transcript:** So what we can do is go down to the mesh renderer here in our particle emitter and you can go down to facing mode and change it to velocity.  So now they're going to orient themselves in the direction of the that they are moving in or so we would like there's still running sideways but you can see you know as they fall you know they're falling down and they're doing these crazy bounces we'll fix that in a minute.  I'm going to actually just move this down because we're going to fix all this in a second.  So we need to fix them facing in the wrong direction even though we have them set to face the direction of their velocity they're facing in the wrong direction.  So we can do that by adding an update mesh orientation under the particle update and we can go and change it to orient to vector stabilization mode just facing and we can change the facing direction here to minus 90.  Okay great now they're finally running in the they're facing the proper direction as they run and that's looking good.  Alright so they're facing the right direction and everything but they're we're still having some problems with speed also I'm going to turn off this God awful preview window it's just flicke...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_022.jpg

### Fixing Zombie Bounce by Changing Restitution, Fixing Clumping by Reducing Bounce Friction [58:24]
**Transcript:** Okay so we still have some people getting stuck and we have some people moving way too fast and we have this crazy bouncing going on.  So let's fix that really quick let's go to the collision here and the way you control the bounce is this variable called restitution under bounce and it's default is 0.6 let's just change it to 0.1 and alright that helps a lot with the bouncing.  However they're you know they're really clumping up here at the beginning some guys are running out ahead but we want to we want to fix this clumping and that's because we have some friction when they collide and we can actually turn this down you know by a good amount so it's 0.25 I changed it to 0.05 and there we go we're we're getting the guys actually starting to run and  alright that's looking really good they are going very fast let's go to our linear force let's turn this down by a lot here let's go to negative 80 and say negative 120 those are the

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_023.jpg

### Lowering Linear Force So They Don't Run So Fast [59:41]
**Transcript:** values that I have in my a bit or that I used in the cinematics and that's looking pretty good also really quickly let's let's get these shadows turned on on the particle on the meshes so

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_024.jpg

### Turning On Cast Shadow for Particles [60:01]
**Transcript:** just select your particle effect and over here in the details panel you can click cast shadow and let's start looking a lot better really quickly  very nice and then of course you know they're just kind of blinking into existence and then you can't see here but they're all falling off the cliff here they're all just disappearing

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_025.jpg

### Adding a Curve to the Mesh Scale So Particles Ease In and Out of existence [60:38]
**Transcript:** let's see we're not going to fly all the way down there and check them out but you can make it so that they you know they're not just blinking in and out of existence you can add a you can scale their meshes in and out to kind of make it you know if you're looking at it up close it's going to look weird  but you know if you're looking at it from afar which is how I recommend you know actually using this if any zombies get like stuck on something you know for a while rather than just like disappearing they will sort of like scale down to zero and just kind of ease out and it just kind of helps with  you know not drawing your eye to that effect so let's just do that really quickly here in the particle update will add a scale mesh size so then we can multiply this vector by a float great and we can turn this float into a curve  and so then in the curve over here we just take this one and drag it down to zero zero and we'll add in a key there and we'll set its value to one and likewise we'll add a key there set its value to one  let's move these a little bit closer to the ends 0.95 good this one do 0.05 we might speed that up a little let's do 0.02  now they're kind of like inflating a...

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_026.jpg

### Outro [63:06]
**Transcript:** that's the effect right there that's that's the whole zombie horde and so you can of course you know play around with all these different parameters add you know more more zombies more animations if anyone knows how to you know set up the actual offset of the animations you know so that they start at a random point maybe  and then if you know how to you know bake multiple animations into the vertex animation texture and then have those randomly selected by the Niagara meter you know please let us know in the comments or you know keep building off this tutorial as I built off the you know the other  people's tutorials and we'll keep kind of you know all helping each other so yeah I hope you enjoyed this and you know I would I would love to show you know the camera effects and you know all the editing and cinematography tricks that went into the opening cinematic  but this is getting this is getting way too long of a tutorial and I think those are better suited for their own standalone tutorial and I might even return to using this particle effect and just focusing on the actual cinematography of it but there you go thanks for watching and I will see you in the next one.

**Frame:** tutorials\frames\how-to-create-a-massive-zombie-horde-in-unreal-engine-55---niagara-crowd-simulat\frame_027.jpg


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
