"""
硬币找零
"""


def coin_change(coins: list, money: int, used) -> int:
    """
    给定要找回的硬币种类和总钱数，求出找零所需最少的硬币数目

    Args:
        - coins: 给定的硬币种类
        - money: 要找的零钱
        - used: 要找的零钱标记
    """
    min_coin = money
    if money in coins:
        used[money - 1] = 1
        return 1
    elif used[money - 1] > 0:
        return used[money - 1]
    else:
        for i in [j for j in coins if j <= money]:
            num_coin = 1 + coin_change(coins, money - i, used)
            if min_coin > num_coin:
                min_coin = num_coin
                used[money - 1] = min_coin
    return min_coin
