import unittest

from pass_potato import pass_potato


class TestPassPotato(unittest.TestCase):
    """ 测试 pass_potato.py """

    def testPassPotato(self):
        self.assertEqual('c', pass_potato(['a', 'b', 'c', 'd', 'e', 'f'], 7))
        self.assertEqual(1, pass_potato([1, 2, 3, 4, 5], 7))

        self.assertEqual('A', pass_potato(['A', 'B', 'C'], 5))
        self.assertEqual(False, pass_potato([True, False], 2 ** 8))


if __name__ == '__main__':
    unittest.main()
