---
title: How I made this AAA Cinematic in Unreal Engine 5 - Move.Ai and Metahuman Animator short film
source: YouTube
url: https://www.youtube.com/watch?v=LpRGFkk3b0k
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-23
ue_version: "UE5"
tags: [cinematics, production-breakdown, mocap, metahuman, move-ai, animation, sequencer, character, performance-capture]
extraction_status: complete
frames_dir: tutorials/frames/how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator/
frame_count: 8
---

# How I made this AAA Cinematic in Unreal Engine 5 - Move.Ai and Metahuman Animator short film

**Source:** [YouTube](https://www.youtube.com/watch?v=LpRGFkk3b0k)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 10m15s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en in this video I'll show you how I made this Mafia themed game teaser in 40 hours of work using AI powered performance capture and Unreal Engine 5 I was able to achieve results that would have required an orders of magnitude bigger team and budget just a few years ago by the end of this video you will see that these powerful film making tools once reserved for AAA Studios might be more attainable than you think but first enjoy the film [Music] apologies for the wait it take care of some D droppers you ain't a d dropper are you didn't think so did you know that one of the most loyal animals in the world are horses most people think dogs are the most loyal which they are but it's horses you can always depend on snakes on the other hand are kiving sneaky double crossing that do anything to wiggle out of circle ances the complete opposite of a fine stallion I hope beg God you stallion it'd be a shame if you turned out to be a snake please you have to help me he's not telling the truth shut the up you shut your godamn mouth or I'll rip your tongue out shove it down your God throat [Music] peace you're going to bump me either way I'm not doing the God thing he is prove that you're a stallion prove to me that I contr trust you blindly please he's lying whatever he's telling you isn't true can it you to off a guy without knowing if he's truly guilty or not I have a family kids people who depend on me to live mother not with the chitchat make your choice all right thanks for watching this short film was actually written as a teaser for a potential Mafia themed game and was sent to me by a viewer of the channel which was awesome so thank you anyway for this project I used my usual performance capture Tech stack uh so to speak which included move Pro which is move ai's multi- camera motion capture solution I'm using six GoPro 10s running at 120 FPS for the face capture I'm using metahuman animator which requires an iPhone 12 or newer the phone is held in place with a roko head rig which is $300 and totally worth it if you have multiple people using the headrig uh because it's adjustable um and for the voice morphing I used 11 Labs you shut your godam mouth or I'll rip your tongue out shove it down your God throat now a license for move Pro costs $7,000 per year this allows for capturing up to two people at a time uh but with the ability to add as many as say 20 cameras if you want this is by far the most expensive of all the tools used in this workflow but you can actually achieve pretty similar results with much cheaper motion capture Solutions including move ai's iPhone app move one or radical motion which I really want to do a video about uh if you want to know how to do full performance capture on a budget I have a complete in-depth tutorial right here on this channel completely free that shows how to get cinematic character animation with metahumans and all this is done using tools that are very cheap or completely free capturing all the animations for this film only took an hour or so uh but the footage has to be uploaded to move ai's online platform for processing where each clip can take an hour or two to process depending on the length the Face animation is easy to process using Unreal engines built-in tool metahuman animator but still took a few hours to process all the different face animations the bulk of the work uh came from actually setting up the scenes and doing the actual cinematography now I'm curious to know what you think about the quality of the motion capture in this video I think it turned out pretty good considering there's very little cleanup on these animations at least compared to what I've gotten in the past uh I've gotten the raw animation to be far less jittery but I feel like some of these animations could have still used a tiny bit of smoothing on the curves to give them just a little more feeling of weight uh the hands definitely still needed some fixing but they're pretty easy to clean up using the hand pose Library I have built up over time now move AI is pretty awesome when it comes to capturing multiple actors at the same time since it really gets the actors positions in space and relative to each other uh really well but since I was acting out all the parts myself I had to correct some things like eyelines or in this case the hand position pulling the bag off the head and I did a few shortcuts to make the process faster so anything that had any sort of hand interaction happened off screen like when he hands him the gun here you can see I had to hold the cigarette away from my face so it wouldn't interfere with the face capture and then manually adjust the animation to get it to line up so I wanted to try out using some humans from the scan store they sell extremely detailed scans of people that are easily compatible with metahumans with higher resolution skin and wrinkle Maps they also just look a little less metahuman for lack of a better term anyway now doing custom metahuman work is still something that is not quite easy or fast enough for me to have incorporated into my workflow yet so I had an artist do some work on them to get the injuries and teeth in place um here he's working in substance painter and I'm not exactly sure what he's doing in this footage but it looks cool and you get the idea now every Mafia movie needs some sort of parable or story about animals and betrayal or something and this one was no exception uh this turned out to be a lot of walking and talking uh and through an environment with a lot of turns and stairs uh but I only have a small space to record the m in so I just had to walk back and forth in the space and piece the animations together in the sequencer I also don't have a great way to do stairs uh I can do small stairs using some apple boxes but nothing like a full staircase this is definitely an advantage uh that inertial suits have like roko or accents and that you can take them in more interesting places more easily so I decided to try using a single camera Solution by radical mode uh but this was really the best I could do so yeah that was definitely not going to work I ended up just getting an animation from mixo and showing a few shots of them going down the stairs and shortcuts like that just work sometimes people may say this still looks like a game or still has an element of The Uncanny Valley to it which I can totally see uh but look where the tech is now and where you think it will will go in just a year or two or by Unreal Engine 6 my guess is a lot better metahuman animator the tool in Unreal Engine That does the Face animation didn't even exist until last year and now makes AAA quality Face animation possible using just an iPhone it seems clear to me that this medium will grow significantly and it won't be long until more mainstream content is made with it in fact the last season of Love death and robots had an episode made an Unreal Engine using metahumans so start learning these tools now they will evolve quickly and even if you don't plan on working in the industry in any way this gives you the ability to create movies of all kinds that you might have had in your head or you know you know some concept that you've had uh you can you can do that now way way cheaper than was uh possible before uh I also think there will be some really interesting Crossover with the performance capture industry and VR uh which is actually a topic I plan to make an entire video on if anything uh it's really good for previs and I have a whole video that dives into that process right here

**Frame:** tutorials\frames\how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator\frame_000.jpg


---

## Structured Notes

### Core Technique
Mafia game teaser cinematic breakdown (40 hours) using Move AI MovePro (6 GoPro 10s, 120FPS multi-cam) + MetaHuman Animator (iPhone + Rokoko head rig $300) + 3D Scan Store MetaHumans + ElevenLabs voice morph. Key practical lessons: off-screen hand interactions, cigarette-away-from-face trick, Mixamo for stair descent, Hand Pose Library for cleanup. Budget alternative: Move AI Move One (iPhone app) or Radical Motion.

### Summary
Charlie Driscoll's Mafia-themed game teaser breakdown demonstrates the full performance-capture pipeline using commercially available tools. Move AI MovePro: 6 GoPro 10s in 360° rig running at 120FPS → upload to Move AI cloud → 1-2hr processing per clip → retarget to MetaHuman. MetaHuman Animator: iPhone 12+ in Rokoko adjustable head rig ($300) → face capture processed in UE5. 3D Scan Store heads for higher-realism skin (custom injury/teeth work in Substance Painter by artist collaborator). All roles performed solo → challenges: eyeline corrections, hand position for off-screen interactions, cigarette held away from face to avoid tracker confusion. Small capture volume → walk back and forth, stitch in Sequencer. Stair problem solved with Mixamo stair animation + minimal stair shots. Hand Pose Library for finger cleanup. ElevenLabs voice morphing for dialogue. Budget alternatives noted: Move One (iPhone app) or Radical Motion for body; MetaHuman Animator works with just iPhone.

### Key Steps

**Tech stack setup:**
1. Move AI MovePro: 6 × GoPro 10 at 120FPS in circular rig (can expand to 20 cams)
2. Upload raw footage to Move AI online platform → wait 1-2 hrs per clip for processing
3. Download processed animation → retarget to MetaHuman skeleton in UE5
4. MetaHuman Animator: iPhone 12+ in Rokoko adjustable head rig → film face performance
5. MetaHuman Animator (UE5 built-in tool) → process face footage → apply to MetaHuman face rig
6. ElevenLabs: record dialogue → voice-morph per character

**Solo actor tricks:**
- Off-screen hand interactions: hand-off of objects (gun, bag) happens outside frame to avoid fake-looking hand contact
- Cigarette held away from face when near mouth to prevent facial tracking interference
- Eyeline corrections: manually offset in Sequencer when acting both parts
- Walk back and forth in small space → stitch together in Sequencer for longer walking scenes
- Stairs: no tall staircase in capture volume → use Mixamo stair descent animation + show only brief shots

**MetaHuman quality enhancement:**
1. 3D Scan Store: purchase MetaHuman-compatible head scans (high-res skin/wrinkle maps)
2. Import and replace head in MetaHuman; commission artist for injury/teeth customization (Substance Painter)
3. Hand Pose Library: build library of hand poses over time → apply to fix finger positions

**Budget alternatives:**
- Body: Move AI Move One (iPhone app, no GoPros) or Radical Motion
- Body + Face: MetaHuman Animator + iPhone is free/low-cost without head rig; add Rokoko rig for stability

### UE Systems / Blueprints / Settings
- **Move AI MovePro**: 6-20 camera markerless multi-cam system; $7,000/year; captures 2 actors simultaneously; output directly to MetaHuman-compatible FBX
- **Move AI Move One**: budget iPhone app alternative; single camera; less accurate than multi-cam
- **Radical Motion**: another budget body mocap solution (AI-based, single camera)
- **MetaHuman Animator**: UE5 built-in tool; iPhone 12+ face capture; processes .move files from Rokoko head rig; outputs face animation directly to MetaHuman blend shapes
- **Rokoko head rig**: adjustable phone mount; $300; works with MetaHuman Animator; adjustable for multiple actors
- **Hand Pose Library**: personal library of keyframed hand poses in UE5; used for fast hand cleanup on animation tracks
- **3D Scan Store**: photogrammetry human head scans; MetaHuman-compatible; significantly more realistic skin than default MetaHuman heads

### Difficulty
Advanced (full pipeline including mocap processing, retargeting, compositing workarounds)

### UE Version
UE5

### Tags
[cinematics, production-breakdown, mocap, metahuman, move-ai, animation, sequencer, character, performance-capture]

---

## Related Entries
- how-i-made-this-aaa-battle-scene-in-unreal-engine-5.md (same author, naval battle with same Move AI pipeline)
- how-i-created-a-massive-crowd-of-metahumans-for-a-brutal-gladiator-film---unreal.md (same author, OverCrowd + Move AI)
- faster-than-ai-and-7-times-the-fun-speed-up-animation-and-get-exactly-what-you-w.md (Rokoko Smartsuit body mocap — inertial suit alternative)
