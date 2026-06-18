"""
Batch extraction for 26 new tutorials (Arthur Tasquin + Official UE channel).
Writes Structured Notes and updates extraction_status to complete.
"""
import re, os

def update_file(path, frontmatter_updates, structured_notes, related_entries):
    with open(path, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    # Update frontmatter fields
    for key, value in frontmatter_updates.items():
        content = re.sub(
            rf'^{key}: .+$',
            f'{key}: {value}',
            content,
            flags=re.MULTILINE
        )

    # Replace structured notes block
    new_notes = f"""### Core Technique
{structured_notes["core"]}

### Summary
{structured_notes["summary"]}

### Key Steps
{structured_notes["steps"]}

### UE Systems / Blueprints / Settings
{structured_notes["systems"]}

### Difficulty
{structured_notes["difficulty"]}

### UE Version
{structured_notes["version"]}

### Tags
{structured_notes["tags"]}

---

## Related Entries
{related_entries}"""

    content = re.sub(
        r'### Core Technique\n.*?## Related Entries\n.*',
        new_notes,
        content,
        flags=re.DOTALL
    )

    with open(path, 'w', encoding='utf-8-sig', newline='\r\n') as f:
        f.write(content)
    print(f"  Done: {os.path.basename(path)}")


EXTRACTIONS = {

"tutorials/realistic-and-physical-lighting-in-ue5-what-is-pbl.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["lighting", "rendering", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Physically-Based Lighting (PBL) theory for digital artists — understanding the 4 essential lighting units (Candela, Lumen, Lux, cd/m²) and building a real-world reference database for accurate UE5 light values.",
        "summary": "Arthur Tasquin, a real-time artist from the VFX industry, introduces PBL: using real-world light intensities in CG lighting for consistency and coherence. Covers the 4 lighting units mapped to UE light types, how to sample data with a light meter, multi-scenario projects using Sub-Levels + Level Sequences, and his PBL Database FAB plugin. Part 1 of 2.",
        "steps": """1. Learn the 4 PBL units: **Candela** (light source intensity → Point/Spot lights), **Lumen** (total light output → area lights), **Lux** (illuminance on a surface → Sun/Sky), **cd/m²** (luminance → displays/emissive)
2. Use an incident light meter (Lux meter) to sample real-world illuminance values; point at subject, read value
3. Build a reference database of light scenarios (indoor, outdoor, artificial, natural) sorted by unit, location, category
4. Install the **PBL Database** plugin (FAB) for in-editor access to sampled reference values with tag-based filtering
5. Set up **Sub-Levels** (Window > Levels) for each lighting scenario to isolate lighting assets
6. Create dedicated **Level Sequences** per scenario to contain all animated lighting properties
7. Match UE camera **Exposure Compensation** to real-world EV values for consistent renders""",
        "systems": """`Point Light` → Intensity in Candela
`Rect Light` / `Area Light` → Intensity in Lumen
`Directional Light` → Lux (illuminance)
`Emissive Materials` → Nits (cd/m²)
`Sub-levels` (Window > Levels) → lighting scenario isolation
`Level Sequence` → per-scenario lighting animation container
PBL Database plugin (FAB) → real-world reference values with tag filter""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "lighting, rendering, intermediate",
    },
    "related": "- `references/rendering-pipeline.md` — Lumen, exposure, camera settings\n- `tutorials/realistic-and-physical-lighting-in-ue5-the-pbl-workflow.md` — Part 2: practical application\n- `references/sequencer-cinematics.md` — Level Sequences for scenario management",
},

"tutorials/realistic-and-physical-lighting-in-ue5-the-pbl-workflow.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["lighting", "rendering", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Applying Physically-Based Lighting in UE5 practice — using PBL Database plugin values in real lighting scenarios, cinematic exposure workflow, and where PBL succeeds vs. falls short.",
        "summary": "Part 2 of Arthur Tasquin's PBL series. Translates theory into a working UE5 lighting workflow: pulling real-world values from the PBL Database plugin, applying them to different scenario types (interior, exterior, artificial, natural), setting camera exposure via EV values, and identifying where strict PBL values must be overridden for cinematic goals.",
        "steps": """1. Open the **PBL Database** plugin panel; select matching scenario tags (interior, natural, evening, etc.)
2. Read the recommended Lux/Lumen/Candela values for the scenario and enter them into the corresponding UE light
3. Set `Directional Light` intensity using Lux values (real overcast ≈ 10,000 lx; golden hour ≈ 30,000 lx)
4. Set camera `Exposure → Manual` mode, target EV matching real-world scenario (indoor ≈ EV 8–10)
5. Iterate: compare render to reference photograph; adjust only exposure compensation, not light values, first
6. Where PBL falls short (e.g. deep interiors with no bounce), intentionally deviate — document the deviation
7. Use Sub-Level workflow from Part 1 to switch between scenario presets for lighting studies""",
        "systems": """`PBL Database Plugin` (FAB) → real-world light value reference organized by scenario
`Directional Light → Intensity (Lux)` → solar illuminance values
`Post Process Volume → Exposure → Manual EV100` → match real-world exposure
`Rect Light / Area Light → Intensity (Lumen)` → practical light sources
`Auto Exposure` → disable during PBL workflow; use Manual EV100""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "lighting, rendering, intermediate",
    },
    "related": "- `tutorials/realistic-and-physical-lighting-in-ue5-what-is-pbl.md` — Part 1: theory and units\n- `references/rendering-pipeline.md` — exposure, post-process, Lumen\n- `references/color-pipeline.md` — color grading after PBL render",
},

"tutorials/slow-motion-secrets-how-to-time-warp-animation-in-unreal-engine.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["animation", "sequencer", "cinematics", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Time-warping animation in Sequencer — using the `Time Warp` track and `Rate Scale` to create non-destructive slow motion moments on existing animation clips.",
        "summary": "Covers how to add slow-motion to pre-existing animation in Sequencer without re-animating. Demonstrates the Time Warp track on a control rig sub-sequence to retime specific hit/impact moments, and Rate Scale on animation clips for constant slow-down. Includes camera/chromatic aberration integration for stylized slo-mo.",
        "steps": """1. Open the Level Sequence containing the shot; locate the control rig sub-sequence
2. Right-click the animation/control rig track → **Add Time Warp Track**
3. Keyframe the Time Warp value: `1.0` = normal, `0.25` = 25% speed (slow motion)
4. Add easing keys around the slow-mo section to smoothly ramp in and out
5. Alternatively, select an animation clip in Sequencer → right-click → **Edit Section** → adjust `Rate Scale` (0.25 = 4x slower)
6. For camera: add chromatic aberration via Post Process Volume → `Lens → Chromatic Aberration Intensity` keyframed to peak at slo-mo moment
7. Preview in Sequencer (Shift+Space) to verify timing; adjust Time Warp keys as needed""",
        "systems": """`Time Warp Track` (Sequencer) → non-destructive retiming of animation sections
`Rate Scale` (animation clip property) → constant speed multiplier for entire clip
`Post Process Volume → Chromatic Aberration` → slo-mo visual enhancement
`Control Rig Sub-Sequence` → where Time Warp is most commonly applied""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "animation, sequencer, cinematics, intermediate",
    },
    "related": "- `references/sequencer-cinematics.md` — Sequencer track types and timeline workflow\n- `references/control-rig-animation.md` — Control Rig sub-sequence structure",
},

"tutorials/introduction-to-substrate-materials-unreal-engine-57.md": {
    "fm": {"ue_version": '"UE 5.7"', "tags": '["materials", "shaders", "substrate", "rendering", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Introduction to Substrate material framework — enabled by default from UE 5.7; `Substrate Slab` node replaces legacy material shading models for layered, physically-accurate surface rendering.",
        "summary": "Official Epic overview of Substrate in UE 5.7 (now enabled by default). Covers the Substrate Slab node structure (F0/F90 reflectivity, roughness, fuzz/glint advanced features), two GBuffer format options (high-fidelity vs. performance), and how Substrate gives artists more layering control than the traditional material system.",
        "steps": """1. Substrate is enabled by default in UE 5.7+ — no manual activation needed (check `Project Settings → Rendering → Substrate`)
