---
title: Intro to UnrealReader - Nuke 13.2
source: YouTube
url: https://www.youtube.com/watch?v=cZTO4ojzX2g
author: William Faucher
ingested: 2026-06-23
ue_version: "UE5"
tags: [nuke, compositing, unrealreader, render-passes, mrq, colorspace, camera-extraction, cryptomatte, pipeline, virtual-production]
extraction_status: complete
frames_dir: tutorials/frames/intro-to-unrealreader---nuke-132/
frame_count: 12
---

# Intro to UnrealReader - Nuke 13.2

**Source:** [YouTube](https://www.youtube.com/watch?v=cZTO4ojzX2g)
**Author:** William Faucher
**Duration:** 20m48s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Today we're talking about an exciting and underrated tool, and that is the Unreal Reader plugin  from the Foundry. With the 13.2 version of Nuke, the Unreal Reader comes built in,  and integration with Unreal Engine 5 is now supported, and it works like a charm.  Now, full disclosure, Foundry did provide me with a new license to make this video,  but I'm not being paid to promote this, they have no say in what I talk about in this video,  no money changed hands, this video does have a sponsor though, and that is CG Spectrum.  Now, what is Unreal Reader, and more importantly for those unaware, what the heck is Nuke? Nuke  is the industry standard for compositing, so as you're doing any kind of serious comp work in VFX,  chances are you're going to be using Nuke at some point. Under the hood, the Unreal Reader  node connects Nuke to Unreal's Movie Render Q using the Nuke server plugin over a TCP IP connection.  Unreal Reader makes it quick and easy for you to generate live renders from Movie Render Q,  change the render settings, control the results in Nuke by breaking down your renders into layers,  render passes, even tweaking shot framing by overriding the Unreal camera. Overall, it is amazing  to have this, and if you haven't been using this yet, you really should. Now, a few good things  to know about, as of Nuke 13.2, the following versions of Nuke are supported with the Unreal Reader.  We've got Nuke X, Nuke Studio, Nuke Indy, and Nuke Non-Commercial, which means that you can  test out the Unreal Reader for free. The standard regular version of Nuke doesn't support  Unreal Reader in terms of altering the existing render data, but it can pull through renders with  existing settings or loading existing Nuke scripts with the Unreal Reader node in them. Nuke  server is currently available on Windows for Unreal Engine 5, which a Mac OS version coming soon,  and for those of you interested in a Linux version, you can request a dev build through their  support, which I'll include a link to down below. I'm also going to include an FAQ just because  there's a few good bits of information that you might want to know about. So let's jump right  into how to get all of this set up right after a message from my sponsor. A big thank you to CG

**Frame:** tutorials\frames\intro-to-unrealreader---nuke-132\frame_000.jpg

### CG Spectrum [2:04]
**Transcript:** Spectrum for sponsoring this video. CG Spectrum is a global top-ranked training provider offering  specialized online courses in Real-Time 3D, game development, animation, VFX, and digital painting.  They're an Unreal Autoride Training Center and Unreal Academic Partner, and their courses include  personalized mentorship from industry professionals. I mentor CG Spectrum myself part-time and help  develop their Real-Time 3D, Technical Art, and Virtual Production course. Right here is an example  from one of my students. So if you want to learn Unreal Engine with an industry mentor guiding you,  check out the link below or visit CG Spectrum.com for more info. You'll get the most practical and  up-to-date knowledge, along with the skills, connection, and industry awareness that film and  video game studios are hiring for. Thanks again to CG Spectrum for sponsoring this video. And with

**Frame:** tutorials\frames\intro-to-unrealreader---nuke-132\frame_001.jpg

### Necessary Plugin - Nuke Server [2:52]
**Transcript:** that done, let's talk about how to get the Unreal Reader set up. Now before we do anything  in Unreal or Nuke, the first thing we need to do is download the Nuke server plugin that you can  find in the link below. You can't find this plugin on the Epic Marketplace because it is a custom  plugin built by Foundry. When you get to this page here, scroll down all the way to the bottom,  and you're going to see we've got Nuke 13.2 or 13.1 and download the plugin for the Unreal Engine  version that you're using. So in my case, I'll be using Unreal Engine 5 on Windows to go ahead and  download that. Once you've unzipped the file, you're going to find a Foundry folder in there.  And we need to copy that folder into the Plug-in folder of your Unreal Engine install. By default,  for most people, it's going to be found in C, Program Files, Epic Games. And in my case,  I'm going to go to the UE5.0 folder, go to Engine, Plug-ins, and you can copy paste the Foundry  folder directly into the Plug-ins folder right here. You'll see I already have the Foundry folder  copied there. Go ahead and do that. Once you've done this, go ahead and start Unreal and will now be  able to enable that plugin. So now with UE5 open, I'm going to go to the Settings button up top here,

**Frame:** tutorials\frames\intro-to-unrealreader---nuke-132\frame_002.jpg

### Nuke Server setup in Unreal Engine [4:05]
**Transcript:** go to Plug-ins, and in the Search Panel up top here, we're going to search for Nuke. And if you  copied the folder correctly into your Plug-ins folder, you should have the Nuke Server plugin show  up here. Make sure that's enabled. You'll have to restart the Engine and then we'll be ready to go.  I'm going to close this. And now there's one last thing we need to do before we can jump right into Nuke.  So with the Engine restarted, we can now click on the Window button up top here.  And now you should have a Nuke Server option show up right here. Click on this, and you'll get a  Nuke window popping up. The port number by default, I believe, is 9000. The number you use in Unreal  doesn't really matter. What is important is that the number you use in Nuke later matches this number.  So for now, just leave it a default, hit the Start Server button, and when the Server status  says running, we're now ready to jump into Nuke for the first time. So now I have Nuke X open,

**Frame:** tutorials\frames\intro-to-unrealreader---nuke-132\frame_003.jpg

### UnrealReader node in Nuke [5:07]
**Transcript:** but the plugin also works with Nuke Studio, Nuke Non-Commercial, and Nuke Indy as well. No problems.  So the first thing we need to do is we're going to click on the Viewer section down here,  press the Tab key, and search for Unreal Reader. Click on this, and you'll have a new node showing up  right here. And now you'll see up on the top right hand corner here, we've got port 9000,  which is usually the default. For me, in Unreal, it was set to 4,500, and I'm going to hit Connect  Server. And now, if you've done everything correctly, you should have the Unreal Engine version  right here, fetch later shows up. Unreal Reader and Nuke is now connected with Unreal Engine  directly. But maybe you don't see anything. The screen is still black. There's one thing we need to do.  If you're not familiar with how Nuke works. So we're going to select our Unreal Reader node right  here and press the One key. And basically, pressing the One key has connected our Unreal Reader node  to the Viewer. And you'll see we have a little One key here. If I have something like a Grade node,  for example, and I pressed the Two key, you'll see the Viewer is now showing the Grade node. Of course,  there's nothing there, so that's normal. But you get the idea. I toggle between One and Two. That's how  you can tell the viewer what to show. This is going to be important for later. So with the Unreal Reader  node loaded, you'll see here we have the Project Path where we can designate which project is being  loaded. We can choose the Map that we want to load and the Sequence as well. So, for example, if I  have another Sequence I want to load instead, I can click here and choose this one, for example.  And it's going to update automatically. So this is, for example, just another shot that I had where  the camera is panning and we have some motion blurred elements here. It's really cool and very  easy to switch between levels and sequences directly within the Unreal Reader. It's going to update  live in front of you. Next, we can choose the Scene Unit, the Render Mode. And the Render Mode is  basically if you want to designate whether or not you want to use Stencil layers. And if you don't  know how to use Stencil layers, I have a video about that right up here. So go check that out if  you need it. In Image Format, it's where we choose the Image Resolution of our shot. So in my case,  I want to render this as UHD4K. As you can see, it's going to update automatically for you. Next,  we have Overscan right here. If you need to work with Lens Distortions and stuff, Overscan is a  fantastic way to do that. We've got the Frame Range of our Sequence automatically being updated  right here. So you don't need to manually put that in. Next at the bottom here, we have the Right  section. And we're going to get into that a little bit later because Unreal Reader is not actually  writing anything to disk. Unreal Reader is streaming data directly from the Movie Render queue  under the hood. So at some point, after adjusting all of your render setting, you're going to want to  write this render to disk. Right? You're going to want to write those frames. But we're going to get  into that a little bit later. Feel free to use the chapters down below to skip to the appropriate  part of the video. Now, before we carry on here, let's address one of the glaring issues that we

**Frame:** tutorials\frames\intro-to-unrealreader---nuke-132\frame_004.jpg

### Addressing Possible Colorspace Issues [8:11]
**Transcript:** have here. And that is color. You'll see the colors here are kind of washed out and flat and  over saturated and looks frankly terrible. Taking a look at this screenshot from Unreal right here,  that's what we should be getting. But this is what we see in Nuke instead. And for those of you who  have watched my color grading tutorial in Divinci Resolve, again, you can watch that video right here if  you haven't already. You're going to know why Nuke is looking this way. And the reason for that  is color space. Nuke is expecting a linear image, but by default, Unreal does not spit out a linear  render. So the first thing we need to do is go to the Advanced tab of the Unreal Reader. And right  here in Color Output, we need to disable the tone curve. By disabling the tone curve, it's going  to send Nuke a linear image. So I'm going to click that here and you'll see things already look  a whole lot better. If I toggle this back and forth before and after, it is a whole lot better. But  the color is still off. And in this specific shot, I actually do like how overfacerated and the  tonality of the colors, I think this actually works very well for the shot. But it doesn't match what  we have in Unreal. And the reason for that is because Nuke thinks that this render is in Aces.  But if not, it's a linear SRGB image. So we just need to tell Nuke how to interpret that. And the  way to do that is we're going to select our Unreal Reader node here, press the Tab key, and we're  going to search for OCEIO Color Space. And we're going to double click on the OCEIO Color Space node,  go to Input, Color Spaces, Utility, Utility, Linear, SRGB. And now your render should match pretty much  what you have in Unreal. And that is how you address the glaring color space issues right here.  If this was a read node, we could just directly put in the input transforms of the read node. But  again, we're going to get into that a little bit later. So going back to our Unreal Reader node,  I'm going to go through all of the settings with you. And how do we go along? I'm going to show you  some of the render settings that I use for my own renders in 95% of cases. So let's do that right  now. And starting off with the render tab up top here, this here is quite possibly the best part  of the Unreal Reader node. And you'll see here we have all of our render passes in one nice clean list.  For those of you who are familiar with the movie render to you, you'll know that using render  passes is a little bit unintuitive and sometimes it's hard to find them or sometimes they don't show up  at all. So thank you to the team at the Foundry for coming up with this solution because now we have  all of our render passes here and a wonderful description of what all of those render passes do.  So in my case, I'm going to turn on crypto mat, world depth, world normal, and maybe world position as well.

**Frame:** tutorials\frames\intro-to-unrealreader---nuke-132\frame_005.jpg

### Picking Stencil Layers [11:20]
**Transcript:** All right, so future will here chiming in just because there is one really cool feature I forgot  to talk about in the initial recording. And that's showing off the preview layers feature. So  going back to my Unreal Reader tab here, I'm going to set the render mode to stencil layers  and bear with me here. With that done, going back to the render tab here, I'm going to click on  preview layers. And now this is going to preview our object IDs. And now by clicking the picker add  button right here, I can hold the control shift key and click to select individual objects  in my scene and create my own mask that way. If you hold control shift and drag, you're going to  select multiple objects like this and they all show up in the layer list right here, which is  absolutely awesome. I can click the picker remove button here, control shift drag to remove  object from my selection, like so. Also by going back and setting the render mode back to  full image, once you have your render passes set up here, you can visualize them by going to the  RGB button over here. And you'll see we got world depth, world normal world position. By clicking  on one of them, you should get your render passes showing up like so. If for whatever reason your  render passes don't show up here, you can click on the update channel list button right here or  in the Unreal Reader tab, click on fetch latest. Once you do that, you should have all of the render  passes you chose show up in the list here. And with that said, let's get back to the original

**Frame:** tutorials\frames\intro-to-unrealreader---nuke-132\frame_006.jpg

### Render Layers [12:55]
**Transcript:** recording. Now going to the advanced tab here, this is probably something you're going to be very  familiar with if you've been using the movie render to you. So we've got the deferred rendering tab.  In the crypto mat, we determine which object IDs we want to you want the material, the actors,  so on and so forth. The anti aliasing sample. Again, if you watch my movie render to you tutorial

**Frame:** tutorials\frames\intro-to-unrealreader---nuke-132\frame_007.jpg

### Advanced Tab - Movie Render Queue Settings [13:15]
**Transcript:** right here, you'll find I do a deep dive into which settings to use here. Now for my own sick,  I usually set this to 16 and with the anti aliasing methods set to none. 16 temporal sub samples will  give you a much cleaner motion blur, much better results, much better edges along your models.  And 16 is usually more than enough. Sometimes I need to bob it up to 32, but it's rare.  For those of you who are using lumen, you might want to increase the render warmup count and the  engine warmup count to something like 30 or 50, because as you're probably aware, lumen needs a few  frames to kind of settle down a little bit. So if you render the shot here and you notice that  there is no jihad or no global illumination, no indirect illumination, it's probably because you  don't have any render warmup frames. So increase both the render and engine warmup frames if you run into  any issues with lumen. Next, we got the shutter timing, color output, and the rest of the bottom  game overrides high resolution. I never really touched these. I just leave it a default.  If you want to disable motion blur entirely, we can click the disable motion blur button right here.

**Frame:** tutorials\frames\intro-to-unrealreader---nuke-132\frame_008.jpg

### Cameras [14:25]
**Transcript:** And next, let's go to the camera tab over here. And this is where things get really interesting.  So what I'm going to do now is I'm going to click the link output button here, click on create camera,  and you'll see we now have a new camera node selected right here. So if I select this and press the  one key, you'll see now we are kind of in a 3D world space type of thing. And if I zoom out,  you'll see we now have a camera here. And if I scrub through the timeline here,  like this, you'll see this camera is actually hooked up with the camera animation that I have in  Unreal in my sequence. So I animated the camera in Unreal and Unreal Leader is able to read that  camera data and bring it into Nuke in a 3D space. Now, I'm not an advanced compositor, but I can  tell you that having access to the actual camera that's being used in our renders is immensely powerful.  It's amazing for any kind of 3D projection or any kind of matte painting work. There are hundreds  of possibilities and reasons for using this. So it's absolutely awesome to have access to that data.  Again, a big thank you to the team at the Foundry for coming up with this. This is so cool. But  there's one more thing we can do with this and it's pretty awesome. So I'm going to select this here.  I'm going to delete that and I'm going to create my own camera.  And now we have a new camera one. I'm going to grab this like that, move it up here,  move it up in world space like this. And now I'm going to connect this to my Unreal Reader node.  I'm going to click on my Unreal Reader node or OCIO node, press the one key and you'll see the  camera that we just created in Nuke is overriding the camera that we have in Unreal, which means that  any compositor or anyone working in post production can create their own camera and render  straight from Unreal using that custom camera. So if a compositor need to make some small changes  to the camera or position or any of the depth of field settings, they can do that right here.  Probably a bit of a niche use case, but it's still very cool to know about because I'm sure  someone else there wants to use this. So I'm going to delete this and revert back to my default one.  So to be clear, when you delete the custom camera that you made, it's going to revert automatically  to the camera that is in your Unreal Engine sequence. Going back to the Unreal Reader node,  the last tab up here is the variables tab. And this is where we designate all of our console  variables by clicking the add button, entering your console variable, so r.screen percentage with  the value of 200. For example, if you want to remove it, click on this and delete it. It's pretty  straightforward, very self-explanatory. So the last thing we want to do is we want to be able to

**Frame:** tutorials\frames\intro-to-unrealreader---nuke-132\frame_009.jpg

### Writing Renders to Disk [17:23]
**Transcript:** write our files to disk, right? So I'm going to go through this with you just because I know it's  a little bit weird for those of you who are new to Nuke. So in order to write this render to disk,  we're going to click on the little folder icon right here at the bottom of the Unreal Reader node.  I'm going to choose this folder here, and you'll see we have the file path, but you still need to tell  Nuke what the name of your file is going to be because Nuke doesn't have a way to know that. So  I'm going to call this render example underscore a underscore. And next we need to add some hashtags.  I'm going to add forward them because the hashtags are what's going to designate the  frame number. Okay, this is not going to be added automatically. So this is very important,  otherwise your shots are not going to render. And lastly, we need to write dot EXR like this  because otherwise it's not going to write properly, even though we designated the file type here.  So having the hashtags and the dot EXR at the end is the most important part of this  right tool feature here. And we're going to click on right to disk right here. So when you click the  right to disk button here, you'll see we have a new read node show up here, but it says error.  Sometimes don't worry. The reason for that is because when you do that, Unreal has to actually  render your frame so it can take a while and depending on the complexity of your shot, the duration  of your shot and your render settings, it can take anywhere between a few seconds and several hours  to render. So a, just wait a little bit and b, just go ahead, double click your read node,  and click on the folder icon here and pick the correct render in the list. So right here,  it's render example a, just like that. And with the read node selected here, we're going to press the  one key and then we now have our render. I'm just going to select my Unreal Reader here and press the  D key to disable it because I don't want this running in the background right now. So now with our  read node selected, we can scrub through the timeline and see our camera animation. Just fine.  But of course, the colors are wrong. So you can either use the same OCIO color space,  trick W's earlier, or by double clicking on the read node, we can go to the input transform,  go to color spaces, utility, utility, linear, srgb. And now our render should match what we have in  Unreal. Just because we're telling Nuke in the input transform how to interpret this render.  And if I wanted to visualize my object IDs, press the tab button, search for crypto mat,  plug this into my read node here, press the one key in my crypto mat node, and you'll see we now  have all of our object IDs right there. Of course, this is going to depend on your Unreal  Reader node settings in the advanced tab by ID type. So depending on what she rendered, this is going  to change that. So guys, I know this was a lot of information to take in, but I hope you're  starting to see the power and how useful the Unreal Reader node is for both production. How are you  going to be using it? What are some features that you would like to see implemented in the Unreal  Reader? Let me know in the comments down below. So guys, I hope you found this video helpful. If you

**Frame:** tutorials\frames\intro-to-unrealreader---nuke-132\frame_010.jpg

### Outro & Thanks [20:36]
**Transcript:** did, do consider subscribing and giving it the old sums up. Thanks so much for watching. And as always,  happy rendering.

**Frame:** tutorials\frames\intro-to-unrealreader---nuke-132\frame_011.jpg


---

## Structured Notes

### Core Technique
Unreal Reader (Foundry/Nuke 13.2) connects Nuke directly to UE5's Movie Render Queue over TCP/IP. Streams live renders into Nuke without writing to disk first. Features: render pass selection (cryptomatte, world depth, world normal, world position) from Nuke's UI; stencil layer picker (control+shift+click objects in render); UE camera extraction → Nuke Camera node (follows UE animation); camera override from Nuke; console variable injection; write-to-disk via Write node (must manually add `####.exr` to filename). Color fix: Advanced tab → Disable Tone Curve → add OCIO ColorSpace node → Input: Utility/Linear/SRGB.

### Summary
20-minute intro by William Faucher to the Unreal Reader node in Nuke 13.2 (built-in, not a separate download). Setup: download "Nuke Server" plugin from Foundry → copy to Engine/Plugins → enable in UE5 → Window → Nuke Server → Start Server (default port 9000). In Nuke: Tab → search "Unreal Reader" → connect to UE port → shows live MRQ render. Color space issue: disable tone curve in Advanced tab → add OCIO ColorSpace (Utility/Linear/SRGB). Render passes (cryptomatte, world depth, world normal, world position) available in Render tab. Stencil layer picker lets you click objects in render to build per-object masks. Camera tab: creates Nuke Camera node linked to UE sequence animation; can override with custom Nuke camera. Write to disk: click folder icon → set path with `####.exr` suffix → "Write to Disk" → generates a Read node pointing to output. Lumen warmup: increase Render Warmup and Engine Warmup to 30-50 frames if GI is missing. Temporal subsamples: 16 recommended in Advanced tab.

### Key Steps
1. **Install Nuke Server plugin**:
   - Download from Foundry website (Nuke 13.2 page, bottom); choose UE version (UE5 Windows)
   - Unzip → copy "Foundry" folder → paste into `C:\Program Files\Epic Games\UE5.x\Engine\Plugins\`
2. **Enable plugin in UE**:
   - Settings → Plugins → search "Nuke" → enable "Nuke Server" → restart engine
3. **Start Nuke Server**:
   - Window → Nuke Server → port default 9000 → Start Server → wait for "Running" status
4. **Add Unreal Reader in Nuke**:
   - Viewer area → Tab → search "Unreal Reader" → click to place node
   - Set port to match UE Nuke Server port → click "Connect Server"
   - Select Unreal Reader node → press **1** key to connect to Viewer
5. **Configure project/sequence**:
   - Unreal Reader: Project Path → your .uproject; Map → level; Sequence → your Level Sequence
   - Image Format: select resolution (e.g., UHD 4K)
   - Frame Range auto-populated from sequence
6. **Fix color space** (critical):
   - Unreal Reader → Advanced tab → Color Output → enable "Disable Tone Curve"
   - Tab → OCIO ColorSpace node → Input Color Space: Utility → Utility → Linear → SRGB
   - Connect OCIO node between Unreal Reader and Viewer
7. **Select render passes** (Render tab):
   - Enable: Cryptomatte, World Depth, World Normal, World Position as needed
   - Preview passes via RGB button → select pass from dropdown
   - If passes don't appear: "Update Channel List" or "Fetch Latest" in Unreal Reader tab
8. **Stencil layer picker** (object masks):
   - Render Mode → Stencil Layers → Render tab → Preview Layers
   - Hold Ctrl+Shift → click object in viewer to add to layer; drag to select multiple
   - Ctrl+Shift → Picker Remove button to remove from selection
9. **Camera extraction**:
   - Camera tab → Link Output → Create Camera → new Nuke Camera node appears
   - Select Camera node → press 1 → see 3D space with animated camera matching UE sequence
   - Optionally create own Nuke camera → connect to Unreal Reader → overrides UE camera for render
10. **Console variables**:
    - Variables tab → Add button → enter CVar name (e.g., `r.ScreenPercentage`) → value (e.g., 200)
11. **Anti-aliasing (Advanced tab)**:
    - Anti-Aliasing: Override → None; Temporal Sample Count: 16 (or 32 for complex shots)
    - Lumen: Render Warmup Count + Engine Warmup Count → set to 30-50 if GI missing
12. **Write to disk**:
    - Click folder icon at bottom of Unreal Reader node → choose output directory
    - Set filename: `render_name_####.exr` (must manually add `####` and `.exr` — not auto-added)
    - Click "Write to Disk" → triggers MRQ render → generates Read node
    - If Read node shows error: wait (rendering takes time); then double-click Read node → pick rendered file
    - Color fix for Read node: Input Transform → Utility → Linear SRGB

### UE Systems / Blueprints / Settings
- **Nuke Server plugin** (Foundry) — TCP/IP server running in UE; port configurable; Window → Nuke Server → Start Server; Windows only for UE5 as of Nuke 13.2; Mac/Linux in development
- **Unreal Reader node (Nuke 13.2+)** — built into Nuke X, Nuke Studio, Nuke Indy, Nuke Non-Commercial; connects to UE via Nuke Server port; streams MRQ renders live; NOT available in standard Nuke
- **Port matching** — UE Nuke Server port must match Nuke Unreal Reader port; default 9000 in docs but tutorial's UE was 4500; set both to same value
- **Disable Tone Curve** — in Unreal Reader Advanced tab; sends linear image to Nuke instead of tonemapped; required for correct Nuke color management
- **OCIO ColorSpace node (Nuke)** — Input: Utility/Linear/SRGB; interprets UE's linear sRGB render correctly; prevents oversaturation artifacts
- **Render Passes in Unreal Reader** — Cryptomatte, World Depth, World Normal, World Position; selected in Render tab; more user-friendly than raw MRQ UI
- **Stencil Layers mode** — alternative to Cryptomatte; Ctrl+Shift+click objects in live preview → builds per-object mask; requires Render Mode: Stencil Layers
- **Camera node extraction** — Camera tab → Create Camera; Nuke Camera automatically follows UE Level Sequence camera animation; usable for 3D projections and matte painting; overridable with custom Nuke camera
- **Write to Disk** — Unreal Reader → folder icon → filename must include `####.exr` manually; triggers MRQ background render; outputs a Read node for the resulting EXR sequence
- **Temporal subsamples (Advanced tab)** — Anti-Aliasing: None + 16 temporal samples recommended; 32 for difficult shots; same as MRQ subsampling setting
- **Lumen warmup** — Render Warmup Count + Engine Warmup Count → increase to 30-50 frames if indirect illumination is missing from renders

### Difficulty
Intermediate. Setup is straightforward once you know the Nuke Server plugin must be manually downloaded from Foundry. Color space fix is mandatory and non-obvious. The Write to Disk filename format (`####.exr`) is a gotcha. Camera override and Stencil Layers are advanced features.

### UE Version
UE5.0 (Nuke 13.2 UnrealReader supports UE5; UE4 not supported; Windows only at time of tutorial)

### Tags
nuke, compositing, unrealreader, render-passes, mrq, colorspace, camera-extraction, cryptomatte, pipeline, virtual-production

---

## Related Entries
- `improve-your-renders-with-unreal-movie-render-queue-part-1---goodbye-sequencer-4.md` — MRQ setup that Unreal Reader uses under the hood
- `improve-your-vfx-with-lens-flares-anamorphic-tutorial.md` — Nuke compositing with UE renders (anamorphic lens flares)
- `why-you-should-be-using-stencil-render-layers---unreal-engine-426.md` — Stencil Layers explained in detail
- `how-to-render-cryptomatte-in-unreal-new-in-426.md` — Cryptomatte/Object ID rendering in MRQ
