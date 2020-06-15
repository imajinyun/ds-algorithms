import unittest

from e.binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def testBinarySearchTreeLength(self):
        bst = BinarySearchTree()
        self.assertEqual(0, bst.length())

    def testBinarySearchTreeGetAndPut(self):
        bst = BinarySearchTree()
        bst.put(1, 'a')
        self.assertEqual('a', bst.get(1))

        bst.put(2, 'b')
        self.assertEqual('b', bst.get(2))

        bst.put(3, 'c')
        self.assertEqual('c', bst.get(3))

        bst.put(4, 'd')
        self.assertEqual('d', bst.get(4))

        bst.put(5, 'e')
        self.assertEqual('e', bst.get(5))

        bst.put(6, 'f')
        self.assertEqual('f', bst.get(6))

        items = []
        for node in bst:
            items.append(node)
        self.assertEqual([1, 2, 3, 4, 5, 6], items)

    def testBinarySearchTreeDelete(self):
        bst = BinarySearchTree()
        bst.put(1, 'A')
        bst.put(2, 'B')
        bst.put(3, 'C')
        bst.put(4, 'D')
        bst.put(5, 'E')

        bst.delete(2)
        self.assertEqual(4, bst.length())

        items = []
        [items.append(k) for k in bst]
        self.assertEqual([1, 3, 4, 5], items)

        items = []
        bst.delete(3)
        [items.append(k) for k in bst]
        self.assertEqual([1, 4, 5], items)


if __name__ == '__main__':
    unittest.main()
