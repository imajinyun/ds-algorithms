from a.stack import Stack


def decimal_to_any(num: int, base: int):
    """ 将十进制数转换成任意进制数 """
    stack, digits = Stack(), '0123456789ABCDEF'

    while num > 0:
        rem = num % base
        stack.push(rem)
        num //= base

    result = ''
    while not stack.isEmpty():
        result += str(digits[stack.pop()])

    if base == 16:
        flag = False
        for i in result:
            if i not in 'ABCDEF':
                flag = True
                break

        return int(result) if flag else (result if result else 0)
    return int(result) if result else 0
