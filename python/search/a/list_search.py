"""
列表元素搜索
"""


class ListSearch:

    @staticmethod
    def disorderSearch(items: list, value) -> bool:
        pos, found = 0, False
        while pos < len(items) and not found:
            if items[pos] == value:
                found = True
            else:
                pos += 1
        return found

    @staticmethod
    def orderSearch(items: list, value: int) -> bool:
        pos, found, stop = 0, False, False
        while pos < len(items) and not found and not stop:
            if items[pos] == value:
                found = True
            else:
                if items[pos] > value:
                    stop = True
                else:
                    pos += 1
        return found
