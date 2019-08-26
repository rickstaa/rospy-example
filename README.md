# A simple ros python node example
[![Ros version](https://img.shields.io/badge/ROS%20version-Melodic-green)](https://wiki.ros.org/melodic)
[![Python 2](https://img.shields.io/badge/python%203-2.7-green.svg)](https://www.python.org/)

This repository contains a simple ROS python pack.

## How to use

1. Clone the repository in a `catkin_ws/src` folder.
2. Source the `/opt/ros/<ROS_VERSION>/setup.bash` file.
3. Run `catkin build` or `catkin_make` from within the `catkin_ws/src` folder.
4. Start the clock_call node using the `roslaunch my_robot_pkg launch_example.launch` command.

## Known problems

By default it only works with python 2.7 [see this issue](https://stackoverflow.com/questions/54094876/ros-melodic-installation-with-python-3-only-and-without-messing-up-system-librar). A guide on how to use
`Python3` in ROS Melodic or Noetic can be found [here](https://wiki.ros.org/UsingPython3).
