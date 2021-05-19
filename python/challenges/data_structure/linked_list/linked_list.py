# Define Node
from typing import overload
import sys

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

  def append(self, value):
        
        new_node = Node(value)
        current = self.head
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
            
  def insertAfter(self, value, newVal):
    
        new_node = Node(newVal)
        current = self.head
        if not self.head:
                self.head = new_node
        else:
            current = self.head
            while current.next:
                if current.next.data == value:
                    current = current.next
                    old_node = current.next
                    current.next = new_node
                    new_node.next = old_node
                    return  f' "{newVal}" added secssfuly...'
                else:
                    current = current.next
                    
            return "this node is not exist!"



  
  def kthFromEnd(self,k:int):
    '''
    this function will find the value of the node number k
    from the end and return it .. if k is out of range or negative 
    it will return error message
    '''
    length = 0
    current = self.head
    while(current):
        length += 1
        current = current.next

    if k >= length or k < 0:
      return f"{k} is not in the range of the list"  
        
    current = self.head

    for i in range(0,length-k-1):
        current = current.next
    return current.data

  def length(self):
      length = 0
      current = self.head
      while(current):
          length += 1
          current = current.next
      return length



  
  # def zipLists(first, second):
  #    '''
  #   this function will take two linked list and merge them in a zip style
  #   ex: linked_list1 = 1->2->3->None , linked_list2 = 4->5->6->None
  #   will return 1->4->2->5->3->6->None 
  #   '''
  #   #  current1 = first.head
  #   #  current2 = second.head
  #   #  length1 =0
  #   #  length2 =0
  #   #  temp = {}
  #   #  while(current1):
  #   #     length1 += 1
  #   #     current1 = current1.next

  #   #  while(current2):
  #   #     length2 += 1
  #   #     current2 = current2.next
  #    print("first", first.length())
  #    print("second",second.length())

  #    if first.length() < second.length():
  #      temp =first
  #      first = second
  #      second =temp

  #    current1 = first.head
  #    current2 = second.head

  #    while current1 and current2:

  #           first_next = current1.next
  #           second_next = current2.next
  
  #           current2.next = first_next 
  #           current1.next = current2 

  #           current1 = first_next
  #           current2 = second_next
  #           second.head = current2

  #    return f"{first}"





  def zipLists(first_ll, second_ll):
    new_linked_list = Linked_list()

    if first_ll.length() > second_ll.length():
        longer_ll = first_ll.length()
    else:
        longer_ll = second_ll.length() 

    current1 = first_ll.head
    current2 = second_ll.head

    for i in range(longer_ll):
        if current1:
            new_linked_list.append(current1.data)
            current1 = current1.next
        if current2:
            new_linked_list.append(current2.data)
            current2 = current2.next    
        
    return new_linked_list.__str__()



llist1 = Linked_list()
llist2 = Linked_list()
llist1.append(3)
llist1.append(2)
llist1.append(1)
# llist1.append(6)
# llist1.append(5)
# llist1.append(4)
# llist1.append(6)
# llist1.append(5)
# llist1.append(4)
  
print ("First Linked List:")
# print(llist1)
  
llist2.append(8)
llist2.append(7)
llist2.append(6)
llist2.append(5)
llist2.append(4)
  
print ("Second Linked List:")
  
print(llist2)
print(Linked_list.zipLists(llist1,llist2))
  
# print ("Modified first linked list:")
# print(llist1)
  
# print ("Modified second linked list:")
# print(llist2)




# linked = Linked_list()
# linked.insert("Reem")
# linked.insert("Manar")
# linked.insert(10)
# linked.insert("Manar")
# linked.insert(10)

# print(linked)

# Write program here
if __name__ == "__main__":
  pass
