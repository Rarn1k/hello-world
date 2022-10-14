from random import *
from turtle import Turtle, done, Screen


def tree(i: int, dist, tur: Turtle):
    angle = randint(20, 35)
    multi = 0.75
    size = int(dist / 15 + 2)
    if i <= 0:
        return 1
    tur.pensize(size)
    tur.forward(dist)
    tur.right(angle)
    i -= 1
    if i == 1:
        tur.pencolor("green")
    tree(i, dist * multi + 3, tur)
    tur.left(angle * 2)
    if i == 1:
        tur.pencolor("green")
    tree(i, dist * multi + 3, tur)
    # if i <= 2:
    #     tur.color("green")
    #     tur.stamp()
    #     tur.color("#51361a")

    tur.right(angle)
    tur.backward(dist)
    tur.pencolor("#51361a")


def main() -> None:
    t = Turtle()
    s = Screen()

    t.hideturtle()
    t.penup()
    t.sety(-300)
    t.pendown()
    t.pencolor("#51361a")
    t.shape("arrow")
    t.pensize(18)
    t.speed(10)
    t.left(90)

    s.tracer(20, 100)
    tree(12, 150, t)
    done()


if __name__ == "__main__":
    main()
