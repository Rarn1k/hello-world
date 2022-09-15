from turtle import Screen


def print_screen_data(screen: Screen) -> None:
    text = (
        f"Размеры: {screen.screensize()}\n"
        f"Цвет фона: {screen.bgcolor()}\n"
        f"Фоновый рисунок: {screen.bgpic()}\n"
    )
    print(text)


def main() -> None:
    screen = Screen()
    screen.screensize(canvwidth=200, canvheight=200, bg="blue")
    print_screen_data(screen)

    screen.screensize(canvwidth=300, canvheight=300)
    screen.bgcolor("green")
    screen.bgpic(picname="turtle.gif")
    print_screen_data(screen)

    # screen.clear() # clearscreen
    # screen.reset() # resetscreen

    screen.mainloop()


if __name__ == "__main__":
    main()
