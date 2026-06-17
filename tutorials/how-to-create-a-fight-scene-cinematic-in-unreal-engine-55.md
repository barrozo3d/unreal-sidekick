---
title: How to create a fight scene cinematic in Unreal Engine 5.5
source: YouTube
url: https://www.youtube.com/watch?v=26c4TVIYZ8k
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "5.5"
tags: [mocap, metahuman, metahuman-animator, move-ai, fight-scene, kung-fu, reallusion, animation-pack, dubbing, elevenlabs, vdb, ue5]
extraction_status: complete
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
**Transcript:** The most challenging in real life has been very challenging, yet gameplay is no match for this game.  I'll quickly make a movie about速度.  What can I portray?  But there's not much to it.  For the first time, I was able to fish,  back to the  To defeat this.  The part that I just...  How should I be?  Take the bullets I shot into  Hey  And for the number of blows, please  speak sensitively  No one will request for your support  And then make your wishes to get out  I have to be the one who is the most powerful.  You are so powerful.  You are the reason why you are doing this.  You are the most excellent student in my life.  You have to be the one who is the most powerful.  You are the master of the master.  You think you are the one who is the most powerful.  You are the master of the master.  You are the master.  You are the master.  You are the master.  You are the master.  I will never let you down...  ...that will kill you.  I am not your student.  Alright, thanks for watching.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_001.jpg

### Reallusion Animation Pack [2:54]
**Transcript:** So the idea for this really came from seeing this animation pack from real illusion.  I think I saw it in a YouTube video by J.S. Films like a year ago or something.  And I was just like, I have to make something with this.  And it's this pack of amazing hand-to-hand combat animations.  I think there's 68 animations or so.  You really just drop them into Unreal Engine and you have the basis of a fight scene right  there.  But I just remember thinking they were so cool and all I would have to do is come up  with kind of like a story and some performance capture to kind of tie these choreographed  fight scene animations together.  And so I was just browsing fab for an environment and the thumbnail for this one just jumped right

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_002.jpg

### Setting up the Scene [3:38]
**Transcript:** out at me.  I was like, I love that look.  This burning tree and the destroyed temple around it.  I knew I could use the fire to sort of motivate the lighting and that would act as sort of my  main light source.  And I could sort of frame the characters against the fire.  And I just dropped in the metahumans with their outfits and pulled in some of the animations  from real illusion, got them retargeted to the metahumans and was just kind of set up a  camera and kind of moved around a little bit and was like, okay, this is totally working.  I had some more ember and fire and smoke particles in the background just to kind of busy it  up, liven up the space behind the characters.  And then of course I used easy rain.  I mean, rain just adds so much drama to a scene, so much ambiance.  And I was like, all right, I got my aesthetic down.  And I basically just came up with a story, you know, around these things.  This is not the best script, but this is really just a vehicle to get us into the fight  choreography, which is what I wanted to practice filming in the first place.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_003.jpg

### Performance Capture with Move.AI [4:50]
**Transcript:** So all the performance capture was done using Move Pro, which is the multi-camera solution  from Move AI.  And this is a great system.  I've been using it for almost a year now.  And I've gotten it down so I can get really good body captures every time.  And the hands definitely still struggle, though.  And in this case, there was something wrong with the retargeter.  And using the hand poses, I wasn't even really able to fix the hands, but whatever.  There were a few times where I have to kind of, you know, whip the camera or something,  you know, to kind of hide the transition from choreographed animations to my animations.  But I think overall it worked fine.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_004.jpg

### VDB Explosion Effects [5:36]
**Transcript:** So in addition to that, I found these VDB assets with these explosion effects.  And I was like, this is perfect for some sort of, you know, dragon ball Z style, energy  blasts or something.  So maybe we can tie that into the story somehow as well.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_005.jpg

### Dubbing to Chinese using Elevenlabs [5:53]
**Transcript:** And then for some reason, I decided it would be cooler if it was all in Chinese instead  of English.  But I would deliver the whole thing in English and then using some AI tools and animation  tools.  I would change my performance into Chinese while still maintaining the original sort  of performance that I give in English, if that makes sense.  For Bidden Scrolls, warned of this power's price, does not serve you.  It consumes you.  So the whole script is written in English and I give the performances in English and capture  my face using Metacumin animator the same way I would normally.  And then I take that audio that English audio, upload that to 11 labs.  And then using the 11 labs dubbing tool, I then convert the lines into Chinese and it  clones my voice sort of.  But the idea is that it's my voice, my performance, but just delivered back in Chinese.  I then used the audio to lip sync tool which just takes the audio and generates full facial  animation from that audio.  And so then I copied the keyframes from the Chinese animation mouth onto the original animation.  And the results were okay.  This is extremely tedious and I'm not entirely sure if it's worth it.  But I would ...

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_006.jpg

