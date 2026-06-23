---
title: How to Create the ULTIMATE Previz with Polycam, Metahumans, and Move.AI in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=ova-8EAD8eg
author: Charlie Driscoll - Unreal Engine Filmmaking
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-create-the-ultimate-previz-with-polycam-metahumans-and-moveai-in-unreal-e/
frame_count: 4
---

# How to Create the ULTIMATE Previz with Polycam, Metahumans, and Move.AI in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=ova-8EAD8eg)
**Author:** Charlie Driscoll - Unreal Engine Filmmaking
**Duration:** 9m33s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** What if I told you the future of filmmaking isn't just about what happens on set, but what happens inside a video game engine first? Recently, my production company took on a challenging project, a short film about Alzheimer's disease that required complex camera movements, intricate dance sequences, and seamless transitions between memories. But instead of creating a traditional shot list or storyboard, I tried something different. I decided to shoot the entire film before I shot the actual film. Using Unreal Engine, Performance Capture, and a LiDAR scan of our location, I created a complete digital version of our story. Crazy? Maybe. Overkill? I thought so too. But what happened next completely changed how I think about filmmaking? In the next few minutes, I'm going to show you exactly how I turned a real house into a digital set, acted out all the roles myself, and used a video game engine to plan every single shot of our film. More importantly, I'll show you whether this elaborate process actually made our final film better. And the answer might surprise you. Now I'd used Unreal Engine to create more basic pre-visits for a few projects before. Early last year, we shot a different short film for the same client, which took place in an ambulance. I found an ambulance on the Unreal Engine marketplace that almost exactly matched the ambulance we would be filming in. And I was able to figure out the lighting, camera angles, and timing of the edit very precisely. That preparation allowed us to get nearly 50 shots in a single 10-hour day. Now for this project, I decided to scan the house we would be filming in using an app called Polycam, which makes it super easy to scan a location using an iPhone or iPad. You just start recording and point, slowly moving around the space you want to scan. The blue shows where you need to record more information, and you can see the geometry taking shape as you move. I scanned the whole first floor of the house, knowing I could pick out areas for filming later. I didn't worry about anything like mirrors or windows or foliage, and just focused on scanning as much of the nooks and crannies and details as possible. This whole process took roughly 25 minutes, but the part I found particularly shocking, shocking, I tell you, is how fast the scan was ready. It took maybe 15 minutes or less to upload and process the scan, and I was able to preview it on my device before even leaving. On my computer, I selected the remesh option, crank the geometry slider all the way up, change the textures to 8K, and hit remesh, and it turned out pretty good. From there, I just exported the FBX and imported that into Unreal. I dropped it into a scene where it looks tiny, but I just scaled it up by 100x, and it seemed to be accurate. Here I'm just turning off any light sources in the map, but you can actually just go up here and change your viewport from lit to unlit, and you can see the scan with all it's baked in lighting, and you can just fly around and check it out. It's quite lumpy and looks AI-generated in a weird way, but for our purposes, it's perfect. But since this is unlit, we need to add some actual lighting, because if we dropped any object or character in here, it would look completely unlit and very weird. So I just turned the lighting back on and started adding rectangular lights to all the windows in order to mimic the natural lighting. This was just a workaround. This wasn't meant to be completely realistic, just to give me an idea of the natural lighting. And this is what I ended up with. I then started blocking out the scenes with some metacumins. Also here you can see I turned on Path Tracing, and the lighting looks much more realistic. I would have preferred the previous to look this way, but no way did I have enough time for Path Tracing. You can cut out holes in the geometry where the windows would be to simulate sunlight. You can do this either in Blender or in Unreal using the Boolean modeling tool in the modeling tab. And then you just combine that with a cube fitted to the window where you want the whole. You can then use a directional light as the sun and move it around as needed. Unreal Engine also has a way to simulate the exact sun position based on the locations GPS coordinates and time of day, which was what they did in Dune for pre-production. But this seemed like too much work for this project to get everything set up and looking in a way that would actually be accurate to what I would be seeing on set. So I actually got into the performance capture pretty quickly after getting the environment set up. Since I wanted actual animated metacumins to help block the shots out more accurately. I used my usual setup of Move AI with 6-Go Pro Tens for the body capture and metacumin animator with an iPhone 13 and Rococo Headrig for the face capture. To save time, I would do multiple performances in the same take. So I would act out the husband's part, then without cutting, just act out the wife's part, knowing I could split them in Unreal Engine in the sequencer. This really saves a lot of time when it comes to processing the animations, both for the face and the body. I did a small amount of animation cleanup, mostly just baking the animations to control rigs so I can adjust the eye lines or smooth out any really bad jitter. I didn't even bother cleaning up the hands. Honestly, this made the whole process way more fun since I didn't get to bog down in tedious cleanup. And we were able to try some really interesting things like capturing two people dancing. So here's my wife and me putting our wedding dance classes to good use. And you can see the capture did pretty well. Not perfect, but good enough. You're not creating some pretty uncanny valley animations, but they actually served their purpose in helping me envision the cut. So here I'll sort of throw everything together to just show how seamlessly the pre-vis can flow into the final shot. I can do all the playing and experimenting with the camera movement and framing and transitions in Unreal. This allows me to make quick and easy decisions on set when it comes to lighting and communicating to the crew. And I was also using a smaller camera, which helped a ton with moving quickly. But here you can see how closely I was able to match the pre-vis shot. And again, Unreal makes it easy to fly around and find your next shot. So when you're on set, you know exactly where to go, what to do, and how the shot should look. Overall, I was able to match everything really well. Having the pre-vis on my phone allowed me to cross-reference the actual camera movement, which made it possible to grab a large amount of fairly complex shots. Now in these side-by-side examples, I changed the cuts a little so they would match perfectly. The actual cut won't match it frame for frame like this, but I did this to illustrate how good of a tool Unreal Engine is for visualizing stuff like this. Especially when you go the extra mile and use full performance capture. Having such a clear vision of the final film also helps the entire cast and crew perform more efficiently and confidently. And allows you to focus on executing the shots efficiently and ultimately pull off more ambitious ideas. Now, the final film is not done yet, but I think I can still answer the question from the beginning, which does this process actually make the final film better. Well, emphatically yes. Obviously the concept in script were amazing, the actors gave amazing performances, and the crew executed really well. But from a cinematography and editing standpoint, I think it's undeniable how useful this technique of actually adding in placeholder performances to your pre-vis and getting creative with the camera movement in Unreal Engine is. Now the whole pre-vis process was spread out over five days, which included me going to the house and scanning it, and I was there for about 45 minutes total. Doing all the animations only took me about an hour or two, since there wasn't too much dialogue. However, uploading and processing all that motion capture footage and face animations took maybe five or six hours total for about ten body and face animations. Then I spent probably a good 16 hours doing the actual pre-vis over the course of two days. I won't go into too much detail on the process of setting up metahumans with motion capture animations and face animations, but if you want to know more about that, I'll just have an in-depth tutorial on this channel right here where I show the complete process of performance capture from capturing the animation to polishing the animation, to building the environment, etc. and all using tools that are very cheap or completely free. So let me know in the comments if this is a technique you might try or if you think this level of preparation is unnecessary. Do you use Unreal Engine for pre-vis? Or if so, how? And let me know what you thought of this video. Do you like seeing Unreal Engine applied to live action filmmaking? Anyway, thanks for watching. My name's Charlie, and if you found anything in here valuable or entertaining, please consider leaving a like or subscribing. Or both.

**Frame:** tutorials\frames\how-to-create-the-ultimate-previz-with-polycam-metahumans-and-moveai-in-unreal-e\frame_000.jpg


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
