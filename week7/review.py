# 필요한거 import

import math

#  숫자를 입력받아, 해당하는 구구단을 출력하는 함수 gugudan(dan)를 만드시오.
dan = int(input("원하는 단을 입력하세요: "))
def gugudan(dan):
    for i in range(1, 10):
        gugu = i * dan
        print(gugu)

gugudan(dan)

# 섭씨를 화씨로 바꾸는 함수 c2f(t_c) 함수를 만드시오
t_c = int(input("섭씨온도를 입력하세요: "))
def c2f(t_c):
    temp_c = (t_c - 32) / 1.8
    print("화씨온도는 {}입니다.".format(temp_c))
c2f(t_c)


# 숫자 n이 주어졌을 때, 1부터 n까지의 합을 구하시오. 함수명은 sum_n(n)
n = int(input("n값을 입력하세요: "))
def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total = total + i
    print(total)

sum_n(n)



def main():
    # 원의 면적 구하기
    r = int(input("반지름을 입력하쎄용: "))
    circle = math.pi * r ** 2
    print("반지름은 {}입니당~".format(circle))



    # 칼로리 구하기 (과일마다 섭취 g를 입력 받아서 칼로리 출력하기)
    #한라봉 49 kcal/100g
    #딸기 35 kcal/100g
    #바나나 80 kcal/100g
    hanrabong = int(input("한라봉 몇 gram 드셨어영? "))
    strawberry = int(input("딸기 몇 gram 드셨어영? "))
    banana = int(input("바나나 몇 gram 드셨어영? "))
    total_kcal = (hanrabong/100) * 49 + (strawberry/100) * 35 + (banana/100) * 80
    print("당신은 총 {}kcal 드셨습니다^^.".format(total_kcal))




    # x, y를 입력받아서, 어느 사사분면인지 출력
    x = int(input("x값을 입력하세요: "))
    y = int(input("y값을 입력하세요: "))

    if x > 0 and y > 0:
     print("1사분면 입니다.")
    elif x < 0 and y < 0:
        print("2사분면 입니다.")
    elif x < 0 and y < 0:
        print("3사분면 입니다.")
    else:
        print("4사분면 입니다.")



    # 칼로리 구하기 (과일마다 섭취 g를 입력 받아서 칼로리 출력하기) 위에 칼로리 이용, 이번엔 딕셔너리 사용
    eat_hanrabong = int(input("한라봉 몇 gram 드셨어영? "))
    eat_strawberry = int(input("딸기 몇 gram 드셨어영? "))
    eat_banana = int(input("바나나 몇 gram 드셨어영? "))
    kcal = {"hanrabong": 49 / 100, "strawberry": 35 / 100, "banana": 80 / 100}
    total = kcal['hanrabong'] * eat_hanrabong + kcal['strawberry'] * eat_strawberry + kcal['banana'] * eat_banana
    print("총{}kcal 드셨습니당~".format(total))



    # 반지름 입력 받아서 원의 둘레, 면적 출력 (둘레 소수점 1자리, 원의 면적 소수점 2자리)
    r = int(input("반지름을 입력하세요: "))
    wonju = 2 * r * math.pi
    circular_mil = r **2 * math.pi
    print("원의 둘레는 {:.1f}이고, 원의 면적은 {:.2f} 입니다".format(wonju, circular_mil))










if __name__ == '__main__':
    main()