class Vertex:

    def __init__(self, key) -> None:
        self.key = key
        self.vto = {}

    def __str__(self) -> str:
        return str(self.key) + 'vertexTo: ' + str([x.key for x in self.vto])

    def addNeighbor(self, neighbor, weight=0) -> None:
        self.vto[neighbor] = weight

    def getAllVertices(self):
        return self.vto.keys()

    def getKey(self):
        return self.key

    def getWeight(self, neighbor):
        return self.vto[neighbor]
