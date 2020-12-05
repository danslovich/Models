#!/bin/bash

#Daniel Slovich - Robot spawner
rosservice call gazebo/delete_model dd_robot > /dev/null
rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/dd_rob/models/model.sdf -sdf -model dd_robot -y 0.0 -x 0.0 -z 0.5 > /dev/null
