# from challenges.data_structure.tree.tree import *
# import pytest
# def test_init_empty():
#     binary_tree = Binary_tree()
#     actual = binary_tree.__str__()
#     expected = 'None'
#     assert actual == expected

# def test_init_one():
#  node1 = TNode(1)
#  binary_tree = Binary_tree(node1)
#  actual = binary_tree.__str__()
#  expected = '1'
#  assert actual == expected


# def test_init_right_and_left():
#  node1 = TNode(1)
#  node1.left = TNode(2)
#  node1.right = TNode(3)
#  binary_tree = Binary_tree(node1)
#  actual = [binary_tree.root.value , binary_tree.root.left.value , binary_tree.root.right.value]
#  expected = [1,2,3]
#  assert actual == expected

# def test_pre_order(tree_test):
#  binary_tree = Binary_tree(tree_test)
#  actual = [binary_tree.pre_order()]
#  expected = [[1, 2, 3, 4, 5]]
#  assert actual == expected

# def test_in_order(tree_test):
#  binary_tree = Binary_tree(tree_test)
#  actual = [binary_tree.in_order()]
#  expected = [[2, 1, 4, 3, 5]]
#  assert actual == expected

# def test_post_order(tree_test):
#  binary_tree = Binary_tree(tree_test)
#  actual = [binary_tree.post_order()]
#  expected =  [[2, 4, 5, 3, 1]]
#  assert actual == expected

# def test_add_in_BST():
#     sb = Binary_search_tree()
#     sb.add(50)
#     sb.add(20)
#     sb.add(600)
#     sb.add(100)
#     sb.add(1)
#     sb.add(1000)
#     actual = sb.in_order()
#     expected = [1, 20, 50, 100, 600, 1000]
#     assert actual == expected

# def test_contains(tree_test):
#     sb = Binary_search_tree()
#     sb.add(50)
#     sb.add(20)
#     sb.add(600)
#     sb.add(100)
#     sb.add(1)
#     sb.add(1000)
#     actual = [ sb.contains(0) , sb.contains(20) , sb.contains(1)]
#     expected = [False, True, True]
#     assert actual == expected

# def test_maximum_empty():
#     node1 = TNode()
#     binary_tree = Binary_tree(node1)
#     with pytest.raises(EmptyTreeException):
#         binary_tree.find_maximum_value()
# def test_maximum():
#   node1 = TNode(4)
#   node1.left = TNode(2)
#   node1.right = TNode(3)
#   node1.right.left = TNode(1)
#   node1.right.right = TNode(5)
#   binary_tree = Binary_tree(node1)
#   actual = binary_tree.find_maximum_value()
#   expected = 5
#   assert actual == expected


# def test_breadth_first(tree_breadth):
#     actual = tree_breadth.bread_first()
#     expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
#     assert actual == expected




# @pytest.fixture
# def tree_test():
#     node1 = TNode(1)
#     node1.left = TNode(2)
#     node1.right = TNode(3)
#     node1.right.left = TNode(4)
#     node1.right.right = TNode(5)
#     return node1


# @pytest.fixture
# def tree_breadth():
#     node1 = TNode(2)
#     node1.left = TNode(7)
#     node1.left.right = TNode(6)
#     node1.left.right.left = TNode(5)
#     node1.left.right.right = TNode(11)
#     node1.left.left = TNode(2)
#     node1.right = TNode(5)
#     node1.right.right = TNode(9)
#     node1.right.right.left = TNode(4)
#     binary_tree = Binary_tree(node1)
#     return binary_tree
