def dan(x):
    for i in range(1,10):
        print("{} * {} = {}".format(x,i,x*i))



def main():
    x= int(input("원하는 단을 입력하세요: "))
    dan(x)
if __name__ == '__main__':
    main()
