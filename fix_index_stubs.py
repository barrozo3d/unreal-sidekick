import re

idx = open('tutorials/INDEX.md', 'r', encoding='utf-8-sig').read()

replacements = []

# 1. unreal-engine-5.8-release-notes
old1 = "### unreal-engine-5.8-release-notes\n- **Source:** Epic Documentation\n- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5.8-release-notes\n- **Pages:** 1\n- **UE Version:** [PENDING]\n- **Tags:** [PENDING]\n- **Summary:** [PENDING EXTRACTION]\n- **File:** tutorials/unreal-engine-58-release-notes.md"
new1 = "### Unreal Engine 5.8 Release Notes (Epic Documentation)\n- **Source:** Epic Documentation\n- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5.8-release-notes\n- **Pages:** 1 (ToC only - dynamic page; full content in `references/release-notes-ue58.md`)\n- **UE Version:** 5.8\n- **Tags:** ue5-8, rendering, cinematics, animation, metahuman, audio, metasounds, lumen, nanite\n- **Summary:** UE 5.8 is the last planned major UE5 release. Key promotions: MegaLights to production-ready, Movie Render Graph fully production-ready, Accumulation DOF production-ready, Control Rig Dynamics 5x faster and production-ready. New experimental features: Animation Mixer (layer animations in Sequencer), MetaHuman Crowd, MCP Server Plugin (AI <> UE editor). Audio additions: Audio Subtitles Beta, MetaSound Pages, WASAPI. MetaHuman Animator gains audio-driven mode.\n- **File:** tutorials/unreal-engine-58-release-notes.md\n- **Also see:** `references/release-notes-ue58.md` (synthesized full reference)"
replacements.append((old1, new1))

# 2. lip-sync-in-unreal-engine
old2 = "### lip-sync-in-unreal-engine\n- **Source:** Epic Documentation\n- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/lip-sync-in-unreal-engine\n- **Pages:** 1\n- **UE Version:** [PENDING]\n- **Tags:** [PENDING]\n- **Summary:** [PENDING EXTRACTION]\n- **File:** tutorials/lip-sync-in-unreal-engine.md"
new2 = "### Lip Sync in Unreal Engine (Epic Documentation)\n- **Source:** Epic Documentation\n- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/lip-sync-in-unreal-engine\n- **Pages:** 1 (sparse - dynamic page; full reference in `references/lip-sync.md`)\n- **UE Version:** UE 5.0+\n- **Tags:** lip-sync, metahuman, audio, animation, blueprint\n- **Summary:** Epic documentation hub for lip sync in Unreal Engine. Covers OVR Lipsync plugin (Meta plugin for phoneme-driven MetaHuman jaw animation), MetaHuman Animator audio-driven mode (UE5.8+), and integration with Sequencer audio tracks. Full practical workflow including 11 Labs integration in `references/lip-sync.md`.\n- **File:** tutorials/lip-sync-in-unreal-engine.md\n- **Also see:** `references/lip-sync.md` (complete practical reference)"
replacements.append((old2, new2))

# 3. color-management-in-unreal-engine
old3 = "### color-management-in-unreal-engine\n- **Source:** Epic Documentation\n- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/color-management-in-unreal-engine\n- **Pages:** 1\n- **UE Version:** [PENDING]\n- **Tags:** [PENDING]\n- **Summary:** [PENDING EXTRACTION]\n- **File:** tutorials/color-management-in-unreal-engine.md"
new3 = "### Color Management in Unreal Engine (Epic Documentation)\n- **Source:** Epic Documentation\n- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/color-management-in-unreal-engine\n- **Pages:** 1 (sparse - dynamic page; full reference in `references/color-pipeline.md`)\n- **UE Version:** UE 5.0+\n- **Tags:** color-grading, ocio, rendering, cinematics, davinci, post-process\n- **Summary:** Epic documentation hub for UE color management. Covers OCIO (Open Color IO) integration for shared color transforms between UE and DaVinci Resolve, Post Process Volume color grading parameters, LUT import workflow, ACES/sRGB pipelines, and EXR export settings for compositing. Full workflow in `references/color-pipeline.md`.\n- **File:** tutorials/color-management-in-unreal-engine.md\n- **Also see:** `references/color-pipeline.md` (complete practical reference)"
replacements.append((old3, new3))

