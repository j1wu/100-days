import doctest

def fib(n):
  """
  In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence, and characterized by the fact that every number after the first two is the sum of the two preceding ones.

  >>> fib(0)
  1
  >>> fib(1)
  1
  >>> fib(2)
  2
  >>> fib(3)
  3
  >>> fib(4)
  5
  >>> fib(5)
  8
  """
  pass


if __name__ == '__main__':
  doctest.testmod()