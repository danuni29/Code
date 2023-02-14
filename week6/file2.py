def main():
    f = open("numbers2.txt")
    text = f.readlines()
    a = []
    for i in text:
        b = i.strip('\n')
        a.append(int(b))
    print(a)
    print("총 숫자의 갯수는 {}".format(len(a)))
    print("주어진 숫자의 평균은 {}".format(sum(a)/len(a)))
    print("주어진 숫자의 최댓값은 {}".format(max(a)))
    print("주어진 숫자의 최솟값은 {}".format(min(a)))

if __name__ == '__main__':
    main()