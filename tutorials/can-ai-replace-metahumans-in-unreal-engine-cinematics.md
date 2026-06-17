---
title: Can AI Replace MetaHumans in Unreal Engine Cinematics?
source: YouTube
url: https://www.youtube.com/watch?v=NLVMJX-5ahc
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.x"
tags: [ai-video, kling, metahuman, mocap, overcrowd, compositing, character-replacement, nano-banana, quickmagic-ai, metahuman-animator, wardrobe, ue5]
extraction_status: complete
frames_dir: tutorials/frames/can-ai-replace-metahumans-in-unreal-engine-cinematics/
frame_count: 9
---

# Can AI Replace MetaHumans in Unreal Engine Cinematics?

**Source:** [YouTube](https://www.youtube.com/watch?v=NLVMJX-5ahc)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 13m9s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Can AI replace MetaHumans in Unreal Engine? [0:00]
**Transcript:** Can AI replace metihumans or 3D characters in Unreal Engine Cinematics?  Well, that answer depends on how you define a few things.  The short answer is not yet.  At least not really.  Not if you're going for a pixel perfect, highly robust animation pipeline.  But if you're open to a little experimentation and are a little AI curious like myself,  the answers start to get pretty interesting.  So what you're seeing here is Kling01 selectively replacing a metihuman version of me  with a more true-to-life AI version of me.  That AI version is generated from just a handful of reference photos of my face  and the outfit is made from just a single reference image made in Google's NanoBanana.  And in this video, I'll show you the very simple pipeline I used using Kling,  motion capture and Unreal Engine to achieve these shots.

**Frame:** tutorials\frames\can-ai-replace-metahumans-in-unreal-engine-cinematics\frame_000.jpg

### What Kling o1 is actually doing (and what it isn’t) [1:04]
**Transcript:** Hi, I'm Charlie and don't worry, I'm not replacing myself with an AI version.  I'm not in my studio today, I'm actually out visiting family for the holidays.  And what you're seeing is actually Kling's brand new generative video model,  the motion control feature which dropped literally as I was making this video.  So I decided to sort of integrate it in and use it on these talking heads that I'm doing.  And we'll talk a little bit more about it later because it's very relevant.  So for this video, I spent hundreds of dollars stress testing the brand new Kling01 generative video model  with Unreal Engine 5.  I wanted to see where this workflow actually holds up, where it falls apart,  and what it might realistically look like in the near future.  Okay, so this is a test to see just how well MetaHumanAnimator works with the scan of my own face.  Now the idea of doing an AI style transfer on footage using something like ComfyUI  has been around for a while now.  And that's still the more professional, controllable way to do this.  Reallusion has also released a new plugin that does something very similar.  And I'm planning on testing that very soon.  But all of that is really hard.  ...

**Frame:** tutorials\frames\can-ai-replace-metahumans-in-unreal-engine-cinematics\frame_001.jpg

### Why wardrobe is the biggest bottleneck in Unreal filmmaking [2:26]
**Transcript:** Kling was showing off this new feature in their brand new01 model,  which swaps wardrobes based on just a reference image.  And honestly, it looked way too good to be true.  You see in Unreal Engine and MetaHuman filmmaking, wardrobes is definitely a big bottleneck.  Now don't get me wrong, there are tons of amazing assets on the fab marketplace for MetaHuman's.  And I've used a lot of them.  They've made my videos look incredible.  And Kling is not a replacement for those assets.  But if you need something specific, like a very particular type of armor from a specific culture or time period,  it usually just doesn't exist on the marketplace.  So your options are either higher in an artist to build and rig it for you,  or you settle for something that's close enough.  Imagine you could dress your characters any way you wanted to.  With just a couple images, you get consistent outfits across all your shots.

**Frame:** tutorials\frames\can-ai-replace-metahumans-in-unreal-engine-cinematics\frame_002.jpg

### Real-world footage tests and AI wardrobe swaps [3:28]
**Transcript:** In these early tests, I'm just using real world footage of myself as the base.  I generated a clean front and back reference image for an outfit,  fed that into Kling, and that becomes the wardrobe for the character in the shot.  And honestly, the results kind of blew my mind.  Stuff like the metal armor actually looks like it's receiving the environmental lighting and some reflections.  And the cloth physics on this cowboy outfit are kind of insane.  And what's really crazy is you can even do pets like dogs.  Whoa!  So just to be clear what's happening here, Kling is replacing me entirely, both the outfit and the face.  If I just told Kling to replace my outfit using the reference image,  it would just turn me into a random dude wearing the outfit.  So I had to create a sort of mini-lora of myself, which is actually a feature Kling01 has called Elements.  This allows you to upload several reference photos for characters, objects, environments, and outfits,  and then use those elements in your prompts.  The idea is to give your characters more consistency across different shots.  So by telling Kling to replace the blonde man in the video with the Charlie character element,  wearing...

**Frame:** tutorials\frames\can-ai-replace-metahumans-in-unreal-engine-cinematics\frame_003.jpg

### Identity consistency, LoRA / Elements, and lip-sync limits [5:00]
**Transcript:** You can take photos from real world references, or, say, historical images.  In this case, I took a photo of a vase and told Nano Banana to create a front and back reference image of the blue suit in the photo.  I can then use that reference image to make myself wearing it using Kling.  Darn, who knows what I'm saying?  Now, as you can see, LipSync is pretty hit or miss with the AI recreation, and honestly, it's mostly miss.  Kling01 does have an additional lip sync pass, where it will sort of composite generated lips over your character.  And this can be done from either text to speech, or from a reference audio track.  But the results never really looked that great to me.  So I'm kind of resigned to LipSync just not quite being there with this technology yet, although that's something I expect to improve very soon.  In fact, as I mentioned earlier, while I was making this video, Kling actually dropped their brand new Motion Control feature with their 2.6 video generator.

**Frame:** tutorials\frames\can-ai-replace-metahumans-in-unreal-engine-cinematics\frame_004.jpg

### Hallucinations, prompt discipline, and AI stability [6:09]
**Transcript:** And this allows you to puppet a character with a reference video for the animation, and a reference image for what you want your character to look like.  And that's what I've been using for all of these talking head videos of myself.  And so looking at this, I think the lip sync with the Kling01 sort of swapping model, that's going to improve really soon.  So here I did a test with a random cowboy image I generated, and it recreates the camera movement really well.  Of course, it is making up the rest of my studio outside the image, so it's not quite what I want to use yet, but it's still very compelling.  Now Kling01 is still a little unstable, and crazy hallucinations still happen.  Occasionally something appears that wasn't there before.  I even had a few runs where the environment changed completely.  And yes, honey, that woman coming out of the bedroom is definitely AI generated I swear.  But I found that if I followed a very strict prompt structure, explicitly telling it to keep everything the same except the character in Wardrobe, the results were surprisingly consistent.  So the real world tests were looking really good, but it comes with an obvious limitation that I'm sure...

**Frame:** tutorials\frames\can-ai-replace-metahumans-in-unreal-engine-cinematics\frame_005.jpg

### Why Unreal Engine unlocks real creative freedom [7:26]
**Transcript:** What I really wanted was the freedom of camera movement and blocking and environments that I get from Unreal Engine and Motion Capture.  Once I moved this workflow into Unreal using many humans as placeholders driven by motion capture, it really started to look cool.  So one test I wanted to do was to see just how much of the scene I could generate using really basic placeholders in Unreal.  So then I started to layer it.  I would do one pass for one building, then another pass for a different structure, and then I did a third pass for the weather in this case heavy snow.  I tried adding some moving cars, I tried using moving cubes as references and telling Kling to replace them with a horse drawn carriage, and the objects would appear, but they wouldn't move.  They just sat there.  So my takeaway from these tests are that Kling is best used to change one or two specific things about the shot.  In this case, the character and the wardrobe, and ideally everything else like the environment would be handled by Unreal Engine.

**Frame:** tutorials\frames\can-ai-replace-metahumans-in-unreal-engine-cinematics\frame_006.jpg

### Stress testing in Unreal (DMX stage, Electric Dreams, crowds) [8:31]
**Transcript:** So I moved to the Unreal Engine sample projects, specifically the DMX lighting sample and the Electric Dreams procedural generation demo.  The DMX scene was great for stress testing Kling because of all the crazy effects and the moving lights.  I went to Suno and generated a song, I played it back to capture the performance, processed the body with quick magic AI, and processed the face with metahumananimator.  Now in the background, I wanted a huge cheering crowd.  So I used my crowd simulation plugin Overcrowd combined with a pack of actor core characters from Real Lusion to fill the stadium with thousands of cheering fans.  For the rock star look, I used Nano Banana to take the same reference images from my regular character element, and then give them an 80s rocker haircut.  And then filled it to generate an 80s rocker style outfit with French.  And this is what it gave me, so I rolled with it.  And the results of these tests were pretty interesting.  I'm definitely pushing the AI model with these camera movements, and you can see the face breaking down at a distance.  But the body still looks pretty good.  And up close, there are definitely some moments that feel realistic.  A...

**Frame:** tutorials\frames\can-ai-replace-metahumans-in-unreal-engine-cinematics\frame_007.jpg

### Fight choreography, wide-shot hacks, and final takeaways [10:41]
**Transcript:** These are tightly choreographed two-person sword fighting animations with lots of contact and weapon movement, which usually breaks generative video models immediately.  I exported these shots with no motion blur, which made it much easier for the AI to track the swords.  Then I replaced the blue and yellow meta humans with reference images of two nights, and honestly it did a better job than I expected.  So another important limitation showed up when I started doing wider shots.  The cling is kind of near-sighted. If the character is too small in the frame, it won't reliably swap them.  And as filmmakers, we obviously want wide shots. So I came up with a little bit of a cheat.  I rendered the same camera move twice, once very wide with an 18-millimeter lens, keeping the character centered as the camera moved.  Then I rendered it again very tight at 300 millimeters, so the character filled the whole frame.  I ran the close-up through cling, so it would lock onto the character, and then in Premiere I scaled that result down, and composited it back over the wide shot with a soft feathered mask.  It's not elegant, but it works.  Now, the reason this got expensive fast is because it's ...

**Frame:** tutorials\frames\can-ai-replace-metahumans-in-unreal-engine-cinematics\frame_008.jpg


---

## Structured Notes

### Core Technique
Hybrid UE5 + Kling 01 AI video pipeline: mocap-driven MetaHuman as body placeholder → render from UE → Kling 01 replaces character face/wardrobe using Kling Elements (identity LoRA from reference photos) + NanoBanana outfit reference images. Wide-shot hack: dual-render (18mm wide + 300mm tight) → Kling tight version → composite back over wide.

### Summary
Charlie Driscoll stress-tests Kling 01 generative video model as a MetaHuman visual replacement tool. Core idea: UE5 handles camera freedom, blocking, environment, and mocap animation — Kling 01 handles character stylization (face + wardrobe). Kling Elements feature creates a character identity from 3–5 reference photos (mini-LoRA). NanoBanana generates consistent front/back outfit reference images. Key findings: best for replacing one or two things per pass; UE handles environment. LipSync unreliable. Wide-shot limitation solved with dual-render composite hack. No motion blur export helps AI track fast objects. OverCrowd + ActorCore for crowd backgrounds. Kling Motion Control (2.6 model) for talking-head puppet animation.

### Key Steps
1. **Capture mocap**: QuickMagic AI → body; MetaHuman Animator → face; retarget to MetaHuman in UE5
2. **Build UE shot**: MetaHuman as placeholder; set camera, environment, lighting; OverCrowd + ActorCore for crowds
3. **Generate outfit reference**: NanoBanana (or similar) → front + back view of desired costume from single reference image
4. **Create Kling Element**: upload 3–5 reference photos of actor → Kling Elements → consistent character identity across shots
5. **Render with no motion blur**: disabling motion blur helps AI track fast-moving objects (swords, weapons)
6. **Run through Kling 01**: strict prompt — "replace [description] with [character element] wearing [outfit element], keep everything else exactly the same"
7. **Wide-shot hack**: render same move twice — (a) 18mm wide full composition, (b) 300mm tight with character filling frame → run (b) through Kling → Premiere: scale (b) down, composite over (a) with soft feathered mask
8. **Layered passes**: separate Kling passes per complex element (building, structure, weather); composite results
9. **Kling Motion Control** (v2.6): feed reference video (animation source) + reference image (character look) → talking head or motion-puppeted output

### UE Systems / Blueprints / Settings
- **MetaHuman** — body/motion placeholder for AI replacement pipeline
- **MetaHuman Animator** — facial mocap processing
- **OverCrowd plugin** (FAB, Charlie Driscoll) + **ActorCore** (Reallusion) — crowd/army fill
- **Render settings** — disable motion blur for AI-trackable output
- **DMX sample / Electric Dreams** — stress-test environments used

### Difficulty
Advanced (experimental; requires Kling, NanoBanana, compositing in Premiere)

### UE Version
UE5 (MetaHuman Animator, OverCrowd, FAB)

### Tags
ai-video, kling, metahuman, mocap, overcrowd, compositing, character-replacement, nano-banana, quickmagic-ai, metahuman-animator, wardrobe, ue5

---

## Related Entries
- Other Charlie Driscoll tutorials (QuickMagic AI, Move.AI, OverCrowd crowds, Mimem.ai)
- MetaHuman Animator facial capture tutorials
- OverCrowd crowd simulation tutorials
