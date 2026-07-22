---
title: Everything You Should Know About MegaLights! - Unreal Engine 5.5 Lighting Tutorial For Beginners
source: YouTube
url: https://www.youtube.com/watch?v=A_7t9BqeQ_A
author: Karim Yasser
ingested: 2026-07-21
ue_version: "UE 5.5 (MegaLights experimental)"
tags: [lighting, lumen, megalights, rendering, post-process, beginner, intermediate, ue5-5]
extraction_status: complete
frames_dir: tutorials/frames/everything-you-should-know-about-megalights---unreal-engine-55-lighting-tutorial/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Everything You Should Know About MegaLights! - Unreal Engine 5.5 Lighting Tutorial For Beginners

**Source:** [YouTube](https://www.youtube.com/watch?v=A_7t9BqeQ_A)
**Author:** Karim Yasser
**Duration:** 30m22s | 17 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] If you are struggling with lighting performance and you cannot use as many light sources as you want,
[0:06] then this video is designed specifically for you.
[0:10] It doesn't matter what is your skill level, because I will discuss every bind step by step so you can follow up with me.
[0:18] The video will be separated in a lot of chapters and it covers a lot of the fundamentals of the engine and even installing Unreal Engine 5.5.
[0:28] So if there is a topic you already know some information about it, you can skip it and start directly with the topic or chapter you want.
[0:37] We will also go into a lot of technical aspects of Lumen and MegaLights and I will show you a lot of tips and tricks to get the best out of this feature.
[0:48] At the end of this video, you will be able to use MegaLights efficiently with some tips and tricks for Lumen to get very high quality results and a lot of more topics.
[0:58] So let's start with the learning objectives.


### Learning Outcomes [1:01]
**Transcript (timestamped):**
[1:01] What are the learning outcomes of this video?
[1:04] First, we will go through the epic launcher and configure the project settings to maximize the effectiveness of Lumen and MegaLights.
[1:14] Then you will get fundamental knowledge of the different light actors inside Unreal Engine 5.5.
[1:21] We will talk about the differences between static and dynamic lighting, more details about light mobility.
[1:28] Then you will be able to differentiate between software ray tracing and hardware ray tracing and when to use each one of them depending on the case you are at.
[1:40] You will then know how to use Lumen properly inside your project and configure its project settings to maximize the quality of Lumen and get a good performance out of it.
[1:51] Then we will start using MegaLights feature and get the needed information you will have to know to start using it effectively and convert your existing projects to start using MegaLights.
[2:05] And also we will discuss the differences between the ray tracing shadows and virtual shadow map method and we will get a quick highlight about the shadowing methods available inside Unreal Engine.
[2:17] Also, you will be able to know how to utilize post-process volumes to get high quality results out of Lumen, MegaLights and other options to control your environment if you are using multiple volumes inside your scene.
[2:33] And to make sure you maintain quality and consistency over different areas.
[2:38] And at the end of the video, we will know what are the limitations of MegaLights as it's still an experimental feature inside Unreal Engine.
[2:47] Also, you will know how to quickly run a performance overview after applying MegaLights to your existing lighting actors.
[2:54] So let's get started.


