---
title: Performance Profiling with Unreal Insights (Basics) | Unreal Engine 4 & Unreal Engine 5 Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=etkLE6BEKoM
author: Shawnthebro
ingested: 2026-07-20
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/performance-profiling-with-unreal-insights-basics-unreal-engine-4-unreal-engine-/
frame_count: 0
frame_status: pending-selection
---

# Performance Profiling with Unreal Insights (Basics) | Unreal Engine 4 & Unreal Engine 5 Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=etkLE6BEKoM)
**Author:** Shawnthebro
**Duration:** 14m23s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py performance-profiling-with-unreal-insights-basics-unreal-engine-4-unreal-engine- <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] What's up guys, Sean the Bro here, and in today's episode we are going to be going over
[0:17] tracing or performance profiling, and so this is going to be a method of determining how well
[0:22] your game is running, what's taking up the most of your CPU, your GPU, memory, all that stuff,
[0:29] so we're going to be able to see if there are things we should tone down to make the game perform
[0:33] better, or if there are things that we have more leniency with so we can increase what we do with
[0:40] our budget there, so if we want to add more visual effects, we want to add more states to our AI
[0:45] behavior, we may be able to do that. Now this is my fighting game, so I'm using this as the example,
[0:53] but this will work with any Unreal project, and it also works in Unreal Engine 4 as well, but the
[0:58] method is a little bit different because in Unreal Engine 4 it was the session front end, and then
[1:02] eventually it became Unreal Insights, we're going to be covering Unreal Insights today specifically
[1:06] in UE5, if there is interest in the session front end in UE4, I will gladly put out content on that,
[1:12] but this will work with any Unreal project, so before we do that if you want to check out how we
[1:17] did the fighting game, what you were just seeing on the screen there following along with that
[1:21] series, I'll link you to the playlist right here in the top right corner just so you can get caught
[1:25] up, again it's not relevant for today's episode, but if you're interested then feel free to check
[1:29] that out, believe there are 250 episodes to date, alternatively if you're not interested in that,
[1:35] I do recommend you watch these episodes as well, these episodes are my debugging episodes, they
[1:40] are also generic episodes that show you how to debug any Unreal Engine project, debugging is one of
[1:45] your best tools as a programmer, and I recommend you learn it if you're not comfortable or familiar
[1:49] with it in Unreal Engine, but with those things aside we can go ahead and get started, so I'm in
[1:54] Unreal Engine and this specifically is 5.3.2, any version of Unreal Engine 5 is going to be pretty
[1:59] similar to this, so down toward the bottom of your window here you have this button with the
[2:06] little drop down arrow that says trace, you can select that and open up this little pop-up here,
[2:11] a lot of this is preferences and settings for your traces as well as where to store them,
[2:16] then you can also start a trace from here, I keep everything default for today's episode,
[2:21] but just be aware that you have these options available to you, we will go into some of them
[2:24] in more depth, but the one we actually care about for right now is this Unreal Insights button,
[2:29] the session browser, if we click that button it opens up this window, this is the Unreal Insights
[2:35] session browser, I don't have any traces in here, but as you do performance analysis you will get
[2:41] some in this section, so the first thing we want to do at this point is actually trace something,
[2:45] you can either do it through the menu I was showing you earlier with all the other settings,
[2:49] or you can just press this button right here which is start tracing, so if you press that button
[2:54] you'll get a little notification that the trace is started and it does start right here while you're
[2:58] in the editor, to actually perform performance analysis and profiling on our game we want to load
[3:03] up the game and let's say you load into a level, so we'll load two characters, we'll load the default
[3:10] level, I'll let the intros play that way we can analyze that as well,
[3:30] we are now in our game and it is being traced at the current moment, so now we can come over here
[3:35] and do something, let's go ahead and spawn a hitbox, jump in the air, crouch down, all basic
[3:42] stuff, let's get into some collision stuff, visual effects, sound effects, we can do pushing of the
[3:51] opponent, throws, we can use cheat codes, give everybody super and then we can use a super move,
[4:07] x move, there we go, we got materials changing, the timer counting down, and let's see if we can do
[4:17] a super move, I believe it is the x button, there we go, so we have all those things going on,
[4:40] so now we can go ahead and close our game and stop tracing, you can just press this button again
[4:44] or go to your menu and click stop trace, now at this point we want to go to the menu I was showing
[4:50] you earlier which is unreal insights, so if we click that button we'll get that same pop-up we did
[4:55] before and this time we should have a file there, you can see it loaded up and we do, we have all
[5:00] the information that we could want about this file, so let me make it the proper size for this window,
[5:05] you can't see it because it's off of my screen capture here, but there's a little icon with
[5:10] unreal engine and a magnifying glass, that is unreal insights, it's this icon right here, it will show
[5:14] up in your toolbar at the bottom, if you're on windows, and then you can look at the name of the
[5:20] file, now the name by default goes to the date and time, you have your platform which is windows 64,
[5:28] the app name is just unreal editor, you can do traces on other things like packaged games,
[5:33] but this is coming from the editor, the build config is debug game which is the default when
[5:37] you're playing in the editor, again if you're doing a packaged game or standalone game you could change
[5:42] that, build target is the editor, here's the file size, now these file sizes do get big pretty quickly,
[5:50] so you may want to clean these up if you don't have a lot of space or save them out to a special
[5:53] location, but when you're ready you can go ahead and double click this or click open trace at the
[5:57] bottom to open up the actual trace, and you can see that we have our GPU, our game thread, and a
[6:04] bunch of other things in here, and so if you look up at the top here you can see how your game was
[6:10] running at every single frame, and you can zoom in to really see every single frame if you want,
[6:15] so you can see your times here, and that timestamp that you see at the start like it says 28
[6:20] minutes 40 seconds, that's actually how long the editor has been open in this case or how long the
[6:24] project has been open, it's not your in-game time like I didn't have the game open for 28 minutes,
[6:29] I had the editor open before I started recording this, and so it's tracing that, if you go to the
[6:34] start you see I started at 27 minutes and 1.96 seconds, so this shows you your fps at every
[6:40] given frame as well as how long each frame took, which is super useful because then you can look
[6:45] at spikes like this, when you want to figure out the reason for your spike you can go down here
[6:49] to this section, so below the graph you have here you go to this area, when you click on a frame it
[6:55] changes everything down here, because it's going to show you everything that was happening during
[7:00] that frame, and you can see it's very precise, like I can scroll in and I can see microseconds
[7:11] even down to some nanoseconds, you can use your scroll wheel to scroll in and out here
[7:16] for Unreal Insights, now the main objective you want to reach to run your game at 60 fps is 16.6
[7:23] milliseconds, see in the little pop-up window where it says game frame 6862 above my cursor,
[7:29] and then in parentheses it has 55.5 fps, it's saying at 18 milliseconds per frame you're running at
[7:36] 55.5 fps, so click on any frame you want to go to and investigate, let's pick this rendering frame
[7:42] 11,545, let's click it, it took 19.92 milliseconds on this frame, so we were getting about 50.2 frames
[7:49] per second at this point, so you can see we're a little bit under where we want to be, and we may
[7:54] want to investigate why that is, once you click on that frame it will highlight the section of what
[7:59] occurred in the time period of the frame we clicked on, remember it was 19.9 milliseconds for that
[8:04] entire frame, this is a 19.9 millisecond window that we have here, this blue section that we have
[8:10] that my mouse is going between, at this point you can scroll up and down through this list to see
[8:18] what was taking up the most, the game thread does have the f-engine loop tick going the whole time,
[8:22] f-engine loop tick was running here, and we can click on that, when we click on that we'll see a
[8:27] section that says call ease down here, if we resize our windows a little bit we can get more space here,
[8:35] so f-engine loop tick was taking up that entire 19.9 millisecond spot, in fact it took longer than
[8:41] that, but for this frame it was filling that entire time slot, now you have the hierarchy here, so we
[8:47] can see we go from tick to frame to slate tick, which is what draws to the screen, then we had to
[8:52] draw windows, then we had pre-pass, the text value is something we can make sense of, it's actually
[8:57] retrieving a text value from some blueprint or widget, since it's in slate we can assume it's a
[9:03] widget, if we go down one more we have git p1 combo rating text, so git p1 combo rating text is
[9:10] something that we have in our base character HUD to actually determine what our combo rating was
[9:15] for player one, so if they've hit the opponent three four times we have to figure out what the
[9:20] rating was, if it was good, great, excellent, combo king, or one of our other values that we have in
[9:25] our game for that, it's taking up 34.6 microseconds, and of that operation we have git enumerator user
[9:33] friendly name, so this is returning the enum value from the result that we pass into it,
[9:38] and then converting from string to text, which is when we display it to the screen,
[9:43] that's taking up 3.1 microseconds,
[9:48] that's just one component here, we have git damage text, git stun frames text, git startup
[9:52] frames text, git press any input text, git active frames text, git recovery frames text,
[9:59] p2 combo rating, round timer, p1 name, p2 name, combo counter, all of these things are functions
[10:06] that we have on our base character HUD that have to be rendered by slate, and the engine is taking
[10:11] and updating that every single frame, and it's taking up some time, now it's normal, these things
[10:16] are going to take time, this is why performance can be really important, because all these little
[10:21] things add up and they don't seem like they make a big difference, but they can, but understanding
[10:25] where they come from, and each part that is being checked in here is really useful to learning what
[10:31] affects your performance and what doesn't, you can see I've opened up a lot of these other ones,
[10:35] and even is valid checks are showing in here, when we have to check to see if something is valid,
[10:41] it takes time, it's only 1.7 microseconds, it's small, but it does take time, so all the values
[10:47] you see in all these drop downs adds up to this git text value, after git text value though, we
[10:54] have git value, and if you open up git value, it is your images, so we have combo counter
[10:59] visibilities, we have our image device brush, we have our p1 character image, as well as our
[11:07] function calls and checks in here, so all that adds up to our frame time as well,
[11:13] then we have the widget invalidating itself, so that it has to redraw every time, and there's
[11:17] so much in here that you can view and look at, and this is just for the game thread, you can look
[11:22] at GPU and stuff as well, however you'll notice there's not much on my side for GPU, on what you
[11:28] call it CPU bound, the GPU is waiting on the CPU, if we go back to this one here, like I was saying,
[11:34] the git p1 combo writing text is taking up the most microseconds of the text values,
[11:39] if we go back into the editor, I can show you exactly where that's at,
[11:43] it's in our base game mode HUD, and I can go into my graph, and you'll see I have a function
[11:50] git p1 combo writing text, so this function is taking the most time out of all the text values,
[11:56] you can see here's the enum to string that it was mentioning earlier, if we go back to
[12:01] Unreal Insights, enumerator user friendly name, that is getting the enum to string node here,
[12:09] and then we're converting it to text, that is the next section here, convert string to text,
[12:17] so you can quite literally come into some logic that you had that you just checked out in Unreal
[12:22] Insights, and adjust this, and maybe I don't need to convert this to a string first, maybe I want
[12:26] to access a data table instead of converting the string, little things like this can make the
[12:31] difference in the long run depending on what you need in your game, how many things you have active,
[12:36] and how optimized you are, so we want to fix this, now I'm going to have an entire episode
[12:40] dedicated to cleaning up each of our tutorials as we get into that, so expect a fighting game one
[12:45] very soon because I'm doing that as I'm going into the AI stuff, this is actually an older build that
[12:50] I have, because I've already done some of this cleanup using this exact method, but for now I
[12:56] just want to show you how to get in here, click on things, understand a little bit of what they mean,
[13:01] I have one other Unreal Insights episode planned where we can go over Unreal Insights for packaged
[13:06] projects as well, packaged projects should run faster than in editor projects, so if you're not
[13:10] reaching the speed that you want, it's not necessarily the end of the world, your packaged
[13:14] project should be significantly faster, you still want the editor to run very fast, but there's always
[13:19] that as an option too, you should check that out and see what speeds you get, so we have a lot more
[13:23] we're going to do with Unreal Insights, but I wanted to get you familiar with it, just how to trace,
[13:27] how to do a quick investigation on what's slowing things down, so anyway guys that's all I got for
[13:31] you today, I hope you enjoyed this episode on using Unreal Insights and I hope you can use it
[13:35] and find it helpful, if you do and can then please subscribe to the channel, it helps me out more than
[13:41] anything else you can do, but I do have a paid option, if you want to support me you can support
[13:44] me on Patreon, YouTube Memberships, or Discord subscriptions, you'll get extra benefits for
[13:49] doing that too, if you need any assistance using Unreal Insights or want more depth than what I
[13:54] gave you here, then feel free to join the Discord community, there's a link in the description,
[13:58] I would be happy to help you out, otherwise guys that's all I got for you today, so thank you so
[14:02] much for watching, I'm Sean The Bro and I'll see you in the next one, goodbye guys!



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
