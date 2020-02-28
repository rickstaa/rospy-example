#!/usr/bin/env python
import time
import rospy

## Clock Subscriber ##
#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String


class talker(object):
    def __init__(self):
        pub = rospy.Publisher("chatter", String, queue_size=10)
        rospy.init_node("talker", anonymous=True)
        rate = rospy.Rate(10)  # 10hz
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()


class listener(object):
    def __init__(self):

        # In ROS, nodes are uniquely named. If two nodes with the same
        # name are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node("listener", anonymous=True)

        rospy.Subscriber("chatter", String, self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


if __name__ == "__main__":
    ros_talker = talker()
    ros_listener = listener()

