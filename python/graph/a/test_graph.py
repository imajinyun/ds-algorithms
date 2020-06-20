import unittest

from a.graph import Graph


class TestGraph(unittest.TestCase):

    def testGraphAddVertex(self):
        graph = Graph()
        self.assertEqual(1, graph.addVertex(1).getKey())
        self.assertEqual('A', graph.addVertex('A').getKey())

        self.assertTrue(1 in graph.getVertices())
        self.assertTrue('A' in graph.getVertices())
        self.assertFalse('a' in graph.getVertices())

    def testGraphAddEdge(self):
        graph = Graph()
        [graph.addVertex(k) for k in range(6)]
        graph.addEdge(0, 1, 5)
        graph.addEdge(0, 5, 2)
        graph.addEdge(1, 2, 4)
        graph.addEdge(2, 3, 9)
        graph.addEdge(3, 4, 7)
        graph.addEdge(3, 5, 3)
        graph.addEdge(4, 0, 1)
        graph.addEdge(5, 4, 8)
        graph.addEdge(5, 2, 1)

        items, keys = [1, 5, 2, 3, 4, 5, 0, 4, 2], []
        for key, vertex in enumerate(graph):
            for item in vertex.getAllVertices():
                self.assertEqual(key, vertex.getKey())
                keys.append(item.getKey())
        self.assertEqual(items, keys)


if __name__ == '__main__':
    unittest.main()
