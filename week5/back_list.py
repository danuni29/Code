def range_list(n, x):
    for i in range(0, n+1):
        print(x[i])

def main():
    n=int(input("입력하세요"))
    x = [3, 7, 25, 10, 2, 13]
    range_list(n, x)

if __name__ == '__main__':
    main()