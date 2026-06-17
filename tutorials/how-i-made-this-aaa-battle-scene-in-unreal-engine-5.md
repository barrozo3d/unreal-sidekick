---
title: How I made this AAA battle scene in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=P2eR9gGPZnA
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.x"
tags: [mocap, metahuman, move-ai, naval-battle, battle-scene, ocean, vfx-particles, sequencer, elevenlabs, ue5]
extraction_status: complete
frames_dir: tutorials/frames/how-i-made-this-aaa-battle-scene-in-unreal-engine-5/
frame_count: 14
---

# How I made this AAA battle scene in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=P2eR9gGPZnA)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 13m37s | 14 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In this video, you'll see how I made this historic naval battle scene in Unreal Engine 5.

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_000.jpg

### Short Film [0:06]
**Transcript:** In the summer of 1588, Spain's greatest fleet sailed for England.  Over 30,000 soldiers and sailors believed they were on the verge of rewriting history.  They were to invade, conquer, and overthrow Queen Elizabeth I.  We are attacking.  Come on, come on!  For these men, the mission was clear. They are confidence on the waiver.  Spain was the most powerful empire on Earth, and this amada, it's salt.  Commanding this fleet was the Duke of Medina Sedone, for him and his men, victory was not just possible.  It was sir, Missignor, we are attacking England.  They are going to give the men who are preparing for the battle.  Our victory is secured.  We will overcome the number, Missignor.  Victory, as fate would have it, was not in fact secure.  The battle is over.

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_001.jpg

### Inspiration [1:47]
**Transcript:** Alright, thanks for watching.  My inspiration for this project came from the Epic History channel on YouTube, and there are series Nelson's Battles in 3D.  They use 3D models and graphics to show these naval battles, and I thought this would be perfect to do in Unreal Engine.  I'm like, how hard could it be? You just get some ships and some ocean, and there you go.  I went to the Unreal Engine Marketplace and just typed in ship, and after searching around, landed on this really awesome Spanish galleon.  That gave me the idea to just do the battle between the Spanish Armada and England in the 1500s.

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_002.jpg

### Animating the Ships [2:32]
**Transcript:** In Unreal Engine, I just duplicated the ship a bunch of times, and through down Waterline Pro is the ocean asset.  After just keyframing them a little bit, got them moving around, and adding a little bit of swaying, a little bit of bobbing, and so on.  That looked pretty good, actually, just keyframing that.  After just moving the camera around and watching the ship move, I ended up getting some pretty decent shots.  This looks pretty good, but it was kind of boring.

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_003.jpg

### Adding Metahuman Crew [3:11]
**Transcript:** I figured, what if we actually got down on the ships and saw some meta-humans?  I started throwing some meta-humans in there, and I started dressing them up with this asset pack from Polyphoria that I have called Medieval Armor.  It's great, they're really high quality, they're kind of pricey, but they look great.  I just dragged the clothing into the skeletal mesh slot on the meta-humans replacing their clothing, and it works really well.  Honestly, I'm kind of just making this up as I go.  Let's get some crew in there.  I end up with about 10 individual meta-humans, most of them are duplicates of each other.  I figured, okay, that's enough to fill the deck and make it look like there's a crew here.  Keep in mind, I'm not entirely sure how I'm going to do this.  I'm kind of experimenting as I go.  I'm just kind of spacing the meta-humans out around the ship, putting them in interesting places.  I have both the ship and all of the meta-humans added to the sequencer, and in the sequencer, they're all the meta-humans are attached to the ship.  That's how they're able to move relative to the ship like that.  I have a few guys with some basic animations from a pirate motion capture pac...

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_004.jpg

### Motion Capture and Move.AI Setup [5:08]
**Transcript:** I use Move AI for my motion capture, which uses six go pros in a ring to capture the motion.  For the face animation, I use a meta-human animator, and I have a Rococo head rig which you'll see in a little minute.  Everything, and then here I am just calibrating, and you'll see some performances coming up here.  My lord, we're going to get to the England.  Take the men that are prepared for the battle.  Your victory is safe.  We'll overcome it in a number.  I wanted to see if Move AI would work for getting an animation of climbing the rigging.  I set up a ladder in my volume, and honestly, it worked pretty well.  It wasn't perfect. I definitely had to do some cleanup on this animation, but overall I thought the result was cool.

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_005.jpg

