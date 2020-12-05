#! /usr/bin/env python
#
# Author: Daniel Slovich
# 
# Creates DD robot
#

import subprocess

# spawns DD robot
def spawnDD():
    subprocess.call(['sh','/home/user/catkin_ws/src/dd_rob/scripts/dd_spawn.sh'])  

if __name__=="__main__":
    spawnDD()