2. In Material Editor, use the **`Substrate Slab`** node as the primary material expression
3. Configure `F0` (facing reflectivity) and `F90` (glancing angle reflectivity) for PBR accuracy
4. Set `Roughness` input for microsurface detail
5. Enable `Fuzz` layer for velvet/fabric surfaces; enable `Glint` for sparkle (car paint, glitter)
6. Layer multiple Slab nodes using **`Substrate Layer`** blend nodes
7. Choose GBuffer format in `Project Settings → Rendering → Substrate → GBuffer Format`: `8-Byte` (performance) or `16-Byte` (maximum fidelity)
8. Path Tracing is fully supported with Substrate — no special setup needed""",
        "systems": """`Substrate Slab` node — primary material primitive replacing old shading models
`F0 / F90` inputs → physically accurate reflectivity at facing and glancing angles
`Fuzz` input → microfiber/velvet surface layer
`Glint` input → sparkle highlights (car paint, metallic flake)
`Substrate Layer` node → blend/stack multiple Slab layers
`Project Settings → Rendering → Substrate → GBuffer Format` → 8-Byte (perf) or 16-Byte (fidelity)""",
        "difficulty": "Intermediate",
        "version": "UE 5.7",
        "tags": "materials, shaders, substrate, rendering, intermediate",
    },
    "related": "- `references/materials-shaders.md` — broader material system reference\n- `tutorials/everything-you-wanted-to-know-about-substratebut-are-too-afraid-to-ask-unreal-fe.md` — deep dive Unreal Fest talk\n- `references/rendering-pipeline.md` — Path Tracing compatibility",
},

"tutorials/ue5-constraints-are-easy-parent-constraint-workflow-for-animators.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["animation", "control-rig", "rigging", "sequencer", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Parent Constraint workflow in UE5 Sequencer — attaching character IK controls to props (or vice versa) for contact-hold animation without socket-based distortion.",
        "summary": "Practical guide to UE5's constraint system for animators. Demonstrates Parent Constraints in a door-opening shot: attaching hands to the door object so both move together, avoiding the rotation-socket distortion that occurs when attaching the door to the hands. Much simpler than Maya constraints — set up directly in Sequencer with keyable weights.",
        "steps": """1. In Sequencer, select the character's Control Rig track → open the animation in **Animation Mode**
2. Select the IK hand control that needs to follow a prop
3. In the `Constraints` panel (Anim Outliner or right-click control) → **Add Parent Constraint**
4. Pick the target object (e.g. the door skeletal mesh) as the constraint parent
5. The hand will now follow the door's transform — key the **Constraint Weight** at 0 before contact, ramp to 1 at contact frame
6. Animate the door separately (or via the prop's own animation track)
7. To release: key Constraint Weight back to 0 at the frame the hand leaves the prop
8. **Tip:** attach hands TO the prop, not prop to hands — avoids joint-socket extraction artifacts on rotation""",
        "systems": """`Parent Constraint` (Control Rig / Sequencer) → attaches one control's transform to another object
`Constraint Weight` track → keyable 0–1 blend to activate/deactivate constraint
`Anim Outliner` → constraint management UI in Animation Mode
Best practice: attach character IK to prop (not prop to character) to avoid socket distortion on rotation""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "animation, control-rig, rigging, sequencer, intermediate",
    },
    "related": "- `references/control-rig-animation.md` — Control Rig IK, FK, and layering\n- `tutorials/dynamic-space-switching-in-ue5-pro-ik-hand-constraint-techniques.md` — space switching for IK hands",
},

"tutorials/new-ue5-motion-trails-20-heat-map-camera-space-stabilization.md": {
    "fm": {"ue_version": '"UE 5.6"', "tags": '["animation", "sequencer", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Motion Trails 2.0 (introduced UE 5.6) — Heat Map visualization and Camera Space Stabilization modes for evaluating animation arc quality and viewport stability.",
        "summary": "Official UE tutorial on the new Motion Trails system added in 5.6. Covers the Heat Map mode which color-codes trail speed (useful for spotting pops/holds), and Camera Space Stabilization which keeps trails relative to the camera for cleaner arc evaluation even on moving cameras. Part of the ACOM Animation Sample project tutorial series.",
        "steps": """1. With a character/control selected in Sequencer, open **Motion Trails**: `Viewport → Show → Advanced → Motion Trails`
2. Select the controls to visualize (IK hands, feet, head) and enable Motion Trails for them
3. Switch to **Heat Map mode** in the Motion Trails settings panel — trail colors indicate speed (cool = slow, hot = fast)
4. Use Heat Map to spot timing issues: sudden color jumps = pops; extended cool regions = unintended holds
5. Enable **Camera Space Stabilization** — trails are now evaluated relative to the active camera rather than world space
6. Camera Space mode makes arc evaluation meaningful even on camera-moving shots
7. Adjust keyframes based on Heat Map feedback; re-evaluate trail to verify fix""",
        "systems": """`Motion Trails` (Viewport Show flags) → visualize bone/control arcs over time
`Heat Map Mode` → color-codes trail by velocity; cold=slow, hot=fast; use to spot pops/holds
`Camera Space Stabilization` → evaluates trails relative to camera (5.6+), improves arc review on moving shots
`ACOM Animation Sample Project` (Fab) → reference project for this tutorial series""",
        "difficulty": "Intermediate",
        "version": "UE 5.6",
        "tags": "animation, sequencer, intermediate, ue5-6",
    },
    "related": "- `references/control-rig-animation.md` — Control Rig animation tools\n- `references/sequencer-cinematics.md` — Sequencer workflow",
},

"tutorials/dynamic-space-switching-in-ue5-pro-ik-hand-constraint-techniques.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["animation", "control-rig", "rigging", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Dynamic Space Switching for IK hands in UE5 — changing the IK parent space between body parts (world, root, spine, chest) on a per-key basis directly in the viewport.",
        "summary": "Demonstrates UE5's built-in space switching system for IK controls in Control Rig. Shows how to switch an IK hand from world-locked to body-relative space mid-animation — essential for contact/holding shots — using the control's space switch property in the Anim Outliner. Covers the difference between world-space IK and body-space IK and when each is appropriate.",
        "steps": """1. In Animation Mode, select an IK hand control in the viewport
2. In the **Anim Outliner**, find the control → look for the `Space` property or right-click → **Switch Space**
3. Available spaces typically include: `World`, `Root`, `Pelvis`, `Spine`, `Chest`, `Parent`
4. Key the current space at the frame before switching (to preserve position)
5. Advance one frame, switch to the new space → key to lock
6. The control will now move with the new parent space from that frame forward
7. **Tip:** when a character grabs an object, switch IK hand space to the object's bone/socket so the hand sticks automatically
8. Combine with Parent Constraints for prop-holding shots""",
        "systems": """`Space Switching` property (IK Control in Control Rig) → parent space selector: World / Root / Pelvis / Spine / Chest
`Anim Outliner` → shows space property per control; key directly here
`IK Hand Control` → stays locked in chosen space; great for contact moments
`FK Hand Control` → body-relative by default; use when hand does not need to stay fixed in world""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "animation, control-rig, rigging, intermediate",
    },
    "related": "- `references/control-rig-animation.md` — full IK/FK and Control Rig reference\n- `tutorials/ue5-constraints-are-easy-parent-constraint-workflow-for-animators.md` — Parent Constraints for prop attachment",
},

"tutorials/pose-library-additive-mode-layer-animation-poses-in-unreal-engine.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["animation", "control-rig", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Pose Library in Animation Mode — saving, recalling, and blending between rig poses; using Additive Mode to layer corrective poses on top of existing animation.",
        "summary": "Official UE guide to the Pose Library tool available in Animation Mode. Covers creating pose assets from selected controls (e.g. fist shape for right hand), using the blend slider to apply poses partially, the Additive Mode which adds a pose delta on top of existing keyframe data, and using saved poses as one-click selection sets for complex rig controls.",
        "steps": """1. In Animation Mode, go to **Poses** panel (`Window → Poses` or the toolbar Poses button)
