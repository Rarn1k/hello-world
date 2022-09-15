from turtle import Screen


def main() -> None:
    screen = Screen()
    text = screen.textinput(title="Title", prompt="Prompt")
    print(f"Your input: {text}")

    num = screen.numinput(title="Title", prompt="Prompt", default=5, minval=0, maxval=9)
    print(type(num))
    print(f"Your number: {num}")

    screen.mainloop()


if __name__ == "__main__":
    main()
