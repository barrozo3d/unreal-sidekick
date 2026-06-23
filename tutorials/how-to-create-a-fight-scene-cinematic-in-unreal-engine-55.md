---
title: How to create a fight scene cinematic in Unreal Engine 5.5
source: YouTube
url: https://www.youtube.com/watch?v=26c4TVIYZ8k
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-create-a-fight-scene-cinematic-in-unreal-engine-55/
frame_count: 9
---

# How to create a fight scene cinematic in Unreal Engine 5.5

**Source:** [YouTube](https://www.youtube.com/watch?v=26c4TVIYZ8k)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 9m33s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Fight scenes are awesome, and if you've ever wanted to direct one yourself, this one's for you.  In this video, I'll show you how I created this Kung Fu Fight scene in Unreal Engine 5.  Combining my own performance capture with an animation pack from Real Illusion,  I was able to achieve some crazy results and in record time.  On top of that, I'll show you how I dubbed the English performances to Chinese using 11 labs and metahuman animator.  But first, enjoy the film.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_000.jpg

### BROKEN FIST Short Film [0:26]
**Transcript:** There are two of us already here holidays.  The flow of motion can be pulled to see sudden atmosphere.  If complete it at the bottom, please overcome it.  the end of this  the end of this  I know  X  how to  build and yield  with this powerful perpetual  I will destroy your mansion and destroy your city.  Then, I will take revenge on the rich.  I will never be able to escape.  You are so stupid!  You are the reason why you are doing this.  You are the most excellent student in my life.  You are not the only one who can do this.  You are the master of the prison.  You think you can do this?  You are so stupid.  You are so stupid.  I will destroy his mansion.  Next, I will take revenge on you.  Then I will take revenge on you.  I will not be your student.  So you...  You are not the only one who can do this.  What?  Jason.  I can't believe it.  Alright, thanks for watching.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_001.jpg

### Reallusion Animation Pack [2:54]
**Transcript:** So, the idea for this really came from seeing this animation pack from Real Lusion.  I think I saw it in a YouTube video by JS Films like a year ago or something.  And, you know, I was just like, I have to make something with this.  And, it is this pack of amazing hand-to-hand combat animations.  I think there are 68 animations or so.  You really just drop them into Unreal Engine and you have the basis of a fight scene right there.  And, I just remember thinking they were so cool.  And, you know, all I would have to do is come up with kind of like a story and some performance capture to kind of tie these choreographed fight scene animations together.  And so I was just browsing fab for an environment.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_002.jpg

### Setting up the Scene [3:38]
**Transcript:** And, the thumbnail for this one just jumped right out at me.  I was like, I love that look.  This burning tree and the destroyed temple around it.  I knew I could use the fire to sort of motivate the lighting.  And, that would act as sort of my main light source.  And, I could sort of frame the characters against the fire.  And, you know, I just dropped in the metahumans with their outfits and, you know, pulled in some of the animations from real illusion, got them retargeted to metahumans.  And, was just kind of, you know, set up a camera and kind of moved around a little bit.  And, was like, okay, this is totally working.  I had some more ember and fire and smoke particles in the background.  It's just to kind of busy it up, liven up the space behind the characters.  And then, of course, I used Easy Rain.  I mean, Rain just adds so much drama to a scene, so much ambiance.  And, I was like, all right, I got my aesthetic down.  And, I basically just came up with a story, you know, around these things.  This is not the best script, but this is really just a vehicle to get us into the fight choreography, which is what I wanted to practice filming in the first place.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_003.jpg

### Performance Capture with Move.AI [4:50]
**Transcript:** So, all the performance capture was done using Move Pro, which is the multi-camera solution from Move AI.  And, this is a great system. I've been using it for almost a year now.  And, I've gotten it down, so I can get really good body captures every time.  And, the hands definitely still struggle, though.  And, in this case, there was something wrong with the retargeter.  And, using the hand poses, I wasn't even really able to fix the hands, but whatever.  There were a few times where I have to kind of, you know, whip the camera or something, you know, to kind of hide the transition from choreographed animations to my animations.  But, I think overall it worked fine.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_004.jpg

### VDB Explosion Effects [5:36]
**Transcript:** So, in addition to that, I found these VDB assets with these explosion effects.  And, I was like, this is perfect for some sort of, you know, dragon ballsy style, energy blasts or something.  So, maybe we can tie that into the story somehow as well.  And then, for some reason, I decided it would be cooler if it was all in Chinese instead of English.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_005.jpg

### Dubbing to Chinese using Elevenlabs [5:53]
**Transcript:** But, I would deliver the whole thing in English and then using some AI tools and animation tools, I would change my performance into Chinese,  while still maintaining the original sort of performance that I give in English, if that makes sense.  For Bidden Scrolls, warned of this power's price, does not serve you. It consumes you.  So, the whole script is written in English and I give the performances in English  and capture my face using Metacumin Animator the same way I would normally.  And then, I take that audio, that English audio, upload that to 11 labs.  And then, using the 11 labs dubbing tool, I then convert the lines into Chinese.  And, it clones my voice sort of.  But, the idea is that it's my voice, my performance, but just delivered back in Chinese.  I then used the audio to lip sync tool, which just takes the audio and generates full facial animation from that audio.  So, I copy the keyframes from the Chinese animation mouth onto the original animation.  And, the results were okay.  This is extremely tedious and I'm not entirely sure if it's worth it, but I would just kind of do a test and it looked pretty cool.  And I was like, you know what, I'm going to keep going with it.  So, I kind of just committed to doing the video like this.  And, if you want to try out 11 labs and support the channel at the same time, I do have an affiliate link in the description or right up here.  And, the sound design was really fun actually. I'm not a great sound mixer or sound designer.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_006.jpg

### Sound Design using Artlist.io [7:53]
**Transcript:** I just use art list, which I've used for years. I've used it for my commercial projects for music mostly.  But, I've recently started using for all the sound design for these Unreal Engine films.  And, they have a plugin that just integrates right into Adobe Premiere.  And, so, I'm able to just literally, you know, search whatever sound effect I want and drop it right into the timeline.  And, just layer tons of sound effects and music elements and stems from the music.  Yeah, I also have an affiliate link for art list. So, if you want to try them out and support the channel at the same time, it's in the description or right up here.  Something that's really interesting about these animation packs is I haven't found anything really similar to this.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_007.jpg

### Do You Want More Animations Like These? [8:40]
**Transcript:** Sure, there are paired animations on FAB and elsewhere. But, there's not a lot of great choreography that you can drop into a fight scene like this.  And, I'm wondering, you know, what the market is like for that because I'd really like to create more.  So, I don't know, let me know in the comments if you like using assets like this.  You know, do you think these ones are overpriced? I think it's like $110 for this whole pack.  You used to be able to buy the animations individually, I think, but you can't anymore.  Anyway, you know, if this is something you would use, like say sword fighting or other forms of hand-to-hand combat or choreography,  you know, let me know if that's something that you like to use in your productions.  Alright, thanks for watching and I will see you in the next one.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_008.jpg

### Outro [9:30]


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
