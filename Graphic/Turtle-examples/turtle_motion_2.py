from turtle import Turtle, Vec2D, done


def print_turtle_data(tur: Turtle) -> None:
    print(f"Координаты: {tur.pos()}\nУгол направления: {tur.heading()}\n")


def main() -> None:
    tur = Turtle()
    tur.setx(x=100)
    print_turtle_data(tur)

    tur.sety(y=200)
    print_turtle_data(tur)

    tur.goto(x=200, y=200)  # setpos, setposition
    print_turtle_data(tur)
    tur.goto(x=(210, 220))
    print_turtle_data(tur)
    vector = Vec2D(x=100, y=150)
    tur.goto(x=vector)
    print_turtle_data(tur)

    tur.setheading(to_angle=135)  # seth
    print_turtle_data(tur)
    tur.forward(distance=50)
    print_turtle_data(tur)

    done()


if __name__ == "__main__":
    main()
