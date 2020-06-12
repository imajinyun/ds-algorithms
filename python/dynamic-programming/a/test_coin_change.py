import unittest

from a.coin_change import CoinChange


class TestCoinChange(unittest.TestCase):

    def testCoinChange1(self):
        self.assertEqual(1, CoinChange.coinChange1([1, 5, 10, 25], 1, [0] * 2))
        self.assertEqual(1, CoinChange.coinChange1([1, 5, 10, 25], 5, [0] * 6))
        self.assertEqual(1, CoinChange.coinChange1([1, 5, 10, 25], 10, [0] * 11))
        self.assertEqual(1, CoinChange.coinChange1([1, 5, 10, 25], 25, [0] * 26))

        self.assertEqual(3, CoinChange.coinChange1([1, 5, 10, 25], 3, [0] * 4))
        self.assertEqual(4, CoinChange.coinChange1([1, 5, 10, 25], 8, [0] * 9))
        self.assertEqual(4, CoinChange.coinChange1([1, 5, 10, 25], 13, [0] * 14))
        self.assertEqual(5, CoinChange.coinChange1([1, 5, 10, 25], 18, [0] * 19))
        self.assertEqual(6, CoinChange.coinChange1([1, 5, 10, 25], 63, [0] * 64))

        self.assertEqual(3, CoinChange.coinChange1([1, 5, 10, 21, 25], 63, [0] * 64))

    def testCoinChange2(self):
        self.assertEqual(1, CoinChange.coinChange2([1, 5, 10, 25], 1, [0] * 2, [0] * 2))
        self.assertEqual(1, CoinChange.coinChange2([1, 5, 10, 25], 5, [0] * 6, [0] * 6))
        self.assertEqual(1, CoinChange.coinChange2([1, 5, 10, 25], 10, [0] * 11, [0] * 11))
        self.assertEqual(1, CoinChange.coinChange2([1, 5, 10, 25], 25, [0] * 26, [0] * 26))

        self.assertEqual(3, CoinChange.coinChange2([1, 5, 10, 25], 3, [0] * 4, [0] * 4))
        self.assertEqual(4, CoinChange.coinChange2([1, 5, 10, 25], 8, [0] * 9, [0] * 9))
        self.assertEqual(4, CoinChange.coinChange2([1, 5, 10, 25], 13, [0] * 14, [0] * 14))
        self.assertEqual(5, CoinChange.coinChange2([1, 5, 10, 25], 18, [0] * 19, [0] * 19))
        self.assertEqual(6, CoinChange.coinChange2([1, 5, 10, 25], 63, [0] * 64, [0] * 64))

        self.assertEqual(3, CoinChange.coinChange2([1, 5, 10, 21, 25], 63, [0] * 64, [0] * 64))

    def testGetCoins(self):
        money, coins, used = 18, [0] * 19, [0] * 19
        self.assertEqual(5, CoinChange.coinChange2([1, 5, 10, 25], money, coins, used))
        self.assertEqual([1, 1, 1, 5, 10], CoinChange.getCoins(used, money))

        money, coins, used = 63, [0] * 64, [0] * 64
        self.assertEqual(3, CoinChange.coinChange2([1, 5, 10, 21, 25], money, coins, used))
        self.assertEqual([21, 21, 21], CoinChange.getCoins(used, money))
        self.assertEqual([10, 21, 21], CoinChange.getCoins(used, 52))


if __name__ == '__main__':
    unittest.main()
