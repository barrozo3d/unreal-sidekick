---
class: topic-reference
verified: no
sources: []
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# Blueprints Scripting — Reference

## Blueprint Types

| Type | Use |
|------|-----|
| **Actor Blueprint** | Placeable in level — has Transform, Components |
| **Blueprint Interface** | Define function signatures — implement in any BP |
| **Blueprint Function Library** | Static utility functions — callable anywhere |
| **Blueprint Macro Library** | Reusable graph segments |
| **Anim Blueprint** | Animation logic for Skeletal Meshes |
| **Widget Blueprint** | UMG UI elements |

## Event Graph — Common Events

```
Event BeginPlay       -- fires when actor spawns / level starts
Event Tick            -- fires every frame (Delta Seconds available)
Event EndPlay         -- fires when actor is destroyed / level ends
Event Hit             -- physics collision
Event ActorBeginOverlap / EndOverlap -- trigger volumes
Custom Event          -- user-defined, can be called by name or dispatched
```

## Key Node Categories for VFX/Cinematics

### Spawning
```
Spawn Actor from Class     -- spawn any actor at runtime
Spawn Emitter at Location  -- spawn Niagara system (legacy: cascade)
Spawn System at Location   -- spawn Niagara system (UE5)
Spawn System Attached      -- attach Niagara system to a component
```

### Timeline
```
Timeline           -- keyframeable curves in Blueprint (float, vector, color, event)
                      use for: animated parameter changes, timed events
Play / Play from Start / Reverse / Stop
Bind event to Timeline's Update pin for per-frame callbacks
```

### Sequencer Control
```
Get Sequence Player          -- get active Sequence Player component
Play / Stop / Pause          -- control playback
Set Playback Position        -- jump to specific time
Get Current Time             -- read current playhead position
Get Bound Objects            -- get actors bound to a Sequencer track
```

### Material Control
```
Create Dynamic Material Instance     -- make a runtime-editable material copy
Set Scalar Parameter Value           -- set float parameter
Set Vector Parameter Value           -- set color/vector parameter
Set Texture Parameter Value          -- swap texture at runtime
```

### Niagara Control
```
Get Niagara Component            -- get the Niagara System on this actor
Activate / Deactivate            -- start/stop emitter
Set Niagara Variable (float/vector/bool/int)  -- set exposed Niagara parameters
Reset System                     -- restart the simulation
```

## Common Patterns for VFX Cinematics

### Trigger effect on overlap
```
Event ActorBeginOverlap
→ Spawn System at Location (Niagara asset, Get Actor Location)
→ Play Sound at Location
```

### Animate material over time using Timeline
```
Event BeginPlay
→ Create Dynamic Material Instance (material slot 0)
→ Timeline [0-1 float curve over 2s]
  Update: Set Scalar Parameter Value (DynMat, "Opacity", Timeline output)
  Finished: (optional cleanup)
```

### Camera shake on event
```
Custom Event "OnImpact"
→ Get Player Camera Manager
→ Start Camera Shake (shake class, scale)
```

### Parameter-driven VFX from Sequencer
```
// In Sequencer: add Event Track → key an event → assign Custom Event
// In Blueprint: implement the Custom Event name:
Custom Event "TriggerExplosion"
→ Spawn System at Location
```

## Blueprint Types (Complete)

| Type | Location | Use |
|------|----------|-----|
| **Level Blueprint** | Per-level, Editor-only | Level-specific events; trigger streaming, fire Sequencer events |
| **Actor Blueprint** | Content Browser | Placeable actor with components and logic |
| **Widget Blueprint** | Content Browser | UMG UI elements |
| **Anim Blueprint** | Content Browser | Animation state machines, blend graphs |
| **Blueprint Interface** | Content Browser | Define shared function signatures — implement in multiple classes |
| **Blueprint Function Library** | Content Browser | Static utility functions; no state; callable anywhere |
| **Blueprint Macro Library** | Content Browser | Reusable collapsed graph segments |
| **Data Asset** | Content Browser | Pure data storage; no logic; use for config/tables |
| **Game Mode Blueprint** | Content Browser | Rules of the game; sets pawn class, HUD, controller |
| **Player Controller** | Content Browser | Player input handling; cross-level persistence |
| **Game Instance** | Content Browser | Persists across level loads; global game state |

## Actor Communication Patterns

### Pattern 1: Direct Reference (tightest coupling)
```
// Use when: both actors are known, same level
[Get All Actors of Class (TargetActor)]
    → Pin to variable → call function directly
// Or: expose a public variable, drag actor reference from level into BP
```

### Pattern 2: Cast To (common, requires class knowledge)
```
// Use when: you have an actor reference but need the specific class
[Get Player Pawn] → [Cast To MyCharacterBP]
    → Success: call MyCharacterBP functions
    → Fail: (handle missing actor)
```

### Pattern 3: Blueprint Interface (loose coupling, best for VFX triggers)
```
// Create: Content Browser → Blueprint Interface (BPI_Triggerable)
// Add function: Trigger(Effect: NiagaraSystem)
// Implement in any actor class that should receive it
// Call from anyone:
[Get Overlapping Actors]
    → For Each Loop
        → [Does Implement Interface? BPI_Triggerable]
            → [Call Interface Message: Trigger]
```

### Pattern 4: Event Dispatcher (one-to-many broadcast)
```
// In source Blueprint: create Event Dispatcher "OnExplode"
// In receiver Blueprint:
[Get Reference to Source]
    → [Bind Event to OnExplode] → [Custom Event: HandleExplosion]
// Trigger broadcast (in source):
[Call OnExplode]  // all bound receivers fire
```

### Pattern 5: Game State / Game Instance (global data)
```
// Read global data from anywhere:
[Get Game State] → [Cast To MyGameState]
    → access replicated properties (score, phase, wave)
// Persist across levels:
[Get Game Instance] → [Cast To MyGameInstance]
    → access persistent save data
```

## Variable Types Reference

| Type | Notes |
|------|-------|
| `Boolean` | True/False |
| `Integer` | 32-bit int |
| `Integer64` | 64-bit int |
| `Float` | 32-bit float |
| `Double` | 64-bit float (default in UE5) |
| `String` | UTF-16 text |
| `Name` | Hashed identifier (fast comparison) |
| `Text` | Localizable text |
| `Vector` | 3D float vector |
| `Rotator` | Pitch/Yaw/Roll |
| `Transform` | Location + Rotation + Scale |
| `Color` | RGBA 8-bit |
| `Linear Color` | RGBA 32-bit float |
| `Object Reference` | Pointer to any UObject |
| `Class Reference` | Reference to a class type (for spawning) |
| `Soft Object Reference` | Async-loadable object ref |
| `Interface` | Reference typed to an interface |
| `Enum` | Named integer values |
| `Struct` | Group of variables |
| `Array` | Dynamic list |
| `Map` | Key-value store |
| `Set` | Unique-value collection |

## Performance Notes
- **Avoid Tick** when possible — use Timers (`Set Timer by Event`) or event-driven
- **Use interfaces** for actor communication — avoids hard casting
- **Compile regularly** — BP compiler catches most errors
- For heavy logic: move to C++ function library, call from BP
- **Blueprint nativization** (deprecated UE5) → prefer C++ for hot paths
- `Is Valid` check before using any actor reference — levels can change
- Use `Async` nodes (Load Asset Async, Delay) to avoid hitching on expensive ops
