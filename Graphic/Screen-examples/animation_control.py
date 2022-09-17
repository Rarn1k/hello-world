from turtle import Screen, Turtle


def main() -> None:
    screen = Screen()
    screen.delay(delay=100)

    tur = Turtle()
    tur.forward(distance=100)
    tur.right(angle=90)
    tur.forward(distance=100)

    screen.tracer(n=5, delay=100)

    screen.update()

    screen.mainloop()


if __name__ == "__main__":
    main()
