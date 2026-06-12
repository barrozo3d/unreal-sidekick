---
title: Improve Your Renders With Movie Render Queue PART 2 - FIVE Things You Need To Know (Unreal 4.26)
source: YouTube
url: https://www.youtube.com/watch?v=2U1wP8sJgfU
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 4.26"
tags: [rendering, movie-render-queue, mrq, cryptomatte, object-id, depth-of-field, z-depth, render-presets, render-queue, limitations, william-faucher, intermediate, ue4]
extraction_status: complete
frames_dir: tutorials/frames/improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn/
frame_count: 0
---

# Improve Your Renders With Movie Render Queue PART 2 - FIVE Things You Need To Know (Unreal 4.26)

**Source:** [YouTube](https://www.youtube.com/watch?v=2U1wP8sJgfU)
**Author:** William Faucher
**Duration:** 11m50s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey there and welcome to part two of how to improve your rendered with the movie render queue  So over the past week many of you reached out to me with some issues  You've had and your render weren't working and it's been a real pleasure helping you guys out  So is that any point during this video you have a question?  Don't hesitate to leave a comment down below and I'll get back to you as soon as I thought of the can  So in this video we're gonna be talking about a few hidden tools so quality of life settings  But most importantly, I really want to touch base on a few  Limitation that the movie render queue has now  I'm not saying that you can't use them in production because it is production ready  But it's really good to know about these limitations because they could very well end up blind-signing you at the end of a production  So enough talking let's go


### Limitation / Issue #1 - Object ID Pass When Subsampling [0:38]
**Transcript:** Alright, so one of the big limitations and something you should really be aware of when it comes to using  Movie render queue has to do with the object IDs when using  Sub sampling so anti-aliasing sub sampling so as you can see here  I've got my render setting from the movie render queue  All the rendering is an EXR sequence 16 bit  I've got anti-aliasing to none and I'm gonna set the sample to about 32 alright and  I've got my console variables here in order to get some proper  Sub sampling and proper results. This is what we covered this in a previous video  So we're gonna go ahead and add the object IDs limited tag here alright  So this means that we're gonna be rendering out a object ID pass with some high quality sub sampling now  The issue that you have here is when you use sub sampling the render times are going to increase  Astronomically, so let's go ahead and render this right now and you'll see what I mean. I'm gonna hit render local  And you can see right now already  It's hanging like it tend to hang around the 13 sub samples  I'm just rendering 15 frames here and you can see it just kind of just hangs a lot  It's really slow  Now this is not a this is normal and it h...


### Limitation / Issue #2 - No DoF with Object ID Pass [3:56]
**Transcript:** Cryptomat or object ID pass that we just read her now now  So looking at our object ID pass here. I've got the ferns mask  Right here now let's zoom in a little bit we can see that  With rendering with sub sample we got a nice clean motion blur so the cryptomat or object ID takes motion blur into account  But if you look carefully, you notice is another problem. There's another big problem  Now notice how completely out of focus these ferns are  But take a look at this ferns here look at this mask  Let's zoom in a little bit so you can see more clearly  So if you look carefully, you know if I toggle this you'll see that the object ID pass the mask that we get does not  Actually cover the entire range doesn't that the field is not working now to see more clearly. I'm going to go to this pot here and  Look at this mask here. Look how out of focus the pot is compared to the mask now if I select this  Edge here you'll see  Look at this edge selection compared to the out of focusness of the pot itself look at this mask  I cannot use this this is  Actually unusable. This is useless. So  We can conclude that  The field is not taken into consideration when you render object ID passes motio...


### Limitation / Issue #3 - Lack of 32-bit .EXR Zdepth [6:29]
**Transcript:** So another gripe that I've had with the movie render queue so far after you think it for a week is the lack of 32 bit support  Now as you can see here we have got EXR sequence 16 bit for most cases  This is going to be more than enough especially with the sub sampling  You don't need 32 bit color data, but it we want 32 bit depth  We want a proper 32 bit floating point data because it's just going to give you that much better result now  If you use the sequencer we're going to go to sequencer tab here, right? We're going to go to render this video and  Custom render passes here. You can do  Seen depth world units and this is actually a Z depth Z depth pass if you capture frames in HDR it technically renders it out  At a 32 bit EXR, but  The cover using sequencer you lose the benefit of the sub sampling you don't get the high quality render that the movie render queue offers with sequencer  Sequencer is kind of handicaps in that respect  But it does offer a 32 bit Z depth pass. It's not very good especially around along the edges  So if let's say you've got a character and  Detail behind him the edge of the character in there can be really bad especially when you get motion blur  An...


### Handy Feature #1 - Render Presets [8:23]
**Transcript:** Now one nice little feature that i'm using all the time and that's the little presets button up here  Now you may or may not have seen it already, but i think i should mention it anyway  If you've got you know a lot of stuff set out here especially console variables  You know you got a long list of things that you don't want to have to go find online  Copy paste every single time you know you if you're elaborately set up your your render path and everything your resolution  And you don't want to change it every single time you render a shot you can save a preset  So you can just click on the presets button up here save as preset you choose where you want to save it  Click save and there it is now every single time you want to add a new job  Let's go ahead and let's delete this right here  So let's say i'm going to go let's say i'm going to go ahead and add burn in  PNG sequence and object ID here okay, so i got a very complex thing  I can go ahead click presets save as preset and say preset William  Save and now you can kind of go get  Whatever preset you want every single time without having to re-enter your data. This is not a ground breaking  Trick but it's good to know


### Handy Feature #2 - Render Queue [9:30]
**Transcript:** Now the last thing we're going to talk about and this little trick here is the main reason i made this video to begin with  And this is the neat little tool that i'm going to use all the time  This is going to save me so much time and that feature is well  The render queue okay, I didn't cover this for my first video. I'm covering it now  It should go without saying it says it in name a render queue  So as you can see we've got map one shot one here. I've gone ahead and i've made two other shots  So we're going to go ahead and click the render button here  We're going to add shot two and we're going to add shot three  Now before which sequencer you had to open up the map  Click the button down here  rendered this video  capture movie  wait for it to render then you had to you know open up the next map capture movie  Open up the next map and so on and so forth you had to do this for every single shot  It was an extremely time consuming process  If you wanted to if you had 50 shots to render you were going to be up all night  Opening it up every single map and running them out  but now with the movie render queue  And this should go without saying because it said that in the name ren...


### Outro [11:34]
**Transcript:** So as always I hope this has helped you guys out  If you have any questions whatsoever  Don't hesitate to leave a comment down below  I'll get back to you as soon as I can  Don't forget to like and subscribe and I'll see you guys next week



---

## Structured Notes

### Core Technique
MRQ Part 2 — three production-critical limitations of MRQ's Object ID/Cryptomatte and Z-depth passes (slow sub-sampling, no DOF support, no 32-bit depth), plus two powerful productivity features (render presets and batch render queue).

### Summary
11-minute follow-up to MRQ Part 1. Covers hard-won production lessons: Object ID passes are extremely slow with subsampling AND don't support depth of field (making the masks nearly unusable for DOF compositing). Z-depth is only 16-bit. On the productivity side: render presets save your full MRQ config for reuse, and the queue lets you batch all your shots to render overnight unattended.

### Key Steps

**Limitation 1: Object ID Pass + Subsampling = Very Slow**
- Object ID pass with AA=None + high spatial samples causes extreme render time (hangs at ~13 sub-samples per frame)
- Each sub-sample re-renders the Object ID pass → exponential time increase
- Workaround: render Object ID pass without subsampling (separate render pass at lower quality for masking only)

**Limitation 2: Object ID / Cryptomatte = No DOF**
- Object ID mask does NOT account for depth of field
- Out-of-focus objects still get a hard-edged mask → impossible to use for DOF blending in comp
- Resolution: use **Stencil Render Layers** instead (supports DOF natively — see stencil layers tutorial)

**Limitation 3: No 32-bit Z-Depth from MRQ**
- MRQ only outputs 16-bit EXR
- Z-depth (Scene Depth World Units) is 16-bit → insufficient precision for clean DOF in Nuke
- Sequencer can output 32-bit depth BUT loses subsampling quality
- No perfect solution in UE4.26 — a production tradeoff

**Productivity Feature 1: Render Presets**
1. Set up your full MRQ config (output paths, AA settings, console vars, render passes, resolution)
2. Click the Presets button (top right of MRQ window)
3. Save as Preset → name it
4. On any new project: Presets → load preset → entire config restores instantly

**Productivity Feature 2: Batch Render Queue**
1. Open MRQ
2. Click the + Render button → add Shot 1 sequence
3. Click + Render button again → add Shot 2
4. Repeat for all shots in production
5. Hit Render Local → renders all shots in sequence, unattended
6. Before MRQ: had to open each map manually, capture movie, wait, repeat → overnight impossible
7. Now: queue 50 shots, go home, come back to finished renders

### UE Systems / Blueprints / Settings

**Object ID / Cryptomatte Pass Caveats:**
```
// Object ID with subsampling = VERY SLOW
// Object ID does NOT support Depth of Field in masks
// Z-Depth (Scene Depth World Units) = 16-bit only from MRQ

// Workaround for DOF-accurate masks: use Stencil Render Layers instead
```

**Render Presets Location:**
- MRQ window → Presets button (top right) → Save as Preset / Load Preset

### Difficulty
Intermediate — assumes MRQ Part 1 knowledge; covers production gotchas

### UE Version
UE 4.26 (limitations partly resolved in later versions; core concepts still apply)

### Tags
rendering, movie-render-queue, mrq, cryptomatte, object-id, depth-of-field, z-depth, render-presets, render-queue, limitations, william-faucher, intermediate, ue4

---

## Related Entries
- `tutorials/improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4.md` — MRQ Part 1
- `tutorials/why-you-should-be-using-stencil-render-layers---unreal-engine-426.md` — Stencil Layers (fix for DOF masking)
- `tutorials/how-to-render-cryptomatte-in-unreal-new-in-426.md` — Cryptomatte setup
