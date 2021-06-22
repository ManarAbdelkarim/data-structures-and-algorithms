from challenges.tree_intersection.tree_intersection import *
import pytest

def test_tree_intersection(tree_test1, list_test2):
    actual = tree_intersection(tree_test1, list_test2)
    expected =  ['100', '125', '160', '175', '200', '350', '500']
    assert actual == expected


################################################################

@pytest.fixture
def tree_test1():
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
    return binary_tree1
@pytest.fixture
def list_test2():
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
    return binary_tree2




