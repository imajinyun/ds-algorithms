import unittest

from a.bubble_sort import *


class TestBubbleSort(unittest.TestCase):
    """ 测试 bubble_sort.py """

    def testBubbleSort(self):
        a = [9, 5, 7, 1, 3]
        self.assertEqual([1, 3, 5, 7, 9], bubble_sort(a))
        self.assertEqual([1, 3, 5, 7, 9], bubble_sort2(a))
        self.assertEqual([1, 3, 5, 7, 9], bubble_sort3(a))

        b = [8, 0, 2, 4, 6]
        self.assertEqual([0, 2, 4, 6, 8], bubble_sort(b))
        self.assertEqual([0, 2, 4, 6, 8], bubble_sort2(b))
        self.assertEqual([0, 2, 4, 6, 8], bubble_sort3(b))


if __name__ == '__main__':
    unittest.main()
