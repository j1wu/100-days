import doctest

def pair_sum(arr,k):
  """
  Given an integer array, output all the unique pairs that sum up to a specific value k.

  >>> pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
  6
  >>> pair_sum([1,2,3,1],3)
  1
  >>> pair_sum([1,3,2,2],4)
  2
  """
  result = 0
  pairs = []

  for num in arr:
    target = k - num

    if target in arr:
      pairs.append([num, target])
      result += 1
      arr.remove(target)

  # print('\n'.join(map(str,pairs)))
  return result


if __name__ == '__main__':
  doctest.testmod()