2. Select the rig controls you want to save (e.g. all right hand controls via Anim Outliner shift-click)
3. Click **Create Pose** → name it (e.g. `fist_R`) → asset saved to Content Browser
4. To apply: select destination controls → click pose thumbnail in the Poses panel
5. Use the **Blend** slider (0–1) to partially apply the pose
6. Enable **Additive Mode** toggle → pose is now applied as a delta on top of the current animation curve data
7. Use Additive Mode to layer corrective shapes (subtle fist tightening, shoulder adjustment) without destroying base animation
8. **Selection Set trick:** save a pose with multiple controls selected → clicking it re-selects those controls (acts as a selection set button)""",
        "systems": """`Poses Panel` (Animation Mode → Window → Poses) → UI for creating/applying/managing poses
`Create Pose` → saves current selected control transforms as a reusable asset
`Blend Slider` (0–1) → partial pose application
`Additive Mode` → pose applied as delta on top of existing keyframe data (non-destructive overlay)
`Capture Thumbnail` → update pose preview icon to current frame""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "animation, control-rig, intermediate",
    },
    "related": "- `references/control-rig-animation.md` — Control Rig animation tools\n- `tutorials/non-destructive-animation-in-ue5-layered-control-rigs-explained.md` — layered control rigs",
},

"tutorials/mastering-the-ue5-tweener-tool-push-pull-overshoot-animation.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["animation", "sequencer", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Tween Tool in UE5 Animation Mode — Push, Pull, Overshoot, Average, and Ease In/Out modes for non-destructively adjusting timing and pose blending between keyframes.",
        "summary": "Covers each mode of UE5's Tween Tool for animators: Push (extend toward next key), Pull (snap toward previous key), Overshoot (exaggerate beyond next key), Average (blend to 50% midpoint), and Ease variants. Demonstrated on a throwing animation to add anticipation and follow-through without re-keying. Each mode is accessible in the Animation toolbar.",
        "steps": """1. In Animation Mode, select the controls to tween
2. Scrub the timeline to the frame you want to adjust
3. Open the **Tween Tool** from the Animation toolbar (or `T` shortcut)
4. **Pull mode** (drag left): moves current pose toward the previous key — useful for anticipation
5. **Push mode** (drag right): moves current pose toward the next key — useful for follow-through
6. **Overshoot mode**: moves pose PAST the next key — adds exaggeration/snap to a hit
7. **Average mode**: blends current pose toward the mathematical midpoint between prev/next keys — smooths breakdowns
8. **Ease In / Ease Out**: slides the tangent timing without moving the pose value
9. Drag the Tween slider left/right to the desired amount; release to commit the tweak""",
        "systems": """`Tween Tool` (Animation Mode toolbar) → T shortcut or toolbar icon
Pull → toward previous key; Push → toward next key; Overshoot → past next key
Average → 50% midpoint blend; Ease In/Out → tangent timing adjustment
Works on selected controls only — select fewer controls for targeted tweaks""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "animation, sequencer, intermediate",
    },
    "related": "- `references/control-rig-animation.md` — Control Rig animation tools\n- `tutorials/ue5-curve-editor-20-new-lattice-tool-curve-scaling-hacks-ue-56.md` — Curve Editor for precision key editing",
},

"tutorials/ue5-curve-editor-20-new-lattice-tool-curve-scaling-hacks-ue-56.md": {
    "fm": {"ue_version": '"UE 5.6"', "tags": '["animation", "sequencer", "intermediate", "ue5-6"]', "extraction_status": "complete"},
    "notes": {
        "core": "Curve Editor 2.0 features in UE 5.6 — Lattice Tool for multi-key region manipulation and Curve Scaling hacks for non-uniform timing adjustment across multiple curves simultaneously.",
        "summary": "Tutorial on the Curve Editor enhancements in UE 5.6, particularly the new Lattice Tool which lets you draw a bounding region around multiple keys and warp them together (compress timing, add easing, reshape arcs non-destructively). Also covers curve scaling shortcuts for scaling value ranges and timing widths of selected key groups.",
        "steps": """1. In Animation Mode, open the **Curve Editor** (bottom panel or `Ctrl+Alt+C`)
2. Select a control rig sub-sequence to display its curves
3. **Lattice Tool** (new 5.6): click the lattice icon in the Curve Editor toolbar
4. Draw a selection box around the keys you want to shape; a lattice cage appears
5. Drag lattice handles to warp the timing/value of all enclosed keys simultaneously
6. **Curve Scaling**: select keys across multiple curves → use `Ctrl+drag` on the time axis to scale timing
7. Use `Alt+drag` on the value axis to scale the value range of selected keys
8. **Buffer Curves**: see `tutorials/ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks.md` for save/recall""",
        "systems": """`Curve Editor` (Animation Mode → bottom panel) → direct spline editing for all rig controls
`Lattice Tool` (5.6+) → multi-key region warp; draw box, drag handles to reshape
`Curve Scaling` → `Ctrl+drag` time axis (scale timing); `Alt+drag` value axis (scale values)
`Control Rig Sub-Sequence` → access for per-curve key data
`ACOM Animation Sample Project` → demo project used in tutorial""",
        "difficulty": "Intermediate",
        "version": "UE 5.6",
        "tags": "animation, sequencer, intermediate, ue5-6",
    },
    "related": "- `tutorials/ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks.md` — Buffer Curves and Smart Snap\n- `references/control-rig-animation.md` — Control Rig reference",
},

"tutorials/ue5-animation-layers-non-destructive-camera-shake-character-tweaks.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["animation", "sequencer", "cinematics", "camera", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Sequencer Animation Layers — adding non-destructive additive animation tracks on top of existing character or camera rig animation without altering the base performance.",
        "summary": "Covers UE5's Animation Layers in Sequencer for both characters and camera rigs. Demonstrates adding a camera shake layer on top of a Control Rig camera animation without touching the original keyframe data — layers blend additively and can be weighted/muted independently. Same workflow applies to characters for secondary motion, LOD adjustments, and micro-corrections.",
        "steps": """1. In Sequencer, find the character or camera Control Rig sub-sequence
