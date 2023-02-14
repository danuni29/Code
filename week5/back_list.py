def range_list(n, x):
    for i in range(0, n+1):
        print(x[i])


def range_list2(n):
    results = []
    for i in range(n):
        # results.append(i)
        print(i)

def main():
    n=int(input("입력하세요"))
    range_list2(n)

if __name__ == '__main__':
    main()