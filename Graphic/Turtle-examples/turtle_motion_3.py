from turtle import Turtle, done


def print_turtle_data(tur: Turtle) -> None:
    print(f"Координаты: {tur.pos()}\nУгол направления: {tur.heading()}\n")


def main() -> None:
    tur = Turtle()
    tur.circle(radius=100)  # counterclockwise
    print_turtle_data(tur)
    tur.circle(radius=-50)  # clockwise
    print_turtle_data(tur)

    tur.circle(
        radius=90, extent=270
    )  # extent – an angle – determines which part of the circle is drawn
    print_turtle_data(tur)
    tur.circle(
        radius=50, steps=6
    )  # inscribed regular polygon, steps determines the number of steps to use
    print_turtle_data(tur)

    tur.home()
    print_turtle_data(tur)

    tur.forward(distance=100)
    tur.dot(10, "blue")  # size is not given => size = max(pensize+4, 2*pensize)
    tur.backward(distance=200)
    stamp_id = tur.stamp()

    tur.left(angle=60)
    tur.forward(distance=200)
    tur.clearstamp(stampid=stamp_id)
    tur.clearstamps(
        n=None
    )  # if n is None, delete all stamps, if n > 0 delete first n stamps, else if n < 0 delete last n stamps

    done()


if __name__ == "__main__":
    main()
