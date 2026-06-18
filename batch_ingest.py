"""
Batch ingest script for Unreal Sidekick skill.
Runs ingest.py on each URL sequentially, logging progress and errors.
Usage: python batch_ingest.py
"""
import subprocess
import sys
import os
import json
from datetime import datetime

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
INGEST_PY  = os.path.join(SKILL_DIR, "ingest.py")
LOG_FILE   = os.path.join(SKILL_DIR, "batch_ingest_log.json")

# Already-ingested URLs (skip these)
ALREADY_DONE = {
    "https://www.youtube.com/watch?v=771myWapQ_s",  # Green Screen Media Plate
}

# ── BOUNDLESS ENTERTAINMENT FILMS (Light Forge / Gemini / Cinematic VFX) ──────
BOUNDLESS = [
    ("z9t4XIoNsHY", "3D Tracking Natively in Unreal Engine - FULL TUTORIAL"),
    ("uMJXtDJf6VQ", "I BUILT The Camera Tracking Tool I Always Wished Unreal Had"),
    ("Zy5A6bDz9xw", "Unreal Engine's Secret Weapon for Cinematic Lighting"),
    ("YqPy2yM7X-s", "The Simplest Rendering Trick 90% of Unreal Artists Miss"),
    ("dF_W-9OBjus", "The Ultimate Plugin for Filmmaking in Unreal Engine"),
    ("f4izPHpbfZI", "How to Render Chaos Cloth Simulations with Motion Blur [The RIGHT Way]"),
    ("rUZxS3IwZhQ", "5 VFX Techniques You've Been Taught that are Actually Wrong"),
    ("YhJGuB5fCfU", "Unlock Thousands of Free Assets in Unreal Engine"),
    ("j3Kq0TIR2SI", "No Cost Virtual Production is Here - And it's Changing Filmmaking"),
    ("oGZJ4PcKqBE", "These Simple Mistakes are RUINING your VFX"),
    ("oSux_qv3dzs", "The 5 Secrets to Hollywood-Level Visual Effects With No Budget"),
    ("BW0oesmih9I", "Unreal Engine 5.4 Cinematic PREVIS Course"),
    ("SstexNmLc68", "How Unreal Engine is Changing Filmmaking Forever"),
    ("dZmnDDSNUEY", "BEST SETTINGS for Unreal Engine 5.6 - PERFECT Renders Every Time"),
    ("o5ZInDwU73I", "How to Make Your Unreal Engine Renders Look REAL"),
    ("BCWThDhzImI", "FASTEST Way to Optimize Unreal Engine 5.6 for Cinematic Renders - Path Tracer Pro"),
    ("RfTVeIwB2Dw", "Unreal Engine 5.7 Filmmaking Course - Unreal Engine for Filmmakers (2026 UPDATE!)"),
    ("6w8cEVgikrg", "Why Modern VFX DON'T Suck - Low Budget Virtual Production"),
    ("OvvtTYB46b8", "Unreal Engine 5 Compositing Tutorial - Composite Any Scene Fully Inside of UE5"),
    ("zOcXC-imA5U", "Why Modern VFX Suck (And How to Make Yours Not Suck) PART 2"),
    ("qPVS75PM5eU", "Why Modern VFX Suck (And How to Make Yours Not Suck)"),
    ("5zJktaYwK-I", "Unreal Engine for Filmmakers - Cinematic VFX for FREE - UE5 [PART 2]"),
    ("Yl_VJqmll-E", "Unreal Engine for Filmmakers - Add Cinematic VFX to your Films for FREE - UE5 [PART 1]"),
    ("SMCTeoj9YaA", "Unreal Engine for Filmmakers - How to Make your Lighting CINEMATIC"),
    ("mGcyo5rh7l0", "FREE Unreal Engine 5.3 Beginner Course - Create Cinematic 3D Worlds"),
    ("_K8qfjcYbmE", "Unreal Engine Filmmaking COURSE - Create Cinematic 3D Worlds"),
    ("39nmue2lIdA", "Unreal Engine Compositing Tutorial - UNREAL ENGINE FOR FILMMAKERS"),
    ("gzdYccMYjak", "Unreal Engine for Filmmakers - Incredible Realtime Particle Simulations for Free"),
    ("gFO0qhdLKec", "Unreal Engine for Filmmakers - Cinematic Camera Settings & Setting up Virtual Camera"),
    ("0ltfUCHwevY", "Unreal Engine Depth Fog TUTORIAL [Path Traced]"),
    ("ibAyJjNbnpo", "DUNE Cinematography Breakdown | HOW TO GET THE DUNE LOOK"),
    ("IUkD87VSmyg", "Unreal Engine for Filmmakers - Create Cinematic 3D Worlds for Free"),
    ("g8aHQqbQfOU", "Easiest Way to Get CINEMATIC Renders in UNREAL ENGINE - Path Tracing"),
    ("S8nDuuIucCc", "Roger Deakins Lighting Tutorial - BLADE RUNNER 2049"),
    ("v38O-9KTqx4", "3D TRACKED CAMERA FROM AFTER EFFECTS TO UNREAL ENGINE | TUTORIAL"),
]