2. Click **+ Track → Animation Layer** to add a new layer above the base animation
3. The new layer is empty and additive by default — it adds on top without replacing
4. Animate the layer's controls (e.g. camera position jitter, shoulder sway)
5. Adjust the **Layer Weight** in the track header (0 = off, 1 = full)
6. Key the Layer Weight to fade layers in/out per shot
7. **Camera Shake** use case: add a camera layer → animate small random translation/rotation offsets → result blends with the main camera move
8. **Character micro-correction** use case: add a layer → fix a specific joint overlap without re-animating the full performance
9. Layers can be muted/soloed in the track header for comparison""",
        "systems": """`Animation Layer Track` (Sequencer) → additive non-destructive animation on top of base sequence
`Layer Weight` → 0–1 keyable blend; mute/solo in track header
`Camera Rig` in Sequencer → skeletal mesh camera rig with its own Control Rig + animation layer
Works on both character Control Rig and camera rig sub-sequences""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "animation, sequencer, cinematics, camera, intermediate",
    },
    "related": "- `references/sequencer-cinematics.md` — Sequencer track types\n- `references/control-rig-animation.md` — Control Rig additive layers\n- `tutorials/non-destructive-animation-in-ue5-layered-control-rigs-explained.md` — layered control rigs",
},

"tutorials/ue5-curve-editor-secrets-buffer-curves-smart-snap-keyframe-tricks.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["animation", "sequencer", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Curve Editor workflow secrets — Buffer Curves (save/restore curve states as comparison reference) and Smart Snap (frame-accurate key placement with intelligent snapping).",
        "summary": "Reveals two powerful but underused Curve Editor features: Buffer Curves, which lets you save the current state of selected curves as a ghost reference and swap back and forth for A/B comparison; and Smart Snap, which intelligently snaps keys to nearby frames, handles, or curve intersections. Also covers a technique for adding a Camera Cut Track to a sub-sequence for quick camera navigation when editing deeply nested shots.",
        "steps": """1. In the Curve Editor, select the curves/keys you want to save as reference
2. **Buffer Curves**: right-click → **Buffer Curves** (or the Buffer button in toolbar) → curve state saved as ghost
3. After editing, compare by right-click → **Swap Buffer** — toggles between current and saved state
4. Use Buffer Curves for A/B: save a good timing, experiment, swap back if experiment fails
5. **Smart Snap**: enable the snap icon in Curve Editor toolbar → when dragging keys, they snap to nearby frames or curve intersections
6. Smart Snap respects the sequence frame rate; avoids sub-frame keys accidentally
7. **Camera Cut Track trick**: when editing a nested sub-sequence without a camera, add a Camera Cut Track pointing to the parent camera → enables quick camera view toggle inside the sub-sequence""",
        "systems": """`Buffer Curves` (Curve Editor right-click) → save/restore curve state for A/B comparison; Swap Buffer toggles
`Smart Snap` (Curve Editor toolbar) → intelligent key snapping to frames/handles/intersections
`Camera Cut Track` in sub-sequence → enables camera view access when navigating nested sequences
`Curve Editor` → accessible via bottom panel in Animation Mode""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "animation, sequencer, intermediate",
    },
    "related": "- `tutorials/ue5-curve-editor-20-new-lattice-tool-curve-scaling-hacks-ue-56.md` — Lattice Tool and curve scaling\n- `references/sequencer-cinematics.md` — Sequencer sub-sequence workflow",
},

"tutorials/non-destructive-animation-in-ue5-layered-control-rigs-explained.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["animation", "control-rig", "sequencer", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Layer Control Rigs in Sequencer — adding a live Modular Control Rig on top of a baked Animation Sequence to make non-destructive corrections and additive adjustments.",
        "summary": "Shows how to add a secondary Control Rig layer in Sequencer on top of an existing baked animation. The layer rig evaluates additively — you can tweak wrist rotation, fix foot sliding, or add secondary motion without touching the source animation data. Also notes a 2D sprite laser blast technique: hand-drawn 2D animation on a billboard lit mesh actor.",
        "steps": """1. In Sequencer, find the character's Animation Sequence track (baked mocap or keyframed)
2. Click **+ Track** on the Skeletal Mesh track → **Control Rig** → choose **Modular Control Rig** or a full body rig
3. The new Control Rig track evaluates ON TOP of the animation sequence additively
4. In the Control Rig track, scrub to the correction frame → move/rotate the desired control
5. Keys written to the Layer Control Rig track only; original Animation Sequence untouched
6. **Weight** the control rig layer (0–1) in the track header to blend the correction in
7. To remove: mute or delete the Control Rig layer track — original animation restored instantly
8. Use for: foot IK correction, wrist orientation fix, secondary bone override, stylistic exaggeration""",
        "systems": """`Layer Control Rig Track` (Sequencer → + Track → Control Rig) → additive rig on top of baked animation
`Modular Control Rig` → full body rig; use a partial/hand rig for targeted corrections
`Track Weight` (0–1) → blend layer contribution
`Animation Sequence` (base track) → untouched; layer sits above in evaluation stack
`2D Sprite / Lit Translucent Billboard` → technique for hand-drawn laser/VFX overlays on 3D scene""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "animation, control-rig, sequencer, intermediate",
    },
    "related": "- `references/control-rig-animation.md` — full Control Rig reference\n- `tutorials/ue5-animation-layers-non-destructive-camera-shake-character-tweaks.md` — animation layers on camera rigs\n- `tutorials/baking-animation-in-ue5-control-rig-to-animation-sequence-back.md` — baking round-trip",
},

"tutorials/baking-animation-in-ue5-control-rig-to-animation-sequence-back.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["animation", "control-rig", "sequencer", "pipeline", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Animation baking round-trip in UE5 — converting a live Control Rig in Sequencer to a baked Animation Sequence and back, understanding when each form is appropriate.",
        "summary": "Explains the difference between animating with a live Control Rig (interactive, editable) vs. a baked Animation Sequence (performant, portable) in Sequencer. Covers the bake workflow (Control Rig → Animation Sequence via right-click Bake To Animation Sequence), the reverse (re-link an Animation Sequence back to a Control Rig for editing), and production tradeoffs. Part of the ACOM Animation Sample tutorial series.",
        "steps": """1. Animate character using a live **Control Rig** sub-sequence in Sequencer
2. To bake: right-click the Control Rig track → **Bake To Animation Sequence** → choose output path and frame range
3. A new `.uasset` Animation Sequence is created; the Control Rig track is replaced (or kept)
4. Baked animation is portable and performant — use for crowd sims, AnimToTexture, MRQ renders
5. To re-edit: right-click the Animation Sequence track → **Link To Control Rig** → choose your rig
6. A live Control Rig layer is added on top of the baked sequence for additive editing
7. Re-bake after edits to update the base animation asset
8. **Rule of thumb:** keep live Control Rig during production; bake for delivery/export""",
        "systems": """`Bake To Animation Sequence` (right-click Control Rig track) → creates portable .uasset from live rig
`Link To Control Rig` (right-click Anim Sequence track) → re-attach rig for editing
`Control Rig Sub-Sequence` → live, editable; heavier viewport cost
`Animation Sequence` → baked, fast, portable; used for AnimToTexture, crowd instancing
Frame range and bone filter selectable at bake time""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "animation, control-rig, sequencer, pipeline, intermediate",
    },
    "related": "- `references/control-rig-animation.md` — Control Rig full reference\n- `tutorials/non-destructive-animation-in-ue5-layered-control-rigs-explained.md` — layer rigs for non-destructive edits\n- `references/sequencer-cinematics.md` — Sequencer pipeline",
},

"tutorials/stylized-animation-control-rig-characters-in-unreal-engine-5.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["animation", "control-rig", "rigging", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Exploring and animating a Control Rig character (non-MetaHuman) in UE5 — opening the character asset, inspecting the Modular Control Rig setup, and beginning keyframe animation in Animation Mode.",
        "summary": "Third video in the ACOM Animation Hub series. Focuses on the character Beta from the ACOM sample — a stylized non-MetaHuman robot character with a full Modular Control Rig. Shows how to open a character's Control Rig via the Content Browser, inspect IK/FK controls, switch to Animation Mode in Sequencer, and start posing/keyframing. Discusses FK vs IK tradeoffs for stylized characters.",
        "steps": """1. Find the character asset in the Content Browser: `Assets/Characters/[CharacterName]`
