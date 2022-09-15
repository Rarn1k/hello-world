from turtle import Screen, Turtle


def handle_on_space_release() -> None:
    tur.circle(radius=50)


def handle_on_up_press() -> None:
    tur.setheading(to_angle=90)
    tur.forward(distance=100)


def handle_on_down_press() -> None:
    tur.setheading(to_angle=270)
    tur.forward(distance=100)


def handle_on_left_press() -> None:
    tur.setheading(to_angle=180)
    tur.forward(distance=100)


def handle_on_right_press() -> None:
    tur.setheading(to_angle=0)
    tur.forward(distance=100)


def handle_on_left_click(x: float, y: float) -> None:
    print(f"Координаты: ({x}, {y})")
    screen.bgcolor("red")


def handle_on_left_click_2(x: float, y: float) -> None:
    print(f"Координаты: ({x}, {y})")
    screen.bgpic("turtle.gif")
    print(screen.bgpic())


def handle_on_wheel_click(x: float, y: float) -> None:
    print(f"Координатыs: ({x}, {y})")
    screen.bgcolor("green")
    screen.bgpic("nopic")


def handle_on_right_click(x: float, y: float) -> None:
    print(f"Координаты: ({x}, {y})")
    screen.bgcolor("blue")
    screen.bgpic("nopic")


def change_background_color() -> None:
    screen.bgcolor("violet")


screen = Screen()
tur = Turtle()


def main() -> None:
    screen.onkey(fun=handle_on_space_release, key="space")  # onkeyrelease

    screen.onkeypress(fun=handle_on_up_press, key="Up")
    screen.onkeypress(fun=handle_on_down_press, key="Down")
    screen.onkeypress(fun=handle_on_left_press, key="Left")
    screen.onkeypress(fun=handle_on_right_press, key="Right")

    screen.onclick(fun=handle_on_left_click, btn=1)  # onscreenclick
    screen.onclick(handle_on_left_click_2, btn=1, add=True)
    # screen.onclick(fun=handle_on_left_click_2, btn=1)
    screen.onclick(fun=handle_on_wheel_click, btn=2)
    screen.onclick(fun=handle_on_right_click, btn=3)

    screen.ontimer(fun=change_background_color, t=1000)

    screen.listen()
    screen.mainloop()  # done


if __name__ == "__main__":
    main()
