import unittest

from f.quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):

    def testQuickSort(self):
        a = [7, 9, 1, 3, 5]
        b = [8, 0, 2, 6, 4]
        c = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        self.assertEqual([1, 3, 5, 7, 9], quick_sort(a))
        self.assertEqual([0, 2, 4, 6, 8], quick_sort(b))
        self.assertEqual([17, 20, 26, 31, 44, 54, 55, 77, 93], quick_sort(c))


if __name__ == '__main__':
    unittest.main()
