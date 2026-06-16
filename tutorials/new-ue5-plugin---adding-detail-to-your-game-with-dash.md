---
title: New UE5 Plugin - Adding Detail to Your Game with DASH
source: YouTube
url: https://www.youtube.com/watch?v=UO2ehs5OjEw
author: Polygonflow Dash
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/new-ue5-plugin---adding-detail-to-your-game-with-dash/
frame_count: 10
---

# New UE5 Plugin - Adding Detail to Your Game with DASH

**Source:** [YouTube](https://www.youtube.com/watch?v=UO2ehs5OjEw)
**Author:** Polygonflow Dash
**Duration:** 8m58s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey everyone, Josh Powers for Polygon Flow.  And today I want to show you some great new features that have come online in recent updates  to Dash and how you can leverage these powerful new tools for your game environments.  So let's jump to it.  Here I have the base scene of an environment laid out.

**Frame:** tutorials\frames\new-ue5-plugin---adding-detail-to-your-game-with-dash\frame_000.jpg

### Starting Scene [0:15]
**Transcript:** This is mostly using modular pieces from Megascans or assets I custom made for this project.  But as you can see, this foundation by itself is feeling pretty bland and uninteresting for  a player to walk through.  So let's use Dash to quickly create something that is much more exciting.

**Frame:** tutorials\frames\new-ue5-plugin---adding-detail-to-your-game-with-dash\frame_001.jpg

### Adding Megascans Props With Dash [0:35]
**Transcript:** Working with layers in mind, I want to start with some props turned throughout to give  the player a sense of a dystopian type of world.  To do this, we'll go up to the newly designed content library icon right here and open  up Dash's content library, where we can begin to browse through our downloaded assets from  the Megascans library.  Placing these assets is as simple as dragging and dropping them into your scene.  Then you can use the placement tool to quickly move, scale, and rotate these assets to fit  with the scene.  However, you might not always be able to find the assets you need in Megascans, especially  when it comes to the more man-made objects, which has me excited to show off a brand new  feature to Dash's content library, the integration of Polyhaven.

**Frame:** tutorials\frames\new-ue5-plugin---adding-detail-to-your-game-with-dash\frame_002.jpg

### Adding Poly Haven Props With Dash [1:20]
**Transcript:** To switch over to Polyhaven, simply click this arrow icon here and then select Polyhaven.  This will give you instant access to Polyhaven's models, textures, and even HDRI skies right  inside Dash.  Like normal, all you need to do is drag an asset into your scene.  And if the asset is not already downloaded, Dash will automatically download the asset  for you.  You can also choose different resolutions to download by clicking on these tabs that  pop up when you highlight a thumbnail.  Having access to this growing library of content gives me even more ammunition to use  when filling out a scene like this, allowing me to tell the story I want even faster.  So I highly encourage you to take full advantage of this fantastic library of assets to help  you get your new scene up and running in no time.

**Frame:** tutorials\frames\new-ue5-plugin---adding-detail-to-your-game-with-dash\frame_003.jpg

### Using Dash Decal Tool [2:19]
**Transcript:** Alright now that we have a lot of the large to medium sized props placed, I feel like  we can start dropping in some decals.  With Dash, there's two ways to approach this.  The first is very similar to placing models.  We simply need to find a decal in the content library, and then drag and drop it into the  scene.  From here, we can move, scale, and rotate the decal to our liking.  There are a few other hotkeys specific to decals, but otherwise this operates very similarly  to asset placement.  So you should feel right at home using this.  Another way we can place decals is to scatter them.  To do this, you can grab multiple decals by holding down Shift and clicking on the assets  in the content library, and then drag them into your scene while holding down Control.  Once you let off the mouse button, you'll see a menu pop up with a few different options.  In this case, we'll go ahead and scatter these decals.  From here, we can adjust the various parameters of the decal scatter to our liking.  I recommend you use decals of similar scales per scatter, so that way when you adjust  the min and max scale, it doesn't feel too small or too large compared to the subject  matter of the d...

**Frame:** tutorials\frames\new-ue5-plugin---adding-detail-to-your-game-with-dash\frame_004.jpg

### Using Dash to Scatter Weeds [3:54]
**Transcript:** Now we can start to scatter some overgrowth across our scene.  I have a tree here that's growing out from the ground, but it feels a bit odd by itself.  So to help soften the transition to the ground, we can scatter some weeds by holding down  Control and selecting scatter.  And then we can tell these weeds to only grow near this tree by selecting the tree and  then adding it to the proximity mask option in our scatter properties menu.  And then we need to invert the results.  Now as I slide this number up, you can see the weeds start to extend out from the base  of the tree.  And now all we need to do is start playing around with some of the other scatter settings  to increase the density to get a heavier, more lush collection of grass and weeds near  the tree.  We can also add some other objects to the proximity list to get some additional overgrowth  as well.  Now you might notice that the weeds are a bit too clean near the edges, giving us a bit  of a semicircle look.

**Frame:** tutorials\frames\new-ue5-plugin---adding-detail-to-your-game-with-dash\frame_005.jpg

### Converting Instances to Foliage [4:54]
**Transcript:** Now there are multiple ways we can address this issue in dash, but today I want to talk  about a relatively new feature that we've implemented.  If we select the scatter, we can go up to the prompt bar and type foliage, and then  all we need to do is select convert instances to foliage.  This will pop up warning that this is not an undoable action, which means you are committing  to your current scatter placement.  So I highly recommend you tweak the settings until you are very happy with it and then  do this next step.  With that completed, we are now free to go to the foliage mode and the drop down, and  now you can see that the entirety of this scatter has become a foliage actor.  From here, we can add or remove some of the weeds to quickly reshape the edges of the  weeds to give us a more manual control over the placement of the initial scatter.  This is an incredible new feature that allows you to leverage the power of scatter to get  your vegetation nearly finished and then gives you the reins to give it that final touch.  Alright, back in this little alcove, I want to have a lot of trash and debris piled up.

**Frame:** tutorials\frames\new-ue5-plugin---adding-detail-to-your-game-with-dash\frame_006.jpg

### Dropping in Trash Bags with Dash Physics Tool [6:00]
**Transcript:** Fortunately, this is really easy to accomplish with Dash's physics tool.  All we need to do is select a few items to work with, such as these trash bags.  And then, with them selected, we can run the Dash physics tool.  We'll go ahead and hit set dynamic, and then start.  The bags will drop to the ground, and from here, all we need to do is hit the duplicate  button and watch the chaos turn to beauty.  I use the same technique in a few other places as well to give a truly random appearance  to clutter and debris piling up.  From here, it's just a matter of polishing, and one way we can add a lot of great detail  to this scene is adding a lot of cables.

**Frame:** tutorials\frames\new-ue5-plugin---adding-detail-to-your-game-with-dash\frame_007.jpg

### Placing Complex Cables with Dash [6:50]
**Transcript:** Adding this before would be a pretty large time sync, as you would have to create curves,  manually move them into position, change their appearance of gravity, wash, rinse, and repeat.  But one of the easiest tools to use in Dash is also one of the most powerful.  So here I have a couple of simple boxes along this balcony ceiling that has the same texture  as the balcony.  You can use any static mesh you want for this, but for this example, I kept it simple.  So all we need to do is select the boxes, then type cable into the prompt bar, and select  the cable tool.  Now all we need to do is add the selected models to the object list, and instantly you'll  see a cable generated between the various meshes we added.  From here, I can play with some of the settings, such as the radius of the cables, how many  cables will be part of this bundle by adjusting the duplicates, the min and max gravity, and  my favorite setting, connection rate, which allows us to drum up a whole lot of chaos  to these cables by having additional connection points between the various points on another  cable.  This gives that really crowded look in just seconds, which adds a lot to a scene like this.  There a...

**Frame:** tutorials\frames\new-ue5-plugin---adding-detail-to-your-game-with-dash\frame_008.jpg

### Jumping into the Environment [8:08]
**Transcript:** And there you have it.  Using Dash truly speeds up my workflow when working on an environment like this, allowing  me to not just fill my scene with a bunch of noise, but rather lets me carefully curate  where content goes while taking away the tedious tasks of placing everything by hand.  It's the best of both worlds and letting me keep my creativity and vision while giving  me the time to focus on the scene as a whole.  I hope this video was helpful for you, and that you were able to learn some of the great  new features in Dash.  And this is just the tip of the iceberg of what's yet to come from this amazing tool.  Thank you so much for watching, and we'll see you in the next one.

**Frame:** tutorials\frames\new-ue5-plugin---adding-detail-to-your-game-with-dash\frame_009.jpg


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
