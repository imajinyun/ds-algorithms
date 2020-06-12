"""
插入排序
"""


def insertion_sort(items: list) -> list:
    for i in range(1, len(items)):
        j, value = i, items[i]
        while j > 0 and items[j - 1] > value:
            items[j], j = items[j - 1], j - 1
        items[j] = value
    return items
