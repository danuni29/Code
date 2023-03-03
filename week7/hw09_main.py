# 1) 총 강수량 : sum(rainfall) : sum(rainfall) : sum(rainfall) : sum(rainfall) : sum(rainfall) : sum(rainfall) -> 함수 따로 만들지 않아도 됨. 메인에서 값 확인만 .
# 2) 강우 일수는 ? count_rain_days ount_rain_days ount_rain_days ount_rain_days (rainfall) (rainfall) (rainfall) (rainfall)
def count_rain_days(rainfall):
    total_rain_days = 0
    for i in rainfall:
        if i != 0:
            total_rain_days += 1

    return total_rain_days


# 3) 여름철 (6 월-8월) 총 강수량은 ? sumifs umifs(rainfall, months, selected=[6,7,8])
def sumifs(rainfall, months, selected=[6,7,8]):
    days = len(months)
    total_rainfall = 0
    for i in range(days):
        if months[i] in selected:
            total_rainfall += rainfall[i]
    return total_rainfall





# 4) 최장연속강우일수는 ? longest_rain_days longest_rain_days longest_rain_days longest_rain_days longest_rain_days (rainfall)(rainfall)(rainfall)(rainfall) (rainfall) (rainfall)
def longest_rain_days(rainfall):
    rainy_days = []
    rain = 0
    for i in rainfall:
        if i != 0:
            rain += 1
        else:
            rainy_days.append(rain)
            rain = 0
    if rain != 0:
        rainy_days.append(rain)
    return max(rainy_days)


# 5) 강우이벤트 중 최대 강수량은 ? 비가 연속으로 올 때, 하나의 강우 이벤트로 가정
def maximum_rainfall_event(rainfall):
    rain_event = 0
    rain_event_2 = []
    for i in rainfall:
        if i > 0:
            rain_event += i
        else:
            rain_event_2.append(rain_event)
            rain_event = 0
    return max(rain_event_2)



# 6) 일교차가 가장 큰날짜와 일교차?
def maximum_temp_gap(dates, tmax, tmin):
    gap = 0
    day = []
    for i in range(len(dates)):
        temp_gap = tmax[i] - tmin[i]
        if temp_gap > gap:
            gap = temp_gap
            day = dates[i]

    return day, gap





# 7) 적산온도는?
def gdd(dates, tavg):
    temp = 0
    month = [5, 6, 7, 8, 9]
    for i in range(len(dates)):
        if dates[i][1] in month:
            if tavg[i] >= 5:
                temp += tavg[i]-5
    return temp





def main():
    f = open("../week6/weather(146)_2021-2021.csv")
    lines = f.readlines()
    rainfall = [float(x.split(",")[9]) for x in lines[1:]]
    tavg = [float(x.split(",")[4]) for x in lines[1:]]
    tmax = [float(x.split(",")[3]) for x in lines[1:]]
    tmin = [float(x.split(",")[5]) for x in lines[1:]]
    months = [int(x.split(",")[1]) for x in lines[1:]]
    dates = [[int(x.split(",")[0]), int(x.split(",")[1]), int(x.split(",")[2])] for x in lines[1:]]
    # # 1) 총 강수량
    print("총 강수량: {:.1f} mm".format(sum(rainfall)))
    # 2) 총 강우일수
    print("총 강우일수: {:d} 일".format(count_rain_days(rainfall)))
    # 3) 여름철 (6 월-8월) 총 강수량은 ?
    print("여름철 (6 월-8월) 총 강수량은 {:.1f} mm".format(sumifs(rainfall, months, [6,7,8])))
    # 4) 최장연속강우일수는 ?
    print("최장연속강우일수: {:d}일".format(longest_rain_days(rainfall)))
    # 5) 강우이벤트 중 최대 강수량은 ?
    print("강우이벤트 중 최대 강수량: {:.1f}".format(maximum_rainfall_event(rainfall)))
    # 6) 일교차가 가장 큰날짜와 일교차?
    print("일교차가 가장 큰날짜: {}, 일교차: {:.1f}도".format(*maximum_temp_gap(dates, tmax, tmin)))
    # 7) 적산온도는?
    print("적산온도는 {:.1f} degree-days".format(gdd(dates, tavg)))


if __name__ == "__main__":
    main()
