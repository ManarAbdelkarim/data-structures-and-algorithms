from challenges.graph_business_trip.graph_business_trip import *
import pytest
def test(fixture):
    trips = ["Amman", "irbid"]
    actual = business_trip(fixture, trips)
    expected = "True, Cost:70"
    assert actual == expected




@pytest.fixture()
def fixture():
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
    return myGraph




