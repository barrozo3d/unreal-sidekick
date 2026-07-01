---
title: Motion Capture Sword Fighting Cinematic in Unreal Engine 5 - Move.AI and Metahumans
source: YouTube
url: https://www.youtube.com/watch?v=ukk4vw-bIpA
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-23
ue_version: "UE5"
tags: [mocap, move-ai, metahuman, swordfight, cinematics, sequencer, control-rig, short-film, choreography, handheld-camera]
extraction_status: complete
frames_dir: tutorials/frames/motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma/
frame_count: 5
---

# Motion Capture Sword Fighting Cinematic in Unreal Engine 5 - Move.AI and Metahumans

**Source:** [YouTube](https://www.youtube.com/watch?v=ukk4vw-bIpA)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 8m1s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In this video, I'll show you how I made this choreographed sword fighting scene in Unreal Engine 5.

**Frame:** tutorials\frames\motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma\frame_000.jpg

### SHORT FILM [0:06]
**Transcript:** So this was one of the funnest videos I've done in a long time.

**Frame:** tutorials\frames\motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma\frame_001.jpg

### Choreography with Professional Stuntmen [0:51]
**Transcript:** And that's because I was finally able to do something that I wanted to do since I got my hands on this motion capture technology in the first place.  I was finally able to get two actors at the same time into the motion capture volume to do some fight choreography.  I made a fight scene video recently that was a Kung Fu fight.  And the whole inspiration for that film was that I'd found a way around needing to do choreography.  That's because there was this animation pack from real illusion of hand-to-hand combat.  And it had paired animations that were 5, 10 seconds long.  And it showed the two characters interacting and fighting.  And the choreography was so good. The animations were awesome.  And it was so easy to just take two of these animations and put them into a scene and then start setting up the cameras.  And I wanted to do the same thing with a sword fight.  But the problem is there's not a lot of great paired animations out there.  There are paired animations where you might have one or two moves or something.  But everything that's out there would be so tedious to stitch together into an actual fight scene.  It's almost not really worth it.  And as far as I've gotten making films entirely on my own, filming actual fight choreography with myself is really difficult.  So I worked with two local stuntmen and choreographers who came in for just really just two hours.  And in that two hours they were able to just walk right into the volume and start messing around.  And coming up with some choreography really on the spot.  One, two, three, two, one.  And I'll do the follow-up.  And we ended up with a ton of great animations.  The whole process was really smooth actually.  I mean, the motion capture system performed really well.  We didn't have to worry about them putting on suits or anything like that.  We just made sure they were wearing a wardrobe that would work well with the capture.  Well, you know, and then be comfortable for them to do their choreography.  The whole goal was to see if we could use the Move Pro motion capture system that I have to capture something similar to the real illusion hand-to-hand combat animation pack.  Almost all the animations turned out really well.  The actors were able to do a combination of improv and actually blocking some scenes out, choreographing some stuff.  And then just letting, you know, physics become a factor as well.  And like I said, that whole motion capture process took two hours.  And I just started watching all of the little preview videos.  I pulled some into Unreal Engine.

**Frame:** tutorials\frames\motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma\frame_002.jpg

### Assembling the Scene in Unreal Engine [3:50]
**Transcript:** I just found a scene that I had had in my library for a while.  This is really awesome, sort of broken down cathedral.  And it had just amazing lighting already.  I did very little to change the lighting here.  And then I just dropped in two metahumans.  And I used the Medieval Armor pack from Polyphoria for the clothing.  And then got the animations that I wanted to use, chopped up and into the sequencer and applied to each metahuman.  Once that was in place, I baked the animations to the control rig.  And that allowed me to go in and actually fine-tune the animations.  Honestly, there was not a lot of cleanup done to these animations.  You know, I did go in and just remove the hand tracking because one hand is literally just holding a sword.  So no need for hand animation.  And then the main thing that I was doing was going through and making sure the swords were actually connecting.  Because the swords are just attached to the hand bone.  And so, you know, you can see when I just put the animations in, the swords aren't really lining up because like the actual angle of the wrist isn't being tracked accurately.  So that was the one thing I had to go in and manually adjust.  And I could do a lot better job, but you know, for this it was fine.  I knew I was going to kind of use some shaky camera and frame it in a way that would hide it.  But honestly, I only spent maybe two hours cleaning the animation up.  And once that was cleaned up, I just dropped in two cameras.  You know, I did one camera for one guy and another for the other.  And they're just set up on two sort of opposite sides.  And then I probably spent maybe 20 to 30 minutes on each camera just tracking and animating it by hand.  You know, kind of just going a little bit down the sequencer and reframing and then putting a key frame in.  I knew if I could get the handheld shakiness just right, it would really sell it.  And I knew I wanted to, you know, I really wanted to feel the impacts right of the combat.  At first I was thinking like, oh, maybe the camera would shake a little every time the swords would hit.  But that doesn't actually make sense.  So I kind of just came up with the idea of them like bumping into the camera or like hitting the camera by accident or something.  And it ended up working really well.  I just put in like a little bit of camera shake and kind of animated the camera when it was when it was near by the characters.  And it turned out really well.  But yeah, it's awesome to have these sort of Lego pieces of a fight scene that you can mix and match to sort of build your own choreography.

**Frame:** tutorials\frames\motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma\frame_003.jpg

### Ideas for more Battle Scene Mocap [6:33]
**Transcript:** And then you can, you know, you can set it in any setting you want, use any camera angles, you know, make it any style.  And the idea is that I'm building enough Lego pieces and I'm building blocks to eventually make a whole battle scene, you know, of any kind of scale.  So in this case, it's just a generic short sword because that was the easiest to do.  And also because I think it has a lot of uses.  But, you know, we want to do, you know, other types of swords, maybe katanas or samurai sword style stuff.  You know, broad sword, pikes spears.  Also all the sorts of things you might see in a medieval battle scene.  So let me know in the comments, you know, what other kinds of choreography you'd like to see.  You know, what could you imagine using this to create yourself?  Alright, that's enough for this video.  If you found it interesting or valuable in any way, please consider leaving a like and subscribing.  Come by the discord, show off what you're making, you know, and we love to just talk all things unrelentient filmmaking.  It's a great, really helpful supportive community and it's awesome.  I think it's turning into one of the best, you know, online resources for this kind of thing.  Alright, my name's Charlie and I will see you in the next one.

**Frame:** tutorials\frames\motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma\frame_004.jpg


---

## Structured Notes

### Core Technique
"Lego pieces" fight choreography approach: capture many short (5-10s) paired combat animations with Move.AI (markerless mocap, no suits) → chop and mix/match in UE5 Sequencer to assemble any fight scene. Two actors simultaneously in the Move.AI volume. Bake to Control Rig for wrist/weapon alignment cleanup. Manual hand-animated cameras with intentional "camera bump" timing for impact feel.

### Summary
8-minute Charlie Driscoll film breakdown of a Move.AI-powered two-actor sword fight cinematic in UE5. Workflow: hired two professional stuntmen for 2 hours → Move.AI captured full range of improv + blocked combat animations → imported into UE5, assigned to two MetaHumans with Medieval Armor pack → chopped animations into Sequencer → baked to Control Rig for cleanup (removed hand tracking on sword hand, adjusted wrist angles for sword contact) → two manually-keyframed handheld cameras (one per fighter, opposite sides) with camera bump effects at impact moments. Entire animation cleanup ≈ 2 hours; each camera ≈ 20-30 minutes.

### Key Steps
**Mocap Shoot (Move.AI):**
1. Hire choreographers/stuntmen; 2-hour shoot is sufficient for many usable clips
2. Move.AI: markerless, suitless — no setup per actor; just wardrobe that works with capture
3. Two actors simultaneously in the volume; improv + blocked choreography
4. Preview clips immediately in Move.AI; select best performances

**UE5 Assembly:**
1. Source environment from library (cathedral); evaluate existing lighting — minimal changes if it's already good
2. Drop in two MetaHumans; apply **Medieval Armor pack from Polyphoria** for clothing
3. Chop desired animations → Sequencer → assign to each MetaHuman
4. Right-click animation → **Bake to Control Rig** for manual cleanup

**Animation Cleanup (Control Rig):**
- Remove hand tracking on sword-holding hand (no need for hand animation when gripping weapon)
- Manually adjust wrist rotation keyframes so weapons actually make contact at correct angles
- Rough cleanup acceptable if camera angles + shaky cam will hide imperfections
- ~2 hours total cleanup time for a full fight scene

**Camera Work:**
1. Two cameras: one per fighter, placed on roughly opposite sides
2. Manual keyframe camera-tracking: advance timeline → reframe → add keyframe; repeat
3. ~20-30 minutes per camera
4. Handheld shakiness (small constant camera motion) to sell realism
5. "Camera bump" — instead of screen shake at sword hits, animate camera position itself slightly when fighters pass close to camera (more realistic than digital shake)

### UE Systems / Blueprints / Settings
- **Move.AI / Move Pro** — markerless suitless mocap; two actors simultaneously; no suit setup; wardrobe-friendly; previews clips in Move.AI app before export to UE
- **Bake to Control Rig** — Sequencer right-click animation → Bake to Control Rig; converts mocap to editable keyframe curves; required for weapon alignment cleanup
- **MetaHuman** — two custom MetaHumans as fighters; Medieval Armor (Polyphoria) attached as clothing
- **Weapon / prop attachment** — sword attached to hand bone; no automatic wrist tracking accuracy → must manually correct in Control Rig after baking
- **Paired animations** — 5-10s combat interaction clips where both characters perform matching moves; more useful than single-character animations for fight scenes
- **Handheld camera keyframing** — manual camera position keyframing in Sequencer; advance a few frames, reframe viewport, set key; gives organic camera movement
- **Camera bump effect** — animated camera position shift when characters pass near camera; simulates accidental physical contact vs. synthetic digital shake

### Difficulty
Intermediate. Requires Move.AI system (markerless mocap hardware/software). UE5 portion is straightforward Sequencer + Control Rig cleanup. Camera work is time-consuming but procedural. Most effort is in animation cleanup (wrist angles for weapon contact).

### UE Version
UE5 (no specific minor version; Move.AI + MetaHuman Sequencer workflow)

### Tags
mocap, move-ai, metahuman, swordfight, cinematics, sequencer, control-rig, short-film, choreography, handheld-camera

---

## Related Entries
- `moveai-and-unreal-engine-5-metahuman-cinematic---hacker.md` — Charlie Driscoll Move.AI + MetaHuman Animator cinematic pipeline
- `moveai-and-unreal-engine-5-metahuman-short-film---gigantic-joe.md` — Gigantic Joe: Move.AI + ElevenLabs + scale character short film
- `motion-capture-isnt-just-for-hollywood-any-more.md` — Josh Toonen Rococo suit mocap pipeline; similar filmmaking cycle but with different mocap system
- `metahumans-in-unreal-engine.md` — MetaHuman Blueprint structure, animation, Control Rig setup
