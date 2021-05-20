class EmptyStackException(Exception):
  pass



class Node: 
  def __init__(self, value=None):
    self.value = value
    self.next = None

class Stack:
  def __init__(self, node=None):
    self.top = node
  
  def push(self, value):
    if not self.top:
      self.top = Node(value)
    else:
      node = Node(value)
      node.next = self.top
      self.top = node
  
  def pop(self):
      if not self.is_empty():
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
      raise EmptyStackException("Cannot pop from an empty stack")
  
  def is_empty(self):
    """ Returns True if Empty and false otherwise """
    if self.top:
      return False
    return True

  def peek(self):
    """ Returns the value at the top without modifying the stack, raises an exception otherwise """
    if not self.is_empty():
      return self.top.value
    
    raise EmptyStackException("Cannot peek an empty stack")
  
  def __str__(self):
    current = self.top
    items = []
    while current:
      items.append(str(current.value))
      current = current.next
    return "\n".join(items)

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None


  def is_empty(self):
    """ Returns True if Empty and false otherwise """
    if self.front:
      return False
    return True

  def enqueue(self, value):
    """ Add an item to the rear fo the queue """
    node = Node(value)

    if not self.front:
      # we have an emtpy queue
      self.front = node
      self.rear = node
    else:
      # make sure the previous rear will now point to the new node
      self.rear.next = node
      # move our rear to point to the new node
      self.rear = self.rear.next


  def dequeue(self):
      """ delete an item to the rear fo the queue """
      if not self.is_empty():
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value
      raise EmptyStackException("Cannot dequeue an empty queue")

  def peek(self):
    """ Returns the value at the top without modifying the stack, raises an exception otherwise """
    if not self.is_empty():
      return self.front.value
    
    raise EmptyStackException("Cannot peek an empty queue")
      
  def __str__(self):
    current = self.front
    items = []
    while current:
      items.append(str(current.value))
      current = current.next
    return "\n".join(items)

if __name__ == "__main__":
  stack = Stack()
  # print(stack)
  # print(stack.peek())
#   stack.push(5)
#   stack.push(4)
#   stack = Stack()
  stack.push('one')
  stack.push("two")
  stack.push("three")
  print(stack)

  # print(stack)
  # print(stack.peek())
#   print(stack)
#   stack.pop()
#   print(stack)


  queue = Queue()
  queue.enqueue("Manar")
  queue.enqueue("Noura")
  queue.enqueue("Reema")
  print(queue)
  print("*********")
  print(queue.peek())