# 4. Level Streaming in Unreal Engine
old4 = "### Level Streaming in Unreal Engine\n- **Source:** Epic Documentation\n- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/level-streaming-in-unreal-engine\n- **Pages:** 15\n- **UE Version:** [PENDING]\n- **Tags:** [PENDING]\n- **Summary:** [PENDING EXTRACTION]\n- **File:** tutorials/level-streaming-in-unreal-engine.md"
new4 = "### Level Streaming in Unreal Engine (Epic Documentation)\n- **Source:** Epic Documentation\n- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/level-streaming-in-unreal-engine\n- **Pages:** 15\n- **UE Version:** UE 4.0+ (World Partition streaming UE5.0+)\n- **Tags:** level-streaming, narrative, blueprint, pipeline\n- **Summary:** Comprehensive Epic docs on Level Streaming - async-loading and unloading sub-levels at runtime for multi-scene narrative projects. Covers Sub-Level Streaming setup (Load Stream Level / Unload Stream Level Blueprint nodes), World Partition cell-based streaming, Sequencer Level Visibility track, and streaming for cinematics via World Partition Streaming Source. Essential for multi-scene film projects. Practical patterns in `references/narrative-blueprints.md`.\n- **File:** tutorials/level-streaming-in-unreal-engine.md\n- **Also see:** `references/narrative-blueprints.md` (practical streaming + cinematic trigger patterns)"
replacements.append((old4, new4))

# 5. MetaSounds in Unreal Engine
old5 = "### MetaSounds in Unreal Engine\n- **Source:** Epic Documentation\n- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-in-unreal-engine\n- **Pages:** 19\n- **UE Version:** [PENDING]\n- **Tags:** [PENDING]\n- **Summary:** [PENDING EXTRACTION]\n- **File:** tutorials/metasounds-in-unreal-engine.md"
new5 = "### MetaSounds in Unreal Engine (Epic Documentation)\n- **Source:** Epic Documentation\n- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-in-unreal-engine\n- **Pages:** 19\n- **UE Version:** UE 5.0+\n- **Tags:** audio, metasounds, soundscape, blueprint, narrative, cinematics\n- **Summary:** 19-page Epic documentation on MetaSounds - UE5's node-based procedural audio DSP engine. Covers MetaSound Source vs Patch vs Preset architecture, sample-accurate trigger system, Wave Player node, output formats, Presets, graph composition, and Blueprint integration via Execute Trigger Parameter. Includes Sequencer audio track integration, procedural music patterns, and dialogue trigger workflows. UE5.8 additions: MetaSound Pages, Audio Subtitles, Control Bus tracks, WASAPI.\n- **File:** tutorials/metasounds-in-unreal-engine.md\n- **Also see:** `references/audio-metasounds.md` (quick reference + cinematic patterns)"
replacements.append((old5, new5))

# 6. Control Rig in Unreal Engine
old6 = "### Control Rig in Unreal Engine\n- **Source:** Epic Documentation\n- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-unreal-engine\n- **Pages:** 93\n- **UE Version:** [PENDING]\n- **Tags:** [PENDING]\n- **Summary:** [PENDING EXTRACTION]\n- **File:** tutorials/control-rig-in-unreal-engine.md"
new6 = "### Control Rig in Unreal Engine (Epic Documentation)\n- **Source:** Epic Documentation\n- **URL:** https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-unreal-engine\n- **Pages:** 93\n- **UE Version:** UE 4.26+ (Modular CR prod-ready UE5.6+)\n- **Tags:** animation, rigging, control-rig, mocap, metahuman, blueprint, cinematics\n- **Summary:** 93-page comprehensive Epic docs on Control Rig - UE5's node-based procedural rigging system. Covers Control Rig types (Full CR vs Modular CR vs FK), Modular Control Rig module library (IK/FK/Spine/Head/Leg/Arm), mocap cleanup workflow with additive Animation Layers, retargeting via IK Retargeter, and Control Rig in Sequencer. UE5.8 additions: Control Rig Dynamics (cosmetic physics, 5x faster), Control Rig Physics Beta, Direct Mesh Controls, RigMapper, Foot Definition, Skeletal Editor blendshape tools.\n- **File:** tutorials/control-rig-in-unreal-engine.md\n- **Also see:** `references/control-rig-animation.md` (quick reference + mocap cleanup patterns)"
replacements.append((old6, new6))

# Apply text replacements
new_idx = idx
for old, new in replacements:
    if old in new_idx:
        new_idx = new_idx.replace(old, new)
        print(f"Fixed: {old[:55].strip()}")
    else:
        print(f"NOT FOUND: {old[:55].strip()}")

# 7. Remove duplicate lipsync-in-unreal-engine entry
pos = new_idx.find('\n### lipsync-in-unreal-engine\n')
if pos >= 0:
    next_section = new_idx.find('\n### ', pos + 5)
    if next_section >= 0:
        old_dup = new_idx[pos:next_section]
        new_idx = new_idx[:pos] + new_idx[next_section:]
        print("Removed duplicate lipsync-in-unreal-engine entry")
    else:
        print("Could not find end of duplicate lipsync entry")
else:
    print("Duplicate lipsync entry not found (may already be removed)")

# Write back
with open('tutorials/INDEX.md', 'w', encoding='utf-8-sig', newline='\r\n') as f:
    f.write(new_idx)
print("Done writing INDEX.md")
