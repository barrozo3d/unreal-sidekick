---
title: How to Create MASSIVE Crowds and Battle Scenes in Unreal Engine 5 - Niagara and OverCrowd
source: YouTube
url: https://www.youtube.com/watch?v=1BcKEd9UO9k
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-/
frame_count: 47
---

# How to Create MASSIVE Crowds and Battle Scenes in Unreal Engine 5 - Niagara and OverCrowd

**Source:** [YouTube](https://www.youtube.com/watch?v=1BcKEd9UO9k)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 113m5s | 47 section(s)

---

## Raw Data (for Claude Code extraction)


### Introducing Overcrowd: Powerful Crowd Simulation in Unreal Engine [0:00]
**Transcript:** Have you ever wanted to direct epic scenes with massive armies of thousands of modular characters  charging across an open battlefield? Maybe you've imagined harnessing Unreal Engine's  Niagara particle system for cinematic, physics-driven crowd effects? Or perhaps you simply need a  powerful, efficient solution for filling stadiums with modular, cheering augments.  Introducing Overcrowd. A powerful crowd simulation plugin built entirely within Unreal Engine.  With no need for any external third-party software. With Overcrowd, dynamic, large-scale crowd  generation is here for the masses. And in this video, I'll walk you through the basics of

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_000.jpg

### Overview: What We'll Cover in This Tutorial [0:40]
**Transcript:** using Overcrowd and setting up your first modular wargrab. Then we'll look at spawning static  crowds with our population scene boxes and then hooking the crowd up to Niagara for some dynamic  crowd behavior. Hi, I'm Charlie, Unreal Engine filmmaker and co-founder of Overcrowd,

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_001.jpg

### Welcome & Beta Announcement [0:58]
**Transcript:** which is a crowd simulation plugin for Unreal Engine and the sponsor of today's video.  Overcrowd is currently in early beta, so we're releasing it at a reduced price,  reflecting the stable and ready-to-use features. So how does Overcrowd work? And how do you use it?  Well, at its core is our intuitive wargrab editor, a powerful tool integrated directly into Unreal  Engine, allowing you to easily organize modular wargrab, body parts, and baked-in animations.  Overcrowd functions similarly to Unreal Engine's Anum to Texture plugin,

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_002.jpg

### How Overcrowd Works (Vertex Animation Textures & Niagara Integration) [1:35]
**Transcript:** converting animated skeletal meshes into vertex animation textures or vats.  Essentially, static meshes with animations stored in their materials.  This method dramatically enhances performance, enabling the efficient rendering of thousands  or even hundreds of thousands of animated characters simultaneously. These vat characters can  also be seamlessly integrated into Niagara as mesh render particles, enabling the use of  Niagara to drive crowd behavior and basic AI at massive scales. Additionally, Overcrowd supports  metahuman heads and allows you to incorporate facial animations, which is a pretty cool feature  and pretty unique to Overcrowd. The Wargrab editor also lets you spawn basic population boxes.  These are static volumes that instantly populate your scenes with modular vat characters.  So these population boxes are ideal for quickly-populating large areas with stationary crowds,  so it's perfect for scenes like cheering armies or packed stadiums.  In this scene, you can see hundreds of modular characters running down a city street.  Their movements are dynamically driven by a Niagara particle emitter, which is included in this plugin.

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_003.jpg

### Creating Dynamic Crowds with Niagara Particle Emitters (City Scene) [2:53]
**Transcript:** As the UFO moves overhead, a vector force seamlessly attracts the particles upwards,  causing the characters animations to fluidly blend from running to flailing as they're lifted into the air.  And in this scene, Overcrowd showcases its capability to handle battle scenes at truly epic scale.

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_004.jpg

### Massive Battle Scenes with Overcrowd (LOD & Scalability Features) [3:18]
**Transcript:** This features roughly 20,000 modular characters on a massive open battlefield.  Thanks to Overcrowd's Automatic LOD Generation 4 vats, the scene smoothly transitions from expansive,  wide-angle aerial shots to highly detailed close-ups, and it maintains exceptional performance  the whole time. So this seamless scale ability allows, say, filmmakers to freely move their cameras  from sweeping shots down to close-ups of characters, and it opens up tons of possibilities.

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_005.jpg

### Future Goals: Total War-style Battle Simulator & Advanced Niagara Integration [4:07]
**Transcript:** Our ultimate goal with Overcrowd is to develop it into a complete battle simulator, inspired by systems  like the Total War games or the massive software famously used by Peter Jackson for the epic battles  in the Lord of the Rings. Well, we currently offer basic Niagara integrations, such as  driving large armies across battlefields. We plan to expand this significantly, so future  updates will introduce advanced emitters with collision detection and interactive fighting behaviors,

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_006.jpg

### Animation Groups for Paired Combat Animations [4:44]
**Transcript:** and all the stuff you need to create dynamic battles. Additionally, Overcrowd's static population boxes  include an exciting feature called Animation Groups, allowing you to easily spawn thousands of  characters paired together in animated interactions, or little vignettes of paired characters.  So this particular shot is actually featuring our sword fighting animation pack. So this is useful  for populating huge battle scenes, especially background characters, but still maintains  visual quality even when you get up close to it. Another powerful feature that is integrated

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_007.jpg

### Dynamic Swapping from VATs to Interactive Actors (Upcoming Feature) [5:23]
**Transcript:** into Overcrowd is the dynamic swapping from vats to blueprint actors or skeletal meshes,  as your camera or character gets close to them. It can also be activated by a volume,  and this enables direct interaction with the characters. And while dynamic swapping isn't  displayed or detailed in this tutorial, a focused video covering this feature, along with  comprehensive tutorials on leveraging it fully, will be available soon, as it's one of Overcrowd's  most exciting capabilities. Currently, Overcrowd's Niagara integration includes features like

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_008.jpg

### Niagara Integration: Crowd Movement and Collision Avoidance [5:59]
**Transcript:** crowd movement along splines and neighbor grid integration, which enables particle collision and  avoidance. These capabilities are built into the included Niagara midter and allow characters to  realistically move around without running through each other or overlapping. And we cover all  that functionality in detail in this tutorial. Of course, as Overcrowd is still in beta,

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_009.jpg

### Current Beta Limitations & Visual Quirks [6:28]
**Transcript:** we're actively resolving a few visual quirks, such as shading issues under certain lighting  conditions. You will also see here there are a lot of inputs required along the way to get your  vats prepared and to use Niagara. There are a few bugs here and there, but we cover them in this  tutorial and show how to work around them. We are also working to make the tools as easy to use  and automated as possible, while still allowing for maximum flexibility with these powerful tools.  So thank you so much for your patience as we work on these. We are super passionate about  this product and there's just so much cool stuff right around the corner. So the current price is  a reduced price and we will definitely be raising it as we roll out more features and squash bugs.

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_010.jpg

### Tutorial Overview: What You'll Learn Step-by-Step [7:22]
**Transcript:** So the following video is a detailed walkthrough of the basics of Overcrowd. And we'll show you how to  create a modular wardrobe with metahuman heads and facial animations. Add accessories like weapons  and shields, spawn a crowd of cheering people, and how to use the current included Niagara  emitter to make the army charge and follow a spline. So if you've been waiting these past few weeks  for Overcrowd, thank you for your patience. We really wanted to make sure we delivered on getting  something out before Unreal Fest. So make sure to follow the link in the description, comments,  or right up here if you would like to buy it. And if you have purchased Overcrowd already,  thank you so much and enjoy. Now onto the tutorial.

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_011.jpg

### Installing Overcrowd Plugin in Unreal Engine [8:13]
**Transcript:** Okay, so the first thing we want to do is get the plugin installed into our engine. So if you  have bought it on fab, you can kind of skip this process where we just move the plugin into our  directory. But if you've downloaded it from somewhere else, like if we are selling it on our website  or Patreon or something, this is how you will receive it. You'll receive this folder and you just  extract that and then find wherever your engine is installed. And we'll just go in here. Go to  Engine and Plugins and we are looking for Marketplace and right in here. We can just drag that  into there. Great. And now we can go and make a new project. So we'll just click back into here.

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_012.jpg

### Creating & Setting Up a New Unreal Project [9:02]
**Transcript:** And I'm going to make a third person project just so I get the Manny Skeleton and Mesh in there.  Go ahead and name your project. And we'll create that. All right, and here's our new project.  And now I'll show you how to enable the plugin in your project. You just go up here to edit and  plugins. And then you can just start searching for Overcrowd. And there you go right there. And

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_013.jpg

### Enabling the Overcrowd Plugin [9:32]
**Transcript:** just hit yes. And it'll ask to restart. So just go ahead and do that.  All right, great. And now our project is back. And you'll see up here, we have our Overcrowd  button. So we can just go ahead and click that. And that will bring up what we're calling the  Wardrobe Editor. And this is where you will bake all of the animations and into your skeletal

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_014.jpg

### Introduction to the Wardrobe Editor & VAT System [9:54]
**Transcript:** meshes and turn those skeletal meshes and animations into vats or static meshes that are animated  through their material instances. And this will make a lot more sense once we start adding some  objects to it. So I'm going to show you how to use this in the simplest way first. And that's to  bake a single animation into a single skeletal mesh. And you know, and then you can  instance it, you know, in a volume or something. So I'm going to show you how to do that really  quickly, just using the default Manny skeleton. So in our third person project, we can just come  down here to characters, mannequins, meshes. And here we go. We have Manny. So you want to find the  skeletal mesh that you want to, you know, make thousands of or whatever. So we'll go ahead and  we'll open that up. And what we're doing in here is we want to actually edit these materials.  We want to paste a couple of nodes into their materials. And that is what is going to communicate  to the materials, what the animation should be, and how all the vertexes should move. You don't  really have to worry about how it does it. You just have to know this is part of the process where  we prepare the materials and the chara...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_015.jpg

### Preparing Materials for VAT Animation [12:46]
**Transcript:** Okay. And now I want to go back to our mesh. So I'm going to come up here and I'm going to browse to  it in our content window. So you can do that by clicking up here. And we're going to right click.  And we're going to go to scripted asset actions and then overcrowd. And we're going to generate the  LODs. And you can just you can mess around with these. But honestly, the defaults are fine

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_016.jpg

### Generating LODs and VAT Mesh Pairings [13:08]
**Transcript:** for most use use cases. So just hit OK. And that is a really nice feature of overcrowd that it  just does that for you. That's something that you're like my the zombie tutorial. I didn't have  working properly were LODs. So that's nice. And that can just take a second to do. You'll see  there's that window kind of flashing up here. I'm just kind of let it do its thing.  Okay. Great. And then we're going to come back down and right click on the mesh again.  Come back up to scripted asset actions. And then come over to overcrowd. And we're going to click  create that mesh pairing. And what this is going to do is it's going to tag your skeletal mesh  you know with a with a body part or a wardrobe assignment. This will make more sense as we add like  modular packs. You know, and you really want to start tagging all of your individual sort of wardrobe  pieces. But for now, we can just tag this as a full body. So come over here to the body part  and click the little arrow there and then drop down the overcrowd menu. And you'll see all of these  here. And we want the body part sub tag. So we'll open that up. And you can see there's already a  few in here by default. You know, these are yo...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_017.jpg

### Setting Up Your First Wardrobe [15:47]
**Transcript:** this time. So we'll add a new one. And and we'll name this like manny. Okay. And again, we'll select  that. Add new tag. Great. Select that. And apply. Okay. And that should just do that. You can close.  And now you can come up here and select our manny wardrobe. Okay. Great. And that will bring up  these sort of settings over here. And we will get a wardrobe piece added to the wardrobe. So  click this icon over here. We'll close hanger. And this will fill up with a ton of different  things. This is your vat mesh picker. And this is where you'll see all of the different  you know wardrobe pieces or body parts or meshes. And whatever you tag them as you'll see them  all in here. So right now we just have this one. So we'll select that. Okay. And great.  All right. And the next step is to add an animation and get the animations baked to these vats.  So what we want to do first is find the animation reference skeleton. In this case, it's the manny

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_018.jpg

### Adding Animations to Your Wardrobe [17:07]
**Transcript:** skeleton. So we can just click that and populate that there. And now we want to add an actual  animation. And it's really important that all of your body parts that you know, our wardrobe  pieces are the same skeleton as your reference skeleton. And you know, the animations are also  the same skeleton. So it's not, you know, too big of a deal. Most things are targeted for manny.  And so on or metahuman already. But yeah, you don't want to be mixing stuff. You'll get some weird  results. All right. So let's find some animations for manny. We'll come down here. And just take a  look and here. Let's see what we got here. So why don't we add an idle animation? And you know,  actually we'll add a few. So you actually want to add all the animations that you plan to use with  this wardrobe. You want to add them all here. So we're going to go ahead and we'll have to add  these individually. So we'll go ahead and we'll add this idle one here. And we'll give this the  sub tag. We'll open this up. Come to animation. And we want to add a sub tag for idle.  And again, we'll select our any down here. Add new tag. Select the tag. Great. And you want to do  that for like I said, any of the animati...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_019.jpg

### Spawning Crowds Using Populate Scene Boxes [20:15]
**Transcript:** get some of these guys spawned in here and you know, see what that's starting to look like. So we can  do that by adding a populate scene box. And that'll be like a volume. And in that volume,  we'll spawn a bunch of these guys. So again, this is like the simplest way to use this, but still  very effective. Let's see what's come up here to the populate scene menu and grab a populate scene  box. And you'll see there's a couple things up here. There's like a spline. So you can spawn  them along a spline. We'll take a look at that. A null, you know, or a box of volume where you can  exclude them from anyway, we'll just select the box for now. And then come up here and click the  spawn the selected populate scene actor button. Click that and boom. And give it a second to,  you know, prepare the shaders. Again, you know, this can take a while depending on how many  different pieces you've added. But there we go. And we can come down here and you'll see  we have some guys idling, we have some guys walking, and we have some running. And let's just go  ahead and minimize this for a second. I'll select the populate scene box.  And here you'll see these are all the individual people in the b...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_020.jpg

### Adjusting Individual Characters & Animation Control [23:49]
**Transcript:** if you had, you know, if you wanted to kind of like art director scene a little bit, like,  this guy shouldn't be on the blue box. Blue boxes aren't for standing on, you know, you can move  him down there. And perfect. Or like this guy, you know, is kind of like partially in the wall,  you know, you can move him out of there. Anyway, so that's how you do that. And so say we wanted to  control the animations of the crowd and say have them all just be idling. We can do that over here.  If you come and select the populate scene box from your outliner over here, you can then come  down here and pull up the default animations here. And you'll see we have all three of the animations,  you know, from the wardrobe that automatically get added. So, you know, if we wanted them all to  just be idling, we could, you know, take away these. And then I think you want to make sure you  delete these empty ones. And then again, you kind of come up here, use this button to refresh all  of these boxes or any, you know, emitters or anything like that that are dealing with overcrowd.  You can do that right here. So let's push that and boom. Now we have everybody just idling and say you,  you know, want ...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_021.jpg

### Additional Features: Animation Variation & Offsets [26:06]
**Transcript:** want to cover in this sort of really basic tutorial before we move on to doing like a modular crowd.  And so I want to come up here and show, you know, the under this populate scene menu where we selected  the box from before, you can select a spline, for example. And so with that selected, by the way,  when you place these, it's firing just a raycast out from your, the middle of your screen. So you  look where you want to place it. And then it's the same for the box as well. And you click this  button there. And boom, that seemed to have refreshed, or I think that might have refreshed our  other emitter, which is interesting. Anyway, that you can see it just made a spline here.  And so, you know, these are obviously useful for, you know, all sorts of things. Again,  you might have to refresh to see that work properly. Okay. And then yeah, now they're all along the  spline. Yeah, so that could be useful for all sorts of things. I won't go too deep into that.

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_022.jpg

### Spawning Characters Along a Spline Path [27:20]
**Transcript:** Feel free to, you know, explore that spline to be perfectly honest. I haven't used this exact sort  of instance or all that much. But anyway, so say you, you know, wanted to like, this is actually  a good point to bring this up. So say we had done a bunch of stuff to our, our big emitter, our big  box, this first one that we placed down. So I've got that selected. And you know how I placed this  other thing and it refreshed it. Well, that kind of messed up. Like if we had moved some people  around and didn't, you know, and wanted them to stay like that, you know, we don't want that to  get messed up when we are, you know, messing with other overcrowded sections and like hitting this  button up here. So you can lock this. You can select the blueprint up here and click lock placements.

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_023.jpg

### Locking Character Placement & Workflow Tips [28:13]
**Transcript:** And that will stop the, you know, that will stop these from moving around. And I think that  should also stop it from refreshing in general. Yeah. Anyway, still working out all of the features  in this sort of alpha beta version of overcrowded. And so this whole process that we just went  through here, this is the exact process that I did to create the crowds for the Gladiator short film  that I released recently. So it was literally just, you know, a bunch of the only difference was  that I used modular characters instead of just like a single instance like this and had, you know,  multiple cheering animations. And yeah, I just used this box emitter and kind of like placed,  you know, big chunks of, you know, hundreds, I don't know, like three, four hundred characters around  the stadium. And it looked great. Ran really well. And was really easy to use.  So why don't we actually move on to doing some modular characters and a few of the more advanced  features. And again, you know, there's so many things that you can do with overcrowded that we just  don't really have the time to make like the documentation for right now and are still kind of in  the alpha stage. For example, swapp...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_024.jpg

### Working with Modular Characters & MetaHumans [29:51]
**Transcript:** documentation for it. We will probably release a video, you know, just like a short video kind of  showing how to do a really basic version of that. But for now, I'll show you how to do modular crowds.  Okay, so I've just gone ahead and made a new blank level. And I've also gone ahead and added a  few things to my project. I added some metahumans. I wouldn't add it to a male tall normal weight  metahumans to my project. And you know, that's because we're going to use their heads to,  you know, add to our wardrobe. And so, you know, I'm not going to go through how to add a metahumans,  you know, I assume if you're trying to make thousands of metahumans on screen, you know,  how to add a metahumans to your project. If not, you know, plenty of tutorials out there to do that.  I have not tested this with the new 5.6 metahumans and the sort of like in-engine, you know,  metahuman creator. But we're going to test that really soon. And, you know, I don't think it should  cause too many issues. But yeah, like I said, can't confirm. Anyway, so make sure you add some metahumans.  And then you're also going to need to add a modular pack, you know, a modular clothing pack. So,  I'm going to op...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_025.jpg

### Modular Assets & Polyphoria's Medieval Armor Pack [33:06]
**Transcript:** going to need are some animations to use with your characters. And so I, uh, actually migrated over  the same army animations that I used in these cinematics. And, uh, I made all of those animations  and both the body and face animations. They're really cool. Um, let's see if I open them up here.  Um, you'll see in my content browser, it migrated them over. It brought a bunch of stuff that I'll  have to get rid of. Um, but the goal is to package these animations with over crowds. So I just have  to make sure I'm not, you know, sending any of these like preview meshes from the orcs or whatever,  uh, with them. But anyway, if you go ahead and open these up, you'll see, you know, we have a ton of,  um, animations for, you know, uh, these soldiers in the army for carrying shields and weapons,  uh, or unarmed or with just shield or with just a sword. And, uh, and then they all have matching  face animations, actually. So all of these animations were recorded at the same time. Um,  uh, the face animations were recorded at the same time as the body animations. So they all match up.  And, uh, the goal is to make, you know, a super high quality sort of like army simulator or whatever,  like...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_026.jpg

### Preparing Animations for Modular Characters [35:01]
**Transcript:** And in our case, we'll be using the metahuman skeleton. And then, you know, I also have them, uh,  targeted to the mani skeleton as well, just for your convenience. But it's super easy. You know,  you probably already know how to do this. You can even, um, you know, if you right click on an  animation. So, you know, say you have many animations. You need them to be metahuman. You just  right click, uh, and then go up to retarget animations. And then, you know, select the animation you  want. And, uh, you know, so here we've got an orc with a shield cheering. And so we come over here  to our target skeletal mesh, you know, and then select, um, you know, like, um, um,  tall, you know, it doesn't really any metahuman skeleton. And, uh, there you go. And you just hit,  export animations down here. And you can do batch, you can batch that as well. Um, you know,  you could export all of them like that. And, uh, yeah, sometimes that can take a while though,  just so you know, anyway, uh, we don't need to do that.  Okay. So let's start getting our asset pack ready for baking. So I'm going to go over here and open

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_027.jpg

### Setting Up Asset Pack Materials for VATs [36:07]
**Transcript:** up medieval armor and then character parts and meshes and UE5 metah for metahuman. And we have a  base body here. Um, we're not going to worry about that for now. Let's go into the mail. And we'll  open up the chest section here. Okay, lots of things. And, uh, we're not going to do all of them,  but I'm going to show you how you can do a few. So let's go ahead and open this up.  And then right over here, we have our materials. So let's navigate to one of those in our content  browser. Okay, there's that right click on that and click find parent. And, uh, okay. And then,  I'm going to right click on that and that seems to be the parent material for that one. So let's go  ahead and open that up. Great. And here we are again. And let's remember to in our overcrowd window,  you can copy the nodes with this little clipboard. Click that back into here and then we'll copy and  paste those nodes in there. All right, where are we? The normal. Let's grab the normal off, plug it  back into there, pull the normal into there. And then we'll do the world position offset. Great.  Apply. And just go ahead and save that. And I'm going to come back here and I'm going to check to  make sure this shou...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_028.jpg

### Creating Wardrobe Sets with Weapons and Shields [43:06]
**Transcript:** can go and add our newly created torso sections. So here you can see it's starting to populate our  vatmash picker and we got a bunch to select from. So we can actually just, you know, control click  on all of these because why not? Um, it looks like I did add some with a hood. Whoops.  And great. Uh, we'll just hit OK and boom. Now that is starting to add these to the wardrobe.  And let's do the pants again really quickly. So let's come back down to our meshes. Oops. Let's go  into the mail, the boots. And I believe, uh, you know, these pants are all using the same parent  material. So, um, I'm just going to double check really quickly. Like I'm going to open this one.  Um, here's the pants material. Right click on that. Fine parent. Fine parent. Yep. It's that same  one. OK. That's awesome. So let's go back to the pants and also I'll just select all of these.  Right click. Scripted asset actions. Generate LODs. Great.  All right. And once that's done, let's right click again.  Scripted asset actions. Create vatmash pairing. And in this case, let's come down to the body part.  And we can select legs. Great. Let's go ahead and do that. OK.  And I forgot to mention you can see all t...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_029.jpg

### Adding MetaHuman Heads & Facial Animations [51:12]
**Transcript:** Look at the viewport over here. And I'll just let that load really quick. Okay, let's select  the face mesh. All right. And that's that there. I'm going to just navigate to that. And  where is that? There it is. Let's go ahead and open that up.  Great. And there are a lot of materials here in the metahuman head. And, uh, yeah, it would be  nice if we could package some metahumans, uh, you know, or some metahuman heads with this. Um,  not sure if we can do that. So for now, it's up to you to sort of prep your own metahuman heads.  So anyway, let's start with the head material here. I'll navigate to that. And we'll right click,  find parent, right click, find parent, great. And go ahead and open that up. Let's just make sure,  yep, that is the base material. All right. And we're in here and let's go copy our nodes from the  overcrowd window. And we'll control V those into here. Grab the normal, normal, and we'll plug  it. And we have a world position offset in here already. And that is for hiding the neck. Well,  we have to get rid of that. So let's pull that out. And we will plug in our world position  offset. So we're going to miss this sort of neck mask, but you can actually add t...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_030.jpg

### Troubleshooting Common Issues (e.g., Floating Eyeballs) [58:19]
**Transcript:** faces? So you do that by going to your wardrobe and selecting the head body part. Come down here.  And we're going to click this little plus next to that. And that's going to create its own sort of  asset here. And it default assigns this sort of additive facial animation thing to the head  bone. Okay. So obviously you could mess around with this if you really know what you're doing.  But for now, the basics work just fine. And we're going to add a new data asset to here with the  animation. So let's come down here and click. All right. And let's navigate to that using that  button there. All right. And let's go ahead and open this. And we don't need to worry about adding  a reference skeleton here, but we want to come down to here and add some animations. So we're  going to add one of these indexes. And then we need to find a facial animation to add. And then  we'll tag it here. So I'm going to navigate to the face animations that I have. Of course, you  can use any of the one, you know, any that you record using metahuman animator. You know,  but in this case, I'm going to use one that I've already done. So let's see. This is the  weapon and shield wardrobe. Let me grab weapon. L...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_031.jpg

### Facial Animation Integration [60:01]
**Transcript:** Okay. Yeah. That looks great. Yeah. That's it. That's a cheering, cheering man.  Okay. And so we're in here and I'm going to tag that under animation. We're going to tag that  as cheering. Great. And then, you know, you can go ahead and add in the face animations for  the other animations as well. So we have idle walking and running and where you and again,  the wardrobe we're doing is the weapon and shield one. So I'm just going to do that really quickly  and speed it up. And so what I'm doing is just selecting the corresponding face animation to the  corresponding body animation. And that should line up, I think that, you know, these animations were  recorded at the same time. And so yeah, I think it should all line up, but we'll see.  Okay. So we have all of those added and we can come back here. So we're going to come back here  and we're going to bake those animations in. So let's hit bake. All right. And then let's go ahead  and hit refresh. Okay. Let's see what we got going on here. All right. So we have some of the  face animations working. Let's see. Which ones are lined up with which because some, oh, no, we do  have looks like he is, he does have his idle animation. That...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_032.jpg

### Adding Accessories (Weapons & Shields) to Characters [65:27]
**Transcript:** even just jump cut. And then I'm going to show you how to add the weapons and shields. And so if  you need to add something that's like a static mesh or like an accessory or something, I'll show you how  to do that as well. All right. And so here you can see I'm just going into the feet and checking  that the boot material is using one of those master materials. And it is. So I'm going to bake those  and give them a foot tag. And then I'm also going to go to the gloves. And you'll see I'm not adding  the bracers here. Those need to be in like their own separate thing, you know, because if you have  gloves, you're going to want to see hands if there is no gloves there. And then here I'm adding  all the helmets. And I'm adding them to the hair tag. So, you know, if you're going to have,  you know, a mix of helmet and hair, you're going to want them under the same slot. So if there's a helmet,  then there's no hair. And hit refresh and boom. All right. Great. And we have all of our  wardrobe spawned in here. And I thought I got rid of the cape. It actually doesn't look too bad,  even though the cloth physics aren't working. Anyway, I probably want to remove that from there.  Some othe...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_033.jpg

### Converting Static Meshes to Skeletal Meshes for Accessories [68:11]
**Transcript:** with these animations? And we can actually convert these static meshes into skeletal meshes. We can  line them up with like where the hand is for a metahuman in a pose, and then convert it to a skeletal  mesh. And then it can then be baked into a vat with the appropriate animations and skeletons  and added to the wardrobe. So that's what we're going to do right now. I'm going to show you how to  do that. All right. So first thing we can just go ahead and minimize this zoom over here. And we're  going to actually add a new level sequence. And we're going to call this accessory. Okay. Let's go  ahead and save that. Okay. Close there. And I want to add a metahuman to our scene. So I'm going  to come over here to one that I already have added. Go to Coda here. We're just going to go ahead  and drag him right out. And you know, if you're aligning it with, if you're using like a mani  skeleton, you do this with a mannequin instead. But we're using the metahuman's. So let's drag  him out and we're going to zero his location into zero, zero, zero. All right. And then we're going to  add him to our sequencer. And then you can just go ahead and delete these control rigs. And we're  going to ...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_034.jpg

### Finalizing Weapon & Shield Integration [77:05]
**Transcript:** So I think you can figure out how to do that if you basically just reverse engineer what we did for  the sword on the left hand. Do that for the sword on the right hand. Do that for the shield on  the left hand and add it as an accessory weapon L. And so we're just going to go ahead and jump  ahead to that part. Here I'm actually instead of attaching it to his left hand. I want to attach  it to his lower his lower left arm. So that's just one bit that's different from the the right-handed  weapons. And here you can see we're just aligning the shields with his left forearm.  And once you get that aligned with the forearm, then remember you have to reset the origin while it's in  a pose. And then remember we want to change the binding bone from the right hand to the forearm  with a lower lower arm L. That's what we want. And then we're just doing the same old generating the  LODs and then generating the vat mesh pairing. And then here you saw I'm deleting the previous static  meshes. All right. And once that's finished baking, we can just go ahead and refresh and boom.  We've got our guys with shields and weapons. And you know what? Let's just go ahead and make  let's go ahead and ma...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_035.jpg

### Increasing Crowd Size & Variation [79:57]
**Transcript:** height variation and that's going to help a lot. All right. So why don't we actually get all of these  guys just cheering in like a huge formation, you know, just like in the opening cinematics. So  that's really easy to do. So with our emitter here or our box selected, we can come over here  and we can just remove these animations here. We just go ahead and delete everything except for  the cheer index there. So we just go ahead and leave that. And then over here in the spawn  locations in box component, let's select that. And over here, we're it had set our minimum rotation  to say minus five and our max rotation to about five, just like we did earlier on. And then let's  bring up our over crowd window again and refresh that. And there we go. They're all facing in  the same direction and they're all just cheering now. All right. And so, you know, if we wanted to say  have, you know, a ton of these guys that would be extremely easy to do, you know, you just grab  your population box here and expand that out. And I don't know, let's do. Let's do  2,500 refresh. Boom. All right. That's looking pretty cool.  And look how easy it is to just get, you know, a ton of guys just spawned in...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_036.jpg

### Introduction to Niagara Integration [82:11]
**Transcript:** but it totally has Niagara integration. And you'll see it's extremely powerful. Um, it's just that,  you know, this tutorial is getting extremely long. And, uh, you know, it's, it's a lot to go into.  If you know what you're doing with Niagara, you'll, uh, be able to, you know, this will have a  lot of value to you already, you know, the ability to make these modular vats with all of this  functionality. And then, you know, over time, we will add in more Niagara functionality. I mean,  that is, that's where this really starts to be amazing. But for now, I'll just show you some  basic stuff and how you can kind of, you know, start using this with Niagara. And before we do that,  I'm just going to really quickly set up another wardrobe just so you can see two wardrobes working  at the same time. And I'm doing one that's almost exactly the same as the weapon in shield guys,  but I'm, uh, doing it for just weapons. So I want some guys in the army to be holding both  weapons and shields. And then some guys to be just holding weapons. And the best way to do that

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_037.jpg

### Using Multiple Wardrobes with Niagara [83:20]
**Transcript:** is to set up, you know, two separate wardrobes and have the shields included in one and, uh,  not included in the other. And then I also have two separate sets of animations. I have the animation  sets for the guys holding shields and the animations for the guys without shields. And, um, you know,  I just add those same, you know, I have a cheer idol and run animation and I add them to both  wardrobes. So here you can see I have it all set up. And you can see here the animations over here.  They're using the same tags, you know, cheer idol run and walk. Um, and so I have four there,  but you can see that this is for just human weapon as opposed to human weapon and shield if we go  here. So they're using different animations. So one thing, uh, to keep in mind in this stage of  overcrowd, the sort of stage of development, um, if you're using Niagara and you want to use  multiple wardrobes in the same sort of like army or group or emitter, um, you want to make sure  that these animation indexes are the same between the two wardrobes or however many wardrobes you have.  So for example, I have, um, the cheering animation in index zero, uh, the idol animation index one,  etc. And that's ...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_038.jpg

### Known Bugs & Workarounds for Facial Animations [89:21]
**Transcript:** Okay. So let's get this swapped to a Niagara emitter. Right now we have a couple things in the  scene. We have our populate scene box and that we are going to keep and that's going to,  you know, show where we are spawning the guys and, you know, you'll also be able to control how  many are spawned into this box. And right now they're just using this sort of static instancer.  There's this blueprint up here and that is determined in, let's see, right here. You can see the  placement, the overcrowd placement group is set to default and we want to actually, and close,  close that. We want to switch this to Niagara here. So we can go ahead and switch that and  nothing's going to happen yet and that's fine. We need to add our blueprint Niagara emitter to the

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_039.jpg

### Setting Up Niagara Emitters & Spline Movement [90:18]
**Transcript:** scene. So let's hit control P and we'll type BP underscore Niagara crowd base. Great. Let's grab  that and just plop that in there. Okay. Now what do we have here? We have a Niagara emitter.  We have a blueprint that has a spline in here and you can use this spline to  control the flow, the direction of your crowd. And what will happen is it's actually really cool.  Like you can, you can either just leave this spline just like this pointing in that direction  and the crowd will just kind of move in that direction. But you know, say if you wanted to  give them a little bit more flow, you can grab the part of the spline there, grab the end and drag it  out. And if you know how to use splines, it's very easy. You can hold down alt and drag, click drag  out from a point and it will add a new point and create this sort of path like this. And so you  can kind of build out a path for your crowd to follow just like that. And what will happen is the  the each person on the crowd will sort of follow the spline, but they'll do it, you know, based on  where they are. I can't remember the exact sort of math that's going on there, but it's meant to  look like nice and natural. So anyway, let me,...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_040.jpg

### Niagara Neighbor Grid for Collision Avoidance [94:25]
**Transcript:** is actually giving them collision and detection inside of here. So they're all aware of each other  or aware of their neighboring fellows. And so they will be doing some avoidance. And this is super  cool. This is super useful. And I've used this grid, you know, I've expanded this grid to be huge.  So you can actually use it over a large distance. But yeah, as I said, kind of backtracking a little  bit here. So I apologize, but if you select your crowd Niagara crowd base, come in here and select  the emitter, you'll see down here is the grid size. And that's what I sort of changed. You see this  yellow outline here while I have the grid, will I have the emitter selected. That's showing the  bounds of these neighbor grids. So they're going all this whole crowd is going to be aware of each other.  And, you know, avoiding each other as long as they are inside this box. And then as soon as they  get outside the box, then they'll start to, you know, move through each other and so on. And,  you know, you can play with this down here. I changed some settings to, you know, I changed the size  of the grid. And then I also changed the overall the number of cells on each axis. I, you know, I ...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_041.jpg

### Controlling Crowd Animations & Speed in Niagara [100:12]
**Transcript:** overall node and it should be up at the very top. Okay. So let's take a look down here at all  of these variables. And you'll see, uh, if you click on this, you'll see we've got a bunch of  variables here. And this is actually what is controlling the animations that they're playing. And so,  you know, there is the ability to blend between multiple ones. Um, but, you know, what I, you know,  like I said, this is still earlier. We're figuring out all the functionality. If you want to just get  them all walking properly, you just set this index to the, you know, the same number. So let's take a  look at our wardrobe really quickly. So like I said earlier, remember the Niagara system is pulling  from this animation index and not from the tags. So if we look at the animations to blend, it's one  and two. So that's index one, which is idle and two, which is running. Okay. So that's what it's  blending between. Let's just make these guys charge. We'll make them run. So we will just change  this to two. So now there's just the two animations. And let's see, they are now.  They're all running, but they're all running a little slow here. So we have two things that kind of,  a couple things t...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_042.jpg

### Fixing Duplicate Spawn Bug (Workaround) [103:26]
**Transcript:** all down alt. Just going to drag over a version right here. And why don't I'm just going to make  this smaller. This also is how you could set up, you know, big multiple chunks of, you know,  soldiers. So I can show you how to do that as well. Anyway, we drag that box off. I'm going to lower  this to like, let's say, let's say a hundred. So we can see it working properly. So I'll go ahead and  put that in. So now we have two populate scene boxes. I'll pull up our overcrowd menu here and  I'll hit refresh. Great. And this one, I think, should be working properly. Yeah. I don't see any  duplicates in here. Not any guys like running from the exact same placement node. So that's looking  good. And, you know, if you wanted to create, you know, and then if you wanted to say, get rid of  this big one over here, let's come over here and we'll select this. Now, if you just go and delete  this population scene box, it's going to orphan all of these placement nodes. So if I go ahead and  turn these nodes on, remember, we've got this is where all those guys are getting spawned in. And if  we just go and, you know, delete that like that, well, it's going to delete the box, but now,  you know, i...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_043.jpg

### Adding Niagara Crowds to Sequencer & Recording Simulation [107:01]
**Transcript:** to work with these guys for the rest of the tutorial. So I've got one group of 500. And I'm going to  show you how you can add this to a sequencer really quick. So let's come up here. We'll go to add  a level sequence and we'll call this Niagara. Okay. And we'll save that. Great. And why don't we  add now we want to add the Niagara blueprint to our sequencer. So let's come over here and find  this in our outliner. We'll select that. With that selected, come down here. Go to actor to  sequencer and click add BP Niagara crowd base. And we'll come down here and click here. We want to  add this Niagara component underscore zero. That's the Niagara component that's in the blueprint.  And then we're going to select on there. I'm on the component and I'm going to type in life.  And we want to add a Niagara system lifecycle track. Great. So that's going to add that. And then  I'm going to just kind of make this a little bit longer so we can see this play out. And here you  want to drag this red thing out. And that is going to tell us how long we want this to be. And we  want to change this to desired age. Okay. Cool. And now you'll start to see them moving around a  little bit. You can scr...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_044.jpg

### Cinematic Camera Setup & Workflow Tips [110:04]
**Transcript:** add multiple chunks. It gets a little hairy when you start adding multiple Niagara emitters. I'm not  quite sure how to differentiate between all of them. So again, this is still kind of early beta  functionality. But there we go. Okay, we've got them all added. And now we should be able to say we  wanted to do a super epic wide shot like this. There we go. We got a whole whole hoard of dudes  running around. Yep. Looking good. And so like if you wanted to, you know, have a little,  you know, if you wanted to make this into a cinematic, well, first of all, it should be 24 frames per  second. You can now you could add a camera. Just add a camera here. And I'll see. Let's go to this  guy. We'll set it to Vista Vision. Set the crop to 16 by nine. And I'll set the lens to 24.  And yeah, you know, like let's just do like a really quick shot here. Just kind of quickly  made something. We'll kind of do like a sweeping. Cool big sweeping shot here. So here we've got the  camera moving in. They still look a little funny with the running. I know the running animation's  terrible. I'll probably redo all of it. The treadmill I got kind of sucked. But anyway, we're just kind  of playing around ...

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_045.jpg

### Conclusion & Future Development Goals [112:39]
**Transcript:** You know, you've got a crowd that you can now control. You can control its direction using a  spline. You can add it to the sequence where you can, you know, cache it. And yeah, so a little  clunky, but we're getting there, you know, we are getting all this functionality in there. And  it's going to be a super powerful tool.

**Frame:** tutorials\frames\how-to-create-massive-crowds-and-battle-scenes-in-unreal-engine-5---niagara-and-\frame_046.jpg


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
