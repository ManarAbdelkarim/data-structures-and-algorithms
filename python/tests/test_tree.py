from challenges.data_structure.tree.tree import *
import pytest
def test_init_empty():
    binary_tree = BinaryTree()
    actual = binary_tree.__str__()
    expected = 'None'
    assert actual == expected

def test_init_one():
 node1 = TNode(1)
 binary_tree = BinaryTree(node1) 
 actual = binary_tree.__str__()
 expected = '1'
 assert actual == expected


def test_init_right_and_left():
 node1 = TNode(1)
 node1.left = TNode(2)
 node1.right = TNode(3)
 binary_tree = BinaryTree(node1) 
 actual = [binary_tree.root.value , binary_tree.root.left.value , binary_tree.root.right.value]
 expected = [1,2,3]
 assert actual == expected 

def test_pre_order(tree_test):
 binary_tree = BinaryTree(tree_test) 
 actual = [binary_tree.pre_order()]
 expected = ['[ 1 ,   2 ,   3 ,   4 ,   5 ]']
 assert actual == expected 

def test_in_order(tree_test):
 binary_tree = BinaryTree(tree_test) 
 actual = [binary_tree.in_order()]
 expected = ['[ 2 ,   1 ,   4 ,   3 ,   5 ]']
 assert actual == expected 

def test_post_order(tree_test):
 binary_tree = BinaryTree(tree_test) 
 actual = [binary_tree.post_order()]
 expected = ['[ 2 ,   4 ,   5 ,   3 ,   1 ]']
 assert actual == expected 
 
def test_add_in_BST():
    obj = BinarySearchTree()
    bst_node = BSTNode(50)
    bst_node = obj.add(bst_node, 20)
    bst_node = obj.add(bst_node,600)
    bst_node = obj.add(bst_node,100)
    bst_node = obj.add(bst_node,1)
    bst_node = obj.add(bst_node,1000)
    actual = obj.pre_order(bst_node)
    expected = '[ 5 0 ,   2 0 ,   1 ,   6 0 0 ,   1 0 0 ,   1 0 0 0 ]'
    assert actual == expected

def test_contains(tree_test):
    obj = BinarySearchTree()
    bst_node = BSTNode(50)
    bst_node = obj.add(bst_node, 20)
    bst_node = obj.add(bst_node,600)
    bst_node = obj.add(bst_node,100)
    bst_node = obj.add(bst_node,1)
    bst_node = obj.add(bst_node,1000)
    actual = [obj.pre_order(bst_node) , obj.contains(bst_node,0) , obj.contains(bst_node,20) , obj.contains(bst_node,1)]
    expected = ['[ 5 0 ,   2 0 ,   1 ,   6 0 0 ,   1 0 0 ,   1 0 0 0 ]', False, True, True]
    assert actual == expected 

@pytest.fixture
def tree_test():
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    node1.right.left = TNode(4)
    node1.right.right = TNode(5)
    return node1