### Installing Unreal Engine 5.5 [2:56]
**Transcript (timestamped):**
[2:56] First of all, we have to create a new project.
[2:59] So I have the Epic Games launcher opened and this is the screen you should see when you initially open it.
[3:07] After you install it from your browser and sign in with your account, this is the default page you will be landing in.
[3:14] We have to go first to library section and we will see the engine versions.
[3:20] So if you are pretty new to Unreal Engine, you should not see any version in this section.
[3:25] It should be empty.
[3:27] Also, you will not see any projects like mine.
[3:29] So don't worry if your screen is a bit different from mine.
[3:33] Initially, we have to uninstall Unreal Engine 5.5 because MegaLights are not available in any other version.
[3:41] It's only available in 5.5 right now and I will go with you step by step on how to install it.
[3:48] You will see this plus icon next to engine versions.
[3:51] Once you click on it, it will add a version which is great out and you have to select the version you want to install.
[3:58] So in my case, I have 5.5 installed already and I will not be able to reinstall it again.
[4:04] So I have to try it with another version and if you are installing it for the first time,
[4:10] you can follow with the same steps but with another engine version.
[4:14] Let's recap it again.
[4:15] We have the plus icon to press on it and we will see a new great out version.
[4:20] And it's not installed yet.
[4:22] So we have to select the version.
[4:24] When we press on this drop down menu, it will sort out all the versions available for Unreal Engine
[4:30] starting from Unreal Engine 4 up to 5.5.
[4:34] So you have to select 5.5 version and when you are ready, click install and it has some options to choose from.
[4:41] It has the folder, the install location and you can change it using this browse button.
[4:46] When you press on it, you have the freedom to choose wherever you want to locate your engine.
[4:53] I prefer to keep it on an SSD drive to make it faster when it's loading and creating a project.
[5:00] So after choosing the installing location, you have another button which shows options.
[5:06] And what does that actually means?
[5:08] When we press on it, it shows a lot of variety and options.
[5:12] It has the core components, which are the required files for the engine that has to be downloaded and installed properly.
[5:19] And it's great out so you cannot unselect it.
[5:22] But the other options are optional to select and that contains the starter content, templates and feature backs.
[5:29] The engine source, this is more likely for developers who are willing to do some debugging using the engine files.
[5:36] And also we have the target platforms.
[5:39] We will not require any of these options to be enabled.
[5:43] So turning off all of these options can save up some space and also will decrease the download size.
[5:50] Now after that, click apply and press install and it will start downloading the engine files and then install it for you.
[5:58] And once it's ready, it will be available like that.
[6:01] So in order to launch and create our first project, we can do that by pressing launch easily from the Epic launcher.
[6:09] And it will take some time to open, especially if it's the first time.


### Creating Our Project [6:13]
**Transcript (timestamped):**
[6:13] So now after we press launch, it should show this window.
[6:16] We have a variety of options here.
[6:18] I have also other projects.
[6:20] If it's the first time for you, you will not be able to see any of these projects.
[6:24] It should be a blank screen.
[6:26] However, you will be able to see the same categories on the left hand side and the other options.
[6:32] It's just not the project you will be able to see.
[6:34] So to create a new project, we have to go to games.
[6:37] And here we have different templates to start with.
[6:41] We have to use blank.
[6:42] Then we have some other options at the bottom and on the right hand side.
[6:47] Let's start with the options on the right hand side.
[6:49] We have to select Blueprint and the difference between them is a C++ generates some new files for developers and we will not need to use that.
[6:59] So we will keep it at Blueprint, the target platform for desktop and the quality preset to maximum.
[7:05] And we have an option to whether include the starter content or not.
[7:09] So in our case, I'll keep it on and then we have the bottom section to adjust.
[7:14] We have the project location.
[7:16] We can press on this folder icon to browse for a folder.
[7:20] When we press on it, it will open a location.
[7:23] You can use any location to add a project to.
[7:26] So it's up to you to choose the location.
[7:28] I will keep it as it is for Mayan.
[7:30] And then we have to specify the project name.
[7:32] Note, there's some limitations to the naming conventions of the projects.
[7:37] For example, you cannot start with numbers or special characters and you cannot use spaces between words or characters.
[7:44] So for example, if I'm going to type megalites, I have to keep it as one word.
[7:50] If I'm trying to take a space, it will not let me create the project.
[7:54] However, we can use the number and some of the special characters.
[7:58] But as suffix or at the end, the idea is you cannot use it as the first character.
[8:04] So for example, we are going to name the project as megalites underscore tutorial.
[8:10] And then we hit create.
[8:12] The project should take some more time.
[8:14] I will let it to be done and we'll get back to you.


