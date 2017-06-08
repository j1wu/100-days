class Stack(object):
  """
  * Check if its empty
  * Push a new item
  * Pop an item
  * Peek at the top item
  * Return the size
  """
  def __init__(self):
    self.items = []

  def empty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    self.items.pop()

  def peek(self):
    return self.items[len(self.items) - 1]

  def size(self):
    return len(self.items)


stack = Stack()

print(stack.empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
stack.pop()
print(stack.peek())
print(stack.size())