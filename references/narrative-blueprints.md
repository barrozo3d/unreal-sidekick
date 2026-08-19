---
class: topic-reference
verified: no
sources: []
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# Narrative Blueprints & Level Streaming — Reference

**Source:** Epic Documentation (`tutorials/level-streaming-in-unreal-engine.md` — 15 pages) + synthesis  
**UE Version:** Level Streaming since UE4; World Partition streaming since 5.0; Event tracks in Sequencer since 5.0

---

## Level Streaming for Scene Transitions

Level Streaming lets you **async-load and unload sub-levels** at runtime — essential for multi-scene narrative projects to manage memory and enable seamless scene transitions.

### Two approaches

| Approach | When to use |
|----------|-------------|
| **Sub-Level Streaming** (classic) | Explicit load/unload from Blueprint; tight memory control |
| **World Partition** | Open-world; cells auto-load based on camera proximity |

For cinematics: **Sub-Level Streaming** gives you full control over when scenes appear.

---

## Sub-Level Streaming Setup

### Creating streaming levels
1. `Window → Levels` panel → `+` → `Create New Streaming Level`
2. Give it a meaningful name (`L_Scene_01_Prison`, `L_Scene_02_Arena`, etc.)
3. Move actors that belong to that scene into its level: right-click actor → `Move to Level`
4. Default streaming method: `Blueprint` (manual control) vs `Always Loaded` vs `Distance-Based`

### Loading/Unloading from Blueprint (Level Blueprint or Actor Blueprint)

```
// Load a level async (non-blocking)
Load Stream Level (LevelName: "L_Scene_02_Arena", MakeVisibleAfterLoad: true, ShouldBlockOnLoad: false)
  → On Success → [fire cutscene trigger]

// Unload when done
Unload Stream Level (LevelName: "L_Scene_01_Prison")
```

**Key nodes:**
| Node | Description |
|------|-------------|
| `Load Stream Level` | Async loads a streaming level |
| `Unload Stream Level` | Unloads and removes from memory |
| `Get Streaming Level` | Returns a `LevelStreaming` object reference |
| `Is Level Loaded` | Check load state before triggering |
| `Get Level Streaming State` | Returns: Unloaded / Loading / Loaded / MakingVisible / Visible / MakingInvisible |
| `Set Level Visibility` | Toggle visibility without unloading |

### Sequencer Level Visibility track
In Sequencer:
1. `+Track → Level Visibility`
2. Click `+Level` → select streaming levels to control
3. Keyframe `Visible` / `Hidden` states per frame
4. Combine with `Load Stream Level` call on a Sequencer Event track

---

## Triggering Cinematics from Blueprint Events

### Method 1 — Sequencer Event Track (most common for narrative)
1. In Sequencer → `+Track → Event`
2. Right-click timeline → add event at desired frame
3. In event properties: bind to a **Level Blueprint function** or **Actor Blueprint function**
4. The function runs when Sequencer playhead reaches that frame

```
// Level Blueprint function bound to Sequencer Event:
Function: OnExplosionFrame()
  → Spawn Emitter at Location (ParticleSystem: NS_BigExplosion, Location: ExplosionActor.Location)
  → Play Sound at Location (Sound: SFX_Explosion)
  → Shake Camera (ShakeClass: CameraShake_Explosion)
```

### Method 2 — Blueprint trigger volumes (for interactive narrative)
```
Box Trigger Volume → On Actor Begin Overlap
  → [Is it the player?] Branch
  → True → Get Sequence Player → Play (SequenceAsset: LS_CutsceneA)
```

### Method 3 — Level Sequence Player component on Actor
1. Add `Level Sequence Player` component to any Blueprint Actor
2. Assign Level Sequence asset
3. Call `Play`, `Pause`, `Stop` from Blueprint events
4. Great for: TV screens, projectors, triggered flashbacks

---

## Master Sequences for Multi-Scene Films

For a film with multiple shots/scenes:

### Structure
```
L_Master_Sequence.uasset  (Master Level Sequence)
  ├── Shot_01_Intro          (sub-sequence, references L_Scene_Prison streaming level)
  ├── Shot_02_Escape         (sub-sequence)
  ├── Shot_03_Arena_Arrival  (sub-sequence)
  └── Shot_04_Battle         (sub-sequence)
```

