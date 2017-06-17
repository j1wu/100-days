import doctest

def fib(n):
  """
  Created on: 2017-06-12 22:24:38
  Author: Ji Wu

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
  if n == 0 or n == 1:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
  doctest.testmod()