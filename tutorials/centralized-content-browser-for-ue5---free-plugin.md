---
title: CENTRALIZED CONTENT BROWSER FOR UE5 - FREE PLUGIN
source: YouTube
url: https://www.youtube.com/watch?v=rjTv9jWfY4s
author: Polygonflow Dash
ingested: 2026-06-23
ue_version: "UE5"
tags: ["pipeline", "automation", "beginner"]
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
**Transcript:** Now I'm in the new project.  Let's see just how easy it is to drag in assets from other projects.  Let's open the Content Browser.  The other projects should show up here, but sometimes they're not visible right away.  In this case, go into the Preferences menu and click Search for External Projects.  Dash found two external projects.  Now the assets are available in the Content Browser.  I can search through the folders, but it's much easier to just use keywords.  Let's search for trees.  Or search for rocks.  I can easily drag and drop assets into the scene.  Once I have used some assets from another UE project, I can open the UE Content Browser  and see that the original file structure from the original project is mirrored here.  I can also select another project where I've already computed assets and drag them in just as easily.  I can also select another project where I've already computed assets and drag them in just as easily.  By right-clicking and selecting asset details, I can see information select size, triangle count and which text it has.  I can also select another project where I've already computed assets and drag them in just as easily.

**Frame:** tutorials\frames\centralized-content-browser-for-ue5---free-plugin\frame_002.jpg

### Setup Tips [3:47]
**Transcript:** As mentioned before, one way to utilize this feature in the free Dash Content Browser is to create one big Unreal project with all your assets.  And then you can browse, search and use assets from this project in any other future project.  If you prefer even more structure, another way to utilize this feature is to create specific UE projects like for example, city assets, nature assets or stylized assets.  Doing this will make it even easier to find your preferred assets in future under project.  As you can see, the free Dash Content Browser makes building scenes way easier.

**Frame:** tutorials\frames\centralized-content-browser-for-ue5---free-plugin\frame_003.jpg

### Outro [4:19]
**Transcript:** If you want to learn more, check out our YouTube channel or visit the Polygonflow website.  Thank you for watching and see you in the next one.

**Frame:** tutorials\frames\centralized-content-browser-for-ue5---free-plugin\frame_004.jpg


---

## Structured Notes

### Core Technique
Using the free Dash Content Browser plugin's cross-project asset library to avoid re-importing the same 3D assets into every new Unreal project — compute/tag assets once in a "master" project, then drag them into any other project without copying or migrating files.

### Summary
Shorter companion video to the general Dash Content Browser overview, focused specifically on the cross-project reuse workflow. In a project containing your core asset library (e.g. a "UE5 Assets" project, or a Quixel/Megascans project), open Dash's Content Browser → Project Library tab, select the folder(s) to make available externally, optionally enable AI tagging (auto-tags assets from thumbnail content, not just filenames), and click Compute — assets then become available in ANY other UE project without manual copy/migrate. In a new project, if the source project doesn't appear automatically in the Content Browser, use Preferences → Search for External Projects to detect it. Once detected, assets are searchable by keyword (not just folder browsing) and drag-and-drop directly into the new scene; the original project's folder structure is mirrored once an asset has been used. Right-click → Asset Details shows size, triangle count, and tags for any asset before using it. Recommends two organizational strategies: one giant "everything" project, or several topic-specific projects (e.g. city assets, nature assets, stylized assets) for more structured searching later.

### Key Steps
1. Install the free Dash Content Browser plugin (polygonflow.io).
2. In your asset-library project: Dash toolbar → Content Browser → Project Library tab → select the folder(s) to expose → optionally enable AI tagging → click Compute (processes for a few minutes, assets appear as they finish).
3. In a different/new UE project: open the Dash Content Browser; if the source project isn't listed, go to Preferences → Search for External Projects to detect it.
4. Search by keyword (e.g. "trees", "rocks") across all detected external projects' computed assets, or browse by mirrored folder structure; drag-and-drop directly into the scene — no manual copy/migrate step.
5. Right-click any asset → Asset Details for size/triangle-count/tag info before committing to using it.
6. Organize at the project level: either one master "everything" asset project, or several narrower topic-specific projects (city/nature/stylized, etc.) depending on how much structure you want when searching later.

### UE Systems / Blueprints / Settings
Third-party plugin (Dash Content Browser by Polygonflow) — Project Library tab, AI tagging/Compute process, Preferences → Search for External Projects, cross-project mirrored folder structure, Asset Details panel (size, triangle count, tags). Not a native UE5 system.

### Difficulty
Beginner — plugin setup and drag-and-drop workflow, no node/Blueprint work.

### UE Version
Not specified.

### Tags
"pipeline", "automation", "beginner"

---

## Related Entries
- `best-free-unreal-engine-5-asset-management-plugin-in-2025.md` — same plugin (Dash Content Browser) and author, broader feature overview that this video's cross-project workflow is a focused subset of
