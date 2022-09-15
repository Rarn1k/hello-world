from turtle import Screen, Turtle


def print_data(screen: Screen, tur: Turtle) -> None:
    text = (
        f"Mode: {screen.mode()}\n"
        f"Position: {tur.pos()}\n"
        f"Heading: {tur.heading()}\n"
    )
    print(text)


def main() -> None:
    screen = Screen()
    tur = Turtle()

    screen.mode(mode="standard")
    print_data(screen, tur)
    tur.forward(distance=100)
    print_data(screen, tur)

    screen.mode(mode="logo")
    print_data(screen, tur)
    tur.forward(distance=100)
    print_data(screen, tur)

    screen.mode(mode="world")
    print_data(screen, tur)
    tur.forward(distance=100)
    print_data(screen, tur)

    screen.colormode(cmode=1.0)
    screen.bgcolor(1.0, 0, 0)

    screen.colormode(cmode=255)
    screen.bgcolor(0, 255, 0)

    print(f"canvas: {screen.getcanvas()}\n")
    print(f"shapes: {screen.getshapes()}\n")

    screen.register_shape("cursor.gif")  # addshape
    tur.shape("cursor.gif")

    print()
    print(f"turtles: {screen.turtles()}\n")
    print(f"height: {screen.window_height()}\n")
    print(f"width: {screen.window_width()}\n")

    screen.mainloop()


if __name__ == "__main__":
    main()
