##
from challenges.data_structure.graph.graph import *

def business_trip(graph, array) :
     trip_cost = 0
     feasible = True
     values = graph.adjacencyList. items()

     array_of_values = [*values]
     filtered = []
     for place in array_of_values:
         if  place in array:
             filtered.append(place)


     for i in range (0,len(filtered)):
      if array[i] == filtered[i][0].value:
        trip_cost += filtered[i][1][0].weight
      else:
        feasible = False

     if feasible :
      return f'{True}, Cost:{trip_cost}'
     else :
      return False


if __name__ == "__main__":
    myGraph =  Graph()
    zero =  Vertex("zarqa")
    two =  Vertex("Amman")
    three =  Vertex("irbid")
    four =  Vertex("jarash")
    trips = ["Amman", "irbid", "jarash"]

    myGraph.add_vertex(zero)
    myGraph.add_vertex(two)
    myGraph.add_vertex(three)
    myGraph.add_vertex(four)

    myGraph.add_edge(zero, two, 100)
    myGraph.add_edge(two, three, 50)
    myGraph.add_edge(three, four, 20)

    print(business_trip(myGraph, trips))
