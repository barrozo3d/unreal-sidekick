---
title: Mastering the UE5 Tweener Tool: Push Pull & Overshoot Animation
source: YouTube
url: https://www.youtube.com/watch?v=oUPOBsCrWwE
author: Unreal Engine
ingested: 2026-06-23
ue_version: "UE5"
tags: [animation, sequencer, curves-editor, tween-tool, keyframing, polish, workflow, animator-tools, blend, overshoot]
extraction_status: complete
frames_dir: tutorials/frames/mastering-the-ue5-tweener-tool-push-pull-overshoot-animation/
frame_count: 4
---

# Mastering the UE5 Tweener Tool: Push Pull & Overshoot Animation

**Source:** [YouTube](https://www.youtube.com/watch?v=oUPOBsCrWwE)
**Author:** Unreal Engine
**Duration:** 11m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** In this video, I'm going to walk you through each of the different modes that we have in the tween tool to adjust the keys on your curves and start blending between your different poses. Let's talk about the tween tool. I think a lot of us are familiar with it and how it works in other tools. Let's dive into what Unreal has to offer us. So here I am in shot number, what shot is this? This is shot 65. We've got beta here, grabbing and lifting this big old thing and throwing it. I've extended the shot a little bit so that we have a little more runtime at the end just to sit with the pose. Now, what we're going to do is I'm going to show you how the throw can be modified using the tween tools. With all this motion in mind, I want to just grab the main controls to pilot this animation. So I'm going to go ahead and just grab maybe the body. I don't know if the hips are in use, but I'll grab that too. I'll grab the upper shoulder torso area, grab the neck, grab the head. I'm going to grab the hands. This one is currently using IK, which means I also need the pole vector for the elbow. I'm going to need this hand, which is an FK. So I'll grab the hand, the elbow, the upper arm, and then can't forget the shoulders for both of these. He's doing a big throw, which means that the shoulders are going to be a big part of this. Then I'll also grab the actual canister. That's what's moving that. Now with those things I'll select it, I'm back in my sequencer and these are the keyframes on the curves for those specific controls. What I'm going to do now is go scrub around and find here he has to grab, does this power lift, and then wow, he starts to throw it. So maybe I want to mess with this. I'll go right here. I'll set a key. I'll grab this key in particular, and now for this pose. We're going from this kind of squashed and stretch to the throw. He's getting ready to chuck this thing. But here on this frame, I'm going to zoom in maybe on this blue control, I guess, or this red one. What is this red one? This is the arm. This is the left arm, IK. That's a great example. So let me turn on this off. Here you can see we're going to focus on this one key, on this one curve. But if I wanted to do tween adjustments using the blend neighbor, what's going to happen is with nothing selected, it'll apply to everything on this frame for my selection. I start dragging this. It's going to leave the pose in the current position. All these controls will stay where they're at, but they'll start to blend from their current location towards the adjacent key frames on the left or the right. So the frame 169 or frame 175. So if I start to drag this, I start right here, and I start to blend to the left. If I come this way, I start to go back to this original pose and blend to the right. But the main thing I'm trying to point out here is that blend neighbor, when I start to move this thing, it's just blending from the current location. That's very different than the behavior of tween. If I drop this down and go to tween, tween behaves very much the same way except that as soon as I start to move it, the arm is going to snap. It changes drastically because using the tween slider is going to take any individual curve here. You'll see we have this key and this key. And then this one is not exactly right in the middle. It's kind of towards the bottom. So if I take blend neighbor, it'll just start here and adjust from that current location. But if I switch to tween and I start touching it, this becomes a 0% and 100%. Meaning this is 50% the moment I touch it, every single one of these keys snaps to the 50% point between the adjacent key frames. So tween is nice if you want to override your current pose and put this pose right in between the two other keys. Usually though, blend neighbor, that's the reason that this is a default. So if I click all the way on the left, it'll just say, hey, copy the last key frame. And now it's done that. No animation really happens here except for something like the elbow, which I'll deal with that later. But I can blend out of that a little bit here or whatever. So blend neighbor and tween work very much the same, but their behavior is just to either keep the current pose as the base or override the base and just jump to the halfway point. Now blend ease is a nice one because I can use that to sort of create an ease key frame. The further I go towards the right, the more like the right key is going to want to be. So I go just a little bit from that. It becomes an ease in for the right adjacent key. I go all the way over to the left just about it becomes an ease out of the left adjacent key. And if I start to go kind of in this middle area, it just becomes a softer or a more aggressive blend. So blend ease just helps you to find a way to favor one or the other pose. So in this particular case, I could blend out. So he squashes in and he starts to blend out and starts to throw it a little bit sooner. If that makes sense. So blend ease is just a quick way to generate ease key frames. Push pull will amplify and de amplify a pose. And so whatever the curves are doing, you have to focus not on the pose in the viewport, but on sort of the data in the curve editor. So here you can see this red curve, right? It came down to this plateau and I've kind of kept it this plateau and then it goes back vertically. If I push this and I go more amplification, it's going to extend that curve as if it had momentum and kept going in that direction, which means I'm going to get more of this squash pose. In the direction that was already going, I can go more, more, more. And I can really break my pose here. But what this is doing is amplifying whatever the current poses and saying, give me more of that that tension. Whereas pulling it says, hey, go back towards wherever you were before. It'll undo the pose a little bit. And so here you will squash out and then immediately start to throw. It does not hold it at all. Versus if I go back to blood neighbor, I can go ahead and just say, hey, go back to where you were before. But then there's another thing you can do with all of these sliders. You can also switch them to overshoot mode. So if I'm saying, hey, you know, I like this pose, but I don't want to hold it in place before just going back. Out to the throw, I actually wish I could exaggerate this. One trick you can do is maybe I'll come back over here and I'll say, hey, the next pose is going to be that compression. I'll go in the middle and I'll say, I wish I could blend to that compression, but then go beyond it. If I hit this little button here or hit control you control you activate your deactivates overshoot mode. It'll allow me to say, hey, let's go ahead and match that adjacent keyframe and go beyond it. So I can even get more compression. Now it's a lot of order. So I'm going to just copy this value to this key where I'm doing my changes. So now he kind of compresses and then compresses a little bit more and then he goes to throw it. I can do this silver curve. What that did is I basically had, you know, if I wanted to overshoot the following key, this is only going to take me up to the adjacent key. But if I turn on overshoot mode, I can switch this on. I can hit the adjacent key and go even beyond it. Right? Just like that. So you can see I've gone beyond the adjacent key and the trick here that I use is I'll just get rid of this follow up key and move this to take its place. And that will give me really cheap and easy overshoots. Wee! I can turn this back off if I don't want to keep it that way. So now we've covered blend neighbor, we've covered tween, we've covered push pull, we've done blend ease, move relative, time offset and smooth rough are next. Now, smooth rough is probably the easiest one to show you. And that's if, you know, we've got animation happening. I can take these keys, I can switch to smooth rough. And what it'll do is if I drag to the left, it'll just smoothen out whatever the keys are doing. Maybe I'll just focus on the red one and I'll look at this data here. And if I take this section here and I say, hey, smooth, it will basically reduce the contrast between the different points. Or if I go rough, it'll add contrast and try to make bumps bumpier. So hopefully that's, you know, decently clear. This one's really nice for adjusting all of the animation in an area and saying, hey, I want to smooth everything out or I want to make everything a little bit more jittery. Stop this down again and we've got time offset. Now time offset is interesting, it's, it's a bit of a weird one. What it will do is it will keep the frames on which keys have been set. And so the key frame data will stay on these current poses or will stay on the frames. I'm not going to change the timing of the keys, but what it will do is it's going to basically take the values inside the curves and offset that to other nearby keys. So it becomes kind of like a wave. If I grab all of these keys just like this and I move the time offset, it'll take this shape and push it. See how I'm basically moving the entire key like set of data. The key frames stay in the same spot, but the data inside of them, the values, kind of get moved to retime stuff. So it will retime the animation without changing the actual position in time of the key frames. So this will basically let the whole throw happen sooner without changing my key times. If that makes any sense to you. So visually you can see I'm retimeing the animation, but it's not like doing this and shifting the actual keys in the timeline. So that's time offset. It's a little bit weird. And then last up, if I switch over to move relative, this one's really handy to connect bits of animation together. Now move relative is a weird one. It sort of allows you to connect big selections of data to other parts of your graph or your curves. So let's just say I had all this data and I had animated something here, but maybe I copy pasted it from elsewhere and I got copy pasted like over there. And for some reason that made sense. I think it's now going to be very broken. Yep, freaking out. But we say, oh no, no, no, that animation is exactly as I want it to be. I don't want to change anything. I just want to like reconnect it to something else. I can use this selection and I can say connect to the left key frames or connect to the right key frames. So I just say, hey, go ahead and just lock on to that final pose or whatever. Now to come back and look at it, it should just reconnect and there we go. It's good to go. So what it does is it just takes data and just links it back up. Very handy for taking like different animation clips or mocap moments and sort of reconnecting them to when there's offset animation or things like that. So we were just kind of a specialty one. Some of these are some of these are things you use in very specific cases. Others like blend to neighbor or push pole or blend these use them just truly all the time. And so again, you can use them in the curve editor themselves. You can use them in the viewport and whichever place you have your mouse is where the hotkeys will take effect. So if I, for example, hold down the you key and click and drag, it's going to use blend neighbor in the bottom one. But if I have the top one to the tween, you know, so if I'm holding you and left clicking over here or if I'm holding you and left clicking up here, it's going to use whichever one I'm in the window of. So if I only have one, then it won't do anything up here. What it will do it for hold you and left click down here. And so you is your hotkey to activate it, control you is your overshoot mode, shift you, will cycle through them. And that is a quick run through of your different tween tools.

**Frame:** tutorials\frames\mastering-the-ue5-tweener-tool-push-pull-overshoot-animation\frame_000.jpg


---

## Structured Notes

### Core Technique
UE5 Sequencer Tween Tool: 8 slider modes for adjusting keyframe values in the Curves Editor or viewport. Each mode treats the current key value differently as a base or override. Hotkey: **U** (hold + drag in active window); **Ctrl+U** = overshoot mode on/off; **Shift+U** = cycle modes. Works wherever the mouse cursor is (Curves Editor vs viewport).

### Summary
11-minute Unreal Engine tutorial covering all 8 modes of the Tween Tool in UE5 Sequencer. Demo uses a character throw animation (shot 65, Beta rig). Covers: Blend Neighbor (default, preserves current pose as base), Tween (snaps to 50% midpoint between neighbors), Blend Ease (ease in/out towards either adjacent key), Push Pull (amplify or de-amplify current curve direction), Overshoot Mode (exceed adjacent key value for exaggeration), Smooth/Rough (reduce or add contrast between keys), Time Offset (retime animation values without moving keyframe positions), Move Relative (reconnect offset animation data to adjacent keys). Essential for fast pose polish and blending in Sequencer.

### Key Steps
**Tween Modes (all available in Curves Editor bottom panel and viewport):**

1. **Blend Neighbor** (default):
   - Blends from *current* key value towards left or right adjacent keyframes
   - Dragging left → blend toward previous key; right → blend toward next key
   - Current pose stays as starting base — does NOT snap

2. **Tween**:
   - As soon as you touch the slider, every selected key *snaps to 50%* between its two adjacent keyframes
   - Drag further to blend beyond 50% toward either neighbor
   - Use when you want to override current pose and center it between neighbors

3. **Blend Ease**:
   - Generates ease keyframes that favor one adjacent key or the other
   - Far right = ease *into* the right key; far left = ease *out of* the left key
   - Middle range = softer/harder blend; use to create quick ease in/out moments

4. **Push Pull**:
   - Push (drag right) = amplifies the curve in the direction it was already traveling → more of current motion
   - Pull (drag left) = de-amplifies → less of current motion, returns toward previous state
   - Focus on curve data, not viewport pose; can break pose if pushed too far

5. **Overshoot Mode** (Ctrl+U toggle, works with any slider):
   - Normal slider max = adjacent key value; overshoot allows exceeding it
   - Trick: blend to adjacent key then overshoot → delete original adjacent key and replace with overshooted key → cheap exaggerated pose
   - Use with Blend Neighbor or Tween for quick secondary motion emphasis

6. **Smooth / Rough**:
   - Smooth (drag left) = reduces contrast between key values → softer/smoother motion
   - Rough (drag right) = increases contrast → adds jitter/bumpiness
   - Apply to a range of keys; great for cleaning up mocap or adding organic life

7. **Time Offset**:
   - Key *positions* in timeline stay fixed; key *values* shift to neighboring frames
   - Effectively retimes the animation wave without moving actual keyframe positions
   - Use to make an action happen sooner/later without touching keyframe timing

8. **Move Relative**:
   - Reconnects a selected block of animation to adjacent keyframes
   - Use after copy-paste from elsewhere left an offset gap in the data
   - "Connect to left" or "connect to right" — snaps data to continue from the neighbor

**Hotkeys:**
- **U** — activate tween slider in active window (Curves Editor or viewport)
- **Ctrl+U** — toggle overshoot mode
- **Shift+U** — cycle through all 8 modes

### UE Systems / Blueprints / Settings
- **Tween Tool** — Sequencer → Curves Editor bottom panel; 8 modes; also accessible in viewport while animating; hotkey U (hold + drag); mode switcher dropdown
- **Blend Neighbor** — default mode; blends from current value toward left/right adjacent key; preserves current pose as base
- **Tween** — snaps all selected keys to 50% between neighbors on first touch; overrides current pose
- **Blend Ease** — generates ease-in/ease-out keyframes; favors either adjacent neighbor based on slider position
- **Push Pull** — curve-direction amplifier; push = more; pull = less; operates on curve data not viewport pose
- **Overshoot Mode** (Ctrl+U) — extends any slider's range past the adjacent key value; pairs with Blend Neighbor/Tween for exaggeration; works across all modes
- **Smooth/Rough** — contrast adjuster across a key range; smooth = reduce jitter; rough = add jitter
- **Time Offset** — value shifting within fixed keyframe positions; retimes animation without moving keys in timeline
- **Move Relative** — reconnects offset animation data blocks to adjacent keyframes; resolves copy-paste gaps
- **Curves Editor** — UE5 Sequencer sub-panel; shows curve data per bone/control; tween operations apply per-curve
- **IK/FK rigs** — tutorial uses IK arm (requires pole vector) + FK hand; tween tool works identically on both; select all relevant controls before applying

### Difficulty
Intermediate. Requires familiarity with Sequencer, the Curves Editor, and basic animation concepts (keyframes, easing, IK/FK). The tool itself is straightforward — the nuance is knowing which mode to reach for and reading curve data vs viewport pose.

### UE Version
UE5 (Sequencer Curves Editor with Tween Tool as shown — UE5 feature set)

### Tags
animation, sequencer, curves-editor, tween-tool, keyframing, polish, workflow, animator-tools, blend, overshoot

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [1:12] tutorials/frames/mastering-the-ue5-tweener-tool-push-pull-overshoot-animation/frame_000.jpg
- [3:35] tutorials/frames/mastering-the-ue5-tweener-tool-push-pull-overshoot-animation/frame_001.jpg
- [6:35] tutorials/frames/mastering-the-ue5-tweener-tool-push-pull-overshoot-animation/frame_002.jpg
- [9:34] tutorials/frames/mastering-the-ue5-tweener-tool-push-pull-overshoot-animation/frame_003.jpg

## Related Entries
- `make-films-in-unreal-everything-you-need-to-create-your-first-short-beginner-sta.md` — beginner Sequencer/filmmaking pipeline; Curves Editor basics
- `motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter.md` — motion blending techniques (if present)
- `live-link-hub-tips-unreal-engine-animation-hub.md` — animation recording via Live Link Hub
