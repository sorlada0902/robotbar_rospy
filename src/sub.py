#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64
def callback(msg):
    rospy.loginfo(msg)
    
rospy.init_node("sub")
rospy.Subscriber("Topic", Int64,callback, queue_size=10)
rospy.spin()