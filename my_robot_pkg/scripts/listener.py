#! /usr/bin/env python
import rospy
import time
from rospy_example.rospy_example import listener

## Main function ##
# Executed when script is run directly
if __name__ == '__main__':
        rospy.init_node('listener', anonymous=True)
        clock_object = listener()