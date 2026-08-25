---
title: NON-DESTRUCTIVE Animation in UE5! Layered Control Rigs Explained
source: YouTube
url: https://www.youtube.com/watch?v=A8U_8iPc5hA
author: Unreal Engine
ingested: 2026-06-23
ue_version: "UE5.4+"
tags: [animation, control-rig, layered-animation, non-destructive, sequencer, anim-sequence, workflow, animator-tools, ue5-4, blend]
extraction_status: complete
frames_dir: tutorials/frames/non-destructive-animation-in-ue5-layered-control-rigs-explained/
frame_count: 4
---

# NON-DESTRUCTIVE Animation in UE5! Layered Control Rigs Explained

**Source:** [YouTube](https://www.youtube.com/watch?v=A8U_8iPc5hA)
**Author:** Unreal Engine
**Duration:** 9m29s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** In this video, I'm going to show you how to make non-destructive changes on top of pre-existing animation instead of Unreal Engine. And there's several ways to do this, but in this particular case, I'm going to show you how to use layer control rigs to get the job done. And as a quick reminder, I do have an animation YouTube channel if you want to go even deeper into these topics, as well as my own courses where I teach animation in Unreal Engine super, super in-depth. So with that, let's jump in. Here we are in our sample project. I'm currently looking at Shot 52, which has all these robots firing these fun little laser weapons. Now, to get here, I am just in the episodes in Trebeta, and it is right here, Shot 52. I'm in this level sequence. I'm currently just in a blank environment, just so I think it's cool to be able to see exactly what's in this particular shot. And so if I hit play, this is what we've got with our characters. Now, just as quick heads up, these fun little laser blasts are actually not 3D elements. If I leave the camera view and go find my camera, I can look really closely here, and you'll see that the laser blasts are actually 2D hand drawn animations on a little media plane in front of the camera. Super fun. Just in case you're looking for the blast, they won't be there. Now, what we're going to do is we're going to make some changes to the animation of this robot without dealing with all of the original keyframe data. Because, as I've shown in a previous video, we have different options of dealing with this animation data. We have the baked animation, which is a subsequent set inside of here, has this robot basically being piloted by an animation clip, an animation sequence. Pre-packaged animation data that the animator has created, baked down, and we're now using this clip to drive the character. But, if I navigate back out, I can go back to the anim work, which I believe, if I go ahead and mute the baked animation, until I go in here and I unmute the control rigs, I can see that one of these, I don't know which one it is, is it this top one? Yes. This anim work subsequent actually contains the character with the entire live control rig. So, I think it's a robot number one. Robot number one. So, instead of here, I've got all of this animation data, the original keyframes. That's great. But, let's say I don't want to mess with the original keyframe data. Like, I don't want to touch this robot. I think it's perfect. I don't want to mess with it. It looks awesome. But, I want to tweak it. I want to tweak it non-destructively in a way that doesn't make me deal with all this other data that someone else has already done stuff with. So, what are the options we have? Is I'm going to go back to my shot sequence. I'm going to mute the live control rig again. Go back to the baked animation, where everything is just already set up. And I'm going to go into this baked animation sub sequence and find this particular character. Robot number one. Here he is. So, you can see that this character, by mute the character, boop, gone. The character, the weapons, each part has its own animation baked off individually. So, what I want to do is specifically make maybe some posing override. Maybe I want to make some changes where when he fires his gun, maybe I want his head to spin around or something. Just a fun little cartoony spin. Now, to do this, we have a lot of different options. In the previous video, I showed that you could bake this animation sequence down, which will give us all the keyframes, but then that's a lot of data to sort through. Instead, what I want to do is I want to just add a rig on top of this existing animation data. Now, to do that, if I select this character, this particular skeletal mesh asset here in the sequencer, I can add a control rig directly to it right here with control rig. Now, if I just do this by itself, scroll down and find the robot control rig, you'll notice it won't go exactly as you might expect. If I select this, the character disappears. He's actually just over at origin somewhere over there. So, I'll select the character, hit F, and there he is. Now, you'll notice I got the control rig. I got what I wanted, but Unreal is basically listening to me a little bit too much. It says, oh, hey, you had animation data on this character, but you added a rig. You want to override it? What do you want to do? Well, I didn't want to do all the animation myself. I wanted to build off of what was already there. And so, the way it's evaluating right now is it's saying, hey, there is an animation sequence currently here, but let's go ahead and ignore that and just let you do your work. Ah, it's not what I wanted. Let's go ahead and just delete the rig off the character. Boop! And the character is now back over there listening to that animation sequence again, which is a crazy thing, by the way, that we just deleted the rig off of a character. That's what just happened. Anyways, this time, what I want to do is I want to do it in a particular way. I want to add the control rig, but in a layered capacity. So, let's do the same steps. Click on this character, add a control rig, but this time, I'm going to use this little checkbox at the top. This is layered. And now, it'll add the control rig on top of the existing animation sequence data. So now, I can go ahead and scrub, and you can see that all that animation is still there. And what's cool is what's different from just baking from the animation sequence to a regular control rig, is in this case, when I select, say, the head control, there's no keyframes on it. There's no data whatsoever. So if I look closely, we still have the animation sequence, and that's where all this motion is coming from, but the robot control rig is empty. There's no keys anywhere on here. My recommendation is just off the bat, let's go ahead and just set a key on the whole character. Best practice is just to set a key on a full control rig at some point, just so auto key is ready for any changes we make. So now, you know, he'll go ahead and here, he'll pull his weapon up. I'll zoom out a little bit so we can see. Do do do do. Let me select his head control. Set a key with S, bam. And now, I'll go ahead and just spin him around. Wee. There you go. Now, I just spun him 360 degrees or so, but if I go ahead and scrub, it doesn't look like it happened. Now, the reason for this, this is a little bit different than Maya. Unreal is actually trying to prevent gimbal lock and any issues like that. And so even though I just spun the rotation ball around 360, Unreal recognized that the original pose was not that different from the final pose. He was still facing forward in both cases. And so it kind of corrected that 360 over rotation. Is that, are you sure you want to do that? And so what I want to do is actually just grab the rotation in Z. Grab this little, grab the keyframe. And I'll just do the same math operation that I might be used to in Maya. Now, I could drag this. I could just move this up 360 degrees or I could use the same math operations that I'm used to in tools like Maya. Or I can come up to my value and say plus equals 360. And that'll now do a math operation that adds 360 degrees to that value. So now, the head spins. So you're going to look at that. Pew. Right? So that's fun. Now, what I can do is jump back into my camera view, which actually I can't see my camera here. It's in the main sequence, right? Here's a little camera cut track. I can see my main camera button here. But if I'm in this baked animation sequence in particular, I don't have a button for my camera. There are different ways to get to my camera. But in case you're ever in this situation, I can go ahead and just add a camera cut track here. And because this level sequence is tied to the other one in the breadcrumbs, this will access the same camera. So anyways, now I'm going to play. He runs in and, pew. His head spins around. And that's going to fun. But what's cool about this and why I call it non-destructive is this animation is on its own separate layer. Right? I can grab that head control. I can look at the curves. And that's the only thing I have going on, just that one spinning animation. It doesn't affect the state. It doesn't affect the data that was already there. And if I'm not sure I really like it, what's nice is this control rig can be muted. So if I go into the middle here and say, oh, I don't know if I like this change that I'm making, I can just mute the control rig altogether. Just turn it off. Now I can see what it looks like before my change. And that's the original data. Right? He runs in. Does this thing? Fires. But I can go ahead and say, now turn back on my control rig. And you can see that I'm basically turning on and off the control rig in real time, I'm just rigging in on rig in the character, but I'm just hiding it for the moment. So I'll turn it back off. No spin. Turn it back on. Spin. And so that's a really cool way that we can add animation data with clean curves on top of an existing animation sequence. Super, super handy. The feature came out in 5.4 and you can use it just across the board in everything you do in Unreal Engine from now. It's an optional feature. And if you ever want to adjust it after the fact, you go, oh, I added this. I didn't want it to be layered or I did want it to be layered. You can also right click on it. And there is a convert to layered checkbox. Though I do recommend instead of using this checkbox, it tends to work a little bit more seamlessly. If you, when you're first adding the control rig, you pick at that point. Some rigs don't have a problem. Some rigs get a little bit funny. And that's just based on the way that the logic was created for the actual control rig. So my recommendation, hope it helps. And I hope you enjoy using layered control rigs to add non-destructive animation onto these different animation sequences for our project. In the next videos, I'm going to show you some other semi-non-destructive ways to work with the keyframe data directly and animation layers. See you there.

**Frame:** tutorials\frames\non-destructive-animation-in-ue5-layered-control-rigs-explained\frame_000.jpg


---

## Structured Notes

### Core Technique
Layered Control Rigs (UE5.4+): add a Control Rig to a skeletal mesh in Sequencer using the **Layered** checkbox → the rig evaluates ON TOP of the existing animation sequence without overriding it. The rig starts with zero keys — only the changes you add are stored. Mute the rig track to compare before/after non-destructively. The original animation sequence data is never touched.

### Summary
9-minute Epic Animation Hub tutorial (same "Sir Wade" ACOM project, robot laser fight scene Shot 52). Demonstrates the key difference between adding a normal Control Rig (overrides animation) vs. a Layered Control Rig (additive, non-destructive). Shows: muting baked vs. live anim subsequences to understand existing data structure; adding Control Rig without Layered → character loses animation; adding with Layered checkbox → animation preserved + rig adds on top; setting initial S-key best practice; math operations in UE rotation fields (`+=360`); muting rig track to A/B compare; right-click Convert to Layered option. Feature introduced in UE5.4.

### Key Steps
1. **Understand existing animation structure**:
   - Baked animation = animation sequence clip driving character (no editable keyframes)
   - Live anim = subsequence with full Control Rig keyframes (for original animator edits)
   - Select the baked animation version for non-destructive overlay
2. **Add a normal Control Rig (wrong way — for context)**:
   - Select skeletal mesh in Sequencer → **+ Track** → **Control Rig** → pick rig class
   - Result: animation sequence is ignored; character goes to origin with empty rig
   - Delete the rig → character reverts to animation sequence
3. **Add a Layered Control Rig (correct way)**:
   - Select skeletal mesh in Sequencer → **+ Track** → **Control Rig**
   - Before confirming, check the **Layered** checkbox at the top of the rig picker
   - Control Rig is added ON TOP of existing animation; character continues playing original animation
   - All rig controls start with zero keys → only your additions are stored
4. **Initial key best practice**:
   - Select all controls → press **S** to set a key on the full rig at frame 0
   - Ensures Auto Key is primed and won't miss any changes you make
5. **Add animation overrides**:
   - Select control (e.g., head) → scrub to target frame → set a key (S)
   - Adjust as needed; example: spin head 360° in Z rotation
6. **Prevent 360° cancellation bug**:
   - UE auto-corrects identical start/end poses (removes apparent 360° spins)
   - Fix: select the keyframe → in the value field, use `+=360` math operation instead of dragging the rotation handle
   - This adds 360 degrees to the stored value rather than relying on the drag which UE may interpret as no net change
7. **A/B compare**:
   - Right-click the Control Rig track in Sequencer → **Mute** → original animation plays without overlay
   - Un-mute → layered changes reapply
8. **Convert after-the-fact**:
   - Right-click existing Control Rig track → **Convert to Layered** checkbox available
   - Note: adding as Layered from the start is more reliable; some rigs behave unexpectedly on conversion

### UE Systems / Blueprints / Settings
- **Layered Control Rig** — Control Rig added with "Layered" checkbox; evaluates additively on top of existing animation sequence; zero keys by default; introduced UE5.4; works across all UE5.4+ projects
- **Layered checkbox** — appears in the Control Rig picker dialog when adding via Sequencer → Track menu; must check BEFORE adding the rig
- **Normal Control Rig (non-layered)** — completely overrides animation sequence; character loses existing animation; starts from bind pose
- **Mute track** — right-click Control Rig track → Mute; toggles rig on/off for non-destructive A/B comparison; original animation sequence is never affected
- **`+=360` math operation** — type `+=360` in UE rotation field to add 360 degrees to current value; works as `+= N` or `-= N` for any numeric field; prevents UE's anti-gimbal-lock from canceling full-rotation spins
- **S key** — sets keyframe on all selected controls at current frame; use at frame 0 on full rig as best practice for auto-key priming
- **Convert to Layered** — right-click existing CR track; can convert post-hoc but may have rig-specific issues; prefer choosing at creation time
- **Animation Subsequence** — Sequencer hierarchy: main sequence → subsequence (baked anim / live anim); baked subsequence contains animation sequences per body part; add layered CR inside baked subsequence for cleanest separation

### Difficulty
Beginner-Intermediate. The concept is simple (one checkbox), but understanding why it's needed (vs. normal CR) and the `+=360` workaround for full rotations are non-obvious.

### UE Version
UE5.4+ (Layered Control Rigs introduced in UE5.4)

### Tags
animation, control-rig, layered-animation, non-destructive, sequencer, anim-sequence, workflow, animator-tools, ue5-4, blend

---

## Captured Frames

<!-- BUG 6 REPAIR 2026-08-25. These frames were captured at
     duration * (0.1, 0.3, 0.55, 0.8), but the .md parked them under a
     fallback '### Full Content [0:00]' heading, so reground_frames.py
     re-captured them at 0:00 and produced title cards. Moments below are
     re-derived from the source's duration, not chosen. Bullet refs take
     precedence over the heading layout, so the stale [0:00] line above is
     ignored. Still BLIND-ERA moments: legible, not content-anchored. -->

- [0:57] tutorials/frames/non-destructive-animation-in-ue5-layered-control-rigs-explained/frame_000.jpg
- [2:51] tutorials/frames/non-destructive-animation-in-ue5-layered-control-rigs-explained/frame_001.jpg
- [5:13] tutorials/frames/non-destructive-animation-in-ue5-layered-control-rigs-explained/frame_002.jpg
- [7:35] tutorials/frames/non-destructive-animation-in-ue5-layered-control-rigs-explained/frame_003.jpg

## Related Entries
- `motion-blending-bone-matching-for-unreal-engine---make-films-in-unreal-ep2-inter.md` — bone matching + Layered FK Control Rig additive; related non-destructive workflow
- `mastering-the-ue5-tweener-tool-push-pull-overshoot-animation.md` — animation polish tools; pairs with layered CR for non-destructive tweening
- `ue5-animation-layers-non-destructive-camera-shake-character-tweaks.md` — animation layers for camera shake and character tweaks (related non-destructive topic)
- `new-ue5-motion-trails-20-heat-map-camera-space-stabilization.md` — Motion Trails for reviewing layered animation arc quality
