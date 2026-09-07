---
title: Lumen in Unreal Engine | A Closer Look
source: YouTube
url: https://www.youtube.com/watch?v=2qc7I6bfRBo
author: Karim Yasser
ingested: 2026-09-07
ue_version: "UE 5.5+ (inferred)"
tags: [lumen, reflections, radiosity, surface-cache, console-variables, console-commands, global-illumination, flickering, noise, debugging, rendering, lighting, advanced, youtube, ue5]
extraction_status: complete
frames_dir: tutorials/frames/lumen-in-unreal-engine-a-closer-look/
frame_count: 10
frame_status: complete
uncertainty_frames: []
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Lumen in Unreal Engine | A Closer Look

**Source:** [YouTube](https://www.youtube.com/watch?v=2qc7I6bfRBo)
**Author:** Karim Yasser
**Duration:** 10m33s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] And the frame rate...
[0:05] It's...
[0:06] I believe it was working on 120 more FPS,
[0:10] but probably because of the streaming and recording,
[0:13] and the other project is opened.
[0:15] It's now not working on the same frame rate,
[0:19] but it was hitting over, or more than, 120 FPS.
[0:24] So now, you can see...
[0:27] Like, here's a flickering, as you can see.
[0:31] And I'm sure everyone in here is annoyed by this flickering.
[0:36] And the thing is, I'm not going directly
[0:39] and increasing the final gather quality.
[0:42] But what I'm doing is using...
[0:47] Like, now as you can see, the frame rate is as it is,
[0:51] flickering is not here as before.
[0:54] And...
[0:56] Let me show you...
[0:59] What actually happens.
[1:04] This is...
[1:05] I'll go in depth later on in next chapters,
[1:09] like how we can debug, when we can start,
[1:12] and each of these, what actually each of them does.
[1:17] So, simply...
[1:20] Let's reset this one to default.
[1:23] I want to reset...
[1:27] These to default.
[1:30] Default.
[1:31] So now, as you can see,
[1:33] where is the visualized props?
[1:38] Yeah.
[1:39] This is usually what we can see,
[1:42] is default settings.
[1:44] These props are representing what luminos are.
[1:47] Are representing what lumen is actually doing now,
[1:51] or it's trying to do.
[1:53] So, what we have is, like,
[1:56] a temporal or a historic frame accumulated together.
[2:01] So, it's not using proper number.
[2:03] So, if we are using one, we can...
[2:07] Give this one as default.
[2:09] So, these historical data,
[2:13] it could be used for GI, for radiosity,
[2:17] or the GI solutions,
[2:20] where it could be used for reflections.
[2:22] And these spheres themselves,
[2:25] we can have higher resolution for each one.
[2:31] Yeah. So, here the...
[2:34] Where is the resolution?
[2:37] Yeah, this one.
[2:38] This is one, for example.
[2:40] As you can see, it's not taking anything into account.
[2:43] And there is another console command,
[2:45] like, that stops the frames or the accumulations.
[2:51] So, you can see what actually the resolution is doing here.
[2:54] So, you can note it in a better way.
[2:57] Let me...
[2:59] I'll search for it.
[3:00] So, it will be easier for you to understand.
[3:06] As you can see now,
[3:08] this is how the...
[3:09] Of course, it will update, but it's not in the same...
[3:13] Time.
[3:15] So, that's what Lumen can see now.
[3:18] For sure, if you are using this in real time,
[3:20] it will not update Lumen.
[3:21] So, it's just for debug.
[3:23] But if we try to increase the resolution,
[3:25] this is two, three, four.
[3:28] As you can see now, higher resolution,
[3:29] it creates cleaner data on these spheres here.
[3:35] So, if you try to be 16, 32, 64,
[3:39] for sure higher number might not introduce better results.
[3:43] By default, but this is what we are looking at.
[3:47] This is one.
[3:49] So, it's very bad resolution.
[3:51] It's not capturing the colors correctly.
[3:53] And these commands by default are not tuned to be...
[3:57] To the best numbers or the...
[4:00] Because it might be different from a project to another.
[4:04] So, if you try to increase this to two,
[4:07] it's already much better.
[4:09] This is three, this is four.
[4:11] Let's give it to 16.
[4:12] So, it's cleaner, it's smoother,
[4:15] and it's having better data.
[4:17] For sure, it still has some like these black spots.
[4:20] But it's not like that for sure.
[4:24] This is too bad.
[4:25] This is 16, for example.
[4:27] And we have also the rigidity, the max rate intensity.
[4:30] Like, this is one.
[4:33] I think default is 40, I believe.
[4:38] Probably 40.
[4:39] So, if you have lower number,
[4:41] it will reduce the amount of the rays added.
[4:46] Or it clamps the amount of rays that are projected.
[4:50] So, you might have less or weaker...
[4:54] Not weaker, but less pride GI.
[4:57] But you might not notice the flickering more in the noise,
[5:01] or the noise in the reflections.
[5:03] So, let's give this to four.
[5:05] This is temporal, I believe.
[5:10] Yeah, I'm not sure...
[5:12] I'm not sure correctly what this one was doing,
[5:14] but might need the updates.
[5:19] Yeah, as you can see.
[5:22] Not sure the default of it was zero or one.
[5:26] Let's keep this to zero.
[5:29] Here, the luminosity and the rigidity,
[5:31] the temporal max frames accumulated by default,
[5:36] it's set to four, eight,
[5:39] it might depend on different projects.
[5:41] So, we can increase it,
[5:43] try high number like 1024.
[5:49] And these props, let's reduce the size of them to one.
[5:54] So, we have smaller props now,
[5:57] and they reflect much more accurate surfaces like these.
[6:02] Or even if we try to disable them.
[6:05] So, this is one.
[6:12] This is...
[6:16] Can you notice that here, probably?
[6:19] This is one.
[6:21] This is 124.
[6:23] So, it's giving more accurate results.
[6:25] And same goes... We'll see that in reflections as well.
[6:28] Here in reflections, max rates, this is zero.
[6:32] So, no raise or max rate is zero.
[6:36] So, we are limiting or calving them to zero.
[6:39] This is four, this is one, this is 100.
[6:42] So, as you can see, higher numbers, it's not clamping,
[6:46] it's giving or pushing the threshold or the maximum of it.
[6:50] So, let's keep it to four max frames accumulated,
[6:53] but for reflections this time,
[6:56] this is one, as you can see, very noisy.
[6:59] This is 1024.
[7:01] This is more accurate.
[7:03] So, this is one, as you can see here.
[7:07] Let's show if you can see it well.
[7:10] And this is 1024.
[7:13] Way softer and much, much better.
[7:17] And for sure, you can have also the surface cache,
[7:21] you can have also the surface cache,
[7:24] card max resolution, this is 1024.
[7:29] Yeah, this is four, for example, this is a max, this is 1024.
[7:34] This might be noticeable in here.
[7:37] Yeah, as you can see, consider to 40 or 4K, 496.
[7:43] And that downsample factor,
[7:47] this is related to GI probably and the small details like this.
[7:54] This is, I think the, yeah, the pixel size of the screen.
[7:59] So, the lower the number, the better the value.
[8:03] You might not sit here on these edges.
[8:06] This is one, yeah, here, it's like, blacked out.
[8:14] It's not adding proper inclusion.
[8:19] And it's not taking into account the space between the objects.
[8:23] So, the lower the number, the better the result at the end.
[8:28] And even our performance is still the same.
[8:33] So, you can increase this to a higher number.
[8:37] You can increase this one as well.
[8:39] You can increase the resolution.
[8:42] So, if we are visualizing the props now, like that,
[8:47] of course, we cannot get rid of that flickering
[8:50] because it's updating in real time.
[8:52] But the thing is, if you are not getting like weird colors or so,
[8:59] this is how it should work because it's not always static.
[9:03] If it's static, so it's not updating or it's not changing in real time.
[9:08] So, that's why we can't see that always.
[9:11] But once you have lower props like these,
[9:15] it will be easier to notice.
[9:18] So, for sure, we can go more in depth into that later on.
[9:25] This is zero.
[9:28] Yeah, so, as you can see here, it's cleaner.
[9:31] Yeah, and we have the specular scale as well.
[9:34] If you want to increase the specularity,
[9:36] if you want to increase the specularity of the scene,
[9:40] this is not correct in terms of PPR.
[9:44] But this is like, for example, this is more close to a post-tracing result.
[9:51] This is not just like the blue moon look.
[9:56] It's more closer to post-tracing.
[9:59] But it's too bright in here, so you have to be careful of it
[10:03] because you can see the differences here.
[10:05] So, you could push it, but it's not too much.
[10:08] And there is another one.
[10:10] It's called the Lumen Reflections and Contrast.
[10:16] Yeah, R, the Lumen Reflections and Contrast.
[10:18] This is zero. It's not having anything.
[10:20] This can reduce it just slightly if you want less reflections overall.
[10:26] But for sure, this is not accurate for PPL or from physically based.



