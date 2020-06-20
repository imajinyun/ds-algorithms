import unittest

from f.avl_search_tree import AVLSearchTree


class TestAVLSearchTree(unittest.TestCase):

    def testBinarySearchTreeLength(self):
        avl = AVLSearchTree()
        self.assertEqual(0, avl.length())
        [avl.put(k, v) for k, v in enumerate(list(range(1, 10001)))]
        self.assertEqual(10000, len(avl.getTreeValues()))

    def testAVLSearchTreeGetAndPut(self):
        avl = AVLSearchTree()
        avl.put(11, 'A1')
        self.assertEqual('A1', avl.get(11))

        avl.put(22, 'B2')
        self.assertEqual('B2', avl.get(22))

        avl.put(33, 'C3')
        self.assertEqual('C3', avl.get(33))

        avl.put(44, 'D4')
        self.assertEqual('D4', avl.get(44))

        avl.put(55, 'E5')
        self.assertEqual('E5', avl.get(55))

        avl.put(66, 'F6')
        self.assertEqual('F6', avl.get(66))

        keys = []
        [keys.append(node) for node in avl]
        self.assertListEqual([11, 22, 33, 44, 55, 66], keys)
        self.assertListEqual(['D4', 'B2', 'E5', 'A1', 'C3', 'F6'], avl.getTreeValues())

    def testAVLSearchTreeRotate(self):
        avl = AVLSearchTree()
        values = ['E', 'C', 'F', 'B', 'D', 'A']
        [avl.put(i, i) for i in values]
        self.assertEqual(['C', 'B', 'E', 'A', 'D', 'F'], avl.getTreeValues())

    def testAVLSearchTreeDelete(self):
        avl = AVLSearchTree()
        values = [60, 25, 100, 17, 35, 80, 120, 30, 28]
        [avl.put(i, i) for i in values]
        self.assertEqual([60, 25, 100, 17, 30, 80, 120, 28, 35], avl.getTreeValues())

        avl.delete(120)
        self.assertEqual([60, 25, 100, 17, 30, 80, 28, 35], avl.getTreeValues())


if __name__ == '__main__':
    unittest.main()
