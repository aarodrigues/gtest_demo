cmake_minimum_required(VERSION 2.8)

project(test_factorial)

set (CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON) #...is required...
set(CMAKE_CXX_EXTENSIONS OFF)
set( CMAKE_INCLUDE_CURRENT_DIR ON )
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")

find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIR})

set(SOURCES "test_factorial.cc")

add_executable(${PROJECT_NAME} ${SOURCES})

# linking libraries 
target_link_libraries(
    ${PROJECT_NAME}
    ${GTEST_LIBRARY}
    ${GTEST_MAIN_LIBRARY}
    factorial_library
)

# Allow ctest find availables tests
add_test(
    NAME ${PROJECT_NAME} 
    COMMAND ${PROJECT_NAME}
)
