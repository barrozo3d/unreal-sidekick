---
title: Unreal Engine for Filmmakers - How to Make your Lighting CINEMATIC
source: YouTube
url: https://www.youtube.com/watch?v=SMCTeoj9YaA
author: Boundless Entertainment
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic/
frame_count: 9
---

# Unreal Engine for Filmmakers - How to Make your Lighting CINEMATIC

**Source:** [YouTube](https://www.youtube.com/watch?v=SMCTeoj9YaA)
**Author:** Boundless Entertainment
**Duration:** 10m55s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro & Gemini Update [0:00]
**Transcript:** What's going on guys Sam here? I know it's been a while and I'm sorry  I've been away, but in today's video I have a couple of huge announcements for you  So the reason that I've been pretty absent from both the channel and the online community in general is because I've been  Finishing up my first major short film Gemini. I'm super excited to finally have it finished  I'm super happy with it and I can't wait for you all to see it  But the reason that that's good for you guys is because I've learned a ton by working on this project  And I really wanted to share it with you. So that's why I've created a brand new course in Unreal Engine 5

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic\frame_000.jpg

### Unreal Engine 5 Filmmaking Course [0:27]
**Transcript:** Which goes over the industry standard pipeline for creating a visual effect shot using Unreal  From building a full scene inside of Unreal from the ground up to rendering that scene with the most cinematic render settings possible  As well as including a ton of data to use in the compositing stage of your workflow all the way to utilizing all that data inside of your  Compositor in order to get the best possible result out of your Unreal Engine renders  So the course really is a full guide to the post production and visual effects workflow with Unreal Engine and you guys don't want to miss it  So check out the link below for more information on that and I can't wait to see you guys over there at boundless-resource.com  So into the main part of this video, which is an excerpt from the course that I just mentioned

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic\frame_001.jpg

### Basic Night Scene Lighting Styles [1:09]
**Transcript:** What I want to talk about today is how to light a night scene inside of Unreal Engine and there's a lot of different ways of lighting a night scene  a lot of different styles in today's cinema especially from the softer more overcast night scene look to a harder more full moon type lighting style  So in this video, I'm gonna be covering how to light your night scene with that kind of harder full moon type of look  And the meat of the video is going to be going into how to get god rays or light shafts in Unreal Engine 5 for your night scene  So part of what's important about a night scene is your sky or lack thereof

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic\frame_002.jpg

### Adding a Sky [1:47]
**Transcript:** So adding an hdri texture of the night sky and then reducing its intensity is a great way to do that  And you can see me doing that quickly here  That's going to set the tone of your scene and it's gonna give your audience the information right off of that that they're looking at a night scene  Okay, so basically what I have in my scene here is I just have some fog cards that I've added and I have a couple of

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic\frame_003.jpg

### Shooting from Shadow & Lighting Theory [2:05]
**Transcript:** Point lights that I've added to my scene we're not really gonna go over that today  What I'm gonna be focusing on is the directional light and the exponential height fog and how to get  Nice light shafts in your scene. So the first thing that we're gonna do is kind of figure out our basic lighting setup  So I've got my directional light and I'm just gonna pull it into my scene here off the bat  We have some pretty flat looking lighting what I'm gonna do is  Go into my cine camera actor and I can start  Rotating this around and you do that by hitting E on the keyboard  It's gonna bring up this rotation setting and you can start moving your light around in your scene  So we need to figure out where we want to light the scene from in the original example. I kind of did something like this over here  To get these nice lines and these shadows coming across and you can see the  Direction of the light source from this arrow right here and that's the original lighting option  I chose but you can also light it from over here  But what you want to keep in mind here is kind of the theory of lighting your scene and generally you want to shoot from the shadow side  So what that means is my ligh...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic\frame_004.jpg

### Directional Light Settings [4:30]
**Transcript:** So if I go in here, this is a really hard edge and what we can do to modify that is we can change this source angle  And that's basically just going to increase the softness of your shadows  And so if I turn that up a little bit you can see what's happening there  I'm going to leave this somewhere around two and a half  We have our intensity. I might just crank this up to like 13 and  What I really want to talk about here is our indirect lighting intensity  So what this is is it's basically control over the lumen  Feature in Unreal Engine indirect lighting is light that comes into your scene and then bounces around onto different objects in your scene  And if you look here if we set this to zero we have no  light that's bouncing off of any object in our scene onto this building for example in order to enable that  We can turn our indirect lighting intensity up and you can immediately see what's happening here  Now we suddenly have some nice lighting that is bouncing up onto the other objects in our scene  It's bouncing in a realistic way. So I won't get too much into this  But you can at least see that now, you know, this lighting is bouncing off of the ground off of this building ...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic\frame_005.jpg

### Exponential Height Fog [6:25]
**Transcript:** The next thing that I'm going to add is our exponential height fog  It's just going to add a little bit of volume into our scene. So if I turn this up to something like one  You can see that we need to modify our fog in scattering color  We're just going to turn this up all the way to white  So now you can see this is going to add some depth into our scene and I go for that a lot in the course  Adding fog is going to give our eye information about the depth of our scene  So we can tell that this object is further away than this object  And that's something that really helps as a cinematographer or anybody that's creating a 3D render like this  So I'm just going to set up these fog settings really quickly so I can show you guys our fog height fog is going to be two and  That's just going to eliminate some of the fog up in the tops of our buildings  We're going to go down here and we're going to turn on volumetric fog and that's going to just have a more realistic  reaction between the light that's coming into our scene and the fog that we have set up in our scene  Then we actually have control over the distribution of that light throughout our scene  So if we turn this number up you...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic\frame_006.jpg

### Adding God Rays [8:10]
**Transcript:** Now we can go down here and turn on light shaft occlusion and that's going to allow us to see those light rays  Even better because objects that are between us and the directional light are going to acclude that lighting and so we're not going to be able to see  The fog as well unless we're looking directly at the light and that means that we can see these nice god rays in here when we're obscured behind an object  So if we go into our cine camera actor what's important about lighting a night scene like this if you want to add those god rays  You're going to need a couple of things so you need a darker background and that's going to be provided right here by  This shadow area and also this dark sky that we have back here  So you can completely leave out the sky or you can enable an hri texture, which is what I did  You know, that's kind of up to you  But if you see now if we move our light around  You can see that we're getting those nice god rays coming into our scene and the more directly we're looking towards the light  The more we're going to see those god rays  So if I go directly from the side you can't really see the god rays if you go over here like this now  We're starting...

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic\frame_007.jpg

### Recap & Wrap Up [10:00]
**Transcript:** I hope you found this helpful and I hope that you're able to use this in your own projects  Lighting is one of the most important things in your scene and it's going to add a ton of realism  And it's going to add that cinematic quality more so than almost any other aspect of your scene and lighting is honestly one of the biggest  Improvements that has gone into Unreal Engine 5 with the addition of Lumen  So you're really going to want to use that to its max potential  So once again if you like this video definitely head over to my website balance-resource.com  The link is in the description and check out the course over there  I think you guys are really going to find this valuable and I can't wait to hear what you think of it  So thank you guys for watching  I'm glad to be back and don't forget to like comment and subscribe for more videos like this  So have a good one guys

**Frame:** tutorials\frames\unreal-engine-for-filmmakers---how-to-make-your-lighting-cinematic\frame_008.jpg


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
