def minmax(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

def main():
    x = [3, 7, 25, 10, 2, 13]
    mn = minmax(x)[0]
    mx = minmax(x)[1]
    print("가장 작은수는 {}이고, 가장 큰 수는 {}입니다.".format(mn,mx))

if __name__ == '__main__':
    main()

