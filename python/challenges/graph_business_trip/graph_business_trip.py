##
from challenges.data_structure.graph.graph import *
from challenges.data_structure.stacks_and_queues.stacks_and_queues import *


def business_trip(graph, array):
    trip_cost = 0
    feasible = True
    values = graph.adjacencyList.items()

    array_of_values = [*values]
    filtered = []

    for place in array_of_values:
        if place[0].value in array:
            filtered.append(place)
    for i,elem in enumerate(filtered):
        if array[i] == elem[0].value:


            if elem[0].value == filtered[i][0].value:
                trip_cost += filtered[i][1][0].weight
            else:
                feasible = False

    if feasible:
        return f"{True}, Cost:{trip_cost}"
    else:
        return False


undirectedEdges = [
  [0, 1],
  [1, 2],
  [2, 0],
  [3, 4]
];


def bipartite(graph, src):
    q = Queue()
    flag = {}
    flag[src] = 'A'
    q.enqueue([src,None])
    while not q.is_empty() :
        temp = q.dequeue()
        if temp[1] and temp[0] not in flag.keys():
            if flag[temp[1]] =='A':
                flag[temp[0]] = 'B'
            else:
                flag[temp[0]] = 'A'
        for neighbor in graph.get_neighbors(temp[0]):
            if neighbor.vertex in flag.keys() :
                if flag[neighbor.vertex] == flag[temp[0]]:
                    return False
            if not neighbor.vertex in flag.keys() :
                q.enqueue([neighbor.vertex,temp[0]])
    return True


# const undirectedEdges = [
#   [0, 1],
#   [1, 2],
#   [1, 3],
# ];
def minimum_Height_Tree( n: int, edges: list) -> list:
    if n <= 2:
        return [x for x in range(n) ]

    adj = [set() for x in range(n)]
    for start, end in edges:
        adj[start].add(end)
        adj[end].add(start)

    print(adj)
    leaves = []
    for i in range(n):
       if  len(adj[i]) == 1:
           leaves.append(i)

    remaining = n
    while remaining > 2:
        remaining -= len(leaves)
        temp = []
        for leaf in leaves:
            for idx in adj[leaf]:
                adj[idx].remove(leaf)
                if len(adj[idx]) == 1:
                    temp.append(idx)
        leaves = temp
    return leaves

#######################




# def connected_component(undirectedEdges):
#     g = Graph()
#     added_list = set()
#     for undirectedEdge in undirectedEdges:
#         if undirectedEdge[0] not in added_list:
#             v1 = g.add_vertex_directly(undirectedEdge[0])
#         if undirectedEdge[1] not in added_list:
#             v2 = g.add_vertex_directly(undirectedEdge[1])
#         g.add_undirected_edge(v1,v2)
#     print(g.adjacencyList)
#     visited = set()
#     counter = 0
#     def dfs(vertex, visited):
#          if vertex not in visited:
#              visited.add(vertex)
#              for neighbor in g.get_neighbors(vertex):
#                  dfs(neighbor, visited)

#     for vertex in g.adjacencyList.keys():
#         if not vertex in visited:
#             dfs(vertex, visited)
#             counter +=1

#     return counter




def connected_component(adjacencyList):
    g = Graph()
    g.adjacencyList = adjacencyList
    visited = set()
    counter = 0
    def dfs(vertex, visited):
         if vertex not in visited:
             visited.add(vertex)
             for neighbor in g.get_neighbors(vertex):
                 dfs(neighbor, visited)

    for vertex in g.adjacencyList.keys():
        if not vertex in visited:
            dfs(vertex, visited)
            counter +=1

    return counter

def connected_component(adjacencyList):
    g = Graph()
    g.adjacencyList = adjacencyList
    visited = set()
    counter = 0
    def dfs(vertex, visited):
         if vertex not in visited:
             visited.add(vertex)
             for neighbor in g.get_neighbors(vertex):
                 dfs(neighbor, visited)

    for vertex in g.adjacencyList.keys():
        if not vertex in visited:
            dfs(vertex, visited)
            counter +=1

    return counter











if __name__ == "__main__":
    myGraph =  Graph()
    Zarqa =  Vertex("zarqa")
    Amman =  Vertex("Amman")
    Irbid =  Vertex("irbid")
    Jarash =  Vertex("jarash")
    trips = ["Amman", "irbid"]

    myGraph.add_vertex(Zarqa)
    myGraph.add_vertex(Amman)
    myGraph.add_vertex(Irbid)
    myGraph.add_vertex(Jarash)

    myGraph.add_edge(Zarqa, Amman, 100)
    myGraph.add_edge(Amman, Irbid, 50)
    myGraph.add_edge(Irbid, Jarash, 20)
    # print( bipartite(myGraph, Zarqa))

    graph = Graph()
    one =Vertex('1')
    two =Vertex('2')
    three =Vertex('3')
    four =Vertex('4')
    # five =Vertex('5')
    six =Vertex('6')


    graph.add_vertex(one)
    graph.add_vertex(two)
    graph.add_vertex( three )
    graph.add_vertex(four)
    # graph.add_vertex(five)
    graph.add_vertex(six)


    graph.add_undirected_edge(one, three, 100)
    graph.add_undirected_edge(three, two, 50)
    graph.add_undirected_edge(two, four, 20)
    # graph.add_undirected_edge(four, five, 100)
    # graph.add_undirected_edge(five, six, 50)
    graph.add_undirected_edge(six, three, 20)
    # print(graph.adjacencyList)
    # print('here we have',graph.get_neighbors(one)[0].vertex.value)
    # print(graph.DFS())
    # lets =[]
    # for key in graph.adjacencyList.keys():
    #     for value in graph.adjacencyList[key]:
    #         lets.append(value.vertex.value)
    #     print('key', key.value , ':', lets)
    #     lets = []
    # print( bipartite(graph, one))
    undirectedEdges = [
  [0, 1],
  [0,6],
  [3,4],
  [3,5],
  [1, 2],
  [1, 3],
];
    # adj : [[1,6],[0,2,3],[1],[1, 4,5]]

    # print(minimum_Height_Tree(undirectedEdges , 7))
    # print(minimum_Height_Tree( 7,undirectedEdges))





    print(business_trip(myGraph, trips))

    # adjacencyList = {0: [1, 2], 1: [2, 0], 2: [0], 3: [4], 4: [3], 5:[]}

    # print('the answer :' ,connected_component(adjacencyList))