### Creating master sequences
1. `Content Browser → right-click → Cinematics → Master Level Sequence`
2. Add sub-sequences: `+Track → Subsequence Track` → drag Level Sequence assets in
3. Each sub-sequence can have its own cameras, MetaHumans, events
4. Master sequence controls playback order and shot timing

### Camera cuts across sub-sequences
- Master Sequence has a **Director Track (Camera Cuts)**
- Add camera cut keys that reference cameras from each sub-sequence
- The master director track overrides individual shot cameras

---

## World Partition Streaming `[5.0+]`

For open-world narrative or large outdoor environments:
- Enable: `World Settings → World Partition → Enable Streaming`
- Actors are grouped into **cells** (configurable grid size, default 128m)
- Cells load/unload automatically based on streaming sources (player camera, etc.)
- Add `World Partition Streaming Source` component to your Cine Camera for correct streaming in cinematics

**Gotcha:** World Partition cells don't respect your Sequencer camera position by default — add `World Partition Streaming Source` component to your cinematic camera actor, or the level may not load the correct cells during render.

---

## Blueprint-Driven Dialogue Systems

For basic in-engine dialogue without a plugin:

### Simple dialogue trigger pattern
```
// In-world NPC Actor Blueprint:

// 1. Overlap trigger
On Actor Begin Overlap (Player)
  → Branch: bHasBeenTriggered? → False
  → Set bHasBeenTriggered = True
  → Get Level Sequence Player → Play (DialogueSequence_01)
  → [Dialogue sequence plays — camera cuts, MetaHuman face anim, subtitle track]

// 2. In Sequencer: Event Track at end of dialogue
Event: OnDialogueComplete
  → Level BP: Show next objective / unlock door / spawn next trigger
```

### Dialogue Sequencer tracks
| Track | Content |
|-------|---------|
| Camera Cut track | Cut to face cam for speaker |
| MetaHuman Animation track | Body + face anim from mocap/MetaHuman Animator |
| Audio track | 11 Labs voice audio file |
| Event track | Trigger next dialogue, update quest state |
| Subtitle track `[5.8]` | On-screen subtitles synced to audio |

---

## Timeline Actors for Environmental Storytelling

Blueprint `Timeline` node for looping or triggered environmental animation:

```
Event BeginPlay
  → Play from Start (Timeline: DoorOpenTimeline)
  → Timeline Alpha output (0→1 over 2s)
  → Lerp (A: ClosedRotation, B: OpenRotation, Alpha: TimelineAlpha)
  → Set Relative Rotation (DoorMesh)
```

Common uses:
- Doors, drawbridges, gates triggered by Sequencer events
- Flickering lights (keyframe light intensity on Timeline)
- Camera shake ramp-up (animate `ShakeScale` on CameraShakeModifier)

---

## Level Blueprint vs Actor Blueprint for Narrative

| Use case | Where |
|----------|-------|
| Scene-global events (loading next level, ambient music) | Level Blueprint |
| Character-specific triggers (NPC dialogue, patrol start) | Actor Blueprint |
| Sequencer-bound events | Level Blueprint (Sequencer Event tracks bind to Level BP functions) |
| Reusable trigger volumes | Blueprint Actor class |

---

## Common Gotchas

| Problem | Fix |
|---------|-----|
| Streaming level loads but nothing appears | `MakeVisibleAfterLoad: true` on `Load Stream Level` node |
| Sub-sequence actors T-pose at start | Check `Evaluation Type: Always Re-evaluate` on animation tracks |
| Sequencer Event not firing | Ensure `Event Track` binding is set to a valid Level Blueprint function |
| Camera cut plays wrong camera | Verify Director Track camera references match the sub-sequence's cameras |
| World Partition cells not loading for cinematic camera | Add `World Partition Streaming Source` component to Cine Camera Actor |
| Dialogue audio and face anim out of sync | Ensure both audio file and MetaHuman Animator output are at 24/30fps matching sequence fps |
