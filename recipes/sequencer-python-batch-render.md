# Recipe: Sequencer Python Batch Render

**Goal:** Use Unreal Python to batch-render multiple Level Sequences (or multiple shots in one sequence) via the Movie Render Queue, without opening the UI manually.  
**UE Systems:** unreal Python API, Movie Render Queue, Sequencer, MRQ  
**Difficulty:** Advanced

---

## Overview

This recipe provides a ready-to-use Python script that:
1. Discovers all Level Sequences in a given Content Browser path
2. Creates an MRQ job for each sequence with a reusable preset
3. Renders all jobs sequentially
4. Prints a summary

Run it from: `Tools → Execute Python Script` or from the Python console.

---

## Prerequisites

- Python Editor Script Plugin enabled
- Movie Render Queue plugin enabled
- A saved MRQ Preset asset in your Content Browser (or use the default settings inline)

---

## Script 1 — Batch Render All Sequences in a Folder

```python
"""
batch_render.py
Renders all Level Sequences in /Game/Cinematics/ with the saved MRQ preset.
Run via: Tools → Execute Python Script
"""
import unreal

# ─── Configuration ──────────────────────────────────────────────────────────────
SEQUENCES_PATH   = "/Game/Cinematics"       # Content Browser path to search
OUTPUT_DIR       = "D:/Renders/{sequence}"  # {sequence} replaced at runtime
PRESET_PATH      = "/Game/MRQ/MainPreset"   # Optional saved preset asset path
                                            # Set to None to use default settings

# ─── Discover sequences ─────────────────────────────────────────────────────────
asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
assets = asset_registry.get_assets_by_path(SEQUENCES_PATH, recursive=True)

sequences = [
    a for a in assets
    if a.asset_class_path.asset_name == "LevelSequence"
]

if not sequences:
    unreal.log_error(f"No Level Sequences found in {SEQUENCES_PATH}")
    raise SystemExit

unreal.log(f"Found {len(sequences)} sequences to render.")

# ─── Set up MRQ ─────────────────────────────────────────────────────────────────
subsystem = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)
queue     = subsystem.get_queue()
queue.delete_all_jobs()

executor  = unreal.MoviePipelinePIEExecutor()

for asset_data in sequences:
    seq_asset = unreal.load_asset(str(asset_data.object_path))
    seq_name  = asset_data.asset_name

    job = queue.allocate_new_job(unreal.MoviePipelineExecutorJob)
    job.sequence = unreal.SoftObjectPath(str(asset_data.object_path))
    job.map = unreal.EditorLevelLibrary.get_editor_world().get_path_name()
    job.job_name = str(seq_name)

    # ── Load preset or configure inline ─────────────────────────────────────────
    if PRESET_PATH:
        preset = unreal.load_asset(PRESET_PATH)
        if preset:
            job.set_preset_origin(preset)
        else:
            unreal.log_warning(f"Preset not found at {PRESET_PATH}, using defaults.")
    else:
        # Inline settings — configure programmatically
        config = job.get_configuration()
        _configure_job(config, seq_name)

    unreal.log(f"Queued: {seq_name}")

# ─── Render ─────────────────────────────────────────────────────────────────────
def on_executor_finished(executor, success):
    unreal.log(f"Batch render {'succeeded' if success else 'FAILED'}.")

executor.on_executor_finished_delegate.add_callable(on_executor_finished)
subsystem.render_queue_with_executor_instance(executor)
unreal.log("Batch render started.")


def _configure_job(config, seq_name):
    """Configure job settings inline (used when no preset is set)."""
    # Output settings
    output = config.find_or_add_setting_by_class(unreal.MoviePipelineOutputSetting)
    output.output_directory    = unreal.DirectoryPath(
        OUTPUT_DIR.replace("{sequence}", seq_name)
    )
    output.file_name_format    = "{sequence_name}_{frame_number}"
    output.output_resolution   = unreal.IntPoint(1920, 1080)
    output.override_existing_output = True
    output.flush_disk_writes_per_shot = True

    # Anti-aliasing
    aa = config.find_or_add_setting_by_class(unreal.MoviePipelineAntiAliasingSetting)
    aa.temporal_sample_count = 8
    aa.spatial_sample_count  = 1
    aa.render_warm_up_count  = 32
    aa.use_camera_cut_for_warm_up = True

    # EXR output
    exr = config.find_or_add_setting_by_class(unreal.MoviePipelineImageSequenceOutput_EXR)
    exr.compression = unreal.EXRCompressionFormat.ZIP
    exr.multilayer  = True

    # Deferred pass
    config.find_or_add_setting_by_class(unreal.MoviePipelineDeferredPassBase)
```

