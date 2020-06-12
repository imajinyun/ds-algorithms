"""
硬币找零
"""


class CoinChange:

    @staticmethod
    def coinChange1(types: list, money: int, used: list) -> int:
        """
        给定要找回的硬币种类和总钱数，求出找零所需最少的硬币数目

        Args:
            - types: 给定的硬币种类
            - money: 要找的零钱
            - used: 要找的零钱标记
        """
        for i in range(money + 1):
            num = i
            for j in [k for k in types if k <= i]:
                if num > used[i - j] + 1:
                    num = used[i - j] + 1
            used[i] = num
        return used[money]

    @staticmethod
    def coinChange2(types: list, money: int, coins: list, used: list) -> int:
        for i in range(money + 1):
            num, coin = i, 1
            for j in [k for k in types if k <= i]:
                if num > coins[i - j] + 1:
                    num, coin = coins[i - j] + 1, j
            coins[i], used[i] = num, coin
        return coins[money]

    @staticmethod
    def getCoins(used: list, money: int) -> list:
        coin = money
        items = []
        while coin > 0:
            current = used[coin]
            items.append(current)
            coin -= current
        return items
