class Queue2Stacks(object):
  """
  Given the Stack class below, implement a Queue class using two stacks! Use a Python list data structure as your Stack.
  """
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def enqueue(self,element):
    pass

  def dequeue(self):
    pass

if __name__ == '__main__':
  q = Queue2Stacks()

  for i in range(5):
      q.enqueue(i)

  for i in range(5):
      print(q.dequeue())
