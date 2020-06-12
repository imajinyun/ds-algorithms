"""
有序列表二分搜索
"""


def binary_search(items: list, value: int) -> bool:
    if len(items) == 0:
        return False
    else:
        middle = len(items) // 2
        if items[middle] == value:
            return True
        else:
            if value > items[middle]:
                return binary_search(items[middle + 1:], value)
            else:
                return binary_search(items[:middle], value)
