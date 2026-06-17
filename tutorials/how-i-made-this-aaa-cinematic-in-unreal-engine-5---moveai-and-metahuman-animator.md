---
title: How I made this AAA Cinematic in Unreal Engine 5 - Move.Ai and Metahuman Animator short film
source: YouTube
url: https://www.youtube.com/watch?v=LpRGFkk3b0k
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.x"
tags: [mocap, metahuman, metahuman-animator, move-ai, short-film, mafia, custom-metahuman, scan-store, hand-pose-library, ue5]
extraction_status: complete
frames_dir: tutorials/frames/how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator/
frame_count: 8
---

# How I made this AAA Cinematic in Unreal Engine 5 - Move.Ai and Metahuman Animator short film

**Source:** [YouTube](https://www.youtube.com/watch?v=LpRGFkk3b0k)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 10m15s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In this video, I'll show you how I made this mafia-themed game teaser in 40 hours of work.  Using AI-powered performance capture and Unreal Engine 5, I was able to achieve results that would have required in orders of magnitude bigger team and budget just a few years ago.  By the end of this video, you will see that these powerful filmmaking tools once reserved for AAA studios might be more attainable than you think.  But first, enjoy the film.

**Frame:** tutorials\frames\how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator\frame_000.jpg

### Short Film [0:27]
**Transcript:** I'm going to show you how I made this game.  Apologies for the wait and it takes some dude's office.  You ain't a dude's office, I didn't think so.  Did you know that one of the most loyal animals in the world are horses?  Most people think dogs are the most loyal, which they are.  But it's horses who can always depend on them.  Snakes, on the other hand, are codnivy, sneaky, double crossing.  But the way they think, the way they're going to get out of circumstances, the complete opposite of a fine stallion.  I hope that God's you a stallion.  It'd be a shame if you didn't doubt that it'd be a snake.  Um...  Um...  Please, you have to help me. He's not telling the truth.  Shut the... God.  You shut your goddamn mouth or I'll rip your tongue out, shove it down your goddamn throat.  You're gonna bump me either way.  I'm not the one that got the thing.  He is.  Prove that you're a stallion.  Prove to me that I can trust you blindly.  Please, he's lying.  Whatever he's telling you isn't true.  Can it?  You the awful guy without knowing if he's truly guilty or not.  I have a family.  Kids.  People who depend on me to what?  Mother.  Oh!  Number, Chit-Chit. Make your choice.  Alright, th...

**Frame:** tutorials\frames\how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator\frame_001.jpg

### Performance Capture Tools Used [3:20]
**Transcript:** This short film was actually written as a teaser for a potential mafia-themed game  and was sent to me by a viewer of the channel, which was awesome.  So, thank you.  Anyway, for this project, I used my usual performance capture tech stack, so to speak,  which included MovePro, which is MoveAI's multi-camera motion capture solution.  I'm using 6 GoPro10s running at 120FPS.  For the face capture, I'm using MetaHumanAnimator, which requires an iPhone 12 or newer.  The phone is held in place with a Rococo head rig, which is $300 and totally worth it  if you have multiple people using the head rig because it's adjustable.  And for the voice morphing, I used 11 labs.  You shut your goddamn mouth, or I'll rip your tongue out, shove it down your gut and throw it.  Peace.  Now, a license for MovePro costs $7,000 per year.  This allows for capturing up to two people at a time.  But with the ability to add as many as, say, 20 cameras if you want.  This is by far the most expensive of all the tools used in this workflow.  But you can actually achieve pretty similar results with much cheaper motion capture solutions,  including MoveAI's iPhone app, MoveOne, or Radical Motion, which I really wa...

**Frame:** tutorials\frames\how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator\frame_002.jpg

### Performance Capture Tutorial Link [4:51]
**Transcript:** I have a complete in-depth tutorial right here on this channel, completely free,  that shows how to get cinematic character animation with Metahumans.  And all this is done using tools that are very cheap or completely free.  Capturing all the animations for this film only took an hour or so.

**Frame:** tutorials\frames\how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator\frame_003.jpg

### Processing the Animations [5:10]
**Transcript:** But the footage has to be uploaded to MoveAI's online platform for processing,  where each clip can take an hour or two to process, depending on the length.  The face animation is easy to process using Unreal Engine's built-in tool Metahuman animator,  but still took a few hours to process all the different face animations.  The bulk of the work came from actually setting up the scenes and doing the actual cinematography.  Now, I'm curious to know what you think about the quality of the motion capture in this video.  I think it turned out pretty good considering there is very little cleanup on these animations,  at least compared to what I've gotten in the past.  I've gotten the raw animation to be far less jittery,  but I feel like some of these animations could have still used a tiny bit of smoothing on the curves  to give them just a little more feeling of weight.  The hands definitely still needed some fixing,  but they're pretty easy to clean up using the hand pose library I have built up over time.  Now, Movie Eye is pretty awesome when it comes to capturing multiple actors at the same time,  since it really gets the actors positions in space and relative to each other really...

**Frame:** tutorials\frames\how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator\frame_004.jpg

### Scan Stone and Custom Metahuman Work [6:57]
**Transcript:** So I wanted to try out using some meta-humans from the scan store.  They sell extremely detailed scans of people that are easily compatible with meta-humans,  with higher resolution skin and wrinkle maps.  They also just look a little less meta-human-y for lack of a better term.  Anyway, now doing custom meta-human work is still something that is not quite easy,  or fast enough for me to have incorporated into my workflow yet.  So I had an artist do some work on them to get the injuries and teeth in place.  Here he's working in substance painter,  and I'm not exactly sure what he's doing in this footage, but it looks cool, and you get the idea.  Now every Mafia movie needs some sort of parable or story about animals and betrayal or something,

**Frame:** tutorials\frames\how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator\frame_005.jpg

### Animating Walking Down Stairs and Through the Environment [7:38]
**Transcript:** and this one was no exception.  This turned out to be a lot of walking and talking,  and through an environment with a lot of turns and stairs.  But I only have a small space to record the mocap in,  so I just had to walk back and forth in the space and piece the animations together in the sequencer.  I also don't have a great way to do stairs.  I can do small stairs using some Apple boxes, but nothing like a full staircase.  This is definitely an advantage that inertial suits have, like Rococo or XSense,  and that you can take them in more interesting places more easily.  So I decided to try using a single camera solution by Radical Motion,  but this was really the best I could do.  So yeah, that was definitely not going to work.  I ended up just getting an animation from Mixamao and showing a few shots of them going down the stairs.  And shortcuts like that just work sometimes.  People may say this still looks like a game, or still has an element of the uncanny valley to it,

**Frame:** tutorials\frames\how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator\frame_006.jpg

### Uncanny Valley and Where is this Going? [8:48]
**Transcript:** which I can totally see.  But look where the tech is now, and where you think it will go in just a year or two,  or by Unreal Engine 6.  My guess is a lot better.  MetaHuman Animator, the tool in Unreal Engine that does the face animation,  didn't even exist until last year, and now makes AAA quality face animation possible using just an iPhone.  It seems clear to me that this medium will grow significantly,  and it won't be long until more mainstream content is made with it.  In fact, the last season of Love Death and Robots had an episode made in Unreal Engine using MetaHuman,  so start learning these tools now, they will evolve quickly.  And even if you don't plan on working in the industry in any way,  this gives you the ability to create movies of all kinds that you might have had in your head,  or some concept that you've had.  You can do that now way cheaper than was possible before.  I also think there will be some really interesting crossover with the performance capture industry and VR,  which is actually a topic I plan to make an entire video on.  If anything, it's really good for Previs, and I have a whole video that dives into that process right here.

**Frame:** tutorials\frames\how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator\frame_007.jpg


---

## Structured Notes

### Core Technique
Full production breakdown of a 40-hour mafia-themed game teaser cinematic made with Move.AI Pro multi-cam (6 GoPro 10s at 120fps) for body capture, MetaHuman Animator for face capture, 3D Scan Store custom MetaHuman heads for photorealistic characters, and hand pose library cleanup — demonstrating AAA-quality results achievable by a small team.

### Summary
Charlie Driscoll presents a behind-the-scenes breakdown of a mafia-themed game teaser cinematic made in approximately 40 hours using Unreal Engine 5. Move.AI Pro ($7,000/year license) captures up to two actors simultaneously with 6 GoPro 10 cameras at 120fps; MetaHuman Animator provides free face capture via iPhone 12+ in a Rokoko head rig. 3D Scan Store heads with high-resolution skin maps make characters less "MetaHuman-y." A contract artist handles custom MetaHuman work (injuries, teeth) in Substance Painter. The bulk of production time goes to scene setup and cinematography. Animation cleanup uses a hand pose library. Stairs and complex environments remain a known limitation addressed with Mixamo stock animations.

### Key Steps
1. Use Move.AI Pro (6 GoPro 10s, 120fps) to capture 1-hour acting session (multiple takes of all scenes).
2. Upload footage to Move.AI cloud platform; process each clip (1-2 hours per clip); download FBX per actor.
3. Process face animations in MetaHuman Animator; sync body/face using hand-clap mouth-pop technique.
4. Commission character artist (Upwork) to add injuries/teeth to 3D Scan Store MetaHuman heads in Substance Painter.
5. Import and retarget animations to MetaHumans in Sequencer; perform minimal cleanup (hand pose library for hands).
6. For stairs/complex movement: use single-camera solution (Radical Motion) or Mixamo stock animations as fallback.
7. Build environment scenes; set up cameras; perform animation cleanup on curves as needed.

### UE Systems / Blueprints / Settings
- Move.AI Pro multi-cam (6 GoPro 10s, 120fps, 2-actor simultaneous capture, $7,000/year)
- MetaHuman Animator (face capture, iPhone 12+ required, Rokoko head rig $300)
- Level Sequencer (multi-actor animation, camera cuts)
- Hand Pose Library (accumulated hand pose corrections)
- 3D Scan Store head integration with MetaHuman (high-res skin textures)
- Substance Painter (custom MetaHuman material work, outsourced)
- Radical Motion (single-camera mocap, tested as fallback for stairs — results poor)
- Mixamo (fallback for stair/complex movement)
- ElevenLabs (voice morphing)

### Difficulty
Intermediate

### UE Version
5.x

### Tags
mocap, metahuman, metahuman-animator, move-ai, short-film, mafia, custom-metahuman, scan-store, hand-pose-library, ue5

---

## Related Entries
- `how-i-use-moveai-and-metahumans-to-achieve-aaa-character-animation-in-unreal-eng.md` — earlier two-actor Move.AI pipeline overview with orc/knight scene
- `cinematic-motion-capture-with-move-one-and-metahuman-animator---unreal-engine-54.md` — budget version of this same pipeline using Move One instead of Pro
- `moveai-unreal-engine-54-motion-capture-short-film-using-custom-orc-metahumans---.md` — orc MetaHuman short film using custom characters in UE 5.4
