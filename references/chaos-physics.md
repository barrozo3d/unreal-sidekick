# Chaos Physics — Reference

Chaos is UE5's physics engine — replaces PhysX. Covers rigid bodies, destruction, cloth, vehicles, fluids, and physics fields.

## Chaos Destruction

### Geometry Collections (Fracture)
```
Workflow:
1. Select Static Mesh Actor in level
2. Fracture Editor (Window > Fracture) → apply fracture patterns
3. Generate Geometry Collection Asset
4. Place in level → set Damage Threshold
5. Anchor Field: use Field System Actor → Anchor Field Cluster to prevent base from falling
```

### Fracture Patterns
| Pattern | Use |
|---------|-----|
| Uniform Voronoi | Random organic fractures |
| Clustered Voronoi | Grouped chunks (better performance) |
| Radial | Impact-style outward fracture |
| Slicing | Clean cuts |
| Planar | Single plane splits |
| Brick | Brick/tile layouts |

### Key Properties
```
Damage Threshold        -- hit force needed to break (lower = easier to destroy)
Cluster Damage Threshold -- separate nested cluster groups
Max Cluster Level       -- how many fracture levels to simulate
Mass                    -- per-chunk mass (auto from mesh volume)
Linear Damping          -- slow down linear velocity
Angular Damping         -- slow down spinning
```

### Anchoring Pieces (keep base attached)
```
// Field System Actor → Anchor Field Cluster
// Or: in Fracture Editor, mark specific pieces as "Never break"
```

---

## Chaos Cloth

### Setup
```
1. Skeletal mesh with cloth painted geometry
2. Clothing Tool (in Persona): paint Max Distance, Backstop, Self Collision
3. Cloth Asset assigned to Skeletal Mesh component
4. Chaos Cloth Config: Air Damping, Gravity Scale, Stiffness, Drag
```

### Key Cloth Properties
| Property | Effect |
|----------|--------|
| `Max Distance` | How far cloth can move from animated pose (0 = rigid) |
| `Backstop` | Prevents cloth penetrating body |
| `Wind` | PhysicsVolume → Wind direction and speed |
| `Damping` | Velocity damping per-frame |
| `Stiffness (Stretch)` | Resistance to stretching |
| `Stiffness (Bend)` | Resistance to bending |
| `Self Collision Thickness` | Prevents self-intersection |

### ML Cloth (UE 5.3+)
- Offline-trained cloth simulation at near-Chaos quality but real-time cost
- Requires training data capture from full Chaos simulation
- Use: hero character cloth that runs on consoles

---

## Rigid Body Dynamics

### Physics Asset (Skeletal Mesh Physics)
```
// Per-bone collision bodies + constraints
Physics Asset Editor:
- Add bodies to bones (capsule/box/sphere/convex)
- Add constraints between adjacent bodies
- Simulate in editor for preview
```

### Key Body Settings
| Setting | Notes |
|---------|-------|
| `Linear Damping` | 0 = no resistance; 0.01–0.1 typical |
| `Angular Damping` | 0 = spins forever; 0.01–0.05 typical |
| `Enable Gravity` | Off for floating/floating FX |
| `Collision Response` | Block/Overlap/Ignore per channel |
| `Mass (kg)` | Auto from volume; or set manually |
| `Linear/Angular Velocity Constraints` | Lock specific axes |
| `COM Offset` | Move center of mass for stability |

### Constraints (Joint Types)
| Type | Locked Axes |
|------|------------|
| Fixed | All — rigid weld |
| Hinge | 1 rotation axis free |
| Prismatic | 1 translation axis free |
| Ball & Socket | 2 rotation axes free |
| Free | All free (cloth-like) |

---

## Chaos Vehicles

### Setup
```
1. Create Vehicle Blueprint (parent: WheeledVehiclePawn or ChaosVehiclePawn)
2. Assign Physics Asset with collision bodies
3. Add Chaos Vehicle Movement Component
4. Configure: Max Speed, Torque Curve, Differential, Suspension
5. Add wheel blueprints (ChaosVehicleWheel) per axle
```

### Key Vehicle CVars for Debug
```
p.Vehicle.ShowDebug 1         -- show vehicle debug overlay
p.Chaos.Vehicle.EnableSleeping 0  -- prevent sleeping on slopes
```

---

## Physics Fields

Force and strain fields that affect Geometry Collections and rigid bodies.

| Field Type | Effect |
|------------|--------|
| **Radial Vector Field** | Force radiating outward from a point (explosion impulse) |
| **Uniform Vector Field** | Constant force in one direction (wind) |
| **Drag Field** | Damping force (slow down pieces) |
| **Anchor Field Cluster** | Lock selected Geometry Collection clusters in place |
| **Strain Field** | Apply damage/breaking strain to Geometry Collections |
| **Sleep Field** | Put sleeping physics bodies to rest |

```
// Blueprint: spawn radial explosion at impact point
[Spawn Actor from Class → AFieldSystemActor]
→ Set Field System [Radial Vector Field, Magnitude: 50000, Falloff: 5m]
→ Apply Field (Target: GeometryCollectionComponent)
→ Destroy Actor after 0.1s
```

---

## Networked Physics (UE 5.x)

| Mode | Description |
|------|-------------|
| **Resimulation** | Authority reruns simulation on desync; clients follow |
| **Interpolation** | Smooth client-side display of authority state |
| **Prediction** | Client predicts, reconciles with authority state |

- Enable: Physics Settings → Network Physics Prediction → Enable
- Use for: vehicles, interactive physics objects, destructibles

---

## Chaos Visual Debugger (CVD)

Tool for offline capture and replay of physics simulation.

```
Enable capture:
p.Chaos.Solver.DebugDraw 1
p.Chaos.Solver.CaptureCSV 1

Open CVD: Window → Developer Tools → Chaos Visual Debugger
```

---

## Physics Performance Tips

- **Sleep Threshold**: set `Linear Sleep Threshold` + `Angular Sleep Threshold` to put inactive bodies to sleep
- **Field System**: destroy Field System actors immediately after applying — they update every tick
- **Geometry Collections**: limit `Max Cluster Level` to 1-2 for realtime; 3+ for cinematics
- **Chaos Cloth**: disable `Self Collision` for distant/background characters
- **Physics Substeps**: lower substep count for performance; higher for accuracy
  ```
  p.chaos.solver.substeps 4   // default 4; increase to 8-16 for complex constraints
  ```
