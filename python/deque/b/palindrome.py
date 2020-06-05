from a.deque import Deque


def palindrome(s: str) -> bool:
    """ 实现回文检测 """
    deque = Deque()
    for ch in s:
        deque.addRear(ch)

    equaled = True
    while deque.size() > 1 and equaled:
        front, rear = deque.removeFront(), deque.removeRear()
        if front != rear:
            equaled = False

    return equaled