# ── BLACK EYE CAMERAS V2 ───────────────────────────────────────────────────────
BLACKEYE = [
    ("vs6yjL-l_FQ", "Unreal Engine Black Eye Cameras v2: START HERE Tutorial"),
    ("SbFbNYrBO7s", "Unreal Engine Black Eye Cameras v2: Gameplay cameras are here"),
    ("U5FGuo59IJc", "Unreal Engine Black Eye cameras: Behind the Lens"),
    ("vKG_qFXKcyY", "Unreal Engine Black Eye cameras: Dynamic Dialog intro"),
    ("MFrmcgQHGJk", "Unreal Engine Black Eye Cameras for Gameplay: Top Down"),
    ("Wh-QAH49C70", "Unreal Engine Black Eye Cameras: Car camera INTRO"),
    ("4X16gnNVD1E", "Unreal Engine Black Eye Cameras: Car Cameras! Gameplay and Cinematics"),
    ("3KxVyOQwTRo", "Unreal Engine Black Eye Cameras | START HERE Tutorial"),
    ("2MeieZV_A1E", "Unreal Engine Black Eye Cameras: Speed of Thought"),
    ("NOOpWzeC0Mg", "Unreal Engine Black Eye Cameras: That's a Cool Shot #1 Pedestal Pan"),
    ("w2CBsFWMUys", "Unreal Engine Black Eye Cameras: V1.2 Preview Shot List module"),
    ("sda3K-M2j0g", "Unreal Engine Black Eye Cameras: Your Cinematics, Reinvented"),
    ("oZ_0JPrN-hE", "Unreal Engine Black Eye Cameras: Look Around Tutorial"),
    ("ub1_ET0LLJc", "Unreal Engine Black Eye Cameras: Cam Switcher Tutorial"),
    ("ctm38XzfzIo", "Unreal Engine Black Eye Cameras: v1.1.7 Switcher + Pilot"),
    ("rw5OmVtBri8", "Unreal Engine Black Eye Cameras: Unleash Your Army of Camera Operators"),
    ("WNkFghUIA7M", "Unreal Engine Black Eye Cameras: Supercharge your workflow"),
    ("7jNy5snGOJM", "Unreal Engine Black Eye Cameras: Crazy Millennium Falcon shot with only 7 keyframes"),
    ("94UWBG7hKDI", "Unreal Engine Black Eye Cameras: Version 1.1.1: Keyable Weights in Sequencer"),
    ("uUxE0gaOvnQ", "Unreal Engine Black Eye Cameras: Version 1.1 New Features: Cross Camera"),
    ("WBgBhPjzzbI", "Unreal Engine Black Eye Cameras: Version 1.1 New Features: Multi_Subject LookAt Weights"),
    ("D_CrTaBzEa4", "Unreal Engine Black Eye Cameras: Bake down cam anims"),
    ("JGnNpbWiT_0", "Unreal Engine Black Eye Cameras: Overview Tutorial"),
    ("VADulk2Gao4", "Unreal Engine Black Eye Cameras: Change Anims"),
    ("jhNjKV70uzk", "Unreal Engine | Black Eye Cameras: Rapid shot prototyping"),
    ("oYYxZc2jO2c", "Unreal Engine Black Eye Cameras: Follow Component: Dwell Radius"),
    ("W4UZ4-vLxxw", "Unreal Engine | Black Eye Cameras: 2 person combat side camera tutorial"),
    ("hcd3Ohyjr_E", "Unreal Engine Black Eye Cameras: November release"),
    ("x18zbUJoI9U", "Unreal Engine Black Eye Cameras: Multiple targets on a character"),
    ("lzFH7Peyyk0", "Unreal Engine Black Eye Cameras: Multiple follow and look at modules"),
]

