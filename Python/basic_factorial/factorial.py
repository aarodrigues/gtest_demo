import unittest

def factorial(n):
  return 1 if (n < 1) else factorial(n-1) * n


class TestFactorial(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(factorial(0),1)

    def test_positive(self):
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(3),6)
        self.assertEqual(factorial(8),40320)

if __name__ == '__main__':
    # print(factorial(10))
     unittest.main()