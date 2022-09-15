from turtle import Turtle, done


def main() -> None:
    tur = Turtle()
    tur.speed(speed=1)
    tur.hideturtle()  # ht
    print(f"Видимость: {tur.isvisible()}")
    tur.forward(distance=100)

    tur.showturtle()
    print(f"Видимость: {tur.isvisible()}\n")

    tur.shape(
        name="turtle"
    )  # arrow, turtle, circle, square, triangle, classic; ref: register_shape
    print(f"Форма: {tur.shape()}\n")

    tur.resizemode(rmode="auto")  # auto, user, noresize
    print(f"Resize mode: {tur.resizemode()}\n")

    tur.pencolor("blue")
    tur.shapesize(
        stretch_wid=1.0, stretch_len=1.0, outline=1.0
    )  # turtlesize; resizemode("user") is called
    print(f"Shape size: {tur.shapesize()}\n")

    tur.shearfactor(shear=-1.0)  # Сдвиг
    print(f"Shear factor: {tur.shearfactor()}")
    tur.stamp()
    tur.forward(distance=50)
    tur.shearfactor(shear=1.0)
    print(f"Shear factor: {tur.shearfactor()}")
    tur.stamp()
    tur.forward(distance=50)
    tur.shearfactor(shear=0.0)
    print(f"Shear factor: {tur.shearfactor()}")
    tur.stamp()

    done()


if __name__ == "__main__":
    main()
