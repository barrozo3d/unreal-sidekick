---
title: Motion Capture isn't just for Hollywood any more...
source: YouTube
url: https://www.youtube.com/watch?v=hoCoa8gMP-M
author: Josh Toonen
ingested: 2026-06-18
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/motion-capture-isnt-just-for-hollywood-any-more/
frame_count: 10
---

# Motion Capture isn't just for Hollywood any more...

**Source:** [YouTube](https://www.youtube.com/watch?v=hoCoa8gMP-M)
**Author:** Josh Toonen
**Duration:** 18m26s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Motion Capture for Indie Filmmaking [0:00]
**Transcript:** What if you could start making your own sci-fi films and action scenes at a fraction of the time?  Well now you can, using motion capture. Believe it or not, any one of you can start using motion  capture and start making Hollywood-level films just like this from home, saving you hundreds of  hours and getting better results than having to painstakingly keyframe everything yourself.  I spent the last decade working in Hollywood visual effects, and the last two years making animated  films an unreal engine. But it wasn't until I made this samurai sword fight that I was able to  brew my own sci-fi action scenes to life faster than ever. So in this video, you'll learn all the  shortcuts in my exact process to go from an idea to final animation, even if you're not an  animator yourself. You'll see just how streamlined this workflow is, and why motion capture isn't just  for big studios anymore. It's now a tool that all of us filmmakers can actually use.  Now the traditional way of making animated films is you start with a storyboard,  then you make your pre-vis, and then you make the final result. In each step it uses a different  software. But with Unreal Engine 5 we can go from story...

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_000.jpg

### Four stages to bring any film to life [1:50]
**Transcript:** So in this lesson we'll cover the four stages that every motion capture production goes through.  We'll start with an overview and then dive into each step, and it all starts with the build.  Start out by collecting inspiration and building your film sets and environments along with your  3D characters. The second step is motion capture, where you'll work with actors together on set to  create a real performance, and then you'll need to clean up your motion capture data to get a clean  animation. Then we'll start the filmmaking cycle. This is when you set up your cameras,  assemble your first edit, and then improve the animations through the camera lens. Then you can  decide what parts of your motion capture you need to improve and upgrade, which is super easy when  you have a control rig. And lastly, when your edit is locked, we'll move on to lighting and effects,  and we'll add in the finishing touches and composite our renders to make them look photo real.  Let's talk about building and sourcing your 3D characters. In our case, we started from an

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_001.jpg

### Build - 3D characters and environments [2:44]
**Transcript:** existing 3D model to save us some time on the first version and start right away with a rig.  But we did make some major changes to the 3D model by creating a custom helmet to match the  original concepts and references, and we completely replaced the materials and textures and created  our own in Substance Painter. Now most people skip over this super important step. Look development.  Once you've created your textures in Substance Painter, your character isn't done just yet.  You need to preview your characters under real lighting conditions, and we want to stress test  the materials to make sure they'll hold up under any situation. The easiest way to do this is to  create a turntable. Put your character in the middle and set up some lights, and rotate your asset  around by 360 degrees, so you see every side of your object. Then do a second pass where you  rotate the lights. This will start to reveal if anything looks artificial or fake in your materials.  And if there's anything not looking right, just continue adjusting your textures and materials  until it looks true to life. Next, let's talk about motion capture and what it takes to get great

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_002.jpg

### Budget friendly Mocap options [3:44]
**Transcript:** results yourself. Now there's many different options for motion capture, ranging from completely  free by just using your webcam or your iPhone, all the way to dedicated motion capture studios,  which are tens of thousands of dollars per day. But if you're on an indie budget,  I would recommend Rococo. It's what we use to shoot the motion capture for this short,  and we use Rococo smart suits and smart gloves to capture the performance for our sword fight.  Now, why I went with Rococo is that we could capture two suits at the same time,  and by using their smart gloves we could actually get hand animation, which can be pretty tricky  and time consuming to do yourself, especially with characters holding swords and weapons.  Now if you want to jump into the action and make your own sci-fi films yourself, Rococo is awesome  enough to give every one of you watching this video a discount store wide. Just use coupon code  unreal vaffx at checkout, and you'll get an extra 5% off your entire order. I'll leave a link  down below for the bundle we used on this exact project. Now if you're using a Rococo system on set,

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_003.jpg

### The perfect motion capture workflow [4:42]
**Transcript:** all of the data is transmitted from the suits directly into Rococo studio, and it's connected  by using a Wi-Fi router. Now we're not using that for internet, modern day routers are insanely  fast at sending data between devices. The easy way to get started in Rococo studio is by creating an  actor profile for each actor wearing a smart suit. Here you can enter in the height for your actors,  and pick whether they're male or female body types, and you can specify any measurement so your  skeleton perfectly matches your actor. We created our two actor profiles, and then when we created  a new project, you simply add these actors into your scene, and you connect your smart suit and  smart gloves. We started every single take by having one of our actors clap their hands so we could  align the motion capture data with the video and audio tracks. And to keep things organized,  we created a folder for each setup and a take number for each attempt. In between each take, we would  recalibrate our motion capture suits to get the best results possible. Just press the recalibrate  button at the top of Rococo studio, and your actors just need to stand still with their hands  by their side for ...

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_004.jpg

### Copy your animation to new characters [11:03]
**Transcript:** thing I did was I took the Rococo animations and I put them inside of the environment. Then,  I would add a sword onto the character and set up a camera so I could start thinking of new  angles and interesting shots even with this basic character. But, if you want to transfer your  Rococo animations onto your character, the next step is retargeting. We need to retarget the  animations from our Rococo rig to our character rig. So, I imported all of my characters and  animations into Unreal, including the Rococo skeleton character, and then I created retargeting  assets for both characters. This way, I could preview all those animations on our samurai characters,  and even before we had our finished model and our finished textures, I could preview the animations  on the final rig. Now, once our motion capture is imported and we've done our first pass of retargeting

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_005.jpg

### Filmmaking cycle on Unreal Engine 5 [11:52]
**Transcript:** animations, that's when the filmmaking cycle begins. We'll start creating cameras and rendering  our shots, then dropping those into our edit, and then jumping right back into Unreal to adjust and  animate our characters in camera. And we'll do this for every single take that has an interesting  performance. Now, the goal at this stage isn't just to look at your motion capture data, it's to  assemble your first edit. In filmmaking, if you don't have an edit, you don't have anything.  We need to build a timeline with video and audio, and the way to do that is to render out our motion  capture data through a camera. So, the typical setup is I would add both characters into sequencer,  then I would find motion capture performances that are interesting and assign those takes onto each  character and align them in the center of my environment. Then I would create multiple cameras  with different focal lengths. Typically, I'll create at least one wide shot, which would have a focal  length of 20 to 40 millimeters, and then I would create a close-up for each character, and for the lens,  you something between 50 and 150 millimeters. Then, I'd try to find one special moment and create a  c...

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_006.jpg

### Editing your Animated Film [14:48]
**Transcript:** together, and that's why our goal is to get there as fast as possible. Now because we rendered out  these really long takes, when we drag in our renders, it's just like getting footage from onset.  You can bring in each take, watch through the footage, and clip out any selects or highlights  from the cool moments that you see, and assemble the best ones together. And it's super important to  bring in basic music and sound effects as early as possible too. In our case, we were making a  music video, so we had a soundtrack that we could start pacing our shots to. Now I never expect this  first version to be perfect. It's just your first draft, but once you find some camera movement that

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_007.jpg

### How to Edit + Improve Your animations [15:21]
**Transcript:** you're happy with, and you find a nice flow and pace to your film, you can jump back into Unreal and  make adjustments. Where we'll improve our animation, or come up with new ideas and adjust our animation.  Once you've decided on the right camera moves and frame ranges, we can lock our edit and improve  our animation and motion capture inside of Unreal by using control rigs. Using the same exact  workflow we used before. We'll start out with our animation clips, and then we would right click  on our asset, and bake this animation onto a control rig. Then we'll use additive tracks and the  curve graph editor to perfect our animation. And then the cycle continues. Keep watching your edit,  and update your cameras, and character animation until you have a version of your edit that has the  right pace and flow between each shot. At this stage, just focus on the composition and the flow  across your entire film. Once everything is locked, only then should you move on to the next step,

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_008.jpg

### Adding Lighting + FX in cinematics [16:16]
**Transcript:** lighting and effects. It's important to save this step until the end, and I honestly wouldn't  worry about lighting or effects whatsoever until you have a first draft of your edit.  Lighting will change the mood of your film, but ultimately it won't change the story. So there's  no point in lighting before the camera and animation has a great first pass. Because if you end up  moving the camera, your lighting will look totally different. At any point, you can press play and drag  your lights across your scene, and I really like this method of finding new ideas and new lights  in a really interactive way. And from this point forward, filmmaking in Unreal is a very iterative  process. Keep improving your shots and improving your film one version at a time. On War of Being,  we didn't finish our character assets until the very end. We continued updating the cloth,  the helmet, and physics assets as we went. And anytime there was an error in our render, we would  update that physics assets, and now we have the improved version for the next shot too.  And when you go to make your final renders, the only thing that changes in the end is you'll  increase your render settings and use a hig...

**Frame:** tutorials\frames\motion-capture-isnt-just-for-hollywood-any-more\frame_009.jpg


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
