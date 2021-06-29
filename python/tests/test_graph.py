from challenges.data_structure.graph.graph import *
import pytest

# Node can be successfully added to the graph
def test_add_vertex():
    g =  Graph()
    zero =  Vertex(0)
    actual = g.add_vertex(zero)
    expected =[]
    assert actual == expected


# An edge can be successfully added to the graph
def test_add_edge():
    g =  Graph()
    zero =  Vertex(0)
    one =  Vertex(1)
    g.add_vertex(zero)
    g.add_vertex(one)
    actual = g.add_edge(one, zero, 3)[0].weight
    expected = 3
    assert actual == expected
# A collection of all nodes can be properly retrieved from the graph
def test_add_nodes(test_):
    actual = test_.get_unique_vertices()
    expected = {0, 1, 2, 3, 4, 5}
    assert actual == expected

# Neighbors are returned with the weight between nodes included
def test_get_nighbors():
    g =  Graph()
    zero =  Vertex(0)
    one =  Vertex(1)
    two =  Vertex(2)
    g.add_vertex(zero)
    g.add_vertex(one)
    g.add_vertex(two)
    g.add_edge(zero, two, 3)
    g.add_edge(zero, one)
    actual = g.get_children(zero)
    expected = [[2,3],[1,0]]
    assert actual == expected

# The proper size is returned, representing the number of nodes in the graph
def test_size(test_):
    actual = test_.size()
    expected = 8
    assert actual == expected

# A graph with only one node and edge can be properly returned

def test_get_nighbors_one_node():
    g =  Graph()
    zero =  Vertex(0)
    g.add_vertex(zero)
    g.add_edge(zero, zero, 3)
    actual = g.get_children(zero)
    expected = [[0,3]]
    assert actual == expected

def test_breadth_first():
    g =  Graph()
    zero =  Vertex(0)
    one =  Vertex(1)
    two =  Vertex(2)
    twoToo =  Vertex(2)
    three =  Vertex(3)
    four =  Vertex(4)
    fourToo =  Vertex(4)
    five =  Vertex(5)

    g.add_vertex(zero)
    g.add_vertex(one)
    g.add_vertex(two)
    g.add_vertex(twoToo)
    g.add_vertex(three)
    g.add_vertex(four)
    g.add_vertex(fourToo)
    g.add_vertex(five)

    g.add_edge(one, two, 3)
    g.add_edge(one, three)
    g.add_edge(one, four)
    g.add_edge(three, five)
    g.add_edge(four, five)
    actual = []
    x = g.breadth_first(one)
    for v in x:
        actual.append(v.value)
    expected = [1, 2, 3, 4, 5]
    assert expected == actual

def test_breadth_first_search(test_BFS):
    actual = test_BFS.BFS()
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    assert actual == expected



@pytest.fixture
def test_():
  g =  Graph()
  zero =  Vertex(0)
  one =  Vertex(1)
  two =  Vertex(2)
  twoToo =  Vertex(2)
  three =  Vertex(3)
  four =  Vertex(4)
  fourToo =  Vertex(4)
  five =  Vertex(5)

  g.add_vertex(zero)
  g.add_vertex(one)
  g.add_vertex(two)
  g.add_vertex(twoToo)
  g.add_vertex(three)
  g.add_vertex(four)
  g.add_vertex(fourToo)
  g.add_vertex(five)

  return g

@pytest.fixture
def test_BFS():
    gl = Graph()
    A = gl.add_vertex_directly('A')
    B = gl.add_vertex_directly('B')
    C = gl.add_vertex_directly('C')
    G = gl.add_vertex_directly('G')
    D = gl.add_vertex_directly('D')
    E = gl.add_vertex_directly('E')
    H = gl.add_vertex_directly('H')
    F = gl.add_vertex_directly('F')
    gl.add_edge(A, B)
    gl.add_edge(A, D)
    gl.add_edge(B, C)
    gl.add_edge(C, G)
    gl.add_edge(D, E)
    gl.add_edge(D, H)
    gl.add_edge(D, F)
    gl.add_edge(H, F)
    return gl