2. Double-click to open the **Skeletal Mesh** editor → inspect the rig hierarchy
3. Drag the character into a **Level Sequence** in Sequencer
4. On the character track, click **+ Sub-Sequence → Control Rig** to add an animation sub-sequence
5. Select **Modular Control Rig** (or the character's specific full-body rig)
6. Enter **Animation Mode** (Sequencer toolbar) to enable interactive posing
7. Select controls in the viewport or the **Anim Outliner** panel
8. Use `G` key to toggle between FK (rotate-only) and IK (position-based) control modes
9. Set keys with `S` (all controls) or `Ctrl+S` (selected controls only)""",
        "systems": """`Content Browser → Assets/Characters` → character skeletal mesh location
`Modular Control Rig` → pre-built IK/FK module library; drag controls in viewport
`Anim Outliner` (Animation Mode) → hierarchical list of all rig controls
`G key` → FK/IK toggle for limb controls
`S` → set keys for all visible controls; `Ctrl+S` → selected only
`Animation Mode` (Sequencer toolbar) → activates posing tools""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "animation, control-rig, rigging, intermediate",
    },
    "related": "- `references/control-rig-animation.md` — Modular Control Rig and IK reference\n- `tutorials/baking-animation-in-ue5-control-rig-to-animation-sequence-back.md` — baking the finished animation",
},

"tutorials/advanced-ue5-cinematic-workflow-camera-rigs-custom-viewports.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["sequencer", "cinematics", "camera", "pipeline", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Advanced Sequencer cinematic workflow — sub-sequences structure, camera rig skeletal mesh + Control Rig setup, and custom multi-panel viewport layouts for simultaneous camera + perspective editing.",
        "summary": "Second video in the ACOM Animation Hub series. Covers the master Level Sequence → sub-sequences hierarchy (all are just Level Sequences; naming is organizational), setting up a Camera Rig Skeletal Mesh with its own Control Rig track for physically-driven camera moves, and configuring custom viewport layouts (e.g. 2-panel: camera view left, perspective right) for efficient animation editing.",
        "steps": """1. In Sequencer, inspect the master Level Sequence → Shot Track → each shot is a sub-sequence Level Sequence
2. Double-click a shot to enter it; `breadcrumb` path shown at top of Sequencer
3. Inside a shot, find the **Camera Rig** skeletal mesh track — it's a separate Skeletal Mesh Actor
4. The Camera Rig has its own **Control Rig sub-sequence** for animating the camera physically
5. The actual **Cine Camera Actor** is a child of the Camera Rig — inherits its transform
6. To set up custom viewport: `Viewport → Layout` dropdown → choose a split layout (2×1, 1+2, etc.)
7. In one viewport: press `G` → Pilot the Camera for the camera POV
8. In the other: keep as Perspective for working around the scene
9. Lock the camera viewport to a specific shot camera using the camera selector dropdown""",
        "systems": """`Shot Track` (master Level Sequence) → contains sub-sequences as individual shots
`Sub-sequence` → just a Level Sequence nested inside another; same asset type
`Camera Rig Skeletal Mesh` → physically-simulated camera crane/dolly; driven by Control Rig
`Cine Camera Actor` → parented to Camera Rig; inherits physical motion
`Viewport → Layout` → split into multiple panels; one camera view + one perspective
`Breadcrumb Trail` (Sequencer top bar) → shows nesting depth; click to navigate up""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "sequencer, cinematics, camera, pipeline, intermediate",
    },
    "related": "- `references/sequencer-cinematics.md` — Sequencer structure and camera workflow\n- `tutorials/level-management-sub-levels-spawnables-possessibles-in-ue5.md` — level organization for cinematics",
},

"tutorials/level-management-sub-levels-spawnables-possessibles-in-ue5.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["sequencer", "cinematics", "narrative", "pipeline", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Level organization for cinematic productions — Sub-Levels in the Levels panel for modular asset/lighting management, and Spawnables vs. Possessibles in Sequencer for actor lifecycle control.",
        "summary": "First video in the ACOM Animation Hub series (world/level overview). Covers the Levels panel (Window > Levels) and using Sub-Levels to isolate lighting, geometry, and assets per zone — toggle entire level chunks on/off. Then explains Sequencer's Spawnables (spawned by Sequencer; exist only during playback; portable between levels) vs. Possessibles (already in level; Sequencer takes control; level-specific). Critical distinction for cinematic production flexibility.",
        "steps": """1. Open **Window → Levels** to see the sub-level hierarchy for the persistent world
2. Each sub-level contains isolated content (lighting, environment geometry, props) — toggle visibility/loading per sub-level
3. To control sub-levels from Sequencer: add a **Level Visibility Track** → reference specific sub-levels by name
4. **Spawnables**: in Sequencer, click the actor's track header `+` → `Convert to Spawnable` → now the actor is managed by Sequencer (spawns/despawns with the sequence)
5. **Possessibles**: default mode — Sequencer takes control of an actor that already exists in the level
6. Use **Spawnables** for characters/cameras that move between shots or sequences (portable)
7. Use **Possessibles** for environment actors that are permanently placed in the level
8. **Level Streaming Volumes** or Blueprint can auto-load/unload sub-levels based on player/camera position""",
        "systems": """`Window → Levels` panel → sub-level manager; toggle load/visibility per sub-level
`Level Visibility Track` (Sequencer) → load/unload sub-levels at specific frames
`Spawnable` (Sequencer) → actor created and destroyed by Sequencer; portable; green 'S' icon
`Possessible` (Sequencer) → pre-placed level actor; Sequencer controls properties only; yellow 'P' icon
`World Composition` / `World Partition` → alternative streaming for open-world projects""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "sequencer, cinematics, narrative, pipeline, intermediate",
    },
    "related": "- `references/narrative-blueprints.md` — level streaming and Blueprint-triggered cinematics\n- `references/sequencer-cinematics.md` — Sequencer track types and sub-sequences\n- `tutorials/advanced-ue5-cinematic-workflow-camera-rigs-custom-viewports.md` — sub-sequences structure",
},

