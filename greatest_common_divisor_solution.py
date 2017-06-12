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
  max_ans = min(a, b)

  for ans in range(max_ans, 0, -1):
    if a % ans == 0 and b % ans ==0:
      return ans
    else:
      continue


if __name__ == '__main__':
  doctest.testmod()