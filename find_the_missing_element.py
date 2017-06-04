import doctest

def finder(arr1,arr2):
  """
  Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

  >>> finder([5,5,7,7],[5,7,7])
  5
  >>> finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
  5
  >>> finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])
  6
  """
  pass


if __name__ == '__main__':
  doctest.testmod()