"tutorials/metahumans-for-mocap-unreal-engine-animation-hub.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["metahuman", "animation", "mocap", "blueprint", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Setting up a MetaHuman for Mocap Manager — creating a `CaptureCharacter`-derived Blueprint that inherits the MetaHuman's skeletal mesh components, enabling real-time mocap streaming.",
        "summary": "Animation Hub tutorial on adapting a MetaHuman for use with Mocap Manager live capture. The standard MetaHuman Blueprint cannot be used directly — a new Blueprint inheriting from `CaptureCharacter` must be created, and the Skeletal Mesh components (body, head, groom, clothing) manually copied over. The resulting actor can then receive Live Link data from Mocap Manager for real-time face and body capture.",
        "steps": """1. Open your MetaHuman Blueprint in the editor
2. Create a **New Blueprint Class** → parent class: `CaptureCharacter` (search for it in the class picker)
3. Name the new BP (e.g. `CaptureCharacter_MH_[CharacterName]`)
4. Open both the original MetaHuman BP and the new CaptureCharacter BP side-by-side
5. From the MetaHuman BP: **copy** the `Body` Skeletal Mesh component → paste into the new BP's component hierarchy
6. Copy all remaining Skeletal Mesh components (face, torso accessories, groom) → paste into new BP
7. Verify all mesh assets are correctly assigned in the Details panel of each component
8. Set the **LOD Sync** and **Animation Blueprint** references to match the original MetaHuman
9. Place the new `CaptureCharacter` BP in the level → point Live Link source at it for mocap streaming""",
        "systems": """`CaptureCharacter` class → base class for MetaHumans used with Mocap Manager; enables Live Link body/face
`Blueprint Class → Reparent` or new → inherit from CaptureCharacter
Skeletal Mesh components (Body, Face, Torso, Groom) → must be manually copied from original MetaHuman BP
`Live Link` → connects Mocap Manager capture data to the CaptureCharacter BP
`LOD Sync` → synchronize LOD levels across all MetaHuman mesh components""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "metahuman, animation, mocap, blueprint, intermediate",
    },
    "related": "- `references/metahuman-reference.md` — MetaHuman setup, LOD, animation\n- `tutorials/metahuman-realtime-animator-best-practices-unreal-engine-animation-hub.md` — webcam MetaHuman Animator\n- `tutorials/live-link-hub-tips-unreal-engine-animation-hub.md` — Live Link Hub setup",
},

"tutorials/everything-you-wanted-to-know-about-substratebut-are-too-afraid-to-ask-unreal-fe.md": {
    "fm": {"ue_version": '"UE 5.7"', "tags": '["materials", "shaders", "substrate", "rendering", "advanced"]', "extraction_status": "complete"},
    "notes": {
        "core": "Deep-dive Substrate system talk (Unreal Fest Stockholm 2025) — architecture, GBuffer formats, layering system, path tracing support, migration from legacy shading models, and practical usage patterns for games, linear, and CG-viz.",
        "summary": "43-minute technical session by Nathaniel Morgan (Principal Technical Artist, Epic) covering everything about Substrate: why it replaces the legacy shading model system, the Slab node architecture, two GBuffer memory formats (8-byte performance vs. 16-byte fidelity), material layering via the operator stack, Substrate's path tracing integration, and migration guides. Production-ready as of UE 5.7 and enabled by default.",
        "steps": """1. Substrate enabled by default in 5.7 — check `Project Settings → Rendering → Substrate → Enable Substrate`
2. Choose **GBuffer Format**: `Substrate 8-Byte` (performance; mobile/console) or `Substrate 16-Byte` (fidelity; PC/linear)
3. Core unit: **Substrate Slab** node → configure F0, F90, Roughness, Diffuse Albedo, Normal
4. Add optional **Fuzz Layer** for cloth/velvet; **Glint** for car paint sparkle; **SSS** for skin
5. Use **Substrate Layer Blend** nodes to stack multiple Slab nodes (by weight or mask)
6. **Thin Film Interference** node → iridescent surfaces (soap bubbles, oil slicks, beetle wings)
7. Legacy material output nodes (`DefaultLit`, `Unlit`, etc.) auto-migrate — existing materials should work
8. Substrate materials work in both rasterization and **Path Tracing** without any special nodes
9. For advanced SSS (subsurface scattering) skin: use the `Subsurface` Slab parameter instead of the legacy SSS shading model""",
        "systems": """`Substrate Slab` node → physically-accurate surface primitive (F0, F90, Roughness, Albedo, Normal, Fuzz, Glint, SSS, Anisotropy)
`Substrate Layer Blend` → stack multiple Slabs with mask or weight
`Thin Film Interference` node → iridescent surface effect
`Project Settings → Rendering → Substrate → GBuffer Format` → 8-Byte (performance) or 16-Byte (fidelity)
Path Tracing → fully compatible; no extra nodes required
Legacy materials → auto-migrate; no manual rework for basic surfaces
Principal engineers: Sebastian Haleir + Charles de Rousier""",
        "difficulty": "Advanced",
        "version": "UE 5.7",
        "tags": "materials, shaders, substrate, rendering, advanced",
    },
    "related": "- `tutorials/introduction-to-substrate-materials-unreal-engine-57.md` — beginner intro to Substrate\n- `references/materials-shaders.md` — full materials reference\n- `references/rendering-pipeline.md` — Path Tracing integration",
},

"tutorials/unreal-engine-5-animation-cinematic-production-overview.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["animation", "sequencer", "cinematics", "pipeline", "beginner"]', "extraction_status": "complete"},
    "notes": {
        "core": "High-level overview of cinematic animation production in UE5 using the ACOM Animation Sample Project — project structure, Level Sequences, sub-sequences, and the animation editing workflow.",
        "summary": "First video in Sir Wade's UE5 Animation tutorial series using the ACOM (Agora Studio) animation sample project available on FAB. Overview of the full project: welcome level, stylized characters (Beta + Gamma robots), the master Level Sequence structure, how shots are organized as sub-sequences, and what tools will be covered in subsequent videos. Entry point for the entire series.",
        "steps": """1. Download the **ACOM Animation Sample Project** from Fab (free)
2. Open project → `Welcome Level` shows idle characters; hit Play to preview
3. Open **Level Sequences** (Content Browser → Episodes → IntroBeta) to find the main cinematic sequence
4. Inspect the **Master Sequence** → contains a Shot Track with individual shot sub-sequences
5. Open a shot sub-sequence → see character tracks, camera tracks, Control Rig sub-sequences
6. Switch to **Animation Mode** (Sequencer toolbar toggle) to enable interactive posing
7. Character details: stylized robot by Agora Studio; uses Modular Control Rig + UE physics for secondary motion
8. Following videos in series cover: animation data (baking), curve editor, constraints, motion trails, layers""",
        "systems": """`ACOM Animation Sample Project` (Fab, free) → full cinematic production project by Agora Studio
`Master Level Sequence` → contains Shot Track → individual shot sub-sequences
`Animation Mode` (Sequencer toolbar) → enables interactive Control Rig posing
`Modular Control Rig` → character rig used for Beta/Gamma robots
`ACOM Project structure`: Episodes → IntroBeta → master sequence → shot sub-sequences""",
        "difficulty": "Beginner",
        "version": "UE5",
        "tags": "animation, sequencer, cinematics, pipeline, beginner",
    },
    "related": "- `references/sequencer-cinematics.md` — Sequencer and Level Sequence reference\n- `tutorials/advanced-ue5-cinematic-workflow-camera-rigs-custom-viewports.md` — sub-sequences deep dive\n- `tutorials/level-management-sub-levels-spawnables-possessibles-in-ue5.md` — level structure",
},

"tutorials/metahuman-realtime-animator-best-practices-unreal-engine-animation-hub.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["metahuman", "animation", "mocap", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Webcam-based MetaHuman Animator facial capture — setting up a USB webcam via Live Link for real-time performance capture with best practices for frame rate, resolution, and environment.",
        "summary": "Practical best practices for using MetaHuman Animator with a webcam source via Live Link. Covers enabling the MetaHuman Live Link plugin, configuring the source (`Add Source → MetaHuman Video`), optimal camera settings (720p/90fps preferred over 1080p/60fps for facial capture quality), lighting environment requirements, and recording workflow. Uses a Logitech Brio as the test camera.",
        "steps": """1. Enable plugins: `Edit → Plugins → MetaHuman Live Link` (+ Face AR Streaming, Live Link)
