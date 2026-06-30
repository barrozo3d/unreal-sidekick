---
title: UE5 Constraints Are EASY! Parent Constraint Workflow for Animators
source: YouTube
url: https://www.youtube.com/watch?v=LHK3J5m_43c
author: Unreal Engine
ingested: 2026-06-23
ue_version: "UE5"
tags: [animation, constraints, parent-constraint, sequencer, control-rig, ik, workflow, technique, characters, cinematics]
extraction_status: complete
frames_dir: tutorials/frames/ue5-constraints-are-easy-parent-constraint-workflow-for-animators/
frame_count: 4
---

# UE5 Constraints Are EASY! Parent Constraint Workflow for Animators

**Source:** [YouTube](https://www.youtube.com/watch?v=LHK3J5m_43c)
**Author:** Unreal Engine
**Duration:** 9m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Alright, in this video we're talking constraints, something that is near and dear to me, and I know it's every animator's favorite topic. In all seriousness, I know people usually hate this, but and I'm real, it's actually really easy and super simple to use as opposed to Maya where it requires a PhD in 3D animation to understand how to do constraints properly. It's very simple here, I think you're going to like it a lot. So what we'll do is we'll use this shot, this is shot 50, where beta breaks through this wall and rips it open. Now what we're going to do is we're actually going to set up a constraint system so that we can adjust the timing of the door's opening. And my preference here is going to be, actually, we'll go ahead and get the lighting out of here. Give it some of that stuff out of the way, no clutter. My preference is going to be to take the hands and attach them to the door instead of the other way around. The reason for that is if we attach the doors to the hands, well, when the hands start to rotate like this, the doors will start to pull out of the sockets. But if we attach the hands to the doors, then we can just kind of move it up and down, where is the button? There we go, up and down, and the hands will come along for the right. A little bit simpler. So let's go ahead and do that. Very, very easy. All we need to do is say, hey, hand you right there, IK arm. Go ahead and just twirl down our constraint menu and we'll say add a constraint, add a parent constraint. Actually, you know what, hit escape. I should probably pick a frame. Let's pick a frame and say, you know what, where do we want to begin? Let's go to frame 130, 131. We're going to 131. As of 131, take this hand and I'll go to constraints and add a parent constraint. And we can pick the control itself or we can click the skeletal mesh and grab a joint inside. Usually that's what we do. It's a deeper constraint. So let's go ahead and just select the door corridor skeletal mesh. When I select that, it'll say which bone do we want to attach to. We want the top panel here. And so just like that, we're done. That's the constraint. Now how do we know? How do we know? What do we just do? If I come down to my sequencer and I look inside this left arm, IK, I can twirl that open and I can see that there is a parent relationship that's been created as of 131. Now, unlike Maya, which when you create a constraint instead of Maya, it makes the constraint as if it's always been there. So then it's just always attached. But unlike Maya here and I'm real, all the animation preceding my constraint is the same. Then once I hit this moment, the rest is now dynamically attached. Now you'll see that the hand is slipping out of the way now. And that is because the animation is, it still has animation. Again, in Maya, when you do a constraint, you have to set up this sort of scapegoat situation where the object that you're constraining has to have some kind of a group or a locator so that it's self contained within a safe bubble that you can train that bubble to the other object. And you have to sort of nest things together to be able to still animate and constrain the same objects and have that control. That's not necessary here and I'm real. And so I already have a bunch of animation on this hand control that you're seeing happening on top of the constraint. And so to not double transform it, I can actually just get rid of the majority of this key frame animation. So I was just taking my location, my rotation, my scale, all this stuff, and I'll just like delete most of it after this point. Yeah, why not? Just give it all that. So now you'll grab the door. There's no more animation on the hand, but the hand comes with the door, right? There's still finger animation. So there's some still some nice stuff going on here. But now the hand isn't doing weird other stuff. But that's what's nice about this system is now, if I say, all right, let me grab that that upper, what do you call that, that like panel top thing up here? That corridor door with its keyframes, I can go into the curve editor of it and we can take the translation, which access is this going to be why looks like the Y control. Here we have the motion that pulls this up just like that. I can adjust all of this. I can just say, you don't want to just clear out some keyframes and, you know, maybe I want to use my tween tools. And I want to adjust this like that. Boom. With one slider, I'm moving both the hand and the door. So I can go ahead and just leave this lower for a while so that it doesn't really open and then it slams open. Bam! Or maybe I want to say, you know, really slow it down. Do you need pushes it? Or maybe it's like a really slow thing. It's very linear and even, little boring, but you know, maybe it's really, really light. And he just, whoop, you know, probably not. I like the way we had it before. I like keeping it nice and low and we will slam it open. To do both, right. And so we now have this really easy method of taking this one control, doing our thing, but what if we want to take the hand off the door at a certain point? We can just select that hand, and we can turn the constraint off by just coming up to our constraints area and clicking this active keyframe button. And here you can see down in the sequencer, you can see both in the sequencer itself with the left hand control. You can see inside of it the parent where we have all the preceding animation, the attached section that we were driving with the door. And then as soon as I turned off the constraint, the animation itself or the hand itself is now free of this door. I can take the door and send it away. And it's no longer constrained. But the hand is able to have its own animation as well. And so the keyframe data that I had on the hand has now been baked back down to the hand control so that everything that you do is preserved when you switch on or off a constraint. It preserves what you were doing. It doesn't snap back to some weird rest position. It doesn't change everything you did previously. As if the constraint has always been there, it's a much smarter system than inside of Maya, which is really really nice. And it's so easy to work with. I'm not sure what happened to his face there. Please ignore that. It's a really flexible system. And you can see here that we've got this entire hand animation where everything inside of here driven by a constraint and we're going to go. We can do the other hand as well, just really fast. I'll take the IK hand. I'll find the pose where he grabs it. So maybe I'll just go right here. Looks like frame 130. Sure. We'll take frame 130. We've got this hand control. Add a constraint. I can, again, I can pick the control object, but it's better to usually grab the actual skeleton mesh and specify a bone. And we'll say panel bottom for that. In this particular case, now we've got the right arm IK that's now doing its own thing. It grabs on. It's got additional animation. So it's probably going to get a little bit weird looking towards the end. So I'll go ahead and just say all of my animation data after the constraint is unnecessary. And now I'll say throughout this whole section, if I want to take the up and down, which is this guy translate. Here we go. I can start to clear out some of these keyframes. Maybe mess with the interpolation. And I can just kind of adjust, right? And maybe I just want to push this whole thing to happen a little bit later. Just like that, using my curve editor and bam. Now his fingers flex, go like this. Now his fingers flex and he pushes it with the heel of his hand and bam. And if I want to turn that constraint off, all I need to do, once again, is select the hand control itself and just click this button. Boop. And now you can see in real time, it turned off the constraint and re-converted the animation that the hand had back into the space of the hand versus the space of the door. So constraints are really that easy inside of Unreal, super powerful, super easy, actually a lot of fun to work with. And you can do some really crazy stuff stacking on top of each other. That's so much more to talk about with constraints. You can bake them. All kinds of cool stuff. But if you want to know more about that, you can check out my YouTube channel where I have a bunch of tutorials. I also have classes on my website. If you want to go super deep into the workflows and what you can do with animation that I'm real. But here in this series, we're going to wrap it up here with constraints and move on in the next video to the formers. Very fun.

**Frame:** tutorials\frames\ue5-constraints-are-easy-parent-constraint-workflow-for-animators\frame_000.jpg


---

## Structured Notes

### Core Technique
Parent Constraints in UE5 Sequencer — attach one control rig control to a skeletal mesh bone so it follows that bone's animation automatically. Demonstrated with a character (Beta) ripping open a door: hands constrained to door panels (not door to hands — prevents socket tearing). Key advantages over Maya: constraint activates only from the frame it's created (preceding animation untouched); no locator/group setup required; deactivating a constraint automatically bakes the hand's motion back into the control's own space.

### Summary
9m9s official UE5 constraints tutorial (instructor: Sir Wade) using Shot 50 from the ACOM project. Beta rips open a wall; goal: adjust door-opening timing while keeping hands attached. Workflow: select IK hand control → Constraints panel → Add Parent Constraint → pick door Skeletal Mesh → pick bone (top/bottom panel). After constraining: delete existing animation keys on the hand after the constraint frame (prevents double-transform). Now editing the door's Y-translation curve moves both hand and door together. To release: select hand → Constraints panel → click **Active Keyframe** button to toggle off. UE automatically bakes the constraint-driven motion back to the control's own keyframes — no snapping or reset. Demonstrated for both left hand (top panel) and right hand (bottom panel). Comparison with Maya: Maya requires locator group setup; UE constraints are frame-by-frame local — much simpler.

### Key Steps
**Choosing constraint direction:**
1. Attach **hands to door** (not door to hands); moving the door will pull the hands with it; if you attached door to hands, rotating the hand would pull door out of position

**Adding a parent constraint:**
2. Move playhead to the frame where the hand should first grab the object (e.g., frame 130/131)
3. Select the IK hand control in the viewport
4. In the **Constraints** panel (or animation toolbar) → **Add Constraint → Add Parent Constraint**
5. When prompted: click the **Skeletal Mesh** of the target object (not just the actor/control) → specify the **bone** to attach to (e.g., "panel_top" or "panel_bottom")
6. Constraint is now active from that frame onward; all preceding animation on the hand is preserved unchanged

**Clean up double-transform:**
7. After constraining, the hand still has its old location/rotation/scale keyframes fighting with the constraint
8. Select the hand control → in Sequencer, select all keyframes after the constraint frame → delete them
9. Hand now follows purely the door bone's motion; finger animation (still on separate controls) is preserved

**Editing timing via the constrained object:**
10. Select the door Skeletal Mesh → open Curve Editor → find the translation axis (Y or Z) → adjust keyframes: hold lower, then slam open; or slow linear pull; or any timing desired
11. Both the door and hand move together — no need to touch the hand keyframes at all

**Turning off the constraint:**
12. Select the hand IK control → in the Constraints panel → click the **Active Keyframe** button (toggle off at desired frame)
13. UE automatically re-bakes the constraint-driven motion back into the hand control's own space
14. Hand is now free of the door; previous animation before the constraint is still intact

**Second hand:**
15. Repeat for the right IK hand: go to the grab frame → Add Parent Constraint → pick the door SM → select bottom panel bone
16. Clean up post-constraint keyframes; adjust door curve for pacing

### UE Systems / Blueprints / Settings
- **Constraints panel** (animation mode) — found in the animation toolbar; lists active constraints; provides "Add Constraint" submenu; Active Keyframe toggle to turn on/off per frame
- **Parent Constraint** — locks a control to a bone's transform (position + rotation); full 6DOF follow; other constraint types include point, rotation-only, etc. (not covered)
- **Constraint activation frame** — UE5 constraint only applies from the frame it was created onward; preceding animation is NOT affected (Maya applies constraint as if it's always existed — opposite behavior)
- **Double-transform issue** — after constraining, existing keyframes on the control conflict with constraint; delete post-constraint keyframes on the constrained control to fix
- **Active Keyframe button** — per-frame toggle that turns the constraint on or off; creates a keyframe on the constraint track in Sequencer; when turned off, UE bakes the constraint-driven motion back into the control's own keyframes automatically
- **Constraint track in Sequencer** — visible as a sub-track inside the Control Rig section; shows "parent" entry with sections for constrained and free ranges
- **Bone-level targeting** — when adding a constraint, selecting the Skeletal Mesh and specifying a bone gives a deeper/more stable constraint than targeting the control actor directly
- **Bake constraint** (mentioned but not demonstrated) — Constraints tab → Bake; converts constraint relationship to pure keyframes; needed before rendering (guarantees viewport = render)

**Key workflow principle:**
- Constrain the follower to the driver (hands → door), not driver to follower
- This keeps the editing target (door timing) as the single source of truth

### Difficulty
Beginner. Much simpler than Maya constraints; no rigging knowledge needed. UE handles all the offset math automatically.

### UE Version
UE5 (ACOM project, official Unreal Engine tutorial series)

### Tags
animation, constraints, parent-constraint, sequencer, control-rig, ik, workflow, technique, characters, cinematics

---

## Related Entries
- `ue5-animation-layers-non-destructive-camera-shake-character-tweaks.md` — companion tutorial by same instructor; animation layers for non-destructive tweaks
- `stylized-animation-control-rig-characters-in-unreal-engine-5.md` — ACOM rig intro; same project/instructor
- `this-free-plugin-changes-filmmaking-forever-unreal-5.md` — OneClick Control Rig; uses parent constraint to lock hand to gun; bake constraints before rendering
- `ue5-curve-editor-20-new-lattice-tool-curve-scaling-hacks-ue-56.md` — Curve Editor for adjusting constraint-driven timing curves
