from turtle import *

"""
用 turtle 模块递归地绘制螺旋线
"""


def draw_spiral(length: int, turtle: Turtle):
    if length > 0:
        turtle.forward(length)
        turtle.right(90)
        draw_spiral(length - 5, turtle)


def main():
    turtle = Turtle()
    turtle.pencolor('#44AE7E')
    turtle.pensize(5)
    screen = turtle.getscreen()
    draw_spiral(100, turtle)
    screen.exitonclick()


if __name__ == '__main__':
    main()
