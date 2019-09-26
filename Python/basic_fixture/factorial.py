class Factorial:

  def factorial(self,n):
    return 1 if (n < 1) else self.factorial(n-1) * n