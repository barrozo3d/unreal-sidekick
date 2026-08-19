---
class: topic-reference
verified: no
sources: []
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# Control Rig & Animation — Reference

**Source:** Epic Documentation (`tutorials/control-rig-in-unreal-engine.md` — 93 pages)  
**UE Version:** Available since 4.26; Modular Control Rig production-ready 5.6; Dynamics/Physics in 5.8

---

## What Control Rig Is

Control Rig is UE5's **node-based procedural rigging and animation system**. It runs entirely inside UE — no DCC tool needed for rigging. Primary uses for cinematic work:
- Post-mocap cleanup and correction (additive IK layers on top of captured animation)
- Custom character rigs (non-MetaHuman skeletal meshes)
- Procedural motion (secondary animation, physics-driven cosmetics)
- Facial rigging beyond MetaHuman Animator's output

---

## Control Rig Types

| Type | Use |
|------|-----|
| **Control Rig** | Full custom rig built from scratch; complete procedural control |
| **Modular Control Rig** `[5.6+ prod]` | Drag-and-drop pre-built IK/FK module library; fastest setup |
| **FK Control Rig** | Simple FK-only rig auto-generated from skeleton |
| **Pose Library** | Stored poses recalled in Sequencer or via Blueprint |

---

## Modular Control Rig `[5.6+ production ready]`

### Setup
1. In Content Browser → right-click Skeleton or Skeletal Mesh → `Create Modular Control Rig`
2. **Module Library panel**: drag FK/IK/Spine/Leg/Arm/Head modules onto the character
3. Connect bone targets: each module has **Connectors** (blue pins) — drag to matching bones
4. Modules auto-solve IK/FK, pole vectors, twist correction

### Key modules
| Module | Solves |
|--------|--------|
| `Full Body IK` | Full-body IK with root and limb constraints |
| `Leg (2-Bone IK)` | Foot placement IK |
| `Arm (2-Bone IK)` | Hand/elbow IK |
| `Spine (IK)` | Spine arc / world-space torso control |
| `Head (Look At)` | Eye/head look-at towards target |
| `FK Chain` | FK rotation controls for chains (tail, spine, fingers) |

### `[5.8]` Modular Control Rig improvements
- New hotkeys for hierarchy management
- Mirroring behavior refinements
- Visibility options per module
- Improved connector workflow

---

## Using Control Rig for Mocap Cleanup

### Workflow: additive layer on top of imported mocap
1. Import mocap FBX → IK Retargeter → bake to MetaHuman animation asset
2. In Sequencer → MetaHuman `Animation` track → right-click → `Add Animation Layer`
3. Layer type: **Control Rig** → select your Modular Control Rig
4. **Record mode**: move controls in viewport; corrections bake as additive on top of original mocap
5. Common corrections:
   - Foot sliding: add Leg IK pins to floor plane
   - Elbow pop: adjust pole vector on Arm IK
   - Head wobble: add Look At constraint to stabilize
   - Finger collapse: FK Chain module on fingers → pose adjust

### `[5.5+]` Animation Layers
- Non-destructive additive corrections on Sequencer tracks
- `Right-click Animation track → Add Animation Layer → Control Rig`
- Layer blend modes: Additive, Override, Per-Bone Additive

### `[5.8]` Animation Mixer (Experimental)
- **Layer and mask directly in Sequencer** — no AnimBP needed
- Bone matching + offset root motion between clips
- Transitions between animation clips in-timeline

---

## Control Rig Dynamics `[5.8 — Production Ready]`

Lightweight particle-based solver for **cosmetic secondary motion** (hair, ponytails, earrings, cloth flaps, tails). **5× faster** than previous Chaos-based solutions.

### Setup
1. In Control Rig graph → add `Dynamics Chain` module from Module Library
2. Connect root bone (e.g., `head`) and chain end (e.g., `hair_tip`)
3. Set: **Stiffness**, **Damping**, **Gravity Scale**, **Iterations**
4. Preview: click Play in Control Rig editor

### Key parameters
| Parameter | Effect |
|-----------|--------|
| `Stiffness` | 0 = limp noodle, 1 = rigid |
| `Damping` | Higher = less oscillation |
| `Gravity Scale` | Downward pull strength |
| `Collision Sphere Radius` | Prevent chain intersecting body |

---

## Control Rig Physics (Beta) `[5.8]`

Force-based layered rig — sits on top of existing animation as a runtime layer. More physically accurate than Dynamics for heavier cloth/physics:
- Add `Control Rig Physics` component to MetaHuman Blueprint
- Assign physics modules in `Physics` tab of Modular Control Rig
- Good for: loose garments, heavy capes, physics-driven skirts

---

## Skeletal Editor Blendshape Tools `[5.8]`

For MetaHuman facial rig refinement and custom skeletal meshes:
- **Joint locking**: lock bones during sculpt to prevent accidental transforms
- **Morph target mirroring**: auto-mirror blendshapes (critical for facial symmetry)
- **Lattice deformer**: cage-based broad deformation
- **Mesh element selection**: vertex/edge/face selection modes
- Improved brush behaviors for weight painting and sculpting

---

## Control Rig in Sequencer

### Adding Control Rig track to a character in Sequencer
1. Select MetaHuman/Skeletal Mesh actor in Sequencer
2. `+Track → Animation → Control Rig` (choose your rig asset)
3. Controls appear in Sequencer — keyframe individual controls (sliders, rotators)
4. `Bake to Control Rig`: right-click Animation track → converts animation asset to editable Control Rig keys

### Recording Control Rig performance
1. In Sequencer toolbar → `Record` button
2. Move controls in viewport → keys recorded in real-time
3. Good for: adjusting hand poses frame-by-frame after mocap import

---

## Retargeting Reference `[5.8]`

### IK Retargeter setup
1. Create `IK Rig` for source skeleton (e.g., imported mocap FBX skeleton)
2. Create `IK Rig` for target skeleton (MetaHuman `metahuman_base_skel`)
3. Create `IK Retargeter` asset → set Source + Target IK Rigs
4. Map bone chains in the Retargeter
5. **Bake animation**: right-click animation in retargeter → `Export Retargeted Assets`

### `[5.8]` Foot Definition for Retargeting
- Define foot planes and toe bones explicitly
- Greatly improves ground contact across character size/proportion differences

### `[5.8]` Retarget Override Sets
- Single IK Retargeter handles multiple body type relationships
- Override specific bone mappings per character set without extra assets

---

## Direct Mesh Controls (Experimental) `[5.8]`

- Rig controls rendered **directly on the skeletal mesh surface** in viewport
- Click mesh to select and manipulate controls — no separate control shapes needed
- Useful for facial rig controls on complex facial topology

---

## RigMapper (Beta) `[5.8]`

Improved node graph for **facial animation transfers**:
- Remap facial blend shapes across different character types
- Expanded remap curves stack
- Useful when transferring MetaHuman Animator output to non-MetaHuman facial rigs

---

## Common Gotchas

| Problem | Fix |
|---------|-----|
| Modular Control Rig T-poses in render | Bake animation to new asset before MRQ — Control Rig doesn't evaluate at render-time by default |
| IK feet floating | Add `IK Foot Floor Constraint` node + set floor plane height |
| Dynamics jitter on first frame | Increase `Simulation Warmup Frames` in Dynamics settings |
| Wrong bone scale after mocap retarget | Use `Retarget Override Sets` to adjust per-bone chain length scaling |
| Blend shape names don't match | Use RigMapper to remap facial curve names between rig types |
