---
title: Render separate SHADOWS from Unreal Engine 5.8 with the Shadow Reflection Catcher (Composure EP5)
source: YouTube
url: https://www.youtube.com/watch?v=HrAWf7b8vww
author: Dean Yurke - Unreal Engine and VFX Filmmaking
ingested: 2026-07-15
ue_version: "5.8"
tags: [composure, shadow-catcher, movie-render-graph, deferred-rendering, dilation-pass, compositing, davinci-resolve, fusion, ar]
extraction_status: complete
frames_dir: tutorials/frames/render-separate-shadows-from-unreal-engine-58-with-the-shadow-reflection-catcher/
frame_count: 10
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Render separate SHADOWS from Unreal Engine 5.8 with the Shadow Reflection Catcher (Composure EP5)

**Source:** [YouTube](https://www.youtube.com/watch?v=HrAWf7b8vww)
**Author:** Dean Yurke - Unreal Engine and VFX Filmmaking
**Duration:** 11m2s | 12 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro: The power of Unreal Engine's viewport recording vs. traditional compositing [0:00]
**Transcript (timestamped):**
[0:00] Now, let's get off.
[0:01] So all of this is recorded directly inside
[0:03] of Unreal Engine's viewport in 3D in context,
[0:06] which is mind blowing.
[0:08] But if you're from a traditional compositing background
[0:10] myself and you want to get all of these elements
[0:13] into your favorite compositing software,
[0:15] I'm going to show you that in this video right now.


### Recap: AR in Unreal Engine 5.8 and 3D camera projection [0:18]
**Transcript (timestamped):**
[0:19] So this is a follow up to my last video
[0:21] on how to do augmented reality in Unreal Engine 5.8.
[0:25] So currently this is composited directly inside of the viewport
[0:29] in 3D using camera projections.
[0:32] So I turn this off and we look around here.
[0:34] So here we are in a 3D space.
[0:36] And we've got a camera up here that's
[0:37] re-projecting this video onto geometry and then re-filming it.
[0:42] And these are called composite mesh actors.
[0:45] And here we can use a mask now and combine it
[0:47] with a composite mesh actor.
[0:49] So we can make things work in 3D.
[0:51] As we go around the world, these sort of like camera projections
[0:54] are existing in 3D.
[0:56] So this is super cool and completely weird.


### Why we need separate render layers for high-end VFX compositing [0:58]
**Transcript (timestamped):**
[0:59] But if you're a compositor, you're
[1:00] used to having layers so that, saying this example,
[1:04] this character here was intersecting the edge of the sofa.
[1:07] And so it's kind of eating in a little bit here.
[1:09] And if I come back a bit, his shadow, when he's over me,
[1:13] we're getting a slight edge.
[1:15] So we're going to render out these elements as separate layers
[1:19] so that we can combine them together and really
[1:22] finesse these things in comp.
[1:24] Now if you're from the Visual Effects world,
[1:25] you're used to renders taking 30 minutes overnight renders,
[1:28] basically.
[1:29] And because it takes so long to render with a regular renderer,
[1:33] you don't really want to make any changes,
[1:35] because then you've got to spend another day
[1:36] with a render farm rendering the shop.
[1:39] So you want to have lots of AOVs and render layers
[1:42] so that you can dial all these things in comp, which
[1:44] is much faster compared to rendering in a traditional renderer.
[1:48] But with Unreal Engine and games,
[1:51] it's used to rendering really, really fast.
[1:53] So it doesn't keep on you that information.
[1:54] It's using deferred rendering.


### Understanding deferred rendering and baked lighting in games [1:55]
**Transcript (timestamped):**
[1:56] Now deferred rendering, if you're from the games world,
[1:58] you'll kind of understand this.
[2:00] So in games, the fastest way to render
[2:03] is if you go into the Unlit mode.
[2:05] But this, look at that, they're already
[2:07] it's really fast.
[2:08] But this doesn't look so good.
[2:10] But to make it look good, you're rendering lit.
[2:12] And now it's going to calculate all the lighting
[2:14] and the bounce and the global illumination, et cetera.
[2:16] So that is much slower.
[2:20] There's a trick in video games where you bake the lighting.
[2:23] What that does is it calculates all of the influence
[2:25] from the lights and the bounce from the global illumination.
[2:28] And it basically gives you one channel, which
[2:31] is a multiply channel.
[2:32] And that looks like this.


### How baked lighting works as a multiply layer [2:33]
**Transcript (timestamped):**
[2:33] So if I go into my shadow reflection catcher
[2:37] and change that from a multiply to an over,
[2:41] it actually looks like this.
[2:42] I'm going to turn him off too.
[2:43] And it's like, oh, what is that?
[2:45] The reason why this is white is that this is a multiply layer.
[2:48] So it's going to take this value, which is, say, 1,
[2:50] and it's going to multiply the background by that value.
[2:54] So anything times 1 is the same value.
[2:56] So it can look exactly the same where it's white.
[2:59] Whereas here, where we got a bit of blue and a bit of yellow,
[3:02] it's going to multiply that by a different value.
[3:05] And so that will then subtract this value from the base layer.
[3:10] And so what that gives you when you actually change it
[3:11] from an over to a multiply is it looks like it's the correct lighting.
[3:16] So that's how video games are able to render super fast
[3:19] if they're using baked lighting.
[3:20] So that's awesome for video games, because it's really fast.
[3:22] But it's terrible for compositing.
[3:24] If you don't have control of, say, the catch shadow
[3:26] and the intensity of this light or that light.
[3:29] And so from a comp, we come in and we're like,
[3:32] what can we have?
[3:33] And the answer is not much.
[3:35] But from now, we're going to at least
[3:37] give you the shadow reflection layer, thanks to composure.


### Increasing render fidelity: Adjusting render target resolution [3:40]
**Transcript (timestamped):**
[3:40] So before we render this past, there's
[3:41] one thing we can do to increase the fidelity of the renders.
[3:44] And that is to go to our render target resolution
[3:47] under our shadow reflection catcher
[3:49] and change this default 540p resolution.
[3:53] So I'm going to make it 1440p.
[3:55] And if you look here, I have to blow this up,
[3:57] you'll see the quality of this will improve.
[4:02] Jalega, it does tick so well.
[4:04] So this isn't the final render resolution.
[4:07] That set inside of our movie render graph.


### Configuring Movie Render Graph for the Shadow Catcher pass [4:10]
**Transcript (timestamped):**
[4:11] So I'm going to go into my movie render graph
[4:12] and load up my settings for my previous spawn,
[4:15] just my alien shot here.
[4:17] And then we'll go into that configuration.
[4:19] And then I kind of go over this in detail on the last video.
[4:22] And I go to my output directory and then make a layer.
[4:26] We're going to call this one shadow catcher.
[4:29] I'm going to go in there and I'm going to say select folder.
[4:32] And then we're going to go into our EXR sequence.
[4:35] And I'm going to give it a name.
[4:37] And it'll be shadow reflection dot frame them.
[4:43] And then we'll hit save on that.
[4:46] Lower this and then I just hit render.
[4:49] And this will render this out.
[4:51] So our shadow reflection render pass has now been done.


### Handling occlusion issues when rendering characters separately [4:55]
**Transcript (timestamped):**
[4:55] And so next what we want to do is we want to render
[4:57] just our character on his own.
[5:00] But we're going to have a slight issue in that say,
[5:03] we're at a frame like this.
[5:04] I'm just going to change my shadow reflection capture
[5:07] back to its default multiply.
[5:09] Now I've got me currently, I'm projected
[5:12] onto a piece of geometry.
[5:15] And let me turn off here.
[5:16] So I'm in 3D.
[5:18] So from this camera, I'm projecting the video
[5:20] onto this piece of geometry.
[5:22] And I'm cutting it out with a mat.
[5:24] Now if I go back into here, now when he's over this character,
[5:29] I ideally, I don't want this here.
[5:31] But if I turn my layer off to get this perfect edge here,
[5:38] so I can put this back on top, you can see now
[5:41] that I've lost my shadows.
[5:42] So when you put me on, I'm shadowing this.
[5:46] But when you turn me off, I'm getting what I want.
[5:49] So we need an in-between stage.


### Using the new Dilation Pass in UE 5.8 to fix edge artifacts [5:51]
**Transcript (timestamped):**
[5:51] And thankfully, in Unreal 5.8, there is now a dilation pass.
[5:57] So we go and select our layer.
[6:00] And then we go under here under Media Passes.
[6:03] And we add a plus dilation.
[6:07] And then I'm just going to change it from RGBA just
[6:10] to the alpha.
[6:12] And now I'm going to shrink this mat here.
[6:15] So if I shrink this mat, you can see what's going on there.
[6:18] Look.
[6:19] So we're still getting the influence of the shadow.
[6:21] It's a couple of pixels slightly smaller.
[6:24] But it's enough to allow me to be able to put this back on top.
[6:27] And I'm also going to turn off this Carry RGB with alpha.
[6:30] That gets rid of that little white edge that we're getting there.
[6:33] So we can shrink this mat in to minus 20.
[6:38] So let's do that on all the layers.
[6:40] So I'm just going to select my camera one, going to add a dilation.
[6:48] Shrink that down, change it from red, green, blue, turn those off.
[6:53] And then you can see this here.
[6:55] Still have a little white thing.
[6:56] Turn off Carry off, RGBA thing.
[6:59] So now when he goes behind this, you'll
[7:01] still get the influence of it.
[7:03] But it won't be eating his edges.
[7:05] So now all of these mats are slightly smaller,
[7:08] but I'll take it.


### Setting up the Main Render (Beauty) pass with alpha [7:10]
**Transcript (timestamped):**
[7:10] So next thing we have to do is we have to go into our main render.
[7:15] And then we go and change the operation of him.
[7:18] He's our main render.
[7:20] And we're going to change that from an over to a non.
[7:25] And so now when we come to render this, all of those objects are still there.
[7:30] And they're still casting a shadow.
[7:31] And because I've got the dilate pass on,
[7:33] I've got a little bit more of the original render.
[7:36] So that when we do it this in 2D, I'll
[7:38] be able to get nicer edges.
[7:40] Woof!
[7:41] So now we're ready to render.
[7:43] And we go into our movie render graph.
[7:45] And then we specify the name of the pass.
[7:48] And I've already done it beauty.
[7:50] And then hit save.
[7:51] And then hit render.
[7:54] And now when it renders, you should see this checkerboard.
[7:58] Because that's showing you that this has got an alpha.


### Compositing in DaVinci Resolve: Recreating the shadow with Multiply mode Creative use cases: UFO shadows and traditional call-to-actions [8:00]
**Transcript (timestamped):**
[8:00] So I'm in Dimitri Resolve, but you can use a few favorite compositing or editorial software
[8:04] is.
[8:05] And we've got our three passes that we rendered.
[8:08] So we've got our background layer.
[8:10] And we've got our foreground.
[8:11] And it's going to find somewhere where we will shadow.
[8:14] And then we've got our shadow reflection pass.
[8:16] And at the moment, by default, it's set to normal mode.
[8:19] So you go to your composite mode, and you change it from normal to multiply.
[8:25] There we are.
[8:26] And so now it's multiplying that background by that pass.
[8:29] And so it's recreating what we were getting inside of Unreal Engine.
[8:33] Hurrah!
[8:34] So you can see here now that it's got the eroded edges.
[8:37] So what we really want to do is go into a compositing type software and really finesse
[8:41] these edges using those magic masks or better.
[8:44] But before we do that, I wanted to show you some of the use cases.
[8:47] So in this one, I've got my little UFO.
[8:51] And then I've got a shadow for him.
[8:53] And the shadow is done exactly the same way.
[8:54] So I rendered the hymns separately.
[8:56] And then I rendered the shadow reflection layer.
[8:58] By default, it would look like this.
[9:00] But we're going into our multiply mode.
[9:04] And then I'm changing the opacity.
[9:05] So you can mix this on off.
[9:06] So it's great for like title stuff and transitions.
[9:09] And more of your traditional sort of call to actions.
[9:16] So here, you can change the background and put this over whatever you want.
[9:20] All right.
[9:21] Hint, hint.


### Fusion: Node setup for shadow layers and magic masks [9:22]
**Transcript (timestamped):**
[9:22] OK.
[9:23] Now we're going to go into Fusion.
[9:25] So in Fusion, I've got my plate.
[9:27] And then I've got a resize, because it's a different resolution.
[9:30] And then we've got our shadow reflection layer.
[9:33] And I'm using, in the merge node,
[9:35] I'm using a multiply.
[9:37] And then on top of that, I'm adding my character.
[9:41] And then over here, because this is using our eroded version,
[9:46] I wanted to bring in one of our channels
[9:48] that we made earlier with our magic masks.
[9:50] And I'm using a channel booleum to turn the blue channel into the alpha.
[9:55] And then that gives us this.
[9:57] And then I'm adding in a road and a blur.
[9:59] So we can put this layer back on top of this layer.
[10:06] So now we can restore that layer.
[10:08] And then we can go through and apply that to everywhere.
[10:10] So as I go back here, when he stands up and goes in front of me,
[10:16] his hand's going in front.
[10:18] So now I'd need to take this off and I could either do a little mat here,
[10:22] or I can go through and animate the transparency of this one here.
[10:28] So there's a bunch more things that we could do
[10:29] that I'm not going to cover things like adding grain
[10:31] using the regular non-distorted plate
[10:34] and actually distorting all of our magic masks and renders.
[10:37] That way you're keeping the integrity of the plate,
[10:40] chromatic aberration on our renders, basically,
[10:43] as a whole, another six-part video series that I'm not going to make.
[10:46] All right, so now I'm going to go and start thinking about
[10:50] the original thing I was going to write next,
[10:52] which is the composite depth for measure actors.
[10:55] So wish me luck on that, and I'll see you on the next Composure video.



---

## Captured Frames

- [0:32] tutorials/frames/render-separate-shadows-from-unreal-engine-58-with-the-shadow-reflection-catcher/frame_000.jpg
- [1:04] tutorials/frames/render-separate-shadows-from-unreal-engine-58-with-the-shadow-reflection-catcher/frame_001.jpg
- [2:33] tutorials/frames/render-separate-shadows-from-unreal-engine-58-with-the-shadow-reflection-catcher/frame_002.jpg
- [3:53] tutorials/frames/render-separate-shadows-from-unreal-engine-58-with-the-shadow-reflection-catcher/frame_003.jpg
- [4:26] tutorials/frames/render-separate-shadows-from-unreal-engine-58-with-the-shadow-reflection-catcher/frame_004.jpg
- [6:03] tutorials/frames/render-separate-shadows-from-unreal-engine-58-with-the-shadow-reflection-catcher/frame_005.jpg
- [7:18] tutorials/frames/render-separate-shadows-from-unreal-engine-58-with-the-shadow-reflection-catcher/frame_006.jpg
- [7:58] tutorials/frames/render-separate-shadows-from-unreal-engine-58-with-the-shadow-reflection-catcher/frame_007.jpg
- [8:19] tutorials/frames/render-separate-shadows-from-unreal-engine-58-with-the-shadow-reflection-catcher/frame_008.jpg
- [9:33] tutorials/frames/render-separate-shadows-from-unreal-engine-58-with-the-shadow-reflection-catcher/frame_009.jpg

---

## Structured Notes

### Core Technique
Break Unreal Engine's real-time, in-viewport Composure AR composite (which normally bakes character, shadow/reflection, and background together directly in 3D) back apart into **separate renderable layers** — a Beauty pass (character only, alpha-masked), a Shadow Reflection Catcher pass (baked lighting/shadow/GI influence as a multiply layer), and the background plate — so a traditional compositor can recombine and finesse them frame-accurately in Resolve/Fusion/Nuke, using Unreal 5.8's new **Dilation pass** to fix edge-eating artifacts that occur when a masked character and its separately-rendered shadow don't align pixel-perfectly.

### Summary
The starting point is a Composure-based AR setup (from a prior video) where a live-action character is re-projected in 3D onto a **Composite Mesh Actor** and re-filmed by a virtual camera, with a **Shadow Reflection Catcher** layer providing the ground/environment shadow and reflection contribution. For a traditional VFX compositor used to working with separated render layers (as opposed to games' baked, single-pass **deferred rendering** — where an Unlit render is near-instant but a fully Lit render bakes in all lighting/GI/bounce as one multiply-mode layer for real-time speed), this baked single-layer approach is too rigid for comp-side lighting adjustments. The Shadow Reflection Catcher layer, when toggled from **Multiply to Over** blend mode in Composure, reveals what it actually contains: a mostly-white multiply layer where value 1 leaves the background unchanged, and darker/tinted regions subtract light or add color influence from bounce lighting — this is why flipping it to Over mode looks like a ghostly white silhouette rather than a normal image. Before rendering, render fidelity is bumped by raising the Shadow Reflection Catcher's **Render Target Resolution** from the 540p default up to 1440p (independent of the final Movie Render Graph output resolution) for visibly cleaner shadow/reflection detail. The Shadow Catcher pass is then rendered via **Movie Render Graph**, configuring a named output layer ("shadow catcher"), an output directory, and an EXR image-sequence naming pattern, then hitting Render. Rendering the **character separately** exposes an occlusion problem: since the character is a camera-projected texture cut out with a mask on a piece of 3D geometry, when the character passes behind another object in the scene, disabling the character layer to get a clean occlusion edge also removes the character's contribution to the shadow/reflection pass — losing the correct "character casts a shadow on this surface" interaction. The fix is Unreal 5.8's new **Dilation pass**: added under a layer's Media Passes, set to operate on the Alpha channel only (not RGBA), it shrinks/erodes the character's alpha mask by a controllable amount (e.g. by -20) so the mask edge sits a few pixels inside the character's true silhouette — this keeps enough of the character present to preserve correct shadow-casting influence on the Shadow Catcher pass while still leaving a small enough footprint that a separately-rendered foreground layer can be composited cleanly on top without edge artifacts; disabling **Carry RGB with Alpha** on the same pass removes an additional thin white fringe. This Dilation setup is applied to every relevant camera/layer combination that needs it. The **Main/Beauty render** pass has its blend operation changed from Over to **None** (so it renders with a clean alpha channel rather than pre-composited against the background) and is rendered through Movie Render Graph as a named "beauty" output — its render preview shows a checkerboard pattern confirming the alpha channel exported correctly. In compositing (demonstrated in **DaVinci Resolve** first, then **Fusion**), the three separately-rendered EXR sequences — background plate, character/beauty foreground, and shadow-reflection layer — are recombined: the Shadow Reflection layer's composite mode is changed from Normal to **Multiply** against the background (recreating the same lighting interaction Unreal was doing internally), then the character foreground is placed on top. In Fusion specifically, since the foreground uses the eroded/dilated alpha, an additional **Channel Booleum** node repurposes the blue channel from an earlier "magic mask" pass as a cleaner alpha, followed by an erode and blur to soften the mask edge before merging the character back on top of the shadow-multiplied background — restoring correct occlusion when the character passes in front of or behind other scene elements (with manual masking or animated transparency needed for partial-occlusion cases like a hand crossing in front of another object). Beyond the base film application, the same three-layer (plate / character-or-object / shadow-reflection-multiply) technique is shown applied to a stylized "UFO with shadow" composite for title cards and call-to-action graphics, where the shadow-reflection layer's opacity can simply be animated/mixed to taste against any arbitrary background.

### Key Steps
1. Start from an existing Composure-based AR/3D-composite setup with a Composite Mesh Actor (camera-projected character re-filmed in 3D) and a **Shadow Reflection Catcher** layer providing baked shadow/reflection/GI influence.
2. Understand why this baked single-multiply-layer approach exists: it's the deferred-rendering trick games use for real-time speed (Unlit = instant, Lit = fully baked lighting as one multiply channel) — flip the Shadow Reflection Catcher from Multiply to Over mode to visually inspect what's actually baked into that layer (mostly-white = no change, darker/tinted = subtracted/added light influence).
3. Increase the **Shadow Reflection Catcher's Render Target Resolution** (e.g. 540p default → 1440p) for higher-fidelity shadow/reflection detail before final render (independent of the Movie Render Graph output resolution).
4. Render the **Shadow Catcher pass** via Movie Render Graph: configure a named output layer, output directory, and EXR sequence naming, then render.
5. Identify the occlusion problem when preparing to render the character separately: disabling the character to get a clean edge against occluding objects also removes its shadow-casting contribution to the Shadow Catcher pass.
6. Add Unreal 5.8's new **Dilation pass** (under the layer's Media Passes) set to operate on **Alpha only**; shrink/erode the mask (e.g. -20) so it sits slightly inside the true character silhouette, preserving enough presence for correct shadow influence while minimizing edge artifacts; disable **Carry RGB with Alpha** to remove a residual white fringe. Apply this to every camera/layer combination that needs it.
7. Set the **Main/Beauty render** pass's blend operation from Over to **None** so it exports with a usable alpha channel rather than being pre-composited; render via Movie Render Graph as a named "beauty" pass and confirm the checkerboard alpha pattern in the render preview.
8. In a compositing package (DaVinci Resolve or Fusion), bring in the three rendered EXR sequences: background plate, character/beauty foreground, and shadow-reflection layer.
9. Change the shadow-reflection layer's composite/merge mode from Normal to **Multiply** against the background to recreate the correct lighting interaction, then place the character foreground on top.
10. (Fusion-specific) Since the foreground uses the eroded/dilated alpha, use a **Channel Booleum** to repurpose a "magic mask" pass's blue channel as a cleaner alpha, then erode + blur it before the final merge to restore clean occlusion behavior as the character passes in front of/behind other elements.
11. Apply the same three-layer (plate / subject / shadow-multiply) technique to non-character use cases (e.g. a floating object with a shadow) for title cards, transitions, or call-to-action graphics by simply animating the shadow layer's opacity/mix over an arbitrary background.

### UE Systems / Blueprints / Settings
Composure (Compositing Element pipeline), Composite Mesh Actor, Shadow Reflection Catcher layer (Multiply/Over blend modes, Render Target Resolution), Movie Render Graph (named output layers, EXR sequence output, per-layer blend operation override to None for alpha export), Media Passes → Dilation pass (Alpha-only channel targeting, erosion amount), Carry RGB with Alpha toggle, deferred rendering / baked lighting concept (Unlit vs. Lit render modes).

### Difficulty
Intermediate (requires prior familiarity with the Composure AR/compositing pipeline from an earlier video in the series; the Dilation-pass edge-fix workflow and cross-application compositing setup are approachable once that foundation is in place).

### UE Version
5.8 (per video title; new Dilation pass feature confirmed as introduced in this version).

### Tags
composure, shadow-catcher, movie-render-graph, deferred-rendering, dilation-pass, compositing, davinci-resolve, fusion, ar

---

## Related Entries
[No related entries yet — first Composure/AR-compositing tutorial ingested into this knowledge base; future Composure episodes (e.g. the referenced "composite depth for measure actors" follow-up) should cross-link here once ingested.]
