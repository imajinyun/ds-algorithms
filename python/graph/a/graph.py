from a.vertex import Vertex


class Graph:

    def __init__(self) -> None:
        self.vertices = {}
        self.size = 0

    def __iter__(self) -> iter:
        return iter(self.vertices.values())

    def length(self) -> int:
        return self.size

    def __contains__(self, key):
        return self.vertices[key] if key in self.vertices else None

    def addVertex(self, key) -> Vertex:
        vertex = Vertex(key)
        self.vertices[key] = vertex
        self.size += 1

        return vertex

    def addEdge(self, fm, to, cost=0) -> None:
        if fm not in self.vertices:
            self.addVertex(fm)
        if to not in self.vertices:
            self.addVertex(to)
        self.vertices[fm].addNeighbor(self.vertices[to], cost)

    def getVertex(self, key) -> Vertex:
        return self.vertices[key]

    def getVertices(self):
        return self.vertices.keys()