### Unreal Engine 5.5 Layout Fundamentals [8:17]
**Transcript (timestamped):**
[8:17] So this is the initial screen you might get.
[8:20] Yours might be different.
[8:22] So we have to keep consistency between me and you.
[8:26] So to do that, we have to go to window, go all the way down to load layout.
[8:32] And we have the default layouts, default editor layout.
[8:36] And instead of that, I will be using UE4 classic layout.
[8:41] After pressing on it, it should be changed automatically to the new layout.
[8:46] And if you, for some reason, missed out your layout like this and you have moved the tabs out of their positions,
[8:53] you can reset the layout from the same option going to window, load layout and choose UE4 classic layout.
[9:01] I will go very quickly to give you a brief about the tabs on the left hand side.
[9:07] You have place actors in which you can search for any actor you want.
[9:11] You can drag and drop actors from the place actors menu.
[9:14] And then the next tab is the content browser.
[9:17] Simply, this is your files holder.
[9:19] And that means you can create the files, store the assets.
[9:23] Also, you can import assets from your machine into the project.
[9:27] And always you have a search bar to search for specific assets if you have a big project.
[9:33] And also you have filters.
[9:34] Usually, you will not see these filters, but I have them already.
[9:38] You can add your own filters by right clicking here in this empty space and choose any filter you want.
[9:45] So for example, I will choose Niagara system.
[9:47] It will add a filter for Niagara system and will turn it on.
[9:51] As our project doesn't have any file for Niagara system, it shows no results.
[9:57] So to turn it off, I will click on it.
[9:59] So it toggles the filter on and off.
[10:02] If you want to delete it, you can right click on it and choose remove Niagara system.
[10:08] So that's it for the content browser.
[10:10] On the right hand side, we have two tabs, the Outliner, which lists all the actors that exist in your scene.
[10:17] And the Details panel, you will notice it has no options to view if we are not selecting any actor.
[10:24] So if I'm going to select, for example, the directional light, it will show some options
[10:29] available specifically for the directional light.
[10:32] And these options will change based on the actor you are choosing.
[10:36] If I selected the skylight, it has totally different options.
[10:40] However, it may have some common options between multiple light actors,
[10:44] but usually these options are designed specifically for each actor.
[10:48] So you have to keep in mind the actors that you are selecting to adjust the details based on it.
[10:54] So this is a quick overview about the engine default tabs.
[10:59] There is a bunch of other tabs available, but these are the most commonly used tabs in each project.


### Creating A New Level [11:05]
**Transcript (timestamped):**
[11:05] So now after we did a quick overview, we want to create our first level to start with.
[11:11] So in order to do that, we will go to the Content Browser, right click on your mouse,
[11:16] create a new folder, let's call it Maps.
[11:19] Now double tap on Maps, open it, and we have to create a new level.
[11:25] Now we have two ways to create a new level.
[11:27] We can right click in a blank space and select Level or go to File and choose New Level.
[11:34] What we will have now is a variety of options.
[11:37] These first two are designed to be working with World Partition, which is a new system of streaming,
[11:43] large maps, and environments.
[11:45] We will not be using it for this project.
[11:47] We might be using the basic or empty level.
[11:50] I prefer to go with the basic because it has some objects to work with.
[11:54] I'll press on basic and hit Create, hit Don't Save.
[11:58] Here it is, a new level, but we'll notice that the maps is still empty.
[12:03] So we have to go to File, choose Save Current Level.
[12:06] After doing that, it will open a new tab, go to Maps, and in the bottom section,
[12:11] give this level a proper naming.
[12:14] Name it level underscore mega lights underscore overview, just to keep it as much descriptive as possible.
[12:20] And now we have our level saved in the Content Browser.


### Different Light Actors Explained [12:23]
**Transcript (timestamped):**
[12:23] We will discuss the difference between these three light actors.
[12:28] The point light, the spotlight, and the rectangular light.
[12:33] It's also known as area light.
[12:35] I just want to turn off the directional light because it's a bit bright.
[12:40] So I'm going to select my directional light, go to the Details panel,
[12:44] and I will set the intensity to zero.
[12:48] And it will dynamically turn off all my global lighting in the scene.
[12:53] Now we have a better overview of these lights and what is going on.
[12:57] We can select these two lights.
[13:03] And on this icon, I will press on it so it toggles the visibility of these actors.
[13:09] So I can hide and unhide them.
[13:10] So let's go in a very quick way about the difference between each one.
[13:14] The point light is like a pulp light, which eliminates the area around it in all the directions.
[13:21] So it's a bit expensive on performance.
[13:24] Next one is the spotlight.
[13:26] It has a cone, so it's not spreading the light in all the directions.
[13:30] However, it's using a specific angle to spread the light in.
[13:35] And it's more usable for many light sources to have a directionality of the light and not
[13:41] having the light spreading all the way through our environment.
[13:45] And the third one is the red light or the area light,
[13:49] which is also restricted to a specific boundaries, but it's not like a cone.
[13:55] It's more like a studio light that we are using in real life.
[13:58] And this one is the most expensive because it's using ray tracing shadows.
[14:03] And this type of light is the one that is more used with mega lights as it has ray
[14:10] traced shadows and mega lights is designed to work efficiently with ray traced shadows.
[14:15] So keep in mind this kind of light as we will use in upcoming explanation.


