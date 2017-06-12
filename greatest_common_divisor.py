import doctest

def gcd(a, b):
  """
  Find the greatest common divisor of two positive integers, which is the largest integer that divides each of them without remainder.

  >>> gcd(2, 12)
  2
  >>> gcd(6, 12)
  6
  >>> gcd(9, 12)
  3
  >>> gcd(17, 12)
  1
  """
  pass


if __name__ == '__main__':
  doctest.testmod()