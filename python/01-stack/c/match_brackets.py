from a.stack import Stack


def is_match_brackets(str) -> bool:
    """匹配括号（仅匹配 () 出现的情况）"""
    stack = Stack()
    paired = True
    index = 0
    while index < len(str) and paired:
        symbol = str[index]

        if symbol == '(':
            stack.push(symbol)
        else:
            if stack.isEmpty():
                paired = False
            else:
                stack.pop()
        index += 1

    if paired and stack.isEmpty():
        return True
    else:
        return False
