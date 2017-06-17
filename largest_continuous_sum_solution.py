import doctest

def large_cont_sum(arr):
  """
  Created on: 2017-06-05 22:24:38
  Author: Ji Wu

  Given an array of integers (positive and negative) find the largest continuous sum.

  >>> large_cont_sum([1,2,-1,3,4,-1])
  9
  >>> large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
  29
  >>> large_cont_sum([-1,1])
  1
  """
  if len(arr) == 0:
    return 0

  max_sum = current_sum = arr[0]

  for num in arr[1:]:
    current_sum += num

    if current_sum < num:
      current_sum = num

    if current_sum > max_sum:
      max_sum = current_sum

  return max_sum


if __name__ == '__main__':
  doctest.testmod()