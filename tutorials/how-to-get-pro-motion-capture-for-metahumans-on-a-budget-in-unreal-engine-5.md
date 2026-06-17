---
title: How to Get PRO Motion Capture for MetaHumans on a Budget in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=wys5jEhtpY0
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-17
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5/
frame_count: 25
---

# How to Get PRO Motion Capture for MetaHumans on a Budget in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=wys5jEhtpY0)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 13m8s | 25 section(s)

---

## Raw Data (for Claude Code extraction)


### Why this kind of animation used to cost thousands [0:00]
**Transcript:** This kind of animation captured for Unreal Engine using performance capture  typically requires a professional multi-cam motion capture setup and that  usually means thousands of dollars in software and hardware at least it did until  very recent. It turns out Mima Mei is a multi-camera  markerless mocap solution that has kind of flown under the radar for the last seven or eight months  and in theory it has features similar to studio grade systems like Move Pro but at a much cheaper  price point. So in this video I'm going to see if Mima really is the indie multi-cam mocap solution

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_000.jpg

### Introducing mimem.ai (multicamera markerless mocap) [0:38]
**Transcript:** we've all been waiting for and check this out it can even do treadmills.  Hi I'm Charlie and for the last year and a half on this channel I've been trying to answer a

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_001.jpg

### Channel goal: pushing Unreal Engine with cheap tools [0:55]
**Transcript:** very simple question which is how far can you realistically push Unreal Engine filmmaking if you  deliberately limit yourself to the cheapest and simplest mocap tools possible. In my last tutorial  I showed what I still think is the easiest and cheapest way to do single camera performance capture  for metahumans in Unreal Engine 5. You can use a single android phone to capture both face and body

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_002.jpg

### Cheapest single-camera MetaHuman capture recap [1:19]
**Transcript:** at the same time without the need for a head rig and I think you can do a lot with that very simple setup.

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_003.jpg

### When single-camera mocap hits its limits [1:34]
**Transcript:** But what if you want to take your performance capture to the next level? You know incorporate a  head rig to capture your face and maybe add another camera or two for more complex blocking  or even capture two actors at the same time. The only viable option I had found for multi-camera  mocap was move pro and I've used that a lot on this channel. It has incredible quality and can

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_004.jpg

### Move Pro overview and studio-grade pricing [1:57]
**Transcript:** handle multiple actors with complex blocking and is definitely a studio grade system.  But with that quality comes studio level pricing starting around $7,000 per year.  But the cheap single camera mocap solutions seemed so close for so many use cases.  If only you could just add one or two more cameras for a little bit more money.

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_005.jpg

### The gap between single-cam and multicam mocap [2:23]
**Transcript:** And I don't mean expensive cameras. I mean cameras that anyone could get their hands on.  Like a webcam or a laptop's webcam and an android phone. Well it turns out Mimma AI's cheapest  tier starts at just $25 per month and it allows you to do exactly that.

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_006.jpg

### Mimem’s $25/month entry tier explained [2:41]
**Transcript:** So here you can see Henry the zombie who is captured using two 1080p webcams and a phone at 30  frames per second and processed using Mimma's $25 tier. For reference I'm captured using six  go pros and processed using Mimma's more expensive tier. But we'll get to that in a minute.  For now I want to show you just how easy it is to use Mimma's in browser mocap using three  cheap cameras. So if you go to Mimma.ai and select new animation you can choose between uploading

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_007.jpg

### Recording multicamera mocap in the browser [3:14]
**Transcript:** your own footage or recording in browser with webcams and smartphones which is what we will try first.  Now on this page you can select the cameras you want to use. So I'll turn on the external webcam,  my laptops webcam and then I'll hit the big green iOS slash android button to bring up a QR code  which I scan with my phone which connects over Wi-Fi. Make sure your phone and laptop are on

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_008.jpg

### Camera placement tips (webcams + phone) [3:46]
**Transcript:** the same Wi-Fi network. Then you can set your phone up to capture your third angle.  You can see I tried to keep them as wide as possible with at least two getting a good view of my  feet but as you will see it is not too important that you stay in frame the entire time.

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_009.jpg

### No calibration or sync required [4:04]
**Transcript:** Now you can start recording and moving about your volume. No need to calibrate or sink your footage.  And honestly I'm really impressed with just the raw capture. As you can see it gets pretty decent  hand tracking and that will actually improve the closer you are to the camera. But overall it's  staying really stable as I move around the volume, turning in all different directions.  It's not getting confused or anything. I mean getting down on the ground and then back up like  this again would be very hit or miss with a single camera solution. And the fact that this work  was what gave me the idea to do the zombie scene as a demo. And the fast motion works really well  even at 30 frames per second which I think is a limitation of the browser-based recording. If you  upload you can upload higher frame rates. So once you are done recording you can hit stop recording

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_010.jpg

### Reviewing takes and inserting a T-pose [5:08]
**Transcript:** and make sure to wait for your phone to finish uploading its footage. Then click next to go to  the review page. Here make sure you select this option that says insert T-Pose at keyframe zero  or you will have issues retargeting your animation in Unreal Engine. Then hit next name your animation

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_011.jpg

### Processing time and exporting FBX [5:29]
**Transcript:** and it will start uploading and processing. Now how long this takes will depend on your internet  connection and how long you recorded for. But for me it took about 13 minutes total for a minute  and 40 seconds of recording. Once it's done you can review the animation and download the FBX for  Unreal Engine. Now when importing it is very important to generate a new skeleton for each animation.  Since there can be slight variations in the skeletons in different animations. So every time you

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_012.jpg

