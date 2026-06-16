---
title: Unreal Engine Compositing Tutorial - UNREAL ENGINE FOR FILMMAKERS [Course Link in Description]
source: YouTube
url: https://www.youtube.com/watch?v=39nmue2lIdA
author: Boundless Entertainment
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-compositing-tutorial---unreal-engine-for-filmmakers-course-link-in/
frame_count: 8
---

# Unreal Engine Compositing Tutorial - UNREAL ENGINE FOR FILMMAKERS [Course Link in Description]

**Source:** [YouTube](https://www.youtube.com/watch?v=39nmue2lIdA)
**Author:** Boundless Entertainment
**Duration:** 8m46s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** What's going on guys Sam here again and I apologize for the long break between videos  I've been working really hard on the unreal engine course for filmmakers as well as my new film Gemini  Which I've made a lot of progress on and I'm really excited to share with you guys everything that I've learned on that  So there's gonna be a lot of new content coming up soon and also I'm gonna be finally releasing Gemini  Sometime in the next few months so stay tuned for that as well, but in today's video  I want to go over how to composite media textures and layers inside of Unreal Engine  So this technique is gonna be useful for integrating any sort of media  Textures or layers that you want to put into your unreligion projects  So this is gonna be useful for creating fog cards green screen compositing or any sort of other video layer that you want to  Integrate into your unreligion project  So in this particular tutorial, I'm gonna go over how to make fog cards inside of Unreal Engine  And then how to composite those into your scene get them to play back properly in the sequencer and any other details that might come up along the way

**Frame:** tutorials\frames\unreal-engine-compositing-tutorial---unreal-engine-for-filmmakers-course-link-in\frame_000.jpg

### IMPORTANT UPDATE [1:00]
**Transcript:** So before we get into the video  I just want to let you guys know that I am migrating all of my content over to a new channel called Balance Entertainment 2  I'll put a link on the screen right now so you guys can go over and check that out subscribe to it  I'm not gonna be posting on this channel anymore in the future  I will keep posting a few videos until I have everybody  Migrated to the new channel, but just so you guys know if you are interested in subscribing to Balance Entertainment  Hit over to that new channel and make sure you click the subscribe button there. I really appreciate it  So without any further introduction, let's get into the video

**Frame:** tutorials\frames\unreal-engine-compositing-tutorial---unreal-engine-for-filmmakers-course-link-in\frame_001.jpg

### Setting up Media Player [1:31]
**Transcript:** So the first thing that we want to do is we want to import our  atmosphere into our project and this is just an MP4  HT64 file that I've rendered out of after effects and  All we're gonna do is right click in here and we're gonna go in here to media and then we're gonna click on  Media player and we're gonna check video output media texture asset click okay  And we're just gonna name this something that's gonna create a media texture and we're also going to have this media player  So if we double click on our media player  It's gonna open this window and what we want to do is go and find our atmosphere  Oh one file and it's going to be this one. We're gonna double click that and we're gonna hit save  Okay, and we can close out of this. So now we're gonna do we have our texture here

**Frame:** tutorials\frames\unreal-engine-compositing-tutorial---unreal-engine-for-filmmakers-course-link-in\frame_002.jpg

### Setting up Plane [2:17]
**Transcript:** We can create a plane so I'm gonna go up here and search  plane and we just drag one into our scene here and  Then we're gonna do is we're gonna take our scale. We're gonna unclick this and we're gonna do  16 and then hit tab and click nine and what that's gonna do is just gonna set our aspect ratio for us  We want our aspect ratio of this plane to match the aspect ratio of our footage, which is 16 by nine  so what I'm gonna do is just rotate this and  We have our plane, okay, so I'm just gonna take this and drag it onto our plane  That's gonna create a material for us. We can double click on this material go into it and I'm gonna maximize this window

**Frame:** tutorials\frames\unreal-engine-compositing-tutorial---unreal-engine-for-filmmakers-course-link-in\frame_003.jpg

### Material Settings [2:56]
**Transcript:** Make it bigger and what we want to do here is  We're gonna map our opacity and we're going to just set up our texture for this video material  So what we want to do since we want it to have it just transparency this video doesn't actually have transparency yet  So we need to create that so what we're gonna do is go to our blend mode and we're gonna click that and click on translucent and  We can alt click on the base color here so that we get rid of that and we're gonna take our texture sample and drag out the RGB  And we're gonna go into a multiply node. We're gonna do we're gonna multiply by a scalar parameter  So we're gonna hold S on the keyboard and click it's gonna create a scalar parameter and we're just gonna call this  strength  The setting here will determine the strength or opacity of our fog layer  So what we're gonna do is take this multiply node and drag it into our emissive color  All right, and then what we're gonna do is go down here and create another scalar parameter and we're gonna call this one opacity  So this is going to be the actual opacity of our fog layer and  We can set our default value and what I like to do when I'm doing these fog layers in order to c...

**Frame:** tutorials\frames\unreal-engine-compositing-tutorial---unreal-engine-for-filmmakers-course-link-in\frame_004.jpg

### Setting up the Sequencer [4:41]
**Transcript:** And that's because we have to set up so that it will actually play in our sequence  So if I go up to our cinematics and I go to our camera move to here. That's our sequence  Just ignore all these other fog layers that I have in here. So what we're gonna do is go and we're gonna add a  Media track so that our media player can actually play this when we play through our sequence  So we go up here to track and I'm gonna do media track and  Then I'm going to click this little plus sign on the media and we're gonna click on atmosphere 0.1  Which is what we just created and then the last thing that we have to do is right click on our media track and go up here to edit section  We can click on our media texture and what we need to do is set up  Our media texture so that it plays properly. So we're gonna click on this  ATM01 tutorial video because that's the one we just created and  Now what we can do is just drag this out and  We want to drag this all the way to the end  We can always reposition this so at the start here that is the start of our clip playing and this will be the end of our clip playing  It's not an infinite clip  So it's not going to play forever. I've faded it out so tha...

**Frame:** tutorials\frames\unreal-engine-compositing-tutorial---unreal-engine-for-filmmakers-course-link-in\frame_005.jpg

### Fixing Shadows [6:52]
**Transcript:** You're gonna see that it's actually going to be casting a shadow on our ground  And we don't want that because it's just gonna cast the shadow of a plane if we had an actual  Opacity or alpha mask  For this layer we could have the shadow and properly cast a shadow  But we don't have that for this material. So what we're gonna do is go into our details here and just turn off  Our cast shadow and that's not gonna be this that weird shadow anymore  So that's all gonna be fixed up then  But that's just essentially how you set up these fog cards and that's going to allow you to really add a lot of movement to your scene  You can also use this to composite using video clips  If you want to as well. So that's a really useful technique  So that about wraps it up for this video guys

**Frame:** tutorials\frames\unreal-engine-compositing-tutorial---unreal-engine-for-filmmakers-course-link-in\frame_006.jpg

### Unreal Engine Course & New Channel [7:40]
**Transcript:** Thank you for watching and I hope it was helpful to you. So if you guys like this video  It is actually a bit of an excerpt from the Unreal Engine course that I'm working on  It's almost done and I'm really excited to share with you guys  So if you're interested in that stay tuned subscribe to the new channel  And I can't wait to hear what you guys think. I do want to say that I've started moving all of my content over to a new channel  It's currently called balance entertainment too so that there's not confusion  But I am going to be migrating all of my videos to that new channel and soon  I'm only going to be posting my videos to that channel  So this current channel is not going to exist anymore  Make sure you head over and subscribe to that new channel  I'm gonna put a link in the description and I'll also put a link on the screen right here  So don't forget to do that  I would greatly appreciate it and it'll really help me out especially in the long run and also a special  Thank you to everybody who has already migrated to the new channel. I appreciate it  So once again, thanks for watching and have a good one guys

**Frame:** tutorials\frames\unreal-engine-compositing-tutorial---unreal-engine-for-filmmakers-course-link-in\frame_007.jpg


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
