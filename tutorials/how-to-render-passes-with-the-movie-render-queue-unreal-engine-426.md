---
title: How to: Render Passes with the Movie Render Queue (Unreal Engine 4.26)
source: YouTube
url: https://www.youtube.com/watch?v=ova8s1H-mUI
author: William Faucher
ingested: 2026-06-23
ue_version: "UE4.26"
tags: [render-passes, mrq, movie-render-queue, z-depth, world-normal, exr, compositing, deferred-rendering]
extraction_status: complete
frames_dir: tutorials/frames/how-to-render-passes-with-the-movie-render-queue-unreal-engine-426/
frame_count: 6
---

# How to: Render Passes with the Movie Render Queue (Unreal Engine 4.26)

**Source:** [YouTube](https://www.youtube.com/watch?v=ova8s1H-mUI)
**Author:** William Faucher
**Duration:** 5m7s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey guys, and welcome to the first installment of Two Minute Tuesdays.  In my last video, I said that you could not render out all of sequencer's render passes  with the movie render queue.  It turns out that was not quite true and I totally stand corrected.  If you haven't seen that video already, you can check it out right here.  Now in this video, I'll be showing you how we can render out all of sequencer's render  passes, but this time with the movie render queue.  Let's put it timer down and let's get started.

**Frame:** tutorials\frames\how-to-render-passes-with-the-movie-render-queue-unreal-engine-426\frame_000.jpg

### Adding Render Passes to MRQ [0:23]
**Transcript:** With the movie render queue open, okay?  I went ahead and I added my sequencer right here with the big render button here.  Let's go into settings and you'll see there isn't, there doesn't seem to be a way to  add render passes like sequencer has, right?  So I'm going to go to setting, there just is no option for render passes.  The way you do it is a little bit hidden.  It's hidden and it's really not intuitive and it's really easy to admit.  If you didn't know any better, you would just think it's not there and that's what I thought  in my previous video.  But I would roll and this is how.  Now in the deferred rendering tab, you're going to want to go ahead and see here where  it says additional post process materials.  You want to hit the little plus.  When the little plus opened up here, click the little arrow here and you need to look  for the pro-frothless material in this case, the scene depth world units.  Now if you didn't know any better, you click on this, everything on material in the project  showed up here, you really have to know what to look for.  This is really bad user interface design on Epic part.  Why they couldn't make it the same as sequencer?  I'll never know.  Now, let's go ahead and search here.  Search as it's for scene depths.  Scene depth world units.  Click that, make sure you hit enable.  Hit accept and you're ready for render.  You're seeing depth world units pass.  So in your Z-Devs pass, if you want to add another render path, you just go ahead and

**Frame:** tutorials\frames\how-to-render-passes-with-the-movie-render-queue-unreal-engine-426\frame_001.jpg

### Adding additional passes [1:39]
**Transcript:** do the same thing.  You just add another one.  So add element.  I'm going to search for, let's see what sequencer has here.  Sequencer has, let's say I want world normal.  Okay?  I'm going to go ahead and search for in a none tab here, world normal.  So we render queue world normal.  Click that, hit enable and that is the symbol of that.  That is how you go ahead and add all the render passes that sequencer has with the movie

**Frame:** tutorials\frames\how-to-render-passes-with-the-movie-render-queue-unreal-engine-426\frame_002.jpg

### Available Render Passes List [2:02]
**Transcript:** render queue, with the added benefit of having all the multi sampling.  Now one thing I do stand by, however, is the quality of the Z-Devs pass.  So in this case, the scene depth world units.  So this is a claim I made in my live video.  I absolutely stand by the fact that this is unusable for production.  It's not very good.  It's something and we'll see why by jumping into Nuke.  So I'm going to go ahead and hit accept render local and now to this rendering, let's jump  into Nuke and see the result of the Z-Dev path that we get from this, even with multi sampling.

**Frame:** tutorials\frames\how-to-render-passes-with-the-movie-render-queue-unreal-engine-426\frame_003.jpg

### Zdepth/Scene Depth analysis in Nuke (Defocus) [2:38]
**Transcript:** Alright, so now we're Nuke.  I went ahead and brought in the EXR file that we just rendered from Unreal.  So as you can see here, I rendered a scene with no depth of field because I'm going  to be applying the depth of field with the help of the scene depth world units that we  just rendered out.  I have the EXR file right here.  But when I had added the Z-Dev focus node, now what this does is it uses the depth path  that we got that's baked into the EXR layer and de-focuses the scene based on that.  So let's go ahead and I'm going to crank up the value that's something pretty high here  and now it's working.  And you can see it's de-focussed everything and I got to choose the focal point here.  So now the focal point is on the rear pot here.  I'm going to move this focal point and bring it right here to the front pot.  Now I'm going to maybe tone this down a bit.  You can see this is actually pretty cool.  So we have full control over the depth of field in Nuke.  And this is actually quite a useful way to work.  I love having the freedom of controlling the amount of de-focusing and the position of  the de-focusing in post.  It's just a lot easier to work with.  It's a lot faster and this looks pretty good at first glance, right?  So if I move ahead and go to the next frame or something, this actually doesn't look too  bad.  But if we take a closer look, this is where the scene depths from Unreal really begin to  fall apart and that's around the edges.  So you can see here when you go closer, we can see all these artifacts around the edges.  Let's look at the foliage as well.  See if we get all these nasty little artifacts here.  And that is because the scene depths that we get from Unreal is not the edges just look  like garbage.  It's really bad.  It's completely unusable.  This just does not look very good.  So I can't use this in production.  Compers are going to hate you.  This is not very good.  So it's something, but in my opinion, it's not good enough to really be used properly.  So we're able to get all the sequinsered render passes out with multi sampling, but  scene depths, it's not quite there yet.  It's not good enough for vfx work.

**Frame:** tutorials\frames\how-to-render-passes-with-the-movie-render-queue-unreal-engine-426\frame_004.jpg

### Outro and Thanks [4:52]
**Transcript:** And there you have it folks.  So thanks for so much for watching guys.  That concludes my first two minute Tuesday.  I know I've completely blasted past the two minute mark.  But hey, I hope you learned a little something.  If you have, leave a comment down below.  Don't forget to like and subscribe.  It means the world to me.  And I'll see you guys next week.

**Frame:** tutorials\frames\how-to-render-passes-with-the-movie-render-queue-unreal-engine-426\frame_005.jpg


---

## Structured Notes

### Core Technique
Adding render passes (Z-depth, world normal, etc.) to Movie Render Queue in UE4.26. Passes are hidden inside the Deferred Rendering tab under "Additional Post Process Materials" — not obvious like Sequencer's render pass UI. Search by pass name, enable, then output to EXR. Critical caveat: Scene Depth (Z-depth) from UE4 has production-breaking edge artifacts — unusable for post DoF compositing in Nuke/Fusion.

### Summary
5-minute tutorial by William Faucher (correction video) showing that MRQ does support Sequencer's render passes — but the UI hides them in the Deferred Rendering tab → Additional Post Process Materials. You must search by pass name and enable each pass individually. MRQ adds the benefit of multi-sampling over Sequencer's built-in render passes. However, the Z-depth (Scene Depth World Units) pass has severe edge artifacts in UE4 and is not production-usable.

### Key Steps
1. **Open MRQ settings** — Window → Cinematics → Movie Render Queue → Render → click sequence → Unsafe Config → Settings
2. **Access Deferred Rendering tab** — in MRQ settings, click on the Deferred Rendering item in the settings list
3. **Add render pass** — Additional Post Process Materials → click + (plus) → search for pass name:
   - Z-depth: search "scene depth world units" → select → Enable
   - World Normal: search "world normal" → select "render queue world normal" → Enable
   - Repeat for any additional passes (click "Add Element" each time)
4. **Set output to EXR** — Settings → Add Output → EXR Sequence (recommended for multi-pass compositing)
5. **Accept + Render Local**
6. **Verify in Nuke/Fusion** — EXR contains requested render passes as separate channels

### UE Systems / Blueprints / Settings
- **Deferred Rendering tab** — MRQ settings panel; contains "Additional Post Process Materials" where render passes are hidden
- **Additional Post Process Materials** — drop-down + button; search field for pass names; requires knowing the exact post-process material name
- **Scene Depth World Units** — Z-depth render pass; search name: "scene depth world units"; KNOWN ISSUE: edge artifacts around objects make this unusable for production DoF compositing (bleed/fringing at object boundaries); Epic has NOT improved this as of UE4.26
- **World Normal** — surface normal render pass; search name: "render queue world normal"; usable for relighting
- **Multi-sampling advantage** — MRQ render passes get multi-sampling (anti-aliased, higher quality) vs Sequencer's built-in render passes; main reason to use MRQ for render passes
- **EXR output** — required for multi-channel render pass output; passes bake into EXR channels
- **Z-depth artifact issue** — edge pixels around geometry have garbage data; causes halos/bleed when used for Defocus in Nuke; "compers are going to hate you" — not recommended for VFX production work

### Difficulty
Beginner-Intermediate. Straightforward once you know where the hidden "Additional Post Process Materials" field is. Main knowledge gap: pass names are not intuitive and you must search by name.

### UE Version
UE4.26 (MRQ render passes available in UE5 with same Deferred Rendering tab approach; Z-depth quality improved somewhat in UE5)

### Tags
render-passes, mrq, movie-render-queue, z-depth, world-normal, exr, compositing, deferred-rendering

---

## Related Entries
- `how-to-render-cryptomatte-in-unreal-new-in-426.md` — companion: adding Cryptomatte/Object ID passes in MRQ
- `improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn.md` — additional MRQ render quality tips
- `the-2025-guide-to-rendering-in-unreal-engine-5.md` — UE5 rendering guide covering modern MRQ setup
- `why-you-should-be-using-stencil-render-layers---unreal-engine-426.md` — alternative object isolation method
