from turtle import Turtle, done


def print_turtle_data(tur: Turtle) -> None:
    print(f"Координаты: {tur.pos()}\nУгол направления: {tur.heading()}\n")


def main() -> None:
    tur = Turtle()
    tur.speed(speed=1)
    print(f"Текущая скорость: {tur.speed()}")
    tur.speed(speed="slow")  # speed=3
    print(f"Текущая скорость: {tur.speed()}")

    for _ in range(4):
        tur.forward(distance=100)
        tur.left(angle=90)

    for _ in range(8):
        tur.undo()

    done()


if __name__ == "__main__":
    main()
