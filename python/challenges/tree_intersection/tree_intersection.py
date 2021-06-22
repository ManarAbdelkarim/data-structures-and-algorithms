

class Node():
  def __init__(self, data=None):
      self.data = data
      self.next = None
  def __str__(self):
    return f"{self.data}"


class LinkedList:
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
        '''
        this method to append value in the last node
        input ==> value
        '''
        if value is None:
            raise  TypeError("insert() missing 1 required positional argument: 'value' ")
        else:
            new_node = Node(value)
            if not self.head:
                self.head = new_node
            else:
                new_node = Node(value)
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

class Hashmap:

    def __init__(self, size = 1024):
        """[summary]
        No default inputs.
        """
        self.size = size
        self.buckets = [None] * size


    def hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)*int(key)
        hashed_key = (sum *19)% self.size
        return hashed_key

    def add(self, key, value):
        """[summary]
        Hashes key, adds key and value pair to table. Handles collisions as necessary.
        Args:
            key ([type]): [description]
            value ([int]): [description]
        """

        index = self.hash(key)

        if self.buckets[index] == None:
            bucket = LinkedList()

        else:
            bucket = self.buckets[index]    # bucket is now a linked list

        bucket.append(
            {
                'key': key,
                'value': value,
            }
        )

        self.buckets[index] = bucket

    def get(self, key):
        """[summary]
        Takes in key and returns the value from the table. Handles collisions as necessary.
        Args:
            key ([string]): [description]
        Raises:
            KeyError: [if key not found]
            KeyError: [if key is invalid]
        Returns:
            [string]: [returns the value of hashed key]
        """
        idx = self.hash(key)
        bucket = self.buckets[idx]

        if bucket == None:
            return None

        current = bucket.head

        while current:

            if current.data['key'] == key:
                return current

            current = current.next

        return None



class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, data):
        node = Node(data)

        if not self.front:
            self.front = node
        else:
            current = self.front
            while current.next:
                current = current.next
            current.next = node
            node.next = None

    def dequeue(self):
        if not self.isEmpty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.data
        return "empty"

    def isEmpty(self):
        if self.front:
            return False
        return True

class TNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def preOrder(self):
        tree = []

        if self.root:

            def walk(node):

                tree.append(node.data)

                if node.left:
                    walk(node.left)

                if node.right:
                    walk(node.right)

            walk(self.root)
            return tree

        else:
            return "tree is empty"

    def inOrder(self):
        tree = []

        if self.root:

            def walk(node):

                if node.left:
                    walk(node.left)

                tree.append(node.data)

                if node.right:
                    walk(node.right)

            walk(self.root)
            return tree

        else:
            return "tree is empty"

    def postOrder(self):
        tree = []

        if self.root:

            def walk(node):

                if node.left:
                    walk(node.left)

                if node.right:
                    walk(node.right)

                tree.append(node.data)

            walk(self.root)
            return tree

        else:
            return "tree is empty"

    def find_maximum_value(self):

        maximum_value = self.root.data

        def walk(root):

            nonlocal maximum_value

            if root.data > maximum_value:
                maximum_value = root.data

            if root.left:
                walk(root.left)

            if root.right:
                walk(root.right)

            return maximum_value

        return walk(self.root)

    def breadth_first(self):
        q = Queue()

        q.enqueue(self.root)

        result = []

        temp = None

        while not q.isEmpty():

            temp = q.dequeue()

            result.append(temp.data)

            if temp.left:
                q.enqueue(temp.left)

            if temp.right:
                q.enqueue(temp.right)

        return result


def tree_intersection(fTree, sTree):
    fTreeInOrder = fTree.inOrder();
    sTreeInOrder = sTree.inOrder();
    if len(fTreeInOrder) == 0:
        return []
    if len(sTreeInOrder) == 0:
        return []
    result = [];
    myHashTable = Hashmap();

    for  node_value in fTreeInOrder:
         myHashTable.add(f'{node_value}', node_value)

    for  i in sTreeInOrder:
        find = myHashTable.get(f'{i}')
        if find and find.data['key'] not in result :
             result.append(find.data['key'])

    return result;


if __name__ == "__main__":
	tree1 = TNode(150)
	tree1.left = TNode(100)
	tree1.left.left = TNode(75)
	tree1.left.right = TNode(160)
	tree1.left.right.left = TNode(125)
	tree1.left.right.right = TNode(175)
	tree1.right = TNode(250)
	tree1.right.left = TNode(200)
	tree1.right.right = TNode(350)
	tree1.right.right.left = TNode(300)
	tree1.right.right.right = TNode(500)
	tree1.right.right.right.right = TNode(500)

	binary_tree1 = BinaryTree(tree1)
	tree2 = TNode(42)
	tree2.left = TNode(100)
	tree2.left.left = TNode(15)
	tree2.left.right = TNode(160)
	tree2.left.right.left = TNode(125)
	tree2.left.right.right = TNode(175)
	tree2.right = TNode(600)
	tree2.right.left = TNode(200)
	tree2.right.right = TNode(350)
	tree2.right.right.left = TNode(4)
	tree2.right.right.right = TNode(500)
	tree2.right.right.right.right = TNode(500)


	binary_tree2 = BinaryTree(tree2)
	print(tree_intersection(binary_tree1, binary_tree2))


