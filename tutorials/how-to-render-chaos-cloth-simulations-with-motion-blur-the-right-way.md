---
title: How to Render Chaos Cloth Simulations with Motion Blur [The RIGHT Way]
source: YouTube
url: https://www.youtube.com/watch?v=f4izPHpbfZI
author: Boundless Entertainment
ingested: 2026-06-16
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way/
frame_count: 10
---

# How to Render Chaos Cloth Simulations with Motion Blur [The RIGHT Way]

**Source:** [YouTube](https://www.youtube.com/watch?v=f4izPHpbfZI)
**Author:** Boundless Entertainment
**Duration:** 14m6s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** What's going on guys Sam here and in today's video we're going to be covering a little bit about  Chaos Cloth Simulations. So our main concern in this video is rendering our Chaos simulation  with motion blur using the movie render queue. So we're going to be using temporal sub sampling.  If you don't know what that is we're going to get into that later in the video but the problem  with temporal sub sampling is that it causes a lot of issues when you're working with Chaos Cloth  Simulations. So this video is for anybody who wants to use Chaos Cloth Simulations but still be  able to render with high quality motion blur. And you guys are really going to want to stick around  to the end of this video because there is a weird buggy caveat to this process that you're going  to need to know if you want to actually make this work properly. And then I'm also going to be doing  a little bit of a giveaway at the very end of this video that you guys are going to want to stick  around for. The key is we're going to be using caching for our Chaos Cloth Simulation in order to  accomplish this. So what I have here is this little scene that I've created for the Unreal Engine  for Filmmakers cours...

**Frame:** tutorials\frames\how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way\frame_000.jpg

### Adding Wind [1:26]
**Transcript:** helpers in my scene. And you can see that I have a wind actor right here. So you're going to find  that by simply going into place actors and go to wind. And we're just going to add a wind  directional source. These are good starting point if you want just a little bit of wind in your scene.  So let's go ahead and just hit simulate. And that's going to show us the simulation in our viewport.  This wind is now actually blowing this cape around as well as these little shoulder  dusters that he has up here. Now we want to get into what this tutorial is really about and that  is going to be how to render this. So what happens when you go to actually render this is if we go

**Frame:** tutorials\frames\how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way\frame_001.jpg

### Temporal Subsampling Explained [2:00]
**Transcript:** in here and render I have a render preset setup here already. So when we're rendering something  and I'm using a deferred rendering but this is the same concept with a path trace rendering.  We're going to want to use a higher temporal sample count in order to get high quality motion  blur. So temporal samples essentially break up each frame into the specified number of subframes.  So in this case 21 subframes what that does is like for example this snowflake that's moving here.  Each frame of the sequence that we're rendering is going to be broken up into 21 subframes and  that snowflake is going to move just a little tiny bit in each of those subframes. And when those  subframes are combined together into the final image by Unreal Engine we see that little bit of  movement over those 21 frames all combined together as motion blur. So that's how we get high quality  motion blur inside of Unreal Engine because otherwise we're going to be relying on the motion blur  post processing effect which is not ideal. The problem with that is that when we actually render with  temporal sub samples right here in our anti aliasing settings it's going to cause the cape to do  all kinds of crazy ...

**Frame:** tutorials\frames\how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way\frame_002.jpg

### Caching Explained [3:23]
**Transcript:** actually cache the animation of our claw simulation. So we're going to run the simulation inside of  our editor and we're going to actually capture the animation inside of our editor so that we actually  have it as essentially an animation asset the same as the animation asset I have right here for my  character except it's just going to be the cloth. Then what we're going to do is because we have  that cached we don't then have to actually simulate the cloth when we render. So it's already pre-simulated  those frames are saved and it's just going to render them as it should and then we are able to render  with high quality motion blur without any problems. And the way that we do that is with the take  recorder. So in a second we're going to get into that but first chaos cache managers are going to  give us the option to control things like the chaos destruction simulations that are available in  Unreal Engine as well as the chaos cloth simulation I'm about to do. So we can drag and drop one of  those into our scene but instead we want to actually make one based off of a particular actor. So  we're going to choose in this case our revenant character right here and we're going to go...

**Frame:** tutorials\frames\how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way\frame_003.jpg

### Setting up the Take Recorder [5:48]
**Transcript:** going to go to take recorder. That's going to close out of the sequence that we had just loaded up.  Don't worry we're going to get right back into it in a moment. If you've ever worked with  Vive trackers you might have encountered the take recorder previously it's also used for like  Niagara fluids or chaos simulations. Basically a way of capturing live data and pulling it  into Unreal Engine and also at the same time caching that data if you choose. We need to open our  sequence so we're going to click on this little arrow right there and this is where we can open a  sequence to record into and we're just going to scroll down and find the shot that we need which  is this one in my case and here we go we're right back into our sequence. Alright so now we actually  need to add the source of our simulation which is going to be our chaos simulation so we're going  to go down here to source and we can choose from actor and that's what we're going to use. You can  also choose like a live link source that's if you're doing virtual production with like a Vive  camera tracker or chaos cache we're not going to use that we're going to make sure that we use  actor from actor and then we're ...

**Frame:** tutorials\frames\how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way\frame_004.jpg

### Using the Take Recorder [9:03]
**Transcript:** record on the take recorder it's going to give us a nice countdown to one and bam it's going to  start recording so you can see it's going through our timeline and recording with the animation  right here. All right it reached the end so it stopped automatically now we can just go ahead and  hit stop here on our simulation. So all we did there was play our simulation let it simulate as  if we were playing a game and then we just recorded the animation for the actor that we specified  right here in our take recorder. That's the basic process behind any simulation caching for  Unreal Engine. The process itself might look a little bit different but that's the basics behind  the concept. All right so if we go in here we can now play back our animation and see what we got  here. At this point we're going to want to save everything so go file save all. Now there's a bit

**Frame:** tutorials\frames\how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way\frame_005.jpg

### Chaos Cache Sequencer Bug Fix [9:57]
**Transcript:** of a caveat with this and it seems to just be simply a bug with with Unreal Engine. We actually  have to get rid of this chaos track right here and then re-add it in order to actually save  this animation because if we go ahead and just go and render this right now it's actually going  to re-simulate it during the render and overwrite this work that we've done here. So we're going to  close out of the take recorder first. Okay that's the first thing and we're going to go into our  sequence right here. You can see that we have our nice cached simulation and what we're going to do  is make sure that we've saved everything and then we're going to go ahead and just delete this.  But all we're going to do here is grab our chaos cache manager and we're just going to drag and  drop it right here into our sequence. You don't have to put it under this folder. I'm just doing  that because that's how it did it initially. Okay so we're almost back to where we were. We're going  to click on the chaos cache manager and we're going to click plus track and we're going to do chaos  cache right here. Okay and there we go you're going to see that we actually have our chaos cached  simulation right ba...

**Frame:** tutorials\frames\how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way\frame_006.jpg

### Rendering [11:43]
**Transcript:** is go ahead and render this. So I've got this render preset setup. What we're going to do is I do  EXR sequence 16 bit deferred rendering. You can also use path tracing with this but when it comes  to anti aliasing we're going to set the method to none and we're going to set the spatial sample count  to one and we're going to set our temporal sample count to 21. You can set this to whatever you  want to. As I said before the temporal sample count is going to increase the quality of that motion  blur the more you increase it. Color output I have an OCIO config. If you want to learn more about  the all this stuff I covered in great detail in the unrelegied for filmmakers course I'm also  going to be making some videos about some console variables that I've come across that are really  helpful for things like heterogeneous volumes fixing some issues like I had some flickering going on.  So stay tuned for that video we're going to make sure that we have the game overrides turned on  and then we set our output and we're ready to go here. So we can go ahead and click on render  close out of this and then we're going to click on render local and we're going to get a proper  final result w...

**Frame:** tutorials\frames\how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way\frame_007.jpg

### Ways to Learn Unreal Engine [12:51]
**Transcript:** that's just getting started that's going to get you well on your way to creating awesome scenes  like this as well as the unrelegied for filmmakers course will recover everything about this scene  as well as several other scenes and then also we have just come out with the virtual filmmakers  playbook course which is going to teach you indie virtual production in literally any space.  We made a pretty massive film inside of basically a closet it was like a two by two meter space  or something like that and I partnered up with Joshua M. Kerr on that project turned out amazing  and if you guys want to see that I will leave a link to the video where we talk about that in  the description and also in the upper right corner of this video. So I'm going to leave a coupon

**Frame:** tutorials\frames\how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way\frame_008.jpg

### Giveaway :P [13:36]
**Transcript:** code in the description of this video for the first 100 people it'll be 20% off anything on the  website that includes the unrelegion for filmmakers course the virtual filmmakers playbook and even the  bundle. Now if you missed this one just make sure that you subscribe to the channel I'm going to be  continuing to release some of these coupon codes just kind of show my appreciation for you guys  support and to help out anybody who is watching my channel because I really do appreciate you guys  checking out these videos so thanks again for watching and I hope you guys have a good one.

**Frame:** tutorials\frames\how-to-render-chaos-cloth-simulations-with-motion-blur-the-right-way\frame_009.jpg


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