---

## Captured Frames

- [0:27] tutorials/frames/lumen-in-unreal-engine-a-closer-look/frame_000.jpg
- [1:44] tutorials/frames/lumen-in-unreal-engine-a-closer-look/frame_001.jpg
- [3:28] tutorials/frames/lumen-in-unreal-engine-a-closer-look/frame_002.jpg
- [4:33] tutorials/frames/lumen-in-unreal-engine-a-closer-look/frame_003.jpg
- [5:43] tutorials/frames/lumen-in-unreal-engine-a-closer-look/frame_004.jpg
- [7:10] tutorials/frames/lumen-in-unreal-engine-a-closer-look/frame_005.jpg
- [7:29] tutorials/frames/lumen-in-unreal-engine-a-closer-look/frame_006.jpg
- [8:06] tutorials/frames/lumen-in-unreal-engine-a-closer-look/frame_007.jpg
- [9:34] tutorials/frames/lumen-in-unreal-engine-a-closer-look/frame_008.jpg
- [10:16] tutorials/frames/lumen-in-unreal-engine-a-closer-look/frame_009.jpg

---

## Structured Notes

### Core Technique
Curing Lumen GI and reflection flicker/noise by tuning `LumenScene.Radiosity`, `Lumen.Reflections` and `LumenScene.SurfaceCache` console variables in the **Console Variables Editor** panel — using `r.LumenScene.Radiosity.VisualizeProbes` as a live debug view of what Lumen is actually resolving — instead of reaching for Final Gather Quality.

