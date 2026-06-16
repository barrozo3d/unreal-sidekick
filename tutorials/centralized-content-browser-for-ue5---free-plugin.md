---
title: CENTRALIZED CONTENT BROWSER FOR UE5 - FREE PLUGIN
source: YouTube
url: https://www.youtube.com/watch?v=rjTv9jWfY4s
author: Polygonflow Dash
ingested: 2026-06-16
plugin_version: dash-1.6
ue_version: "UE 5.x"
tags: [dash-1.6, content-library, asset-management, cross-project, ai-tagging, polyhaven, beginner]
extraction_status: complete
frames_dir: tutorials/frames/centralized-content-browser-for-ue5---free-plugin/
frame_count: 5
---

# CENTRALIZED CONTENT BROWSER FOR UE5 - FREE PLUGIN

**Source:** [YouTube](https://www.youtube.com/watch?v=rjTv9jWfY4s)
**Author:** Polygonflow Dash
**Duration:** 4m50s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** I used to hate the fact that every time I open a new project in Unreal, I have to re-import  my 3DS-ets.  Finally, we have a solution for you.  It's a feature that in our Unreal Engine plugin called the Dash Content Browser and it's  completely free.  You all have to import your S1 time and they will be available for you in all your other  projects.  It has saved me a ton of time.  Let me show you how it works.

**Frame:** tutorials\frames\centralized-content-browser-for-ue5---free-plugin\frame_000.jpg

### Initial Setup [0:24]
**Transcript:** First, let's download the free Dash Content Browser from the polygon for a website.  You will find the link in the description.  Once I have installed Dash, I will open all my UE5 assets project that contains all my  essential assets.  I also have the Darkrain's Megascans project here and I will make those assets easily accessible  in a new project as well.  I've opened all my UE5 assets project.  You can see all my assets nicely lined up.  I will open the Content Browser and under the project library tab, you will see the  follow structure on the left, but no assets have been computed yet.  I select the folder I want to make available in other projects.  I can also choose whether or not I want to use AI taking for the assets.  AI taking has to find your assets way more easily because Dash's AI taking system automatically  adds text based on thumbnails, not just fine names.  I will click on the Compute button and you will see the assets start appearing.  Once the process is finished, these assets will be accessible in any project.  No need to copy or migrate them manually.

**Frame:** tutorials\frames\centralized-content-browser-for-ue5---free-plugin\frame_001.jpg

### Using Assets from Other Projects [1:38]
**Transcript:** Now I'm in the new project.  Let's see just how easy it is to drag in assets from other projects.  Let's open the Content Browser.  The other projects should show up here, but sometimes they're not visible right away.  In this case, go into the Preferences menu and click Search for External Projects.  Dash found two external projects.  Now the assets are available in the Content Browser.  I can search through the folders, but it's much easier to just use keywords.  Let's search for trees.  Or search for rocks.  I can easily drag and drop assets into the scene.  Once I have used some assets from another UE project, I can open the UE Content Browser  and see that the original file structure from the original project is mirrored here.  I can also select another project where I've already computed assets and drag them in just as easily.  I can also select another project where I've already computed assets and drag them in just as easily.  By right-clicking and selecting SAD details, I can see information select size, triangle count,  and which text it has.  By right-clicking and selecting SAD details, I can see information select size, triangle count, and which text it has.  I can also...

**Frame:** tutorials\frames\centralized-content-browser-for-ue5---free-plugin\frame_002.jpg

### Setup Tips [3:47]
**Transcript:** As mentioned before, one way to utilize this feature in the free Dash Content Browser is to create one big Unreal project with all your assets.  And then you can browse, search, and use assets from this project in any other future project.  If you prefer even more structure, another way to utilize this feature is to create specific UE projects like for example, city assets, nature assets, or stylized assets.  Doing this will make it even easier to find your preferred assets in future under projects.  As you can see, the free Dash Content Browser makes building scenes way easier.

**Frame:** tutorials\frames\centralized-content-browser-for-ue5---free-plugin\frame_003.jpg

### Outro [4:19]
**Transcript:** If you want to learn more, check out our YouTube channel or visit the Polygonflow website.  Thank you for watching and see you in the next one.

**Frame:** tutorials\frames\centralized-content-browser-for-ue5---free-plugin\frame_004.jpg


---

## Structured Notes

### Core Technique
Dash 1.6 cross-project asset access — compute assets in a source project once, then search and drag-drop them into any future UE5 project directly from the Dash Content Browser without migration or re-import.

### Summary
5-minute tutorial introducing the centralized/cross-project feature of the free Dash Content Browser. Compute assets in one "source" UE project (with optional AI tagging for property-based search) → open any new project → Preferences → Search for External Projects → computed assets appear and are browseable by keyword. Original file structure from the source project is mirrored in the UE Content Browser when assets are used. Recommended workflows: one master asset project OR category-specific projects (city, nature, stylized).

### Key Steps
1. **Open source project** — the project where your 3D assets live; open Dash Content Browser → Project Library tab
2. **Select folder** — choose the folder(s) to make globally available; enable AI Tagging option
3. **Click Compute** — Dash AI processes thumbnails and generates tags; may take a few minutes; runs once and persists
4. **Open new/target project** — open Dash Content Browser; if external projects not visible → Preferences → Search for External Projects → Dash auto-discovers computed projects
5. **Search and use** — type keywords (`trees`, `rocks`, `city`) to search across external project assets; drag and drop directly into scene
6. **Right-click → Asset Details** — view physical size, triangle count, AI-generated tags
7. **Check UE Content Browser** — source project's file structure is mirrored when assets are used (original files, not copies)

### UE Systems / Blueprints / Settings
- **Cross-project compute** — Compute in source project marks assets as globally discoverable; no file migration
- **Preferences → Search for External Projects** — auto-discovers all UE projects with computed Dash assets on the machine
- **AI Tagging (optional)** — enables property-based search across external project assets (`trees`, `wooden`, `blue`)
- **UE Content Browser mirroring** — when an external asset is dropped into a scene, UE creates a reference in the native Content Browser mirroring source folder structure
- **Organization strategies** — Option A: one master "all assets" project; Option B: category projects (city/nature/stylized) for structured browsing

### Difficulty
Beginner

### UE Version
UE 5.x (Dash 1.6)

### Tags
`#dash-1.6` `#content-library` `#asset-management` `#cross-project` `#ai-tagging` `#polyhaven` `#beginner`

---

## Related Entries
- [[best-free-unreal-engine-5-asset-management-plugin-in-2025]] — full Content Browser feature set including Collections + Unified View
- [[auto-tag-sort-1000-ue5-assetsmonth-with-this-free-content-browser]] — AI tagging workflow
- [[architecture-scenes-made-easy-in-unreal-engine-5---dash-tutorial]] — cross-project tree access used in production (Dash 1.6 mention)
- [[2000-free-high-quality-assets-for-any-unreal-engine-project]] — Poly Haven + IES libraries
