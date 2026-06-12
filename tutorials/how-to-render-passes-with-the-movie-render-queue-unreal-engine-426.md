---
title: How to: Render Passes with the Movie Render Queue (Unreal Engine 4.26)
source: YouTube
url: https://www.youtube.com/watch?v=ova8s1H-mUI
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 4.26"
tags: [rendering, movie-render-queue, mrq, render-passes, z-depth, scene-depth, post-process-materials, nuke, william-faucher, beginner, ue4]
extraction_status: complete
frames_dir: tutorials/frames/how-to-render-passes-with-the-movie-render-queue-unreal-engine-426/
frame_count: 0
---

# How to: Render Passes with the Movie Render Queue (Unreal Engine 4.26)

**Source:** [YouTube](https://www.youtube.com/watch?v=ova8s1H-mUI)
**Author:** William Faucher
**Duration:** 5m7s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey guys, and welcome to the first installment of Two Minute Tuesdays.  In my last video, I said that you could not render out all of sequencer's render passes  with the movie render queue.  It turns out that was not quite true and I totally stand corrected.  If you haven't seen that video already, you can check it out right here.  Now in this video, I'll be showing you how we can render out all of sequencer's render  passes, but this time with the movie render queue.  Let's put it timer down and let's get started.


### Adding Render Passes to MRQ [0:23]
**Transcript:** With the movie render queue open, okay?  I went ahead and I added my sequencer right here with the big render button here.  Let's go into settings and you'll see there isn't, there doesn't seem to be a way to  add render passes like sequencer has, right?  So I'm going to go to setting, there just is no option for render passes.  The way you do it is a little bit hidden.  It's hidden and it's really not intuitive and it's really easy to admit.  If you didn't know any better, you would just think it's not there and that's what I thought  in my previous video.  But I would roll and this is how.  Now in the deferred rendering tab, you're going to want to go ahead and see here where  it says additional post process materials.  You want to hit the little plus.  When the little plus opened up here, click the little arrow here and you need to look  for the pro-frothless material in this case, the scene depth world units.  Now if you didn't know any better, you click on this, everything on material in the project  showed up here, you really have to know what to look for.  This is really bad user interface design on Epic part.  Why they couldn't make it the same as sequencer?  I'll never kno...


### Adding additional passes [1:39]
**Transcript:** do the same thing.  You just add another one.  So add element.  I'm going to search for, let's see what sequencer has here.  Sequencer has, let's say I want world normal.  Okay?  I'm going to go ahead and search for in a none tab here, world normal.  So we render queue world normal.  Click that, hit enable and that is the symbol of that.  That is how you go ahead and add all the render passes that sequencer has with the movie


### Available Render Passes List [2:02]
**Transcript:** render queue, with the added benefit of having all the multi sampling.  Now one thing I do stand by, however, is the quality of the Z-Devs pass.  So in this case, the scene depth world units.  So this is a claim I made in my live video.  I absolutely stand by the fact that this is unusable for production.  It's not very good.  It's something and we'll see why by jumping into Nuke.  So I'm going to go ahead and hit accept render local and now to this rendering, let's jump  into Nuke and see the result of the Z-Dev path that we get from this, even with multi sampling.


### Zdepth/Scene Depth analysis in Nuke (Defocus) [2:38]
**Transcript:** Alright, so now we're Nuke.  I went ahead and brought in the EXR file that we just rendered from Unreal.  So as you can see here, I rendered a scene with no depth of field because I'm going  to be applying the depth of field with the help of the scene depth world units that we  just rendered out.  I have the EXR file right here.  But when I had added the Z-Dev focus node, now what this does is it uses the depth path  that we got that's baked into the EXR layer and de-focuses the scene based on that.  So let's go ahead and I'm going to crank up the value that's something pretty high here  and now it's working.  And you can see it's de-focussed everything and I got to choose the focal point here.  So now the focal point is on the rear pot here.  I'm going to move this focal point and bring it right here to the front pot.  Now I'm going to maybe tone this down a bit.  You can see this is actually pretty cool.  So we have full control over the depth of field in Nuke.  And this is actually quite a useful way to work.  I love having the freedom of controlling the amount of de-focusing and the position of  the de-focusing in post.  It's just a lot easier to work with.  It's a lot faster a...


### Outro and Thanks [4:52]
**Transcript:** And there you have it folks.  So thanks for so much for watching guys.  That concludes my first two minute Tuesday.  I know I've completely blasted past the two minute mark.  But hey, I hope you learned a little something.  If you have, leave a comment down below.  Don't forget to like and subscribe.  It means the world to me.  And I'll see you guys next week.



---

## Structured Notes

### Core Technique
Adding render passes (Z-depth, World Normal, etc.) to MRQ via the hidden Additional Post Process Materials slot in the Deferred Rendering tab — a non-obvious workflow that allows MRQ to output the same render passes as Sequencer, with the added benefit of subsampling quality.

### Summary
5-minute quick tutorial (Two Minute Tuesday format) correcting a claim from MRQ Part 1. Render passes ARE available in MRQ — they're just hidden under "Additional Post Process Materials" in the Deferred Rendering tab. Shows how to add Scene Depth (World Units), World Normal, and any other post-process material pass. Demonstrates result in Nuke for DOF workflow using the Z-depth channel.

### Key Steps

**Add Render Passes to MRQ:**
1. MRQ → job settings → Rendering tab (Deferred Rendering section)
2. Look for **Additional Post Process Materials** → click + button
3. Click the dropdown arrow → search for the render pass material by name
4. Select the pass → check Enable
5. Repeat for each additional pass

**Available Pass Names to Search For:**
| Pass | Material Name |
|------|--------------|
| Z-Depth | `Scene Depth World Units` |
| World Normal | `World Normal` |
| AO | Ambient Occlusion related |
| Motion Vectors | Motion Blur related |

**Warning:** The material browser shows ALL materials in the project — you must know the specific name. No user-friendly "add render pass" button like in Sequencer.

**MRQ vs. Sequencer Passes:**
- MRQ: hidden but works + has subsampling quality
- Sequencer: obvious UI + 32-bit Z-depth but no subsampling

**Z-Depth in Nuke:**
1. Render with Scene Depth World Units pass (multi-layer EXR)
2. In Nuke: bring in EXR → ZDefocus node → use depth channel
3. Focal point control via ZDefocus settings
4. Result: full control over DOF in post (position, amount, bokeh)
5. Caveat: depth edges at motion-blurred areas can be problematic

### UE Systems / Blueprints / Settings

**MRQ Deferred Rendering — Add Post Process Pass:**
```
MRQ Settings > Rendering > Deferred Rendering:
  Additional Post Process Materials:
    + (add) → [dropdown arrow] → search material name
    e.g., "Scene Depth World Units" → Enable ✓
    
Output:
  EXR Sequence → check Multi-Layer ✓
  // All passes baked into one multi-layer EXR per frame
```

### Difficulty
Beginner — short tutorial; assumes basic MRQ knowledge

### UE Version
UE 4.26 (workflow same in UE5)

### Tags
rendering, movie-render-queue, mrq, render-passes, z-depth, scene-depth, post-process-materials, nuke, william-faucher, beginner, ue4

---

## Related Entries
- `tutorials/improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4.md` — MRQ Part 1
- `tutorials/improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn.md` — MRQ Part 2 (Z-depth limitations)
- `tutorials/why-you-should-be-using-stencil-render-layers---unreal-engine-426.md` — Better alternative for compositing
