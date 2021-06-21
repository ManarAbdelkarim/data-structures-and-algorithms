# from  ..linked_list.linked_list import *

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
            if current.data[0] == value[0]:
                current.data[1] = value[1]
                return
            while current.next:
                if current.next.data[0] == value[0]:
                    current.next.data[1] = value[1]
                    return
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


class Hashmap:
    """
    this is obviously a hashmap class
    """

    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * self.size


    def hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        hashed_key = (sum *19)% self.size
        return hashed_key
    def __str__(self):
        output = []

        for i in self.map:
            if i:
                current = i.head
                while current:
                    output.append(' -> '.join(current.data))
                    current = current.next
        string_hash = ' ,'.join(output)
        return string_hash


    # def add(self, key, value):
    #    hashed_key = self.hash(key)
    #    if self.contains(key):
    #         current = self.map[hashed_key].head
    #         while current:
    #             if key == current.data[0]:
    #                 current.data[1] =  value
    #             current = current.next
    #             return self
    #    if not self.map[hashed_key]:
    #        self.map[hashed_key] = Linked_list()
    #    self.map[hashed_key].append([ key, value])
    #    return self.__str__()

    def add(self, key, value):
        index = self.hash(key)
        if not self.map[index]:
            self.map[index] = Linked_list()
        self.map[index].append([key, value])
        return [key, value]



    def get(self, key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            current = self.map[hashed_key].head
            while current:
                if key == current.data[0] :
                    return current.data[1]
                current = current.next
        return "not found"



    def contains(self, key):
        index = self.hash(key)
        if self.map[index]:
            current = self.map[index].head
            while current:
                if key == current.data[0]:
                    return True
                current = current.next
        return False


if __name__ == "__main__":
    hash_map = Hashmap()
    print(hash_map.add('Mnaar','she is sleepy all day'))
    print(hash_map.add('Noura','she is sleepy all day'))
    hash_map.add('Noura','she is solving trees all  day')
    hash_map.add('Noura','she is solving trees all  day')
    hash_map.add('Noura','she is solving trees all  day')
    hash_map.add('Tala','she is eating all day')
    hash_map.add('Noura','she is solving trees all  day')
    hash_map.add('Manar','she is studying all day')
    hash_map.add('Maanr','she is studying all day')
    hash_map.add('Manar','she is studying all day')


    hash_map.add('rana','she is Manar but in backward')
    hash_map.add('ranaM','she is Manar but in backward')
    # print(hash_map.get('Noura'))
    print(hash_map)
    print('pass')

