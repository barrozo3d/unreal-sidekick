---
title: New Unreal Engine 5.8 Metahuman Crowd Plugin
source: YouTube
url: https://www.youtube.com/watch?v=bJIPlvmoTVw
author: Smart Poly
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/new-unreal-engine-58-metahuman-crowd-plugin/
frame_count: 4
---

# New Unreal Engine 5.8 Metahuman Crowd Plugin

**Source:** [YouTube](https://www.youtube.com/watch?v=bJIPlvmoTVw)
**Author:** Smart Poly
**Duration:** 9m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello guys, welcome back to another video. Epic Games just officially dropped on religion 5.8, and along with it they introduced a brand new feature called the MetaHuman crowd plugin. The MetaHuman crowd plugin allows you to assemble optimized instances of MetaHuman characters to create crowds simulated by mass, scaling from the tens to thousands of characters. The new experimental plugin provides a complete assembly pipeline with seamless transitions between high fidelity actors and low fidelity instance skeletal meshes based on camera distance. And in this video we'll be checking out the new MetaHuman crowd plugin, the sample project, which is currently free to download on fab, and I'll actually show you guys how to get your hands on it. Also before we get into the video, I just released my new Unreligion masterclass course bundle. I just launched a brand new Unreligion masterclass course, this bundles together all of my courses showing you how to make games inside of Unreligion. This masterclass course has over 150 plus hours of learning content, and I will show you how to make eight different games from complete scratch. You'll master multiplayer networking, survival mechanics, AI, user interfaces, game optimization, mobile development, and so much more, included in the masterclass bundle or all the completed game project source files. So you can use them as a reference while you learn, or if you just want the completed game project we have you covered. Check out the Unreligion masterclass link in the description below, and with that being said, let's get right back to the video. Alright guys, so here we are in the sample project. As you can see on our screen right now we have over a thousand metahumans spawn into this level, and just to prove that these are indeed metahumans, we're going to zoom up in here, and we should be able to check out some of these characters in here. But yeah, as you can see, you should be able to see like the details on the skin. So these are indeed metahumans characters. What the metahuman crowd plugin allows you to do is to have these high fidelity metahuman characters, and basically to explain what's going on here, you have first at the very top left there the FPS. Right now it's running at about 50 FPS. Now take that performance with a grain of salt because I do have my recording software and probably like 20 tabs of Chrome open. Plus this is running in the editor. So again, there's all that performance overhead that you have to take into consideration. So the FPS, you know, mileage may vary. So we have the numbers at the top left, we have 1000 metahumans that are currently spawned in. However, right now where I'm looking, there's only 400 on screen. So the number on screen is going to show us how many we can see on screen. So if I actually zoom all the way out here, we should be able to see all 1000 metahumans on screen at the same time. Okay, you can see that they're actually calling out there. So if I zoom out up in the very top, you can see that they're actually being called out. So that's how many are on screen. And now currently I have zero metahuman actors. So there's no actual high fidelity meshes until I actually zoom up into here. Now you can see there's five, about five at a certain given time. So I can zoom in here. And basically if we're up real close to the actors, it should stream into an actual high fidelity character model. So yeah, that is basically what's going on. And again, the FPS is sort of capped around 60. And I do have a bunch of random things going on in the background. Plus this is the in editor performance. So again, the mileage may vary. And the impressive thing about it is that all these characters are moving at random paths. So all these characters are randomly navigating. And this is all powered using the mass AI system or the mass entity system, which we saw in like the city sample project. Basically, that's what they're using to have all of these random NPCs navigate around. Now over here, we can see that these NPCs, these metahumans over here are actually following a path, the predetermined path. So you can see they're sort of like walking in this line. But also they have avoidance. So you can see that they're sort of walking and avoiding each other, which is also another feature of the mass entity system. So again, these are things that we've seen in the city sample project. But now we're just seeing it in a more on a more massive scale. Because in the city sample project, they were quite limited on how many NPCs were spawned in the level. Whereas right now we have a thousand of these characters moving all with unique outfits. And that's another thing about this plugin is you can build complete modular components. So you can have the head, the hair, the clothing, you know, whether that's the different boots, the shoes, as you can see, all of the parts of the outfit can be customized and basically randomized. So you can have random NPCs in the level. And also I believe this is using the night. So if we go ahead and use the command r.nana visualize triangles here. Yeah, so everything all of the metahuman characters have manites enabled on them. So let's go ahead and zoom in real quick. And looks like I think the base models might not have manites. I'm not sure what's going on there. You can see that they're black like that. You see those ones are kind of highlighted in black. But yeah, these are all the triangles. So let's go ahead and just zoom out here. So let's go ahead and check out the next thing, which is the crowd collection asset. So this is basically like a metahuman collection asset, which allows you to see sort of all the different outfits that you want to set up for your metahuman characters. So this sort of has all the different presets for the heads. I don't know if you can see this here on the left. But these are all the presets, the head customization, the different shoes, the pants, the hair options, all that stuff. So if we select this, it looks like we have actual asset file, all the references, but also it looks like we can change the colors. So we have the stitch color on the jeans. So maybe you change that and mess around with all of those parameters, but also looks like we have the shirt color over here. So maybe we'll change this to like a bright green or something like that, save that, apply changes and save. And so hypothetically, you could go in and add your own custom, you know, metahuman clothing and outfits in here. And this is where it will pull from. Also another thing is if you press O on the keyboard, you get this little widget. So you can adjust the time, which basically affects the simulation. So right now they're running at the same speed. If I press O and slow this down, we can kind of slow down the simulation and kind of get a better look at some of the characters, the detail on these guys. So yeah, that is sort of the detail on the characters. As you can see, let me know guys think about this down in the comments down below. Yeah, so you can see all of the up close metahuman character details. And let's press O again, we have the adjust time, we have the movement speed. So again, we could just actually we can just completely freeze this. So maybe we can take a look at the character here and ask for the actual geometry. Let's take a look at the wireframe. Yeah, this is what you're kind of dealing with. And I'm going to say it's pretty well. I think game optimized compared to like the other metahuman base models, like the cinematic versions. So yeah, as you can see, the geometry is pretty good. I don't want to say optimize for games. Where else can you get a thousand different characters with different outfits, you know, running at 60 FPS with, you know, crowd interaction, simulation, all that stuff. So yeah, that is basically the metahuman crowd plugin. Now how to actually get your hands on it. So you can head over to Fab right now and go over to the metahuman crowd sample project over here. And basically you can just add this to your library. And essentially, this is just a plugin sample project. So you'll add it to your Unreal Engine 5.8 install. And then you want to create a new project. Go to your plugins and search for the metahuman crowd. And you want to enable the metahuman crowd plugin, which is experimental as well as the metahuman crowd content, which is the sample project that you claim from Fab. So again, you need to claim the sample project from Fab over here and install the plugin to 5.8 to get this sample project downloaded. So yeah, that is pretty much it for this video. I wanted to just make a quick showcase video of the plugin itself. I'm excited to hear you guys' thoughts on this. I think that this is very promising, seeing as this is a experimental feature currently. And this is a way to simulate over, you know, a thousand different characters on the screen and run it around, you know, 50 to 60 FPS. Again, the performance you need to take with the grain assault because again, this is just editor performance as well as I do have a bunch of random recording stuff. So just take the results with a grain assault. But yeah, let me know what you guys' thoughts on this down in the comments down below. And as always, I'll see you guys in the next one.

**Frame:** tutorials\frames\new-unreal-engine-58-metahuman-crowd-plugin\frame_000.jpg


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
