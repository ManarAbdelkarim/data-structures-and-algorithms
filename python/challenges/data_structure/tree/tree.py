# import pysnooper
# from challenges.data_structure.stacks_and_queues.stacks_and_queues import *


class EmptyStackException(Exception):
  pass
class EmptyTreeException(Exception):
  pass
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None



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


class TNode:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

class Binary_tree:
  def __init__(self, root=None):
    self.root = root
    self.pre_values = []
    self.in_values = []
    self.post_values = []
    self.maximum_value = None

  def __str__(self):
    if self.root is None:
        return f"{self.root}"
    return f"{self.root.value}"

  def pre_order(self):
    """ Pre-order traversal of our tree """
    def walk(root):
      self.pre_values.append(root.value)

      if root.left:
        walk(root.left)
      
      if root.right:
        walk(root.right)
         
    walk(self.root)
    return self.pre_values

  def in_order(self):
    """ Pre-order traversal of our tree """
    def walk(root):

      if root.left:
        walk(root.left)

      self.in_values.append(root.value)

      if root.right:
        walk(root.right)
         
    walk(self.root)
    return self.in_values
  
  def post_order(self):
    """ Pre-order traversal of our tree """
    def walk(root):

      if root.left:
        walk(root.left)

      if root.right:
        walk(root.right)

      self.post_values.append(root.value)
   
    walk(self.root)
    return self.post_values

  # def find_maximum_value(self):
  #   """return the maximum value stored in the tree"""
  #   max_val = max(self.in_order())
  #   return max_val

  def find_maximum_value(self):
      """ find the maximum value """
      if self.root.value is not None:
          self.maximum_value = self.root.value
      else:
        raise EmptyTreeException("the tree is empty") 
      def walk(root):
        
        if root.left:
          walk(root.left)

        if self.maximum_value < root.value:
          self.maximum_value = root.value
          
        if root.right:
          walk(root.right)
      

      walk(self.root)
    
      return self.maximum_value

  # def pre_order_iter(self):
  #   stack = Stack()
  #   stack.push(self.root)

  #   while not stack.is_empty():
  #     item = stack.pop()
  #     print(item.value)

  #     if item.right is not None:
  #       stack.push(item.right)

  #     if item.left is not None:
  #       stack.push(item.left)
  
  def bread_first(self):
     # Use queque for FIFO
     self.bread_first_list = []
     queque = Queue()
     queque.enqueue(self.root)
     while not queque.is_empty():
      item = queque.dequeue()
      self.bread_first_list.append(item.value)

      if item.left is not None:
        queque.enqueue(item.left)

      if item.right is not None:
        queque.enqueue(item.right)

     return self.bread_first_list
          

class Binary_search_tree:
  def __init__(self,value=None):
    self.node = TNode(value)
  def add(self,value):
    if (self.node.value == None):
      self.node.value = value
    else:
      if value == self.node.value: 
        return 'no duplicates aloowed in binary search self'
      if (value < self.node.value):
        if(self.node.left):
          self.node.left.add(value)
        else: 
          self.node.left = Binary_search_tree(value)
      else:
        if(self.node.right):
          self.node.right.add(value)
        else: 
          self.node.right = Binary_search_tree(value)

  def in_order(self, lst = []):
    if (self.node.left):
        self.node.left.in_order(lst)
    lst.append(self.node.value)
    if (self.node.right):
        self.node.right.in_order(lst)
    return lst

  def contains(self,value,parent= None):
    if value == self.node.value: return True
    if (value < self.node.value):
      if (self.node.left):
        return self.node.left.contains(value, self.node)
      else: 
        return False
    else:
      if (self.node.right):
        return self.node.right.contains(value, self.node)
      else:
        return False


# if __name__ == "__main__":
node1 = TNode(2)
node1.left = TNode(7)
node1.left.right = TNode(6)
node1.left.right.left = TNode(5)
node1.left.right.right = TNode(11)
node1.left.left = TNode(2)
node1.right = TNode(5)
node1.right.right = TNode(9)
node1.right.right.left = TNode(4)
binary_tree = Binary_tree(node1)
print(f' here bread_first {binary_tree.bread_first()}')

  # print(binary_tree.pre_order())
  # print("-"*20)
  # print(binary_tree.in_order())

  # print("-"*20)
  # print(binary_tree.post_order())

print("the maximum is " , binary_tree.find_maximum_value())

  # sb = Binary_search_tree()
  # sb.add(5)
  # sb.add(4)
  # sb.add(3)
  # sb.add(1)
  # sb.add(2)
  # sb.add(6)
  # sb.add(100)
  # sb.add(0)
  # print(sb.contains(3),sb.contains(13))
  # print(sb.in_order())


  # I change my code to Nour Code Temporally to get the previous code with one perameter












  
# class Stack:
#   def __init__(self, node=None):
#     self.top = node
  
#   def push(self, value):
#     if not self.top:
#         self.top = Node(value)
#     else:
#         node = Node(value)
#         node.next = self.top
#         self.top = node

#   def pop(self):
#     if not self.is_empty():
#       temp_node = self.top
#       self.top = self.top.next
#       temp_node.next = None
#       return temp_node.value
#     raise Exception("Cannot pop an empty Stack")
  
