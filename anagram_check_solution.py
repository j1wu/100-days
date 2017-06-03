# Problem
# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

from nose.tools import assert_equal

def anagram(s1,s2):
  s1_list = [letter for letter in s1 if letter is not " "]
  s2_list = [letter for letter in s2 if letter is not " "]
  
  if len(s1_list) != len(s2_list):
    return False

  for letter in s1_list:
    if not letter in s2_list:
      return False

  return True


class AnagramTest(object):
  def test(self,sol):
    assert_equal(sol('go go go','gggooo'),True)
    assert_equal(sol('abc','cba'),True)
    assert_equal(sol('hi man','hi     man'),True)
    assert_equal(sol('aabbcc','aabbc'),False)
    assert_equal(sol('123','1 2'),False)
    assert_equal(sol('public relations', 'crap built on lies'),True)
    assert_equal(sol('clint eastwood', 'old west action'),True)
    print("ALL TEST CASES PASSED")

t = AnagramTest()
t.test(anagram)