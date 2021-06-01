from challenges.data_structure.tree.tree import *
import pytest
def test_k_array(node1_test):
    
  k_tree = K_tree(node1_test)
 
  actual = k_tree.FizzBuzzTree()
  expected = ['2', '7', 'Fizz', 'Fizz', 'Fizz', '2', 'Fizz', 'Buzz', '1', '8']
  assert actual == expected


@pytest.fixture
def node1_test():
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
  return node1
