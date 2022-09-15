from turtle import Screen


def main() -> None:
    screen = Screen()
    screen.setup()  # turtle.cfg
    screen.title("My title")
    screen.exitonclick()


if __name__ == "__main__":
    main()
