#! /usr/bin/env python
import rospy
import time
from rospy_example.rospy_example import talker

## Main function ##
# Executed when script is run directly
if __name__ == '__main__':
        rospy.init_node('talker', anonymous=True)
        clock_object = talker()