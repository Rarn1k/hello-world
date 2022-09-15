from turtle import *


def main() -> None:
    speed(speed=5)
    color("red", "yellow")
    begin_fill()
    while True:
        forward(distance=200)
        left(angle=170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()


if __name__ == "__main__":
    main()
