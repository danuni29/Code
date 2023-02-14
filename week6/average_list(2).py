def average(nums):
    list_sum = 0
    list_count = 0
    for num in nums:
        list_sum += num
        list_count += 1
    if list_count >0:
        return list_sum / list_count
    return None

def main():
    numbers = [80, 90, 100, 90]
    print("주어진 리스트는", numbers)
    print("평균은 {:.1f}".format(average(numbers)))
if __name__ == '__main__':
    main()