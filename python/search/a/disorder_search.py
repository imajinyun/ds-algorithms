"""
无序列表搜索
"""


def search(items, value):
    pos, found = 0, False
    while pos < len(items) and not found:
        if items[pos] == value:
            found = True
        else:
            pos += 1

    return found
