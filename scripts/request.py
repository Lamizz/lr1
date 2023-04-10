#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray
rospy.init_node('request')
pub = rospy.Publisher('request_polynomial', Int16MultiArray, queue_size=10)
rate = rospy.Rate(1)

def callback(msg):
  rospy.loginfo('Summing listens: %s', msg.data)
  rospy.Subscriber('summing_request' , Int8, callback, queue_size=10)
def Request():
  poly_msg = Int16MultiArray()
  var = [2, 4, 5]
  while not rospy.is_shutdown():
   poly_msg.data = var
   rospy.loginfo('Request says: %s', poly_msg.data)
   pub.publish(poly_msg)
   rate.sleep()
try:
  Request()
except (rospy.ROSInterruptException, KeyboardInterrupt):
  rospy.logerr('Exception catched')
