---
title: Intro to UnrealReader - Nuke 13.2
source: YouTube
url: https://www.youtube.com/watch?v=cZTO4ojzX2g
author: William Faucher
ingested: 2026-06-12
ue_version: "UE 5.0"
tags: [rendering, compositing, nuke, unreal-reader, mrq, stencil-layers, render-passes, camera-data, pipeline, advanced, william-faucher, ue5]
extraction_status: complete
frames_dir: tutorials/frames/intro-to-unrealreader---nuke-132/
frame_count: 0
---

# Intro to UnrealReader - Nuke 13.2

**Source:** [YouTube](https://www.youtube.com/watch?v=cZTO4ojzX2g)
**Author:** William Faucher
**Duration:** 20m48s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Today we're talking about an exciting and underrated tool, and that is the Unreal Reader plugin  from the Foundry. With the 13.2 version of Nuke, the Unreal Reader comes built in,  and integration with Unreal Engine 5 is now supported, and it works like a charm.  Now, full disclosure, Foundry did provide me with a new license to make this video,  but I'm not being paid to promote this, they have no say in what I talk about in this video,  no money changed hands, this video does have a sponsor though, and that is CG Spectrum.  Now, what is Unreal Reader, and more importantly for those unaware, what the heck is Nuke? Nuke  is the industry standard for compositing, so as you're doing any kind of serious comp work in VFX,  chances are you're going to be using Nuke at some point. Under the hood, the Unreal Reader  node connects Nuke to Unreal's Movie Render Q using the Nuke server plugin over a TCP IP connection.  Unreal Reader makes it quick and easy for you to generate live renders from Movie Render Q,  change the render settings, control the results in Nuke by breaking down your renders into layers,  render passes, even tweaking shot framing by overriding the Unreal camera. Overall, ...


### CG Spectrum [2:04]
**Transcript:** Spectrum for sponsoring this video. CG Spectrum is a global top-ranked training provider offering  specialized online courses in Real-Time 3D, game development, animation, VFX, and digital painting.  They're an Unreal Autoride Training Center and Unreal Academic Partner, and their courses include  personalized mentorship from industry professionals. I mentor CG Spectrum myself part-time and help  develop their Real-Time 3D, Technical Art, and Virtual Production course. Right here is an example  from one of my students. So if you want to learn Unreal Engine with an industry mentor guiding you,  check out the link below or visit CG Spectrum.com for more info. You'll get the most practical and  up-to-date knowledge, along with the skills, connection, and industry awareness that film and  video game studios are hiring for. Thanks again to CG Spectrum for sponsoring this video. And with


### Necessary Plugin - Nuke Server [2:52]
**Transcript:** that done, let's talk about how to get the Unreal Reader set up. Now before we do anything  in Unreal or Nuke, the first thing we need to do is download the Nuke server plugin that you can  find in the link below. You can't find this plugin on the Epic Marketplace because it is a custom  plugin built by Foundry. When you get to this page here, scroll down all the way to the bottom,  and you're going to see we've got Nuke 13.2 or 13.1 and download the plugin for the Unreal Engine  version that you're using. So in my case, I'll be using Unreal Engine 5 on Windows to go ahead and  download that. Once you've unzipped the file, you're going to find a Foundry folder in there.  And we need to copy that folder into the Plug-in folder of your Unreal Engine install. By default,  for most people, it's going to be found in C, Program Files, Epic Games. And in my case,  I'm going to go to the UE5.0 folder, go to Engine, Plug-ins, and you can copy paste the Foundry  folder directly into the Plug-ins folder right here. You'll see I already have the Foundry folder  copied there. Go ahead and do that. Once you've done this, go ahead and start Unreal and will now be  able to enable that plugin. So n...


### Nuke Server setup in Unreal Engine [4:05]
**Transcript:** go to Plug-ins, and in the Search Panel up top here, we're going to search for Nuke. And if you  copied the folder correctly into your Plug-ins folder, you should have the Nuke Server plugin show  up here. Make sure that's enabled. You'll have to restart the Engine and then we'll be ready to go.  I'm going to close this. And now there's one last thing we need to do before we can jump right into Nuke.  So with the Engine restarted, we can now click on the Window button up top here.  And now you should have a Nuke Server option show up right here. Click on this, and you'll get a  Nuke window popping up. The port number by default, I believe, is 9000. The number you use in Unreal  doesn't really matter. What is important is that the number you use in Nuke later matches this number.  So for now, just leave it a default, hit the Start Server button, and when the Server status  says running, we're now ready to jump into Nuke for the first time. So now I have Nuke X open,


### UnrealReader node in Nuke [5:07]
**Transcript:** but the plugin also works with Nuke Studio, Nuke Non-Commercial, and Nuke Indy as well. No problems.  So the first thing we need to do is we're going to click on the Viewer section down here,  press the Tab key, and search for Unreal Reader. Click on this, and you'll have a new node showing up  right here. And now you'll see up on the top right hand corner here, we've got port 9000,  which is usually the default. For me, in Unreal, it was set to 4,500, and I'm going to hit Connect  Server. And now, if you've done everything correctly, you should have the Unreal Engine version  right here, fetch later shows up. Unreal Reader and Nuke is now connected with Unreal Engine  directly. But maybe you don't see anything. The screen is still black. There's one thing we need to do.  If you're not familiar with how Nuke works. So we're going to select our Unreal Reader node right  here and press the One key. And basically, pressing the One key has connected our Unreal Reader node  to the Viewer. And you'll see we have a little One key here. If I have something like a Grade node,  for example, and I pressed the Two key, you'll see the Viewer is now showing the Grade node. Of course,  there's no...


### Addressing Possible Colorspace Issues [8:11]
**Transcript:** have here. And that is color. You'll see the colors here are kind of washed out and flat and  over saturated and looks frankly terrible. Taking a look at this screenshot from Unreal right here,  that's what we should be getting. But this is what we see in Nuke instead. And for those of you who  have watched my color grading tutorial in Divinci Resolve, again, you can watch that video right here if  you haven't already. You're going to know why Nuke is looking this way. And the reason for that  is color space. Nuke is expecting a linear image, but by default, Unreal does not spit out a linear  render. So the first thing we need to do is go to the Advanced tab of the Unreal Reader. And right  here in Color Output, we need to disable the tone curve. By disabling the tone curve, it's going  to send Nuke a linear image. So I'm going to click that here and you'll see things already look  a whole lot better. If I toggle this back and forth before and after, it is a whole lot better. But  the color is still off. And in this specific shot, I actually do like how overfacerated and the  tonality of the colors, I think this actually works very well for the shot. But it doesn't match what  we h...


### Picking Stencil Layers [11:20]
**Transcript:** All right, so future will here chiming in just because there is one really cool feature I forgot  to talk about in the initial recording. And that's showing off the preview layers feature. So  going back to my Unreal Reader tab here, I'm going to set the render mode to stencil layers  and bear with me here. With that done, going back to the render tab here, I'm going to click on  preview layers. And now this is going to preview our object IDs. And now by clicking the picker add  button right here, I can hold the control shift key and click to select individual objects  in my scene and create my own mask that way. If you hold control shift and drag, you're going to  select multiple objects like this and they all show up in the layer list right here, which is  absolutely awesome. I can click the picker remove button here, control shift drag to remove  object from my selection, like so. Also by going back and setting the render mode back to  full image, once you have your render passes set up here, you can visualize them by going to the  RGB button over here. And you'll see we got world depth, world normal world position. By clicking  on one of them, you should get your render passes ...


### Render Layers [12:55]
**Transcript:** recording. Now going to the advanced tab here, this is probably something you're going to be very  familiar with if you've been using the movie render to you. So we've got the deferred rendering tab.  In the crypto mat, we determine which object IDs we want to you want the material, the actors,  so on and so forth. The anti aliasing sample. Again, if you watch my movie render to you tutorial


### Advanced Tab - Movie Render Queue Settings [13:15]
**Transcript:** right here, you'll find I do a deep dive into which settings to use here. Now for my own sick,  I usually set this to 16 and with the anti aliasing methods set to none. 16 temporal sub samples will  give you a much cleaner motion blur, much better results, much better edges along your models.  And 16 is usually more than enough. Sometimes I need to bob it up to 32, but it's rare.  For those of you who are using lumen, you might want to increase the render warmup count and the  engine warmup count to something like 30 or 50, because as you're probably aware, lumen needs a few  frames to kind of settle down a little bit. So if you render the shot here and you notice that  there is no jihad or no global illumination, no indirect illumination, it's probably because you  don't have any render warmup frames. So increase both the render and engine warmup frames if you run into  any issues with lumen. Next, we got the shutter timing, color output, and the rest of the bottom  game overrides high resolution. I never really touched these. I just leave it a default.  If you want to disable motion blur entirely, we can click the disable motion blur button right here.


### Cameras [14:25]
**Transcript:** And next, let's go to the camera tab over here. And this is where things get really interesting.  So what I'm going to do now is I'm going to click the link output button here, click on create camera,  and you'll see we now have a new camera node selected right here. So if I select this and press the  one key, you'll see now we are kind of in a 3D world space type of thing. And if I zoom out,  you'll see we now have a camera here. And if I scrub through the timeline here,  like this, you'll see this camera is actually hooked up with the camera animation that I have in  Unreal in my sequence. So I animated the camera in Unreal and Unreal Leader is able to read that  camera data and bring it into Nuke in a 3D space. Now, I'm not an advanced compositor, but I can  tell you that having access to the actual camera that's being used in our renders is immensely powerful.  It's amazing for any kind of 3D projection or any kind of matte painting work. There are hundreds  of possibilities and reasons for using this. So it's absolutely awesome to have access to that data.  Again, a big thank you to the team at the Foundry for coming up with this. This is so cool. But  there's one more thing w...


### Writing Renders to Disk [17:23]
**Transcript:** write our files to disk, right? So I'm going to go through this with you just because I know it's  a little bit weird for those of you who are new to Nuke. So in order to write this render to disk,  we're going to click on the little folder icon right here at the bottom of the Unreal Reader node.  I'm going to choose this folder here, and you'll see we have the file path, but you still need to tell  Nuke what the name of your file is going to be because Nuke doesn't have a way to know that. So  I'm going to call this render example underscore a underscore. And next we need to add some hashtags.  I'm going to add forward them because the hashtags are what's going to designate the  frame number. Okay, this is not going to be added automatically. So this is very important,  otherwise your shots are not going to render. And lastly, we need to write dot EXR like this  because otherwise it's not going to write properly, even though we designated the file type here.  So having the hashtags and the dot EXR at the end is the most important part of this  right tool feature here. And we're going to click on right to disk right here. So when you click the  right to disk button here, you'll see...


### Outro & Thanks [20:36]
**Transcript:** did, do consider subscribing and giving it the old sums up. Thanks so much for watching. And as always,  happy rendering.



---

## Structured Notes

### Core Technique
Unreal Reader plugin for Nuke 13.2 — live TCP/IP bridge from Nuke directly to Unreal's Movie Render Queue. Allows triggering renders from Nuke, receiving render passes (stencil layers, world normal, depth), controlling settings, and even pulling camera data into Nuke's 3D scene for projection work.

### Summary
20-minute introduction to Foundry's UnrealReader plugin (built into Nuke 13.2). The plugin connects Nuke to Unreal over TCP/IP — you set up a Nuke Server in UE, then the UnrealReader node in Nuke connects and can control MRQ renders live. Key features: live render preview in Nuke viewer, all MRQ settings accessible (AA, stencil layers, color output, warmup frames), Cryptomatte/object ID picker, render pass visualization, and live camera data export into Nuke's 3D space. The camera tracking feature alone makes it powerful for matte painting and projection work.

### Key Steps

**Installation:**
1. Download Nuke Server plugin from Foundry (NOT on Epic Marketplace — custom plugin)
2. Select the download for your Nuke version (13.2) and UE version
3. Extract → find the `Foundry` folder
4. Copy `Foundry` folder into: `C:\Program Files\Epic Games\UE_5.0\Engine\Plugins\`
5. Launch Unreal → Settings → Plugins → search "Nuke" → enable **Nuke Server**
6. Restart engine

**Starting the Server in Unreal:**
1. Window → Nuke Server
2. Port number: default `9000` (note this number for Nuke)
3. Click **Start Server**
4. Status shows "Running" → ready

**Connecting in Nuke:**
1. In Node Graph → press Tab → search "UnrealReader" → create node
2. Set port to match Unreal server (9000 by default)
3. Click **Connect Server**
4. Unreal Engine version shows in the node panel → connected

**Display in Nuke Viewer:**
- Select UnrealReader node → press **1 key** to connect to Viewer
- If nothing shows: check the 1 key, check port match, check server is running

**Fix Washed-Out Colors:**
1. Select UnrealReader node → Advanced tab
2. **Disable Tone Curve** ✓ → Nuke receives linear image
3. Apply OCIO colorspace conversion in Nuke if needed for correct display

**Stencil Layers / Object ID Picker:**
1. UnrealReader → Render Mode → **Stencil Layers**
2. Click **Preview Layers** → objects highlighted in viewport
3. Ctrl+Shift+click → select individual objects as layers
4. Ctrl+Shift+drag → multi-select
5. Layers appear in layer list for export as separate passes

**Render Passes Visualization:**
- Set Render Mode → Full Image
- Click **RGB** button → dropdown shows: World Depth, World Normal, World Position
- Click any pass to preview it in the Nuke Viewer

**Live Camera Export:**
1. UnrealReader → Camera tab
2. Click **Link Output** → Create Camera
3. Select camera node → press **1** key
4. Camera animates in sync with Unreal sequence camera
5. Enables: 3D projection, matte painting, camera-matched geometry

**Render Warmup for Lumen:**
```
Advanced tab:
  Engine Warm Up Frame Count: 30–50
  Render Warm Up Frame Count: 30–50
// Lumen needs time to settle — without this, first frames have no GI
```

**Writing Renders to Disk from Nuke:**
1. UnrealReader → click folder icon
2. Set output path
3. File name: `render_name_####.exr` — hashtags REQUIRED for frame numbers, `.exr` REQUIRED at end
4. Click **Write to Disk**

### UE Systems / Blueprints / Settings

**Nuke Server in Unreal:**
```
Window → Nuke Server:
  Port: 9000 (default)
  Start Server → Status: Running

Plugins required: Nuke Server (from Foundry Engine/Plugins folder)
```

**UnrealReader MRQ Settings (accessible from Nuke):**
```
Advanced tab → Anti-Aliasing:
  Override AA: True
  AA Method: None
  Temporal Sub Samples: 16
  Engine Warm Up: 30 (for Lumen)

Advanced tab → Color Output:
  Disable Tone Curve: True   // REQUIRED for linear image in Nuke

Camera tab:
  Link Output → Create Camera   // exports UE camera to Nuke 3D
```

### Difficulty
Advanced — requires Nuke license, Foundry plugin, and understanding of compositing pipeline

### UE Version
UE 5.0 (Unreal Reader supports UE5 from Nuke 13.2+)

### Tags
rendering, compositing, nuke, unreal-reader, mrq, stencil-layers, render-passes, camera-data, pipeline, advanced, william-faucher, ue5

---

## Related Entries
- `tutorials/why-you-should-be-using-stencil-render-layers---unreal-engine-426.md` — Stencil layers in MRQ
- `tutorials/how-to-render-passes-with-the-movie-render-queue-unreal-engine-426.md` — Render passes in MRQ
- `tutorials/unreal-to-davinci-resolve-workflow---aces-srgb.md` — Alternative: Resolve-based pipeline
