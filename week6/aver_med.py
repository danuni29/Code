def text2list(numbers):
    tokens = numbers.split(' ')
    numbers = []
    for i in tokens:
        numbers.append(int(i))
    return numbers

def average(nums):
    return sum(nums)/len(nums)

def median(nums):
    nums = sorted(nums)
    if len(nums) % 2 != 0:
        dan = int((len(nums)+1)/2 - 1)
        return nums[dan]
    else:
        dan = int(len(nums)/2)
        return nums[dan]

def main():

    input_text = "5 10 3 4 7"
    nums = text2list(input_text)
    print("주어진 리스트는", nums)
    print("평균값은{:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
if __name__ == '__main__':
    main()