---
title: Slow Motion SECRETS! How to Time Warp Animation in Unreal Engine
source: YouTube
url: https://www.youtube.com/watch?v=d-_hv7IXjkM
author: Unreal Engine
ingested: 2026-06-23
ue_version: "UE5"
tags: [animation, sequencer, time-warp, slow-motion, play-rate, curves, timing, workflow, animator-tools, post-production]
extraction_status: complete
frames_dir: tutorials/frames/slow-motion-secrets-how-to-time-warp-animation-in-unreal-engine/
frame_count: 4
---

# Slow Motion SECRETS! How to Time Warp Animation in Unreal Engine

**Source:** [YouTube](https://www.youtube.com/watch?v=d-_hv7IXjkM)
**Author:** Unreal Engine
**Duration:** 10m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en In this video, I'm going to show you how to do time warp slow-mo adjustments to the timing of your animation. Now, in this project, we have that happening, but it's not happening with sort of the Unreal Engine tool method. It's happening manually. The animators manually animated the slow motion with just slower key frame data and just general animation timing. But let's say that you had animated something and you realized later, I want this slow motion moment. So, what I'll do is I'm actually going to leave this shot and go find another shot where maybe like here we've got these different moments of of great impact and fight sequences. So, let's add some slow motion to this. We'll use shot 60 as our example. He comes in, he uppercuts this dude, and does this helicopter spin. Let's Let's try some stuff. We can do one of these punches. We can obviously do the spin or maybe we'll do this wham right there. I really like this last punch because it's got all this cool chromatic aberration effects drawing stuff there. I feel like that'd be sweet. So, maybe we'll do that punch in slow-mo. Now, in this particular case, because we're looking at the full production, right, we have this whole list of subsequence data. You know, we've got the effects, we've got lighting, we've got a lot of different things all playing into this. If it were just animation, then we could apply this to just the animation track. And if I want to do a time effect to the entire shot as a whole, what I can do is I can add a new track to my sequencer. So I'll say add time warp. And there's different kinds of time warps. There's also different ways you can do this, but this is the way I'm going to go with today. Now, there are a couple different ways we can add slow motion to a shot as a whole. Uh, for example, if I go into add, there is something called a time dilation track. That's a thing. But I'm going to use time warp. And there are two kinds of time warp. a play rate curve or a time warp curve. Let's experiment with both. So, I'll start off by saying add time warp. And we'll start with the play rate curve. If I drop that in, what that's going to give me is sort of this extra little it's going to give me this extra track on top with a value of one. And one is basically the speed of time represented here. So, I've got my regular playhead and then my like representative playhead. So, if I come in here and maybe I'll go to this frame. I'll set a key on my play rate curve here. I'll go, you know, maybe two frames deeper. And I'm going to slow this down to like 0.2. So, now you can see that I'm now changing the rate of time. And it's it's an interesting thing that's happening is that my regular playhead is telling me like how fast I should be going like where the time of the timeline has, you know, continued to move through. But this little set of keys has now changed the rate of how time is progressing within the actual sequences. And that's this other orange thing. And so maybe what I'll do is I'll set this down to like 0.1, you know, actually. Let me get rid of uh one of these keys. Let me go with my my curve editor. Uh if I go to my play rate curve, I can I can see the different values. Get rid of that. Move this over here. And uh now I can go All right, here we go. And maybe I want to adjust this a little bit longer. Too too far. Be further. You can see too. I mean, realistically, you can also see that like this was not meant to be played so slow. So, I'm starting to see the uh the duplicate arms. I'm also not seeing the actual contact point, right? So, like the character is making contact here because that's where the animator intended for me to see it, but I'm now interpolating where the arm is actually connecting. Fun little fact just about Unreal is like you're able to interpolate like way down between key frames. And so, in this case, I might actually need to go in and and make some tweaks to make this work, but whatever. It's fine. And then maybe I want to have here I'll go ahead and re key the playback curve and set this back to a value of one. And so what's weird about this this particular mode is I've set a play rate curve. I've got these keys and the keys are like not exactly corresponding to the sequences that are underneath them. I'm basically keying the orange key in a way, like the orange playback curve, the the brighter one, even though the keys are it's it's strange. It's a little bit odd, I'll admit. So, if I now go in here, he does his thing. Swing, swing, attack, attack, and then it comes back to normal and then it continues. I mean, it's really easy, right? Really easy way to just slow down time and all the other stuff just works and I can rettime that really, really quickly. But I can also just say, you know what, let's try something else. Delete. And now it'll play back at normal speed once again. So if I want to try the other method, I can go add time warp curve or sorry, add time warp. And then this time I'll go to a time warp curve instead of a play rate curve. And this one, it's similar, but it's a little different. So I'll do the same thing in the same spot. I'll go right here. Time warp curve. Set a key. But this time instead of having a play rate where it's like a value of one and then 0 2 was like 20% of the speed. In this case a time warp curve is a direct control of the frame count. So here it's set to 850. But if I say you know what I want this to be like 837. What this will do is create an interpolation of the actual like frame numbers that I'm on. So if I take this and hit play, I'm going to see this animation play out. And then maybe I'll expand this and take this way further. It'll basically interpolate between frames. What was this? 835 or 831 and way over here. 878. Whatever 878 was supposed to be where this orange one is, it's now being played over here. But then I've got to go back in. I've got to sort of ramp back into regular time. uh because I am not looking at linear time. And so now this is almost like how you can ret time video reference inside of Maya if you've ever done that where I'm now directly controlling the actual frame numbers instead of the play rate. So this is more of a I'm I'm setting specific keys of the frames that I want to see at certain times. There goes that and it plays back. And so this is this is I think a little bit more confusing, a little bit harder to work with in this particular way. Um, also I don't usually like having like the time warp curve on like the full shot. I want the shot itself to sort [snorts] of contain this information. And so this process, it's really easy to do as you can see. But like where to organize it is the tricky part. I don't usually like to have those those sort of highlevel time curves on like the top level sequence. I think it makes a little bit more sense to do it actually within this shot itself because then we can control the playback like within the shot and then when you go back out to the the main edit it's sort of self-contained but depending on the way that the data is laid out. It may or may not make sense because the whole like playhead leaving the bounds of like our cropped area here like we only have however many frames we have until we hit this red line. Sometimes depending on like if you've got all the stuff broken out into subsequences or if you've got stuff cut off, you know, play with it. You might want to do it here in the shot, you might want to do it at the higher level sequence level. You typically don't want to do it like where your animation key frames are because then you're managing like key frames in time, but time itself is being adjusted by this like higher level track. That can be a mess. So, it's usually best to keep your actual key frame data separate from your like time key frame data. That way, you're just like reading animation data and adjusting that with time versus having them both like work in the same environment. I I wouldn't recommend that, but hopefully this was a cool way just so you can see, you know, how to add a really quick and easy slow motion effect without having to adjust all of your animation key frames. However, that said, if your interpolation isn't like super spot-on, you might need to do a little bit extra work to compensate for the fact that, you know, the animation wasn't originally intended to be seen so slow. Right? So, if I step through it, you can see that we go from, you know, he anticipates and he just immediately punches them. And it looks great with this timeline, but as we interpolated, we saw some of the problems and the flaws with this animation. itself. On one hand, it makes slowing time down much easier, but on the other hand, it does create a little bit of extra animation work, but is that less work than actually having to animate the entire thing fully in slow-mo yourself? Up to you. Your call. That's the whole thing with these tools in Unreal is it gives you so many options, so many different ways that you can tackle problems. And so hopefully these videos have been a fun look into how you as an individual or you as a team might go about creating your own animated projects with characters like these with tools like these in these full sequences with shots and subsequences. Hopefully this was just a helpful learning experience and I hope you get a lot out of it. And so we really hope you enjoyed these videos. Thank you so much for watching all of this. If you found this helpful and you want more of it, again I'm Sirade and you can find me over on YouTube. I've got a whole animation channel where I'd love to hear from you. Jump in the comments, let me know what you want to see. And if you'd like a more personal approach, do you want a classroom environment where you can actually ask your direct workflow questions and I can hopefully help you sort it out? I have my own courses, as you've heard me say before, and if I can, I'd love to help. But thanks so much, and happy animating.

**Frame:** tutorials\frames\slow-motion-secrets-how-to-time-warp-animation-in-unreal-engine\frame_000.jpg


---

## Structured Notes

### Core Technique
Time Warp in UE5 Sequencer: add a Time Warp track to a sequence → control playback speed over time without touching animation keyframes. Two modes: **Play Rate Curve** (speed multiplier; 1.0=normal, 0.2=20% speed) vs **Time Warp Curve** (direct frame number control — keyframe which frame number to show at which timeline position). Best practice: keep time warp track at the shot level (not animation keyframe level, not top-level sequence) for clean organization.

### Summary
10-minute Epic Animation Hub tutorial (Sir Wade / ACOM project, fight sequence Shot 60). Demonstrates adding non-destructive slow motion to a fully animated sequence by adding a Time Warp track at the sequence level. Compares two modes: Play Rate Curve (intuitive speed percentage; orange secondary playhead shows modified time; set to 0.1 for 10% speed then key back to 1.0) and Time Warp Curve (direct frame number keying; similar to Maya's retime video reference tool). Advises against: placing time warp on animation keyframe tracks (conflicting keys) or at top-level sequence (hard to organize). Tradeoff: time warp interpolates between keyframes — animation intended for normal speed may show artifacts (e.g., duplicate arms) at extreme slow motion and may require additional cleanup.

### Key Steps
1. **Add Time Warp track** to Level Sequence:
   - In Sequencer → **+ Track** → **Time Warp** (not Time Dilation — that's a separate system)
2. **Choose mode**:
   - **Play Rate Curve**: Add Time Warp → **Play Rate Curve**
   - **Time Warp Curve**: Add Time Warp → **Time Warp Curve**
3. **Play Rate Curve** (recommended for most use cases):
   - Track shows a curve with value 1.0 (normal speed) and an orange secondary playhead
   - Scrub to frame just BEFORE desired slow-mo point → set key (value = 1.0)
   - Advance 1-2 frames → set key at target speed (e.g., 0.2 = 20% speed, 0.1 = 10% speed)
   - At end of slow-mo moment → set key back to 1.0
   - Orange playhead shows the modified time position vs original playhead position
   - Use Curve Editor to smooth/adjust key tangents and timing
4. **Time Warp Curve** (frame-number-based):
   - Track shows actual frame numbers at each timeline position
   - Key a specific frame number at a specific point in time → interpolates between keyed frame numbers
   - Similar to Maya's retime video reference tool
   - More confusing; better for precise frame-level control
5. **Organization best practice**:
   - Avoid placing time warp at the **animation keyframe** level (time conflicts with actual keys)
   - Avoid placing at the very **top-level sequence** (harder to find/manage)
   - Best: place at the **shot/subsequence level** (self-contained; reads clean from parent sequence)
6. **Check for artifacts**:
   - Preview slow-mo: step through frame-by-frame
   - Animation interpolated between original keyframes — may show IK artifacts, arm duplication, missed contact frames
   - If artifacts unacceptable: either reduce slow-mo amount OR manually add extra keyframes in the animation to support the interpolation

### UE Systems / Blueprints / Settings
- **Time Warp track** — Sequencer track type; Add Track → Time Warp; two sub-types:
  - **Play Rate Curve**: speed multiplier; value 1.0=normal; value 0.1=10% speed; set ramp keys for gradual acceleration/deceleration
  - **Time Warp Curve**: direct frame-number control; key which frame # to display at each timeline position; more like video retiming
- **Time Dilation track** — different track also available; not covered in this video; system-wide time dilation
- **Orange playhead** — secondary playhead in Play Rate Curve mode; shows where in the original animation the current (time-warped) frame corresponds to
- **Curve Editor** — view time warp keys and adjust tangents; access via right-click on track or dedicated Curve Editor panel
- **Non-destructive**: original animation keyframes unchanged; time warp track adds a layer on top; delete track to restore normal speed

**Tradeoffs:**
| Method | Pros | Cons |
|--------|------|------|
| Play Rate Curve | Intuitive (speed %) | Orange/real playhead relationship can be confusing |
| Time Warp Curve | Precise frame control | Complex; harder to conceptualize |
| Manual animation (no time warp) | Full control; no artifacts | Must animate keyframes at slow speed from the start |

### Difficulty
Beginner-Intermediate. Adding the track is trivial. Understanding Play Rate vs Time Warp curve behavior requires a bit of mental model building. Managing interpolation artifacts at extreme slow-mo is intermediate.

### UE Version
UE5 (ACOM project; same animation hub tutorial series; feature available in UE4 as well)

### Tags
animation, sequencer, time-warp, slow-motion, play-rate, curves, timing, workflow, animator-tools, post-production

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [1:02] tutorials/frames/slow-motion-secrets-how-to-time-warp-animation-in-unreal-engine/frame_000.jpg
- [3:07] tutorials/frames/slow-motion-secrets-how-to-time-warp-animation-in-unreal-engine/frame_001.jpg
- [5:42] tutorials/frames/slow-motion-secrets-how-to-time-warp-animation-in-unreal-engine/frame_002.jpg
- [8:18] tutorials/frames/slow-motion-secrets-how-to-time-warp-animation-in-unreal-engine/frame_003.jpg

## Related Entries
- `mastering-the-ue5-tweener-tool-push-pull-overshoot-animation.md` — Tween Tool; timing polish at the keyframe level (different approach to timing adjustment)
- `ue5-curve-editor-20-new-lattice-tool-curve-scaling-hacks-ue-56.md` — Curve Editor 2.0; manages animation timing at keyframe level (complementary to time warp)
- `non-destructive-animation-in-ue5-layered-control-rigs-explained.md` — other non-destructive animation overlay techniques in Sequencer
- `motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter.md` — animation timing/blending; clip-level timing tools
