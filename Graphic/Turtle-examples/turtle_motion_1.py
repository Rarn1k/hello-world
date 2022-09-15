from turtle import Turtle, done


def print_turtle_data(tur: Turtle) -> None:
    print(f"Координаты: {tur.pos()}\nУгол направления: {tur.heading()}\n")


def main() -> None:
    tur = Turtle()
    tur.forward(distance=100)  # fd
    print_turtle_data(tur)

    tur.backward(distance=200)  # bk, back
    print_turtle_data(tur)

    tur.right(angle=90)  # rt
    print_turtle_data(tur)
    tur.forward(distance=100)
    print_turtle_data(tur)

    tur.left(angle=45)  # lt
    print_turtle_data(tur)
    tur.forward(distance=200)
    print_turtle_data(tur)

    done()


if __name__ == "__main__":
    main()
