---
title: MetaHuman Realtime Animator Best Practices | Unreal Engine Animation Hub
source: YouTube
url: https://www.youtube.com/watch?v=PgzSGQnWVcU
author: Unreal Engine
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/metahuman-realtime-animator-best-practices-unreal-engine-animation-hub/
frame_count: 4
---

# MetaHuman Realtime Animator Best Practices | Unreal Engine Animation Hub

**Source:** [YouTube](https://www.youtube.com/watch?v=PgzSGQnWVcU)
**Author:** Unreal Engine
**Duration:** 9m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Welcome to Animation Hub. Today we're going to be looking at best practices for using a webcam for metahuman animator. So before we can use the metahuman animator face it's important to make sure the plug-ins are enabled so I'll go to plug-ins here. So I don't know exactly which ones of these you need, imagine you need most of them but certainly for the live link aspect of this you'll need the metahuman live link plug-in enabled. So in my case I'm using a Logitech Brieo which is a nice little accessible web camera. And to get that set up on this metahuman which by the way is a very standard preset metahuman nothing special here and then I'm just going to go to add source in my live link window and then choose metahuman video. As you can see I've got my Brieo there and also you'll notice it's capable of doing the 12 AE by 720 90 FPS. There's a lot of options here but there's 90 FPS one we found is ideal. The extra frame rate that you get over resolution because as you can see I could do 60 at 1080p here but this 90 at 720p is considerably better for visual fidelity and fine kind of facial movements. Now if your frame rate is at 30 FPS you'll probably find that's capturing the face at 60 is absolutely fine but if your target frame rate is 60 then 90 really does benefit you. So I'm able to get this 90 option here because I've got the Logitech webcam plugged into a fast enough USB port so just bear that in mind you need to plug it into a USB 3 port that's got a correct amount of bandwidth and once we've done that you can hit connect and as you'll see if I don't go and select this it's gone green and that's because it can see me and I can go to input video and you can see here I am but you'll notice straight away that actually we're only achieving 36 frames a second out of that 90 which is not ideal and that could be for a number of reasons but one of the clues as to why that is is right here or we can see dropping is yes and what that means is that whether video frames are being dropped because they cannot be processed fast enough which tells us that the webcam is sending us 90 frames per second but we're just not able to process them all and that's because essentially what we're doing is using the same GPU to render this metahuman as we are trying to solve the face. Now I'm going to get into later what you can do to get around this if you want the best quality metahuman being solved in real time but for now let's just look at what we can do to the metahuman in the view port to just use that view port as a preview to the kind of facial quality we can achieve and get 90 frames per second in live link here. So one very quick way I can do that is actually just to turn the hair off so let's try that and we're no longer dropping frames and now we're achieving 90 so there you go that was a really nice quick fix but whatever you need to do to your environment to just give yourself a nice lightweight render to get 90 frames per second here is what you should do. The other thing that could be impacting this frame right here is actually the Logitech camera settings itself so you do need Logitech drivers installed they're called Logitech, called Logitechune. If I just go and get the Logitechune app up I've got mine set up already but yours will probably be something along these lines. So one thing that can impact your frame right here is the auto exposure and because the exposure is controlling the timing of the camera so first of all let's just turn HDR off we don't need that I'm going to leave all the focus on because it's not causing me any harm but if that is jumping around you might want to disable it and let's disable auto exposure and I'm going to show you why this has been a problem. So if I was to raise my exposure up you will see we've got a nice exposed image here but we're now only getting 33 frames per second and that's because at minus 5 the camera is only the camera sensor is staying open long enough to achieve this exposure it can't then capture at 90 frames per second. So in my case on this camera minus 6 is what I required to be able to get up into the higher frame rates and as you can see that's now up in the 80s. Minus 7 also achieves it but it's not the not kind of the best picture really so that works quite well. And there's also this gain here of obviously you can you can control the gain to get a good exposure but really want that gain as low as possible because a noisy image is going to give you a noisy saw of on the MetaHuman. Speaking of which let's get this MetaHuman animating so I'm going to click on the MetaHuman and then go to the Live Link subject and choose the Brio and click use Live Link source and there we go. So as you can see we're now doing a real time solve and this is a real time solve at 90 so it's a really lovely high fidelity facial solve that's catching tiny little movements in my face and giving me a really good lip sync. If we take a look at the noise here for a second I think that's worth discussing so if I was to just open my jaw and hold it open you'll be able to see my lower teeth in the MetaHuman and that's a really good way to assess the quality of the solve so if I just hold my jaw open you can see that's the kind of quality we're getting and then I'm going to turn my lights off and do it and you'll see the difference. If you can see that's a considerably noisy face then as soon as I turn the lights on we get a much smoother face so light is very important too you want to make sure there's enough light and you can have your logitune gain settings as low as possible and an exposure setting that's allows you to achieve the higher frame rates. Now we mentioned earlier about what happens if I want a really high quality MetaHuman at the same time well that's where we can leverage another PC running live link hub because what we'll do is we'll solve the face on that machine and then over live link we'll send the live link data and solve this MetaHuman in full screen on this machine so let me show you how to set that up. So here we are on my laptop and so we're going to want to run live link hub. If you've got the live link hub plug in enabled you can just go down to tools and launch live link hub or if you want to just run it locally then it is available in your engine win64 directory and it's just this application here so let's just run it. So here we are in live link hub and the workflow is very similar actually so we'll just go to add source and choose MetaHuman video and log check Bray is there and I just hit connect. There we go and that's basically the same workflow. So this is now ready to send data over to into Unreal but as you can see there's no clients this would be where you would connect to another machine on the network and the reason it's not connected is that at the moment I've got I've live link hub is not adding any clients automatically so I can drop it down and I can just go to all and there you go we can see our machine and we're sending that live link data. It's really important that live link hub and your instance of Unreal on the other machine is on the same network and a common issue especially if you're using VPN is the UDP port could be different and so if we go to settings and go to UDP messaging just make sure the unicast endpoint is selecting the network that you wish to communicate on and the same is true in Unreal. In project settings just go to UDP messaging and check the unicast endpoint there is correct. So now we can head back over to our main workstation. So here we are back in Unreal. Live link hub is running on my laptop now with the Logitech Bray plugin instead so we've completely removed that solve happening on this GPU and you can see in the live link window that live link hub is sending through the Logitech Bray O subject because the name hasn't changed it's mapping to this metahuman straight away. So that's turned things back on the metahuman that's turned their hair back on and let's look at it full screen. So there we go. So we have a 90 frames per second capture of metahuman which is getting all of my lip fidelity nicely and all the subtle kind of not so subtle facial expressions. This is basically the ideal setup if you're doing a live metahuman capture. So as you can see it's looking great. So thank you very much. I hope this is really useful.

**Frame:** tutorials\frames\metahuman-realtime-animator-best-practices-unreal-engine-animation-hub\frame_000.jpg


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
