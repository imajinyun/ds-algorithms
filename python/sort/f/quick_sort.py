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


def quick_sort2(items: list) -> list:
    if len(items) < 2:
        return items
    else:
        pivot = items[0]
        left = [i for i in items[1:] if i <= pivot]
        right = [i for i in items[1:] if i > pivot]
        return quick_sort2(left) + [pivot] + quick_sort2(right)
