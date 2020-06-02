from a.stack import Stack


def decimal_to_binary(num: int) -> int:
    """将十进制数转换成二进制数"""
    stack = Stack()

    while num > 0:
        rem = num % 2
        stack.push(rem)
        num //= 2

    result = ''
    while not stack.isEmpty():
        result += str(stack.pop())

    return int(result) if result else 0