### Light Mobility [14:20]
**Transcript (timestamped):**
[14:20] Now we have a very important thing to keep an eye on please pay attention for it.
[14:26] And it's the light mobility.
[14:29] Now we have three options for it by default.
[14:31] It's set to stationary, but we also have a static and moveable.
[14:35] Let's get back to that presentation to talk in detail about it.
[14:38] So the static lighting, which also known as the big or pre computed lighting,
[14:44] that means the lighting data in a texture called light maps.
[14:49] This process is called the baking.
[14:51] This is the most performant method of using lights, but it takes time to compute.
[14:57] And this type of mobility we are not using a lot nowadays because we have
[15:01] more powerful technology towards the dynamic or the moveable light.
[15:06] Second one is the stationary stationary is a hybrid solution between static or fully baked
[15:12] and dynamic because it uses dynamic shadow.
[15:16] But still stationary lights, you cannot move them in runtime.
[15:20] This one is a bit more expensive than the static because it uses dynamic shadows,
[15:25] which are expensive to compute on the GPU.
[15:28] The third one, which we are going to use in this video is the movable mobility.
[15:33] And it's also known as dynamic.
[15:35] And this is the most expensive method in rendering because it's all dynamic.
[15:40] And it uses the GPU to do all the calculations without any pre computed lights.
[15:47] So now you know the difference between different light mobilites.
[15:50] You have the static, the stationary, the movable.
[15:53] In our video, we will be using movable.
[15:55] So make sure any light you place in your scene has movable checked.
[16:00] So that's it for this section.
[16:02] So let's do a quick recap.
[16:03] We first created a level and discussed the different types of lights that are not global
[16:09] lights. And also we discussed the different options for light mobility in the static,
[16:15] the stationary, the movable.
[16:16] Next thing we will get into the project settings we need to configure in order to utilize
[16:22] lumen and mega lights.


### Project Settings Tips [16:24]
**Transcript (timestamped):**
[16:24] Now comes the most essential part of our video.
[16:27] You have to pay attention for it.
[16:29] As if you did anything wrong, you might not get the same results as mine.
[16:34] So in this chapter, we are going to use project settings to enable the maximum quality of
[16:41] mega lights and lumen.
[16:42] So first of all, how do we get the access to project settings?
[16:46] Well, we have two options.
[16:48] First, we can go to settings on the top right corner, press on settings and you can see project
[16:54] settings.
[16:54] When you press on it, it will open the project settings or you can go to edit, you will find
[17:00] project settings, press on it and it will open a new tab.
[17:04] It maximized and now pay attention to these options.
[17:07] But before we go through it, we have first to break down the window we see right here.
[17:12] We have on the left hand side a list of options and categories to choose from.
[17:17] And on the right hand side, it's more like the details panel.
[17:20] So we have to go to rendering and we have multiple options to be aware of.
[17:26] First of all, we have to check the global illumination.
[17:29] It should be set to lumen as well as the reflection method.
[17:33] Also set it to lumen.
[17:35] Don't use none.
[17:35] Don't use screen space in order to get full quality that we want.
[17:39] And now there are other options.
[17:41] There is a lumen subcategory and there is option which is use hardware ray tracing when
[17:47] available.
[17:48] This option only available for users who have a graphics card that support ray tracing.
[17:54] And if your graphics card doesn't support ray tracing, you will have to keep this on off.
[17:59] Then you will not use the hardware ray tracing.
[18:02] But instead, you will be able to use the software ray tracing, which is enabled automatically
[18:08] when this one is off.
[18:09] You might get a bit confused right now because there's a difference between the software ray


