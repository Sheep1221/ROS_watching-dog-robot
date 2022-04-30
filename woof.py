#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import UInt16
from playsound import playsound



def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %d", data.data)
    if data.data == 1:
        playsound("woof.mp3")


def listener():
    rospy.init_node('woof')

    rospy.Subscriber('servo', UInt16, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
