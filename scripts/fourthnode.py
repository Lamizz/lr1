#!/usr/bin/env python3
import rospy
import tf
import math
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose

rospy.init_node('turtle')
turtlename = rospy.get_param('~turtle')

def handle_turtle_pose(msg):
    br = tf.TransformBroadcaster()
    
    br.sendTransform((msg.x, msg.y, 0),quaternion_from_euler(0, 0, msg.theta),rospy.Time.now(),turtlename,"world")
    t=rospy.Time.now().to_sec() * math.pi
    
    x=0.5*math.sin(t)
    
    y=0.5*math.cos(t) 
    
    z=0
       
    br.sendTransform((x, y, z), quaternion_from_euler(0, 0, t), rospy.Time.now(), "carrot", turtlename)
rospy.Subscriber('input_pose',Pose,handle_turtle_pose)
rospy.spin()
