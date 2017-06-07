import doctest
import collections

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
  store = collections.OrderedDict()
  lst = list(s)
  output = ''

  for key in lst:
    if not key in store:
      store[key] = 1
    else:
      store[key] += 1

  for key, value in store.items():
    output = output + key + str(value)

  return output


if __name__ == '__main__':
  doctest.testmod()