### Adding Motion Capture to the Scene and Blocking Out Shots [6:08]
**Transcript:** Back in Unreal Engine, I get my performance captures onto the meta-humans and into the sequencer.  Start just scrubbing around and flying a camera around.  I'm still not 100% sure what the shots are going to be.  I'm just looking at different angles and seeing what looks cool.  Playing things back, and I slowly start to get a good idea of the shots that I want.  What's so awesome about Unreal Engine is, in this case, I think there should be some ocean spray spraying up behind them.  I just go to the marketplace and grab some spray splashing particle effects.  Within a minute or two, I've got these particles added to my scene.  I'm just duplicating them along the side of the ship here.  It ends up working really, really well.  Then, similarly, in lining up this shot, I'm looking up at the sky, and I'm like,  there should definitely be some birds in the background there.  I take this old asset that I have that has some bird splines in it, and I just add a spline,  and get some birds working, and there you go.  Then, the guy actually climbing the rigging, this is the only place where I had to do any real animation cleanup.  Here I am just working on an additive layer on his control ri...

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_006.jpg

### Battle Scene Setup [7:44]
**Transcript:** I ended up just finding this particle effect that's an artillery muzzle flash, and I just took that and duplicated it over and over,  and added it to the front of the cannons, as you can see, until all of the cannons had a particle effect,  and then they're all added to the sequencer here.  In the sequencer, I'm able to activate each particle effect, and so I kind of stagger the start,  and I end up getting this really cool effect, and it totally looks like it's firing a broadside blast of the cannons.  I kind of just let that play, and look around for cool shots of it doing that.  Then I got just a smaller galleon model from the marketplace to use the English ships,  and just placed a few of them in there. I didn't need too many, but just enough to make it look like a battle's going on.  And just looking at interesting shots as I'm going, starting to line things up,  and then I add the same artillery particle effect to the English ships as well.  And then you can see I added some cannonball splashes. It's a splash from the same pack as the ocean spray on the side of the ship.  And with a few of those in there, it's starting to look like a battle.

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_007.jpg

### Men Falling from Rigging Shot [9:17]
**Transcript:** So as you can see in this shot, we have some people falling off of the mast,  and for that I used some animations from an asset pack called Dramatic Deaths. It's got some falls.  It has some guys getting like thrown by explosions, and so I wanted to use those for here.  And you know, I start by just kind of getting the animation lined up with a metahuman and getting it into the sequencer.  And then I'm just flying a camera around, kind of scrubbing the animation, and looking at which angles look cool,  and kind of figuring out the shot from there, just kind of playing the animation back, trying different things out.

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_008.jpg

### Deck Chaos Shot [10:00]
**Transcript:** And this next shot is a really perfect example of that as well.  You know, I have that getting thrown by the explosion animation that I wanted to use.  So I just kind of get that in there and get a camera flying around.  And you know, I get some of these other animations. This is from like a scared motion capture pack.  You know, I get that guy in there, and I'm really just kind of feeling out the camera motion here.  You know, the guy is getting thrown, so I'm like, all right, the camera should follow that.  And then, you know, as I turn and see that he's sliding across the ground, I'm like, okay, camera should definitely push in and follow him as he slides there.  And you know, it just kind of naturally comes about just from working in a real-time environment like this.  And you end up with some really cool shots that you might not have envisioned otherwise.  And then this shot of the shipwreck here was really inspired by the asset pack of the shipwreck that I saw that just happened to look just like the galleon.

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_009.jpg

### Shipwreck Shot [11:01]
**Transcript:** So that's a separate asset that I bought.  And then what you're seeing here is waterline pro.  It just looks like that out of the box with the waterline kind of perfectly cutting through the camera like that.  And then I added these, you know, these, just some swimming animations to some, some guys and kind of made it look like they're drowning here.  And just kind of moved them right below the surface and added that swimming animation looping to them.  But yeah, this is a really kind of cool and eerie shot to set up, you know, seeing it in real time like this and kind of, you know, lighting up these drowning dudes.  And then up on the deck, I, you know, I just added a point light to the fire and then there's a guy doing a kind of crawling animation on the deck.  And then I just recorded some voiceover and morphed my voice using 11 labs.  In the summer of 1588, Spain's greatest fleet sailed for England.

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_010.jpg

### Recording VO [12:07]
**Transcript:** Over 30,000 soldiers and sailors believed they were on the verge of rewriting history.

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_011.jpg

