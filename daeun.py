def average(x):
    return sum(x) / len(x)


def main():
    x = [3, 7, 25, 10, 2, 13]
    print("평균은 {}입니다.".format(average(x)))


if __name__ == '__main__':
    main()