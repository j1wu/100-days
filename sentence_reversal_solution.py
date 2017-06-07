import doctest

def rev_word(s):
  """
  Given a string of words, reverse all the words.

  >>> rev_word('    space before')
  'before space'
  >>> rev_word('space after     ')
  'after space'
  >>> rev_word('   Hello John    how are you   ')
  'you are how John Hello'
  >>> rev_word('1')
  '1'
  """
  lst = s.strip().split(' ')
  output = []

  while lst:
    item = lst.pop()
    if item:
      output.append(item)

  return ' '.join(output)


if __name__ == '__main__':
  doctest.testmod()