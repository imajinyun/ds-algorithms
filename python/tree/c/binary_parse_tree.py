"""
解析树思路：
1. 如果当前标记是(，就为当前节点添加一个左子节点，并下沉至该子节点；
2. 如果当前标记在列表['+', '-', '/', '＊']中，就将当前节点的值设为当前标记对应的运算符；为当前节点添加一个右子节点，并下沉至该子节点；
3. 如果当前标记是数字，就将当前节点的值设为这个数并返回至父节点；
4. 如果当前标记是)，就跳到当前节点的父节点；
"""
import sys, operator

from b.binary_tree import BinaryTree

sys.path.append('../../stack')

from a.stack import Stack


def build_parse_tree(expr: str) -> BinaryTree:
    expr, stack, bt = list(expr.replace(' ', '')), Stack(), BinaryTree('')
    stack.push(bt)
    tree = bt

    for i in expr:
        if i == '(':
            tree.insertLeft('')
            stack.push(tree)
            tree = tree.getLeftChild()
        elif i not in '+-*/)':
            tree.setRootValue(eval(i))
            tree = stack.pop()
        elif i in '+-*/':
            tree.setRootValue(i)
            tree.insertRight('')
            stack.push(tree)
            tree = tree.getRightChild()
        elif i == ')':
            tree = stack.pop()
        else:
            raise ValueError('Unknown operator: ' + i)
    return bt


def evaluate(tree: BinaryTree):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    left, right = tree.getLeftChild(), tree.getRightChild()

    if left and right:
        fn = operators[tree.getRootValue()]
        return fn(evaluate(left), evaluate(right))
    else:
        return tree.getRootValue()
