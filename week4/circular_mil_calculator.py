import math

def main():
    r = int(input("반지름을 입력하세요: "))
    x = r * 2 * math.pi
    s = math.pi * r**2
    print("원의 둘레:", round(x,1))
    print("원의 면적:", round(s, 2))

if __name__ == '__main__':
    main()
