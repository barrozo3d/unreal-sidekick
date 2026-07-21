---
title: Landscape Mode Basics (Unreal Engine 5.7) Part 1
source: YouTube
url: https://www.youtube.com/watch?v=rxUsQRcq168
author: R SH
ingested: 2026-07-20
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/landscape-mode-basics-unreal-engine-57-part-1/
frame_count: 0
frame_status: pending-selection
---

# Landscape Mode Basics (Unreal Engine 5.7) Part 1

**Source:** [YouTube](https://www.youtube.com/watch?v=rxUsQRcq168)
**Author:** R SH
**Duration:** 30m45s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py landscape-mode-basics-unreal-engine-57-part-1 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome to my Unreal Engine tutorial for building landscape or terrain,
[0:10] for video games, simulation or whatever you are going to do in your project.
[0:18] My name is Ram and a little bit about me. I'm a technical artist and educational technology
[0:25] expert. I have been teaching 3D modeling animation, game design for a really long time. It is
[0:35] my pleasure to share what I know so far, what I have experienced so far with you and hope
[0:45] you learn something from it and enjoy it. Today, I'm going to start with the very basics
[0:54] of landscape design in Unreal Engine. As you see, I'm already in the Unreal Engine editor.
[1:06] I'm using 5.7.3. Actually, funny thing is I literally updated it just yesterday. I just hope I don't get
[1:15] too many surprises today. What I'm going to do before anything, I'm just going to create a new level
[1:23] and go with the basics, create, and I'm going to get rid of this guy.
[1:29] Now, one of the things that is very important to know before even designing the land is what is it that we're going to do with it?
[1:40] Is it going to be a large landscape for a massive multiplayer game or is it just going to be a small one for something
[1:52] at a smaller scale? Now, assuming that you already know what you are going to build and what characters or props are going to be on it,
[2:06] I actually suggest we add one of the packages we have on Unreal Engine. I'm just going to add the third person to this project.
[2:23] I tell you why because I just want to build based on the third person character we have.
[2:32] Alright, let's add this to the game mode override. There you go. I did that because I want to press play and have this character respond.
[2:44] We don't have a terrain yet and of course the guy is falling off the sky.
[2:48] Now, let's just save this level. I'm going to call this my land and let's just create a new folder here, levels.
[3:03] I just like to be organized. I love naming my assets and put them in a structure. There you go, level. My land is here.
[3:14] We need to change our mode in Unreal Engine. We are now in selection mode. Let's go with landscape mode and immediately I'm just going to press F to focus on the land.
[3:34] Actually, I don't need to. Now, what we have here is a grid. It's not a land, it's nothing yet. It's a grid. Our land will be built on this foundation.
[3:48] So what does that mean? This is the default setting. It means if I literally press create, there you go. I get an absolutely flat land and I'm just going to press play.
[4:01] There you go. My character is literally on top of it. That's not what I want. What I want is, okay, now I press F and it focuses on the object, is to first I understand what this grid is and what it does.
[4:21] Basically, this grid tells you what is the foundation of your terrain. By the way, I already changed the camera speed to 10 because I really like to go back and forth and rotate around as much as fast as possible.
[4:41] It's up to you. Now, the location is obviously so I can, if I go 500 on X, it moves 500 on X. Let's just go back to zero. By default, let's make sure everything is 0, 0, 0 in location and rotation.
[4:58] The scale is 100% on each side. What I really like you guys to understand is the Z or the height. It says 100, but you don't see it because there is no volume yet.
[5:13] That volume, the 100 means how high your land can go. Especially when we use height map and that's actually what I'm going to share with you in the second half of the session is how high it can go.
[5:34] Is it 100? Is it 50? And what not? Now, section size, right now we are 63 by 63. I can go a smaller, but let's stick with 63 by 63.
[5:47] Now, what does this mean? 2 by 2 or 1 by 1? 2 by 2 basically doubles the number of sections inside a component. Sections per component. Let's go back to 1 by 1. Again, we are not doing something big.
[6:05] I might as well just go even to do 31 by 31. And overall resolution, 512, 512. Now, you see by adding resolution, it changed the size of the land grid.
[6:30] Total component is now 64. If I press create, you saw that before, it's just going to give you a flat land.
[6:39] The other thing that I want to mention to you is you can literally import a height map. We're going to do that by the way. So don't get excited, but just bear with me. Let's stick with the principles now.
[6:55] You can import a height map and let that height map be the guiding principles of your land design. Now, I'm going to press create. There you go.
[7:09] I have another tiny land, but it is small enough. If I press play, my character stands on top of it. And now you see I have this brushy thing here.
[7:24] This is the brush that allows us to sculpt the land, build mountains, or create mountains, create rivers or valleys.
[7:35] So take a look here. We have several brushes here in the sculpt mode. So we have manage mode, which you can deal with components, add, remove.
[7:46] We will deal with these in the later sections. You can select each component. You can delete them. You can add to them and so on.
[7:56] So let's go back to sculpt. In the sculpt mode, let's take a look at the brush type. You have a simple circular brush. This is a really cool one, alpha brush.
[8:09] I will go over this later on in the session. Pattern brush and of course the whole dealing with an entire landscape component.
[8:21] Again, we're going to go through all of that strength of the brush. I'm going to actually change the size. This is too big. I'm going to change the brush size to 1000.
[8:32] Maybe a little bit more. 1500. Look, as I press, you can see elevation is happening.
[8:46] Now you want this a little bit more intense. Go with higher strength. I'm not adding pressure. It's just a brush of strength is a little bit more dominant.
[9:03] Now, by default, left click raises the geometry. You want to push it down. You hold shift. Basically, inverts the brush.
[9:24] Now, we have used clay. That means it actually adds geometry. Look what happens here. It's like there is a component added to it. It keeps the top side. It just elevates the rest.
[9:42] Unlike the non-clay one, that everything is elevating on its own. Adding clay, it looks like you are adding something on top of it. It still elevates and raises, but you can see the difference.
[10:03] Now, apply without moving means if I click and hold, it raises it. Let me uncheck this clay brush. Click and hold, it goes up. If I uncheck it, click doesn't do anything. I must move.
[10:23] I hope this makes sense so far. This is another cool area that I really love in Unreal Engine. Especially the ones that work already in tools and applications like Photoshop, ZBrush, Modbox.
[10:42] When you see layers, you know what it is. Now, let's just assume you don't know. People who are here, like literally Unreal and landscape in Unreal is the first thing they are going to sculpt. Bear with me.
[10:56] Layers are one of the greatest tools we have in landscape sculpting in Unreal. It allows you to divide sections or features in your landscape and group them into layers. For example, this first one, I'm going to rename it and call it mountains.
[11:18] This mountain layer is going to house all of the mountains that I have. Or I can just say, you know what? Mountains, the main mountains here. I'm going to create a new one, create a new layer.
[11:48] Let's come back. One landscape editing layer, select. I'm going to name this one side mountains. All of the mountains I have on this side.
[12:05] I'm going to just raise the tool a little bit. There's a strength and there you go.
[12:25] And I'm going to create a new one and call it valleys. And this one, I'm going to hold shift. Maybe not as a strong.
[12:56] Okay. Now each of them, you need to select them to actually make sure the sculpting you do is happening in the proper layer.
[13:11] Now look what happens when I turn off or hide the valleys. Gone. Side mountains. Gone. Mountains, gone. Now side mountains back on.
[13:23] Now take a look. There you go. Take a look here. You have alpha with a number one in it. That one means 100% of the effect that it was there.
[13:43] If you want 50% of that, you say 0.5. You want 10% of that, you said 0.1. That's really little. Let's go 0.25. Okay. You get my point.
[13:54] Okay. Now with that in mind, you could actually say, well, these valleys seem to be too deep. Let's change that to 0.7. 70% of the affected area.
[14:07] There you go. Now let's play. Ooh, the valley is actually falling. I think size wise we are okay. The size makes sense with the size of our characters, which is good. That's what we want.
[14:24] So, well, if it was in my class, I would say if anyone has any questions, if you do, well, I hope what I have provided so far answers your questions.
[14:41] All right. So we went over the layers and now you know how we can sculpt the landscape in different layers. Now let's go over other brush types that we have or sculpting tools.
[15:04] Erase basically means, okay, it's just going to erase everything. Well, yes and no. It doesn't erase the side mountains. Why? Because I'm actually in the mountain layer.
[15:20] So it is going to only erase the mountains. And again, look at the strength because it does matter and erasing doesn't push it down. It just gets it closer to the flat level. Look, it doesn't go below the flat.
[15:36] It does not go below the flat level. All right. Smooth. Again, the same concept applies. You want to smooth something in a layer. Make sure that layer is selected.
[15:50] Smooth. Again, the strength matters. It just softens the sharpness. Your brush size here also matters. Because again, if you have a large brush, bigger area is going to be smoothed.
[16:10] Flatten. Flatten. If you set up your brush size, look at this. I am changing the brush size and the falloff. Now look, brush size, let's just say 2000. Falloff is point. If I say one, sorry, not point one. One. One again means 100%.
[16:36] So look here. No, not 200. 2000. I lost a zero. Look here. It's very, very blended. Now, if I go point five, that means the falloff is half of the brush size. Now it flattens this way. Look, it really flattens wherever it touches.
[17:02] Ramp. All right. Ramp is actually quite cool. Maybe, you know what? Sometimes I want to make sure I'm not messing up too much. So I'm going to create a new layer. I'm going to call this ramp or ramps.
[17:19] So all of the ramps are going to be in this. So ramp, it's not like this one. It's not like a typical brush. You need to show, you need to use and start and end. So one, I'm going to create a ramp from here to here.
[17:36] Actually, I'm going to go up. So I'm going to create a ramp from that corner all the way to that mountain. There you go. Create a ramp. Now, in case that's not very obvious to you what it did, I'm going to actually do one here.
[18:07] There. Add a ramp. There you go. Reset. Reset doesn't mean resetting what you did. For that, you need to undo. Reset actually resets the tool so you can create another one.
[18:28] One. Let's create one here. Oh, no, that's too far.
[18:33] There you go. From that corner to this corner, do a ramp there. Again, the follow-off also matters. Look, the follow-off follows. I'm going to reset. Create a new one here.
[18:53] From this corner to this with a follow-off of almost zero. Look what happens. This one is very, very sharp. Very, very sharp.
[19:06] Reset. Erosion. You really need to know what it is. Sorry, how you are setting up the brush and the brush component because it does actually matter.
[19:24] So I'm going to increase the tool because I really want you to see what it does. Right now you may say, well, it's just like pushing things down. No.
[19:35] The tool's strength is high. Let's go with 0.5. And you could actually say combined layers. So basically means it's going to apply to all of the layers.
[19:48] It's just going to apply to everything or you can just add it to a different layer. Let's just say I'm going to add an erosion layer.
[20:04] Erosion or water erosion. Let me go here. Look.
[20:13] Even though I am in the erosion layer, it is affecting the other layers too.
[20:22] Now threshold 64, thickness 250, iteration. Let's go higher. And noise mode both. So raise and lower what you have.
[20:36] And brush size, let's go lower and the fall of a lot higher.
[20:50] Maybe a little bit strength. Spiritual 60, 90. Okay. There you go. You see how it works.
[21:00] Now, again, if I hide it, the erosion does not show. Then we have hydro.
[21:12] I am still in the, sorry, I need to enable the layer so I can apply. Let's make this a little bit more and bigger.
[21:31] This is water erosion. Again, if I remove it, you see how it is. It's a very cool tool. Or you can just add noise.
[21:49] You can just add noise. This is too heavy.
[21:53] Too less strength. Again, depending on my brush size and fall off. So noise scale, you can go 256.
[22:04] It's very, very large or kind of like very minimal. Look at the noise. Let's just go with, let's say 10.
[22:15] And the tool of strength, maybe 0.1. Look at the noise.
[22:24] I am in the same erosion layer, by the way.
[22:31] Let's press play to actually see how it looks. This is the effect of the noise.
[22:38] The resolution is actually not extremely high. That's why it's a little bit weird looking.
[22:47] But you get my point. Then we have visibility mirror. You can basically change visibility of a certain layer.
[22:59] Or you can, let me zoom back. You can use mirror to basically mirror one side to the other.
[23:11] Let's go with the side mountains and do the mirror.
[23:19] So the side mountain, this side. Copy this side. You want to copy the ramps.
[23:25] You do that. Actually, we don't have any ramps this way. I think we just destroyed them.
[23:36] There you go. Let's mirror the ramps here.
[23:40] Now look at this. Whatever is on this side will copy on this side. So if I press apply, the ramp is going to be gone.
[23:50] So if you want to recreate the ramp, you say positive x to negative x. Then press apply, your ramp copy is here.
[23:59] Not your mountain, only your ramp. There you go.
[24:05] Alright.
[24:10] And of course you can move your mirror across. Let's just say everything here to be copied here.
[24:19] Let's just say apply here. There you go. You got your ramp. Everything copied here.
[24:25] But let's actually, I'm going to undo this. Let's actually, I'm going to get rid of the erosion layer as well.
[24:36] Done. So you see like the layer and all of its content gone.
[24:41] Let's go back to the sculpt mode because what I like to share with you is the type of brush that we can use in a sculpt mode.
[24:51] It's very, very helpful. I'm going to save.
[24:55] Okay. And I'm going to get a little bit closer here.
[25:02] We can add a texture. Look here. Right now the placeholder is this default checker texture.
[25:09] I'm not, you know what? I'm very tempted to press click. I'm going to press click. Look, literally that comes up.
[25:18] Now what you need to know is what does black and white in that texture do?
[25:28] Basically the white raises. Anything white in that pattern will raise your geometry.
[25:40] Now you may say, well, why the dark side is raising?
[25:50] Well, the thing is the dark side here actually represents the white on the texture.
[25:58] Okay. You see the texture is, by the way, rotating.
[26:01] If you wanted to stop, do not turn on auto rotate.
[26:05] Right now it's basically now following the pattern of the texture.
[26:10] So as you see, it's dark, but it's actually white.
[26:14] There you go. It gets elevated.
[26:16] Now with that in mind, I'm going to save this level again.
[26:21] We need to replace that.
[26:23] So I'm going to import something. I'm going to import the texture, but it's not any texture.
[26:29] It's a black and white texture known as brush alpha.
[26:33] People who use Mudbox or ZBrush use this a lot.
[26:37] So you remember and you probably anticipate what it is that I'm going to show you.
[26:44] So I'm going to create a folder here.
[26:46] I'm going to call it textures.
[26:48] I have a habit of organizing a lot.
[26:52] So textures and again alpha.
[26:57] Okay. And I'm going to import those textures.
[27:01] Where are they?
[27:06] There you go.
[27:07] Three textures imported.
[27:09] I'm going to save them.
[27:10] Now look here.
[27:15] Basically, if it looks bright or white, it's going to be raising the geometry
[27:22] or it's going to elevate the geometry.
[27:26] Now let's use this water texture here.
[27:31] Look here.
[27:37] It is elevating.
[27:39] Look at the nice noise it's creating.
[27:42] And if I turn auto rotate, then it's going to actually follow.
[27:50] Follow the path of the...
[27:56] object.
[27:58] Path of the mouse.
[28:00] You know what?
[28:02] Since we now know how to properly use these layers, I'm going to create a new layer.
[28:11] I'm going to call it alphas.
[28:19] So all of the noises that I'm going to create on this is going to happen everywhere.
[28:26] So I can raise the brush size.
[28:32] Not the strength much.
[28:35] I think point one is fine.
[28:40] Okay.
[28:41] The noise is quite obvious.
[28:45] Perfect.
[28:47] Maybe I bring this wood one in there and go around this area and maybe just attack point one five and add a little bit more noise there.
[29:04] And of course, if it's too much, by now you all know how to change that without doing much of effort.
[29:14] Let's go with 80%.
[29:16] Okay.
[29:17] Not bad.
[29:18] Let's go half of that and let's just press play.
[29:23] Okay.
[29:24] Very nice.
[29:25] Not a bad setup so far.
[29:29] Right?
[29:30] Not a bad setup at all.
[29:31] So basically what we did, we created a basic landscape geometry.
[29:39] We sculpted it with the tool, with the alphas.
[29:42] Because it looks decent.
[29:47] Especially, okay, let me move back.
[29:51] Yeah, it looks decent.
[29:52] It's not large.
[29:53] It's decent.
[29:55] Now, what I'm going to do in the next session is we're going to actually go over importing a height map into Unreal Engine and generating a land with that height map.
[30:09] And then improve it or modify it or adjust it with these tools.
[30:17] And in the following, in the session following that, I'm going to go over how to paint your terrain and add vegetation and trees.
[30:28] Until then, and until session number two, which is again, as I said, importing the height map and add the trees.
[30:39] Adding the details.
[30:41] I wish you all the best and see you soon.



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
