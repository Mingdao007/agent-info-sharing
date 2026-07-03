# Source Router Bundles

Public review table for `skill-sync` proposal-only source recommendations.
Machine-readable source is `source-bundles.json`.

Generated/checked: `2026-07-03`

## Bundles

| Bundle | ROS generations | Usage | Cache/Pull policy | Trigger examples | Recommended sources | Trust boundary |
|---|---|---|---|---|---|---|
| `robotics.ft_sensor` | non_ros, ros1, ros2 | current_implementation_baseline, framework_logic_reference, historical_context | index_only, never_clone_or_pull, pullable_if_future_cache_exists | `ati`, `bota`, `force torque`, `force-torque`, `ft sensor`, `f/t sensor`, `actual_TCP_force`, `kunwei` | ros2_control Force Torque Sensor Broadcaster; ATI Net F/T ROS driver; Bota FT Stack; SCHUNK force torque sensor ROS2 driver; Robotiq force torque ROS sources | Mixed ROS1/ROS2 bundle. Prefer official ROS2/vendor sources for current ROS2 work; keep ATI/Robotiq ROS1 legacy sources as framework/protocol reference only. Clone default is no-clone; future pullable candidates must be ROS2 and still require distro, hardware, license, and maintenance checks. |
| `robotics.signal_filtering` | non_ros, ros2 | current_implementation_baseline, offline_analysis | index_only, pullable_if_future_cache_exists | `butterworth`, `filter chain`, `filtering`, `force filter`, `low pass`, `low-pass`, `noise filtering`, `sensor filter` | ROS filters; ros2_control filter-chain integration; SciPy signal processing | Mixed ROS2/non-ROS bundle. Use ROS2 filters/ros2_control for deployed ROS2 runtime paths; use SciPy only for offline filter design and log analysis. Clone default is no-clone unless code-level inspection is required and target distro/package version is verified. |
| `robotics.universal_robots_rtde_tp` | non_ros, ros2 | current_implementation_baseline, framework_logic_reference | index_only, pullable_if_future_cache_exists | `.urp`, `cachedcontents`, `installationrelativepath`, `polyscope`, `programs directory`, `rtde`, `rtde bridge`, `script node` | Universal Robots RTDE Guide; Universal Robots URScript documentation; Universal Robots Client Library | Vendor-official Universal Robots bundle. Use it to start RTDE/URScript/PolyScope package research, but local TP package delivery still requires local gate, upload, fetch-back, and SHA/read-back verification. |
| `robotics.universal_robots_ros2_control` | ros1, ros2 | current_implementation_baseline, framework_logic_reference | pullable_if_future_cache_exists | `controller_manager`, `external control urcap`, `forward_velocity_controller`, `headless ros2`, `ros2 control`, `scaled_joint_trajectory_controller`, `teach pendant mode`, `universal robots ros 2` | Universal Robots ROS 2 Driver; Universal Robots External Control URCap; ros2_control core | Official Universal Robots plus ros-controls bundle. Use for ROS2 control architecture and setup research; bench launch, TP Play, and motion remain separate UR10e live gates. |
| `robotics.rnn_jacobian_force_motion_control` | non_ros, ros2 | current_implementation_baseline, framework_logic_reference, offline_analysis | index_only, pullable_if_future_cache_exists | `damped least squares`, `dls solver`, `finite time convergence`, `force motion control`, `inverse kinematics`, `jacobian`, `jacobian velocity`, `jacobian rnn` | Pinocchio; OSQP; qpsolvers; Task Space Inverse Dynamics | Robotics theory/implementation source starting point. Use these for kinematics, QP, and task-space control references; paper-specific RNN, finite-time convergence, or force-control claims still require source-grounded literature review. |

## Source Classes

| Class | Meaning |
|---|---|
| `official_docs` | Vendor/project documentation, docs site, package index, or official README. |
| `official_repos` | Vendor/project-maintainer repo or org. |
| `major_org_repos` | Large ecosystem orgs that are useful but not vendor official. |
| `community_repos` | Individual or small-group repos useful for discovery but not a default authority source. |
