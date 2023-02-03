def sum_n(n):
    a = n*(n+1)/2
    print(f"결과는 {a}입니다.")

def main():
    n=int(input("입력하세요"))
    sum_n(n)


if __name__ == '__main__':
    main()