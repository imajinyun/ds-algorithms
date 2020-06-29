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


def selection_sort2(items: list) -> list:
    result = []
    for i in range(len(items)):
        smallest = find_smallest(items)
        result.append(items.pop(smallest))
    return result


def find_smallest(items: list) -> int:
    index, smallest = 0, items[0]
    for i in range(1, len(items)):
        if items[i] < smallest:
            index, smallest = i, items[i]
    return index
