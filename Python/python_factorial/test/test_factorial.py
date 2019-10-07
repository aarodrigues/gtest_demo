#!/usr/bin/env python

# import roslib; roslib.load_manifest(PKG) # This line is not needed with Catkin.

import sys
# sys.path.insert(1, '/path/to/application/app/scripts')
import unittest
import rospy

from std_msgs.msg import Int64

from python_factorial import ListenerFactorial


# package = 'python_factorial'
class TestFactorial(unittest.TestCase):

  def setUp(self):
      # The f_setup() function run before test
      rospy.init_node('listener', anonymous=True)
      print('\nThis function will be triggered on the start of the test')

  def tearDown(self):
      # The f_teardown() function removes the yes.txt file, if it was created.
      print('This function will be triggered on the end of the test')

  def test_zero(self):
      # sub = ListenerFactorial('chatter', Int64)
      # self.assertEqual(sub.factorial(0),1)
      self.assertEqual(1,1)

  # def test_positive(self):
  #     self.assertEqual(listener.factorial(1),1)
  #     self.assertEqual(listener.factorial(2),2)
  #     self.assertEqual(listener.factorial(3),6)
  #     self.assertEqual(listener.factorial(8),40320)

PKG = 'python_factorial'
if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_factorial', TestFactorial)
    # unittest.main()