#   def is_empty(self):
#     return not self.top

# class Queue:
#   def __init__(self):
#     self.front = None
#     self.rear = None

# class TNode:
#   def __init__(self, value=None):
#     self.value = value
#     self.left = None
#     self.right = None


# class BinaryTree:
#   def __init__(self, root=None):
#     self.root = root
#   def __str__(self):
#       if self.root is None:
#          return f"{self.root}"
#       return f"{self.root.value}"

#   def pre_order(self):
#     pre_order_list = []
#     """ Pre-order traversal of our tree """
#     def walk(root):
#       if root is  None:
#           raise EmptyTreeException("the tree is empty") 
#       pre_order_list.append(root.value)

#       if root.left:
#         walk(root.left)
      
#       if root.right:
#         walk(root.right)
         
#     walk(self.root)
#     return ' '.join(f"{pre_order_list}")


#   def in_order(self):
#     in_order_list = []
#     """ Pre-order traversal of our tree """
#     def walk(root):
#       if root is  None:
#           raise EmptyTreeException("the tree is empty") 

#       if root.left:
#         walk(root.left)

#       in_order_list.append(root.value)

#       if root.right:
#         walk(root.right)
         
#     walk(self.root)
#     return ' '.join(f"{in_order_list}")
  
#   def post_order(self):
#     """ Pre-order traversal of our tree """
#     post_order_list = []
#     def walk(root):
#       if root is None:
#           raise EmptyTreeException("the tree is empty") 

#       if root.left:
#         walk(root.left)

#       if root.right:
#         walk(root.right)

#       post_order_list.append(root.value)
   
#     walk(self.root)
#     return ' '.join(f"{post_order_list}")




# class Binary_search_tree:
#     def __init__(self,value=None):
#       self.node = TNode(value)
#     def add(self,value):
#         if (self.node.value == None):
#             self.node.value = value
#         else:
#             if value == self.node.value: return 'no duplicates aloowed in binary search self'
#             if (value < self.node.value):
#                 if(self.node.left):
#                     self.node.left.add(value)
#                 else: self.node.left = Binary_search_tree(value)
#             else:
#                 if(self.node.right):
#                     self.node.right.add(value)
#                 else: self.node.right = Binary_search_tree(value)

#     def in_order(self, lst = []):
#         if (self.node.left):
#             self.node.left.in_order(lst)
#         lst.append(self.node.value)
#         if (self.node.right):
#             self.node.right.in_order(lst)
#         return lst

#     def contains(self,value,parent= None):
#         if value == self.node.value: return True
#         if (value < self.node.value):
#             if (self.node.left):
#                 return self.node.left.contains(value, self.node)
#             else: return False
#         else:
#             if (self.node.right):
#                 return  self.node.right.contains(value, self.node)
#             else: return False

#   def pre_order_iter(self):
#     stack = Stack()
#     stack.push(self.root)

#     while not stack.is_empty():
#       item = stack.pop()
#       print(item.value)

#       if item.right is not None:
#         stack.push(item.right)

#       if item.left is not None:
#         stack.push(item.left)
  
#   def bread_first(self):
#      # Use queque for FIFO
#      pass





# # class BSTNode(BinaryTree):
# #     def __init__(self, value= None):
# #         self.value = value
# #         self.left = None
# #         self.right = None
# # # @pysnooper.snoop()
# # class BinarySearchTree:
# #     def __init__(self, root=None):
# #         self.root = root

            
# #     def pre_order(self):
# #         pre_order_list = []
# #         """ Pre-order traversal of our tree """
# #         def walk(root):
# #             if root is  None:
# #                 raise EmptyTreeException("the tree is empty") 
# #                 pre_order_list.append(root.value)

# #             if root.left:
# #                 walk(root.left)
            
# #             if root.right:
# #                 walk(root.right)
                
# #         walk(self.root)
# #         return ' '.join(f"{pre_order_list}")    

    

 
# #     def add(self ,root, value):
# #         if root is None:
# #             return BSTNode(value)
# #         else:
# #             if root.value == value:
# #                 return root
# #             elif root.value < value:
# #                 root.right = self.add(root.right, value)
# #             else:
# #                 root.left = self.add(root.left, value)
# #         print (f"{value} has been added successfully")
# #         return root
    
# #     def pre_order(self,root):
# #         pre_order_list = []

# #         if root is  None:
# #             raise EmptyTreeException("the tree is empty")
# #         new_root = root
# #         def pre_walk(root):
# #             if root:
# #                 pre_order_list.append(root.value)
# #                 if root.left:
# #                      pre_walk(root.left)
      
# #                 if root.right:
# #                      pre_walk(root.right)
                
# #         pre_walk(new_root)
# #         return ' '.join(f"{pre_order_list}")

   
# #     def contains(self,root,value):
# #         self.count_n = 0
# #         self.found = None
# #         if root is None:
# #             raise EmptyTreeException("the tree is empty") 
# #         def contains_search(root,value):
     
# #                 if root is None or root.value == value:
# #                     self.found = root
# #                     return root
            
