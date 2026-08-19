---
class: topic-reference
verified: no
sources: []
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# nDisplay & In-Camera VFX — Reference

nDisplay is UE's multi-display/multi-PC synchronized rendering system for LED walls, projection arrays, and CAVE environments.

## Quick Concepts

| Term | Meaning |
|------|---------|
| **Primary Node** | Master PC — drives all secondaries, accepts VRPN/Live Link input |
| **Secondary Node** | Rendering PC — connects to primary at startup |
| **Cluster Node** | One UE instance; one or more per PC |
| **Config Asset** | `.ndisplay`/`.uasset` — defines the entire cluster topology |
| **nDisplay Root Actor** | Level actor for in-editor preview; not required at runtime |
| **Viewport** | Rendered area = Display/Screen/Mesh + View Origin + Projection Policy |
| **Switchboard** | Python app for remote deployment — starts/syncs/records across cluster PCs |
| **SwitchboardListener** | TCP server on each cluster PC (port default 2980) |
| **ICVFX Camera** | Cine Camera Component that generates the LED inner frustum |
| **Outer Frustum** | The rest of the LED wall surrounding the inner frustum |
| **Projection Policy** | How 3D scene maps to display surface (planar, mesh, MPCDI, VIOSO) |

---

## Default Network Ports

| Port | Purpose |
|------|---------|
| 41001 | Cluster Sync |
| 41002 | Render Sync |
| 41003 | JSON Cluster Events |
| 41004 | Binary Cluster Events |

Change in: Cluster Details panel → Network/Port settings.

---

## Cluster Network Settings

| Parameter | Default | Notes |
|-----------|---------|-------|
| `Connect Retries Amount` | 300 | Attempts before secondary shuts down |
| `Connect Retry Delay` | 1000ms | Wait between retries |
| `Game Start Barrier Timeout` | 18000000ms | Wait for all nodes before first frame |
| `Frame Start Barrier Timeout` | 30000ms | Per-frame game thread sync |
| `Render Sync Barrier Timeout` | 1800000ms | Render thread per-frame sync |

---

## 3D Config Editor Panels

### Components Panel
Add these to the Root Component:
| Component | Use |
|-----------|-----|
| Screen Component | Flat 2D display — defines frustum with View Origin |
| Static Mesh Component | Curved/non-flat display (LED walls) |
| Xform | Named 3D transform; parent for screens/cameras |
| View Origin | Origin point for viewport frustum; has stereo settings |
| ICVFX Camera | Inner frustum camera for in-camera VFX |
| Live Link Component | VRPN/spatial tracking input |

### Cluster Panel
| Element | Description |
|---------|-------------|
| Cluster | Top-level container — one per Config Asset |
| Host | PC with unique IP address |
| Node | UE application instance on that host |
| Viewport | 3D window → assign Display, View Origin, Projection Policy |

### Output Mapping Panel
- Maps Viewports into the 2D application window
- Supports rotate, flip, scale, edge snap operations
- Use NVIDIA Mosaic / AMD Eyefinity for multi-output aggregation

---

## ICVFX Workflow (LED Volume)

```
1. Enable nDisplay plugin + create Config Asset from nDisplay template
2. Config Asset → Components: add ICVFX Camera, Screens for outer frustum, Static Mesh for LED wall
3. Set GPU Index on ICVFX Camera → GPU 1 (second GPU for inner frustum)
4. Set View Origin for outer frustum tracking
5. Add Live Link Component → connect VRPN tracker
6. Deploy with Switchboard:
   a. Launch SwitchboardListener on every PC
   b. Open Switchboard → Add nDisplay Device → browse Config Asset
   c. Set correct IP addresses (not 127.0.0.1 if multi-machine)
   d. Click Connect → Start Unreal
```

---

## Multi-GPU Setup

```
// In Config Asset:
Configuration Render Frame Settings → Multi GPU Mode → Enabled

// Per viewport:
3D Config Editor → select Viewport → Details → GPUIndex = 0 (main GPU)

// Inner frustum (ICVFX Camera):
3D Config Editor → select ICVFX Camera → Details → GPUIndex = 1

// Switchboard: nDisplay node settings → Number of GPUs = 2
```
NVIDIA NVLink: direct GPU-GPU memory transfer (faster). Without NVLink: P2P over PCIe.

---

## Failover

```
// Enable: 3D Config Editor → Cluster Details → Failover Policy → "Drop S-node on fail"
// When a secondary node becomes unresponsive, it's dropped from the cluster
// Timeout values set in Network settings (Render Sync Barrier Timeout)
```

---

## Projection Policies (Extending nDisplay in C++)

| Class | Purpose |
|-------|---------|
| `DisplayClusterProjectionPolicy` | Custom projection math (dome, curved, MPCDI) |
| `DisplayClusterRenderingDevice` | Extends IStereoRendering |
| `DisplayClusterPostProcess` | Six callbacks for viewport post-processing |
| `DisplayClusterRenderSyncPolicy` | Custom sync (nvSwapLock, vSync, skip-frame) |

Supported third-party: Scalable Display, VIOSO, DomeProjection, MPCDI.

---

## Switchboard Features

| Feature | Notes |
|---------|-------|
| Start UE remotely | Launch nDisplay instances on all nodes |
| Take Recording | Embedded TakeRecorder via OSC; VP Roles required |
| P4 Sync + Build | Sync changelists and build across devices |
| nDisplay Monitor | Per-node GPU/CPU/driver/sync status table |
| Console Commands | Send to all nodes: `stat fps`, `r.RayTracing.SceneCaptures 0` |

**OSC setup for take recording:**
- Virtual Production Editor plugin → "Start an OSC Server when editor launches": ✓
- OSC Server Port = OSC Client Port in Switchboard Settings

---

## Adding nDisplay to Existing Project

```
1. Edit → Plugins → search "nDisplay" → Enable ✓
2. Edit → Project Settings → Plugins → nDisplay → Enable ✓
3. Restart editor → reopen project
4. Drag .ndisplay config into Content Browser (auto-converts to .uasset)
```

---

## Blueprint API

```
// Get nDisplay cluster management API:
[Create N Display DisplayCluster Module API]
    → Out API pin → Display Cluster category
        → GetClusterNodesIds()
        → GetClusterId()
        → SetDisplayClusterConfigPath()
        → Input device queries (VRPN)
        → Viewport rendering controls
```

---

## Useful Console Commands During nDisplay Session

```
stat fps                           -- frame rate on all nodes
r.RayTracing.SceneCaptures 0       -- disable RT for inner frustum captures
nDisplay.RenderSync.Policy 2       -- switch sync policy at runtime
nDisplay.Cluster.stats             -- per-node timing stats
```
