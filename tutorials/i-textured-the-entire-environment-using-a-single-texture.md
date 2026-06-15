---
title: I Textured The Entire Environment Using a SINGLE Texture
source: YouTube
url: https://www.youtube.com/watch?v=pkRH_mdAP2E
author: Procedural Minds
ingested: 2026-06-15
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/i-textured-the-entire-environment-using-a-single-texture/
frame_count: 5
---

# I Textured The Entire Environment Using a SINGLE Texture

**Source:** [YouTube](https://www.youtube.com/watch?v=pkRH_mdAP2E)
**Author:** Procedural Minds
**Duration:** 15m48s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### New Environment Style [0:00]
**Transcript:** It's time for another monthly devlog, and there's actually quite a lot that's been done  this past month, at least on a visual sense.  Because if we take a look here, aside from having the animations in for the character, visually  this environment probably looks a little bit different.  Now, don't mind the frame rate and the top right being a little bit lower than before,  that is just because I'm currently inside of the editor itself, because I want to show  off a few different things.  From one of the main things, what I'm showing off is this new visual style that we have.  I've gone ahead and simplified it quite a bit, the character, because of it, reads a lot better.  I think it kind of fits the aesthetic a lot more, and one of the main things is,  if we come here and go into the actual dungeon, you'll see in here,  well, it's all the way down, new visuals carry all the way to the bottom.  Now, there are some parts of it that still need to be a little bit tweaked, but overall,  it's working a lot better.  The enemies read a lot better here, right?  They pop a lot more.  Now, visually there's some stuff that's a little bit different about them,  because I have the normal map up...

**Frame:** tutorials\frames\i-textured-the-entire-environment-using-a-single-texture\frame_000.jpg

### One Texture Setup [1:12]
**Transcript:** And the main thing that I'm pretty happy about here with this style is all of this,  the rocks, the bricks, the columns, absolutely 100% of the environment here in Swords Included,  is done with a single texture, 100% everything.  Even those guys, the trees, it is all one single texture.  I'm quite happy with how it's turning out so far.  And when I say texture, I don't actually mean material.  I mean literally a single texture.  And I mean this texture right here.  This is what I'm using, and this is why I want to show it in the editor.  It is literally just an RGB mask.  We can see here, red channel, green channel, and blue channel,  just has different strokes set up.  Now, there's a little bit of compression artifacting.  It's not a perfect, like, clean setup here.  This is all from the compression.  I could make it uncompressed, but with the style that I have,  you really can't see those little imperfections.  It's not that big of a deal.  Who are skis in area?  I can make it uncompressed.  It is only one texture after all.  Basically, I'm using this RGB mask to drive everything in this environment.  Absolutely everything here.  And there's a few things that I need to tweak,  l...

**Frame:** tutorials\frames\i-textured-the-entire-environment-using-a-single-texture\frame_001.jpg

### Combo Attack System [10:26]
**Transcript:** The other thing that I actually set up  is right all the animations.  So we have the nice dash.  It has been improved.  So as I keep running, it is much better and smoother.  And I've gone ahead and made a combo system.  Look at that full combo system.  So the way it works is, you have three attacks.  So that's the light attacks.  And here's the heavy attacks.  Light attacks have, I believe, a 0.75 second cooldown.  And the EBA attacks have a 1.5 second cooldown.  And as many as you do, will be the cooldown.  So if I do 1, 2, 3, this will be on cooldown for 1.5 seconds.  If I do all three of the heavy attacks,  then the cooldown will be 4.5 seconds.  But you can also combine them.  So for example, I can do left, right, left.  And I'll do the first and the third attack  as the light attack and only do the second attack  as the heavy version.  So you can combine the two.  And the cooldowns will go down according to what you used.  If you use two heavy attacks,  then it will be the time of two heavy attacks.  If you use two light attacks, same thing.  Right, it doesn't matter.  You can play around with it.  And that's important because not only do we have this,  but on the spell versi...

**Frame:** tutorials\frames\i-textured-the-entire-environment-using-a-single-texture\frame_002.jpg

### Snappier Attacks [12:51]
**Transcript:** You have, I think, a 0.1 second  since the end of the animation.  The keep where there is end of animation.  Because now you attack before the animation actually finishes,  which makes it feel a lot more snappy.  That also means for the special attacks,  if I was to run down and press one,  you'll see how quickly I can do the attack  and continue running as I'm holding down.  It is now considerably faster.  The reason is, it is no longer waiting  for the full animation to finish,  which means that it feels a lot snappier.  Now, if you were to press the attack,  it still has more of the animation to go.  And if you weren't doing anything,  it would play the entire animation.  But at a certain point,  once the attack part is done,  you're able to do other things.  You're able to start moving and do everything else.  So you don't feel like you have to dash cancel.  Because before, you would have to do the attack  and then just dash to basically do an animation cancel  to get back to moving around.  And then I realized,  why am I forcing people to animation cancel?  And that shouldn't be a thing.  So I've gone ahead and changed it.  So you could just have it feel a lot snappier  than a...

**Frame:** tutorials\frames\i-textured-the-entire-environment-using-a-single-texture\frame_003.jpg

### Sneak Peak On Next Month's Changes [15:08]
**Transcript:** And for this next month,  I've already started working on new power-ups.  Here's a little sneak peek of the power-ups  that I'm currently working on.  That's all you're getting,  along with potentially a visual style update  for the cards who better fit the environment look.  Now, this all seems interesting to you,  and you would like to support the development of the game  being grabbit on Patreon,  where you can join these wonderful people here  in supporting what I do.  It really means a lot.  And if you'd like to join the community,  the link to the Discord,  everything is down in the description below as always.  And if you're looking for something else to watch,  consider checking out this video.  But I think you're really gonna like.

**Frame:** tutorials\frames\i-textured-the-entire-environment-using-a-single-texture\frame_004.jpg


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
