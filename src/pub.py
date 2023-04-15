#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64

rospy.init_node("pub",anonymous=True) #
pub = rospy.Publisher("Topic", Int64, queue_size=10)
rate = rospy.Rate(10) #hz

msg = 2
while not rospy.is_shutdown():
    pub.publish(msg)
    rate.sleep()
