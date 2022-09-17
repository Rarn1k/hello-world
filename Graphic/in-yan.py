from turtle import Turtle, Screen, done


def main() -> None:
    t = Turtle()
    s = Screen()
    s.bgcolor("light blue")
    t.penup()
    t.sety(100)
    t.pendown()

    t.begin_fill()
    t.left(180)
    t.color("white")
    t.circle(100, 180)
    t.left(180)
    t.circle(-50, 180)
    t.circle(50, 180)
    t.end_fill()

    t.begin_fill()
    t.left(180)
    t.color("black")
    t.circle(-100, 180)
    t.circle(-50, 180)
    t.circle(50, 180)
    t.end_fill()

    t.penup()
    t.sety(-50)
    t.pendown()
    t.dot(50, "white")

    t.penup()
    t.sety(50)
    t.pendown()
    t.dot(50, "black")

    done()


if __name__ == "__main__":
    main()
