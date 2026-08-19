---
class: topic-reference
verified: no
sources: []
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# Python in Unreal Engine — Reference

## Setup

Enable the Python Editor Script Plugin:
```
Edit > Plugins > Search "Python Editor Script Plugin" > Enable > Restart
```

Script locations:
- **Interactive console**: Output Log → Python prompt (bottom)
- **Execute script**: Tools > Execute Python Script
- **Startup scripts**: Project Settings > Python > Startup Scripts
- **Editor Utility Widgets**: Blueprint with Python nodes

## Core Module

```python
import unreal

# Get the editor subsystems
editor_util = unreal.EditorUtilityLibrary()
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
asset_reg   = unreal.AssetRegistryHelpers.get_asset_registry()
editor_lvl  = unreal.EditorLevelLibrary()
```

## Common Operations

### Browse/Load Assets
```python
# Find all assets of a type in a folder
assets = unreal.AssetRegistryHelpers.get_asset_registry().get_assets_by_path(
    '/Game/VFX', recursive=True
)

# Load an asset by path
niagara_sys = unreal.load_asset('/Game/VFX/NS_Fire')

# Get selected assets in Content Browser
selected = unreal.EditorUtilityLibrary.get_selected_assets()
```

### Actor Operations
```python
# Get all actors in level of a specific class
actors = unreal.EditorLevelLibrary.get_all_level_actors()
niagara_actors = [a for a in actors if isinstance(a, unreal.NiagaraActor)]

# Spawn an actor
loc   = unreal.Vector(0, 0, 100)
rot   = unreal.Rotator(0, 0, 0)
actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.NiagaraActor, loc, rot
)

# Set actor transform
actor.set_actor_location(unreal.Vector(100, 200, 0), False, False)
actor.set_actor_rotation(unreal.Rotator(0, 45, 0), False)
```

### Asset Creation
```python
# Create a new asset
factory  = unreal.MaterialFactoryNew()
new_mat  = asset_tools.create_asset('M_NewMaterial', '/Game/Materials', 
                                     unreal.Material, factory)

# Save assets
unreal.EditorAssetLibrary.save_asset('/Game/Materials/M_NewMaterial')

# Duplicate an asset
unreal.EditorAssetLibrary.duplicate_asset(
    '/Game/VFX/NS_Original', '/Game/VFX/NS_Copy'
)
```

### Sequencer
```python
# Get the active Level Sequence
seq_world = unreal.LevelSequenceEditorBlueprintLibrary

# Get all sequence actors in level
seq_actors = [a for a in unreal.EditorLevelLibrary.get_all_level_actors()
              if isinstance(a, unreal.LevelSequenceActor)]

# Play/Stop sequence
for actor in seq_actors:
    player = actor.get_sequence_player()
    player.play()
```

### Material Parameter Automation
```python
# Set scalar parameter on a material instance
mat_inst = unreal.load_asset('/Game/Materials/MI_Fire')
mat_inst.set_scalar_parameter_value('Intensity', 3.0)
mat_inst.set_vector_parameter_value('Color', unreal.LinearColor(1, 0.5, 0, 1))

# Save after changes
unreal.EditorAssetLibrary.save_asset('/Game/Materials/MI_Fire')
```

### Batch Operations
```python
# Batch rename assets
assets = unreal.EditorUtilityLibrary.get_selected_assets()
for asset in assets:
    old_name = asset.get_name()
    new_name = old_name.replace('Old_', 'New_')
    unreal.EditorAssetLibrary.rename_asset(
        asset.get_path_name(),
        f'/Game/Renamed/{new_name}'
    )
```

### Progress Bar for Long Operations
```python
with unreal.ScopedSlowTask(len(items), "Processing...") as task:
    task.make_dialog(True)  # True = can cancel
    for item in items:
        if task.should_cancel():
            break
        task.enter_progress_frame(1, f"Processing {item}")
        # ... do work ...
```

## Useful Utilities

```python
# Print to Output Log
unreal.log("Hello from Python")
unreal.log_warning("Something might be wrong")
unreal.log_error("Something went wrong")

# Run deferred (next frame)
unreal.EditorAssetLibrary.sync_browser_to_objects([asset])

# Get project directory
import os
project_dir = unreal.Paths.project_dir()
content_dir = unreal.Paths.project_content_dir()
```

## Running Scripts

```bash
# From command line (useful for CI/automation):
UnrealEditor.exe [ProjectPath] -run=pythonscript -script=[ScriptPath]

# Or from the editor Output Log:
# py [script_path_relative_to_project]
```
