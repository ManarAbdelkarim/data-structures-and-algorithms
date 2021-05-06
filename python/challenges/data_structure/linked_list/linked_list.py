# Define Node
from typing import overload


class Node():
  def __init__(self, data=None):
      self.data = data
      self.next = None
  # use a magic method so when you print node you see it's value
  def __str__(self):
    return f"{self.data}"


class Linked_list:
  # Constructor
  def __init__(self):
    self.head = None
  # define your append method
  def insert (self, data=None):
    new_node = Node(data)
    # Once we have a head 
    if self.head :
      new_node.next = self.head # set our current pointer to the head
      #Assign new_node to self.head 
    self.head = new_node
      # while there is a following node that's not None
    
   
#   # __str__ , __repr__
  def __str__(self):
  
    """ Returns a string representation of the linked list
        1 -> 3 -> 4 -> null
    """
    # step 0 - create a new empty string
    output = ""
    # step 1 iterate over each node
    current = self.head
    while current:
      # step 2 - append each data to the string
      output += "{%s} -> " %(current.data,) 
      # step 2b:  move to the next item
      current = current.next
    output += " NULL"

    # step 3 - return the final string
    return output

  def includes(self,value):
    current = self.head 
    while (current):
        if current.data == value :
            return True
        current = current.next
    return False


  

# Write program here
if __name__ == "__main__":
  pass