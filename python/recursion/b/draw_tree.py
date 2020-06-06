from turtle import *

"""
绘制树
"""


def draw_tree(size: int, turtle: Turtle):
    if size < 5:
        turtle.pencolor('green')
        turtle.left(30)
        turtle.forward(size)
        turtle.back(size)
        turtle.right(30)
        turtle.pencolor('black')
        return
    turtle.pensize(size // 15)
    turtle.left(30)
    turtle.forward(size)
    draw_tree(size // 2, turtle)

    turtle.right(60)
    draw_tree(size // 2, turtle)
    turtle.left(60)

    turtle.backward(size)
    turtle.right(30)


def main():
    turtle = Turtle()
    screen = turtle.getscreen()
    turtle.getscreen().bgcolor('#4D8CD5')
    turtle.color('black')
    turtle.setheading(60)
    draw_tree(100, turtle)
    turtle.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    main()
