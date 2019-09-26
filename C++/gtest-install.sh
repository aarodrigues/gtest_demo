#!/bin/bash

# download from gtest repositpory on github
git clone  https://github.com/google/googletest.git
# enter googletest directory
cd googletest/googletest
# create build directory and enter into
mkdir build && cd build
# install cmake if it is not installed
if ! type "cmake" > /dev/null; then
  sudo apt-get install -y cmake
fi
# compile google test
sudo cmake -DCMAKE_CXX_COMPILER="c++" -DCMAKE_CXX_FLAGS="-std=c++11" ../
sudo make
# copy files to be found by compiler
sudo cp -r ../include/gtest /usr/local/include/
sudo cp -r lib/libgtest*.a /usr/local/lib/

# sudo rm -r googletest