2. Open **Live Link** window (`Window → Live Link`)
3. `Add Source → MetaHuman Video` → select your webcam from the device list
4. Set camera resolution: **720p @ 90fps** preferred over 1080p @ 60fps (better fine facial motion fidelity)
5. Position webcam at eye level, ~50–60cm from face; even frontal lighting with no harsh shadows
6. In the Sequencer MetaHuman track: `Add → Live Link Control Rig → Live Link Face` (or ARKit)
7. Preview the live capture in the MetaHuman face; adjust `Strength` per blend shape as needed
8. Hit **Record** in Live Link Sequencer integration to bake the performance to an Animation Sequence
9. Review and clean up the captured curves in the Curve Editor""",
        "systems": """`MetaHuman Live Link Plugin` → enables webcam/iPhone face capture via Live Link
`Live Link Window → Add Source → MetaHuman Video` → webcam source setup
Optimal settings: 720p @ 90fps (Logitech Brio or equivalent USB webcam)
`Live Link Face Track` (Sequencer) → real-time MetaHuman face control from Live Link stream
`Record` in Live Link Recorder → bakes to Animation Sequence
Lighting: even, frontal; avoid harsh shadows or backlight for accurate blend shape detection""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "metahuman, animation, mocap, intermediate",
    },
    "related": "- `references/metahuman-reference.md` — MetaHuman setup and animation methods\n- `tutorials/metahumans-for-mocap-unreal-engine-animation-hub.md` — CaptureCharacter setup for Mocap Manager\n- `tutorials/live-link-hub-tips-unreal-engine-animation-hub.md` — Live Link Hub multi-source management\n- `references/lip-sync.md` — audio-driven facial animation",
},

"tutorials/live-link-hub-tips-unreal-engine-animation-hub.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["animation", "mocap", "pipeline", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Live Link Hub standalone app — routing multiple mocap streams (body + face + props) from different systems to multiple UE editor workstations simultaneously over a subnet.",
        "summary": "Covers Live Link Hub as a centralized routing app for professional mocap setups. Demonstrates adding multiple sources (Captury body, OptiTrack, iLinked face) simultaneously, routing streams to multiple UE editor instances on the same subnet, recording all streams together, and managing which clients receive which data. Enables team-based mocap sessions where multiple animators work on different characters from the same live data.",
        "steps": """1. Enable **Live Link Hub Plugin** in UE (`Edit → Plugins → Live Link Hub`)
2. Launch Hub: `Tools → Live Link Hub` (standalone window; can run on a dedicated machine)
3. In Live Link Hub: `Add Source` → choose your mocap system (Captury, OptiTrack, iLinked, MetaHuman Video, etc.)
4. Sources appear in the left panel; subject list populates automatically
5. **Clients** panel (right) shows all UE editor instances on the same subnet — verify correct workstation is listed
6. Assign subjects to clients (optional; default: all subjects broadcast to all clients)
7. Hit **Record All** to capture all streams simultaneously to a single session
8. In each UE editor, open Live Link window → subjects from Hub appear automatically (no local source setup needed)
9. Useful for multi-character scenes: different team members animate different characters from same live data""",
        "systems": """`Live Link Hub` (standalone app) → centralized Live Link routing; Tools → Live Link Hub
`Add Source` → Captury Body, OptiTrack, iLinked Face, MetaHuman Video, etc.
`Clients Panel` → shows all UE editor instances on subnet; assign subjects per client
`Record All` → simultaneous multi-source recording
`Subnet discovery` → automatic; all editors on same network segment see Live Link Hub""",
        "difficulty": "Intermediate",
        "version": "UE5",
        "tags": "animation, mocap, pipeline, intermediate",
    },
    "related": "- `tutorials/metahumans-for-mocap-unreal-engine-animation-hub.md` — CaptureCharacter setup\n- `tutorials/metahuman-realtime-animator-best-practices-unreal-engine-animation-hub.md` — webcam face capture\n- `references/metahuman-reference.md` — MetaHuman animation pipeline",
},

"tutorials/movie-render-graph-intro-unreal-engine-animation-hub.md": {
    "fm": {"ue_version": '"UE 5.8"', "tags": '["rendering", "movie-render-graph", "sequencer", "cinematics", "intermediate"]', "extraction_status": "complete"},
    "notes": {
        "core": "Movie Render Graph (MRG) node-based render pipeline intro — setting up render globals, defining shot layers, and configuring output — the preferred replacement for legacy Movie Render Queue.",
        "summary": "Practical intro to Movie Render Graph from the Animation Hub series, using the ACOM sample project. Shows right-clicking a Level Sequence to create an MRG asset, the node graph interface (Render Globals → Output → Layers), configuring warm-up settings and game overrides, setting up per-layer render passes (beauty, cryptomatte, depth), and triggering a render. MRG is fully production-ready from UE 5.8.",
        "steps": """1. In Content Browser, right-click a Level Sequence → `Cinematic → Movie Render Graph` → name and save the asset
2. Double-click the MRG asset to open the node graph
3. The graph has: `Render Globals` node (warm-up, resolution, frame range) → connected to output layers
4. Configure `Render Globals`: set `Warm Up Frame Count` (30–60 for physics/Niagara), `Resolution`, `Output Directory`
5. Add a **Render Layer** node for the Beauty pass; connect to an **EXR Output** or **PNG Output** node
6. Add additional Render Layer nodes for compositing passes: `Cryptomatte`, `Depth`, `Motion Vectors`
7. Set `Game Overrides` node: disable LOD bias, enable high-quality shadows, disable streaming textures
8. Right-click the graph → **Render** or queue multiple sequences
9. Monitor output in `Output Log` → renders save to specified directory""",
        "systems": """`Movie Render Graph` (Content Browser → Cinematic → Movie Render Graph) → node-based render pipeline
`Render Globals` node → warm-up, resolution, frame rate, output path
`Render Layer` node → per-pass render configuration (beauty, depth, cryptomatte)
`Game Overrides` node → disables streaming, enables high-quality settings for render
`EXR Output` / `PNG Output` nodes → file format selection per layer
Fully production-ready from UE 5.8; replaces linear Movie Render Queue""",
        "difficulty": "Intermediate",
        "version": "UE 5.8",
        "tags": "rendering, movie-render-graph, sequencer, cinematics, intermediate",
    },
    "related": "- `references/sequencer-cinematics.md` — MRQ/MRG settings reference\n- `recipes/mrq-multipass-exr.md` — multi-pass EXR setup\n- `recipes/cinematics-pipeline.md` — full pipeline Stage 7: render",
},

