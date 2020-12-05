#!/bin/bash

#Daniel Slovich - box spawner

rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/dd_rob/models/box.sdf -sdf -x $1 -y $2 -z 5 -model box_$3 &
