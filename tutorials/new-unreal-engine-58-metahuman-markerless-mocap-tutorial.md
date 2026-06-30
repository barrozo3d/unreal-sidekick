---
title: NEW Unreal Engine 5.8 MetaHuman Markerless Mocap Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=b2i1aZbhxAU
author: Smart Poly
ingested: 2026-06-23
ue_version: "UE5.8"
tags: [metahuman, mocap, markerless, live-link, body-tracking, facial-capture, retargeting, plugin, workflow, beginner]
extraction_status: complete
frames_dir: tutorials/frames/new-unreal-engine-58-metahuman-markerless-mocap-tutorial/
frame_count: 4
---

# NEW Unreal Engine 5.8 MetaHuman Markerless Mocap Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=b2i1aZbhxAU)
**Author:** Smart Poly
**Duration:** 14m55s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello guys welcome back to another video. What you're looking at right now is the brand new Unreligion 5.8 Mettahumin, Markylis, Motion Capture Plugin inside of Unrel Engine 5.8. On the left side of my screen I'm simply recording myself with an iPhone camera and as I move my arms as I turn around and if I gesture with my hands like I'm talking maybe this can be an NPC animation we could have you know like an interact where I'm grabbing an item something like that. Unreligion is automatically converting this video footage into real character animation and the crazy part about it is that there's no motion capture suit, there's no markers, no expensive mocap studio involved and the regular video gets processed directly inside of Unrel Engine and in this video we're going to take a look at how the plugin works, how easy is it to actually set up and all the results actually good enough to use in your games and projects. And if you were new here to the channel my name is smartpoly I make all sorts of Unrel Engine news content and tutorials to make sure you drop a like and subscribe for more future videos. Also before we get into the video I just release my new Unreligion Masterclass course bundle. I just launched a brand new Unreligion Masterclass course this bundles together all of my courses showing you how to make games inside of Unrelingion. This Masterclass course has over 150 plus hours of learning content and I will show you how to make eight different games from complete scratch. You'll master multiplayer networking survival mechanics, AI, user interfaces, game optimization, mobile development and so much more included in the masterclass bundle or all the completed game project source files so you can use them as a reference while you learn or if you just want the completed game project we have you covered. Check out the Unrel Engine Masterclass link in the description below and with that being said let's get right back to the video. So the first thing that you'll need to do is create a brand new Unrel Engine 5.8 project. So again this will only work with 5.8 and above then you want to go to your edit plugins and search for metahuman. You'll need to enable the metahuman animator plugin, metahuman animator markless motion capture, metahuman core tech, metahuman core and L, metahuman creator, and then metahuman live link and metahuman SDK. Now if you don't see some of these plugins in here what you'll need to do is when you're downloading Unreligion 5.8 you want to in your options make sure that you download the metahuman creator core data over here. Okay you hit this little checkbox and it will include that in the download. Now if you already downloaded 5.8 all you have to do is come to the launcher, click the options here and modify, click the checkbox, click apply and that will go ahead and download that metahuman core data which includes the metahuman creator and all the assets that you'll need for this video. Okay so go ahead and download that and now create a brand new project and you should see these plugins. So once you enable the plugins you'll restart your project, I've already done that but now that we've restarted it what we can do is we'll need a video and for this tutorial I'm using this video that I recorded on my iPhone. Now you can use any camera you'd like any video capturing software. My case I use the iPhone camera and I actually had to convert this video because it's like a MOV file. So it's not the best quality but obviously you can use a better quality camera like a 4k1 you know 60fps. So this will do for this tutorial. So when you have your video here you want to go and open up live link. So you go to the tools and over here you want to go to the live link hub. So that's under virtual production live link hub. Now we'll go ahead and launch the live link hub program which is basically sort of like another separate unreal editor program so you'll see it'll open it up like this. It says live link hub, unreal editor 5.8. Live link you can actually use this to capture you know motion capture facial animations all that stuff in real time through this program and have it directly linked to Unreal Engine. So there's actually a lot of stuff you can do with this mainly is use for like virtual production but over here under the live data you want to go ahead and hit the drop down and select capture manager. Okay make sure that you do that. Add a device, click the plus icon and select mono video ingest. Okay there's other different ones here like OBS Studio. So again if you're you know doing virtual production and you want like real time capture there's a lot of options there for that but since we're just doing a single video when I select the mono video option here and then we need to add the video file. So in order to do that we select this and we can add a directory right here so click the three dot icon and then basically navigate to wherever you have your videos stored. I have mine on my users downloads in this folder called UE MoCAP. So just select the folder where you have the videos and it should load it here in this browser. Okay then you select the video you want to process. We'll select that one and we'll click this add to Q button. Okay it will add it to our Q over here you can modify the video image quality the audio all that stuff. We're going to leave it as the defaults and then we're just going to click start and what that will do is it will convert this video into an unrelentient file for our project. So just go ahead and give that a second. This video that I'm using it's only probably about a minute and a half maybe two minutes long. So it might take longer depending on your video length and video quality obviously higher quality video like a 4k video will take a little bit longer and once it's 100% complete status is little checkbox you can close the live link hub we're done with that. But now we can go into our content folder and you should have a folder for capture manager imports mono video ingest and you'll see it'll create a new folder for the video name. So in my case I had my MoCAP test one and it created these three different files. We have the capture data the image media source and the sound. So now what we need to do is create a metahuman performance. So right click and create under the metahuman we want to create this metahuman performance asset. Okay so this will be our metahuman performance and then I'm just going to name this MoCAP test and double click open this up. So let's go ahead and dock this up here at the top and so in this metahuman performance asset we want to go over to the details panel over here and we need to select the footage capture data. So hit the drop down and select the MoCAP test or whatever video file it created and you can see there's the video on the left you can scrub through the timeline and see it play through. But then we want to over here in the details select body tracking. Okay so we can see the actual skeleton and then in order to actually have this assigned to like a metahuman character we'll actually need to create a metahuman character. If you have one already you can use that but if you don't see one in this little drop down over here we'll need to create one so I'll show you guys how to do that real quick. Just go to your content folder right click and create a new metahuman under metahuman you want to do a metahuman character. Okay so you'll just create a new metahuman character asset like that and double click open this up. This will open up the metahuman creator editor inside of Unreal Engine and again you should have this plugin as long as you downloaded the metahuman core data when you install Unreal Engine 5.8 but in here just the basics you can select presets over here on the left so there's a bunch of preseted characters that you can choose from so just double click on it and it will load that preset. So for example if I wanted this character we could select that guy. There's a bunch more other different types of characters presets you can also customize it okay but I'm not going to go over that in this video I've made a separate video about that once you're done getting your metahuman in here you just go ahead to assembly okay you'll see that the character is not rigged so you'll need to go over here and click create full rig so we'll go ahead and do that right now okay and then now that we've created the rig it's going to say character is missing textures use downloads texture sources to create them before assembling so you have to download the texture sources so you'll click on that we'll go ahead and download that and then you just click this green assemble button and that will go ahead and create the metahuman character and add it into your content browser so now you should have a new folder for metahumans and it should say you know whatever name the metahuman you created and then you should have the blueprint right here just like that okay so once you've gone ahead and done that now it can come all the way back to our MoCAP performance here and under visualization again just make sure you have body tracking enabled have a little checkbox there and then we're going to select the drop down select our BP new metahuman character and it's going to say use audio clock source we'll just click yes and it should load it just like that okay so now that we have our metahuman character in here we just have to process our video over here so we just go to the process button at the top left click on that and now it's going to go ahead and start processing this animation think using like some sort of machine learning algorithm now this process actually took me quite a long time about an hour or so and I don't know if that's just because it's my PC acting up but yeah maybe if anyone else actually tries this let me know down in the comments if you guys do try this how long of a video clip you try to convert what was the resolution and how long does it actually take you to process it let me know down in the comments down below and maybe also just you know some background computer specs it just seems like this took an awfully long time compared to metahuman animator for example maybe because this is like a full body sort of thing but yeah who knows anyways so I'm going to go ahead and save this and now that we process this data we should be able to just play the animation so we can go ahead and play and yeah as you can see we have me jumping here I'm going to go ahead and real quickly just hide the skeleton so over here we can click show skeleton uncheck that and I will go ahead and hide this skeleton okay so you can see we're moving the arms I'm not actually talking in this video but it will actually do facial motion capture as well okay so if you're talking it will try to capture the face animation as well you can see we have like a weapon equip okay we're pulling out a weapon have a pistol what else do we have in here we have some you know lifting up the legs moving the hands around okay it looks pretty good results grabbing my leg there okay you can see not the greatest one you know grabbing a leg we have like a draw sword animation giving we're giving an item collecting an item okay we're kind of walking back and forth it's really nice they got like the walking movement so it's pretty good for the tracking there okay we're waving okay now we're doing to do the finger tests so wow pretty good results and obviously you could clean this up you could come into sequencer and manually keyframe some animations and kind of just use this as like a starting point that's usually what people do with mocap they'll come and cleaned up later but overall I think this is pretty good results I mean you could record a couple of animations for your game just have it be processed then cut it out and use it for different types of animations so how to actually use this animation so now that we've created this performance basically you can export the animation so we have this export animation which will bake it into an actual sequence so click on that you can rename you know what the name is over here and where you want to save it I'll just click save and you have some settings here I'll just leave it as a default click create okay and so now that you have the file so mine is in my content folder over here the AS, MHP, MocapTest okay you can open it up but you want to probably retarget this animation let's say you want to use this for games you know you could just right click the animation asset and retarget it and then since I have the third person template this is the third person gameplay template I have the different skeletons so we can use you know SKM and Manny then you just select the asset the animation asset over there so click export animations you can choose where you want to export it to we'll just export it to our content folder okay and I'll go ahead retarget the animation to the UE5 skeleton and now we have retargeted animation so we go ahead and open this up as you can see here is the UE5 character and you can basically use this in your games you know you could come in here cut this up in the different parts and use parts of it having like a NPC fighting, quip animations all that stuff you can use as you need so yeah look at that we even have the crouching there okay my quip animation idle like rifle idle there yeah you might need to clean up like the hand parts you can see that the wrist is twisting there and it could just be that part of the video quality if you have a better quality camera like I was using an iPhone and the resolution wasn't the greatest so again if you use a better camera quality might be better but yeah that's going to be pretty much for this tutorial let me know what you guys think about this feature down in the comments down below also if you do try this out let me know your results how long overclip did you try and how long it took to process and yeah that's pretty much it for this video so I hope you guys enjoyed and I'll see you guys in the next one

