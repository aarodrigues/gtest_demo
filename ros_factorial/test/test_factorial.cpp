#include "ros/ros.h"
#include "std_msgs/Int64.h"
#include <gtest/gtest.h>
#include <iostream>

#include "../src/listener.cpp"



TEST(FactorialTest, DealWithZero) {
  EXPECT_EQ(factorial(0), 1);
}

TEST(FactorialTest, HandlesPositiveInput) {
  EXPECT_EQ(factorial(1), 1);
  EXPECT_EQ(factorial(2), 2);
  EXPECT_EQ(factorial(3), 6);
  EXPECT_EQ(factorial(8), 40320);
}

int main(int argc, char **argv){
  testing::InitGoogleTest(&argc, argv);
  ros::init(argc, argv, "tester");
  ros::NodeHandle nh;

  //ros::Subscriber sub = nh.subscribe("chatter", 1000, chatterCallback);

  return RUN_ALL_TESTS();
}