---
title: UE5: Everything About SPRING Motion (Float Lerping)
source: YouTube
url: https://www.youtube.com/watch?v=EvWrGFZshBk
author: Royal Skies
ingested: 2026-08-02
ue_version: "Not specified (UE5.x)"
tags: [blueprint, animation, pipeline, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/ue5-everything-about-spring-motion-float-lerping/
frame_count: 12
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# UE5: Everything About SPRING Motion (Float Lerping)

**Source:** [YouTube](https://www.youtube.com/watch?v=EvWrGFZshBk)
**Author:** Royal Skies
**Duration:** 8m16s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So, you want to make something have smooth, but spring-like movements in Unreal 5?
[0:04] Not a problem.
[0:05] So I needed to learn how to do this to create some smooth military combat drone movements,
[0:09] where I needed the drone to look like it was naturally drifting with the momentum each time it changed directions,
[0:14] and let's just say that I learned a lot more than I wanted to about spring movements.
[0:19] So I'm going to help you avoid wasting your time like I did.
[0:21] There are multiple ways to accomplish this, but the first one I found was called a Vector Spring Interp node.
[0:27] This is Unreal 5's default position spring system.
[0:30] In order to set it up, though, you have to right-click the spring state and promote it to a variable.
[0:34] Get the current location of whatever you're trying to move and drag it to current.
[0:38] And then grab a Get World Delta seconds, drag it into time, then connect it all to set actor location,
[0:43] and now whatever coordinates you have here in the final position, it's going to spring move its way over there,
[0:48] depending on these three values called stiffness, critical dampening, and velocity.
[0:52] Normally, they are all defaulted to one, and the movement looks kind of like this.
[0:56] Now, I know it doesn't look very springy. That's exactly what I thought.
[1:00] I thought I broke the node or something, but what they don't tell you is you're supposed to adjust these numbers.
[1:04] Now, explaining what these numbers do is kind of hard, but I'll do my best.
[1:08] Stiffness is how resistant the actor is to bouncing.
[1:11] The more stiff something is, the less springy, bouncy motions you will see.
[1:15] Critical dampening is like how close the actor sticks to the target once reaching its position.
[1:20] So if you set it to something like 0.1, you will see that when it reaches its target,
[1:24] which is the red dot, that it will overshoot a lot.
[1:27] And if we set it to something like 0.5, it will overshoot less.
[1:31] If we set it to something like 5, it will have almost no overshoot at all.
[1:34] And if we set it to something like 0.5 and set stiffness to something high like 15,
[1:38] you will see that's when we start to get this bouncy springy movement.
[1:41] Velocity is how long it takes for the actor to make it to the new position.
[1:45] If it's less than 1, like 0.1, it will barely make it to its goal.
[1:49] If we set it to 0.5, then you can see it makes it a little bit further, but not quite there.
[1:54] But if we go all the way above 1 to like 5, now you will see it overshoots,
[1:58] and with the spare time, it makes its way back.
[2:01] If we set stiff to 2 and critical to 0.2 and velocity to something like 0.15,
[2:05] we get a really smooth, clean, slow kind of curve when we change directions.
[2:10] These are actually the values that I ended up using for the drone
[2:12] when I tried to mimic motions gliding through the air.
[2:14] So that was my first attempt to make spring motion in Unreal 5,
[2:19] but I didn't really like this setup because I feel like it just overcomplicated things.
[2:23] And one of our awesome patron members, Chloe Valencia,
[2:27] who is an absolutely cracked programmer, sent me this code.
[2:31] Now, she sent this to me way back when we were still in our Unity arc and see Sharp.
[2:36] But I really wanted to try and make it work in Unreal 5, and eventually I did.
[2:40] The blueprint for it looks kind of like this.
[2:43] You take the target position, you subtract it from your location,
[2:46] then you multiply it by a force value, divide it by 100,
[2:49] and then you vector 3 Lerpet by an empty speed vector,
[2:52] and for your alpha, you divide a stiffness value by 100,
[2:55] and then you add that result to your current location.
[2:57] And I know it looks more complicated, but trust me,
[3:01] once you've got it all set up, it's actually way simpler.
[3:04] See, in the default spring node, we needed to balance like five or six different values,
[3:07] and it required you to plug in time and delta seconds.
[3:10] But in this custom version, we only have two values that we need to worry about,
[3:14] stiffness and force.
[3:16] Stiffness translates to bounciness, and force translates to how fast it moves.
[3:21] You can see the results of it here, and personally, I like it a lot more.
[3:25] But you can use whichever method you think works best for you.
[3:27] Now, while I was learning all this stuff, I realized that sometimes,
[3:30] instead of trying to get smooth transitions between two vector 3s,
[3:33] it's nice to be able to get smooth transition between a single flow.
[3:36] For example, the drone has a rotation value.
[3:39] This value controls how locked in the drone is towards the target.
[3:43] Normally, this value is set to zero when it doesn't see any targets,
[3:46] but as soon as it finds one, and it needs to look directly at the target for it to do that,
[3:50] the rotation value needs to be set to something high like 50.
[3:53] However, the problem is, if we change the value to look at the target as soon as it sees one,
[3:57] the drone will instantly face the target abruptly, and it will look kind of choppy.
[4:01] So I needed the way to smoothly transition the rotation value from zero to 50.
[4:06] And for that, I found a few different methods.
[4:09] The first attempt was to just take the vector 3 spring formula,
[4:12] and adjust it for a single flow value.
[4:14] That setup looks like this, and you can see how the value looks on the pink spheres here.
[4:18] Just imagine that on the left side, the value is equal to zero,
[4:21] and on the right, it would equal 50 or like 100 or something.
[4:24] And the stiffness and force controls work exactly the same as they do
[4:27] when we were using them for vector 3s.
[4:29] And that was pretty cool.
[4:30] But then I found that when you're dealing with a float value like this,
[4:34] Unreal actually has some default float alert nodes that we can use, and they look like this.
[4:39] If you just set the start value, set the target value,
[4:42] the speed at which you want it to change, and set the new results like this,
[4:45] we can see the value changing.
[4:47] But the problem is, it's not really smooth.
[4:49] It's kind of abrupt at the beginning.
[4:51] So I did some more digging, and I eventually found that Unreal has this thing called an ease node.
[4:55] And it's pretty cool.
[4:56] What it does is make a float go from one value to another smoothly.
[5:01] You plug in the current value to A, the target value to B, and alpha goes from zero to one.
[5:06] When alpha is zero, the value is A, and when alpha is one, the value is B.
[5:09] So you just plug whatever formula you want that manages alpha,
[5:12] and then you decide what kind of smooth you want based on this function.
[5:17] Now, there's quite a few of them here, but I went ahead and mapped every single one of them out,
[5:21] and you can see what they all look like here.
[5:25] Now, that was cool, but I wanted to do some more digging,
[5:27] and I found there's actually another float ease alert node, which looks like this.
[5:31] It is simpler, and it only has one type of basic Bezier curve option,
[5:35] and it works exactly the same way.
[5:36] The value you want to control goes into A, the target value goes into B,
[5:40] the alpha goes from zero to one, zero being A and one being B,
[5:43] and the exponent should usually be left at two,
[5:46] but it gives you a curve like this.
[5:47] It's just a simple default Bezier curve, simple and clean,
[5:50] and this is actually the node that I prefer to use most of the time,
[5:53] because I just like how simple it is.
[5:55] But there is one final method which I found that allows you to smoothly go from one value to another,
[6:00] which is a timeline.
[6:02] This method is probably the easiest.
[6:04] You just add a timeline, add a float track, you right click, add points.
[6:08] Let's just say at zero seconds, we want a value of zero,
[6:11] and at four seconds, we want a value of 100.
[6:13] You can use these two buttons to zoom out and see the entire graph,
[6:16] and if you select these points and right click one of them,
[6:18] you'll be able to smoothen the curve out like this.
[6:20] This method actually gives you the most control over the transition between the two values,
[6:24] because you can literally shape the curve to however you want.
[6:27] You just take the output and set it to the value you want to control,
[6:30] and you can play it normally or you can play it in reverse.
[6:33] Now, I really like this method, but it has one problem.
[6:35] If you interrupt the timeline before it's over,
[6:38] the values will jump and start at the beginning or the end,
[6:41] which can look a little bit abrupt, so be careful when you use it.
[6:44] And those are all the ways that I have found to do smooth spring motion,
[6:48] or just smooth lurping and interpolation from one value to another.
[6:51] Now, I think the most annoying thing during this entire process
[6:55] was honestly just remembering what everything does.
[6:58] So like when I was using the spring and turp node,
[7:00] I always forget what does stiffness do?
[7:02] What does velocity do?
[7:03] What does dampening do?
[7:05] So I created this standalone project file that has all the settings I normally use on display.
[7:10] So when I'm at work and I need to remember what settings to use to get certain types of movement,
[7:14] I can just open this project, look around and be like,
[7:16] oh yeah, that's the movement I want.
[7:18] And in one glance, I immediately know, okay, I need stiffness at 90,
[7:21] dampening at 0.3 in velocity at 1.
[7:24] And I went ahead and collected all the different tests that I usually do for debugging movement,
[7:28] and I just put them all together in this project,
[7:30] which I simply call the LURP library.
[7:32] It has all the formulas and all the blueprints
[7:35] for how I smoothly transition between values
[7:37] and how to spring LURP vector 3s or floats.
[7:40] If you're a patron or a YouTube member,
[7:42] obviously you can grab this project file for free.
[7:44] Otherwise, you'll be able to find it on my art station or fab for 15 bucks.
[7:48] But it doesn't have any secret information on it
[7:51] that I didn't show you in this video.
[7:52] The paid file is really only for people who just don't want to go through the trouble of making their own LURP library.
[7:57] But the information that you need to create your own
[7:59] will always be here on this video for free courtesy of the monthly members and patrons.
[8:04] Regardless, that's all I got for you today.
[8:06] Hope that helps, and as always, I'll be on a fantastic day, and I'll see you right now.



---

## Captured Frames

- [0:30] tutorials/frames/ue5-everything-about-spring-motion-float-lerping/frame_000.jpg
- [0:52] tutorials/frames/ue5-everything-about-spring-motion-float-lerping/frame_001.jpg
- [1:24] tutorials/frames/ue5-everything-about-spring-motion-float-lerping/frame_002.jpg
- [1:38] tutorials/frames/ue5-everything-about-spring-motion-float-lerping/frame_003.jpg
- [2:05] tutorials/frames/ue5-everything-about-spring-motion-float-lerping/frame_004.jpg
- [2:40] tutorials/frames/ue5-everything-about-spring-motion-float-lerping/frame_005.jpg
- [3:21] tutorials/frames/ue5-everything-about-spring-motion-float-lerping/frame_006.jpg
- [4:14] tutorials/frames/ue5-everything-about-spring-motion-float-lerping/frame_007.jpg
- [4:39] tutorials/frames/ue5-everything-about-spring-motion-float-lerping/frame_008.jpg
- [4:56] tutorials/frames/ue5-everything-about-spring-motion-float-lerping/frame_009.jpg
- [5:25] tutorials/frames/ue5-everything-about-spring-motion-float-lerping/frame_010.jpg
- [6:04] tutorials/frames/ue5-everything-about-spring-motion-float-lerping/frame_011.jpg

---

## Structured Notes

### Core Technique
A survey of every Blueprint method the author found for smooth "spring-like" motion in UE5 — for Vector3 positions (drone drift/momentum) and for single float values (rotation/blend weights) — comparing the built-in `Vector Spring Interp` node, a custom Lerp-based "Sperp" (Spring Lerp) formula, `FInterp To`, the `Ease` node, `Float Ease` (Bezier), and Timelines.

### Summary
Built to solve a specific problem — making a military combat drone drift naturally with momentum when it changes direction — the video walks through six different ways to interpolate motion, in roughly the order the author discovered them, with visual side-by-side comparisons (colored spheres/labels) for each parameter combination. It covers both **Vector3 springs** (position/movement) and **single-float springs** (e.g. a "how locked-on" rotation value going from 0 to 50), ending with the author's personal "Lerp Library" project file (free for patrons/members, $15 on ArtStation/Fab for everyone else) that collects all these formulas and test scenes for quick reference.

### Key Steps
1. **Vector Spring Interp node (built-in):** Right-click the exposed `Spring State` pin → Promote to Variable. Wire `Get Actor Location` → `Current`, `Get World Delta Seconds` → `Delta Time`, target coordinates → `Target`, output → `Set Actor Location`. Tune three exposed values: **Stiffness** (resistance to bouncing — higher = less springy), **Critical Damping Factor** (how tightly it sticks once near target — low values like 0.1 overshoot a lot, ~5 gives almost no overshoot), **Target Velocity Amount** (how fast it reaches the goal — <1 undershoots, >1 overshoots then settles). Author's drone values: Stiffness 2, Critical 0.2, Velocity 0.15.
2. **Custom "Sperp" (Spring Lerp) formula** (contributed by patron Chloe Valencia, ported from a Unity/C# project): `speed = Lerp(speed, (target - position) * force / 100, stiffness / 100); return position + speed`. Implemented as static C# helpers `Sperp1D/2D/3D/4D(position, target, stiffness, force, ref speed)` and, in Blueprint, as: `Target - Current Location` → multiply by **Force** → divide by 100 → feed as alpha-target into a `Vector3 Lerp` against an accumulating speed vector, alpha = **Stiffness** / 100 → add result to current location. Only 2 tunable values (Stiffness = bounciness, Force = speed) versus the 5-6 for the built-in node, and no manual Delta Seconds/time wiring needed.
3. **Float Spring Interp:** same Vector Spring Interp node/math, just typed for a single float instead of Vector3 — used for values like a drone's "target lock" rotation blend (0 → 50).
4. **FInterp To (default float interp node):** plug in `Position`/`Position Target` (start/target), `Interp Speed`, get a smoothed float — simple but "not smooth both ways," abrupt at the start of the transition (author rarely uses it because of this).
5. **Ease node:** inputs `A` (current value), `B` (target value), `Alpha` (0→1, drives A→B), and a **Function** dropdown with many interpolation curve types (Linear, Step, Sinusoidal In/Out/InOut, Ease In/Out/InOut, Expo In/Out/InOut, Circular In/Out/InOut) — author mapped every function's curve shape visually for comparison.
6. **Float Ease (Bezier) node:** simpler alternative — `A`, `B`, `Alpha` (0→1), and an **Exponent** (left at 2 by default) producing a single basic Bezier curve; author's preferred day-to-day method for its simplicity.
7. **Timeline (float track):** Add a Timeline component → add a Float Track → right-click to add keyframe points (e.g. 0s = 0, 4s = 100) → right-click a point to smooth its curve tangents. Output feeds directly into whatever value needs controlling; can Play or Play in Reverse. Gives the most manual control over the transition shape, but **interrupting playback mid-timeline causes the value to jump to the start/end** rather than continuing smoothly — the one caveat to watch for.

### UE Systems / Blueprints / Settings
- **Nodes:** `Vector Spring Interp` / `Float Spring Interp` (Spring State promoted to variable; params: Stiffness, Critical Damping Factor, Delta Time, Mass, Target Velocity Amount), `Lerp` (Vector3), `FInterp To`, `Ease` (Function dropdown), `Float Ease` (Bezier, Exponent param), `Timeline` component with a Float Track.
- **Custom C# reference implementation** (`InterpolatedMovement` static class) shown on-screen: `Sperp1D/2D/3D/4D` methods implementing the Lerp-based spring formula, portable to any engine that supports Lerp.
- **Author's reusable asset:** a standalone "Lerp Library" UE project collecting all six methods with live-tunable test scenes for quick parameter recall — free for Patreon/YouTube members, $15 on ArtStation/Fab otherwise (no info exclusive to the paid version — it's a convenience file, not new content).

### Difficulty
Intermediate — assumes comfort with Blueprint graphs, promoting pins to variables, and basic vector math; no C++ required (the C++ code shown is reference-only/ported-from-Unity, not something the viewer needs to write).

### UE Version
Not specified (Blueprint nodes — Vector/Float Spring Interp, Ease, Float Ease, Timeline — consistent with recent UE5.x).

### Tags
blueprint, animation, pipeline, intermediate

---

## Related Entries
- No other ingested unreal-sidekick tutorial currently covers the Spring Interp / Ease / Float Ease / Timeline interpolation node family in depth — this is the first dedicated entry on Blueprint motion-smoothing techniques. A tangential mention exists in the Black Eye top-down camera tutorial (camera composition "springs back to center" on slowdown), but that's a different, narrower technique (camera lag), not the same node family.
