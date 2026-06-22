---
title: NEW Unreal Engine 5.8 MCP Tutorial (QuickStart Guide)
source: YouTube
url: https://www.youtube.com/watch?v=PqrKqhkj3gQ
author: Smart Poly
ingested: 2026-06-22
ue_version: "5.8"
tags: [mcp, ai-agent, pipeline, blueprints, pcg, quickstart]
extraction_status: complete
frames_dir: tutorials/frames/new-unreal-engine-58-mcp-tutorial-quickstart-guide/
frame_count: 0
---

# NEW Unreal Engine 5.8 MCP Tutorial (QuickStart Guide)

**Source:** [YouTube](https://www.youtube.com/watch?v=PqrKqhkj3gQ)
**Author:** Smart Poly
**Duration:** 12m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello guys, welcome back to another video. In this video I'm going to show you how to set up the brand new Unreligion 5.8 mcp plugin. This plugin allows you to connect AI agents such as cloud code or chat GPT directly into your Unreal Engine project. And once connected, these AI agents can understand the context of your entire project and help you with things like blueprints, PCGgrass, materials, C++ code, level design, asset management, and so much more. The possibilities here are honestly pretty crazy. During the Unreal Fest announcement, Epic actually showcased this technology by having an AI agent create an entire city, started by generating a PCG graph, then used that graph to build out a complete city environment inside, using actual assets from the content browser. There's a lot of potential here, and in this video I'm going to show you exactly what you need to do in order to get everything installed, connected, and working correctly, so you can start using the mcp plugin directly inside of your own Unreal Engine projects. And if you were new here to the channel, my name is smartpoly, I make all sorts of Unreal Engine news, content, and tutorials, so make sure you drop a lik...



---

## Structured Notes

### Core Technique
A quickstart guide for installing and connecting Unreal Engine 5.8's official MCP (Model Context Protocol) plugin, which exposes a project's full context — Blueprints, PCG graphs, materials, C++ code, level design, and asset management — to AI agents such as Claude Code or ChatGPT.

### Summary
Smart Poly introduces the new UE 5.8 MCP plugin, which connects AI agents directly into an Unreal Engine project so the agent can understand and act on the project's actual context rather than working blind. He references Epic's Unreal Fest demo where an AI agent generated a PCG graph and used it to build an entire city from real content-browser assets, framing this as a preview of the plugin's potential. The video then walks through installing the plugin and getting it connected so it works correctly with AI agents from inside the user's own UE projects. (Whisper transcript truncated by ingestion at ~1200 characters; the exact installation/connection steps shown later in the video were not captured here and would need a follow-up pass — e.g. re-running ingestion without the per-chapter truncation, or reviewing the full video directly — for complete step-by-step detail.)

### Key Steps
1. [Context] Understand the MCP plugin's purpose: bridges AI agents (Claude Code, ChatGPT, etc.) into live UE project context
2. [Capabilities] Recognize the scope of what a connected AI agent can act on: Blueprints, PCG graphs, materials, C++ code, level design, asset management
3. [Reference case] Epic's Unreal Fest demo — AI agent builds a PCG graph, then a full city using real content-browser assets
4. [Install] Install the official UE 5.8 MCP plugin (exact steps not captured in available transcript)
5. [Connect] Connect an AI agent client (e.g. Claude Code) to the running UE project via the MCP plugin (exact steps not captured)
6. [Verify] Confirm the connection works correctly before relying on it in a real project

### UE Systems / Blueprints / Settings
- UE 5.8 MCP plugin — official Epic plugin exposing project context (Blueprints, PCG, materials, C++, level design, assets) over the Model Context Protocol
- PCG (Procedural Content Generation) graph — referenced as the basis for the Unreal Fest AI-built-city demo
- AI agent client (Claude Code / ChatGPT) — connects to the MCP plugin to read/act on project context

### Difficulty
Beginner

### UE Version
5.8

### Tags
mcp, ai-agent, pipeline, blueprints, pcg, quickstart

---

## Related Entries
- [How Unreal 5.8 Changed Filmmaking](how-unreal-58-changed-filmmaking.md) — another UE 5.8-focused video, covering filmmaking/rendering features rather than the AI-agent MCP plugin
