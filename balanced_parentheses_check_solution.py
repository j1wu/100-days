import doctest

def balance_check(s):
  """
  Created on: 2017-06-18 17:40:35
  Author: Ji Wu

  Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not.

  >>> balance_check('[](){([[[]]])}(')
  False
  >>> balance_check('[{{{(())}}}]((()))')
  True
  >>> balance_check('[[[]])]')
  False
  """
  if len(s) % 2 != 0:
    return False

  pairs = [('(',')'), ('[', ']'), ('{', '}')]
  open_parens = [pair[0] for pair in pairs]
  stack = []

  for paren in s:
    if paren in open_parens:
      stack.append(paren)
    else:
      pair = (stack.pop(), paren)
      if pair not in pairs:
        return False

  return len(stack) == 0


if __name__ == '__main__':
  doctest.testmod()
