---
title: How Unreal 5.4 Changes Filmmaking
source: YouTube
url: https://www.youtube.com/watch?v=NiOgmvMBcxk
author: Josh Toonen
ingested: 2026-06-18
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-unreal-54-changes-filmmaking/
frame_count: 8
---

# How Unreal 5.4 Changes Filmmaking

**Source:** [YouTube](https://www.youtube.com/watch?v=NiOgmvMBcxk)
**Author:** Josh Toonen
**Duration:** 9m38s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### What's inside Unreal 5.4? [0:00]
**Transcript:** Unreal 5.4 just came out with huge updates for filmmakers and visual effects artists.  Now you can make music videos, commercials, and freelance work using Unreal 5 for free.  Now you don't need Cinema 4D, After Effects, and Photoshop.  Now you've got motion design and text tools that render all in real time.  And rendering just got a huge upgrade that gives your indie VFX workflows all the tools and power of a big budget visual effects studio.  And lastly, you can use this new Nanite update to immediately improve your environment.  If you don't know me, what's up? My name is Josh Tunin and for the last eight years,  I've worked in Hollywood visual effects.  As a visual effects artist and supervisor on movies like Star Wars,  Dungeons & Dragons, and across the spiderverse.  And I started using Unreal Engine every day on set for the virtual production  of Netflix's Avatar the Last Airbender.  So let's break down my top three updates that you can start using in Unreal 5.4.

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_000.jpg

### C4D in Unreal 5 - The Motion Design plug-in [0:50]
**Transcript:** Now you can add text, in titles, and create motion graphics for TVs,  documentaries, and logos.  And there's easy animation tools and presets to add to anything in your scene.  Working with text and vectors used to be a pain in Unreal 5.  And a lot of people would flip flop between Cinema 4D and Unreal.  But now it's super easy using the motion design plugin.  Just enable the motion design plugin and you'll have access to this new motion design tab.  Now you can create 2D or 3D text by selecting your fonts directly in Unreal.  And you can add vector logos by importing .sbg files.  It's never been easier to create movie titles,  logo reveals, or any type of motion graphics work easily and haul in real time.  You can even create custom graphics using their shape tools and rulers  to create title slides just like this.  But to create 3D graphics, all you need to know are the Cloner and Effector tools.  Cloners are an easy way to take a collection of objects  and clone them into new groups or shapes.  Cloners create these 3D shapes, but effectors allow you to animate and modify these.  So now you can create real time procedural animation  by dragging these effectors around or animating...

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_001.jpg

### How Material Designer works [2:40]
**Transcript:** For you Adobe users, now you can edit any material using layers just like in Photoshop.  Instead of using the material node graph, now you can build out materials by adding in new layers,  gradients, and masks that you can edit all in engine and bring your motion graphics to life  just like in After Effects.  But once you learn the tools, you'll render faster inside of Unreal,  and you can add 3D into your arsenal.  So you can design and create all in real time.  As a friendly reminder, if you want to import logos and graphics into Unreal,  make sure Unlit Mode is checked if you want that logo to be unaffected by the lighting.  Otherwise, if you want that logo to react to lighting just like it's in that real 3D scene,  then just uncheck Unlit Mode.  So now you can design and animate your own motion graphics,  saving you more time to be creative.

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_002.jpg

### Update to Nanite (Add Displacement in your Material!) [3:30]
**Transcript:** The next update you have to start using is Nanite.  Specifically, Nanite Tessilation.  Nanite allows you to put billions of polygons in your scene at the same time.  But Nanite got a huge improvement with Unreal 5.4 with Nanite Tessilation.  Now you can dynamically change your displacement in real time, in the viewport.  Displacement takes a 2D image and adds 3D detail so your objects look good up close.  Using this method, you can create better looking terrains just like in this demo from Marvel 1943.  Rise of Hydra.  I tried this out in my Dune project file,  and now I can modify and control this displacement in real time and change it per shot.  So to enable this feature, you just need to file these four steps.  First, go to your plugins and enable Nanite Displaced Mesh.  Next, go into your config folder and open up DefaultEngine.i and I.  I'll leave this text in the description, but just copy and paste these two command variables  into your renderer settings and then press Save.  And make sure to close down and reopen your project.  And then the last two steps for your 3D object in your scene,  just make sure to right click on this mesh and enable Nanite in your content browser...

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_003.jpg

### Other Exciting Updates in UE5.4 [4:55]
**Transcript:** Lastly, I want to cover the huge update they made to rendering in Unreal.  But before that, I want to share some other highlights that you don't want to miss inside of Unreal 5.4.  This first update will let you add animation to any character even if you're not an  animator yourself. Using the new one-click Retargeting update, now you can just right click on any  animation inside of Unreal. And it'll automatically transfer this animation to any other character  in your project. So now you can download any animation from MixMo.com, right click it inside  of Unreal and transfer it over to any character. The next update is Motion Matching, which will give  you AAA level animations and transitions to your characters have realistic weight and physics.  This project file isn't available yet, but it'll be free in the upcoming months so you can  deconstruct this and apply these techniques to your own films and projects. For you visual effects

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_004.jpg

### Movie Render Graph [5:45]
**Transcript:** artists and filmmakers, rendering just got a huge upgrade with the new movie render graph.  You can turn your complicated render settings into easy customizable menus.  This will give you all the power of a big budget visual effects studio all from your home computer.  So to switch over to the movie render graph, it's really easy. Inside a sequencer, you're going to  do the same thing and press on this little movie clapperboard to launch your render. But instead of  clicking here to change our movie render cue settings, let's click on this little arrow and replace  this with a graph instead. Now when we click on our settings, we have a new menu which is the default  render graph. Now all of our render settings are in this top graph here in our warm-up settings,  global game overrides and global output. All the defaults you're used to are exactly the same  and to change your file path and resolution, we just go to our global output settings and change  the directory or final resolution. Now if you want to add an extra layer into our outputs tab,  all we have to do is go on the left hand side and press on the plus icon to add another output.  Now we can rename this to data passes and...

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_005.jpg

### Make Custom Menus in MRG [7:35]
**Transcript:** next to variables and now we have all the data types that we're used to. But the really fast way  to modify any setting and turn it into a variable can be done by right clicking. So if I wanted to make  my output directory customizable, all I'd have to do is right click on our global output settings,  expose the output directory as a new pin and then just right click on here and promote this  to a variable. Just like that. Now the biggest reason everyone's upgrading to the movie render  is all the tools around isolating different objects in your scene. But personally, I like to use  crypto mats or object IDs which work in Newq or After Effects as a way to isolate any object inside  of your scene. This way you're not restricting yourself and baking it down. You can change up  these mats and grab an ID for any object in your entire scene. But there are some huge caveats  with the movie render graph that you have to know. The first is that landscapes are not fully  supported. Spongebobal actors aren't supported as well. So any object that has that little lightning  bolt icon next to it won't render out using the movie render graph. You should also know most people  aren't talking abou...

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_006.jpg

### Overall First Impressions and Final Thoughts [9:00]
**Transcript:** taking advantage of these new features right away, I wouldn't recommend upgrading to Unreal 5.4  just yet. Personally, I'll just be upgrading to take advantage of the motion design tools and  make sure to subscribe if you want more tutorials on how to use it. But for everything else,  I'll be sticking with Unreal 5.3. Let me know in the comments what you think is the most exciting  feature and I might cover it in the next video. Otherwise, if you're new to Unreal, check out our  free Unreal 5 Crash Quartz over at Unreal for VFX.com slash Crash Quartz and make sure to subscribe  to the channel for more Unreal filmmaking and visual effects breakdowns just like this. Thanks for  watching and I'll see you next time. Peace.

**Frame:** tutorials\frames\how-unreal-54-changes-filmmaking\frame_007.jpg


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