### In-Depth Metahuman Motion Capture Tutorial [12:18]
**Transcript:** So obviously this was a pretty high level breakdown, you know, I didn't go into specifics very much.  I kind of just wanted to show what the my creative process looked like, I guess.  But if you're really interested in learning more about motion capture and using metacumens and making scenes like this,  I actually have a really in depth comprehensive tutorial that shows how to do motion capture and use metacumens animator and put it all together in a scene and all the way through export.  And it's done using tools that are either completely free or very cheap, including the motion capture solutions.  So please consider checking that out.

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_012.jpg

### Outro and Thanks! [13:04]
**Transcript:** And if you found this video entertaining or interesting or valuable in any way, please consider leaving a like and subscribing.  And to everyone who has subscribed so far and liked or watched or commented on the videos, thank you so so much.  It is really surprising to see how well the animations and the breakdowns and tutorials are received.  So I really, really appreciate it.  Alright, that's enough for this video.  Thank you very much and see you in the next one.

**Frame:** tutorials\frames\how-i-made-this-aaa-battle-scene-in-unreal-engine-5\frame_013.jpg


---

## Structured Notes

### Core Technique
Historic naval battle scene built by combining duplicated Spanish galleon assets on Waterline Pro ocean, MetaHuman crew with Move.AI mocap (including a climbing-rigging animation), particle effects for cannon fire and ocean spray, and ElevenLabs narration — all assembled by exploring camera angles in real time in Unreal Engine.

### Summary
Charlie Driscoll chronicles the creative process behind a 1588 Spanish Armada battle scene in Unreal Engine 5. Inspired by the Epic History YouTube channel, he builds the scene iteratively: placing and keyframe-animating galleon ships on a Waterline Pro ocean, adding ~10 MetaHuman crew with Polyphoria medieval armor, using pirate mocap packs plus one custom Move.AI climbing-rigging animation, then layering cannon muzzle flash particles (staggered in Sequencer for broadside effect), ocean spray splashes, bird spline assets, and a shipwreck scene with swimming/drowning animations. Shots are discovered organically by flying the camera around the live scene. ElevenLabs produces the voiced narration.

### Key Steps
1. Import Spanish galleon from Marketplace; duplicate multiple times; add Waterline Pro ocean asset.
2. Keyframe ship positions (sway and bob) in Sequencer; fly camera around to find shots.
3. Add ~10 MetaHumans; apply Polyphoria Medieval Armor pack by dragging into skeletal mesh slots; space around ship deck.
4. Add MetaHumans to Sequencer; attach all MetaHumans to ship actor so they move relative to ship.
5. Assign pirate mocap animations to most crew; capture one custom Move.AI climbing animation using a ladder prop in mocap volume; clean up via additive layer on Control Rig.
6. Duplicate and place artillery muzzle flash particle effects on all cannon positions; stagger activation in Sequencer for broadside effect.
7. Add smaller English galleon models; duplicate artillery particles onto English ships; add cannonball splash particles.
8. Set up shipwreck shot: place shipwreck asset (matches galleon style), use Waterline Pro waterline cutting through camera; add swimming/drowning animations to MetaHumans below surface.
9. Add point light to fire on shipwreck deck; set up creeping/crawling animation MetaHuman.
10. Record narration; morph with ElevenLabs; add to Sequencer audio track.

### UE Systems / Blueprints / Settings
- Waterline Pro (ocean asset with waterline camera effect)
- Level Sequencer: ship keyframe animation (transform), particle activation tracks, MetaHuman attached to ship Actor
- Move.AI multi-cam body mocap (6 GoPros)
- MetaHuman Animator (face capture, Rokoko head rig)
- Pirate mocap pack, scared animation pack, Dramatic Deaths animation pack (swimming/falls)
- Control Rig additive layer (rigging cleanup for climbing animation)
- Niagara particles: artillery muzzle flash, ocean spray splashes, cannonball splashes
- Bird spline asset (background atmosphere)
- Polyphoria Medieval Armor Pack (MetaHuman clothing)
- ElevenLabs (narration voice morphing)

### Difficulty
Intermediate

### UE Version
5.x

### Tags
mocap, metahuman, move-ai, naval-battle, battle-scene, ocean, vfx-particles, sequencer, elevenlabs, ue5

---

## Related Entries
- `how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng.md` — Move.AI pipeline overview with two simultaneous actors
- `cinematic-motion-capture-with-move-one-and-metahuman-animator---unreal-engine-54.md` — full beginner tutorial for the underlying mocap pipeline
- `how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator.md` — similar production breakdown with interior mafia-themed cinematic
