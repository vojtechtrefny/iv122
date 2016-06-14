import math

from lib import vector
from cv3.turtle import Turtle


def rotate(sides=3, repeat=200):
    t = Turtle(name="rotate_" + str(sides))

    lenght = 50
    for i in range(repeat):
        for j in range(sides):
            t.forward(lenght)
            t.right(360 / sides)
            t.forward(lenght)
        t.right(90)
        t.penup()
        t.forward(10)
        t.left(85)
        t.pendown()

        lenght += 2

    t.write_svg()


rotate(sides=3)
rotate(sides=4)
rotate(sides=8)
