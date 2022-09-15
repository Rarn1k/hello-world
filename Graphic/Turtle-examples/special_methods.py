from turtle import Turtle, done, register_shape


def main() -> None:
    tur = Turtle()
    tur.begin_poly()
    tur.forward(distance=100)
    tur.left(angle=90)
    tur.forward(distance=50)
    tur.left(angle=90)
    tur.forward(distance=100)
    tur.end_poly()

    poly = tur.get_poly()
    print(f"Многоугольник: {poly}")
    register_shape("rectangle", poly)
    tur.shape(name="rectangle")
    tur.stamp()

    tur.shape(name="turtle")
    tur.setheading(to_angle=0)
    tur.forward(distance=200)

    tur2 = tur.clone()
    tur2.right(angle=90)
    tur2.pencolor("red")
    tur2.forward(distance=100)

    screen = tur.getscreen()
    print(f"Screen: {screen}\n")

    tur.setundobuffer(size=6)
    tur.home()
    for _ in range(4):
        tur.forward(distance=150)
        tur.right(90)

    while tur.undobufferentries() > 0:
        tur.undo()
    tur.undo()  # no effect

    done()


if __name__ == "__main__":
    main()
