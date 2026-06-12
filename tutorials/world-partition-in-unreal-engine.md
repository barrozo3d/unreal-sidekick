---
title: World Partition in Unreal Engine
source: Epic Documentation
url: https://dev.epicgames.com/documentation/unreal-engine/world-partition-in-unreal-engine
ingested: 2026-06-12
ue_version: "UE 5.7"
tags: [world-partition, large-worlds, streaming, data-layers, hlod, one-file-per-actor, level-instancing, environment, pcg, intermediate, advanced, ue5-7]
extraction_status: complete
page_count: 1
---

# World Partition in Unreal Engine

**Source:** [Epic Documentation](https://dev.epicgames.com/documentation/unreal-engine/world-partition-in-unreal-engine)
**Pages crawled:** 1
**Ingested:** 2026-06-12

---

## Raw Documentation Content


### World Partition in Unreal Engine
**URL:** https://dev.epicgames.com/documentation/unreal-engine/world-partition-in-unreal-engine

World Partition in Unreal Engine | Unreal Engine 5.7 Documentation | Epic Developer Community Table of Contents Building large maps used to require developers to manually divide maps into sublevels, then use the Level streaming system to load and unload them as the player traversed the landscape. This method often created issues sharing files between multiple users, and viewing the whole world in context became a difficult task. Click image for full size. World Partition is an automatic data management and distance-based level streaming system that provides a complete solution for large world management. The system removes the previous need to divide large levels into sublevels by storing your world in a single persistent level separated into grid cells, and provides you with an automatic streaming system to load and unload those cells based on distance from a streaming source. World Partition works closely with the following features: One File Per Actor World Partition - Data Layers Level Instancing World Partition - Hierarchical Levels of Detail Enabling World Partition There are three ways to enable World Partition within Unreal Engine: Creating a new project from a template in the Games category. Creating a new Level using the Open World template. Converting existing levels to use World Partition. Creating Your Project using a Games Template World Partition is enabled by default in many of the project templates found in the Games category. Click image for full size. To reduce complexity and provide a scalable solution when creating new projects, grid cell streaming can be enabled and disabled using the Enable Streaming option in the World Settings . Click image for full size. The following templates use World Partition but have Enable Streaming disabled by default: Blank First Person Third Person Top Down Vehicle Advanced Using the Open World Default Map The Open World default map type is designed to be a starting point for creating large open-world maps and comes with the following features enabled by default: World Partition One File Per Actor Data Layers Hierarchical Levels of Detail Click image for full size. The map contains a sample 2 km x 2 km Landscape with a Landscape Material and lighting setup for an outdoor environment. This includes a sky atmosphere, skylight, directional light, exponential height fog, and volumetric clouds. Click image for full size. To use the Open World default map type within your project: Open the File menu and select New Level . Select the Open World map type. Click the Create button to create a new map. Converting Existing Levels to use World Partition You can add World Partition to any Level by converting it using the Tools Convert Level menu option, or by using the World Partition Convert Commandlet. To use the World Partition Convert commandlet, follow these steps: Click image for full size. Command: UnrealEditor.exe QAGame -run=WorldPartitionConvertCommandlet Playground.umap -AllowCommandletRendering To convert your existing Levels to World Partition: In Windows, open a Command Prompt window. At the prompt, begin by navigating to the location of the UnrealEditor.exe executable file. In the above example: c:\Builds\Home_UE5_Engine\Engine\Binaries\Win64 . Next, begin the command with the name of the .exe file that will run the commandlet, UnrealEditor.exe Add the name of the project. Here, QAGame . Continue with the name of the commandlet to run, -run=WorldPartitionConvertCommandlet . Add the name of the map file that will be converted. In the above example Playground.umap . Finish the command with the additional argument -AllowCommandletRendering . Press Enter and the commandlet will convert the map to use World Partition. The following optional arguments are available for this commandlet: Optional Argument Description -SCCProvider=(None,Perforce...) Specifies which source control provider to use. To run without source control, specify -SCCProvider=None . -Verbose Displays verbose logging. -ConversionSuffix Appends the _WP suffix to a converted map. This is useful when converting Levels for testing purposes while keeping the source Level intact. -DeleteSourceLevels Deletes source Levels after conversion. -ReportOnly Reports what would happen during the conversion. Does not do the conversion. -GenerateIni Generates a default .ini conversion file for this map. Does not do the conversion. -SkipStableGUIDValidation Skips the unstable actor GUIDs validation process. Levels with unstable actor GUIDs will result in different conversion output when converting several times. Resaving the Level fixes this. -OnlyMergeSubLevels Converts and merges Levels and Sublevels to One File Per Actor without World Partition. The converted Level can be used as a Level Instance in a World Partition Level. -FoliageTypePath=[Path] Extracts Foliage Types as Assets to the given path. Use if the Level contains embedded Foliage Types. If you want to alter the conversion settings, use a default conversion .ini file with the commandlet. The .ini file needs to be in the same folder as your map file and have the same filename as your map, but with the .ini extension. For example, an .ini file written for the FirstPersonExampleMap.umap would be named FirstPersonExampleMap.ini . Here is an example of a default conversion .ini file: [/Script/UnrealEd.WorldPartitionConvertCommandlet] EditorHashClass=Class'/Script/Engine.WorldPartitionEditorSpatialHash RuntimeHashClass=Class'/Script/Engine.WorldPartitionRuntimeSpatialHash LevelsGridPlacement=(("/Game/Maps/Highrise_Audio", Bounds),("/Game/Maps/Highrise_Collisions_Temp", Bounds),("/Game/Maps/Highrise_Gameplay", Bounds),("/Game/Maps/Highrise_Lights", Bounds),("/Game/Maps/Highrise_Vista", AlwaysLoaded)) HLODLayerAssetsPath= DefaultHLODLayerName= [/Script/Engine.WorldPartitionEditorSpatialHash] CellSize=51200 WorldImage=None Expand code Copy full snippet (15 lines long) Using World Partition The World Partition system works by storing your world in a single persistent Level file and subdividing the space into streamable grid cells using a configurable runtime grid. These cells are loaded and unloaded at runtime by the presence of streaming sources, such as the player. In this way, Unreal Engine only loads the parts of the Level that the player sees and interacts with at a given time. Actors in World Partition When editing the world, Actors can be added anywhere and are automatically assigned to a grid cell based on their Is Spatially Loaded setting, found in their Details panel's World Partition section. Click image for full size. Option Description Runtime Grid Determines in which partition grid this Actor is placed. If None , the grid will be chosen by the partition system. Is Spatially Loaded Determines if the Actor is spatially loaded: If enabled, this Actor is loaded when in range of any streaming source when not assigned to a disabled Data Layer. If disabled, this Actor is loaded when not assigned to a disabled Data Layer. Since Actors are saved to their own individual files using the One File Per Actor feature, you do not need to check out the Level file from source control to make changes to the Actors in the world. This frees up the Level file for others on your team. For more information on the One File Per Actor system and Unreal Engine's integrated source control, see the One File Per Actor documentation. Actors that reference other Actors in the Level will be bundled together and loaded at the same time. Streaming Sources Streaming of grid cells within the grid at runtime is determined by two factors: Streaming Sources Runtime Grid Settings The first is the position of streaming sources in the Level. Click image for full size. Streaming sources are components that define a position in the world and trigger the loading of cells around them. Player Controllers are a streaming source. Other streaming sources can be added to the world using the World Partition Streaming Source component. For example, a streaming source component can be activated at the location that a player will teleport to, so it can load the cells there. Once the grid cells are loaded, the player teleports to the location and the streaming source component is deactivated. Since there is no longer a streaming source at the player's previous location, those grid cells would be unloaded. Using the Player as a Streaming Source Each Player Controller is used as a World Partition streaming source using the Enable Streaming Source option. This is enabled by default: Click image for full size. Using the World Partition Streaming Source Component World Partition streaming is also done using the World Partition Streaming Source component: Click image for full size. This component has the following options: Option Description Default Visualizer Loading Range Determines the size of the debug visualizer grid when the visualizer is enabled. Target Grid Determines the streaming grid affected by this source. Debug Color Determines the color used for debugging. Target HLOD Layer Determines the HLOD Layer affected by the streaming source. Shapes Determines the shape list used to build a custom shape for this streaming source. If empty, will use a sphere with a radius equal to the grid loading range. Priority Determines the priority of the streaming source. If a grid cell intersects multiple streaming sources, its priority will be the highest priority amongst all streaming sources. Streaming Source Enabled Determines if this component is enabled. Target State Determines which state the intersecting grid cell should be in (either Loaded or Activated). If a grid cell intersects multiple streaming sources, the target state will be the highest target value (where activated is greater than loaded). The Blueprint functions Enable Streaming Source and Disable Streaming Source will enable and disable streaming with this component. Click image for full size. The Blueprint function Is Streaming Completed returns true when the component has finished streaming the grid cells that it intersects with. Runtime Grid Settings The second factor that determines whether a grid cell is loaded or unloaded at runtime is the settings of the runtime grid itself. Runtime grid settings are located in the World Settings panel, in the World Partition Setup section. A 2D Runtime Hash grid is provided by default. Using more than one grid can negatively impact performance. For more information on the recommended setup and settings for your 2D Runtime Hash grid, see the Big City map located in the City Sample project. Click image for full size. Option Description Grid Name Contains the name of the runtime grid. Cell Size Determines the size of the grid cells that are used to generate the streaming Levels. In the example, the Cell Size is 256m x 256m x 256m. Loading Range Determines the range from a streaming source where cells are loaded. In the image above, the Loading Range is a 768 meter radius around a streaming source. Block on Slow Streaming Blocks loading in situations where grid cells are not loading fast enough. Priority Determines the priority of the streaming source. If a grid cell intersects multiple streaming sources, its priority will be the highest priority amongst all streaming sources. Debug Color Determines the color of the grid lines that are shown when Preview Grids is enabled. Preview Grids When enabled, displays the grid lines in the viewport. Loading and Unloading Regions in the Editor To support the development of large worlds, the world is initially unloaded. When the Level opens, the Editor only loads Actors that have their Is Spatially Loaded setting marked as False , such as environment backdrops and managers. This supports the development of large worlds where it is impossible to load the entire map in the Editor. Load and Unload Regions Using the World Partition Window In the World Partition window, you can manually select the region to work in. Open the window by... [truncated]


---

## Structured Notes

### Core Topics
World Partition streaming system, Grid cells, Streaming Sources, Data Layers, One File Per Actor, Hierarchical LOD (HLOD), Level Instancing, Level conversion commandlet, Large world design

### Summary
World Partition is UE5's automatic data management and distance-based level streaming system for large worlds. It replaces manual sub-level division with a single persistent level divided into grid cells that load/unload based on streaming sources (player position + explicit streaming source components). Key companion features: One File Per Actor (source control friendly actor storage), Data Layers (toggle-able actor groups), HLOD (automatic LOD for far objects), and Level Instancing (reusable sub-level templates).

### Key Concepts & Systems

| Concept | Description |
|---------|-------------|
| **Grid Cells** | Level divided into configurable cells (default Cell Size 256m); each cell is a streaming Level |
| **Streaming Sources** | Components that define a position; trigger cell loading within `Loading Range` radius |
| **Player Controller** | Default streaming source (enabled by default via `Enable Streaming Source`) |
| **WP Streaming Source Component** | Add to any Actor to serve as a streaming source (e.g., teleport destination) |
| **Is Spatially Loaded** | Actor property: ON = loaded when in range of source; OFF = always loaded |
| **Runtime Grid** | 2D Runtime Hash grid; Cell Size + Loading Range define what's streamed |
| **Data Layers** | Tag actors with layers; layers can be activated/deactivated at runtime (story gating, seasonal changes) |
| **One File Per Actor** | Each actor saved to own file; no Level file checkout needed for edits (source control friendly) |
| **HLOD** | Hierarchical Levels of Detail; auto-generates lower-fidelity proxies for distant cells |
| **Level Instancing** | Reusable sub-level templates; can be placed multiple times in a WP world |
| **Open World Template** | Default map with WP + One File Per Actor + Data Layers + HLOD enabled; 2km×2km landscape |
| **World Partition Window** | Editor window for manually loading/unloading regions and visualizing grid |

**Data Layers:**
- **Editor Data Layers**: visible only in editor (markup layers for organization)
- **Runtime Data Layers**: toggle at runtime via Blueprints → event-driven level streaming
- Use case: unload daytime environment, load nighttime; unload pre-mission map, load post-mission

**One File Per Actor:**
- Actors saved as individual `.uasset` files instead of all-in-level
- Multiple team members can edit different actors simultaneously (no Level file conflict)
- Works with Perforce/Svn/Git via `SCCProvider` argument

### UE Systems / Settings / Code

**World Settings — World Partition Setup:**

| Setting | Description |
|---------|-------------|
| `Enable Streaming` | Toggle distance-based streaming (can disable for smaller maps) |
| `Cell Size` | Grid cell dimensions in cm (default: 25600 cm = 256m) |
| `Loading Range` | Radius from streaming source where cells load (default: 768m) |
| `Block on Slow Streaming` | Blocks loading if cells not streaming fast enough |
| `Preview Grids` | Shows grid visualization in viewport |

**Actor Details — World Partition Section:**

| Property | Description |
|----------|-------------|
| `Runtime Grid` | Which partition grid this actor belongs to |
| `Is Spatially Loaded` | ON = distance-streamed; OFF = always loaded (managers, directors) |
| `Data Layers` | Assign to Data Layers for conditional loading |

**Level Conversion Commandlet:**
```powershell
# Convert existing level to World Partition
UnrealEditor.exe YourProject -run=WorldPartitionConvertCommandlet YourMap.umap -AllowCommandletRendering

# Key flags:
-SCCProvider=None                # No source control
-ConversionSuffix                # Appends _WP to filename (keeps original)
-DeleteSourceLevels              # Removes old sub-levels after conversion
-ReportOnly                      # Preview what would be converted (dry run)
-FoliageTypePath=/Game/Foliage   # Extract embedded foliage types
```

**Blueprint — Enable/Disable Streaming Source:**
```
Context: Level Blueprint or Game Mode

// Pre-load teleport destination
[Get All Actors with Component (WPStreamingSource)]
    → [Enable Streaming Source]  → wait
    → [Is Streaming Completed?] → True
        → [Teleport Player]
        → [Disable Streaming Source]  // Unload previous region
```

**Blueprint — Toggle Data Layer:**
```
Context: Game Mode or Level Blueprint

[Get World Partition Subsystem]
    → [Set Data Layer State (Layer: "NightLayer", State: Activated)]
```

### UE Version
UE 5.7 (World Partition introduced UE 5.0; Data Layers stable UE 5.0; One File Per Actor 5.0; HLOD improvements 5.2+)

### Tags
world-partition, large-worlds, streaming, data-layers, hlod, one-file-per-actor, environment, pcg, intermediate, advanced, ue5-7

---

## Related Entries
- `tutorials/procedural-content-generation-framework-in-unreal-engine.md` — PCG integration with World Partition + Hierarchical Generation
- `tutorials/understanding-the-basics-of-unreal-engine.md` — Levels, Worlds, Actor basics
- `tutorials/animating-characters-and-objects-in-unreal-engine.md` — Sequencer with large worlds
