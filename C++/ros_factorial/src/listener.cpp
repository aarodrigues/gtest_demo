#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Int64.h"


unsigned long factorial(unsigned long n){
  return (n < 1) ? 1 : factorial(n-1) * n;
}


void chatterCallback(const std_msgs::Int64::ConstPtr& msg)
{
  ROS_INFO("I heard: [%ld] factorial: [%ld]", msg->data, factorial(msg->data));
  // std::cout <<  "factorial: " << factorial(10) <<std::endl;
}


