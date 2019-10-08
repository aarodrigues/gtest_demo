#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64

class ListenerFactorial:

    def __init__(self, topic_name, message_type, get_only_first=True):
        self.__message = None
        self.__listened_topic_message = None
        self.__has_msg = False
        self.__get_only_first = get_only_first
        self.sub = rospy.Subscriber(topic_name, message_type, self.chatter_callback)

    def factorial(self,n):
        return 1 if (n < 1) else self.factorial(n-1) * n

    def chatter_callback(self,data):
        self.__listened_topic_message = data.data
        if(self.__get_only_first and not self.__has_msg):
            self.__has_msg = True
            self.__message = self.factorial(data.data)
        elif(not self.__get_only_first):
            self.__has_msg = True
            self.__message = self.factorial(data.data)
        rospy.loginfo(rospy.get_caller_id() + 'I heard %s', self.factorial(data.data))

    def waitForPublisher(self, duration=rospy.rostime.Duration(5.0)):
        deadline = rospy.Time.now() + duration
        while (self.sub.get_num_connections() < 1):
            if (rospy.Time.now() >= deadline and not rospy.core.is_shutdown()):
                output = "No publishers available after "
                output += str(duration.secs) + "s"
                raise RuntimeError(output)
            rospy.rostime.wallsleep(0.001)

    def waitForMessage(self):
        while(not self.__has_msg and not rospy.core.is_shutdown()):
            rospy.sleep(0.001)

    def hasMsg(self):
        return self.__has_msg

    def resetMsg(self):
        self.__has_msg = False
        self.__message = None

    def message(self):
        return self.__message

    def listened(self):
        return self.__listened_topic_message

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    listen = ListenerFactorial('chatter',Int64)
    rospy.spin()
