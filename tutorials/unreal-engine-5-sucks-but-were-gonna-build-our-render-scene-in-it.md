---
title: UNREAL ENGINE 5 SUCKS BUT WERE GONNA BUILD OUR RENDER SCENE IN IT
source: YouTube
url: https://www.youtube.com/watch?v=z-NpMJFsiUA
author: Jared Chavez
ingested: 2026-09-04
ue_version: "UE 5.4+ (inferred)"
tags: [materials, shaders, lighting, camera, post-process, rendering, beginner]
extraction_status: complete
frames_dir: tutorials/frames/unreal-engine-5-sucks-but-were-gonna-build-our-render-scene-in-it/
frame_count: 10
frame_status: complete
uncertainty_frames: []
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# UNREAL ENGINE 5 SUCKS BUT WERE GONNA BUILD OUR RENDER SCENE IN IT

**Source:** [YouTube](https://www.youtube.com/watch?v=z-NpMJFsiUA)
**Author:** Jared Chavez
**Duration:** 12m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Welcome back to Unreal 5 for Character Artist. We're going to pick up where we left off in the last one, which was we went through the process of creating our materials and our textures for our scene and our asset.
[0:12] Now, the next stage of putting together a project inside of Unreal is going to be to build the scene that we're going to start to render our character in.
[0:21] Now, I'm going to keep this very simple, very easy, and quick to do. The first thing that we're going to want to do is build a stage.
[0:28] So let's go ahead and jump over to Maya so that we can create our stage real fast.
[0:32] Okay, in here, all I'm going to do, this is going to be a quick little process. So we will start with a single-sided plane, and we're going to scale it up a little bit, and we're going to extend it out wide.
[0:45] Next, we will just grab this section and extrude up. So this is going to be our stage that we're going to use as our backdrop for our character.
[0:54] This is going to be just a quick little model that we can bring inside of Unreal so that we can have this as our backdrop.
[1:02] So let's add a bevel here, add a couple of segments so that this isn't just a sharp corner, and we'll set this to a value of .33, and this should probably good.
[1:15] There's going to be a little bit of taper off so that we're not going to get a harsh shadow at the bottom, and you can kind of even see here with the way that the normals are acting.
[1:23] That's giving us a nice gradient from this darker section of the backdrop up to this lighter section.
[1:30] Okay, so once we have this, what we're going to want to do is we're going to export this out to Unreal.
[1:36] Then once we have exported our backdrop, we're going to come back to our Unreal scene.
[1:41] Now you'll notice there isn't much going on in this scene. All that's in here currently is a single light as well as our model.
[1:48] Now we're going to go through the process like we did with this model to import our mesh.
[1:53] So let's do that real fast inside of our mesh folder. We'll come here, right click and go to import.
[1:59] Now once we have this dialog box, we don't have to worry about any materials being brought in or any of the meshes being combined because there's only one single mesh.
[2:09] We don't have any materials assigned to this in order to create new materials.
[2:13] So we'll hit import all and that will bring up our backdrop mesh.
[2:18] So if we double click this, we will now have our second window open, which you can notice the scale of this is probably too small.
[2:27] And one of the other things that you may also notice is we are seeing some UV issues down here on this area.
[2:34] This doesn't really matter for the purposes that we're going to use it for.
[2:38] If you do want to create a backdrop that does have tiling textures or any sort of texture information on it, then that is obviously something that you would want to resolve.
[2:48] In this case, I'm just going to be using solid colors, roughness to describe the material of our backdrop.
[2:55] So let's go ahead and save that. And we're going to create a new material for our backdrop.
[3:02] So we'll come here, we will right click, create a new material.
[3:06] And we're going to call this our backdrop underscore master material and per master.
[3:13] And then really quickly, we're just going to start plugging in some values into this so that we can use this to control and create an author of material for our backdrop.
[3:24] So let's go to constant vector three, search next for a constant.
[3:31] And we will also copy that and then paste another constant in here.
[3:37] So our first constant three vector, what this is going to do is this is going to allow us to come in and color tint our material to whatever we want.
[3:47] So that is going to be plugged into our base color.
[3:50] And then our next value is going to be plugged into our metallic.
[3:54] And our last value is going to be plugged into our roughness map.
[3:58] Now, in order to make it that we're not constantly coming into this master material and fiddling with it, what we're going to do is we're going to set this back to our value of zero and set that to a value of white so that we have a black value.
[4:13] And we're going to right click on here and go to convert to parameter.
[4:17] So we'll name this color.
[4:19] We'll do the same for these two by converting to parameter.
[4:24] This is going to be named metal.
[4:26] And then this is going to be named roughness.
[4:31] So now if we go ahead and save that, we'll come back here and we will create an instance of that backdrop material.
[4:40] So backdrop, we will do gray underscore M I now back on our backdrop.
[4:51] Let's open this backup.
[4:52] We'll move this off to the side and we are going to drag and drop this new material and slot it into our material window.
[5:01] So we have that all assigned.
[5:03] Let's go ahead and save that.
[5:05] And what we want to do next is just drag and drop our backdrop into the scene, which is back right here.
[5:13] And it is very teeny tiny.
[5:16] That's totally fine.
[5:17] I don't have a problem scaling this up.
[5:19] If you do want to have some uniformity and consistency between your assets, hopefully you've established a scale from the beginning of your projects in order to keep that consistent through every asset that you're making.
[5:32] But if not, if you're someone like me who just decided to come in and scale up their assets as needed, that is totally fine.
[5:43] So I used a value of 800 and we can see that this now produces a pretty large stage.
[5:50] We'll set this maybe to like 500 instead 500, 500, and then we can walk that.
[5:58] So as you saw, we were able to scale up inside of Unreal in order to give us a good result.
[6:05] Now the problem is the material that we created is really, really, really dark.
[6:10] And what that's ultimately leading to is we're just seeing a black void.
[6:15] We're not getting any bounce light or anything in here.
[6:17] So to alleviate some of that, what we're going to do is come into this material.
[6:22] We're going to save it real quick.
[6:24] We're going to turn on our checkboxes and we can come in and start to play with our material.
[6:30] Now you'll notice that as soon as we do that, you can see some of that material information responding to the light that we have in here.
[6:39] So when it was black, we essentially weren't getting any light response or light bouncing from this.
[6:44] As we start to bring it up, we're starting to get some of that reflection and shadowing on our backdrop, which is what we want.
[6:52] You can also see we do have some reflections happening in the material based on what our roughness value is.
[6:58] So we will adjust that so it's not quite as harsh.
[7:02] And I'm going to set this probably to a value of about point four and don't want it too white.
[7:10] And then I will come in here and start to play with my roughness value.
[7:14] So I'll also set this to a value of about point four.
[7:17] The metallic, if I set this to a value of one, what that's going to indicate is that's going to turn this backdrop into a metalness backdrop,
[7:29] which may or may not be what we want.
[7:31] For this case, I'm going to set this to a value of point one.
[7:36] So there's going to be a little bit of that metallic shine to it, but not too much.
[7:40] Obviously you can play with this depending on what your needs are.
[7:43] So let's go ahead and save this.
[7:45] So we're almost done setting up our scene.
[7:48] The next aspect that we're going to want to tackle is going to be a little bit of a tricky one.
[7:51] So it's first going to start with introducing and adding a light to this scene.
[7:57] So we'll come over here to this little drop down box and come down to cinematic.
[8:02] Next, we're going to drop a cinematic camera actor into our scene.
[8:06] You'll see that it highlights and this is what it looks like.
[8:09] When you click on the actor, you'll get this little window right here that shows what the camera is seeing.
[8:16] So now if I turn this, you can see that is starting to update, but you'll also see something really, really interesting about this image.
[8:26] If we turn from here and then show the model again, it progressively gets brighter over time.
[8:33] Now what's happening here is the camera is acting the way a real world camera would be acting with an adaptive exposure.
[8:41] So imagine if you were to walk outside when you've been in a really dark room and then you walk outside and everything feels really, really bright.
[8:49] Or when you come from a really, really bright outside into a dark room, your eyes need a second to readjust and reexpose to the light.
[8:57] So we're going to do that same sort of process inside of Unreal so that we don't constantly have to worry about our camera adjusting its exposure.
[9:08] So to just check this out a little bit further, if we click on pilot and turn this way and then turn back to our asset, you can see that it slowly starts to reexpose.
[9:18] This isn't a look or something that we want just for the sake of working on an asset.
[9:25] So we're going to fix this really quick, but in order to do that, we're going to come down here to all classes and we're going to search for post process of volume.
[9:35] We'll click that and that is going to drop this little box inside of our scene.
[9:40] Now this box, what this box is going to do is it's going to have a post processing setup or information based on the bounds of this box.
[9:50] So if we click on our camera and pilot it again, if we come over into our box, nothing's going to happen.
[9:57] But if we start to change the information that this box has, then that box is going to provide information inside of the bounds of this box.
[10:07] So I'll illustrate this real quick. We're going to search for exposure and in here we're going to come and click on exposure compensation and we're going to click on min EV 100 and max EV 100.
[10:21] And we're going to set both of these to a value of one.
[10:25] Now you're going to notice that nothing happens.
[10:27] But if we come over here and then go into our post process volume, it's like something switches.
[10:35] Our model is no longer lit really all that bright.
[10:38] And if we turn this way and turn back to it, it never changes. It's not updating.
[10:43] The reason for that is because now we are clamping down our exposure values inside this post process volume.
[10:49] If I come back out here, you can see that our exposure is readjusting.
[10:53] Now this post process volume, you can do one of two things with it.
[10:57] The first one is you could scale it up.
[10:59] You could put it in your scene and you could leave your box.
[11:04] Essentially wherever your camera goes, but that's not really the easiest or most beneficial way of doing it.
[11:10] I usually like to just leave it somewhere in my scene off to the side.
[11:15] And then what I do, I look for infinite extend unbounded.
[11:20] So what that's going to do is it's going to say this post processing volume expands and encapsulates everything in this scene.
[11:27] So we'll go ahead and check this real quick.
[11:29] And now you will notice that even if I go into this bounding box,
[11:33] I don't have that same compensation exposure happening that was happening before, which is good because this makes it easier for me to tune my lights to just work in a true nature of my scene when I'm building out the renders for my character.
[11:47] So if we come to our spotlight real quick, we'll turn this off and we will set this to 15, 25, maybe 55.
[11:57] You can see that we are starting to get a little bit more lighting information into our scene.
[12:04] Maybe we'll set this to 350.
[12:06] And now our scene should be all set up and ready to start building our lighting.
[12:13] So we're going to go ahead and leave it here for right now.
[12:16] Hopefully you guys found this beneficial.
[12:18] If you want to follow along for the rest of the process, make sure to like, subscribe and comment for more.
[12:24] And I will see you guys in the next one.
[12:26] Thanks for stopping by. Bye guys.



---

## Captured Frames

- [1:05] tutorials/frames/unreal-engine-5-sucks-but-were-gonna-build-our-render-scene-in-it/frame_000.jpg
- [3:26] tutorials/frames/unreal-engine-5-sucks-but-were-gonna-build-our-render-scene-in-it/frame_001.jpg
- [4:19] tutorials/frames/unreal-engine-5-sucks-but-were-gonna-build-our-render-scene-in-it/frame_002.jpg
- [5:45] tutorials/frames/unreal-engine-5-sucks-but-were-gonna-build-our-render-scene-in-it/frame_003.jpg
- [7:05] tutorials/frames/unreal-engine-5-sucks-but-were-gonna-build-our-render-scene-in-it/frame_004.jpg
- [7:33] tutorials/frames/unreal-engine-5-sucks-but-were-gonna-build-our-render-scene-in-it/frame_005.jpg
- [8:04] tutorials/frames/unreal-engine-5-sucks-but-were-gonna-build-our-render-scene-in-it/frame_006.jpg
- [9:37] tutorials/frames/unreal-engine-5-sucks-but-were-gonna-build-our-render-scene-in-it/frame_007.jpg
- [10:23] tutorials/frames/unreal-engine-5-sucks-but-were-gonna-build-our-render-scene-in-it/frame_008.jpg
- [11:22] tutorials/frames/unreal-engine-5-sucks-but-were-gonna-build-our-render-scene-in-it/frame_009.jpg

---

## Structured Notes

### Core Technique
Building a minimal character-render stage in Unreal — a bevelled backdrop mesh, a parameterised master material driven through a Material Instance, and a `PostProcessVolume` with `Min EV100` / `Max EV100` clamped and `Infinite Extent (Unbound)` enabled to stop auto-exposure drifting while you light the shot.

### Summary
Part of a "Unreal 5 for Character Artists" series, picking up after materials and textures. The 3D work is deliberately trivial: a single-sided plane in Maya, extruded up into an L-shaped cyclorama and bevelled so the corner reads as a soft gradient rather than a hard shadow line. The Unreal work is where the value is. A master material exposes Color, Metal and Roughness as parameters so the backdrop is tuned through a Material Instance rather than by reopening the graph. Then the real problem: a `CineCameraActor` applies adaptive exposure, so the image re-brightens every time the camera turns — useless for judging lighting. The fix is a `PostProcessVolume` with exposure clamped and its bounds set to unbounded, so it governs the whole level regardless of where the camera sits.

### Key Steps
1. **Model the backdrop in Maya.** Single-sided plane, scaled wide, then extrude one edge upward to form the vertical section of a cyclorama `[transcript 0:32-0:53]`.
2. **Bevel the corner.** A couple of segments at a value of **`0.33`**, so the transition is soft — this avoids a harsh shadow at the base and gives a gradient from the darker floor into the lighter back wall `[transcript 1:02-1:29]`.
3. **Import into Unreal.** Right-click in the mesh folder → Import → `Import All`. No material or mesh-combine options matter here since it is one mesh with nothing assigned `[transcript 1:48-2:17]`.
4. **Expect it to be small, and expect UV problems.** The mesh imports at the wrong scale and has UV issues at the bevel — irrelevant for a solid-colour backdrop, but would need fixing for tiling textures `[transcript 2:18-2:53]`.
5. **Create the master material** `BackDrop_M` `[transcript 2:55-3:12]`.
6. **Wire three inputs**: a `Constant3Vector` into `Base Color`, and two `Constant` scalars into `Metallic` and `Roughness` `[frame_002]` `[transcript 3:24-3:57]`.
7. **Convert them to parameters** — right-click → Convert to Parameter — named **`Color`**, **`Metal`** and **`Roughness`**, so the material never has to be reopened to adjust `[frame_002]` `[transcript 4:13-4:29]`.
8. **Create a Material Instance** (`BackDrop_Grey_MI`) and assign it to the mesh `[frame_005]` `[transcript 4:31-5:04]`.
9. **Scale it in-engine.** The author tries `800`, settles near `500` — noting that a scale convention established at project start is better practice, but scaling as needed is acceptable `[transcript 5:13-5:49]`.
10. **Fix the black-void problem.** A near-black backdrop returns no bounce light at all; raising the Color parameter starts producing visible light response, shadowing and reflections `[transcript 6:05-6:57]`.
11. **Tune the three parameters.** Roughly `0.4` for colour and roughness, and a low `Metallic` — `0.1` per narration, since `1.0` would turn the backdrop fully metallic `[transcript 7:02-7:42]`. The Material Instance panel at the sampled moment reads `Metal 0.744008`, `Roughness 0.45` mid-adjustment `[frame_005]`.
12. **Add a `CineCameraActor`** from the Cinematic category in the placement dropdown `[transcript 7:57-8:15]`.
13. **Observe the actual problem.** Turning the camera away and back makes the image progressively re-brighten — Unreal's adaptive exposure imitating a real camera adjusting to a dark room `[transcript 8:16-9:24]`.
14. **Add a `PostProcessVolume`** via All Classes `[transcript 9:25-9:39]`. It applies its settings only within its box bounds `[transcript 9:40-10:06]`.
15. **Clamp exposure.** Search `expos`, enable **`Min EV100`** and **`Max EV100`** and set both to the same value — narration uses `1` `[frame_008]` `[transcript 10:07-10:24]`. Defaults are `-10.0` and `20.0` `[frame_008]`. Inside the volume the exposure now holds steady; outside it still drifts `[transcript 10:27-10:52]`.
16. **Make it global.** Rather than scaling the box to cover the camera's travel, enable **`Infinite Extent (Unbound)`** under Post Process Volume Settings, so the volume governs the entire level and can sit anywhere `[frame_009]` `[transcript 10:53-11:31]`.
17. **Light it.** With exposure locked, the spotlight can be tuned honestly — the author steps intensity through 15, 25, 55 and lands near `350` `[transcript 11:47-12:06]`.

### UE Systems / Blueprints / Settings
- **`BackDrop_M`** (Material) — `Constant3Vector` → `Base Color`; two `Constant` scalars → `Metallic` and `Roughness`; base pass shader reported at **192 instructions** `[frame_002]`
- **Material parameters** — `Color` (Vector Parameter, `Group: None`, `Sort Priority 32`), `Metal`, `Roughness` `[frame_002]`
- **`BackDrop_Grey_MI`** (Material Instance) — parent `BackDrop_M`; Global Scalar Parameter Values `Metal`, `Roughness`; Global Vector Parameter Values `Color` `[frame_005]`
- **`CineCameraActor`** — placed from the Cinematic category; exhibits adaptive exposure by default `[transcript 7:57-8:15]`
- **`PostProcessVolume`** → Lens → Exposure — `Metering Mode: Auto Exposure Histogram`, `Exposure Compensation`, **`Min EV100`**, **`Max EV100`** (defaults `-10.0` / `20.0`), `Speed Up 3.0`, `Speed Down 1.0`; Advanced: `Low Percent 10.0`, `High Percent 90.0`, `Histogram Min/Max EV100 -10.0 / 20.0` `[frame_008]`
- **`PostProcessVolume`** → Post Process Volume Settings → **`Infinite Extent (Unbound)`** `[frame_009]`
- **Scene actors** — `Backdrop` (StaticMeshActor), `CineCameraActor`, `PostProcessVolume`, `SpotLight`, `Torso_Low` (StaticMeshActor) `[frame_008][frame_009]`
- **Maya side** — single-sided plane, edge extrude, bevel at `0.33` with added segments `[transcript 1:02-1:14]`

> **Frame vs narration.** `[transcript 7:31]` says the Metallic parameter is set to `0.1`;
> the Material Instance panel at `[frame_005]` reads `Metal 0.744008` with `Roughness 0.45`
> — the frame catches the value mid-drag, before it settles. The narration's figures are
> the intent, the frame's are a snapshot. Both recorded rather than picking one.
>
> Also worth naming precisely: narration says "infinite extend unbounded"; the checkbox
> reads **`Infinite Extent (Unbound)`** `[frame_009]`, and the exposure fields are
> **`Min EV100`** / **`Max EV100`** `[frame_008]`.
>
> **The title is clickbait.** Despite "UNREAL ENGINE 5 SUCKS", the video contains no
> criticism of Unreal — it is a straightforward backdrop-and-exposure setup tutorial.

### Difficulty
Beginner

### UE Version
Not stated in narration and not visible in the title or status bar. The Material Editor shows a **`Substrate`** tab alongside `Stats`, and the material output node exposes `Surface Thickness` and `Front Material` pins `[frame_002]` — both Substrate-era, indicating **UE 5.4 or newer**. Recorded as an inference from the UI, not as a confirmed version.

### Tags
materials, shaders, lighting, camera, post-process, rendering, beginner

---

## Related Entries
- [Lighting in Unreal Engine 5 for Beginners](lighting-in-unreal-engine-5-for-beginners.md) — the lighting pass this video stops just short of; locking exposure first is what makes those lights tunable at all; shares lighting, beginner
- [The 2025 Guide to Rendering in Unreal Engine 5](the-2025-guide-to-rendering-in-unreal-engine-5.md) — takes a prepared scene like this one through MRQ output; shares rendering, camera
- [Designing Visuals, Rendering, and Graphics with Unreal Engine](designing-visuals-rendering-and-graphics-with-unreal-engine.md) — Epic's own reference for the post-process and materials systems used here; shares materials, post-process, lighting, rendering
