#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray
rospy.init_node('summing')
def callback(msg):
  array = msg.data
  rospy.loginfo('Summing listenss %s', array)
  summ = sum(array)
  sum_msg = Int16()
  sum_msg.data = summ
  rospy.loginfo('Summing says %s', sum_msg.data)
  pub.publish(sum_msg)  
pub = rospy.Publisher('summing_request', Int16, queue_size=10)
rospy.Subscriber('polynomial_summing', Int16MultiArray, callback, queue_size=10)
rospy.spin()
