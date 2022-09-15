from turtle import Turtle, colormode, done


def print_turtle_data(tur: Turtle) -> None:
    print(f"Координаты: {tur.pos()}\nУгол направления: {tur.heading()}\n")


def main() -> None:
    tur = Turtle()

    tur.pensize(width=10)  # width
    print(f"Толщина пера: {tur.pensize()}")
    tur.forward(distance=50)
    tur.penup()  # pu, up
    print(f"Перо опущено?: {tur.isdown()}")

    tur.left(angle=90)
    tur.forward(distance=50)
    tur.pendown()  # pd, down
    print(f"Перо опущено?: {tur.isdown()}\n")

    tur.left(angle=90)
    tur.backward(distance=100)
    print_turtle_data(tur)

    tur.pensize(width=1)
    tur.left(angle=90)
    tur.pencolor("red")
    print(f"Цвет пера: {tur.pencolor()}")
    tur.forward(distance=50)

    tur.pencolor("#ff00ff")
    print(f"Цвет пера: {tur.pencolor()}\n")
    tur.forward(distance=50)

    print(f"Цветовой режим (color mode): {colormode()}")
    tur.pencolor(0.0, 1.0, 0.0)  # rgb
    print(f"Цвет пера: {tur.pencolor()}")
    tur.forward(distance=50)
    tur.pencolor((0.0, 0.0, 1.0))  # rgb
    print(f"Цвет пера: {tur.pencolor()}\n")
    tur.forward(distance=50)

    colormode(cmode=255)
    print(f"Цветовой режим (color mode): {colormode()}")
    tur.pencolor(0, 255, 0)  # rgb
    print(f"Цвет пера: {tur.pencolor()}")
    tur.forward(distance=50)
    tur.pencolor((0, 0, 255))  # rgb
    print(f"Цвет пера: {tur.pencolor()}\n")
    tur.forward(distance=50)

    tur.goto(x=200, y=200)
    tur.fillcolor("pink")
    print(f"Цвет заливки: {tur.fillcolor()}")
    print(f"Заливка: {tur.filling()}")
    tur.begin_fill()
    print(f"Заливка: {tur.filling()}")
    for _ in range(4):
        tur.forward(100)
        tur.right(90)
    tur.end_fill()
    print(f"Заливка: {tur.filling()}\n")

    tur.color("red", "green")  # ~ pencolor("red") and fillcolor("green")
    print(f"Цвет: {tur.color()}\n")

    tur.write(arg="Hello world")
    tur.forward(distance=50)
    tur.write(
        arg="Hello world", move=True, align="center"
    )  # move=True => the pen is moved to the bottom-right corner of the text

    tur.pencolor("green")
    tur.goto(x=100, y=-100)
    tur.write(arg="hello", align="right", font=("Arial", 15, "normal"))

    # tur.reset()
    # tur.clear()

    done()


if __name__ == "__main__":
    main()
