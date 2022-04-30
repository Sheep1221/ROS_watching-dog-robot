#!/usr/bin/env python
# license removed for brevity

import rospy
import time
import threading
import tkinter as tk
from std_msgs.msg import UInt16

window = tk.Tk()
window.title('window')
lbl_1 = tk.Label(window, text='Warning!!!!!!', bg='red', fg='#263238', font=('Arial', 200))
lbl_1.grid(column=0, row=0)

def autoClose():
    time.sleep(10)
    window.destroy()


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %d", data.data)
    if data.data == 1:
        window = tk.Tk()
        window.title('window')
        lbl_1 = tk.Label(window, text='Warning!!!!!!', bg='red', fg='#263238', font=('Arial', 200))
        lbl_1.grid(column=0, row=0)

        def autoClose():
            time.sleep(10)
            window.destroy()
        
        #t = threading.Thread(target=autoClose)
        #t.start()
        window.mainloop()


def listener():
    rospy.init_node('warning')

    rospy.Subscriber('servo', UInt16, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
