# Source Router Bundles

Public review table for `skill-sync` proposal-only source recommendations.
Machine-readable source is `source-bundles.json`.

Generated/checked: `2026-06-22`

## Bundles

| Bundle | ROS generations | Usage | Cache/Pull policy | Trigger examples | Recommended sources | Trust boundary |
|---|---|---|---|---|---|---|
| `robotics.ft_sensor` | non_ros, ros1, ros2 | current_implementation_baseline, framework_logic_reference, historical_context | index_only, never_clone_or_pull, pullable_if_future_cache_exists | `ati`, `bota`, `force torque`, `force-torque`, `ft sensor`, `f/t sensor`, `netft`, `robotiq` | ros2_control Force Torque Sensor Broadcaster; ATI Net F/T ROS driver; Bota FT Stack; SCHUNK force torque sensor ROS2 driver; Robotiq force torque ROS sources | Mixed ROS1/ROS2 bundle. Prefer official ROS2/vendor sources for current ROS2 work; keep ATI/Robotiq ROS1 legacy sources as framework/protocol reference only. Clone default is no-clone; future pullable candidates must be ROS2 and still require distro, hardware, license, and maintenance checks. |
| `robotics.signal_filtering` | non_ros, ros2 | current_implementation_baseline, offline_analysis | index_only, pullable_if_future_cache_exists | `butterworth`, `filter chain`, `filtering`, `force filter`, `low pass`, `low-pass`, `noise filtering`, `sensor filter` | ROS filters; ros2_control filter-chain integration; SciPy signal processing | Mixed ROS2/non-ROS bundle. Use ROS2 filters/ros2_control for deployed ROS2 runtime paths; use SciPy only for offline filter design and log analysis. Clone default is no-clone unless code-level inspection is required and target distro/package version is verified. |

## Source Classes

| Class | Meaning |
|---|---|
| `official_docs` | Vendor/project documentation, docs site, package index, or official README. |
| `official_repos` | Vendor/project-maintainer repo or org. |
| `major_org_repos` | Large ecosystem orgs that are useful but not vendor official. |
| `community_repos` | Individual or small-group repos useful for discovery but not a default authority source. |
