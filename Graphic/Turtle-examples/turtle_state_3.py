from turtle import Turtle, done


def main() -> None:
    tur = Turtle()
    tur.speed(speed=1)

    tur.stamp()
    tur.forward(distance=50)

    print(f"tilt angle: {tur.tiltangle()}")  # Наклон
    tur.tilt(angle=90)
    print(f"tilt angle: {tur.tiltangle()}")
    tur.stamp()

    tur.forward(distance=50)
    tur.tiltangle(angle=45)
    print(f"tilt angle: {tur.tiltangle()}\n")
    tur.stamp()

    print(f"shape transform: {tur.shapetransform()}\n")
    print(f"shape poly: {tur.get_shapepoly()}")

    done()


if __name__ == "__main__":
    main()
