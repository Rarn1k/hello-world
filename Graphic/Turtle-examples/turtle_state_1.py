from turtle import Turtle, done


def print_turtle_data(tur: Turtle) -> None:
    print(f"Координаты: {tur.pos()}\nУгол направления: {tur.heading()}\n")


def main() -> None:
    tur = Turtle()
    position = tur.position()  # pos
    x = tur.xcor()
    y = tur.ycor()
    heading = tur.heading()
    text = f"Координаты: {position}\nx: {x}\ny: {y}\nУгол направления: {heading}\n"
    print(text)

    tur.goto(x=100, y=100)
    print_turtle_data(tur)
    angle = tur.towards(x=0, y=0)
    print(f"Угол (towards({x}, {y})): {angle}")
    angle = tur.towards(x=150, y=150)
    print(f"Угол (towards({x}, {y})): {angle}\n")

    print_turtle_data(tur)
    distance = tur.distance(x=0, y=100)
    print(f"Расстояние до ({x}, {y}): {distance}")

    done()


if __name__ == "__main__":
    main()