# ── POLYGONFLOW DASH ───────────────────────────────────────────────────────────
POLYGONFLOW = [
    ("MwjUZJ7qkIk", "NEW UE5 ASSET MANAGEMENT PLUGIN - NOW FREE ON FAB"),
    ("bmxYrlidcCM", "DASH 1.11 - UNREAL ENGINE WORLD BUILDING JUST GOT EASIER"),
    ("HL8NDvv1G44", "How to Create a Cinematic Archviz Render with UE5 & Dash"),
    ("EN6X-d6DIb0", "DASH 1.10 - PROCEDURAL SCATTER PRESETS IN UE5"),
    ("GLOQdCQonOg", "Creating a Massive Procedural Game World in UE5 with Dash"),
    ("YHmNyyI998k", "DASH 1.9.3 - NEW UE5 ASSET MARKETPLACE"),
    ("bxeocONsu1Y", "UE5 WORLD BUILDING FOR BEGINNERS - FULL DASH DEMO LEVEL"),
    ("XNac5ylJ5LQ", "DASH 1.9.2 - NEW UE5 TOOLS + AMAZON 3D LIBRARY INTEGRATION"),
    ("qxXQsMCMWfw", "Unreal Engine 5.6 Physics Tools - Asset Placement & Piles Tutorial"),
    ("KsgW-19y4ts", "PROCEDURAL WORLD BUILDING FOR UE5 - PCG ALTERNATIVE"),
    ("_SKfQJ5pAAc", "Unreal Engine & Dash Medieval Environment Tutorial"),
    ("rjTv9jWfY4s", "CENTRALIZED CONTENT BROWSER FOR UE5 - FREE PLUGIN"),
    ("HXyU7Z_Hz_U", "2000 FREE HIGH-QUALITY ASSETS FOR ANY UNREAL ENGINE PROJECT"),
    ("I58cCdLiVF4", "Auto-Tag & Sort 1000 UE5 Assets/Month with This FREE Content Browser"),
    ("bsy4xZvhOqs", "BEST FREE UNREAL ENGINE 5 ASSET MANAGEMENT PLUGIN IN 2025"),
    ("tOpExldNzoA", "DASH 1.9 - MANAGING ASSETS IN UE5 JUST GOT A LOT EASIER"),
    ("rdXL5PtsGnY", "Working Fully Procedurally in Unreal Engine 5 - Custom Asset Tutorial"),
    ("lHZwUtS6hyE", "DASH 1.8.5 - BIG UPDATE FOR UE5 WORLD BUILDING"),
    ("Y_Ja4n3RSf0", "How to Create Vines Procedurally in Unreal Engine 5"),
    ("MoAk8c1ek7A", "Creating a Blend Material in Unreal Engine 5 Just Got Easier"),
    ("RA3yGbCvxIU", "GETTING STARTED WITH DASH - EASY WORLD BUILDING IN UE5"),
    ("s-UQxXkHt8k", "Making Asset Importing Easy in UE5 - Dash Content Browser"),
    ("B6T_VQQK6OU", "DASH 1.7.0 - MASSIVE UE5 WORLD BUILDING TOOL"),
    ("kJhqc5_6usc", "Creating a Helldivers 2 Environment in 79 minutes - UE5 Tutorial"),
    ("plpGMR46HnE", "Recreating a Helldivers 2 Game Environment in UE5 with Dash"),
    ("rBcGl_ScDKs", "How to create a training environment in Unreal Engine 5 - Dash Workflow"),
    ("5aTwhjR5JJE", "How to Re-Create The Walking Dead in Unreal Engine 5 - Dash Workflow"),
    ("N7XLl348vG4", "Architecture Scenes Made Easy in Unreal Engine 5 - Dash Tutorial"),
    ("6U2jbJmqs4k", "No Nodes Procedural Environment in Unreal Engine 5 - Dash Tutorial"),
    ("li914x1WPis", "Dash 1.6.0 Release - Improved Content Library and AI Asset Tagging"),
    ("EezUW6MSqfE", "This Plugin Makes Unreal Engine 5 Even More Amazing - Dash for World Building"),
    ("_9b_dabCpVE", "Realistic Architecture Environment in UE5 - Dash Workflow"),
    ("IU8VFAXOa7w", "How to Scatter Decals in UE5 - World Building Plugin"),
    ("uNzCmzeEISU", "How to Create Procedural Cables in UE5 - World Building Plugin"),
    ("fvlPj3hYgSI", "Dash for UE5 Helps You Organize Your Local 3D Assets with AI Tagging"),
    ("7NKl90gt0w0", "How to Edit Megascans and Poly Haven Materials Easily - UE5 Plugin"),
    ("mYe43x2Dtg0", "What's new in Dash 1.5 - AI Content Tagging, Tool Presets, & More"),
    ("UO2ehs5OjEw", "New UE5 Plugin - Adding Detail to Your Game with DASH"),
    ("i6GTbioHD4k", "Path Scatter: Beginner Guide to Your UE5 Co-Pilot, DASH"),
    ("cC0l3yZMt3M", "Speed Up Your Archviz Workflow with Dash in UE5"),
    ("D4IPvlypNkg", "Surface Scatter: Beginner Guide to Your UE5 Co-Pilot, DASH"),
    ("00kSXM3b788", "Beginner Guide to UE5 Co-Pilot DASH Camera Settings"),
    ("P90HaXlYSNE", "Create Realistic Scatter Using Merge Actors with Dash"),
    ("x6DR-CGi8dE", "Beginner Guide to Road Tool in UE5 Co-Pilot DASH"),
    ("lCicNo8MGNA", "New UE5 Plugin - Easy Environment Creation"),
    ("J0x7Krbgja4", "Beginner Content Library Tutorial for UE5"),
    ("N8kCskb3V1k", "Beginner Terrain Tool Tutorial for UE5"),
    ("oY4pVa6mPYM", "Beginner Water Tool Tutorial for UE5"),
    ("YfHdlxH22cM", "Quick Environment Creation w/ Unreal Engine 5"),
    ("zxVE6uyBEHs", "Environment Breakdown: Underground Horror in UE5"),
    ("hInAtC725VQ", "Tutorial: Create Subtle Realistic Environments in UE5"),
    ("NNBDLTPsktc", "Create Run-down Environments in Minutes - Dash & UE5"),
    ("_7HfCCLiSec", "Simplify Environment Art Creation In Unreal Engine 5"),
    ("pWEnE86hZrM", "New Physics Tool for Unreal Engine 5"),
    ("NVSEN3ND6VU", "Introducing Dash for Unreal Engine 5"),
]