### Summary
A ~10-minute walkthrough of Lumen's internals inside a sci-fi hallway scene (`SciFiHallway` / `MainMap`, 363 actors). Karim shows the flickering problem, then explicitly declines the usual fix of raising Final Gather Quality, and instead drives twelve session-scoped cvars from the Console Variables Editor docked beside Details/World Settings [frame_001]. Enabling radiosity probe visualization renders Lumen's temporally-accumulated hemisphere probes as coloured spheres in the viewport, which makes each cvar's effect directly observable rather than guessed — probe resolution, ray-intensity clamping, temporal accumulation windows, surface-cache card resolution and screen-probe downsampling are each pushed to a bad value and then a good one. The end state (`HemisphereProbeResolution 128`, both temporal windows at `4096`, `DownsampleFactor 1`, `CardMaxResolution 4096`) removes the flicker at broadly comparable frame time [frame_009].

### Key Steps
1. **Reproduce the problem** — visible GI flicker in the hallway at default settings; frame time noted as the baseline to protect [frame_000, transcript 0:27]. He states plainly he is *not* going to fix it by raising Final Gather Quality [transcript 0:36].
2. **Open the Console Variables Editor** — a dockable panel tabbed alongside `Details` / `World Partition` / `World Settings`; entries are added with **+ Console Variable**, each row showing Name / Value / Source, where `Source` reads `Session` for a runtime change and `Constructor` for an untouched default [frame_001].
3. **Turn on probe visualization** — `r.LumenScene.Radiosity.VisualizeProbes 1` draws the radiosity hemisphere probes as spheres; `r.LumenScene.Radiosity.VisualizeProbeRadius` sizes them (5 for an overview, 1 to read fine surface detail) [frame_001, frame_002]. These are debug-only and are returned to `0` / `1` before judging the final image [frame_009].
4. **Probe resolution** — `r.LumenScene.Radiosity.HemisphereProbeResolution` stepped 1 → 2 → 3 → 4 → 16 → 128. At 1 the probes carry almost no usable colour; each step yields visibly cleaner per-probe radiance [frame_002, transcript 2:38–4:15]. Final value 128 [frame_009].
5. **Clamp GI ray intensity** — `r.LumenScene.Radiosity.MaxRayIntensity` (he cites the default as ~40) clamps the contribution of individual bright rays. Lowering it to `4.0` trades a little GI brightness for markedly less fireflying and flicker [frame_001, transcript 4:27–5:03].
6. **GI temporal window** — `r.LumenScene.Radiosity.Temporal.MaxFramesAccumulated`, described as defaulting around 4–8, raised through 64 → 1024 → 4096. This is the single biggest lever on flicker, at the cost of slower response to changing light [frame_001 (64), frame_007 (1024), frame_009 (4096)].
7. **Reflection temporal window** — the same idea on the reflection path: `r.Lumen.Reflections.Temporal.MaxFramesAccumulated` at 1 is very noisy, at 1024/4096 it is dramatically softer and more stable [frame_007, frame_009, transcript 6:56–7:13]. `r.Lumen.Reflections.MaxRayIntensity` clamps reflection rays the same way (set to 4).
8. **Surface cache resolution** — `r.LumenScene.SurfaceCache.CardMaxResolution` moved 4 → 1024 → 4096; low values lose detail in the cached surface representation that both GI and reflections read from [frame_007, frame_009].
9. **Screen-probe downsampling** — `r.Lumen.ScreenProbeGather.DownsampleFactor` is the one that inverts: **lower is better.** At 64 the contact areas and edges go black and the spacing between objects stops being resolved (missing occlusion); at 1 the edges resolve correctly, and he notes performance stayed effectively unchanged [frame_007 (64, degraded), frame_009 (1, final), transcript 7:43–8:33].
10. **Two optional look controls** — `r.Lumen.Reflections.SpecularScale` pushes specular beyond physically-based values toward a path-traced feel (he warns it blows out quickly and is not PBR-correct); `r.Lumen.Reflections.Contrast` reduces overall reflection strength slightly, also not physically correct [frame_008, frame_009, transcript 9:31–10:26].
11. **Disable the debug view** — set `VisualizeProbes` back to `0` before evaluating; while probes are drawn they update in real time and will always appear to flicker, which is expected and not the scene's problem [transcript 8:42–9:18].

