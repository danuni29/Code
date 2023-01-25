import turtle


def main():
    t = turtle.Turtle()
    t.shape("turtle")

    i = 0
    while i < 4:
        t.forward(100)
        t.left(90)
        i = i + 1


if __name__ == '__main__':
    main()
