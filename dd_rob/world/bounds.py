#!/usr/bin/env python3

# Author: Daniel Slovich
# 
# Creates 50mx50m world map with perimeter
# boxes 1 meter apart
#

import rospy
import subprocess
import math
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import Twist, Pose

box = {}
i = 0

# spawns box i at location x,y,z
def spawnBox(x, y):
    global i
    global box
    if (str(x)+str(y) in box.values() or x>25 or y>25):
        return
    else:
        box.update({i: str(x)+str(y)})
        subprocess.call(['sh','/home/user/catkin_ws/src/dd_rob/scripts/box_spawn.sh', str(x), str(y), str(i)])
        i+=1

def getPos(sub):
    buff            = GetModelState()
    buff.model_name = 'dd_robot'
    val             = sub(buff.model_name, 'world')
    x_dist          = val.pose.position.x
    y_dist          = val.pose.position.y

    if  (x_dist<-20):
        spawnBox(-25, math.floor(y_dist)-2)
        spawnBox(-25, math.floor(y_dist)-1)
        spawnBox(-25, math.floor(y_dist))
        spawnBox(-25, math.floor(y_dist)+1)
        spawnBox(-25, math.floor(y_dist)+2)
    if  (x_dist>20):
        spawnBox(25, math.floor(y_dist)-2)
        spawnBox(25, math.floor(y_dist)-1)
        spawnBox(25, math.floor(y_dist))
        spawnBox(25, math.floor(y_dist)+1)
        spawnBox(25, math.floor(y_dist)+2)  
    if  (y_dist<-20):
        spawnBox(math.floor(x_dist)-2, -25)
        spawnBox(math.floor(x_dist)-1, -25)
        spawnBox(math.floor(x_dist)  , -25)
        spawnBox(math.floor(x_dist)+1, -25)
        spawnBox(math.floor(x_dist)+2, -25)
    if  (y_dist>20):
        spawnBox(math.floor(x_dist)-2, 25)
        spawnBox(math.floor(x_dist)-1, 25)
        spawnBox(math.floor(x_dist)  , 25) 
        spawnBox(math.floor(x_dist)+1, 25)
        spawnBox(math.floor(x_dist)+2, 25)

# spawns out of bounds perimeter
def spawnBounds():
    i   =   0
    x   = -25
    y   = -25
    z   =   5
    box =   0
    
    for i in range(0, 25): 
        subprocess.call(['sh', '/home/user/catkin_ws/src/dd_robot/scripts/box_spawn.sh', '-25', str(y), str(z), str(box)])
        box=box+1
        subprocess.call(['sh', '/home/user/catkin_ws/src/dd_robot/scripts/box_spawn.sh', '25', str(-y), str(z), str(box)])
        box=box+1
        subprocess.call(['sh', '/home/user/catkin_ws/src/dd_robot/scripts/box_spawn.sh', str(x), '25', str(z), str(box)])
        box=box+1
        subprocess.call(['sh', '/home/user/catkin_ws/src/dd_robot/scripts/box_spawn.sh', str(-x), '-25', str(z), str(box)])
        box=box+1
        x=x+2
        y=y+2

if __name__=="__main__":
    rospy.init_node('box_server', anonymous=True)
    sub = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    
    while (1):
        getPos(sub)
    rospy.spin()



