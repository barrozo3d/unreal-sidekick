---
title: Pose Library ADDITIVE MODE: Layer Animation Poses in Unreal Engine
source: YouTube
url: https://www.youtube.com/watch?v=YSrYqx19_Y0
author: Unreal Engine
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/pose-library-additive-mode-layer-animation-poses-in-unreal-engine/
frame_count: 4
---

# Pose Library ADDITIVE MODE: Layer Animation Poses in Unreal Engine

**Source:** [YouTube](https://www.youtube.com/watch?v=YSrYqx19_Y0)
**Author:** Unreal Engine
**Duration:** 8m43s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** In this video, I'm going to show you how to use the Pose Library tool to not only apply poses or blend between them, but also use the new additive mode, and I'll also show you how to use it as more or less a selection set button. Another great set of tools you have access to is the Pose Library. So when you're in animation mode, if you go up to poses and hit this button, it will pull up a little window for controlling poses. Now you can go ahead and dock this somewhere if you'd like, and what it will allow you to do is save and refer back to different preset poses for your selected rig. So what I can do is I can grab, for example, all of the right hand bone controls. So if I come over here to my anim outliner, I can grab all of these, like, right meta, pinky, all the different hand controls. So I'll just shift click, all of those different hand controls, they're all selected. And I can save this particular pose as a fist. So with all that selected, I'll go up here to my pose. I'll say create pose, and I'll call this fist underscore R. Great asset. I can redo the thumbnail if I don't like the frame that has got here. I can just say capture thumbnail, and that'll give me a new picture of that fist. It does like that. And I can just kind of scrub through here. And since this is already animated for us, we can pretty much just go around and say, all right, that looks like a pretty cool pose. That looks like a nice grip pose. So I'll save that, and I'll call that grip R, great asset. And I can go again, go in here, and adjust the thumbnail, if I want to get a better photo. And I can basically just save different hand poses throughout the animation. Here, I'll do one more. This is a really nice, like, spread kind of blade pose. So I'll just come in here and do one more create pose, and I'll just say open spread right or something. And now I've saved three different hand poses that I can easily come back and refer to. So if I just scrub forward over here to where I have no keyframe data, watch what happens. I can double click on fist R. And it will set that pose. Now, if I have auto key turned on, that might also set keys. If I don't have auto key turned on, then I need to actually make sure I just turn on the key button. So by double clicking it actually sets a key on these controls. I can also just double click on the grip. I can double click on open spread, and I can easily put in these different hand poses. But what's really cool is that you don't have to just double click them. You can also select them, and you can use this little slider to blend from the current position into a little bit more of a fist, for example. And kind of blend into a fist, just like that. I can sort of figure out where I want to be. Maybe I want to have a little bit more of this grip integrated in and I can make more of like a claw hand like this. But the thing you'll notice is the default behavior is when you start with say the open spread, and I go towards the fist, it is going to get rid of open spread and move towards fist. You can only kind of go from a to B. But let's say you have maybe you want to do a fist, but you just wish that fist was more of a fist. You can actually now hit this little additive button, and it will basically do the math and look for the delta between a default hand position. And whatever it needed to do to get to the fist, you can continue to add those transformations on top of whatever current pose you have. So additive mode, if I use the slider, will continue to add the fist change from default on top of my existing animation. And so at this point, I don't really want to double click anymore. I want to just click and drag. So if I say, all right, I've got a fist, but I want more fist. I can start to click and drag, and it will basically apply more of the same data that it used to get here on top of what's already here. This is a really easy way to like break stuff because you can just kind of push stuff through itself, like that, which is why it's also nice to be able to just say, hey, take off additive, go back and repaste the pose. But let me show you how this can be useful. If I say, hey, you know what, instead of blending from my open spread and blending into a fist, I start to lose the spread and it fully becomes a fist. Instead of doing that, I could just say additive and I can say, you know what, let's just add a little bit of the fist, which is going to add some curl to my current position. So by blending, you can see that I am getting a fist, but it's not like overwriting the original data. It's adding the fist elements to my current pose. It's a subtle difference, but it's an important difference. And so if I had, for example, the grip pose applied. So I have this grip pose. If I go to the open spread and I start to blend that in, it's going to go out of this cloth pose and just become a really relaxed spread. But if I say, hey, let's just add in some of the spread to my cloth pose, then what I'm going to get is it's going to sort of adjust where the fingers are. And you can see I'm getting that that's blade hand motion, but it's not removing the actual grippy part of this pose. Now, whether that's actually a very good pose, debatable. But the additive mode is new and that's really, really powerful. It gives you the ability to start layering on different assets of your poses and combining things into new and exciting ways. We also have mirror settings here, which will allow you to mirror across, you know, right hand to left hand. But in order to do that, you have to tell the mirror table over here, the settings, sort of what the naming convention is for the bone. So it knows what to switch for. But I want to show you how this also applies to the face. So it's all very similar. This entire system works across the whole body. I typically use it for hands all the time. But if you want to do stuff with the face, you can very easily do that as well. So if I take some of these eye controls, grab whatever point here I'm using, you do the mouth, the eyes, whatever. If I just grab these four that one, I say, hey, capture, you know, create this pose and I'll just call this open eyes. There you go. So let's say I change this and I make something similar to a blink control or a blink pose. It's not going to be perfect because I'm going really quickly. But let's just say that these, these and that other yellow one there, these make up my blink. So I'll go ahead and say, blink. Create asset. Typically, I actually like to do this for like both sides left and right. And then it's based on selection. So if I have nothing selected and I just double click on open eyes, nothing happens. But if I select those specific controls and I have them selected here, when I double click open eyes, that's how it will apply them. And so personally, I like to do the entire face all at once because then I can very easily just grab like the left of the right side with these different selection sets. Something like this. And then when I double click blink, I just get the one side based on my selection. Or I can grab the whole face and do it to everything. But now I can take this blink and I sort of blend into the blink and you'll see that it stops at a value of one. But if I say, hey, go additive, I can actually now use it as an overshoot and I can push additional pressure into those eyelids. In this case, I don't need to. Doesn't look very good. But that's what that's what that will do. The other thing that the tool allow you to do is instead of having to grab stuff over here on the right, you can also just say, hey, I want to grab all of the hand controls over here. I have these poses set up. I can just say, hey, grab the fist select controls. And it'll easily just grab all the relevant controls that I was using to work with that pose. So same thing with the eyes. If I'm like, oh, I need to grab my eye poses, open eyes, select controls, pace pose, boom, done. I'm not looking for quite as close. I can, you know, blend something in between and we're going to go select pose done. And so that's the post library in a nutshell. The great thing is because we have this whole sequence of animation data, you can go through all the different shots and just capture different hand and face poses that you like and build out a library without having to actually sit down and pose it yourself. Because in a studio environment, that's the magic of a pose library. You've got all these different people making all these great poses and sharing them as resources to get you the first chunk of the way there. And then of course you'll make your own adjustments and dial things in for your specific shot. But to get hands and faces and, you know, different body parts posed out to be close to what you want. This is a huge time saver. So definitely make sure you don't neglect this tool. It's great.

**Frame:** tutorials\frames\pose-library-additive-mode-layer-animation-poses-in-unreal-engine\frame_000.jpg


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
