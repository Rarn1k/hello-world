from tkinter import PhotoImage
from turtle import Shape, Turtle, done, register_shape


def main() -> None:
    tur = Turtle()

    hex_poly = ((-5, 0), (-2.5, 4.33), (2.5, 4.33), (5, 0), (2.5, -4.33), (-2.5, -4.33))
    s1 = Shape(type_="polygon", data=hex_poly)
    register_shape(name="hex", shape=s1)
    tur.shape("hex")
    tur.stamp()
    tur.forward(distance=100)

    image = PhotoImage(file="cursor.gif")
    s2 = Shape(type_="image", data=image)
    register_shape(name="cursor.gif", shape=s2)
    tur.stamp()
    tur.forward(distance=100)

    s3 = Shape(type_="compound")
    square = ((0, 0), (5, 0), (5, 5), (0, 5))
    s3.addcomponent(poly=square, fill="red")
    triangle = ((5, 0), (10, 0), (7.5, 4.33))
    s3.addcomponent(poly=triangle, fill="blue")
    register_shape(name="square+triangle", shape=s3)
    tur.shape(name="square+triangle")
    tur.tilt(angle=90)
    tur.stamp()

    done()


if __name__ == "__main__":
    main()
