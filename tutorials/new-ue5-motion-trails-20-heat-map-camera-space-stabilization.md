---
title: NEW UE5 Motion Trails 2.0: Heat Map & Camera Space Stabilization
source: YouTube
url: https://www.youtube.com/watch?v=erHPJ8eoXyY
author: Unreal Engine
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/new-ue5-motion-trails-20-heat-map-camera-space-stabilization/
frame_count: 4
---

# NEW UE5 Motion Trails 2.0: Heat Map & Camera Space Stabilization

**Source:** [YouTube](https://www.youtube.com/watch?v=erHPJ8eoXyY)
**Author:** Unreal Engine
**Duration:** 9m43s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey there, welcome back for some more Unreal Animation training. I'm Sir Wade and we're going to take a look at the ACOM Animation Sample Project one last time for a few more videos. This is the fourth series in case you're watching all of them. And we're going to dive into the technical animation tools this time around. In this particular video, we're going to start off with the new Motion Trails that we're introduced in Unreal Engine 5.6, which are very powerful. In case you're just joining us, this is technically the fourth set of videos in this series. And so if you're looking for something to kind of ease in, catch up on some of the others and come on back. But here we are in the Sample Project. I am in Shot 50, which is this awesome shot where he breaks through the door. We've got Gamma jumping through the little gap that gets created and Beta is forced and open the doors. We're going to cover the constraints and other stuff in some later videos, but for now, let's focus on the Motion Trails using Gamma. So here he comes, hopping through the little gap in the door. Let's go ahead and leave our camera behind and we can see him pop on through. There he goes. So I'm going to come in here and grab the body control on Gamma. Now, to activate Motion Trails, it's actually very straightforward. Up at the top of our UI, we have this little bouncing ball icon here. If we click on this, it will automatically create a Motion Trail for the selected object. It's a little bit thin, but it is there. If I hide my control curves, you can see the little purple line, hopefully. Now just to make sure we can see this, I'm going to go up to the top little menu here, scroll this down. I'm going to go to Advanced and I'm going to change the Trail thickness to something like 2. Now you would actually see the change until you sort of refresh this by collapsing the menu. And then it'll pop up. So it's not a dynamic slider. Right off the bat, I'm going to go back in here and change the Trail Style from default, which is just a solid color. And actually, you know what I should do is I should also turn on Show Marks so you can see the individual key frame spots of where the frames are. And we can also go back in here and we can adjust the size of things like Marks. I can maybe switch this to like 10. Maybe make the key size, I don't know, 5. Hit Enter. And then when I go and refresh this little menu, the things all change. So now we have this square key at the end, little marks throughout. But what I want to do is I want to change in the dropdown the Trail Style from default to dash, we'll show you an actual spacing layout of our animation. So now when we hit play, we can actually see the, you know, the spacing as he jumps through the little gap here. Or we can switch it to some other more interesting modes. There's dash, there's also time, which is kind of what you expect for before and after. Before and after of wherever the character is and versus where he's going. But the new one I really like is Heat Map. Heat Map is really interesting. The Heat Map mode shows you where the character is moving the fastest or the slowest. So the hotter the Heat Map, so this red section, for example, the further the distance, the bigger the spacing, anywhere where it's green is where the character is moving at their slowest. So we have some hang time up the top here and that is the slow part speeds up with gravity. A little bit slower there, a little faster there. And so the Heat Map is a really interesting way to look where you can find speed problems. Now if I go back to my camera view, we can see what this looks like. So here is the character's path through space. And you'll notice that as we kind of move around with our camera shake, the trail through space is actually in world space. It's just a plotted out path of where the character is going to go just in 3D space. But one of the big reasons that we like motion trails is sometimes being able to look at it from the specific camera's perspective. Having it in camera space can be very helpful. So what we can do to switch that is we can actually take this motion trail that we have selected. And again, just to get this there, I selected one control and I hit this little button. If I want to just click this button again, that'll turn it off. I'm going to turn it back on and that's a quick and easy way to get in and out of the motion trail. But if I want to change the way the motion trail operates, I can twirl this down. I can go to the top sec body itself and that's the specific pinned trail. You can have multiple things pinned. We'll cover that in a second. But I can actually change the space that this is in. So if I hit this little check box and now I say what object will be wanting to sort of put it in the space of? So I'll pick my camera and it'll say what part of the camera? I want the camera component. If I do that, now what will happen is that this motion trail is more or less going to be parented to the camera. And so if I move around, you'll see that the entire motion trail is kind of shifting in a perspective view. Like the whole thing is moving. As if the character were sliding. What's happening here is it's actually now attached to the camera. It's been stabilized and normalized in camera space. So now I can actually see where the character is going to be and what their arc is going to be from the camera's perspective, considering the camera shake and other camera animation I have in the shot. So that can be really, really helpful, depending on what you're doing, to be able to lock the motion trail into camera space so easily. And if you say, you know what, I don't want that anymore. I want to go back to just world space motion trails to see if I'm having another problem. I can go back to the body control and I can just say, you know what, turn that space off. And I can see that it recalculates and it's moving again in world space. So if I leave the camera view, that motion trail is stable and it just represents the 3D position. Now to go a little bit deeper, if I want to get this thing off, I can just deselect it and that just turns it off. But let's say I want to look at a body control, maybe one of the tail controls and let me see if there's a good head control here. Now I just grab the neck start and that's going to be kind of the base of the skull here. And then maybe I'll grab like the jaw control, which is this little one right under the jaw. That's a good one. We can kind of track where the nose is going to be more or less. But now it might behave a little differently than you expect. If I just click this button, it won't actually just make motion trails for all these objects because I already had a selection. I was already using the body. And so it basically just assumes, oh hey, you just wanted to reenable what we had. Now I can unpin whatever I have already, you know, being shown and displayed with the motion trail. Or I can say pin selected, which I'll go ahead and do. If I say pin selected, it will add any selected objects and create motion trails for those as well. And so here is where I might want to go in and change the trail style from heat map to dashed. Or maybe this is a good example of where you might want to use something like time. Because with so many, you know, lines and curves, it can be a little bit tricky to know where we are in time. So now I can see, ah, the blue section has passed, the red section is where we are, and it's a little bit easier to differentiate sort of where these things are located. But then also you might want to adjust, you know, the size of these things. So if the trail thickness is a little bit too much now, I might bring it down to 1.2, it enter, close that little menu, and that'll shrink them all a little bit, which helps. But anyways, that's what pinning does. I'll click this to just turn everything off, but you can mouse over and you can see some of these hotkeys. You can alt click to remove a selected object from the pin list. You can, you know, basically just add and subtract stuff from what's all being displayed. You can also switch this to show trails on selection. And then if I turn this on, now what it'll do is it'll use my selection. So if I grab a net control or if I grab one of the ear controls or something, it's going to add things based on my selection, which can be handy, but also if I grab a whole bunch of things at once, it can be a little bit overwhelming. I think the default is 10 things here. Yeah, max number of pins, it's set to 10 by default. It doesn't want to pin more than 10 things at once. So you can up that, reduce that, whatever you want to do, just different modes. So you can have selection based trails. You can have pinned trails that are just there all the time. I can unpin the trails so that there's nothing that's always there. But I can grab individual controls and I can, for example, shift click and I will add it to the pin list. And so now I've got a head control here and you can see inside there is my neck pinned trail here. And then there's also an offset button. And so if you hit offset, what that's going to allow you to do is get the manipulator here. You can see that it's turned red. I'm kind of in this this preview mode and I am allowed to now move this. It's defaulted to the center point, I believe, of the actual joint that that control is responsible for. But if you know what, I want this to be offset. It is the neck, but I want it to show me from the top of the neck. I can move this to the top of the neck and it's going to offset sort of where it calculates that path from. So it's still using the same bone at the same control or whatever, but now it's just offset from where it was before. And so these are some of the options that you are given to adjust to how these motion trails are going to operate. You can also change the specific amount of frames if you don't want to have, you know, the whole shot visible all at once. And so you can change it so that you only see, you know, 10 frames and I the direction or whatever. So it kind of shows up goes away and see here. And so that's the new motion trails in a nutshell. It is a very, very handy new rewrite of the tools that gives you a lot of flexibility. And so feel free to explore that, change the colors, the sizes, things like that. And, you know, enjoy visualizing your shot, adjusting your arcs and ensuring that the motion looks the way you want from specific camera angles or just in world space and so on.

**Frame:** tutorials\frames\new-ue5-motion-trails-20-heat-map-camera-space-stabilization\frame_000.jpg


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