# ── CHARLIE DRISCOLL FILM (Mocap / OverCrowd / MetaHumans / AI Animation) ────
CHARLIEDRISCOLL = [
    ("wys5jEhtpY0", "How to Get PRO Motion Capture for MetaHumans on a Budget in Unreal Engine 5"),
    ("NLVMJX-5ahc", "Can AI Replace MetaHumans in Unreal Engine Cinematics?"),
    ("2t3c1KJbBe8", "Recreating BRUTAL Deaths from History in Unreal Engine 5"),
    ("M799eoMK4tw", "The EASIEST and CHEAPEST Motion Capture Setup for Metahumans in Unreal Engine 5.6 (No Headrig)"),
    ("5j6wwCsWpD0", "How to Generate Custom Metahuman Bodies with AI - YVO3D, Faceform Wrap, 2DNAX - Unreal Engine 5"),
    ("PEObW2odtXI", "How to Generate Custom Metahuman Creatures with AI - YVO3D, Faceform Wrap, Unreal Engine 5.6 - Part I"),
    ("h5QzOjs8418", "The best real-time mocap I have ever seen - Captury, Captive Devices, and Metahuman Animator - UE5"),
    ("1BcKEd9UO9k", "How to Create MASSIVE Crowds and Battle Scenes in Unreal Engine 5 - Niagara and OverCrowd"),
    ("y-6aiWvh_GY", "How I created a MASSIVE crowd of Metahumans for a BRUTAL Gladiator film - Unreal Engine 5, OverCrowd"),
    ("ukk4vw-bIpA", "Motion Capture Sword Fighting Cinematic in Unreal Engine 5 - Move.AI and Metahumans"),
    ("aO_ceeiGHuw", "Cinematography Deepdive for Beginners - Camera and Render Settings Tutorial - Unreal Engine 5.5"),
    ("26c4TVIYZ8k", "How to create a fight scene cinematic in Unreal Engine 5.5"),
    ("h6FEW4Kz_Kk", "How to Create A Massive Zombie Horde in Unreal Engine 5.5 - Niagara Crowd Simulation, AnimToTexture"),
    ("i2W2rDsZXk4", "Budget Mocap Tutorial - Quickmagic.AI and Metahuman Animator (Android/Frame Mancer) Unreal Engine 5"),
    ("7xYyfWeAHiA", "Cheap AI Mocap that Actually Works - QuickMagic.Ai, Chaos Destruction, and Metahumans in UE5"),
    ("LpRGFkk3b0k", "How I made this AAA Cinematic in Unreal Engine 5 - Move.Ai and Metahuman Animator short film"),
    ("ova-8EAD8eg", "How to Create the ULTIMATE Previz with Polycam, Metahumans, and Move.AI in Unreal Engine 5"),
    ("P2eR9gGPZnA", "How I made this AAA battle scene in Unreal Engine 5"),
    ("Fp3P0tSnY-Y", "Cinematic Motion Capture with Move One and Metahuman Animator - Unreal Engine 5.4 Beginner Tutorial"),
    ("I3GzRdnFEIw", "Move.AI and Unreal Engine 5 Metahuman Short Film - GIGANTIC JOE"),
    ("-GQWj_20J0g", "How I Use Move.AI and Metahumans to Achieve AAA Character Animation in Unreal Engine 5"),
    ("pq5iEvcntwE", "Move.AI and Unreal Engine 5 Metahuman Cinematic - HACKER"),
    ("iRPYgNrF8BY", "Orc vs. Knight CGI Swordfight - UE5"),
    ("v75dSep_kbE", "Move.AI Unreal Engine 5.4 Motion Capture Short Film Using Custom Orc Metahumans - ENCOUNTER"),
    ("PYTu-rLyPro", "William Wallace - Move.AI and Metahuman short film in Unreal Engine 5"),
]

