#! /usr/bin/env python3
#
#   Author: Daniel Slovich
#   About:  DD robot
#

from geometry_msgs.msg import Twist
from std_msgs.msg import String
import rospy
import time

def inp2Vel(action):
    if(action.data=='forward'):   #fwd
        linear  = 1.0
        angular = 0.0
    elif(action.data=='backward'): #bck
        linear  = -1.0
        angular = 0.0
    elif(action.data=='l_rotate'): #left
        linear  = 0.0
        angular = 1.0
    elif(action.data=='r_rotate'): #right
        linear = 0.0
        angular = -1.0
    else:
        linear  = 0.0
        angular = 0.0
    vel2Cmd(linear, angular)

def vel2Cmd(linear, angular):
    cmd = Twist()
    cmd.linear.x  = linear
    cmd.angular.z = angular
    pub.publish(cmd)
    return

if __name__=='__main__':
    rospy.init_node('dd_mov', anonymous=True)
    sub  = rospy.Subscriber('/dd_inp', String, inp2Vel)
    pub  = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.spin()