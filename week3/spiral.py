import turtle

def main():
    colors = ["red", "purple", "blue", "green", "yellow", "orange"]
    t = turtle.Turtle()

    turtle.bgcolor("black")

    t.speed(0)  # 거북이의 속도를 0으로 설정
    t.width(3)  # 거북이가 그리는 선의 두께를 3으로 설정
    length = 10  # 초기 선의 길이를 10으로 설정

    #선의 길이가 500보다 작으면 반복
    while length < 500:
        t.forward(length)
        t.pencolor(colors[length%6])
        t.right(89)
        length += 5


if __name__ == '__main__':
    main()