"tutorials/advanced-groom-dataflow-setup-in-ue-57-unreal-fest-stockholm-2025.md": {
    "fm": {"ue_version": '"UE 5.7"', "tags": '["metahuman", "rigging", "advanced", "ue5-7"]', "extraction_status": "complete"},
    "notes": {
        "core": "Groom Dataflow framework (UE 5.7) — a node-based procedural system for setting up, deforming, and customizing grooms (hair/fur) inside Unreal Engine, replacing the static import-only pipeline.",
        "summary": "Unreal Fest Stockholm 2025 talk by Michael Fro (Epic Physics Engineer) on the new Groom Dataflow framework in UE 5.7. The old pipeline required all groom setup in DCC (Maya/Houdini) then static import. Dataflow brings a node-based procedural graph inside UE for modifying guides, adding procedural deformations (wind, physics simulation), and blending groom behaviors — without going back to DCC. Covers motivation, Dataflow framework basics, groom integration nodes, and a practical example.",
        "steps": """1. Import your base groom asset as before (USD/Alembic .abc); this is still the starting point
2. Open the groom asset → find the new **Dataflow** tab in the groom editor (UE 5.7+)
3. The Dataflow graph uses nodes to modify the imported groom procedurally
4. Add **Guide Deformation** nodes for dynamic modifications (physics simulation, wind response)
5. Connect groom guides through `Groom Physics` node for real-time strand simulation
6. Add **Blend Shape** nodes to mix between styled and simulated states (e.g. 70% style / 30% physics)
7. The Dataflow graph is re-evaluated at runtime — no baking needed for simulation
8. Use **Groom Binding** asset to bind groom to skeletal mesh (required for character movement)
9. Preview in the groom editor with live physics: adjust stiffness, damping, collision radius""",
        "systems": """`Groom Asset → Dataflow Tab` (UE 5.7+) → node-based procedural groom modification inside engine
`Guide Deformation Node` → applies physical simulation/wind deformation to guides
`Groom Physics Node` → real-time strand simulation parameters (stiffness, damping)
`Blend Shape Node` → mix styled groom with simulated state
`Groom Binding Asset` → binds groom guides to skeletal mesh bones for character animation
Import format: USD Alembic (.abc) from Maya/Houdini still required as base groom""",
        "difficulty": "Advanced",
        "version": "UE 5.7",
        "tags": "metahuman, rigging, advanced, ue5-7",
    },
    "related": "- `tutorials/how-to-create-grooms-for-metahumans-unreal-fest-bali-2025.md` — strand-based groom creation for MetaHumans\n- `references/metahuman-reference.md` — MetaHuman hair and groom setup",
},

"tutorials/large-scale-animated-foliage-in-the-witcher-4-unreal-engine-5-tech-demo-unreal-f.md": {
    "fm": {"ue_version": '"UE 5.7"', "tags": '["nanite", "pcg", "rendering", "pipeline", "advanced", "ue5-7"]', "extraction_status": "complete"},
    "notes": {
        "core": "Large-scale animated foliage techniques from the Witcher 4 UE5 tech demo — vertex animation shaders, Nanite foliage with wind, PCG procedural placement, and performance optimization for console (PS5 @ 60fps).",
        "summary": "Unreal Fest Stockholm 2025 talk by Kevin (Epic) with CD Projekt's Tyce and Vignesh on the Witcher 4 UE5 tech demo foliage pipeline. Covers early experiments, the final solution combining Nanite foliage with a custom vertex animation shader for wind, PCG procedural placement of dense vegetation, and the engine features shipped in UE 5.7 as a result of this collaboration. Running at PS5 60fps with full Lumen/Nanite/TSR.",
        "steps": """1. **Nanite Foliage**: enable Nanite on Static Mesh foliage assets for unlimited polygon count without impostor LODs
2. **Wind animation with Nanite**: use **World Position Offset (WPO)** material with vertex animation shader — Nanite now supports WPO deformation (enabled per-asset, has performance cost)
3. **PCG placement**: use PCG Graph to scatter foliage based on terrain masks, slope, biome rules — replace manual painting
4. Set PCG density parameters driven by distance from camera for streaming LOD behavior
5. **Foliage physics blending**: blend between physics simulation (near) and vertex animation (far) using distance fade
6. **Wind direction system**: global wind parameter collection drives all foliage WPO shaders from one central control
7. Performance: profile `Stat GPU` → vegetation WPO cost; tune WPO `Maximum World Position Offset Displacement` per foliage type
8. Shipped UE 5.7 feature: Nanite WPO improvements specifically from this demo""",
        "systems": """`Nanite → Enable WPO` (per Static Mesh) → Nanite-compatible vertex animation for wind deformation
`World Position Offset (WPO)` material → drives wind sway; controlled by global wind parameter collection
`PCG Graph` → procedural placement of foliage using terrain masks, slope, biome rules
`Stat GPU` → profile WPO vertex animation performance cost
`MPC_Wind` (Material Parameter Collection) → centralized wind direction/speed for all foliage shaders
New in UE 5.7: Nanite WPO enhancements from Witcher 4 collaboration""",
        "difficulty": "Advanced",
        "version": "UE 5.7",
        "tags": "nanite, pcg, rendering, pipeline, advanced, ue5-7",
    },
    "related": "- `references/rendering-pipeline.md` — Nanite and Lumen reference\n- `references/materials-shaders.md` — WPO material expressions",
},

"tutorials/how-to-create-grooms-for-metahumans-unreal-fest-bali-2025.md": {
    "fm": {"ue_version": '"UE5"', "tags": '["metahuman", "rigging", "advanced"]', "extraction_status": "complete"},
    "notes": {
        "core": "Strand-based MetaHuman groom creation workflow — guide-driven system, procedural node modifiers (clumping, noise, curl), and achieving production-quality hair using the MetaHuman Creator + Groom tools.",
        "summary": "30-minute Unreal Fest Bali 2025 session by Hugo Lignac (Epic Groom Team) on creating production-quality grooms for MetaHumans. Covers the foundational guide-driven system, procedural node graph for applying clumping/noise/curl modifiers, the artistic vs. technical balance in hair design, and how MetaHuman Creator's groom presets work under the hood. Targets studios aiming for film/linear quality hair within UE5.",
        "steps": """1. Start from **MetaHuman Creator** groom presets as a base (download via MetaHuman Plugin)
2. Open the groom asset → inspect the **Guide Strands** (low-density splines defining flow and volume)
3. In the **Groom Editor → Nodes**, add procedural modifiers in order:
   - `Clump` → groups nearby strands into natural clusters; set clump radius and per-clump noise
   - `Noise / Curl` → adds randomization and natural variation along strand length
   - `Cut` → trims strand tips to desired length and shape
4. Adjust `Strand Count` (rendered strands, not guides) — film quality: 100K–300K; realtime: 20K–60K
5. Set up **Groom Binding** to bind groom to the MetaHuman's head skeletal mesh
6. In UE: assign groom to the `Groom Component` on the MetaHuman BP's head component
7. Configure `LOD Settings` → reduce strand count at distance; use `Strands → Meshes` conversion for extreme LOD
8. Test with Lumen and Path Tracing — groom renders correctly in both; Path Tracing gives most accurate self-shadowing""",
        "systems": """`Guide Strands` → low-density splines; define hair flow and volume basis for interpolated final strands
`Clump Modifier` → groups strands naturally; most impactful modifier for believability
`Noise / Curl Modifier` → adds randomization along length
`Strand Count` → rendered strands (not guides); balance quality vs. performance
`Groom Binding Asset` → required link between groom guides and character head skeletal mesh
`Groom Component` (MetaHuman BP → Head) → where groom is attached for rendering
LOD: `Strands → Meshes` conversion for distant LOD levels""",
        "difficulty": "Advanced",
        "version": "UE5",
        "tags": "metahuman, rigging, advanced",
    },
    "related": "- `tutorials/advanced-groom-dataflow-setup-in-ue-57-unreal-fest-stockholm-2025.md` — Groom Dataflow for physics/deformation\n- `references/metahuman-reference.md` — MetaHuman setup and components",
},

}  # end EXTRACTIONS


print(f"Processing {len(EXTRACTIONS)} tutorial files...")
for filepath, data in EXTRACTIONS.items():
    update_file(filepath, data["fm"], data["notes"], data["related"])

print("\nAll extractions complete.")