### Software Raytracing Vs. Hardware Raytracing [18:10]
**Transcript (timestamped):**
[18:14] tracing and the hardware ray tracing.
[18:16] So let's get back quickly to the slides.
[18:18] And inside Unreal, we have two options.
[18:21] We have the software ray tracing, which is mimicking the effect of the hardware ray tracing.
[18:26] So it's not as accurate as the hardware ray tracing and you will be limited to many
[18:32] features.
[18:32] So you will not be able to get accurate reflections.
[18:35] And unfortunately, you will not be able to use mega lights because it requires the hardware
[18:40] ray tracing to be turned on.
[18:42] The other type is the hardware ray tracing, which is the more expensive and more accurate.
[18:48] It enables you to use many options.
[18:50] So let's get back to our editor.
[18:52] Now we have to make sure that use hardware ray tracing when available is turned on.
[18:57] The real lighting mode, you can keep it to surface cache.
[19:00] I personally prefer headlighting for reflections.
[19:04] This has a higher quality when you are using lumen with reflective surfaces.
[19:08] And also this option, which is high quality translucency reflections, this is more likely
[19:14] to be working with glass, water and this kind of surfaces that its shader type is translucent.
[19:21] And it gives you much better results when you turn it on.
[19:25] Then the software ray tracing mode, keep it to detail tracing.
[19:29] It's more accurate and it might use a bit more of the memory.
[19:33] There is the screen tracing source.
[19:35] This is a new option.
[19:36] We could use the second option, which will be better for reducing the noise that is generated
[19:42] from lumen with the emissive sources.
[19:45] The last option in the lumen subcategory is the ray traced translucent reflections.
[19:50] Keep it to on, give you much better results.
[19:53] Now we have the option for mega lights under direct lighting.
[19:56] Simply turn it on and that's it.
[19:58] You have now mega lights turned on in your project settings and we still have some other options.
[20:03] So for example, if you have this option grayed out, you will have to enable support hardware
[20:09] ray tracing first in order to open all of these options and be able to choose whatever you want
[20:15] from them.
[20:16] And the last one in this page is the shadow map method.
[20:20] Keep it to virtual shadow maps as it's more consistent now with UE5.5 and it's ready for
[20:26] production.
[20:26] And now we are done with the rendering page.
[20:29] We can scroll down to platforms, go to windows, scroll up and make sure we have
[20:35] dark text 12 in the default RHI and the shader model six.
[20:40] Make sure it's enabled as well and it's not set to shader model five because shader model five
[20:45] has a lot of limitations and many features will not work with it.
[20:49] So now we are done with the project settings.
[20:52] Some of the options we enabled might require a restart.
[20:55] And if that happened, it will show a warning message.
[20:58] Press restart now on it and it will restart the project, re-combine the shaders for you
[21:04] and then the project will be ready.
[21:06] Now we are done with the project settings and we have to do a quick recap about this chapter.
[21:11] We went over the project settings.
[21:12] We discussed the difference between software ray tracing and the hardware ray tracing and
[21:17] the limitations of the software ray tracing.
[21:20] We enabled the project settings we need in order to use lumen and mega lights efficiently.
[21:26] Now we will go through the actual work which is discussing lumen at first,
[21:31] how it works, how should we use it efficiently inside UF5.


### Lumen Explained [21:35]
**Transcript (timestamped):**
[21:35] Now we will talk about lumen.
[21:37] Lumen is a dynamic global illumination and reflection system that is designed specifically
[21:43] for Unreal Engine 5.
[21:44] However, lumen has some inputs that depend on to get the best result out of it.
[21:50] First thing is the light direct intensity, which means the amount of rays or the intensity
[21:57] of the light source.
[21:59] The direct lighting is the first ray of light that hits the surface.
[22:03] And as any object in real life, when we have some light on it, it reflects or bounces some
[22:10] of them, depends on the object's properties.
[22:12] So this bounced lighting is called the indirect light intensity or the indirect lighting.
[22:18] It always has less intensity than the direct lighting as the surface absorbs a bit of the
[22:24] light rays.
[22:25] So when it's reflected, it doesn't have the same energy as before.
[22:29] There's also a third factor, which is the surface diffuse brightness.
[22:33] That means that the brighter the object, the more indirect lighting it will bounce and the
[22:38] darker the object, the less indirect lighting it will bounce.
[22:42] The surface diffuse in Unreal refers to base color value or the albedo.
[22:46] So these three factors you have to keep in mind when you are working with lumen, because
[22:51] when you have a very bright object, the calculations will be wrong.
[22:55] And the same goes if you have very dark objects.
[22:58] So this is a quick overview about lumen.


