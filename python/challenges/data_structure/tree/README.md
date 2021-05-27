# Trees
<!-- Short summary or background information -->
A tree data structure can be defined recursively as a collection of nodes (starting at a root node), where each node is a data structure consisting of a value, together with a list of references to nodes (the “children”), with the constraints that no reference is duplicated, and none points to the root.

A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right child.

## Challenge
<!-- Description of the challenge -->
- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
- Create a BinaryTree class
- Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
- Create a BinarySearchTree class
       -  Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
      -   Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
BST Search : O(h)
BST insert : O(n)
PreOrder : O(n)
PostOrder : O(n)
InOrder : O(n)

## API
<!-- Description of each method publicly available in each of your trees -->
add : add a value to the BST tree
pre_order : display Data in pre_order 
PostOrder : display Data in PostOrder 
InOrder : display Data in InOrder 
in_order : display data in IN_Order for BST 