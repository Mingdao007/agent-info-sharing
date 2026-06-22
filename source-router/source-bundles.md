# Source Router Bundles

Public review table for `skill-sync` proposal-only source recommendations.
Machine-readable source is `source-bundles.json`.

Generated/checked: `2026-06-22`

## Bundles

| Bundle | Trigger examples | Recommended sources | Trust boundary |
|---|---|---|---|
| `robotics.ft_sensor` | `ati`, `bota`, `force torque`, `force-torque`, `ft sensor`, `f/t sensor`, `netft`, `robotiq` | ros2_control Force Torque Sensor Broadcaster; ATI Net F/T ROS driver; Bota FT Stack; SCHUNK force torque sensor ROS2 driver; Robotiq force torque ROS sources | Source recommendations are proposal-only; physical sensor setup still needs local electrical, transport, frame, calibration, and safety validation. |
| `robotics.signal_filtering` | `butterworth`, `filter chain`, `filtering`, `force filter`, `low pass`, `low-pass`, `noise filtering`, `sensor filter` | ROS filters; ros2_control filter-chain integration; SciPy signal processing | Prefer ROS runtime filter chains for deployed robot paths and SciPy for offline analysis or parameter design. |

## Source Classes

| Class | Meaning |
|---|---|
| `official_docs` | Vendor/project documentation, docs site, package index, or official README. |
| `official_repos` | Vendor/project-maintainer repo or org. |
| `major_org_repos` | Large ecosystem orgs that are useful but not vendor official. |
| `community_repos` | Individual or small-group repos useful for discovery but not a default authority source. |
