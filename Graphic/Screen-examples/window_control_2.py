from turtle import Screen, Turtle


def print_screen_data(screen: Screen) -> None:
    text = (
        f"Размеры: {screen.screensize()}\n"
        f"Цвет фона: {screen.bgcolor()}\n"
        f"Фоновый рисунок: {screen.bgpic()}\n"
    )
    print(text)


def print_turtle_data(tur: Turtle) -> None:
    text = f"Координаты: {tur.pos()}\nУгол направления: {tur.heading()}\n"
    print(text)


def main() -> None:
    screen = Screen()
    screen.setworldcoordinates(llx=100, lly=100, urx=200, ury=200)  # mode=world
    print_screen_data(screen)

    tur = Turtle()
    print_turtle_data(tur)

    tur.goto(x=110, y=110)
    tur.stamp()
    tur.goto(x=190, y=190)
    print_turtle_data(tur)

    screen.mainloop()


if __name__ == "__main__":
    main()
