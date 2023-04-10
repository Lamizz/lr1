#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16MultiArray
rospy.init_node('polynomial')
def callback(msg):
 var = msg.data
 rospy.loginfo('Polynomial listens:  %s', var)
 pol = [0, 0, 0]   
 for i in range(len(var)):
    pol[i] = var[i] ** (3 - i)  
 poly_msg = Int16MultiArray()
 poly_msg.data = pol
 rospy.loginfo('Polynomial says: %s', poly_msg.data)
 pub.publish(poly_msg)  
pub = rospy.Publisher('polynomial_summing', Int16MultiArray, queue_size=10)
rospy.Subscriber('request_polynomial', Int16MultiArray, callback, queue_size=10)
rospy.spin()
