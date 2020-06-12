"""
冒泡排序
"""


def bubble_sort(items: list) -> list:
    for i in range(len(items) - 1, 0, -1):
        for j in range(i):
            if items[j] > items[j + 1]:
                tmp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = tmp
    return items


def bubble_sort2(items: list) -> list:
    for i in range(0, len(items) - 1):
        for j in range(i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


def bubble_sort3(items: list) -> list:
    flag = True
    i = len(items) - 1
    while i > 0 and flag:
        flag = False
        for j in range(i):
            if items[j] > items[j + 1]:
                flag = True
                items[j], items[j + 1] = items[j + 1], items[j]
        i -= 1
    return items
