import turtle as t


def print_turtle_data(tur: t.Turtle) -> None:
    print(f"Текущие координаты: {tur.pos()}, угол направления: {tur.heading()}")


def main() -> None:
    s = t.Screen()
    s.bgcolor("violet")

    s.bgpic("turtle.gif")
    s.screensize(canvwidth=500, canvheight=500)

    t.done()


if __name__ == "__main__":
    main()
