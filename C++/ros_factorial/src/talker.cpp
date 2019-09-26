#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Int64.h"

#include <sstream>

/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");

  ros::NodeHandle n;

  // ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
  ros::Publisher chatter_pub = n.advertise<std_msgs::Int64>("chatter", 1000);

  ros::Rate loop_rate(0.5);

  int count = 0;
  while (ros::ok())
  {
    // std_msgs::String msg;

    std_msgs::Int64 msg; // new

    std::stringstream ss;
    ss << "hello world " << count;
    // msg.data = ss.str();
     msg.data = count; // new

    // ROS_INFO("%s", msg.data.c_str());

    ROS_INFO("%ld", msg.data); // new

    chatter_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    ++count;
  }


  return 0;
}