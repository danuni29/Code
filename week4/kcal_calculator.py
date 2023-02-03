
def main():
    eat_orange=int(input("오늘 먹은 한라봉 양(g): ",))
    eat_strawberry=int(input("오늘 먹은 딸기 양(g): "))
    eat_banana=int(input("오늘 먹은 바나나 양(g): "))

    calories = {"한라봉": 49/100, "딸기": 35/100, "바나나": 80/100} #한라봉, 딸기, 바나나
    total_calories = calories['한라봉']*eat_orange+calories['딸기']*eat_strawberry\
                     +calories['바나나']*eat_banana

    print(total_calories)





if __name__ == '__main__':
    main()