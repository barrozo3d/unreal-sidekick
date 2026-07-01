---
title: Budget Mocap Tutorial - Quickmagic.AI and Metahuman Animator (Android/Frame Mancer) Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=i2W2rDsZXk4
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-23
ue_version: "UE5"
tags: [mocap, metahuman, performance-capture, quickmagic, metahuman-animator, android, face-capture, retargeting, budget, cinematics, lighting, camera-shake, elevenlabs, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-/
frame_count: 13
---

# Budget Mocap Tutorial - Quickmagic.AI and Metahuman Animator (Android/Frame Mancer) Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=i2W2rDsZXk4)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 12m40s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In this video, I set out to create a cinematic performance capture scene in Unreal Engine using some of the cheapest tools on the market.  But while these tools might look good for short, tick-tock dances or action shots,  I wanted to find out if they could actually be used for an actual performance with Metahumans.  So I'll be using Quick Magic AI, a MoCAP solution that can get full body and hand animation from a single camera of any kind.  And for the face animation, I'll be using our trusty Metahumane animator.  But this time there's a catch.  I'll be using an Android phone instead of an iPhone.  Thanks to a $20 plugin called FaceDepth Frame Mancer,  Metahumane animator can now be used with any kind of camera.  This rapidly evolving technology is lowering the barrier to Unreal Engine filmmaking like crazy.  So if you're looking to get started as quickly and cheaply as possible, this one's for you.

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_000.jpg

### FINAL FILM [0:51]
**Transcript:** One document in the middle of the night.  Two dead bodies got up to fight.  Back to back, they faced each other.  Do their swords and shot each other.  A deaf man heard the noise and came to kill those two dead boys.  If you don't believe my story's true, ask the blind man in the car.  He's out of tune.  Alright, thanks for watching.

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_001.jpg

### Using QuickMagic for Body Mocap [1:19]
**Transcript:** Before we get started, I want to mention that this video is not sponsored in any way by any of the companies mentioned.  So that said, let's jump right into using QuickMagic.  So this actually ended up taking me a few takes to get a capture I was happy with.  This is just the reality of using these entry-level tools at this current stage.  So really try to give yourself the best conditions for the best capture possible.  I actually found that having the camera handheld rather than static on a tripod seemed to give me  the most stable animation with the least amount of jitters in the hips.  No idea why, but I ended up getting one I liked on the first take of doing it handheld.  And I mean, look how good the hand animations are right out of the box.  And this is one of the cheapest solutions I've found yet.  This cost about $2 worth of credits and took about 10 minutes to process with their paid tier,  which is $10 per month.  As I mentioned, this video is not sponsored by them, but I do have an affiliate link for QuickMagic.  So if you want to try it out and support the channel at the same time,  consider using my co-blow or click here to sign up.  Now, there are a few things in this animation that need to be corrected,  like a few wobbles of the legs or my phone, including my face and messing with the head orientation,  but that's easy enough to fix and on real engine.  So at the same time I was recording the body animation, I was recording the face animation using

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_002.jpg

### Using the Headrig from FaceMotionCapture [2:40]
**Transcript:** my Android phone mounted to my head using a head rig from FaceMotionCapture.com.  Now, full disclosure, I was sent this for free, but I'm under no obligation to say anything about it  or even use it at all in a video. I've just included it in this video because there are not a lot  of great head rigs that I have found in this price point, which is $100. I normally use the  Rococo head rig, which I really like a lot, and I would recommend if you have the money, but  that's $300 to do exactly the same thing. So for lack of better alternatives at this price point,  I can recommend this one, and I've put a link in the description. If you want something even cheaper,  I show how to build your own head rig in my super in-depth budget performance capture tutorial  right here. So now that I have the performance capture and body animation processed on quick magic,

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_003.jpg

### Using Frame Depth Frame Mancer Plugin with Metahuman Animator [3:34]
**Transcript:** I need to bring the face capture footage into Unreal to process with MetaHumanAnimator.  Now, I was going to include a whole step-by-step tutorial and process on installing and using the  frame-mancer plugin, but here's a much more in-depth tutorial on it from the developer himself.  Keep in mind the plugin costs $20, but that's a lot cheaper than an iPhone. Basically, you import your  footage into Unreal and using frame-mancer extract the frames from the video. Frame-mancer will then  use AI to create a depth map for each frame. The frames and depth maps are then combined to create a  capture source, which is then used in the normal MetaHumanAnimator workflow to create the face animation.  And it really is that easy. The plugin adds just a few clicks to an already very simple process for  getting incredible face animation. Now, I would say I'm not getting quite as accurate of a capture as  when I use my iPhone 13, but this is still very good, probably 90% of the way there, and the developer  just added a brand new camera calibration function that I didn't do, but would probably increase the  accuracy beyond what you are seeing here. I ended up doing a few small tweaks to the animation to  make it pop just a little bit more, which I'll show later in the video. Also, one important thing to  keep in mind if you are using this plugin. Do the face capture and MetaHumanAnimator process  as the very first step in your project. Before you even add a MetaHuman to your project,  I'm not sure why, but I kept crashing while processing the animation unless I was doing it in  an empty project. Next, I'll download and add a MetaHuman to my project and then import my animation

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_004.jpg

### Setting up a Metahuman with the Animations [5:15]
**Transcript:** from Quick Magic. Then it's super easy to retarget the animation for MetaHuman's, which you can do  using the animation retargeter. Now I can get the animations onto a MetaHuman into a level sequence.  And this is looking pretty good considering the cost of the tools we're using, but it's definitely  missing something that will make it way more interesting to work on, and that's a voice that  actually fits the character I'm animating. So, to morph my voice using AI, there's no better tool  than 11 laps, which I've used a bunch on this channel. Marvin. Marvin, come in. Are you seeing this?

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_005.jpg

### AI Voice Morphing with ElevenLabs [5:47]
**Transcript:** Apologies for the weight that gets them through throughout this.  You just upload the clip of your dialogue that you want to morph and select the voice you want to  change it to. One dark morning in the middle of the night, two dead boys got up to fight.  So, if you want more if you're voice like this and support the channel at the same time,  please consider using my affiliate link here or in the description. So, to take this animation to

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_006.jpg

### Camera Settings and Setting up the Scene [6:19]
**Transcript:** a more cinematic level for lack of a better term, I decided to use some high quality assets from  Fab. I used this amazing medieval village from the scans factory and I just kind of scouted it  around until I found an area I thought would look good. And I had this asset in mind when I thought  of the video, especially because it had this darker lighting scenario that had great atmosphere  with the volumetric fog and small fires throughout the scene. And for the character's clothing,  I went with the medieval clothing pack from Polyphoria, which I think is some of the best medieval  and fantasy style clothing for metahumans on the market. Now, once the character is in place and  added to the sequencer with animations, I like to get a camera up and the shot framed as soon as  possible. So, to keep the camera focused on the character, I attached a small sphere to her  headbone in the sequencer. I make it invisible and then I add a camera. And for the most cinematic  camera settings, I like to set the film back to 35mm VistaVision and then set the crop to 16x9.  Then set the focus settings to tracking and select the sphere under the actor to track. Now, I can  keyframe the camera movement however I want and the character will be in focus the entire time.  I also added some handheld camera shake, which you can do by creating a camera shake-based  blueprint component. In here, you can change these parameters to change how the camera moves and  how intensely. So, set the duration to minus one to make it generate a continuous shake without  stopping. You can then add it to your camera in the sequencer and drag it out for the length of  your timeline. Now, I ended up changing these settings as I went, so here are the ones I used to  get my camera to move how it does in the final animation. And before I go any further, remember to  set your sequence to 24 frames per second. That's what that's the frame rate that films you. So,  if you want your animation to look more like a movie, set it to 24. It's probably at 30 frames per  second as the default. Now, for the lighting, I wanted it dark basically nighttime and one of the

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_007.jpg

### Lighting [8:30]
**Transcript:** fire next to her to be the main light illuminating her face. So, to kind of supplement the fire,  I added a spotlight from the angle of the fire to make the fire light hit her face better.  And I deleted the skylight from the scene to make the shadows darker. And I played with the  exponential height fog settings quite a bit to get the color to look more like nighttime.  The directional light was angled and colored blue to look like the moonlight and give her an  edge light from behind. And then the lightning is actually just another spotlight that's really bright  and then I've added that to the sequence and activated and deactivated that based on when I want  the lightning to show up. And here I'll show the few tweaks I did to the animation. I baked the

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_008.jpg

### Animation Tweaks [9:18]
**Transcript:** face animation to the face control board then added an additive track to the face control track  where I can make non-destructive edits and add keyframes and make adjustments to the whole  performance of the face. In this case, I felt the crazy wasn't really coming through in the eyes.  So, with the additive track selected in the sequence, or I can then select the eyelid tweaker in the  control board and just open the eyes more. For the hands, I didn't have to do much since the capture  was so good. I just had to rotate the thumbs around which I think is an error with the retargeter.  I mean, this hand tracking is just incredible. Better than Move Pro for sure. I also corrected the  eye line to look exactly at the camera which can be done using a constraint but since I was  bouncing between multiple cameras, sometimes it's easier to just add some keyframes and call it a day.  And of course, I corrected the head orientation where the tracking didn't quite get it right.  Now, I really wanted to get a good rain effect going since I thought the lighting on the wet

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_009.jpg

### Rain Effects and Camera Dirt/Water Droptlets [10:17]
**Transcript:** skin would look a lot better and would add to the ambiance. To achieve the effect, I actually  used two different rain assets from Fab, this animated rain material and easy rain by William Fauschet.  Easy rain was used for the actual rain drops and the animated rain material was used to create  the wet effect since it was easy as just dragging the box into the scene and it overrides all the  materials including the metahumans. And what I think really is the cherry on top here is the dirt  mask I applied to each of the camera angles. I just downloaded a couple images of water and dirt  on camera lenses and applied them to each camera's dirt mask slot. One thing, you have to input a  higher number to get it to show up. Just dragging the slider all the way up doesn't seem to make the  effect visible, at least not enough for what I was going for. And then really the lighting is

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_010.jpg

### More Lighting [11:14]
**Transcript:** then crafted and shaped for each individual shot. I add new lights to the scene to help the  light wrap better from a different camera angle and hide other lights that were used in other shots.  In this case, I'm using two spotlights to help accentuate the fire light and the moon light.  Since the spotlights have a nice hard light that will create nice shadows and make the wetness pop  more and their direction and spread can be easily controlled. And the nice thing about Unreal Engine  is the lights themselves are invisible. So you can put small dim ones really close to the character  to help get the effect you want. And as a general guideline, I try to light the character from the side.  And I'm using some basic color principles and using complementing colors like orange and blue,  which look good and feel motivated by the fire and moonlight. So there you have it. Let me know

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_011.jpg

### 12:40 Outro [12:12]
**Transcript:** down in the comments what you think. Could you see these tools being used to create a whole short film  or even more? If you have any questions about the process or just want to chat more about Unreal  Engine filmmaking, stop on by our Discord, which is growing steadily and is becoming a great  community to share your work and see what others are working on. All right, I'm Charlie.  Thanks for watching and I'll see you in the next one.

**Frame:** tutorials\frames\budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-\frame_012.jpg


---

## Structured Notes

### Core Technique
Budget performance capture pipeline: QuickMagic AI (~$2/take or $10/month) for full body + hands from single camera; FaceDepth Frame Mancer ($20 plugin) to use Android phone with MetaHuman Animator instead of iPhone (AI depth map per frame → standard MHA workflow); retarget to MetaHuman; ElevenLabs for AI voice morphing; camera-tracking via invisible sphere on headbone; camera shake via Blueprint component; complementary orange/blue lighting (fire + moonlight).

### Summary
12m40s production diary by Charlie Driscoll. End-to-end budget performance capture cinematic: (1) QuickMagic AI body mocap — handheld camera gave best stability; cost ~$2; 10min processing; hand animation out-of-box quality exceeds Move Pro; (2) FaceDepth Frame Mancer plugin ($20) — enables MetaHuman Animator with any camera (Android); import footage → plugin extracts frames + AI depth maps → creates capture source → standard MHA workflow; do MHA processing FIRST in empty project (crashes otherwise); (3) MetaHuman retarget animation to custom MetaHuman; (4) ElevenLabs voice morphing for character voice; (5) Scene setup: medieval village (Fab), medieval clothing (Polyphoria); camera attached via invisible sphere on headbone for auto-tracking focus; camera shake Blueprint component (duration=-1 for continuous; tune frequency/intensity); 24fps sequence; night lighting: spotlight for fire at angle, delete skylight for dark shadows, height fog tweaked, blue directional light as moonlight/edge light, keyframed spotlight for lightning effect; (6) Animation polish: bake face animation to Face Control Board, add additive track for non-destructive edits (open eyes, fix eye line, correct head orientation); (7) Rain via two fab-assets (Easy Rain for droplets, animated rain material for wet override); camera dirt mask (water/lens images → camera dirt mask slot; input high number not just slider); per-shot lighting adjustments.

### Key Steps
1. **Body capture**: use QuickMagic AI (browser-based); handheld camera works better than tripod (more stable hip animation); record on neutral lens (no wide angle distortion); export for UE4 mannequin skeleton; ~$2 per take
2. **Face capture (Android)**: use Frame Mancer plugin ($20) for FaceDepth; do MHA processing first in empty project before adding MetaHuman; import face footage → Frame Mancer extracts frames + AI depth maps → creates capture source → run MetaHuman Animator normally
3. **Animation cleanup**: bake face animation to Face Control Board; add Additive Track for non-destructive edits (eyes, eye line, head orientation, thumbs via FK);  fix head orientation keyframes
4. **MetaHuman setup**: import QuickMagic FBX (skeleton=none); RMB animation > Retarget Animation > select MetaHuman skeleton > export; drag MetaHuman to level; add to sequencer; delete control rigs; add animation track with retargeted clip
5. **Camera tracking focus**: attach invisible sphere to character head bone in sequencer; add camera; focus settings → Tracking → select sphere actor
6. **Camera shake**: create Camera Shake Blueprint; set Duration=-1 (continuous); tune frequency/intensity parameters; add to camera in sequencer; drag out for full timeline length
7. **Lighting (night)**:
   - Delete Skylight (darker shadows)
   - Add Spotlight angled from fire direction (simulate fire on face)
   - Directional light: blue color, angled for moonlight edge light
   - Exponential Height Fog: tweak color for nighttime atmosphere
   - Lightning: bright spotlight keyframed on/off in sequencer
8. **Rain**: Easy Rain (Niagara, actual droplets) + animated rain material (box drag into scene; overrides all materials including MetaHuman for wet look); camera dirt mask slot (images of water/dirt on lens; use high numeric value, not just slider)
9. **Per-shot lighting**: hide/show lights per camera angle; supplemental spotlights close to character (hard light for shadows, orange/blue complementary colors); UE lights are invisible so can be placed very close

### UE Systems / Blueprints / Settings
- **QuickMagic AI**: browser platform; AI MoCap tab; T-pose for best results; options: full body + hands, T-pose, moving camera, UE4 mannequin, on-real-floor export; ~$2/take or $10/month
- **Frame Mancer plugin** ($20): FaceDepth extraction from any camera; process in empty project first; standard MetaHuman Animator workflow after
- **Retarget Animation**: RMB animation > Retarget Animations > select target skeletal mesh > Export Animation
- **Camera focus tracking**: Focus Settings → Tracking → Actor reference (invisible sphere on headbone)
- **Camera Shake Blueprint**: Duration=-1; frequency/intensity params; add to camera via sequencer
- **Additive track (Face Control Board)**: bake face animation → + Additive Track on face control rig track → non-destructive edits
- **Rain materials**: Easy Rain (Niagara asset from Fab), animated rain material box (overrides all mats)
- **Camera Dirt Mask**: in camera post-process settings; needs high numeric value to show effect

### Difficulty
Intermediate

### UE Version
UE5

### Tags
[mocap, metahuman, performance-capture, quickmagic, metahuman-animator, android, face-capture, retargeting, budget, cinematics, lighting, camera-shake, elevenlabs, intermediate]

---

## Related Entries
- cheap-ai-mocap-that-actually-works---quickmagicai-chaos-destruction-and-metahuma.md (same author, QuickMagic tracking shot)
- how-i-made-this-aaa-cinematic-in-unreal-engine-5---moveai-and-metahuman-animator.md (Move AI vs QuickMagic)
- budget-mocap-tutorial---quickmagicai-and-metahuman-animator-androidframe-mancer-.md (this file)
