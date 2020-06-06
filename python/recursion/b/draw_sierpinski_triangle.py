from turtle import Turtle

"""
绘制谢尔宾斯基三角形
"""


def draw_sierpinski_triangle(points: list, color: str, turtle: Turtle):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[0])
    turtle.end_fill()


def middle(p, q):
    return (p[0] + q[0]) / 2, (p[1] + q[1]) / 2


def sierpinski(points: list, degree: int, turtle: Turtle):
    colors = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_sierpinski_triangle(points, colors[degree], turtle)
    if degree > 0:
        sierpinski([points[0], middle(points[0], points[1]), middle(points[0], points[2])], degree - 1, turtle)
        sierpinski([points[1], middle(points[0], points[1]), middle(points[1], points[2])], degree - 1, turtle)
        sierpinski([points[2], middle(points[2], points[1]), middle(points[0], points[2])], degree - 1, turtle)


def main():
    turtle = Turtle()
    screen = turtle.getscreen()
    points = [(-400, -200), (0, 400), (400, -200)]
    sierpinski(points, 5, turtle)
    turtle.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    main()
