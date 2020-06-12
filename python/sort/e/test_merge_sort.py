import unittest

from e.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):

    def testMergeSort(self):
        a = [7, 9, 1, 3, 5]
        b = [8, 0, 2, 6, 4]
        c = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        self.assertEqual([1, 3, 5, 7, 9], merge_sort(a))
        self.assertEqual([0, 2, 4, 6, 8], merge_sort(b))
        self.assertEqual([17, 20, 26, 31, 44, 54, 55, 77, 93], merge_sort(c))


if __name__ == '__main__':
    unittest.main()
