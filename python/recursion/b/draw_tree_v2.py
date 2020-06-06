from turtle import Turtle

"""
绘制树
"""


def draw_tree_v2(height: int, turtle: Turtle):
    if height > 0:
        turtle.fd(height)
        turtle.rt(20)
        draw_tree_v2(height - 5, turtle)

        turtle.lt(40)
        draw_tree_v2(height - 5, turtle)

        if height < 25:
            turtle.pencolor('green')
        turtle.rt(20)
        turtle.bk(height)
        turtle.pencolor('black')


def main():
    height = 90
    turtle = Turtle()
    screen = turtle.getscreen()
    turtle.penup()
    turtle.goto(-50, -100)
    turtle.pendown()
    turtle.seth(90)
    draw_tree_v2(height, turtle)
    turtle.color('black')
    turtle.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    main()
