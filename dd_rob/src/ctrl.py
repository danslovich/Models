#! /usr/bin/env python

import rospy
from gazebo_msgs.srv import ApplyJointEffort, GetJointProperties
from geometry_msgs.msg import Twist
from std_msgs.msg import Header


def setRotation(pub, val):
    start_t     = rospy.Time(0    ,0)
    end_t       = rospy.Time(0.01 ,0)
    buff        = ApplyJointEffort()
    buff.effort = val

    buff.joint_name = 'dd_robot::left_wheel_hinge'
    pub(buff.joint_name, -buff.effort, start_t, end_t)
    buff.joint_name = 'dd_robot::right_wheel_hinge'
    pub(buff.joint_name, buff.effort, start_t, end_t)

def setDirection(pub, val):
    start_t     = rospy.Time(0     ,0)
    short_t     = rospy.Time(0.0072,0)
    end_t       = rospy.Time(0.01  ,0)
    buff        = ApplyJointEffort()
    buff.effort = val

    buff.joint_name = 'dd_robot::right_wheel_hinge'
    pub(buff.joint_name, buff.effort, start_t, short_t)
    buff.joint_name = 'dd_robot::left_wheel_hinge'
    pub(buff.joint_name, buff.effort, start_t, end_t)


def getPos(pub):
    buff            = GetJointProperties()
    buff.joint_name = 'dd_robot::left_wheel_hinge'
    val             = pub(buff.joint_name)
    left_wheel      = val.rate[0]
    buff.joint_name = 'dd_robot::right_wheel_hinge'
    val             = pub(buff.joint_name)
    right_wheel     = val.rate[0]
    
    v = (left_wheel, right_wheel)
    return v

def action(cmd):
    if(cmd.linear.x==0):
        setRotation(pub, 50*cmd.angular.z)
    else:
        setDirection(pub, 100*cmd.linear.x)
    
if __name__=="__main__":
    rospy.init_node('dd_ctrl', anonymous=True)
    sub    = rospy.Subscriber('/cmd_vel', Twist, action)
    pub    = rospy.ServiceProxy('/gazebo/apply_joint_effort'   , ApplyJointEffort)
    pubget = rospy.ServiceProxy('/gazebo/get_joint_properties' , GetJointProperties)
    rospy.spin()
    
