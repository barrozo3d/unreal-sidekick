---
title: The EASIEST and CHEAPEST Motion Capture Setup for Metahumans in Unreal Engine 5.6 (No Headrig)
source: YouTube
url: https://www.youtube.com/watch?v=M799eoMK4tw
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56/
frame_count: 18
---

# The EASIEST and CHEAPEST Motion Capture Setup for Metahumans in Unreal Engine 5.6 (No Headrig)

**Source:** [YouTube](https://www.youtube.com/watch?v=M799eoMK4tw)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 22m14s | 18 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In this video, I'll show you how to push single camera performance capture to its absolute limit in Unreal Engine 5.6.  No expensive equipment, no suits, no head rig, just a single Android phone camera,  driving the performances of triple-acquality, metahuman characters.  We'll be putting four of the best single camera mocap solutions head-to-head,  running them through the gauntlet of an entire short film,  comparing cost, accuracy, and speed to see how they perform in real production start to finish.  I'll walk you through using a single camera to capture your mocap,  and how you can combine that exact same footage with metahuman animator to achieve  full performance capture, face and body with as little gear and as little cleanup as possible.  And when you combine that with my crowd simulation plug-in overcrowd,  you'll see how easy it is to create massive battle scenes and zombie hordes that bring true cinematic  scale to your films. The whole idea for this video started back at Unreal Fest in June.

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_000.jpg

### Unreal Fest inspiration [0:56]
**Transcript:** Matt Workman and Corey Strasberger did a live demo on stage, showing real-time performance capture  using a camera-based mocap system for the body and a consumer-grade webcam for the face,  running through metahuman animator live. The fact that this was happening in real-time was  already impressive. They were using the capture, a high-end multi-camera mocap solution.  I actually demoed myself here on this channel. It's incredible tech, but that set up costs  tens of thousands in software and hardware. And that got me thinking, if the face can be captured  with a webcam, what's stopping us from combining that same footage with offline single camera  mocap for the body? This could be the simplest, cheapest, full-performance capture workflow imaginable.  To find out, I wrote a five-minute pirate-themed short film. I wrote out everything from battle scenes,  duels, dialogue scenes between multiple characters, and blocking that would test how much I could  actually walk around and maintain a good capture. Now, I've already used these tools to make short

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_001.jpg

### Test film plan & constraints [2:12]
**Transcript:** tests and tutorials. So in this case, I wanted to see if they could actually be used to make something  resembling an actual film of some kind. I would use as many triple-acquality assets from fab as I  needed, as well as the best assets from my own massive library to make it look as professional as  possible. And of course, any mocap solution of any quality can be cleaned up enough to look good,  depending on how much time and effort and skill you're willing to put into it. But I was interested  in spending as little time cleaning the animation as possible, even if it meant looking a little rough  around the edges. The goal was speed and ease of use, and fun, really. The tier is all mine,

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_002.jpg

### Prep: MetaHumans setup [2:59]
**Transcript:** me too. Now, if you would like to follow along with the tutorial, the first thing you will want to do  is get your MetaHuman characters ready. So your project is ready to ingest your performance capture  and get it processed into your scenes. So everything you'll see here was done in Unreal Engine 5.6  using the brand new generation of MetaHuman's. So make sure you have your MetaHuman Creator Core  data enabled under your Engine install options and then enable all these MetaHuman plugins in your  project. This will give you access to the new MetaHuman Creator right inside your project,  where you can create a MetaHuman from scratch or select one of the brand new presets and work  from there. You can add MetaHuman clothing from the marketplace, and in my case, I use these  amazing pirate outfits from Polyphoria. Then you can rig your character, download the textures,  which in my case, I chose 8K, the highest quality, and then hit Assemble, and your AAA  MetaHuman character is ready for full performance capture. Now that we've done that, let's get  back to capturing our performances. So I needed a camera setup that would work for both MetaHuman  Animator Facial Capture and Full Body MoCAP. Now, I should say, I love head rigs. They're still the

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_003.jpg

### Camera, audio & capture settings [4:15]
**Transcript:** gold standard for facial capture. I've used everything from DIY rigs I built for 30 bucks to a high  end captive devices rig that costs $30,000 and is used in major studios, you know, and then everything  in between. But for this project, the goal was to eliminate as much gear as possible. And the irony  is that as soon as I got rid of my $100 head rig, which I have used in budget MoCAP tutorials in  the past, I ended up buying a $130 wireless mic set from DJI. Because with the phone several meters  away, it would no longer be close enough to get clean audio. So it plugs right into your phone and  captures your audio directly to your footage. So I shot everything on my Samsung Note S23 Ultra,  recording in 4K 60 FPS on the main neutral 1X lens. So avoid the really wide lenses since they  can distort the movement at the edges of your frame. Also, you'll see here that I threw in an A-Pose  and T-Pose at the beginning of my takes. But you actually don't have to do that unless you are using  Marionette as your MoCAP solution. More on that later. But for now, let's look at the test results and

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_004.jpg

### MetaHuman Animator: first results [5:38]
**Transcript:** see how many human animators performed with this single camera setup. And honestly, it held up  surprisingly well, even from across the room, as long as I stayed roughly facing the camera.  Once I had the capture workflow down, I ran every performance through four single camera MoCAP systems.  Quick magic, mesh-capade, move one, and Marionette, using the exact same footage. Same lighting, same

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_005.jpg

### AI mocap shootout overview [6:01]
**Transcript:** framing, same performance. I tested them pretty thoroughly with dozens of clips with different  actions, and while all were capable, two clearly stood out for this project. Quick magic was the  fastest and easiest to use. A one-minute clip processed in about 10 minutes, costing roughly $2.94  per minute of animation. So Quick Magic will only process clips up to 60 seconds long,

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_006.jpg

### QuickMagic: workflow & tips [6:31]
**Transcript:** and under 200 megabytes in size. If the take runs longer than a minute, just split it into segments.  Since Quick Magic and Metahuman animator don't require calibration, you can easily string those  segments together later in sequencer. So then drag and drop the clip into the Quick Magic Web Editor,  select the Unreal Engine 5.6 mannequin skeleton, and if you're doing a seated or upper body  performance, enable upper body only. This is a feature that is unique to Quick Magic. It locks  the hips and auto poses the legs, which is perfect for seated scenes. Then download the FBX.  Now in Unreal Engine's Content Browser, import it as animations only, selecting the UE5 mannequin skeleton.  Then you can right click and retarget the animation, where you can select the Metahuman Skeletal  Mesh and retarget for Metahumans. Now paired with Metahuman animator, Quick Magic captured  subtle performances beautifully. Not that I'm a particularly subtle actor or anything, but it really  got the eye movement matched with the subtle head movement that really brings your performance  capture to life. It's not perfect, but this footage is nearly raw and still feels like it would  not take much to clean it up. The only weakness I found with Quick Magic is walking. On takes with  a lot of blocking, the hips tend to wobble, so I kept it mainly for dialogue and upper body shots.  For movement and spatial accuracy, I used Meshcapade. It's slower, roughly 18 minutes to process

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_007.jpg

### Meshcapade: accuracy & multi-actor [8:11]
**Transcript:** a 30 second clip, and priceier at about $10.80 per minute. But the spatial accuracy is incredibly  solid. It handled walking toward camera, turning, and even shots of me hanging from the ship  ringing with no drift or sliding. The system stayed spatially consistent and handled the more  complex blocking really well. Now Meshcapade also has one unique advantage. It can capture multiple  performers in the same clip. I tested this with footage from my Move Pro sword fighting animations,  and it tracks both actors surprisingly well from a single camera angle. Each clip costs the same,  whether it's one performer or two. So it's great for fight choreography or interaction.  And if cost weren't a factor, Meshcapade might be the overall best choice. It's only really  held back by occasional hand jitter and sometimes odd foot placement, but you can easily frame around  those issues, and the body motion itself is consistently excellent. The other two, move one and  marry a net really come down to value. The Move One S1 model costs $50 a month for about 20 minutes  of processing, roughly $2.50 per minute. And the S2 model with their Dex advanced hand tracking  costs $250 a month or about $8.30 per minute of animation. It's a reliable middle ground option,

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_008.jpg

### Move One & Marionette: value [9:45]
**Transcript:** if you don't mind doing a bit of cleanup like smoothing out jitters. Now, Marionette runs offline  with a flat yearly fee of $150. So your permanent cost is basically zero. It smooths motion more  aggressively, but it's definitely usable with some tweaking and for background animation where  it isn't the main focus. So for the film, I ended up using Quickmagic for expressive, acting  heavy dialogue and Meshcapade for walking and full body movement. Stick around to the end to see

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_009.jpg

### My hybrid picks [10:20]
**Transcript:** the total price breakdown of all the motion capture credits I used to produce the film. Now,  onto the new updated workflow for processing the face animations using Metacumin animator.  To start, we need to import the footage we used for our body mocap using the new Live Link hub,  which you can find under the Tools menu. Change Live Data to Capture Manager, then click Add Device

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_010.jpg

### Face workflow in MetaHuman Animator (step-by-step) [10:40]
**Transcript:** and select Mono Video Ingest. With that selected, change your take directory to the folder with your  mocap performance footage. Then you can select the takes you want to import, which should be the same  clips you uploaded to your single camera mocap platform of choice. So with those selected, click Add to  the queue, then hit Start. Now that the footage is imported, you can start processing it using Metacumin  animator. Start by going to your content browser, right click and go to Metacumin and create new  Metacumin performance. Open that up and change the input type to Monocular Footage. Then under  Footage Capture Data, you can select the clip you want to process. Then you can select a visualization  mesh by clicking this menu and searching Face, and then selecting the Face Mesh of the Metacumin you  would like to see with the performance. Then under Head Movement mode, change it to Disabled,  since we don't want Metacumin animator to process the neck movement only the face. And that's all  you have to do. Just hit Process, let it do its thing, then Export Animation. Then you can create a  new level sequence. Add your Metacumin, delete the control rigs, and add your body and face animations  to the appropriate tracks. They should line up perfectly. Now once all the dialogue and performance

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_011.jpg

### Cinematic fights: Move Pro pack [11:56]
**Transcript:** work was in place, I wanted to push the system further, you know, to see if it could stand alongside  some more professional animation for the action scenes. So for the fight scenes, I used my own  sword fighting mocap pack, captured with Move Pro using a 6-go pro setup. Each animation was  performed by two stunt actors simultaneously. So every strike, parry, and dodge is spatially accurate.  Both performers reacting to each other in real time. Now because these are paired cinematic animations,  they drop right into Unreal already synchronized. These aren't short game loops, they're long  cinematic performances. So you don't have to worry about stringing a bunch of smaller animations  made for games together. And they all come with metacumin facial animations that you can use right  out of the box. You just drop the animations onto two metacumans in your sequence, attach some  swords to their hands, and you have an instant action sequence you can start filming. And if you just  want to experiment, I've made one of the looping sword fight animations free. You can download it by

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_012.jpg

### Spawn big crowds with OverCrowd [13:02]
**Transcript:** signing up for the email list below. Now these sword fighting animations are perfect for creating  large scale battle scenes quickly and efficiently. Overcrowd lets you take modular metacumans and  wardrobes. Pair them with animations and spawn hundreds or even thousands of high quality animated  characters in your scene. You can put paired animations like my sword fighting animation pack in  there, and it will spawn the characters dueling with each other over your entire scene.  It's perfect for background action, so you can focus on your hero characters well,  Overcrowd fills the frame with action. For the cavern sequence, I recorded my own  idle and reaching animations, and then I fed those into Overcrowd and spawned over 5,000 zombies,  which would all reach for the characters as they walked past them above. Now as the co-founder of  Overcrowd, I'm a little biased here, but this is probably the best tool on the market when it comes  to creating large scale battle scenes and crowds like this in Unreal Engine. If you want to bring

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_013.jpg

### Virtual cinematography workflow [14:11]
**Transcript:** epic scale to your films or games, you can find it on fab by following the link in the description  below. Now that we've talked about all the mocap and the crowd stuff and animation,  I want to talk about what my favorite part of the process is, which is doing the virtual cinematography.  It's why I go through the trouble of getting all this animation into Unreal Engine in the first  place, so I have something interesting to film. Each shot was its own sequence, and had its own  camera, lights, and characters, and I converted everything into spawnable actors. That way, when I  open a shot, the assets for that scene appear in the world. If you are making an exterior scene  that is lit by the sun, you can add the scene's directional light to your sequence and convert it  to a spawnable actor. This way, you can easily adjust the angle of the sun from shot to shot,  and it won't interfere with the lighting in the other shots. And when you are making a lot of shots  for the same scene, you can simply duplicate your sequence and use that as the starting point for  your next shot. It keeps the project much more organized, and you can revisit shots weeks later,  and Unreal Engine will rebuild it automatically with the same camera, same lighting, same animation,  etc. So, having a mini-set file for every shot. Now, for the cameras, I used a 70-millimeter iMacs  filmback, because why not? I was switching between 40-millimeter lenses for wides and 80-millimeter  lenses for close-ups. So, these camera and lens settings will give you the compression and depth  of a long lens, but the field of view of a wide one, which will feel more cinematic,  and makes things just kind of feel more grand for lack of a better term. If you want to learn more  about why iMacs looks the way it does, I highly recommend this video by Thomas Flight. So, with all

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_014.jpg

### Short film: Cavern of the Damned [16:05]
**Transcript:** that said, please enjoy the film.  There's a black-hired school, lies in the cavern of the damned, just past the eyes of devil's  reach. I reckon we can make a door of it, as just three days sales from these waters.  It's a coated trivetrain, no man returns.  What name returned? Me?  You sought the treasure and we have to tell Taya. Who are you, old man?  I was kept in the besuantry Isabella, stolen Spanish galleon, 40 guns, 100 soles of ore.  Or dead now. Two British frigates, cut us off the ears and devils reach.  Should have surrendered, the gold free that had taken on.  It made me mad with it. A galleon against two British frigates.  No pirate crew can reload that fast. Where's this treasure then?  We're listening and go tell you.  We covered those red coats like a hurricane due to sailcoarth.  They were stricken, but none were agreed for treasure.  Captain, look out!  You were Sarah's lobotalized mate.  Thank you, Captain.  Who's behind you, Captain?  Out!  The mate and I won that day together, but then we were battle.  That was still the count, my little.  Against we sail the fair.  By the time we found the cave, I'd already decided.  Decided what, old man?  The cavern of the dam.  Every soul who doied seeking that treasure over a thousand years,  clapped below, still hungry, still rich, roughs.  And that was Blackheart's gold.  Enough to buy kingdoms.  Equal shares. Just like they promised.  She's beautiful.  Absolutely beautiful, Captain.  Captain?  The treasure is all mine, beauty.  You promised equal shares.  Well, come and take it.  You betrayed your own, Racy?  What did you do with the gold, your filthy barnacle, Baba?  Never spent a single cursed coer.  The damned old rose to take me treasure from me.  They followed me twenty years.  New curse.  Close.  Runsters.  You sliver.  What are you doing?  See you soon, the treasure still there.  Okay, thanks for watching.  Yeah, so this is what I was able to make in about three weeks,  including about a week of pre-production and testing.  It's obviously pretty rough, especially some of those AI voices.  But it was a lot of fun to work with this extremely minimal mocap pipeline.  So in total, I ended up recording and processing roughly 18 minutes worth of motion capture  animation across all characters and all scenes.

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_015.jpg

### Cost breakdown & takeaways [21:19]
**Transcript:** If the entire thing had been done using Quick Magic at $2.97 per minute, it would have cost  $53.  Meshcapade at $10.80 per minute would have cost $197.  For my hybrid approach I used for the final film, I processed a total of 16.5 minutes  with Quick Magic and 2.5 minutes with Meshcapade for a total of roughly $74 total motion capture cost.

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_016.jpg

### Outro + Discord & free download [21:47]
**Transcript:** All right, if you want to hang out and chat about Unreal Engine filmmaking,  consider coming by the Discord and show us what you're working on.  It is becoming an awesome community and a great resource for this sort of thing.  And sign up for the email list below.  We have exclusive offers and giveaways as well as updates on all my upcoming content.  Okay, I'm Charlie and I'll see you in the next one.

**Frame:** tutorials\frames\the-easiest-and-cheapest-motion-capture-setup-for-metahumans-in-unreal-engine-56\frame_017.jpg


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