### UE Systems / Blueprints / Settings
The full cvar set as it appears in the Console Variables Editor [frame_001, frame_002, frame_007, frame_009]. "Final" is the tuned end-state read directly off the panel in [frame_009].

| # | Console Variable | Role | Final |
|---|---|---|---|
| 1 | `r.LumenScene.Radiosity.HemisphereProbeResolution` | Angular resolution of each radiosity hemisphere probe; low = colours not captured | `128` |
| 2 | `r.LumenScene.Radiosity.MaxRayIntensity` | Clamps single-ray GI contribution; lower = less firefly/flicker, slightly dimmer GI | `4.0` |
| 3 | `r.LumenScene.Radiosity.Temporal` | Master toggle for radiosity temporal accumulation | `1` |
| 4 | `r.LumenScene.Radiosity.Temporal.MaxFramesAccumulated` | GI temporal history length — the primary anti-flicker lever | `4096` |
| 5 | `r.LumenScene.Radiosity.VisualizeProbes` | **Debug only** — draws radiosity probes as spheres | `0` |
| 6 | `r.LumenScene.Radiosity.VisualizeProbeRadius` | **Debug only** — probe sphere size; 1 reads fine detail, 5 for overview | `1` |
| 7 | `r.Lumen.Reflections.Temporal.MaxFramesAccumulated` | Reflection temporal history length | `4096.0` |
| 8 | `r.Lumen.Reflections.MaxRayIntensity` | Clamps single-ray reflection contribution | `4` |
| 9 | `r.Lumen.Reflections.SpecularScale` | Specular multiplier; >1 approaches a path-traced look but breaks PBR | `1.0` |
| 10 | `r.LumenScene.SurfaceCache.CardMaxResolution` | Surface cache card resolution feeding GI + reflections | `4096` |
| 11 | `r.Lumen.ScreenProbeGather.DownsampleFactor` | Screen-probe spacing — **inverted: lower is better**; high values black out edges/occlusion | `1` |
| 12 | `r.LumenScene.Radiosity.Temporal.FixedJitterIndex` | Pins the temporal jitter index; `-1` = normal rotating jitter. He is openly unsure of this one | `-1` |

