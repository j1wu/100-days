import doctest

def longest_substring(s):
  """
  Created on: 2017-06-10 22:24:38
  Author: Ji Wu

  Prints the longest substring of s in which the letters occur in alphabetical order.

  >>> longest_substring('azcbobobegghakl')
  'Longest substring in alphabetical order is: beggh'
  """
  first_letter = s[0]
  last_seen_char_code = ord(first_letter)
  longest_substr = current_substr = [first_letter]

  for letter in s[1:]:
    if ord(letter) >= last_seen_char_code:
      current_substr.append(letter)
    else:
      current_substr = [letter]

    last_seen_char_code = ord(letter)

    if len(current_substr) > len(longest_substr):
      longest_substr = current_substr

  return 'Longest substring in alphabetical order is: ' + ''.join(longest_substr)


if __name__ == '__main__':
  doctest.testmod()