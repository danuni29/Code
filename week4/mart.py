def main():
    mart = {"우유":2800, "계란": 300, "빵":1200, "물":1700}
    cart = ["물", "우유", "계란", "빵"]
    total_cost = 0
    for item in cart:
        total_cost+=mart[item]
    print("총 구매금액은{:,}원입니다.".format(total_cost))
if __name__ == '__main__':
    main()