#!/usr/bin/env python

import sys
import unittest
import rospy

from std_msgs.msg import Int64
from basic_communication import ListenerFactorial

class TestFactorial(unittest.TestCase):

    def setUp(self):
        # The f_setup() function run before test
        rospy.init_node('listener', anonymous=True)
        print('\nThis function will be triggered on the start of the test')

    def tearDown(self):
        # The f_teardown() function removes the yes.txt file, if it was created.
        print('This function will be triggered on the end of the test')

    def test_factorial_message(self):
        listen = ListenerFactorial('chatter', Int64)
        rospy.sleep(2)
        self.assertEqual(listen.message(),120)

    def test_topic_message(self):
        listen = ListenerFactorial('chatter', Int64)
        rospy.sleep(2)
        self.assertEqual(listen.listened(),5)


PKG = 'python_factorial'
if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_factorial', TestFactorial)
    # unittest.main()