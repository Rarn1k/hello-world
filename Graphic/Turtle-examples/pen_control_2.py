from turtle import Turtle, done


def main() -> None:
    tur = Turtle()
    print(f"Перо: {tur.pen()}\n")

    pen = {
        "shown": True,
        "pendown": True,
        "pencolor": "red",
        "fillcolor": (0.0, 1.0, 0.0),  # green
        "pensize": 5,
        "speed": 3,
        "resizemode": "user",  # auto, user, noresize
        "stretchfactor": (1.0, 2.0),  # user
        "outline": 1.0,  # user
        "tilt": 1,  # user
    }
    tur.pen(pen=pen)
    print(f"Перо: {tur.pen()}\n")
    tur.goto(x=100, y=100)

    tur.pen(pencolor="blue")
    print(f"Перо: {tur.pen()}\n")

    done()


if __name__ == "__main__":
    main()
