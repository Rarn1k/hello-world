from math import pi
from turtle import Turtle, done


def print_turtle_data(tur: Turtle) -> None:
    print(f"Координаты: {tur.pos()}\nУгол направления: {tur.heading()}\n")


def main() -> None:
    tur = Turtle()
    tur.radians()
    tur.right(angle=pi)
    print_turtle_data(tur)

    tur.degrees()
    print_turtle_data(tur)

    done()


if __name__ == "__main__":
    main()