### Using Lumen [23:01]
**Transcript (timestamped):**
[23:01] Let's get back to the engine.
[23:02] If we want to try to see how lumen is working, we can go to shapes in the place actors menu,
[23:08] drag and drop a cube, just place it like this.
[23:11] You notice the shadowed area still have some bouncing light.
[23:15] I can show you quickly the difference between using lumen and not using lumen or disabling it.
[23:21] So I can go quickly to the project settings and go again to rendering.
[23:25] Give it a bit tight, smaller, scroll down to global illumination.
[23:29] We can set the lumen to none.
[23:32] And notice here the backside or the shadowed side of the cube.
[23:36] It's totally black right now.
[23:37] And this is with lumen.
[23:38] This is without lumen.
[23:40] It has a significant effect on the shadowed areas.
[23:43] Notice if we are going to increase the intensity, right now it's set to eight.
[23:48] I'm going to set it to 100.
[23:50] You should notice a difference in this shadowed area.
[23:53] So there is a difference between one and 100.
[23:56] Notice if we turn lumen to none, it's totally black.
[23:59] And now what happens if we try to increase the in dark light intensity?
[24:04] We can keep the intensity to 100 and we can try at 10 in the in dark light intensity.
[24:09] Notice it's very bright.
[24:11] So you can control the amount of ounces or indirect lighting specifically for each light actor.
[24:17] Now we are going to jump to mega lights and start using it inside the engine.


### MegaLights Explained [24:22]
**Transcript (timestamped):**
[24:22] So what is mega lights?
[24:23] Mega lights is a new lighting path that is using the direct lighting method.
[24:28] It's designed to work with aerial lights because they have ray traced shadows.
[24:33] And the goal of it is to produce soft dynamic shadows using ray tracing.
[24:39] And at the same time, keeping it performant, which is amazing, you will be able to use
[24:44] thousands of lights in your scene without affecting the performance as before.
[24:49] Of course, it has a downside of minimizing the light and shadow quality because of
[24:54] amount of overlapping lights at the same pixel.
[24:57] Also mega lights is a board the volumetric fog shadowing and you can use media to produce
[25:04] very soft dynamic lights in your scene.


### Using MegaLights [25:06]
**Transcript (timestamped):**
[25:06] So in order to use mega lights, we can try it with the direct light.
[25:11] What I'm going to do is I will set it to movable and I will duplicate it and get
[25:16] as many instances as I can.
[25:19] I will hold alt on the keyboard and drag the light.
[25:22] So now it's duplicating the light actor, then select these four lights, drag again.
[25:28] Now I'm going to duplicate them in front of it, duplicate again, again, again.
[25:33] Now we can check the performance or the frame rate of the scene that is running right now.
[25:39] We can quickly do that by going to view board options and we have show FPS.
[25:44] It's around 90 or 100 FPS.
[25:47] Select all of these lights again, hold alt, drag them.
[25:51] You may notice that the performance is still running around 100 FPS.
[25:55] And that's because we are using mega lights as we have enabled it in the project settings.
[26:00] We can check the state of the mega lights by selecting the lights, all of the lights here.
[26:06] You can see it's around 128 actors, which is a lot of actors.
[26:11] We can go down in the details panel, click on advance to show more options.
[26:16] Scroll all the way down until you find allow mega lights.
[26:20] It's enabled because we have enabled it in project settings.
[26:23] Press on G, get into game view and notice the difference when we disable allow mega lights.
[26:29] It's now around 100 FPS.
[26:31] Now it's around 80 FPS.
[26:34] This is before and after 10 milliseconds versus 12 milliseconds, which is a lot.
[26:39] We can do an extensive testing by duplicating all of these lights again and do it like this.
[26:46] And now it's running around 60 FPS and it's without mega lights.
[26:51] You may have different number.
[26:53] So I'm going to enable it right now and notice it's back to around 90 FPS,
[26:58] which is amazing.
[26:59] And for this kind of many lights in the scene, that's insane.
[27:03] So now we have the option to control the mega lights on and off using each light actor.


### Raytraced Shadows Vs. Virtual Shadow Maps (VSM) [27:09]
**Transcript (timestamped):**
[27:09] And also we can select the shadowing method.
[27:12] There is two methods, which is ray tracing and virtual shadow maps.
[27:15] We have to try to get an object.
[27:17] I'm going to use this cube.
[27:18] Notice how soft these shadows are.
[27:21] If I'm going to select all the lights again and change the shadowing method to
[27:27] virtual shadow map, it changes, but the ray tracing shadow is much softer.
[27:31] And it's recommended to keep it at ray tracing default is referring to the project settings.
[27:36] So if you have set it to virtual shadow maps in the project settings,
[27:39] the default will be virtual shadow maps in the light actors.
[27:42] So in order to make sure you are using the proper one, make sure to keep it to ray tracing.
[27:48] Notice what will happen if we turned on mega lights.
[27:51] And now you can see that there is like an artifacts.
[27:54] So keep in mind to check allow mega lights.


