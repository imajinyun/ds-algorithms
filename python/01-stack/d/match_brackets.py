from a.stack import Stack


def is_match_brackets(string) -> bool:
    """ 匹配括号（仅匹配 (){}[] 出现的情况）"""
    stack, paired, index = Stack(), True, 0

    while index < len(string) and paired:
        symbol = string[index]

        if symbol in '([{':
            stack.push(symbol)
        else:
            if stack.isEmpty():
                paired = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    paired = False
        index += 1

    if paired and stack.isEmpty():
        return True
    else:
        return False


def matches(open, close) -> bool:
    return '([{'.index(open) == ')]}'.index(close)