# ── DEAN YURKE (DaVinci / Unreal / Virtual Production) ───────────────────────
DEANYURKE = [
    ("t7Q1UiBr8e8", "Green Screen Edge Wrap SECRETS (and a LIE!) - Advanced DaVinci to Unreal Engine WORKFLOW"),
    ("0YhVHCoHKkg", "Burn Clip Names onto DaVinci Resolve and FUSION Video (Quick Fusion Tip!)"),
    ("qe2x-puqVl0", "Green Screen OVERSCAN SECRETS (and a LIE!) - Your Ultimate VFX Save! (SERIES BONUS)"),
    ("PPRugNC7POA", "Make Films in Unreal : Everything you need to create your first short (Beginner) Start Here (ep1)"),
    ("XeeIY_fvbq0", "Scale Unreal Engine's User Interface! SQUINT no more! Great for recording UE5 tutorials too!"),
    ("-9-Aq3z-wI4", "UE5 Filmmaking Series | xdus | Animatic to Teaser - Real-Time Micro Budget Movies"),
    ("9-kRF6DFfPE", "A.I. / Real-Time and Surviving Hollywood's VFX industry for 30 years"),
    ("g9VndiQqON0", "How to get precision control in DaVinci Resolve - use Shift Drag!"),
    ("ye0gjAx50oU", "Beat Yourself up with Unreal! RAGDOLL Physics for Filmmaking made Easy (or Hard) in UE5.6!"),
    ("JxHYt9vFQD8", "Motion Blending / Bone Matching for Unreal Engine - Make Films in Unreal : (ep2) (Intermediate)"),
    ("rzMRSDxg33Q", "Unreal Engine VFX Breakdown - Ragdoll Opening Shot"),
    ("6he5ag3nLjs", "EASIEST VFX pipeline EVER with Composite Mesh Actors in Unreal Engine 5.7 (Composure EP1)"),
    ("VbLziZfiyD8", "Green Screen Cards are DEAD! Camera Projections in Unreal Engine change EVERYTHING! (Composure EP2)"),
    ("zlZCKT-5pLU", "Green Screen Integration in Unreal Engine 5.7 Virtual Production got even BETTER! (Composure EP3)"),
    ("xbZNHZ-QGyg", "Advanced Volumetric FOG SECRETS in Unreal Engine 5.7 [Full Course]"),
    ("Wb9hJqPcAwQ", "How to Transform TEXTURE COORDINATES in Unreal Engine Materials (Tutorial)"),
    ("o_AE2kUsF3E", "Faster than AI and 7 times the fun! Speed up Animation and get exactly what you want with Rokoko"),
    ("5cpjK7kKASU", "Unreal Engine Virtual Production: Trigger Explosions and Sound Effects with your Keyboard (Tutorial)"),
    ("1kcelYQLkP0", "Survive the VFX War: Battle-Ready skills you need for Virtual Production in 2026 (NCSU MADtech Q&A)"),
    ("ivE8Bg0EaBo", "How to use the Movie Render Graph in Unreal Engine 5.8 - Simple Setup for Filmmakers."),
    ("H3OfTUhMmmc", "Create SPECTACULAR Depth of Field in Unreal Engine 5.8 with the new ACCUMULATION DOF"),
    ("WenSYKg08Uc", "Where are my Animation Curves!? This MYSTERIOUS SYMBOL will save you HOURS of Frustration!"),
]

