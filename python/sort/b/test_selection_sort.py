import unittest

from b.selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    """ 测试 selection_sort.py """

    def testSelectionSort(self):
        a = [7, 9, 1, 3, 5]
        b = [8, 0, 2, 6, 4]
        self.assertEqual([1, 3, 5, 7, 9], selection_sort(a))
        self.assertEqual([0, 2, 4, 6, 8], selection_sort(b))


if __name__ == '__main__':
    unittest.main()
