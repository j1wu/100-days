class Queue(object):
  """
  Created on: 2017-06-08 22:24:38
  Author: Ji Wu

  * Check if Queue is Empty
  * Enqueue
  * Dequeue
  * Return the size of the Queue
  """
  def __init__(self):
    self.items = []

  def empty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    return self.items.pop(0)

  def size(self):
    return len(self.items)

  def show(self):
    return self.items


queue = Queue()

print(queue.empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.dequeue()
print(queue.show())