# ── JOSH TOONEN (@JoshToonen) — UE tutorials/breakdowns ──────────────────────
JOSHTOONEN = [
    ("N4hq0WUaPmk", "How I Remade the BACKROOMS using VFX"),
    ("g4DIDafH4lM", "every filmmaker should know this VFX workflow"),
    ("eOQM1Tbyw0Y", "How this Unreal Engine 5 film won an Oscar"),
    ("TufXrvN5Ei0", "Recreate the LEGO MOVIE Style in Unreal Engine 5"),
    ("AomczYcvBYM", "How I Made this LEGO Horizon animation in Unreal Engine 5"),
    ("BG_zYneV3mo", "Give me 14 minutes and you'll make cinematic renders"),
    ("hoCoa8gMP-M", "Motion Capture isn't just for Hollywood any more"),
    ("7ENEextL1n8", "Ragdoll Physics are Insanely Easy in Unreal 5"),
    ("ncjHJQPyzto", "How to Make Blade Runner in Unreal 5 (Step-by-step)"),
    ("CneRhBFaLjM", "How to Animate Spider-Man in Unreal Engine 5 (for Beginners)"),
    ("hFM_jGd46as", "Improve Your VFX with Lens Flares (Anamorphic Tutorial)"),
    ("LUoUVC5tXCo", "This Free Plugin Changes Filmmaking Forever [Unreal 5]"),
    ("OLwLqjBtSKk", "Unreal 5 Animation Made Easy! [FREE DOWNLOAD]"),
    ("wFhZxRJZN8E", "Create MUZZLE FLASH Gun FX for Unreal 5 Cinematics"),
    ("Og9za5-VCag", "How I Made a Godzilla Cinematic in Unreal Engine 5"),
    ("NiOgmvMBcxk", "How Unreal 5.4 Changes Filmmaking"),
    ("Qun6BB6Q2tg", "How to ACTUALLY Improve Your Films + VFX (Dune in Unreal 5)"),
    ("-syj6kFf6e4", "How I Remade Dune in 24 Hours using VFX"),
    ("HU7qHi6bn9A", "Unreal 5 Hotkeys Every Filmmaker Must Use"),
    ("0Yc6qJSWet4", "Unreal 5 Secrets Every Filmmaker Must Know"),
    ("56RMmZlDVw4", "The Future of Filmmaking in Unreal 5 (Virtual Production)"),
    ("Cp7sWfiHcJg", "How to Create Cinematic Environments in Unreal Engine 5"),
    ("ixnoglWzwBw", "How to Make a Samurai Film in Unreal 5"),
    ("dT4Vl3PGe08", "The Fastest Way to Learn Lighting in UE5"),
    ("jAz4Lb93gwY", "The #1 Skill You NEED For Lighting in UE5"),
    ("Kjg6kCW2BtY", "Master Cinematic Fog & Volumetric God Rays in UE5"),
    ("4-_mXW1Vwuo", "Unreal Engine Masterclass: Animate Environments The Easy Way"),
    ("VIY1fzRahJY", "How UE5 Created the Most Realistic Game Ever - Unrecord Trailer Breakdown"),
    ("MWFpt3ZQ0zE", "Create a Lightsaber Battle in Unreal 5 (in 10 minutes!)"),
    ("9rRiExTYrpE", "Learning Unreal 5 in One Year (Progression + Lessons)"),
    ("_3PQ19-LMRg", "How We Made The Last of Us: Stay (VFX Breakdown)"),
]

