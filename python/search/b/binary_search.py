"""
有序列表二分搜索
"""


def binary_search(items: list, value: int) -> bool:
    first, last, found = 0, len(items) - 1, False
    while first <= last and not found:
        middle = (last + first) // 2
        if items[middle] == value:
            found = True
        else:
            if value > items[middle]:
                first = middle + 1
            else:
                last = middle - 1
    return found
