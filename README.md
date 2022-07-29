<div align="center">
  <h1>OctoMap Server2</h1>
  <h3>Implementation of octomap for ROS2.0 </h3>
    <a href="https://travis-ci.com/iKrishneel/octomap_server2"><img src="https://travis-ci.com/iKrishneel/octomap_server2.svg?branch=master"></a>
</div>

Port of the ROS1 [octomap server](https://github.com/OctoMap/octomap_mapping) for ROS2.0 

```
# Install octomap
git clone https://github.com/OctoMap/octomap.git
cd octomap
mkdir build && cd build
cmake ..
make

#############################################################

# Set the built libraries in default path
cd /usr/lib/x86_64-linux-gnu/
mkdir octomap
sudo cp /PATH/TO/OCTOMAP/octomap/lib/cmake/octomap/* /usr/lib/x86_64-linux-gnu/octomap/.
sudo cp /PATH/TO/OCTOMAP/octomap/lib/liboctoma* /usr/lib/x86_64-linux-gnu/.

# Build raisin
mv src/octomap_* ../etc/.
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release

# Build octomap
sudo mv /usr/local/include/eigen3 ~/yunho/etc/.  # remove eigen3.4.0 which crashes with eigen 3.3.7 when building octomap
mv ../etc/octomap_* src/.
colcon build --packages-select octomap_msgs octomap_server2 --cmake-args -DCMAKE_BUILD_TYPE=Release
sudo mv ~/yunho/etc/eigen3/ /usr/local/include/.  # move back eigen3.4.0 to where it was

#############################################################

# Run octomap
rs-enumerate-devices -s  # Check whether all three cameras are connected. If not, plug the disconnected camera in a different usb port.

ros2 launch raisin_sensor_ros head_launch.py  # Launch depth cameras
ros2 launch raisin_sensor_ros t265_launch.py  # Launch pose estimation
ros2 launch octomap_server2 octomap_server_launch.py  # Launch octomapping
ros2 launch raisin_sensor_ros rviz_launch.py  # Launch rviz visualization (remote PC) (Not recommended because the mapping process will be slower. Recommend to visualize offline using rosbag.)

ros2 topic hz /raibo_head_pcl2
ros2 topic hz /camera/odom/sample
ros2 topic hz /occupied_cells_vis_array  # 5 ~ 20 in 0.05m resolution
```

#### Installation
Firstly make sure you have [octomap](https://github.com/OctoMap/octomap.git) installed on your system 

Next, clone this ros package to the appropriate ros2 workspace
```bash
$ git clone https://github.com/iKrishneel/octomap_server2.git
```
Clone the dependency repositories to the workspace
```bash
# will clone octomap_msgs to the workspace
$ vcs import . < deps.repos
```

#### Building
Use colcon to build the workspace
```bash
$ colcon build --symlink-install --packages-select octomap_msgs octomap_server2
```

#### Running
Launch the node with appropriate input on topic `cloud_in`
```bash
$ ros2 launch octomap_server2 octomap_server_launch.py
```
