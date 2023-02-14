def largest(numbers):
    return  min(numbers), max(numbers)




def main():
    # x = [1, 2, 3, 4]
    # mn = largest(x)[1]
    # mx = largest(x)[0]
    # print(mn, mx, largest(x))
    input_text = '5 1 3 4 7'
    tokens = input_text.split(' ')
    print(tokens)
    numbers = []
    for i in tokens:
        numbers.append(int(i))
        print(numbers)



if __name__ == '__main__':
    main()