### MegaLights Best Practices [27:57]
**Transcript (timestamped):**
[27:57] And also there is another way to control it, which is using post process volumes.
[28:02] So to get it quickly, we can go to VFX panel in the place actors drag and drop a post process
[28:08] volume press G to see the outline of it, scale it like this, duplicate this object right here.
[28:15] Now we have to make sure we are selecting the proper post process volume,
[28:19] go to rendering features and turn off mega lights.
[28:22] You'll see the difference in the frame rate.
[28:24] It's now turned to around 50 FPS, we can scale up the queue to see much better result and go back
[28:32] to the post process volume, scroll down to mega lights.
[28:35] Notice what's happening when we are turning it on and off and both the result of shadowing
[28:41] and the FPS number.
[28:43] And if we kept it off, when we go outside this post process volume, the effect will be back.
[28:49] Pay attention to the FPS number.
[28:51] We go outside, it's turned to 90 FPS.
[28:54] So it's inside, outside.
[28:58] That's because this post process volume is only affecting this area.
[29:02] And notice when we are a bit far from it, the shadowing is back on the object.
[29:09] And when we go again inside the bounds on the volume getting turned on and off based on our camera
[29:17] location, if it's inside or outside the boundaries of the post process volume.
[29:22] So this is another way to control mega lights and best cases, maybe a global post process
[29:29] volume with mega lights turned on so you can save performance for all the scene and get much
[29:35] better frame rate.
[29:36] And if you are seeing lower quality because of the limitation of mega lights, you can set a
[29:42] specific post process inside a specific region and turn off mega lights and also make sure to
[29:48] not have a lot of flights in this region just to save performance.
[29:52] But usually you may have to keep it on and it's very good to deal with the rect or area lights,
[29:58] as you can see the difference in performance.
[30:01] It's around 60 and now when we just go outside it, it's around 90, which is a big difference.
[30:08] It's around six or seven milliseconds.


### Outro [30:10]
**Transcript (timestamped):**
[30:10] So yeah, that's it for this tutorial.
[30:12] I hope you enjoyed it.
[30:13] We went over a lot of topics and make sure to stay tuned for more advanced tutorials.
[30:18] See you next time.



---

## Captured Frames

- [13:20] tutorials/frames/everything-you-should-know-about-megalights---unreal-engine-55-lighting-tutorial/frame_000.jpg
- [19:56] tutorials/frames/everything-you-should-know-about-megalights---unreal-engine-55-lighting-tutorial/frame_001.jpg
- [23:38] tutorials/frames/everything-you-should-know-about-megalights---unreal-engine-55-lighting-tutorial/frame_002.jpg
- [26:10] tutorials/frames/everything-you-should-know-about-megalights---unreal-engine-55-lighting-tutorial/frame_003.jpg
- [27:30] tutorials/frames/everything-you-should-know-about-megalights---unreal-engine-55-lighting-tutorial/frame_004.jpg
- [28:45] tutorials/frames/everything-you-should-know-about-megalights---unreal-engine-55-lighting-tutorial/frame_005.jpg

---

## Structured Notes

### Core Technique
[UE5.5 required] Complete beginner-to-working setup of MegaLights: the exact Project Settings chain (Lumen GI + reflections, hardware ray tracing, MegaLights under Direct Lighting, Virtual Shadow Maps, DX12/SM6), which light types benefit (Rect/area lights with ray-traced shadows), and the three control levels — project-wide, per-light `Allow MegaLights`, and per-region via Post Process Volume.

### Summary
Karim Yasser's ground-up MegaLights course: from engine install through a live stress test where 128+ movable rect lights run at ~90–100 FPS with MegaLights on versus ~60 FPS off (10ms vs 12–16ms). Explains the prerequisites people miss — MegaLights requires hardware ray tracing (software Lumen users can't use it at all) — plus Lumen's three input factors (direct intensity, indirect intensity, surface diffuse/albedo), ray-traced vs VSM shadow softness, and using PPVs to scope MegaLights on/off per region.

