from turtle import Turtle, done


def handle_on_left_click(x: float, y: float) -> None:
    print(f"Координаты: ({x}, {y})")
    tur.setheading(to_angle=180)


def handle_on_left_click_2(x: float, y: float) -> None:
    print(f"Координаты: ({x}, {y}), {type(x)}")
    tur.pencolor("red")


def handle_on_right_click(x: float, y: float) -> None:
    print(f"Координаты: ({x}, {y})")
    tur.setheading(to_angle=0)


def handle_on_release(x: float, y: float) -> None:
    print(f"Координаты: ({x}, {y})")
    tur.forward(distance=50)


def handle_on_drag(x: float, y: float) -> None:
    print(f"Координаты: ({x}, {y})")
    tur.goto(x=x, y=y)


tur = Turtle()


def main() -> None:
    tur.onclick(fun=handle_on_left_click, btn=1)
    tur.onclick(fun=handle_on_left_click_2, btn=1, add=True)
    # tur.onclick(fun=handle_on_left_click_2, btn=1)
    tur.onclick(fun=handle_on_right_click, btn=3)
    tur.onrelease(fun=handle_on_release, btn=1)
    tur.onrelease(fun=handle_on_release, btn=3)
    tur.ondrag(fun=handle_on_drag)

    done()


if __name__ == "__main__":
    main()
