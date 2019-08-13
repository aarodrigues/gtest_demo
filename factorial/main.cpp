#include<iostream>
#include "factorial.hpp"

int main(){
    Factorial factorial;
    std::cout << factorial.factorial(10) << std::endl;
    return 0;
}