---

## Script 2 — Render Specific Named Shots

For a single Level Sequence with multiple camera cuts (shots):

```python
"""
render_shots.py
Renders specific shot names from a single master sequence.
"""
import unreal

MASTER_SEQUENCE_PATH = "/Game/Cinematics/Master_Sequence"
SHOTS_TO_RENDER      = ["Shot_010", "Shot_030", "Shot_060"]  # empty list = all shots
OUTPUT_DIR           = "D:/Renders/Master_Sequence"

subsystem = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)
queue     = subsystem.get_queue()
queue.delete_all_jobs()

seq = unreal.load_asset(MASTER_SEQUENCE_PATH)

job = queue.allocate_new_job(unreal.MoviePipelineExecutorJob)
job.sequence = unreal.SoftObjectPath(MASTER_SEQUENCE_PATH)
job.map      = unreal.EditorLevelLibrary.get_editor_world().get_path_name()

# Disable shots not in the target list
if SHOTS_TO_RENDER:
    for shot in job.shot_info:
        shot.enabled = (shot.outer_name in SHOTS_TO_RENDER)
        status = "ON " if shot.enabled else "OFF"
        unreal.log(f"  [{status}] {shot.outer_name}")

# Inline config
config = job.get_configuration()
output = config.find_or_add_setting_by_class(unreal.MoviePipelineOutputSetting)
output.output_directory = unreal.DirectoryPath(OUTPUT_DIR)
output.file_name_format = "{sequence_name}_{shot_name}_{frame_number}"

executor = unreal.MoviePipelinePIEExecutor()
subsystem.render_queue_with_executor_instance(executor)
unreal.log(f"Rendering {len(SHOTS_TO_RENDER) or 'all'} shots...")
```

---

## Script 3 — Change Output Settings Across All Queued Jobs

Useful for changing output directory or resolution on already-configured jobs:

```python
"""
update_queue_output.py
Updates output path on all queued MRQ jobs without re-creating them.
"""
import unreal

NEW_OUTPUT = "D:/Renders/v002"
NEW_RES    = unreal.IntPoint(3840, 2160)  # 4K

subsystem = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)
queue     = subsystem.get_queue()

for job in queue.get_jobs():
    config = job.get_configuration()
    output = config.find_or_add_setting_by_class(unreal.MoviePipelineOutputSetting)
    output.output_directory  = unreal.DirectoryPath(f"{NEW_OUTPUT}/{job.job_name}")
    output.output_resolution = NEW_RES
    unreal.log(f"Updated: {job.job_name} → {output.output_directory.path}")

unreal.log("All jobs updated.")
```

---

## Useful MRQ Python Classes

| Class | Purpose |
|-------|---------|
| `MoviePipelineQueueSubsystem` | Main entry point — get queue, render |
| `MoviePipelineExecutorJob` | Represents one render job |
| `MoviePipelinePIEExecutor` | Renders in the current editor session |
| `MoviePipelineNewProcessExecutor` | Renders in a separate UE process (headless) |
| `MoviePipelineOutputSetting` | Output path, resolution, frame range |
| `MoviePipelineAntiAliasingSetting` | Temporal/spatial samples, warm-up |
| `MoviePipelineImageSequenceOutput_EXR` | EXR output (multilayer, compression) |
| `MoviePipelineDeferredPassBase` | Standard deferred rendering pass |
| `MoviePipelinePathTracerPass` | Path Tracer pass |
| `MoviePipelineConsoleVariableSetting` | Console variable overrides per job |

---

## Gotchas

| Problem | Fix |
|---------|-----|
| `render_queue_with_executor_instance` returns immediately | Attach to `on_executor_finished_delegate` for callback |
| Sequence not found | Use `/Game/` prefix, not filesystem path |
| Jobs render with wrong world | Set `job.map` to the correct level path |
| Output overwrites previous renders | Disable `override_existing_output` or version the output dir |
| Render hangs at frame 1 | Low warm-up count; set `render_warm_up_count = 64` |

---

## References
- `references/sequencer-cinematics.md` — MRQ settings, Sequencer workflow
- `references/python-unreal.md` — unreal Python API patterns, module setup
- `recipes/mrq-multipass-exr.md` — Multi-pass EXR render pass configuration
