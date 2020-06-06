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


def decimal_to_str(num: int, base: int) -> str:
    """ 将整数转换成以 2～16 为进制基数的字符串 """
    stack, result = Stack(), ''
    recursive_stack(num, base, stack)
    while not stack.isEmpty():
        result += stack.pop()
    return result


def recursive_stack(num: int, base: int, stack: Stack) -> None:
    s = '0123456789ABCDEF'
    if num < base:
        stack.push(s[num])
    else:
        stack.push(s[num % base])
        recursive_stack(num // base, base, stack)
