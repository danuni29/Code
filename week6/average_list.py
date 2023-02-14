def average(nums):
    return sum(nums)/len(nums)


def main():

    numbers=[80, 90, 100, 90]
    print("주어진 리스트는", numbers)
    print("평균은{:.1f}".format(average(numbers)))
if __name__ == '__main__':
    main()