### Importing into Unreal Engine correctly [6:04]
**Transcript:** import an animation make sure you drag it into a new folder and uncheck import animations only.  Also make sure you check this use T-Zero as ref pose.

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_013.jpg

### Retargeting animations to MetaHumans [6:20]
**Transcript:** Then you can retarget your animation to met a human using the retargeter.  Hey hey come check this out. So here you can see I have the exact same footage from my sword fighting

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_014.jpg

### Sword fighting test: Mimem vs Move Pro [6:39]
**Transcript:** animation pack process twice. On the left I have two actors captured with six go pros and processed  using move pro. The $7,000 per year system. On the right we have memeum which is using just  three of the six go pros and cost $25 per month. Now this is just the raw capture for both systems  but they're both really good. They're both very much spatially accurate and anytime you can do  two actors doing dynamic choreography like this with marcarless mocap it's just super cool but  I think given the cost and ease of use memeum is just incredible.

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_015.jpg

### Limitations of Mimem’s multi-actor capture (beta) [7:40]
**Transcript:** Now I want to be very clear move pro is still the better option if you are looking to do complex  character interactions with multiple actors. memeum's multi actor capture is still in beta  not even advertised and still has some limitations. For example the actors cannot  occlude each other from any of the camera's views. This is actually why I only use three of the  go pros instead of six because both actors are not always fully visible from all angles.  And in this animation they don't actually move past each other or contact each other at all.  If they did the animations would start to break down. Now I know memeum is working on this feature  and I expect it to get a lot better but for now move pro has consistently very impressive results  with very complex choreography. And if you want the final cleaned up versions of these animations  they're available on fab. They are designed to work with metahumans and my crowd simulation plugin  overcrowd so you can start making duels and battle scenes as quickly as possible.

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_016.jpg

### Mimem Pro tier and 10-camera support [8:53]
**Transcript:** Now I want to get to what I think is the true game changer for indie performance capture  which is memeum's pro tier which starts at $200 per month. As I mentioned earlier this whole video  my animations have been captured and processed using the pro subscription which allows you to add up  to 10 cameras. I have been using 6 GoPro 10s recording at 4k 60fps which is the exact same setup I  use with move pro. I also use this same setup to capture the zombie cinematic I teased at the

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_017.jpg

### Six-camera GoPro setup (4K 60fps) [9:21]
**Transcript:** beginning of the video. This setup allows me to capture more complicated movements like  walking down the stairs like this. Something that can be pretty tricky when just using a single camera  solution. Even this movement where I am creeping along the wall looking over my shoulder

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_018.jpg

### Stairs, creeping movement, and ground contact [9:41]
**Transcript:** you know could be done with one camera but likely would not be as spatially accurate.  And of course the encounter where both characters get knocked down with the ground and crawl around  would be next to impossible with a single camera.

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_019.jpg

### GoPro remote recording tip [10:14]
**Transcript:** One quick tip. If you are recording with GoPro's you can use an app called camera tools for  GoPro heroes from toolsforgopro.com. This allows you to connect all your GoPro's to an iPad or  PC and control them all remotely so you can start and stop their recording at the same time.  So overall I am extremely impressed by memeum including the ease of use price and performance.

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_020.jpg

### Mimem credit system explained (tokens & daily limits) [10:42]
**Transcript:** You can even try it with 3 cameras for free. Keep in mind they do have a credit-based system  with daily amounts being issued. These tokens do not accumulate. These are the amounts you can  use daily. And the way the token system works is essentially one token equals 30 frames of video input.  So at the $25 per month tier with 500 tokens per day recording with 3 cameras at 30 frames per second  you get about 2.8 minutes of mocap processing per day. And using 6 cameras at 60 frames per second  on their pro $200 per month tier you get close to 7 minutes of mocap processing per day.

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_021.jpg

### Head rig options for facial capture [11:27]
**Transcript:** Now another thing I want to quickly talk about is the fact that I used a head rig. I used a  Rococo head rig which costs $295 and can hold a phone for recording your face. I really like this  head rig and use it a lot. It's comfortable and adjustable and I really like giving it to  actors when they come in to do motion capture. And if you want something cheaper I have used the  head rig from facemotioncapture.com which costs about $100 and it will definitely get the job done.  I have not tested that one with memeum but I haven't had any issues using it with my other mocap  solutions. Now before we go I want to quickly plug my crowd simulation plugin overcrowd.

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_022.jpg

### OverCrowd plugin overview and updates [12:14]
**Transcript:** This is one of the most powerful tools on fab allowing you to create massive crowds and  armies of modular meta humans in Unreal Engine for cinematics and games. We will have a version for  Unreal Engine 5.7 coming very soon. It is currently in testing and might be out by the time you see  this video. We have some other very exciting updates coming as well which will make overcrowd  way more powerful for gameplay and real time applications. And we will also be releasing some

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_023.jpg

### Final thoughts and wrap-up [12:43]
**Transcript:** pre-made crowds so you can start filling your scenes with tens of thousands of characters  instantly. Alright I'm Charlie thanks so much for watching and if you found any of this valuable  or entertaining please consider leaving a like and subscribing and let me know if there are  any other mocap tools you would like me to explore down in the comments. Okay I will see you in the

**Frame:** tutorials\frames\how-to-get-pro-motion-capture-for-metahumans-on-a-budget-in-unreal-engine-5\frame_024.jpg


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
