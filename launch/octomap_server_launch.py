#!/usr/bin/env python

import os.path as osp

from launch import LaunchDescription, logging
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import \
    PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import ThisLaunchFileDir


def generate_launch_description():

    params = {'resolution': 0.05,
              'frame_id': 'camera_odom_frame', # map
              'base_frame_id': 'base',
              'height_map': False,
              'colored_map': False,
              'color_factor': 0.8,
              'filter_ground': False,
              'filter_speckles': False,
              'ground_filter/distance': 0.04,
              'ground_filter/angle': 0.15,
              'ground_filter/plane_distance': 0.07,
              'compress_map': True,
              'incremental_2D_projection': False,
              'sensor_model/max_range': 5.0,
              'sensor_model/hit': 0.7,
              'sensor_model/miss': 0.4,
              'sensor_model/min': 0.12,
              'sensor_model/max': 0.97,
              'color/r': 0.0,
              'color/g': 0.0,
              'color/b': 1.0,
              'color/a': 1.0,
              'color_free/r': 0.0,
              'color_free/g': 0.0,
              'color_free/b': 1.0,
              'color_free/a': 1.0,
              'publish_free_space': False,
    }
    
    remap = [('cloud_in', '/raibo_head_pcl2')]
    node = Node(package='octomap_server2',
                 executable='octomap_server',
                 output='log',
                 remappings=remap,
                 parameters=[params])
    return LaunchDescription([node])