### Key Steps
1. **Prereqs:** UE 5.5+ only (MegaLights doesn't exist earlier); GPU must support ray tracing — without HWRT, software ray tracing runs Lumen but **cannot run MegaLights**.
2. **Light actor fundamentals:** Point (omnidirectional, expensive), Spot (cone, cheaper directionality), **Rect/area light (studio-style; uses ray-traced shadows — the type MegaLights is designed for)**. Set every light to **Movable** (static = baked lightmaps, stationary = hybrid that can't move at runtime, movable = fully dynamic GPU lighting).
3. **Project Settings → Rendering:** Global Illumination = **Lumen**; Reflection Method = **Lumen** (not None/Screen Space); **Use Hardware Ray Tracing When Available = On**; Ray Lighting Mode = Hit Lighting for Reflections (higher quality on reflective surfaces; Surface Cache is the cheaper default); High Quality Translucency Reflections = On (glass/water); Software Ray Tracing Mode = Detail Tracing; Ray Traced Translucent Reflections = On; **Direct Lighting → MegaLights = On** (grayed out until Support Hardware Ray Tracing is enabled); Shadow Map Method = **Virtual Shadow Maps**.
4. **Platforms → Windows:** Default RHI = **DirectX 12**, **Shader Model 6** (SM5 blocks many features). Restart when prompted (shader recompile).
5. **Lumen mental model:** result = direct light intensity + indirect (bounced) intensity + surface diffuse brightness (albedo) — extreme-bright or extreme-dark albedos break the GI math. Indirect Lighting Intensity is adjustable per light actor (demo: intensity 100 with indirect ×10 visibly floods the shadow side of a cube).
6. **Stress test workflow:** Alt-drag to duplicate a movable rect light into arrays (128+ actors); Viewport Options → Show FPS. With MegaLights: ~100 FPS; per-light Details → Advanced → **Allow MegaLights** off: ~80 FPS; doubling lights again: 60 FPS off vs ~90 FPS on.
7. **Shadow method per light:** Ray Tracing vs Virtual Shadow Map — ray-traced shadows are visibly softer and are the recommended pairing; "Default" inherits the project setting, so set lights explicitly to **Ray Tracing** when using MegaLights (VSM + MegaLights produces artifacts).
8. **Region control:** Post Process Volume → Rendering Features → MegaLights on/off applies only inside the volume bounds (camera-based). Best practice: MegaLights ON globally for performance; scope it OFF in a small PPV only where its quality limits show, and keep light counts low there.
9. **Known limits:** experimental; quality degrades with many overlapping lights on the same pixel; aids volumetric-fog shadowing for soft dynamic lights.

### UE Systems / Blueprints / Settings
- Project Settings → Rendering: GI = Lumen, Reflections = Lumen, HWRT On, Hit Lighting for Reflections, High Quality Translucency Reflections On, Detail Tracing, RT Translucent Reflections On, MegaLights On, VSM
- Platforms → Windows: DX12 RHI + Shader Model 6
- Per-light: Mobility = Movable; Details → Advanced → Allow MegaLights; Shadow Method = Ray Tracing (not Default/VSM)
- PPV → Rendering Features → MegaLights (region-scoped)
- Measured: 128 rect lights ≈ 100 FPS on / 80 FPS off (10 vs 12ms); 256 ≈ 90 on / 60 off
- Editor: Alt-drag duplicate, `G` game view, Viewport Options → Show FPS, Window → Load Layout → UE4 Classic

### Difficulty
Beginner–Intermediate

### UE Version
UE 5.5 (MegaLights experimental; prod-ready 5.8 — the settings chain is unchanged)

### Tags
lighting, lumen, megalights, rendering, post-process, beginner, intermediate, ue5-5

---

## Related Entries
- [It Took Me 7+ Years To Get Interior Lighting That Easy in Unreal Engine 5](it-took-me-7-years-to-get-interior-lighting-that-easy-in-unreal-engine-5.md) — same author applying MegaLights in a real interior scene, plus Lumen flicker/fog CVars
- [How I Use Lumen in AAA Projects | Unreal Engine 5](how-i-use-lumen-in-aaa-projects-unreal-engine-5.md) — same author's deeper Lumen quality guide (HWRT vs SWRT decision, PPV knobs)
- [The Perfect Sky Light in Unreal Engine 5](the-perfect-sky-light-in-unreal-engine-5.md) — companion global-lighting setup from the same author
