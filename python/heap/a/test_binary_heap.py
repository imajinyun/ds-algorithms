import unittest

from a.binary_heap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):

    def setUp(self) -> None:
        self.heap = BinaryHeap()

    def testBinaryHeapIsEmpty(self):
        self.assertTrue(self.heap.isEmpty())

    def testBinaryHeapSize(self):
        self.assertEqual(0, self.heap.size())

    def testBinaryHeapInsert(self):
        self.heap.insert(1)
        self.heap.insert(8)
        self.heap.insert(2)
        self.heap.insert(9)
        self.heap.insert(3)
        self.heap.insert(7)
        self.heap.insert(6)
        self.heap.insert(4)
        self.heap.insert(5)

        self.assertEqual(9, self.heap.size())
        self.assertFalse(self.heap.isEmpty())
        self.assertEqual([0, 1, 3, 2, 4, 8, 7, 6, 9, 5], self.heap.heap)

    def testBinaryHeapBuildHeap(self):
        items = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
        self.heap.buildHeap(items)
        self.assertEqual([0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27], self.heap.heap)
        self.assertEqual(10, self.heap.size())

        self.heap.insert(7)
        """
        加入新节点（7，加入前导符 0 是为了对称对齐）后的树结构：
                   05
              07        11
          14      09  19  21
        33  17  27  18
        """
        self.assertEqual([0, 5, 7, 11, 14, 9, 19, 21, 33, 17, 27, 18], self.heap.heap)

        self.assertEqual(5, self.heap.delMinElement())
        """
        从树中删除节点并调整后的树结构：
                   18
              07        11
          14      09  19  21
        33  17  27
        """
        self.assertEqual([0, 18, 7, 11, 14, 9, 19, 21, 33, 17, 27], self.heap.heap)

        self.assertEqual(18, self.heap.delMinElement())
        """
        从树中删除节点并调整后的树结构：
                   27
              07        11
          14      09  19  21
        33  17
        """
        self.assertEqual([0, 27, 7, 11, 14, 9, 19, 21, 33, 17], self.heap.heap)

        self.assertEqual(27, self.heap.delMinElement())
        """
        从树中删除节点并调整后的树结构：
                   17
              07        11
          14      09  19  21
        33
        """
        self.assertEqual([0, 17, 7, 11, 14, 9, 19, 21, 33], self.heap.heap)

        self.assertEqual(17, self.heap.delMinElement())
        """
        从树中删除节点并调整后的树结构：
                 33
            07        11
        14      09  19  21
        """
        self.assertEqual([0, 33, 7, 11, 14, 9, 19, 21], self.heap.heap)

        self.assertEqual(33, self.heap.delMinElement())
        """
        从树中删除节点并调整后的树结构：
                 21
            07        11
        14      09  19
        """
        self.assertEqual([0, 21, 7, 11, 14, 9, 19], self.heap.heap)

        self.assertEqual(21, self.heap.delMinElement())
        """
        从树中删除节点并调整后的树结构：
                 21
            07        11
        14      09  19
        """
        self.assertEqual([0, 19, 7, 11, 14, 9], self.heap.heap)

        self.assertEqual(19, self.heap.delMinElement())
        """
        从树中删除节点并调整后的树结构：
                 09
            07        11
        14
        """
        self.assertEqual([0, 9, 7, 11, 14], self.heap.heap)

        self.assertEqual(9, self.heap.delMinElement())
        """
        从树中删除节点并调整后的树结构：
             14
        07        11
        """
        self.assertEqual([0, 14, 7, 11], self.heap.heap)

        self.assertEqual(14, self.heap.delMinElement())
        """
        从树中删除节点并调整后的树结构：
             11
        07
        """
        self.assertEqual([0, 11, 7], self.heap.heap)

        """
        从树中删除节点并调整后的树结构：
        07
        """
        self.assertEqual(11, self.heap.delMinElement())
        self.assertEqual([0, 7], self.heap.heap)

        self.assertEqual(7, self.heap.delMinElement())
        self.assertEqual(0, self.heap.size())
        self.assertTrue(self.heap.isEmpty())


if __name__ == '__main__':
    unittest.main()
