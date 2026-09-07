---
title: Lumen in Unreal Engine | A Closer Look
source: YouTube
url: https://www.youtube.com/watch?v=2qc7I6bfRBo
author: Karim Yasser
ingested: 2026-09-07
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/lumen-in-unreal-engine-a-closer-look/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# Lumen in Unreal Engine | A Closer Look

**Source:** [YouTube](https://www.youtube.com/watch?v=2qc7I6bfRBo)
**Author:** Karim Yasser
**Duration:** 10m33s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py lumen-in-unreal-engine-a-closer-look <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### UE Systems / Blueprints / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### UE Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Entries
[PENDING EXTRACTION]