ALL_VIDEOS = (
    [("boundless",        vid_id, title) for vid_id, title in BOUNDLESS]
  + [("blackeye",         vid_id, title) for vid_id, title in BLACKEYE]
  + [("polygonflow",      vid_id, title) for vid_id, title in POLYGONFLOW]
  + [("charliedriscoll",  vid_id, title) for vid_id, title in CHARLIEDRISCOLL]
  + [("deanyurke",        vid_id, title) for vid_id, title in DEANYURKE]
  + [("joshtoonen",       vid_id, title) for vid_id, title in JOSHTOONEN]
)

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            return json.load(f)
    return {}

def save_log(log):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)

def run_ingest(vid_id, title):
    url = "https://www.youtube.com/watch?v=" + vid_id
    print(f"\n{'='*60}")
    print(f"Ingesting: {title}")
    print(f"URL: {url}")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
    print('='*60)
    result = subprocess.run(
        [sys.executable, INGEST_PY, url],
        cwd=SKILL_DIR,
        capture_output=False,
        text=True,
    )
    return result.returncode == 0

def main():
    log = load_log()
    total = len(ALL_VIDEOS)
    done  = sum(1 for _, vid_id, _ in ALL_VIDEOS if log.get(vid_id, {}).get("status") == "ok")
    print(f"Batch ingest: {total} videos total, {done} already done")

    for i, (channel, vid_id, title) in enumerate(ALL_VIDEOS, 1):
        url = "https://www.youtube.com/watch?v=" + vid_id
        if url in ALREADY_DONE:
            print(f"[{i}/{total}] SKIP (already ingested): {title}")
            continue
        entry = log.get(vid_id, {})
        if entry.get("status") == "ok":
            print(f"[{i}/{total}] SKIP (logged done): {title}")
            continue

        print(f"\n[{i}/{total}] [{channel}] {title}")
        success = run_ingest(vid_id, title)
        log[vid_id] = {
            "title": title,
            "channel": channel,
            "status": "ok" if success else "error",
            "timestamp": datetime.now().isoformat(),
        }
        save_log(log)

    ok    = sum(1 for v in log.values() if v.get("status") == "ok")
    error = sum(1 for v in log.values() if v.get("status") == "error")
    print(f"\n\nBatch complete: {ok} ok, {error} errors")
    if error:
        print("Failed videos:")
        for vid_id, v in log.items():
            if v.get("status") == "error":
                print(f"  {vid_id}: {v['title']}")

if __name__ == "__main__":
    main()
