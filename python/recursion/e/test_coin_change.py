import unittest

from e.coin_change import coin_change


class TestCoinChange(unittest.TestCase):
    """ 测试 coin_change.py """

    def testCoinChange(self):
        self.assertEqual(1, coin_change([1, 5, 10, 25], 1, [0] * 1))
        self.assertEqual(1, coin_change([1, 5, 10, 25], 5, [0] * 5))
        self.assertEqual(1, coin_change([1, 5, 10, 25], 10, [0] * 10))
        self.assertEqual(1, coin_change([1, 5, 10, 25], 25, [0] * 25))

        self.assertEqual(3, coin_change([1, 5, 10, 25], 3, [0] * 3))
        self.assertEqual(4, coin_change([1, 5, 10, 25], 8, [0] * 8))
        self.assertEqual(4, coin_change([1, 5, 10, 25], 13, [0] * 13))
        self.assertEqual(5, coin_change([1, 5, 10, 25], 18, [0] * 18))
        self.assertEqual(6, coin_change([1, 5, 10, 25], 63, [0] * 63))

        self.assertEqual(3, coin_change([1, 5, 10, 21, 25], 63, [0] * 63))


if __name__ == '__main__':
    unittest.main()
