from collections import deque
# from challenges.data_structure.stacks_and_queues.stacks_and_queues import *
from collections import deque, defaultdict

# from _pytest import capture


class Queue():

    def __init__(self) -> None:

        self.dq = deque()

    def enqueue(self, value):

        self.dq.appendleft(value)

    def dequeue(self):

        return self.dq.pop()

    def __len__(self):

        return len(self.dq)

class Vertex:
  def __init__(self,value):
    self.value = value

class Edge:
  def __init__(self,vertex, weight =0):
    self.vertex = vertex
    self.weight = weight

class Graph:

  def __init__(self):
    self.adjacencyList = {}


  def add_vertex(self,vertex):

    self.adjacencyList[vertex] =[]
    return self.adjacencyList.get(vertex)
  def add_vertex_directly(self,char):
    vertex = Vertex(char)
    self.adjacencyList[vertex] =[]
    return vertex

  def add_edge(self,start, end, weight =0):
    if not start in self.adjacencyList or  not end in self.adjacencyList:
      raise Exception('NON-EXISTENT VERTEX SITUATION 😱')

    edge = Edge(end, weight)
    self.adjacencyList[start].append(edge)
    return self.adjacencyList.get(start)
#   def get_vertices(self):
#     if not len(self.adjacencyList):
#         raise Exception('GRAPH IS EMPTY 😱')

#     collection = []
#     for k in self.adjacencyList.keys():
#       collection.append(k.value)
#     return collection

  def get_vertices(self):
      return self.adjacencyList.keys()




  def get_unique_vertices(self):
    if not self.size():
         raise Exception('GRAPH IS EMPTY 😱')

    collection = set()
    for k in self.adjacencyList.keys():
      collection.add(k.value)

    return collection


  def get_children (self,vertex):
      result = []
      if len(self.adjacencyList.get(vertex)):
          print('whats wront with', self.adjacencyList.get(vertex))
          for l in range(len(self.adjacencyList.get(vertex))):
            result.append([self.adjacencyList.get(vertex)[l].vertex.value,self.adjacencyList.get(vertex)[l].weight])
      return result

  def get_neighbors(self, vertex):

        return self.adjacencyList.get(vertex, [])

  def __iter__(self):
        """[summary]
            magic function to iterate over the Graph
        Returns:
            [type]: [description]
        """
        self._iter_obj = iter(self.adjacencyList)
        return self._iter_obj


  def breadth_first(self, node):
        queue = Queue()
        visited = set()
        output = []
        visited.add(node)
        queue.enqueue(node)
        while len(queue):
            cuttent_v = queue.dequeue()
            output.append(cuttent_v)
            neighbors = self.get_neighbors(cuttent_v)
            for edge in neighbors:
                vert = edge.vertex
                if vert not in visited:
                    visited.add(vert)
                    queue.enqueue(vert)
        return output

  def DFS(self):
        """
        Graph Depth First Search
        """
        visited = set()
        lst = []
        vertex = next(iter(self.get_vertices()))
        def DFS_helper(vertex):
            visited.add(vertex)
            neighbors = self.get_neighbors(vertex)
            lst.append(vertex.value)
            for neighbor in neighbors:
                if neighbor.vertex not in visited:
                    DFS_helper(neighbor.vertex)
        DFS_helper(vertex)
        return lst



  def size(self):
    return len(self.adjacencyList)



if __name__ == "__main__":
  g =  Graph()
  zero =  Vertex(0)
  one =  Vertex(1)
  two =  Vertex(2)
  twoToo =  Vertex(2)
  three =  Vertex(3)
  four =  Vertex(4)
  fourToo =  Vertex(4)
  five =  Vertex(5)

#   g.add_vertex(zero)
  g.add_vertex(one)
  g.add_vertex(two)
#   g.add_vertex(twoToo)
  g.add_vertex(three)
  g.add_vertex(four)
#   g.add_vertex(fourToo)
  g.add_vertex(five)

  g.add_edge(one, two, 3)
  g.add_edge(one, three)
  g.add_edge(one, four)
  g.add_edge(three, five)
  g.add_edge(four, five)
#   print('here',g.add_edge(one, three))

#   print('size🎉',g.size())
#   print(g.get_vertices())
#   print(g.get_unique_vertices())
#   print('heree',g.get_neighbors(zero))
# print(g.adjacencyList[three])
# x = g.breadth_first(one)
# print(x[0].value)
# for i in range(0,3):
#     # print(g.adjacencyList[one][i].vertex.value)
#     print(x[i].vertex.value)

#   print(g.get_all())

gl = Graph()


A = gl.add_vertex_directly('A')
B = gl.add_vertex_directly('B')
C = gl.add_vertex_directly('C')
G = gl.add_vertex_directly('G')
D = gl.add_vertex_directly('D')
E = gl.add_vertex_directly('E')
H = gl.add_vertex_directly('H')
F = gl.add_vertex_directly('F')
print(F)
gl.add_edge(A, B)
gl.add_edge(A, D)
gl.add_edge(B, C)
gl.add_edge(C, G)
gl.add_edge(D, E)
gl.add_edge(D, H)
gl.add_edge(D, F)
gl.add_edge(H, F)

print(gl.DFS())
