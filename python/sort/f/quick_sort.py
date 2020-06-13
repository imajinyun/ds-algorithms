"""
快速排序
"""


def quick_sort(items: list) -> list:
    if len(items) >= 2:
        middle, left, right = items[len(items) // 2], [], []
        items.remove(middle)
        for i in items:
            right.append(i) if i > middle else left.append(i)
        return quick_sort(left) + [middle] + quick_sort(right)
    else:
        return items