**Frame:** tutorials\frames\new-unreal-engine-58-metahuman-markerless-mocap-tutorial\frame_000.jpg


---

## Structured Notes

### Core Technique
UE5.8 Markerless Mocap Plugin: ingest video footage (iPhone/any camera) → Live Link Hub processes via ML → MetaHuman Performance asset → body + face tracking baked to MetaHuman → export animation sequence → retarget to UE5 skeleton. No suit, no markers, no external software. Full body + hands + face in one pass. Processing time significant (≈1 hour for 2-minute clip in author's test).

### Summary
15-minute Smart Poly walkthrough of the UE5.8 MetaHuman Markerless Mocap Plugin. Record yourself on iPhone → convert MOV to compatible format → ingest via Live Link Hub (Mono Video Ingest) → create MetaHuman Performance asset → assign video + enable body tracking + assign MetaHuman Character BP → click Process (ML-based; takes ~1 hour for 2min clip) → preview in performance editor → Export Animation → retarget to UE5 skeleton. Results: good body/arm tracking, decent hand tracking, some finger detail, wrist twist artifacts at low camera quality. Facial capture included if performer speaks. Final output: retargeted animation sequence usable in games/projects. Plugin setup requires: 7 MetaHuman plugins + MetaHuman Core Data downloaded at install time.

### Key Steps
1. **Prerequisites**:
   - UE5.8 required
   - When downloading UE5.8: enable **MetaHuman Creator Core Data** in Options (or Modify later)
2. **Enable 7 plugins** (Edit → Plugins → search "metahuman"):
   - MetaHuman Animator
   - MetaHuman Animator Markerless Motion Capture
   - MetaHuman Core Tech
   - MetaHuman Core and L
   - MetaHuman Creator
   - MetaHuman Live Link
   - MetaHuman SDK
   - Restart
3. **Prepare video**:
   - Film performer with any camera (iPhone, 4K camera, etc.)
   - Convert if needed (MOV → compatible format); higher quality = better results
4. **Open Live Link Hub**:
   - Tools → Virtual Production → **Live Link Hub**
   - Under **Live Data** dropdown → **Capture Manager**
5. **Add Mono Video Ingest**:
   - Click **+** (Add Device) → **Mono Video Ingest**
   - Click the 3-dot folder icon → navigate to folder containing your video
   - Select video → click **Add to Queue**
   - Click **Start** → waits for processing (creates UE-format capture data file)
   - When status = 100% → close Live Link Hub
6. **Find imported files**:
   - Content Browser → Capture Manager Imports → Mono Video Ingest → [video name folder]
   - Three assets: **Capture Data**, Image Media Source, Sound
7. **Create MetaHuman Character** (if needed):
   - Right-click Content Browser → MetaHuman → **MetaHuman Character**
   - Double-click → opens MetaHuman Creator in-editor
   - Choose preset → customize → **Assembly** → **Create Full Rig** → **Download Texture Sources** → click **Assemble**
   - MetaHuman Blueprint created in content browser
8. **Create MetaHuman Performance asset**:
   - Right-click → MetaHuman → **MetaHuman Performance**
   - Double-click to open
9. **Configure MetaHuman Performance**:
   - Details panel → **Footage** → select the Capture Data asset from step 6
   - Enable **Body Tracking** checkbox
   - **Visualization**: select your MetaHuman Character BP from dropdown → click Yes if prompted about audio clock source
10. **Process**:
    - Click **Process** button (top left)
    - ML processing begins — expect ~1 hour for 2-minute clip (varies by hardware + clip length/resolution)
11. **Preview**: after processing, click Play → MetaHuman performs the captured animation including body + hands + face
12. **Export**:
    - Click **Export Animation** → set name + save location → click Create
    - Animation sequence created in content browser
13. **Retarget** (optional, for games):
    - Right-click animation asset → **Retarget** → select target skeleton (e.g., SKM_Manny for UE5 third person) → Export Animations → save location
    - Retargeted animation now usable in any UE5 character

### UE Systems / Blueprints / Settings
- **MetaHuman Markerless Mocap Plugin** — UE5.8 experimental plugin; ML-based body + hand + face tracking from video; no suit or markers required; UE5.8 only
- **Live Link Hub** — separate application (Tools → Virtual Production → Live Link Hub); manages capture sources; here used as offline video ingest processor
- **Mono Video Ingest** — Live Link Hub device type for single-camera video; outputs Capture Data asset + media source + audio
- **MetaHuman Performance Asset** — editor asset tying Capture Data → MetaHuman Character; contains visualization, body tracking toggle, and Process button
- **MetaHuman Creator (in-editor)** — UE5.8 includes MetaHuman Creator inside UE Editor (previously web-only); requires MetaHuman Creator Core Data download at install
- **Body Tracking** — enable in MetaHuman Performance details; shows skeleton overlay on video; required for full body animation output
- **Export Animation** — bakes MetaHuman Performance to standard Animation Sequence asset
- **Retarget** — right-click animation → retarget to any skeleton; e.g., UE5 Mannequin for game projects
- **Processing time** — ML-based; ~1 hour per 2 minutes of video (author's hardware/quality); varies significantly
- **Camera quality impact** — iPhone MOV quality yielded good body/arm, some wrist twist artifacts; better camera = better results, especially hands/fingers/face

### Difficulty
Beginner-Intermediate (Setup is plugin-heavy; processing is fully automated; cleanup/retargeting is standard workflow).

### UE Version
UE5.8 (Markerless Mocap Plugin UE5.8-specific)

### Tags
metahuman, mocap, markerless, live-link, body-tracking, facial-capture, retargeting, plugin, workflow, beginner

---

## Related Entries
- `metahuman-realtime-animator-best-practices-unreal-engine-animation-hub.md` — real-time webcam face capture (alternative/complementary to markerless)
- `metahumans-for-mocap-unreal-engine-animation-hub.md` — MetaHuman for MoCap Manager; suit-based hardware mocap + MetaHuman
- `unreal-engine-58-new-markerless-motion-capture-tutorial.md` — another UE5.8 markerless tutorial (different author, same feature)
- `motion-capture-isnt-just-for-hollywood-any-more.md` — Rococo suit-based mocap pipeline; comparison: suit vs markerless
- `new-unreal-engine-58-metahuman-crowd-plugin.md` — other UE5.8 MetaHuman feature
