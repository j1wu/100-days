class Deque(object):
  """
  Created on: 2017-06-09 22:24:38
  Author: Ji Wu

  * Check if its empty
  * Add to both front and rear
  * Remove from Front and Rear
  * Check the Size
  """
  def __init__(self):
    self.items = []

  def empty(self):
    return self.items == []

  def size(self):
    return len(self.items)

  def add_front(self, item):
    self.items.insert(0, item)

  def add_rear(self, item):
    self.items.append(item)

  def remove_front(self):
    self.items.pop(0)

  def remove_rear(self):
    self.items.pop()

  def show(self):
    return self.items

deque = Deque()

print(deque.empty())
deque.add_front(1)
deque.add_front(0)
print(deque.show())

deque.add_rear(2)
print(deque.show())

deque.remove_front()
print(deque.show())

deque.remove_rear()
print(deque.show())
