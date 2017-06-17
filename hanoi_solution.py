import doctest

def hanoi(n, fr, to, spare):
  """
  Created on: 2017-06-11 22:24:38
  Author: Ji Wu

  The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
  1. Only one disk can be moved at a time.
  2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
  3. No disk may be placed on top of a smaller disk.

  >>> hanoi(4, 'P1', 'P2', 'P3')
  move from P1 to P3
  move from P1 to P2
  move from P3 to P2
  move from P1 to P3
  move from P2 to P1
  move from P2 to P3
  move from P1 to P3
  move from P1 to P2
  move from P3 to P2
  move from P3 to P1
  move from P2 to P1
  move from P3 to P2
  move from P1 to P3
  move from P1 to P2
  move from P3 to P2
  """
  if n == 1:
    print('move from ' + str(fr) + ' to ' + str(to))
  else:
    hanoi(n-1, fr, spare, to)
    hanoi(1, fr, to, spare)
    hanoi(n-1, spare, to, fr)


if __name__ == '__main__':
  doctest.testmod()