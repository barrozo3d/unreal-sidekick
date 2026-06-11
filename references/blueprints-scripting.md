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

## Performance Notes
- **Avoid Tick** when possible — use Timers (`Set Timer by Event`) or event-driven
- **Use interfaces** for actor communication — avoids hard casting
- **Compile regularly** — BP compiler catches most errors
- For heavy logic: move to C++ function library, call from BP
