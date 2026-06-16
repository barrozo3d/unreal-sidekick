---
title: Unreal Engine's Secret Weapon for Cinematic Lighting
source: YouTube
url: https://www.youtube.com/watch?v=Zy5A6bDz9xw
author: Boundless Entertainment
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engines-secret-weapon-for-cinematic-lighting/
frame_count: 5
---

# Unreal Engine's Secret Weapon for Cinematic Lighting

**Source:** [YouTube](https://www.youtube.com/watch?v=Zy5A6bDz9xw)
**Author:** Boundless Entertainment
**Duration:** 12m47s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** What's going on guys? Sam here and in today's video I'm going to show you how I got this blade runner water  caustic effect using two different methods. The first method is going to be the standard harder way of  doing things and the second is going to be a much simpler way and trust me it's way easier and a lot  more fun. So let's get into it. Now in the description of this video you're going to find a link to

**Frame:** tutorials\frames\unreal-engines-secret-weapon-for-cinematic-lighting\frame_000.jpg

### Method #1 [0:16]
**Transcript:** download a few gobo textures or these textures that you're seeing on the lights right here. So that's  going to allow you to get started and try out some of these textures on your light. So it's fairly  easy to apply a texture to a light using the light function material in Unreal Engine. But when you're  using video it gets a little bit more complicated. So I'm going to show you that process right now.  All right so what we need to do to be able to actually create these is we need an image media  source or a file media source to actually bring in the media into Unreal Engine and then we need a  media player to play back that media and then finally we need a video texture asset which is the  texture that is going to be used in the material instance that is going to be applied to the light.  So I know that sounds a little complicated because it is a little bit complicated. So to get started  we can right click here and we're going to do a file media source. All right so we'll just right  click and search for file media source and we're going to call this FMS for file media source and  we'll call it underscore caustics. We need to use this file media source to tell Unreal Engine that...

**Frame:** tutorials\frames\unreal-engines-secret-weapon-for-cinematic-lighting\frame_001.jpg

### Method #2 [7:37]
**Transcript:** and takes a long time. The easy way is we have created a plug-in called lightforge2.0. The plug-in  actually automates this entire process. So we're going to get rid of this spotlight. Open up  lightforge2.0. We're going to go in here to our gobo section and here we can either select a  spotlight or we can actually just create a new light automatically. So we're going to hit this  choose media file right here and I'm going to choose calm loop slow 04. I'm going to hit open  and you're going to see what that's going to do is actually create all of the textures and the  media players and the media playlists automatically and actually make sure that these textures loop  in your editor every time you open on Relangent. So you don't have to worry about it stopping when  you close the media player or anything like that. It's automatically going to loop. So what I'm  going to do is hit add new light right here and it's going to automatically add a light to my scene  right here and you can see it's already looping. So if we go down here and just set this to like  15,000 lumens you can see there we already have our texture setup with just like two clicks.  And if we then select our spotligh...

**Frame:** tutorials\frames\unreal-engines-secret-weapon-for-cinematic-lighting\frame_002.jpg

### Building Scene Lighting [10:14]
**Transcript:** shadow mask right here and get rid of my blur. So all we did was take a spotlight up here and then  we brought our outer cone angle in bring up our inner cone angle to make that more intense and then  we just shot our light into the scene here move it back a little bit just really increase that  intensity there and you can see that now we're getting some nice lighting on our scene and if we  just increase the source radius a little bit that's going to soften up those shadows then all we  did was just duplicate that light and bring it down here moving into the background and then we  just kind of rotate it into place here and you can see that that is actually still it still has  our light function material applied to it. The other thing we could do is just have this spotlight  selected so just select that spotlight and then just create another gobo texture if we wanted  something totally different we could do that just hit choose media file find a different one  like this one for example it's going to do that and then hit apply to existing light and there we go  we have a totally different texture in our scene and then we go in here and control that one as well  individually. So the...

**Frame:** tutorials\frames\unreal-engines-secret-weapon-for-cinematic-lighting\frame_003.jpg

### Free Gobo Pack Download [11:57]
**Transcript:** that's going to include a free pack of gobo textures for Unreal Engine plus the ultimate rendering  guide which is going to give you a full guide to all the best tips and tricks console commands and  everything you need to get cinematic quality renders without any bugs or issues. So obviously we  worked a bit with light forge 2.0 in this video. If you want to learn more about some of its other  features like the 30 plus lighting presets, the included Unreal Engine lots and color grading suite,  cinematic quality render presets and it's fully integrated interface designed specifically for  filmmaking in Unreal Engine. Just click the link in the description and that'll take you to a page  where you can view full demos, breakdowns and everything you need to know about the plugin.  I hope you guys found this video helpful. Let me know what you want to see next if you have any  questions and what you thought of this video and until next time good luck creating and I'll see  you in the next one.

**Frame:** tutorials\frames\unreal-engines-secret-weapon-for-cinematic-lighting\frame_004.jpg


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
