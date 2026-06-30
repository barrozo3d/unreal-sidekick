---
title: NEW Unreal Engine 5.8 MCP Tutorial (QuickStart Guide)
source: YouTube
url: https://www.youtube.com/watch?v=PqrKqhkj3gQ
author: Smart Poly
ingested: 2026-06-23
ue_version: "UE5.8"
tags: [mcp, ai-agent, claude-code, blueprint, pcg, workflow, automation, plugin, setup, tool]
extraction_status: complete
frames_dir: tutorials/frames/new-unreal-engine-58-mcp-tutorial-quickstart-guide/
frame_count: 4
---

# NEW Unreal Engine 5.8 MCP Tutorial (QuickStart Guide)

**Source:** [YouTube](https://www.youtube.com/watch?v=PqrKqhkj3gQ)
**Author:** Smart Poly
**Duration:** 12m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello guys, welcome back to another video. In this video I'm going to show you how to set up the brand new Unreligion 5.8 mcp plugin. This plugin allows you to connect AI agents such as cloud code or chat GPT directly into your Unreal Engine project. And once connected, these AI agents can understand the context of your entire project and help you with things like blueprints, PCGgrass, materials, C++ code, level design, asset management, and so much more. The possibilities here are honestly pretty crazy. During the Unreal Fest announcement, Epic actually showcased this technology by having an AI agent create an entire city, started by generating a PCG graph, then used that graph to build out a complete city environment inside, using actual assets from the content browser. There's a lot of potential here, and in this video I'm going to show you exactly what you need to do in order to get everything installed, connected, and working correctly, so you can start using the mcp plugin directly inside of your own Unreal Engine projects. And if you were new here to the channel, my name is smartpoly, I make all sorts of Unreal Engine news, content, and tutorials, so make sure you drop a like and subscribe for more future videos. Also, before we get into the video, I just released my new Unreal Engine Masterclass course bundle. I just launched a brand new Unreal Engine Masterclass course. This bundle together all of my courses, showing you how to make games inside of Unreal Engine. This Masterclass course has over 150 plus hours of learning content, and I will show you how to make eight different games from complete scratch. You'll master multiplayer networking, survival mechanics, AI, user interfaces, game optimization, mobile development, and so much more included in the Masterclass bundle or all the completed game project source files. So you can use them as a reference while you learn, or if you just want the completed game project, we have you covered. Check out the Unreal Engine Masterclass link in the description below, and with that being said, let's get right back to the video. Alright, so the first thing that you'll need to do to get started is to download Unreal Engine 5.8. This will only work with 5.8, so go ahead and launch. So we're just going to create a brand new project here. I'll just do a third person. You can rename this to whatever you'd like. I'll name this to my MCP tutorial and click create. Okay, so now that we're in our project, what we need to do is go to our edit plugins, and we need to search and enable a couple of plugins. The first one is the MCP plugin, the Unreal MCP over here. So go ahead and enable that. Okay, then we want to search for Terminal. Terminal is what we're going to use actually communicate with the AI. So go ahead and click yes, and then the last one, which is very important, is the editor toolset. So this editor toolset is what actually connects the Unreal Editor with the AI agent. So this is like bridges the gap, and it gives it context control over blueprints, actors, all the different systems, like PCG, materials, all that stuff. So you want to make sure that you enable this if you want it to be able to edit all of your properties. So enable that and click restart now. All right, now that this has been restarted, we need to configure the actual plugin. So you want to go to your editor preferences, and about halfway down the list over here, you should see model context protocol. So select that. Over here, you can see the server port number and all that information. That's all good. We don't need to change that, but you can also enable to auto start the server. So this will auto start it that way when you launch your project, it'll be already good to go. So click that little check box. Then the other thing that we need to configure is we need to go over to the terminal down here. And we want to add a couple of startup commands. So over here, we have to add a couple three different entries. And basically, I'm going to copy and paste some texts, but I'll have this text in the description. We have set term 256 color over here. And then the other one we need is we need the path to our project. So for that, I'm going to paste this. This is going to be CD, the directory. Again, I'll put this in the description, but this part over here and quotations, this needs to be the path to your unreligion project. So in order to find the path to this exact project that we're in, you just go to your content drawer here. Right click the content folder and do show and explore that will show you exactly where the project is stored on your hard drive. Just copy this path. Okay, everything from the tutorial, the name of the project and up. And then paste that in the quotation. So you'll have your disk in my case, eDrive, unreligion projects, my mcp tutorial, the name of my project. Okay, and the last one, since we're going to be using cloud code, I'm going to type in a cloud. And I'll show you guys how we're going to set this up, but that will just make sure that cloud runs when you actually start up the engine. So basically what these do is when we start up, we open up our project for the first time. We'll set the color, set the directory and also run cloud. Okay, so now we actually need to configure cloud in order for this to work. So for that first, we need to go ahead and install cloud code to our computer. So in order to do that, we'll use the quick start guide from their documentation. Over here, you have the install code. So for Mac, Linux over here, you can run the command for windows. You can either use PowerShell or CMD. I'll use the command prompt. So just type in your search search for CMD and then just copy this command over here. Okay, and then paste it like so. Okay, what it will go ahead and do is install cloud code. Now you might get a message saying that cloud code on windows requires either get for windows for bash or PowerShell installed one of the following. And it has two different links. So what I went ahead and done is downloaded get SCM. So I'll leave a link to that in the description below. And so you'll need to go ahead and download this. So over here to get SCM again, you just go over here to the windows 64 setup. So go ahead and download that. Okay, and once you downloaded get SCM and you'll go through the installation options, you'll just click next. You just click next through all of the different settings. There's a bunch of different settings. You just click next through all them. And then once that's complete, you come back to CMD again, paste the same CMD install command from cloud code into your terminal here. And then once that's finished, it should say cloud code successfully installed just like that. Okay, now the next thing that we'll need to do is set the path. Okay, in order to actually use cloud code, we need to make sure that when we type in a terminal, we add the system environment variable or the path to it. So for that, you just hold down the windows plus R key and type in sysdm.cpl. What this will open up is the system properties because we'll need to add the environment variable. And then we'll need to go over to advance over here and under environment variables, click on that, scroll down. This is the user variables for my current user, which is sp. So you'll do the same for your own user. Over here under the path, you want to select that and click edit. And then at the very bottom, we want to add a new path over here, click the new button. And the path is over here. Okay, so wherever we installed cloud code to this location, in my case, mine's under users, my username sp local bin cloud code.exe. So copy this from bin all the way over like that. And then add a new one, paste it. And it should be like this. See users your username local bin. Okay, so once you do that, click okay, click okay. And okay, over there. And now if you got to reopen up the command prompt again, open up cmd, type in cloud. And we'll click yes, trust this folder. It should say, you know, log in to cloud over here and all that stuff. Okay, now I've already logged in. So if you don't have an account, we'll need to go ahead and do is create one. So you'll just go over to the website cloud.ai and you'll create a new account. You can create a free account with a limited accessibility pro. This is the plan that I'm actually using right now. It's about $20 a month if you do monthly. And then if you want a lot of usage, some people use the max plan, which is a hundred bucks a month. But once you go ahead and create an account and you know, either choose whatever plan you want, then you can come back to the terminal and it will say slash log in. So you'll do like slash log in, okay, and it will open up a window, something like this and you'll go ahead and log in. And once it's all logged in, it should be good to go. Okay, so it should look something like this. So now that that has been done, we come back to our project over here. And we need to run a command in order to set up the config file. And if you're using any other AI, and you can use any AI model of a choice, but for this tutorial, we'll be using cloud code. And if you're using a different model, you can reference the documentation here, which shows you everything you need to know. But over here in the documentation, it shows us the exact steps we need to take. So we need to generate a client config file. In our case, since we're using cloud code, we're going to use this console command over here. You can copy it. But if you're using a different AI agent like cursor, VS code, Gemini, codex, chat, GPT, it has the different commands over here for that. Okay, so once we copy this, we'll go back to our project and in the console command, you'll paste that, press enter. And that should go ahead and generate if we go to our content folder, right click show and explore and go up to the MCP tutorial. It created this new file called the .mcp.json. So if I go ahead and edit this, basically it has the URL and all that stuff. Okay, so that's good to go. And now just make sure that you restart your project. So just close this and then go back to your Epic Games launcher. And then just double click and reopen up your project. Now that we're back in our project, you want to go over to tools. And about halfway down, you'll see terminal. So go ahead and click on that. It's going to ask us if we want to trust this folder. Just click enter in here and it's going to say new MCP server found in this project. And we're going to use this MCP server. And now you should see that it shows the cloud code over here. Welcome back. If you need to log in, you'll do slash log in and you should be able to log into your count. Okay, so let's go ahead and actually test this out. So for our test, I'll just create a new level. So I'm going to create a new level here. And you can choose basic or open world. I think I'll just do open world here. Click create and we have a nice little level. We can start playing around with this. So I'm going to file save our current level to the disk save current level as you can just save it as a new map. Go ahead and save that. But just to test that this is working, we can give this guy a command like create five different colored cubes stacked on top of each other. And my level press enter. Then it should go ahead and start processing. Also, you can change your model right now. I'm using the opus 4.8 model by default. I think it's on it, which is like the lower end model. And I think if you're using the free plan, you won't have access to the higher ones. You won't have access to the higher models. So okay, so it just finished. And yeah, over here, this is where it actually placed it at our player start. So as you can see, we have one, two, three, four, five different cubes. And it looks like created five different static mesh actors over here. And it created five different materials. And actually, these are even material instances. So bonus points for them looks like they use the basic master material. And they created five material instances from that. Which is then used five different colors. So yeah, as you can see, it is working properly. Now you can basically use it to do whatever. You can actually use it to help you debug your code or make different types of blueprints. I've done a little bit of testing and I got it to make a simple soccer ball and a goal that I can score the ball and it will reset. And I'll be making some more future videos testing and showcasing the capabilities. As they showed in the Unreal Fest demo, they use it to create a complete city generator PCG graph. So I'm actually going to try and test that later on. So you want to see a full video on how to do that. Make sure that you subscribe. And also let me know what you guys think about this down in the comments down below. Is this something you're interested in? And is there anything you want me to test out with this? Let me know down in the comments down below. But that's pretty much it for this video. So hope you guys enjoyed and I'll see you guys in the next one.

**Frame:** tutorials\frames\new-unreal-engine-58-mcp-tutorial-quickstart-guide\frame_000.jpg


---

## Structured Notes

### Core Technique
UE5.8 MCP (Model Context Protocol) plugin setup: enables AI agents (Claude Code, ChatGPT, etc.) to connect directly into Unreal Engine with full project context — blueprints, PCG, materials, C++, level design, asset management. Three required plugins: **Unreal MCP**, **Terminal**, **Editor Toolset**. Configure Editor Preferences → Model Context Protocol. Generate `.mcp.json` via console command. Works by running Claude Code (or other AI CLI) in UE's built-in Terminal panel.

### Summary
12-minute Smart Poly quickstart guide for the UE5.8 Model Context Protocol plugin. AI agents connect to UE5.8 through the MCP plugin to understand and modify the entire project. Setup involves: enabling three plugins (Unreal MCP + Terminal + Editor Toolset), configuring auto-start and terminal startup commands (set color, CD to project path, launch `claude`), installing Claude Code CLI on Windows (via CMD; requires Git for Windows for bash), setting PATH environment variable, generating `.mcp.json` via console command, restarting. Demo: Claude Code creates 5 colored cubes in a new level — creates static mesh actors + distinct material instances per cube. Epic Unreal Fest demo showed MCP creating a full PCG-based city.

### Key Steps
1. **Install UE5.8**: MCP plugin requires UE5.8 specifically
2. **Enable three plugins** (Edit → Plugins):
   - **Unreal MCP** (search "MCP")
   - **Terminal** (for AI communication)
   - **Editor Toolset** (bridges editor + AI; gives context over blueprints/actors/PCG/materials)
   - Restart when prompted
3. **Configure MCP**:
   - Edit → Editor Preferences → scroll to **Model Context Protocol**
   - Check **Auto Start Server** → server starts automatically on project open
4. **Configure Terminal startup commands** (Window → Terminal):
   - Add entry: `set term=256color`
   - Add entry: `cd "C:\path\to\your\project"` (find path: right-click Content folder → Show in Explorer, copy up to project name)
   - Add entry: `claude` (or your AI CLI command)
5. **Install Claude Code on Windows**:
   - Open CMD → paste install command from claude.ai docs
   - If prompted about bash: install **Git for Windows** (Git SCM) first, then re-run install command
   - After install: "Claude Code successfully installed"
6. **Set PATH environment variable**:
   - Win+R → `sysdm.cpl` → Advanced → Environment Variables
   - User variables → Path → Edit → New → add: `C:\Users\<username>\AppData\Local\bin`
   - OK → OK → OK; re-open CMD to verify `claude` command works
7. **Log in to Claude**:
   - Type `claude` in CMD → `/login` → follow browser login
   - After login, CMD shows Claude Code ready
8. **Generate MCP config file**:
   - In UE console command field: paste the MCP config generation command (from Epic docs; different per AI agent: Claude, Cursor, VS Code, Gemini, ChatGPT, Codex all have separate commands)
   - Check project folder: `.mcp.json` file created with server URL/port
9. **Restart project**: close and reopen from Epic Games Launcher
10. **Connect**: Tools → Terminal → trust folder → "New MCP server found" prompt → accept → Claude Code appears in terminal, ready for commands
11. **Change model**: can select different Claude models in terminal (default may be Sonnet; Opus 4.8 for higher capability)

### UE Systems / Blueprints / Settings
- **Unreal MCP Plugin** — core MCP server plugin; runs a local server that AI agents connect to; UE5.8 required
- **Terminal Plugin** — built-in UE terminal panel; startup commands run when Terminal first opens; hosts the AI CLI session
- **Editor Toolset Plugin** — gives AI agent context over and control of: Blueprints, actors, PCG graphs, materials, C++, level design, asset management
- **Model Context Protocol (MCP)** — open protocol enabling AI agents to query/modify external tools with full context; Editor Preferences → Model Context Protocol; server port configurable; Auto Start Server option
- **`.mcp.json`** — config file in project root; generated via UE console command; contains server URL; required for AI agent to connect
- **Claude Code CLI** — Anthropic's CLI; used as the AI agent in this tutorial; installed via CMD/PowerShell; requires Git for Windows on Windows; set PATH manually
- **PCG (Procedural Content Generation)** — primary showcase use case for MCP; Epic demo created a full city PCG graph via AI agent
- **Model selection** — can switch Claude models within the terminal session (Sonnet, Opus 4.8, etc.); free plan limited to lower-tier models

### Difficulty
Intermediate (Setup). The actual usage post-setup is beginner-friendly. Setup involves CLI installation, PATH editing, and multi-plugin configuration — not beginner territory. Once running, commanding the AI is conversational.

### UE Version
UE5.8 (MCP plugin is UE5.8-specific; will not work with earlier versions per tutorial)

### Tags
mcp, ai-agent, claude-code, blueprint, pcg, workflow, automation, plugin, setup, tool

---

## Related Entries
- `procedural-content-generation-framework-in-unreal-engine.md` — PCG framework; primary use case for MCP AI automation (city generation demo)
- `new-unreal-engine-58-metahuman-crowd-plugin.md` — another UE5.8 new feature from same author/time period
- `new-unreal-engine-58-metahuman-markerless-mocap-tutorial.md` — UE5.8 markerless mocap (third UE5.8 feature from Smart Poly)
