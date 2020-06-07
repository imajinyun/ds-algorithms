"""
汉诺塔

递归将目标分解成三个子目标：
- 子目标 1：将前 n-1 个盘子从 a 移动到 b 上；
- 子目标 2：将最底下的最后一个盘子从 a 移动到 c 上；
- 子目标 3：将 b 上的 n-1 个盘子移动到 c 上；
- 然后将每个子目标可以继续分解直到 N 为 1；
"""


def move_tower(n: int, a: str, b: str, c: str):
    if n == 1:
        print(a + '->' + c)
    else:
        move_tower(n - 1, a, c, b)
        move_tower(1, a, b, c)
        move_tower(n - 1, b, a, c)


if __name__ == '__main__':
    move_tower(1, 'A', 'B', 'C')
    print()

    move_tower(2, 'A', 'B', 'C')
    print()

    move_tower(3, 'A', 'B', 'C')
    print()

    move_tower(4, 'A', 'B', 'C')
    print()

    move_tower(5, 'A', 'B', 'C')
