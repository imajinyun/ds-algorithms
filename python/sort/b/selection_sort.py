"""
选择排序
"""


def selection_sort(items: list) -> list:
    for i in range(len(items) - 1, 0, -1):
        k = 0
        for j in range(1, i + 1):
            if items[j] > items[k]:
                k = j
        items[i], items[k] = items[k], items[i]

    return items
