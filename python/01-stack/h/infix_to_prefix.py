import string

from a.stack import Stack


def infix_to_prefix(expr):
    """ 从中序表达式到前序表达式的转换 """
    stack, prefixes, operators = Stack(), [], {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
        ')': 1,
    }
    expr = expr.replace(' ', '')[::-1]

    for i in list(expr):
        if i.upper() in string.ascii_uppercase:
            prefixes.append(i)
        elif i == ')':
            stack.push(i)
        elif i == '(':
            top = stack.pop()
            while top != ')':
                prefixes.append(top)
                top = stack.pop()
        else:
            while not stack.isEmpty() and operators[stack.peek()] > operators[i]:
                prefixes.append(stack.pop())
            stack.push(i)

    while not stack.isEmpty():
        prefixes.append(stack.pop())
    return ''.join(prefixes)[::-1]


def prefix_expr_value(expr):
    """ 计算前序表达式的值  """
    stack = Stack()

    for i in list(expr.replace(' ', ''))[::-1]:
        if i in '0123456789':
            stack.push(int(i))
        else:
            a, b = stack.pop(), stack.pop()
            stack.push(calculation(i, a, b))
    return stack.pop()


def calculation(op, a, b):
    """ 根据操作符计算给定操作数 """
    if op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        raise ValueError('Operator parameter error')
