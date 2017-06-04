import doctest

def anagram(s1,s2):
  """
  Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

  >>> anagram('go go go','gggooo')
  True
  >>> anagram('abc','cba')
  True
  >>> anagram('hi man','hi     man')
  True
  >>> anagram('aabbcc','aabbc')
  False
  >>> anagram('123','1 2')
  False
  >>> anagram('public relations', 'crap built on lies')
  True
  >>> anagram('clint eastwood', 'old west action')
  True
  """
  s1_list = [letter for letter in s1 if letter is not " "]
  s2_list = [letter for letter in s2 if letter is not " "]

  if len(s1_list) != len(s2_list):
    return False

  for letter in s1_list:
    if not letter in s2_list:
      return False

  return True


if __name__ == '__main__':
  doctest.testmod()