---
title: DYNAMIC Space Switching in UE5: Pro IK Hand Constraint Techniques
source: YouTube
url: https://www.youtube.com/watch?v=9AavXj11Iw4
author: Unreal Engine
ingested: 2026-06-23
ue_version: "UE5"
tags: [animation, sequencer, ik, space-switching, constraints, control-rig, hand-constraints, posing, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/dynamic-space-switching-in-ue5-pro-ik-hand-constraint-techniques/
frame_count: 4
---

# DYNAMIC Space Switching in UE5: Pro IK Hand Constraint Techniques

**Source:** [YouTube](https://www.youtube.com/watch?v=9AavXj11Iw4)
**Author:** Unreal Engine
**Duration:** 6m32s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Well, go back. In this video, we're going to take a look at some of the posing tools available to us, specifically space switching. Now, space switching is something that often rigs have built in, but I'm real has some really cool features to be able to dynamically adjust where different controls are looking for their parent relationships. If you want to have IK hands, switch into different parts of the body to move alongside things or be locked to certain parts of the body. It's very cool. So, we're going to take a look at that full system and I'll show you how it works. So here we are in shot 65. We've got the live rig with beta grabbing this big canister and chucking it once again. So, I'm going to come zoom in on this hand. Now, this hand is currently an IK, right? It's just sitting there. It's not moving the canister. We don't have any constraints active right now. We'll do that in some follow-up videos. But what I want to do is I want to move this IK hand around, or at least I want to maybe move the body with that IK hand in mind. And so, one of the things that is so good about IK hands, as we probably all know, is that it's locked in space, right? That hand is locked and I can move the body around. But the thing is, sometimes you do want to have the hand not just free-floating, totally locked off in world space. Sometimes you want to adjust where that hand is sort of parented to. And so, if I come over to my left side, I have constraints and I have spaces. Now, spaces and constraints use a lot of the same kinds of math. They're very similar. So, you can do a lot of stuff interchangeably between the two. But if I take this left arm IK control, the thing that's currently used to move the hand around. Right now, the hand itself is in what's called parent base. And I think it's already parented to the world or the global controls. And so, when I move something like the body, you know, it's not affected. That hand is not in the body hierarchy in general. But let's say that for whatever reason, I wanted to be able to move the torso, maybe like this this upper chest control, if I could grab it. I want to move this upper chest control. It's called end, spy an end. Maybe I want the hand inside of that space. So, when I move the upper torso, it actually does move the hand along with it because that may be helpful for how I'm animating. So, what I can do is I can grab this hand control. And I can actually add my own custom space inside of the rig anywhere. So, what I'll do is I'll just add my own space by coming up to the spaces area with this control selected. I'll say add new. I'll type in spine, if I could type correctly. And here I can see that end control. I can also see individual bones. So, what I'll do is I'll just hit end right here. And that just adds it to the list. It doesn't switch me into it yet. I can even say, you know what? Maybe I want to be able to go into body space. So, I'll add the body control as an option as well. And so, now what I'll do is I'll just say as of frame whatever, 170 something. I'll just say, you know what? Switch me into that spine end control. Boop! And that'll now do two things. The first is it changes the space that I'm in, but it also auto converts any animation following that. I'll show you what that looks like here. If I go into the left arm IK, I can twirl this down and you can see the space has actually been key framed. I was in parent space up until frame 169. And now everything after that is now in spine space, which is very, very cool. So, what that means is I'm still in IK, right? I'm still moving around with an IK hand. And if I take this left shoulder, this will have no bearing on it. I can move the shoulder around and that hand is still locked in place. It doesn't, doesn't care. However, now that the hand is in, what is it? Spying end space. I can grab that spine end control and that will move the hand as well. So, it moves the whole upper part of the body. But maybe that's not what I want. Maybe, you know what? I don't want that to be so influential. I want to switch it to the body control itself. That switches my space constraint is basically what it is. And so now, you know, that hand is still a locked off control. I can still move the shoulder and not affect it. Now that I've changed the space to the body, I can also grab this shoulder control and that does not move the hand, right? You can see that the hand is still locked in place. But now it's in body space, which means that when I move the body, it will actually move with the body. And so, that's what's so cool about the space switching is that I can dynamically on the fly not only change the spaces to anything on the rig I want, but I can add new ones super easily. And you can do this with any control. And you can see that the head is in parent space. And if I come down here, you also have a world-aligned things like that. So the attributes that are also able to handle it. So you can do it with the rig controls, the way you'd probably be used to it, where rigs have attributes that you can switch what space you're in. You can also do it here in the space switch menu. If you don't want to have the rig logic handle it, and you can even just use constraints to do this kind of thing. So it's a really, really powerful system. And what's also cool about it is that you can also bake into and out of any space at any time. And so if we said, you know what, I have all this animation, where he comes in and he grabs it. And up until this point, he's in parent space, which means the body is not going to affect the hand position, right? Not at all. Hand still locked. But if I scrub forward, where is it? Here after this switch is made, now when I move the body, the hand is being affected. So whatever the animation is, if I'm like, you know what, I really like that. I want to, I want to sort of lock that down, but I want to switch it to a different space and not worry about it. I can just say bake. And actually, I should probably grab the actual control that I'm trying to work with, which is the hand here. So I can say bake. And you can see that it'll say, hey, which space do you want to bake into? What, for what frames do you want to bake? Just the keys, all the frames, blah, blah, blah, blah. And you could even add a new one here at this point. Say, you know what? I want to bake into something new. I want to bake into head space or something. I'm not going to do that right now. But very powerful tool, very, very cool. And by the way, quick note on this, different controls will have different spaces. You can select the leg. For example, you can see we don't have the same spaces if we had on the arms. So you can do different things for different body parts and it will remember what you had there. So hopefully that's helpful. Again, if you want to go even deeper into these topics, I have an animation YouTube channel where I cover this kind of stuff on my channel and tutorials, as well as my own independent courses where I cover Unreal Animation super in depth. If you want to know what every single one of these buttons does, there's a lot of information to crime under these videos. And hopefully this is helpful. Thanks for watching. I'll see you in the next videos.

**Frame:** tutorials\frames\dynamic-space-switching-in-ue5-pro-ik-hand-constraint-techniques\frame_000.jpg


---

## Structured Notes

### Core Technique
UE5 Sequencer Spaces panel: dynamically add and switch parent spaces for IK controls (e.g., hand IK) at any frame — change from world/parent space to a body bone/control space — with automatic key conversion and bake-to-space workflow.

### Summary
Short official UE tutorial (6m) demonstrating the Spaces panel in UE5's animation/posing workflow. IK hands are locked in world space by default (good for body-independent positioning), but Space Switching lets you dynamically reparent them to any control or bone on the rig at any frame. Demonstrated: left arm IK hand → add "spine_end" and "body" as custom spaces → keyframe the switch at frame 169 (auto-converts subsequent keys) → bake into any space for downstream cleanup. Different controls maintain separate space lists (arm ≠ leg). Also accessible via Constraints tab.

### Key Steps
1. **Understand default:** IK hand control = world space by default; body/torso moves without affecting the hand
2. **Open Spaces panel:** in Sequencer animation editor, left side panel → "Spaces" section (near Constraints)
3. **Select control:** click IK hand control (e.g., left arm IK) in viewport or rig hierarchy
4. **Add custom space:** Spaces panel → "Add New" → type bone/control name (e.g., "spine_end") → select from list → adds as option (doesn't switch yet); repeat for additional spaces (e.g., "body")
5. **Switch space at frame:** scrub to target frame → in Spaces panel → click desired space name → space switches, and all subsequent animation keys are auto-converted to preserve position
6. **View space channel:** Sequencer → expand IK hand control → space attribute is now keyframed (shows switch point)
7. **Result:** hand still IK-locked; shoulder doesn't move it; but moving the spine_end/body control now moves the hand along
8. **Bake into space:** select control → Spaces panel → Bake → choose: target space, frame range (all frames / keys only), source/destination options → bakes animation in that space for clean handoff
9. **Per-control spaces:** different controls have independent space lists (arm spaces ≠ leg spaces); each remembers its custom additions
10. **Alternative access:** Constraints tab uses same math as Spaces; rig attribute controls on the rig itself can also do space switching

### UE Systems / Blueprints / Settings
- **Sequencer Spaces Panel**: UE5 animation posing tool; per-control custom space list; keyframeable space switches; auto-converts downstream animation on switch
- **IK Controls**: by default in parent/world space; Spaces panel overrides parent relationship dynamically per frame
- **Space Switch Keyframe**: animates the "space" attribute on the control; transition is instantaneous (one frame)
- **Bake to Space**: resolves animation into a target space; accepts: target space, frame range, all frames vs. keys only; can bake to a new custom space at bake time
- **Constraints Tab**: parallel system with same math as Spaces; interchangeable for many use cases
- **Rig Attributes**: some rigs also expose space switching as attributes directly on rig controls (classic approach)

### Difficulty
Intermediate — animation posing workflow, brief but dense; assumes familiarity with Sequencer and IK concepts

### UE Version
UE5

### Tags
[animation, sequencer, ik, space-switching, constraints, control-rig, hand-constraints, posing, intermediate]

---

## Related Entries
- control-rig-in-unreal-engine.md (Control Rig system documentation, IK and FBIK)
- dynamic-space-switching-in-ue5-pro-ik-hand-constraint-techniques.md (same video, self-reference removed)
- beat-yourself-up-with-unreal-ragdoll-physics-for-filmmaking-made-easy-or-hard-in.md (animation baking and Sequencer techniques)
