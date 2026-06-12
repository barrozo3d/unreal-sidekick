---
title: Double Your Framerate in UE5 for FREE, Sort Of. - Nvidia DLSS 3.0
source: YouTube
url: https://www.youtube.com/watch?v=RaY_FDaydoQ
author: William Faucher
ingested: 2026-06-12
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/double-your-framerate-in-ue5-for-free-sort-of---nvidia-dlss-30/
frame_count: 0
---

# Double Your Framerate in UE5 for FREE, Sort Of. - Nvidia DLSS 3.0

**Source:** [YouTube](https://www.youtube.com/watch?v=RaY_FDaydoQ)
**Author:** William Faucher
**Duration:** 13m32s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Last year, Nvidia released DLSS 3.0 that included a feature known as frame generation,  which boasted the ability to double your frame rates, and it largely delivered on its promise  with a few substantial caveats, of which we'll get into in this video.  DLSS 3.0 is now available for Unreal Engine 5.2, but should you turn it on?  Can you even benefit from it? What's it even do? Let's jump right in.  Now, Fold is closer and Nvidia did send me an RTX 4080 for testing frame generation  because the 40-series GPU was needed for reasons we'll get into soon.  No money changed hand, and Nvidia has no input on this video's production.


### Important DLSS 3.0 Distinction [0:36]
**Transcript:** Okay, so I need to keep you all in the loop because DLSS 3.0 has a  super confusing naming convention. Think of DLSS 3.0 as a umbrella,  a kind of container for a variety of features and plugins all working together.  It includes the DLSS super-resolution stuff, but also frame generation,  reflex, and IS, and streamline. I kind of wish they made that clearer,  but it is what it is now, you know. So in this video, when I say DLSS 3.0,  I am referring to the global container features, and when I say DLSS,  I'm referring to the AI upscaling tech. The two important features I'll be talking about, though,  are DLSS and frame generation, or frame gen for short. So let's take a look at how it runs,


### How does it perform? [1:20]
**Transcript:** and how easy it is to use. I'm going to make sure I'm running my level in plain editor mode  here, and you'll see I have this overlay, which is set up thanks to the level blueprint you can  find in the DLSS 3.0 sample project you'll get when you download it. Okay, so here we are in the  city level. You'll see we're running it about 30 or so frames per second. It's definitely playable,  but if I go ahead and turn on frame generation right here, pay attention to what happens to my  frame rate. Now we're well over 60 FPS, and everything is substantially smoother. At virtually no  real cost in terms of graphical quality. Now there are a few odd things happening here,  especially on thin objects right here. You'll notice pay attention to what happens with the  lamp post here. We get a little bit of ghosting, a bit of oddness, but I don't think I would  immediately notice it unless I was really paying attention to it. Would I use this for pre-rendered  footage? Probably not, as we tend to pixel-peep those shots a whole lot more, but for  interactive stuff, it looks pretty great. Doubling our frame rate with the click of a button  is pretty insane. So moving on to the value of the ancient...


### TSR vs. DLSS, what's the difference? [3:46]
**Transcript:** probably heard of TSR, or temporal super-resolution, which is Epic's own upscaler that runs by default  in Unreal Engine 5. The key word here is upscaler or upsampler, call it what you want. It essentially  runs Unreal at a lower native resolution, giving a performance boost, higher frame rate, and then  TSR works as magic and artificially upreses everything while preserving detail. That is what  allowed Ub5 to run Lumen and Nanite so efficiently, because at a native resolution, it puts a lot of  strain on your GPU. And video DLSS does a lot of the same by rendering the frame at a lower-based  screen percentage and using machine learning to upres things back up to your desired resolution.  Simply put, these are two different kinds of upscalers with different pros and cons.


### Frame Generation [4:38]
**Transcript:** Now, frame generation however, which is included in DLSS 3.0 is a different beast entirely,  that does something totally different. It uses machine learning to analyze sequential frames and  motion data using optical flow hardware and adds new frames in between the ones your GPU has already  rendered, potentially doubling your frame rate without any upscaling. It's making an educated  guess on what the next frame should look like based on the previous frame and motion vectors  provided by the engine. The cool thing is that frame generation does not need DLSS running to work.  If you want to stick with Unreal default TSR and use frame gen, you can. Any upscaler combined  with frame gen means that Unreal theoretically only need to render 1.8 of the total rendered pixels.  So why should you care? Vastly superior performance. This could be the key to real-time path tracing,  a lot sooner than expected. If we can render a fully passed rate frame at very low resolution,  say 540p at 12 to 15 FPS, UTSR or DLSS to up-rethered to 1080p, and then you'd frame gen to double the  frame rate up to 24 to 30 FPS, we've essentially got real-time path tracing, which could be an absolute  game change...


### Caveats [6:08]
**Transcript:** but DLSS works fine and older GPUs though. Now I know what you're thinking, and video is  screwing over a doughnut with older cards just so that they can sell more of the newer cards.  It's not that. It's because frame gen is dependent on the optical flow hardware found in the  newer cards. It's not some conspiracy to sell newer GPUs. That hardware is present on the 30 and  20-series cards. It's just physically much slower. So even if it is technically possible to run  frame gen on a 30 or 20-series card with a software unlock, the game will be negligible.  In order for frame gen to really do its thing, it needs a certain frame rate to be usable,  something roughly above 30 FPS to begin with. Otherwise the generated frame need to do a lot of  guesswork, which is kind of a bummer because low FPS is when you would need frame gen the most.  So DLSS 3.0 still needs a bit of optimizing for it to be viable on older GPUs.  Now you're probably wondering how can we use this? How is frame gen actually used on a day-to-day


### How to use Frame Generation in Unreal? [7:07]
**Transcript:** basis? Frame gen runs in Unreal in play in editor mode in its own window or running as a packaged  executable. Unfortunately it doesn't work in the Unreal viewport, so if you were hoping for  a viewport upgrade, this is not it. I try getting frame generation to work with the movie  render queue for offline rendering, but it did not seem to have any effect. Unfortunately,  this means that frame gen is mostly for interactive content like games,  archviz, etc. For those of you in virtual production, I did test DLSS 3.0 in end display.  DLSS works, but frame gen seemed to have flickering issues with tells me it had generating frames,  but they all come out black. It could have to do with the fact that I am using a pre-release build  of DLSS 3.0 or end display is just not supported at the moment, or I'm just an idiot and I set it up wrong.  It's very likely, but if any of you manage to get it up and working with the movie render queue  or end display, let me know in the comments below I will stand corrected, and I'll update the  information in the pinned comment. In video, if you're listening, if you manage to get frame gen working  in end display, VR and movie render queue, you have a ...


### Movie Render Queue [9:03]
**Transcript:** by adding the DLSS tab right here and shooting the desired quality settings. DLAA is rendering  full native resolution, so 100% screen percentage, quality is 66.67%, balanced is 58%, performance is  50%, and ultra performance is 33.33%. I did render some frames using the movie render queue for  pixel peeping, and here are my results. Here we have the shot with DLAA versus Unreal TSR. This  render comparison would pretty interesting to me, because while the result look very different,  I can't really tell which one is better. I'm leaning towards the DLAA render looking better,  simply due to the way it rendered the water, and also because the trees pop a bit more,  while preserving the shapes of the castle up here. TSR, however, is quite a bit sharper,  but you can configure the sharpness of any DLAA or DLSS render with the following  console variable. This is not some post processing sharpening, it's actually sharpening the result  itself at render time. One that comes to rendering the best possible top quality renders,  the best way to do that is still, by turning off AA entirely and using 16 plus temporal samples  in the movie render queue. You can find a settings I used in my re...


### Download and Install DLSS 3.0 [10:31]
**Transcript:** here at the link below, and include our installation instruction in the PDF.  Really, it's just about copying over the folders to your engine directory, and enabling these plugins  in your Unreal project of choice right here. There is even a sample project you can run to test out  before adding DLSS 3.0 to your own project. In the project settings under the Nvidia tabs here,  be sure the relevant checkboxes are ticked, and you'll be ready to go. One major issue I have  with this is that it's really hard to know if DLSS or Framjain is actually on and working,  because there's no visual indication that it is running, nor can I know which quality setting is  being used in the viewport. When I run my level in plain editor mode here, if I didn't have the  Nvidia UI, which I have set up thanks to the example DLSS project provided by Nvidia, I would have  no idea what is happening. For normal viewport use, there used to be a menu window pop-up back  in Unreal Engine 4.27, which doesn't exist anymore. My understanding, and I could be wrong,  is that Epic is preventing developers from adding their own custom buttons to unreal UI  shelf to keep it cleaner. Because in their defense, if you en...



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
