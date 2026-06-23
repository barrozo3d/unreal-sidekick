---
title: Improve Your Renders With Movie Render Queue PART 2 - FIVE Things You Need To Know (Unreal 4.26)
source: YouTube
url: https://www.youtube.com/watch?v=2U1wP8sJgfU
author: William Faucher
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn/
frame_count: 7
---

# Improve Your Renders With Movie Render Queue PART 2 - FIVE Things You Need To Know (Unreal 4.26)

**Source:** [YouTube](https://www.youtube.com/watch?v=2U1wP8sJgfU)
**Author:** William Faucher
**Duration:** 11m50s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hey there and welcome to part two of how to improve your rendered with the movie render queue  So over the past week many of you reached out to me with some issues  You've had and your render weren't working and it's been a real pleasure helping you guys out  So is that any point during this video you have a question?  Don't hesitate to leave a comment down below and I'll get back to you as soon as I thought of the can  So in this video we're gonna be talking about a few hidden tools so quality of life settings  But most importantly, I really want to touch base on a few  Limitation that the movie render queue has now  I'm not saying that you can't use them in production because it is production ready  But it's really good to know about these limitations because they could very well end up blind-signing you at the end of a production  So enough talking let's go

**Frame:** tutorials\frames\improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn\frame_000.jpg

### Limitation / Issue #1 - Object ID Pass When Subsampling [0:38]
**Transcript:** Alright, so one of the big limitations and something you should really be aware of when it comes to using  Movie render queue has to do with the object IDs when using  Sub sampling so anti-aliasing sub sampling so as you can see here  I've got my render setting from the movie render queue  All the rendering is an EXR sequence 16 bit  I've got anti-aliasing to none and I'm gonna set the sample to about 32 alright and  I've got my console variables here in order to get some proper  Sub sampling and proper results. This is what we covered this in a previous video  So we're gonna go ahead and add the object IDs limited tag here alright  So this means that we're gonna be rendering out a object ID pass with some high quality sub sampling now  The issue that you have here is when you use sub sampling the render times are going to increase  Astronomically, so let's go ahead and render this right now and you'll see what I mean. I'm gonna hit render local  And you can see right now already  It's hanging like it tend to hang around the 13 sub samples  I'm just rendering 15 frames here and you can see it just kind of just hangs a lot  It's really slow  Now this is not a this is normal and it has a lot of data to write to disk and the more objects  You've gotten your seeing the longer it's gonna be most likely so  This is not a problem in itself the render to gonna get out of this are going to be very high quality  However, you should just be aware that your renders are not gonna be as fast as they normally are  They're going to be substantially slower  So I think you can see I've only rendered three frames now and it's already been  40 almost 45 seconds so  It just doesn't need to be very much aware of because this can really screw you over in a middle of a production  You're counting any render being reasonably fast. You got a deadline and all of a sudden oh, hey our crypto pass  Or our object ID pass is just taking way too long to render  Now you know so once again  Not a major problem in itself and you know in my opinion is actually worse the way because the quality is that much better  But you just really need to be aware of just how much longer it takes to render these shots  So you guys might be wondering well, hey, of course it's gonna take long at a render because you're rendering with sub samples  Yes, I'm aware of that  But the hanging that we've just saw in the just now has to do with cryptomat or object IDs only  So we're going to go ahead and delete the object IDs path and we're still going to render with  32  temporal sample counts, okay, so it's gonna be the same amount of samples as previously  With no anti-aliasing and the console variable are all here once again in 16 bit EXR the only difference is  I'm not rendering the object ID pass and you'll see right now  Just how much faster and how smooth it is. So I'm gonna go ahead and hit render local  And look at those samples climbing up. There's no hanging whatsoever boom one  two for and three frames out and  So you can see there's no hanging the hanging that we saw it's only cryptomat related  So you can go ahead and safely use the sub sample rendering for better quality renders  But just keep in mind that if you use object ID, it's going to be much slower  All right, so let's jump into Photoshop real quick and look at our

**Frame:** tutorials\frames\improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn\frame_001.jpg

### Limitation / Issue #2 - No DoF with Object ID Pass [3:56]
**Transcript:** Cryptomat or object ID pass that we just read her now now  So looking at our object ID pass here. I've got the ferns mask  Right here now let's zoom in a little bit we can see that  With rendering with sub sample we got a nice clean motion blur so the cryptomat or object ID takes motion blur into account  But if you look carefully, you notice is another problem. There's another big problem  Now notice how completely out of focus these ferns are  But take a look at this ferns here look at this mask  Let's zoom in a little bit so you can see more clearly  So if you look carefully, you know if I toggle this you'll see that the object ID pass the mask that we get does not  Actually cover the entire range doesn't that the field is not working now to see more clearly. I'm going to go to this pot here and  Look at this mask here. Look how out of focus the pot is compared to the mask now if I select this  Edge here you'll see  Look at this edge selection compared to the out of focusness of the pot itself look at this mask  I cannot use this this is  Actually unusable. This is useless. So  We can conclude that  The field is not taken into consideration when you render object ID passes motion blur works  But not depths a field now  Normally in a VFX production this would not be a problem and I'll show you why so in a typical VFX  production approach  Step one would be to render the following passes you're gonna render out your beauty pass  You're gonna render out your crypto-met or object ID pass and you're gonna render out a 32 bit Z depths now  Of course you're going to be usually be rendering a lot more path than this  There's so many more other AOVs or render passes that you give to compositors  But to keep it simple I'm gonna keep it limited to these three step two is  You apply the depth of field or defocus in nuke premiere or after effects resolve whatever  With the Z depth render pass so all the depth of field out of the all the defocusing is done in post  You don't actually do it in the render  Why is that because in Arnold or Redshift Vray?  Whatever rendering depth of field is  Super time consuming it takes much much longer to render with that the field then it is to just  Applied that the field in post you have way more control doing it in nuke  It's way faster to do it in nuke  So that's why we do it that way all that it made possible because of the 32 bit Z depth pass now  That brings me to my next point

**Frame:** tutorials\frames\improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn\frame_002.jpg

### Limitation / Issue #3 - Lack of 32-bit .EXR Zdepth [6:29]
**Transcript:** So another gripe that I've had with the movie render queue so far after you think it for a week is the lack of 32 bit support  Now as you can see here we have got EXR sequence 16 bit for most cases  This is going to be more than enough especially with the sub sampling  You don't need 32 bit color data, but it we want 32 bit depth  We want a proper 32 bit floating point data because it's just going to give you that much better result now  If you use the sequencer we're going to go to sequencer tab here, right? We're going to go to render this video and  Custom render passes here. You can do  Seen depth world units and this is actually a Z depth Z depth pass if you capture frames in HDR it technically renders it out  At a 32 bit EXR, but  The cover using sequencer you lose the benefit of the sub sampling you don't get the high quality render that the movie render queue offers with sequencer  Sequencer is kind of handicaps in that respect  But it does offer a 32 bit Z depth pass. It's not very good especially around along the edges  So if let's say you've got a character and  Detail behind him the edge of the character in there can be really bad especially when you get motion blur  And lots of effects and stuff like that. So  Z depth is still not quite there yet. Don't get me wrong the movie render queue is a great step forward  Gone leaps and bounds from sequencer, but  We don't look in here and in the movie rena q is the  Render passes here. We don't have a proper Z depth and that  That that really sucks. This would make for me that would make the movie rena q the complete package, but unfortunately  It's not  This is once again  This is a great release amazing feature that we can get with sub sampling  But it's not quite there yet

**Frame:** tutorials\frames\improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn\frame_003.jpg

### Handy Feature #1 - Render Presets [8:23]
**Transcript:** Now one nice little feature that i'm using all the time and that's the little presets button up here  Now you may or may not have seen it already, but i think i should mention it anyway  If you've got you know a lot of stuff set out here especially console variables  You know you got a long list of things that you don't want to have to go find online  Copy paste every single time you know you if you're elaborately set up your your render path and everything your resolution  And you don't want to change it every single time you render a shot you can save a preset  So you can just click on the presets button up here save as preset you choose where you want to save it  Click save and there it is now every single time you want to add a new job  Let's go ahead and let's delete this right here  So let's say i'm going to go let's say i'm going to go ahead and add burn in  PNG sequence and object ID here okay, so i got a very complex thing  I can go ahead click presets save as preset and say preset William  Save and now you can kind of go get  Whatever preset you want every single time without having to re-enter your data. This is not a ground breaking  Trick but it's good to know

**Frame:** tutorials\frames\improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn\frame_004.jpg

### Handy Feature #2 - Render Queue [9:30]
**Transcript:** Now the last thing we're going to talk about and this little trick here is the main reason i made this video to begin with  And this is the neat little tool that i'm going to use all the time  This is going to save me so much time and that feature is well  The render queue okay, I didn't cover this for my first video. I'm covering it now  It should go without saying it says it in name a render queue  So as you can see we've got map one shot one here. I've gone ahead and i've made two other shots  So we're going to go ahead and click the render button here  We're going to add shot two and we're going to add shot three  Now before which sequencer you had to open up the map  Click the button down here  rendered this video  capture movie  wait for it to render then you had to you know open up the next map capture movie  Open up the next map and so on and so forth you had to do this for every single shot  It was an extremely time consuming process  If you wanted to if you had 50 shots to render you were going to be up all night  Opening it up every single map and running them out  but now with the movie render queue  And this should go without saying because it said that in the name render queue  You can go ahead and just add all these  And now because we have presets made you can kind of just go ahead and configure these  So we can have preset login here or you know the regular  Preset that I have here  chew their output and just render everything in one go  This seems obvious but if you don't already know about this  This is going to make your life so much easier  So all you need to do next it did hit render local and  Let her rip  And now shot two  And shot three  So as you can see you don't need to open up those maps anymore  You can just go add it from one window and render out your entire sequence  Whether it's you know two shots or a hundred shots  This saves me a  Colmossal amount of time. I am so thankful for this neat little feature

**Frame:** tutorials\frames\improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn\frame_005.jpg

### Outro [11:34]
**Transcript:** So as always I hope this has helped you guys out  If you have any questions whatsoever  Don't hesitate to leave a comment down below  I'll get back to you as soon as I can  Don't forget to like and subscribe and I'll see you guys next week

**Frame:** tutorials\frames\improve-your-renders-with-movie-render-queue-part-2---five-things-you-need-to-kn\frame_006.jpg


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