# #                 if root.value < value:
# #                     self.count_n +=1
# #                     return contains_search(root.right,value)
# #                 else:
# #                      self.count_n +=1 
# #                      return contains_search(root.left,value)
# #         contains_search(root,value)
# #         if self.found is None:
# #             print("not found")
# #             return False

# #         print( f"{self.found.value} has been found and the depth of it is {self.count_n}")
# #         return True


# class Binary_search_tree:
#     def __init__(self,value=None):
#       self.node = TNode(value)
#     def add(self,value):
#         if (self.node.value == None):
#             self.node.value = value
#         else:
#             if value == self.node.value: return 'no duplicates aloowed in binary search self'
#             if (value < self.node.value):
#                 if(self.node.left):
#                     self.node.left.add(value)
#                 else: self.node.left = Binary_search_tree(value)
#             else:
#                 if(self.node.right):
#                     self.node.right.add(value)
#                 else: self.node.right = Binary_search_tree(value)

#     def in_order(self, lst = []):
#         if (self.node.left):
#             self.node.left.in_order(lst)
#         lst.append(self.node.value)
#         if (self.node.right):
#             self.node.right.in_order(lst)
#         return lst

#     def contains(self,value,parent= None):
#         if value == self.node.value: return True
#         if (value < self.node.value):
#             if (self.node.left):
#                 return self.node.left.contains(value, self.node)
#             else: return False
#         else:
#             if (self.node.right):
#                 return  self.node.right.contains(value, self.node)
#             else: return False



# if __name__ == "__main__":
#     print(BinaryTree.find_maximum_value())

#     sb = Binary_search_tree()
#     sb.add(5)
#     sb.add(4)
#     sb.add(3)
#     sb.add(1)
#     sb.add(2)
#     sb.add(6)
#     sb.add(100)
#     sb.add(0)
#     print(sb.contains(3),sb.c )
# #     obj = BinarySearchTree()
# #     bst_node = BSTNode(50)
# #     bst_node = obj.add(bst_node, 20)
# #     bst_node = obj.add(bst_node,600)
# #     bst_node = obj.add(bst_node,100)
# #     bst_node = obj.add(bst_node,1)
# #     bst_node = obj.add(bst_node,1000)
# #     print(obj.pre_order(bst_node))
# #     print(obj.contains(bst_node,0))
# #     print(obj.contains(bst_node,20))
# #     print(obj.contains(bst_node,1))



# #     print("-"*50)

# #     node1 = TNode(1)
# #     node1.left = TNode(2)
# #     node1.right = TNode(3)
# #     node1.right.left = TNode(4)
# #     node1.right.right = TNode(5)

# #     binary_tree = BinaryTree(node1)

# #     print(binary_tree.pre_order())
# #     print(binary_tree.pre_order())

# #     # binary_tree.pre_order_iter()
# #     print("-"*20)
# #     print(binary_tree.in_order())

# #     print("-"*20)
# #     print(binary_tree.post_order())


# Think about
class KNode:
  def __init__(self, value=None):
    self.value = value
    # How could you implement this for k of any size?
    self.children = []


class K_tree:
  def __init__(self, root=None):
    self.root = root


  def __str__(self):
    if self.root is None:
        return f"{self.root}"
    return f"{self.root.value}"

  def bread_first(self):
     # Use queque for FIFO
     self.bread_first_list = []
     queque = Queue()
     queque.enqueue(self.root)
     while not queque.is_empty():
      item = queque.dequeue()
      self.bread_first_list.append(item.value)

      if len(item.children) > 0 :
        for i in item.children:
          queque.enqueue(i)


     return self.bread_first_list




  def FizzBuzzTree(self):
     # Use queque for FIFO
     self.fizzbuzzlist = []
     dk_node = KNode(self.root.value)
     
     dk_node.children = self.root.children
     dummy_tree = K_tree(dk_node)

     queque = Queue()
     queque.enqueue(dummy_tree.root)
     while not queque.is_empty():
      item = queque.dequeue()
      print("the item value" , item.value)
      if item.value % 15 == 0:
       item.value = "FizzBuzz"
      elif item.value % 3 ==0 :
       item.value = 'Fizz'
      elif item.value % 5 ==0:
        item.value = 'Buzz'
      else :
        item.value = str(item.value)
      self.fizzbuzzlist.append(item.value)

      if len(item.children) > 0 :
        for i in item.children:
          queque.enqueue(i)

     print(dummy_tree.bread_first())
    #  print(self.bread_first())
     return self.fizzbuzzlist
          

  

if __name__ == "__main__":
  
  node1 = KNode(2)
  node1.children.append(KNode(7))
  node1.children.append(KNode(3))
  node1.children.append(KNode(3))
  node1.children[0].children.append(KNode(6))
  node1.children[1].children.append(KNode(2))
  node1.children[1].children.append(KNode(9))
  node1.children[2].children.append(KNode(5))
  node1.children[2].children.append(KNode(1))
  node1.children[2].children.append(KNode(8))

  k_tree = K_tree(node1)
  print(k_tree.bread_first())
  print(k_tree.FizzBuzzTree())
 


