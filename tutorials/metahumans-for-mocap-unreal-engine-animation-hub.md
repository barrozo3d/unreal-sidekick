---
title: MetaHumans for Mocap | Unreal Engine Animation Hub
source: YouTube
url: https://www.youtube.com/watch?v=myxrzJiLc6I
author: Unreal Engine
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/metahumans-for-mocap-unreal-engine-animation-hub/
frame_count: 4
---

# MetaHumans for Mocap | Unreal Engine Animation Hub

**Source:** [YouTube](https://www.youtube.com/watch?v=myxrzJiLc6I)
**Author:** Unreal Engine
**Duration:** 6m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome to Animation Hub. Today we're going to be looking at how to set up a meta-human for MoCAP manager. So we can't just use them straight out the box. We do need to make a new version of them basically. It needs to be inheriting from their Capture Character class. So I've got my meta-human here and let's just open that up. As you can see we've got the various components and so we're going to create a new blueprint. We're going to make it of Capture Character. There we go. You can call this what you want but I quite like Capture Character MH character. So I want just copying the original name. So I'm going to open these both up. We're going to transfer some assets between them. So let's go full screen. First things first, if we get hold of the body and we copy paste or you can shift the right mouse button. Let's go and paste that onto the Skeletal Mesh asset top slot there. So we've got our arms and legs in. Next let's go and get the rest of the Skeletal Mesh and the groom. So let's select these controls C and then let's paste these over. And so there we go. So we've basically copied that blueprint but it's of a different inherited class. It's parent class is different I should say. So let's close these both down and then in MoCat Manager let's create a new character. Let's call it for now. Capture because that's going to be the data that we the underlying Skeletal data that we're going to use and then MH01. That's going to be the name. The source is going to be our Catery Skeletal and we've already got this set up. And I'm going to in the character class, I'm going to choose the one the class that we just created. And then character mesh you're going to want to add the body for that character. So character 01 body mesh and then create the character asset and then we can spawn it. So as you can see we've already got some anime already had some animation coming in and that's mapped but you will notice I'm sure that the short city shirt isn't lining up. It isn't is an anime. Now we can fix this temporarily by going to the character section on the asset and just toggling this but that's pretty annoying to do every time. And this is something we can fix on the construction. So if I just edit this class, go to the construction script and off of construction, let's just set the leader pose component. And we're going to use, it's only the body and the shorts that's the issue. The face doesn't need this because it gets its animation from a different source which we're going to look into in a sec. So there we go. If you had a meta human with more components than this then you would just build one of these for each mesh. And what we're going to want to do is set it basically say is this mesh, this shorts and t-shirt has a new leader which is the body and we're going to want to tick these two. And what this is doing is basically saying all of your animation is inherited from this component. Hit compile and save. And then just to prove that this is going to work every time we spawn this character, let's just delete these and spawn it again. So it was that one and hit spawn. That's what you can see that's worked great. So, but what about face? Let's sort face out. So we can use webcam for this. So if I go over to the live link tab and add source, go to meta human video. This is available in the meta human live link again. And it can detect our webcam and I quite like the default settings so I'm just going to hit connect. First thing you're going to want to do is go in and disable head orientation, translation and stabilization. The reason being is that we're already getting the head orientation, translation and stabilization off of the capture data. If we had these on, we would get double transforms on the neck which are pretty wacky, pretty fun, but not really what we need. So in order to apply this to the meta human, we do need to combine these sources which is what we're going to use the virtual live link subject for. So we're just going to go to add source again, add a virtual subject. I'm going to call this body and face. Add and then I'm just going to go and add those two subjects. Then back in MoCat Manager, I'm just going to apply, instead of the body data that's coming in on unknown, let's apply the new virtual live link subject where they're combined. And you should now see that she's animating to my facial pose. So if we just want to isolate that to take a closer look, let's just give the source as the webcam. And now you can see it's matching my lips and my eye blinks and my facial expressions. So if we now switch that back to the virtual live link subject, we've combined a two. And that's it and that's how we set up meta humans for MoCat Manager.

**Frame:** tutorials\frames\metahumans-for-mocap-unreal-engine-animation-hub\frame_000.jpg


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
