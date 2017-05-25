## simple_hexapod_gazebo

ROS package providing Gazebo simulation of the Phantom X Hexapod robot.
Also provides a Python interface to the joints and some walk capabilities.

These have been tested in simulation and need some work to be used on the real robot, do not use as-is.

![Phantom X model in Gazebo](/simple_hexapod.png?raw=true "Phantom X model in Gazebo")


## Install

Clone in your catkin workspace and catkin_make it.
Make sure you also have the following packages in your workspace
* simple_hexapod_description: https://github.com/HumaRobotics/simple_hexapod_description
* simple_hexapod_control: https://github.com/HumaRobotics/simple_hexapod_control
    
## Usage

You can launch the simulation with:

    roslaunch simple_hexapod_gazebo simple_hexapod_gazebo.launch
    
PRESS PLAY IN GAZEBO ONLY WHEN EVERYTHING IS LOADED (wait for controllers)

You can run a walk demo with:

    rosrun simple_hexapod_gazebo walker_demo.py

## ROS API

All topics are provided in the /simple_hexapod namespace.

Sensors:

    /simple_hexapod/joint_states

Actuators (radians for position control, arbitrary normalized speed for cmd_vel):

    /simple_hexapod/cmd_vel
    /simple_hexapod/j_c1_lf_position_controller/command
    /simple_hexapod/j_c1_lm_position_controller/command
    /simple_hexapod/j_c1_lr_position_controller/command
    /simple_hexapod/j_c1_rf_position_controller/command
    /simple_hexapod/j_c1_rm_position_controller/command
    /simple_hexapod/j_c1_rr_position_controller/command
    /simple_hexapod/j_thigh_lf_position_controller/command
    /simple_hexapod/j_thigh_lm_position_controller/command
    /simple_hexapod/j_thigh_lr_position_controller/command
    /simple_hexapod/j_thigh_rf_position_controller/command
    /simple_hexapod/j_thigh_rm_position_controller/command
    /simple_hexapod/j_thigh_rr_position_controller/command
    /simple_hexapod/j_tibia_lf_position_controller/command
    /simple_hexapod/j_tibia_lm_position_controller/command
    /simple_hexapod/j_tibia_lr_position_controller/command
    /simple_hexapod/j_tibia_rf_position_controller/command
    /simple_hexapod/j_tibia_rm_position_controller/command
    /simple_hexapod/j_tibia_rr_position_controller/command


## Python API

Basic usage:
```python
import rospy
from simple_hexapod_gazebo.simple_hexapod import Simple_Hexapod

rospy.init_node("walker_demo")

simple_hexapod=Simple_Hexapod()
rospy.sleep(1)

simple_hexapod.set_walk_velocity(1,0,0) # Set full speed ahead for 5 secs
rospy.sleep(5)
simple_hexapod.set_walk_velocity(0,0,0) # Stop
```
## Dependencies

The following ROS packages have to be installed:
* gazebo_ros_control

## License

This software is provided by Génération Robots http://www.generationrobots.com and HumaRobotics http://www.humarobotics.com under the Simplified BSD license