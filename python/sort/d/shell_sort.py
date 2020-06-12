"""
希尔排序
"""


def shell_sort(items: list) -> list:
    n = len(items)
    k = n // 2
    while k > 0:
        for i in range(k, n):
            while i >= k and items[i] < items[i - k]:
                items[i], items[i - k] = items[i - k], items[i]
                i -= k
        k //= 2
    return items
