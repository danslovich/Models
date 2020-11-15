#!/bin/bash

#Daniel Slovich - box spawner

rosrun gazebo_ros spawn_model -file `rospack find dd_robot`/models/box.sdf -sdf -x $1 -y $2 -z $3 -model box_$4
