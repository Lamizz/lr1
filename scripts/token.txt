#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

rospy.init_node('talker')
pub2 = rospy.Publisher('overflow_topic', Int16, queue_size=10)
pub = rospy.Publisher('listener_topic', Int16, queue_size=10)
rate = rospy.Rate(10)
def start_talker():
    msg = Int16()
    alr = Int16()
    a=0
    while not rospy.is_shutdown():
        a = int(a)
        rospy.loginfo(a)
        a= a+2 
        if a>100:
          a=0
          alr.data = a
          pub2.publish(alr)
        msg.data = a
        pub.publish(msg)
     
        rate.sleep()
try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
