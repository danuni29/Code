def f2c(temp_f):
    cc = (temp_f-32) / 1.8
    return "{:.1f}F는 {:.1f}입니다.".format(78, cc)

def main():
    print(f2c(78))

if __name__ == '__main__':
    main()



