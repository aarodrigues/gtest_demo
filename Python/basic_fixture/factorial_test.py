import unittest
from factorial import Factorial

class TestFactorial(unittest.TestCase):

  fact = Factorial()

  def setup_function(self):
      # The f_setup() function run before test
      print('This function will be triggered on the start of the test')

  def teardown_function(self):
      # The f_teardown() function removes the yes.txt file, if it was created.
      print('This function will be triggered on the end of the test')



  def test_zero(self):
      self.assertEqual(self.fact.factorial(0),1)

  def test_positive(self):
      self.assertEqual(self.fact.factorial(1),1)
      self.assertEqual(self.fact.factorial(2),2)
      self.assertEqual(self.fact.factorial(3),6)
      self.assertEqual(self.fact.factorial(8),40320)

if __name__ == '__main__':
    unittest.main()