### Sound Design using Artlist.io [7:53]
**Transcript:** And the sound design was really fun actually.  I'm not a great sound mixer or sound designer.  I just use art list which I've used for years.  I've used it for my commercial projects for music mostly.  But I've recently started to use it for all the sound design for these Unreal Engine films.  And they have a plugin that just integrates right into Adobe Premiere.  And so I'm able to just literally search whatever sound effect I want and drop it right  into the timeline and just layer tons of sound effects and music elements and stems from  the music.  Yeah, I also have an affiliate link for art list.  So if you want to try them out and support the channel at the same time, it's in the  description or right up here.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_007.jpg

### Do You Want More Animations Like These? [8:40]
**Transcript:** Something that's really interesting about these animation packs is I haven't found anything  really similar to this.  Sure, there are paired animations on fab and elsewhere.  But there's not a lot of like great choreography that you can drop into a fight scene like this.  And I'm wondering, you know, what the market is like for that because I'd really like to  create more.  So I don't know, let me know in the comments if you like using assets like this.  You know, do you think these ones are overpriced?  I think it's like $110 for this whole pack.  You used to be able to buy the animations individually, I think, but you can't anymore.  Anyway, you know, if this is something you would use, like say sword fighting or other  forms of hand-to-hand combat or choreography, you know, let me know if that's something  that you like to use in your productions.  Alright, thanks for watching and I will see you in the next one.

**Frame:** tutorials\frames\how-to-create-a-fight-scene-cinematic-in-unreal-engine-55\frame_008.jpg

### Outro [9:30]


---

## Structured Notes

### Core Technique
Combines a Reallusion hand-to-hand combat animation pack (68 paired choreography animations, retargeted to MetaHumans) with Move.AI Pro body capture and MetaHuman Animator face capture for bridging/dialogue shots, then uses ElevenLabs dubbing to translate English performances into Chinese, with AI audio-to-lip-sync applied to blend the dubbed mouth movements.

### Summary
Charlie Driscoll creates a Kung Fu fight scene cinematic in UE 5.5 by building around Reallusion's paired hand-to-hand combat animation pack (~68 animations), which provides choreography "Lego pieces" requiring only bridging performances captured via Move.AI Pro. A destroyed temple with burning tree provides atmosphere; fire/ember/smoke particles and Easy Rain dress the scene. The English dialogue is dubbed to Chinese using ElevenLabs dubbing tool, with the resulting Chinese audio fed into an audio-to-lip-sync tool to generate new MetaHuman facial animation, whose keyframes are manually merged onto the original capture. Sound design uses Artlist.io with its Premiere plugin. VDB explosion assets add energy blast effects inspired by anime-style energy attacks.

### Key Steps
1. Source paired hand-to-hand combat animation pack from Reallusion (68 animations); retarget to MetaHuman skeleton.
2. Find environment (destroyed temple with burning tree from Fab); drop MetaHumans with suitable outfits into scene.
3. Place combat animations in Sequencer; add fire/ember/smoke Niagara particles; add Easy Rain for dramatic ambiance.
4. Capture bridging dialogue/performance shots with Move.AI Pro; apply MetaHuman Animator face capture.
5. Use camera wipe/whip pan to hide transitions between choreographed and captured animation.
6. Write script in English; capture English dialogue for MetaHuman Animator.
7. Upload English audio to ElevenLabs dubbing tool; convert to Chinese (voice cloned to match original performance cadence).
8. Feed Chinese audio into audio-to-lip-sync tool to generate facial animation; copy Chinese mouth keyframes onto original MetaHuman face animation track.
9. Add VDB explosion assets for energy blast effects.
10. Mix sound design using Artlist.io Premiere plugin (layers: SFX hits, music stems, ambient).

### UE Systems / Blueprints / Settings
- Move.AI Pro multi-cam body capture
- MetaHuman Animator (face capture)
- Level Sequencer (combat animation choreography + bridging shots)
- Animation Retargeter (Reallusion pack → MetaHuman skeleton)
- Reallusion Kung Fu animation pack (~68 paired animations)
- Easy Rain asset (rain atmosphere)
- Niagara fire/ember/smoke particles
- VDB explosion assets (energy blast effects)
- ElevenLabs dubbing tool (English → Chinese with voice clone)
- Audio-to-lip-sync tool (Chinese audio → facial animation)
- Artlist.io + Premiere plugin (sound design)
- MetaHuman Control Rig (hand cleanup)

### Difficulty
Intermediate

### UE Version
5.5

### Tags
mocap, metahuman, metahuman-animator, move-ai, fight-scene, kung-fu, reallusion, animation-pack, dubbing, elevenlabs, vdb, ue5

---

## Related Entries
- `motion-capture-sword-fighting-cinematic-in-unreal-engine-5---moveai-and-metahuma.md` — sword fight using same concept (custom mocap replacing animation packs)
- `how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator.md` — mafia cinematic using the same Move.AI + MetaHuman Animator pipeline
- `cinematography-deepdive-for-beginners---camera-and-render-settings-tutorial---un.md` — covers UE 5.5 camera and render settings used in this production
