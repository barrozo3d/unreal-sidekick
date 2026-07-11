# William Faucher YouTube Tutorial Batch Ingestion
# Run from this skill's own directory (any machine)
# Usage: .\ingest_william_faucher.ps1

$ErrorActionPreference = "Continue"
$skillDir = $PSScriptRoot
Set-Location $skillDir

$videos = @(
    # Lighting fundamentals
    "https://www.youtube.com/watch?v=fSbBsXbjxPo",   # Lighting in UE5 for Beginners (44min)
    "https://www.youtube.com/watch?v=1e6oOiKh91U",   # Lumen Explained - IMPORTANT Tips for UE5
    "https://www.youtube.com/watch?v=CFKNoeUPQGQ",   # Things To Know About LUMEN
    "https://www.youtube.com/watch?v=BGoaPyfZlYg",   # Demystifying the Skylight
    "https://www.youtube.com/watch?v=SbxO-Z5rzwk",   # Tips for Sky Atmosphere & Fog
    "https://www.youtube.com/watch?v=yolGEIrhu0s",   # Volumetric Cloud Secrets
    "https://www.youtube.com/watch?v=0GYyHDuaPcg",   # Lighting Interiors in UE5
    "https://www.youtube.com/watch?v=1LfiYtKDsac",   # Lighting a NIGHT-TIME exterior
    "https://www.youtube.com/watch?v=hJohX8T5O-8",   # How To Improve Your Lighting w/ RTXGI
    # Rendering & Path Tracing
    "https://www.youtube.com/watch?v=X5zVhc5ahl0",   # PATH TRACER Explained (26min)
    "https://www.youtube.com/watch?v=P65cADzsP8Q",   # Nanite: Everything You Should Know
    "https://www.youtube.com/watch?v=fVg5ihB8Wdc",   # 2025 Guide to Rendering in UE5
    "https://www.youtube.com/watch?v=F3XSKXhIAuU",   # Fixing the Ugly Shadow Issues in UE5
    "https://www.youtube.com/watch?v=wTYM9TfckOQ",   # Fixing Common UE5 Issues
    "https://www.youtube.com/watch?v=RaY_FDaydoQ",   # Double Your Framerate - DLSS 3.0
    # Movie Render Queue / Pipeline
    "https://www.youtube.com/watch?v=FxvF3zncClA",   # Improve Renders with MRQ Part 1
    "https://www.youtube.com/watch?v=2U1wP8sJgfU",   # Improve Renders with MRQ Part 2
    "https://www.youtube.com/watch?v=ova8s1H-mUI",   # Render Passes with MRQ
    "https://www.youtube.com/watch?v=QUyznLlnchA",   # Stencil / Render Layers
    "https://www.youtube.com/watch?v=Ry4-Q8mBjdg",   # How to Render Cryptomatte
    "https://www.youtube.com/watch?v=lXcerW59onA",   # Fix the Broken First Frame in Sequencer
    "https://www.youtube.com/watch?v=hq1WFFF6iD0",   # Bake Lighting FASTER with GPU Lightmass
    # Color & Compositing Pipeline
    "https://www.youtube.com/watch?v=2Q3CybANHKE",   # 2026 UE to DaVinci Resolve Guide ACES
    "https://www.youtube.com/watch?v=Bo3BvhGdaUo",   # Unreal to DaVinci Resolve Workflow ACES
    "https://www.youtube.com/watch?v=cZTO4ojzX2g",   # Intro to UnrealReader - Nuke 13.2
    # Cinematics & Craft
    "https://www.youtube.com/watch?v=doUDJFKLyZs",   # How To Make Unreal Look More Cinematic
    "https://www.youtube.com/watch?v=HbGJyQVq3tk",   # How I Made This Shot in UE5
    "https://www.youtube.com/watch?v=8eIavj62Mu8"    # How to Add Camera Shake in UE5
)

$total = $videos.Count
Write-Host "Starting batch ingestion of $total William Faucher tutorials..."
Write-Host "Using --skip-video flag (transcript only)"
Write-Host "=" * 60

for ($i = 0; $i -lt $videos.Count; $i++) {
    $url = $videos[$i]
    $num = $i + 1
    Write-Host ""
    Write-Host "[$num/$total] $url"
    Write-Host "-" * 40

    python ingest.py $url --skip-video

    if ($LASTEXITCODE -ne 0) {
        Write-Host "WARNING: ingest.py returned exit code $LASTEXITCODE for $url"
    }

    Write-Host "[$num/$total] Done."

    # Small delay between ingests to be polite to YouTube
    if ($i -lt ($videos.Count - 1)) {
        Start-Sleep -Seconds 3
    }
}

Write-Host ""
Write-Host "=" * 60
Write-Host "Batch ingestion complete. $total videos processed."
Write-Host "Run extraction passes on the new tutorials/william-faucher-*.md files"
