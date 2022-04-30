#!/usr/bin/env python3

import sys
import cv2
import rospy
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
from std_msgs.msg import UInt16



faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if cv2.__version__.startswith('2'):
    PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
    PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT
    HAAR_FLAGS = cv2.cv.CV_HAAR_SCALE_IMAGE

elif cv2.__version__.startswith('3'):
    PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
    PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT
    HAAR_FLAGS = cv2.CV_FEATURE_PARAMS_HAAR

else:
    PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
    PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT
    HAAR_FLAGS = cv2.CV_FEATURE_PARAMS_HAAR

    

def talker():
    pub = rospy.Publisher('servo', UInt16, queue_size=10)
    rospy.init_node('face_detect')
    rate = rospy.Rate(1)
    cap = cv2.VideoCapture(0)
    cap.set(PROP_FRAME_WIDTH, 320)
    cap.set(PROP_FRAME_HEIGHT, 240)
      

    while not rospy.is_shutdown():
        # Capture frame-by-frame
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=HAAR_FLAGS
                )
        #print ("Found {0} faces!".format(len(faces)))
        # Draw a rectangle around the face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # Display the resulting frame
            cv2.imshow("preview", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        # When everything is done, release the capture
        if len(faces)==0:
            val=0
        elif len(faces)>=1:
            val=1

        rospy.loginfo(val)
        pub.publish(val)
        rate.sleep()

    #When eveything is done, release the capture
    cap.release()
    cv2.destortAllWindows()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