Also demonstrated but not left in the list: `r.Lumen.Reflections.Contrast`, typed into the **+ Console Variable** search and confirmed by autocomplete [frame_009].

**Two directional rules worth remembering:**
- Rows 1, 4, 7, 10 — **higher is better** (more resolution / longer history), paid for in latency to lighting changes.
- Row 11 `DownsampleFactor` — **lower is better**; this is the one that reads backwards against the others.

**Workflow note:** the `Source` column distinguishes `Session` (changed this run) from `Constructor` (still at its built-in default), which is how he tracks what he has actually touched. Setting a row back to its default is done with the revert arrow beside the value, not by retyping a remembered number [frame_001].

> **Transcript reliability — read the frames, not the narration.** The speaker works almost entirely in pointing language ("this one", "here", "let's give it to 16") and never says a full cvar name aloud, so *every* variable name above comes from the Console Variables Editor panel in the frames. Whisper additionally produced fluent, plausible mishearings that no confidence check would flag: **"rigidity" → Radiosity**, **"max rate intensity" → MaxRayIntensity**, **"post-tracing" → path tracing**, **"PPR"/"PPL" → PBR**, **"124" → 1024**, **"496" → 4096**, **"calving" → clamping**, **"inclusion" → occlusion**, **"less pride GI" → less bright GI**. Do not quote numbers or names from this file's Raw Data section without checking them against a frame.

### Difficulty
Advanced

### UE Version
Not stated in the video. The editor UI places it at **UE 5.5 or later** — the Content Browser shows the integrated **Fab** button (Fab replaced Quixel Bridge/Marketplace in 5.5) alongside Zen Server and Revision Control status widgets [frame_001]. Treat 5.5+ as an inferred lower bound, not a stated version.

### Tags
lumen, reflections, radiosity, surface-cache, console-variables, console-commands, global-illumination, flickering, noise, debugging, rendering, lighting, advanced, youtube, ue5

---

## Related Entries
- [This One Setting Will Fix Lumen Noise in Unreal Engine 5](this-one-setting-will-fix-lumen-noise-in-unreal-engine-5.md) — **same author, same fix, 28-second version.** That entry recommends `r.LumenScene.Radiosity.Temporal.MaxFramesAccumulated 128` and carries a note that Whisper mistranscribed the command and it was confirmed externally. This tutorial is the in-depth counterpart and **confirms that cvar name first-party from the Console Variables Editor** [frame_001], along with the eleven other cvars around it.
- [How I Use Lumen in AAA Projects | Unreal Engine 5](how-i-use-lumen-in-aaa-projects-unreal-engine-5.md) — same author; the Post Process Volume-level knobs (Final Gather Quality, Ray Lighting Mode) that this tutorial deliberately bypasses in favour of cvars.
- [How to Get Clean Lumen Lighting in Unreal Engine 5](how-to-get-clean-lumen-lighting-in-unreal-engine-5.md) — the *per-light* answer to flicker (Ray Trace Samples Per Pixel) versus this tutorial's *global cvar* answer; also argues against lowering Final Gather Quality.
- [Lumen Explained - IMPORTANT Tips for UE5](lumen-explained---important-tips-for-ue5.md) — surface cache internals and its mesh-splitting constraint; context for `SurfaceCache.CardMaxResolution` here.
- [Things to Know About Lumen (Unreal Engine 5)](things-to-know-about-lumen-unreal-engine-5.md) — the Final Gather Quality / Diffuse Color Boost approach this tutorial positions itself against.
