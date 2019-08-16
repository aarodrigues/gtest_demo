cmake_minimum_required(VERSION 2.8.3)
project(ros_factorial)

set (CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON) #...is required...
set(CMAKE_CXX_EXTENSIONS OFF)
set( CMAKE_INCLUDE_CURRENT_DIR ON )
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

## Declare ROS messages and services
#add_message_files(FILES Num.msg)
#add_service_files(FILES AddTwoInts.srv)

## Generate added messages and services
#generate_messages(DEPENDENCIES std_msgs)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ros_factorial
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(talker src/talker.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})
add_dependencies(talker ros_factorial_messages_cpp)

add_executable(listener  src/main.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})
add_dependencies(listener ros_factorial_messages_cpp)

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
   enable_testing()    
   add_library(listener_test src/listener.cpp)
   catkin_add_gtest( fact_test
      test/test_factorial.cpp
   )    
   target_link_libraries( fact_test
   listener_test
       ${catkin_LIBRARIES}
   )
endif()
