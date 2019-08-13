#include "factorial.hpp"

Factorial::Factorial() {}

Factorial::~Factorial() {}

int Factorial::factorial(int n) {
  return (n < 1) ? 1 : factorial(n-1) * n;
}