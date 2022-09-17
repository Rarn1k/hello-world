import math
from turtle import Turtle, done
from random import *


def main() -> None:
    t = Turtle()
    p = 100
    t.penup()
    t.pensize(3)
    t.setposition(-300, p)
    t.write("P = " + str(p))
    t.pendown()
    t.forward(600)

    t.penup()
    t.pensize(2)
    t.setposition(-300, p)
    t.color("red")
    t.pendown()
    while t.xcor() < 300:
        dist = randrange(60, 100)
        angle = randrange(-70, 70, 20)
        t.left(angle)
        print(angle)
        t.forward(dist)
        if t.color()[1] == "red" and t.ycor() > 100:
            t.color("green")
            gip = (t.ycor() - p) / math.sin(math.radians(angle))
            t.backward(gip)
            t.forward(gip)
        if t.color()[1] == "green" and t.ycor() < 100:
            t.color("red")
            gip = (t.ycor() - p) / math.sin(math.radians(angle))
            t.backward(gip)
            t.forward(gip)
        t.right(angle)

    done()


if __name__ == "__main__":
    main()
