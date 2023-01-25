def main():
    x = int(input("x: "))
    y = int(input("y: "))

    if x > 0 and y > 0:
        print("x=", x, "y=", y, "입력한 좌표는 1사분면 입니다.")
    elif x < 0 and y > 0:
        print("x=", x, "y=", y, "입력한 좌표는 2사분면 입니다.")
    elif x < 0 and y > 0:
        print("x=", x, "y=", y, "입력한 좌표는 3사분면 입니다.")
    else:
        print("x=", x, "y=", y, "입력한 좌표는 4사분면 입니다.")
if __name__ == '__main__':
    main()

