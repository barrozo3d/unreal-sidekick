---
title: Volumetric Cloud Secrets  [Unreal Engine 4 & 5] Works in UE5!
source: YouTube
url: https://www.youtube.com/watch?v=yolGEIrhu0s
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 4.26 & UE5"
tags: [lighting, volumetric-clouds, clouds, cloud-masking, sky, environment, william-faucher, intermediate, ue5]
extraction_status: complete
frames_dir: tutorials/frames/volumetric-cloud-secrets-unreal-engine-4-5-works-in-ue5/
frame_count: 0
---

# Volumetric Cloud Secrets  [Unreal Engine 4 & 5] Works in UE5!

**Source:** [YouTube](https://www.youtube.com/watch?v=yolGEIrhu0s)
**Author:** William Faucher
**Duration:** 15m2s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, it's great to have you back.  The topic of today's video is going to concern  how to direct your volumetric cloud.  Now, anyone who's ever used volumetric clouds  at the under a 4.26 knows that they're kind of limited  in what you can do.  There's not much documentation on how to set these up  to have a bit more control.  But fortunately, Chris Murphy over at Twitter  kind of put me on the right track and be aware  that having full control over the placement  of your clouds is even a thing.  So I gotta get credit where credit is due.  Thank you so much, Chris.  You're the best.  Now, with that being said,  I'm gonna take this to the next level  and show you how you can set up your scene correctly  and have full control over the art direction of your clouds.  No, not you, the creepy clown behind you.  And so, why wait?  Let's go.  Okay, so before we get started,


### Setup [0:57]
**Transcript:** there's two things we need to do here.  So first of which is going to the setting top up top,  click on this and make sure,  and then click on the plugin window,  open up the plugins and here we'll search for volume metrics.  Make sure that the volumetric plugin is enabled  if it's not there,  you're not gonna be able to play the volumetric clouds.  So make sure that's enabled,  restart the engine and we're ready to go.  And before we get started,  there's still one last thing we need to do  and that is paying attention to right here.  So notice in my content browser here,  I've got just my content folder.  There is still one thing we need to enable  to access all the settings that we need for this tutorial.  And you'll notice the bottom right here,  we've got view options.  We're gonna click on this  and make sure that show engine content is selected.  And now notice on the left hand side here,  we've got a whole crap load of other folders.  You're gonna see why we need to enable this real soon.  So hang tight.  Now we're ready to get started  and have a little bit of fun with our clouds.  So the first thing we want to do  is we're gonna create a volumetric cloud system.  So you c...


### Recap [11:24]
**Transcript:** just so you guys can get a quick recap of what you need to do.  So I'm going to select everything here and delete that  and delete my volumetric clouds, done.  Start from scratch one more time.  So we're going to add another volumetric clouds here.  And again, we need to go back and play  through our new blueprints, which  is going to be in volumetric content.  If you don't have this folder here,  don't forget to go enable show engine content.  And then we're going to go to the tools, cloud compositing,  blueprints, cloud max object, cloud max generator.  Cloud max object, I'm going to move this guy away,  head the heck back.  And the last thing we need to do now,  set the scale to 25 or something.  And now we just need to change the material  on our volumetric cloud actor.  So I'm going to go find that in volumetric content, content,  sky, materials, and I'm going to use profiles,  BILOE.  Try this here.  And just like that, now we're starting  to get something a bit more interesting.  It's really simple that it works out of the box.  There's not that much to change.  There's no master materials or complex materials  to set up.  This works pretty darn well out of the box.  You can...


### Bonus Tip [14:05]
**Transcript:** And when you're really trying to get a shot  to look really good and you got your camera all set up  and you just want to look cloud to look perfect,  this is the way to do it.  Now, just one last bonus tip for you guys  in the event that you want to delete your clouds,  what you need to do is select your cloud mask objects,  delete them, but you'll see, hey,  my clouds are still there.  How do I get rid of them?  You just need to go to your cloud mask generator  in your outliner right here.  And you'll see right here where it says render clouds.  And by clicking that, it's going to update your render targets  and all the clouds that you deleted will be gone.  It's really as simple as that.  And that concludes yet another video.  Thank you so much for watching guys.  Again, if you have any questions or something's not working,  leave a comment down below and I'll try to get back to you  if possible.  I can't make any promises,  but don't take it personally if I don't.  It's not because I'm ignoring you, I promise.  So as always guys, don't forget to like and subscribe.  And I'll see you guys next week.



---

## Structured Notes

### Core Technique
Art-directing volumetric clouds in UE using the Cloud Mask Generator Blueprint workflow — enables precise placement and control over cloud positions instead of relying on procedural randomness.

### Summary
Hidden technique for controlling volumetric cloud placement in UE4.26/5 using the Volumetric plugin's Cloud Mask Generator and Cloud Mask Object Blueprints. These are engine content (hidden by default — need "Show Engine Content" enabled). Place Cloud Mask Objects where you want clouds, run the Cloud Mask Generator to render cloud masks, apply the BILOE material profile for realistic results.

### Key Steps

**Prerequisites:**
1. Edit → Plugins → search "Volumetric" → enable Volumetric plugin → Restart
2. Content Browser → View Options → **Show Engine Content** ✓

**Cloud Mask Workflow:**
1. Create Volumetric Cloud Actor: Place Actors → Volumetric Cloud
2. Find Cloud Blueprints: Engine Content → Volumetric Content → Content → Sky → Tools → Cloud Compositing → Blueprints
3. Place **Cloud Mask Object** Blueprint in scene → move to where you want clouds
   - Scale up (e.g. 25) to cover desired area
4. Place **Cloud Mask Generator** Blueprint in scene
5. Generator renders cloud masks from your mask objects
6. Change material on Volumetric Cloud Actor:
   - Engine Content → Volumetric Content → Content → Sky → Materials → Profiles → **BILOE**
7. To update: tick "Render Clouds" on Cloud Mask Generator to refresh

**Remove Clouds:**
1. Delete all Cloud Mask Objects
2. Select Cloud Mask Generator → tick "Render Clouds" to update render targets

**Recommended Profile Material:**
- `BILOE` — good realistic cumulus appearance; works well out of the box

### UE Systems / Blueprints / Settings

**Key Assets (Engine Content — Show Engine Content required):**
```
/Engine/Volumetric Content/Content/Sky/Tools/Cloud Compositing/Blueprints/
    Cloud Mask Object     -- place where you want clouds
    Cloud Mask Generator  -- renders the cloud mask from placed objects
    
/Engine/Volumetric Content/Content/Sky/Materials/Profiles/
    BILOE                 -- realistic cumulus material profile
```

**Tips:**
- Each Cloud Mask Object affects clouds in its area when the generator re-renders
- Multiple objects = multiple cloud groupings
- Scale controls the cloud footprint
- After deleting masks: must tick "Render Clouds" on generator to clear old masks

### Difficulty
Intermediate — requires knowing where engine content is hidden

### UE Version
UE 4.26 & UE5 (workflow identical)

### Tags
lighting, volumetric-clouds, clouds, cloud-masking, sky, environment, william-faucher, intermediate, ue5

---

## Related Entries
- `tutorials/tips-for-sky-atmosphere-fog---unreal-engine-5-ue4.md` — Sky Atmosphere complement
- `tutorials/demystifying-the-skylight-unreal-engine-4-5.md` — Skylight for cloud lighting
- `tutorials/lighting-in-unreal-engine-5-for-beginners.md` — Full lighting tutorial
