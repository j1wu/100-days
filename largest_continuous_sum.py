import doctest

def large_cont_sum(arr):
  """
  Given an array of integers (positive and negative) find the largest continuous sum.

  >>> large_cont_sum([1,2,-1,3,4,-1])
  9
  >>> large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
  29
  >>> large_cont_sum([-1,1])
  1
  """
  pass


if __name__ == '__main__':
  doctest.testmod()