import doctest

def compress(s):
  """
  Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

  >>> compress('')
  ''
  >>> compress('AABBCC')
  'A2B2C2'
  >>> compress('AAABCCDDDDD')
  'A3B1C2D5'
  """
  pass


if __name__ == '__main__':
  doctest.testmod()