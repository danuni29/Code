# 1) 총 강수량 : sum(rainfall) : sum(rainfall) : sum(rainfall) : sum(rainfall) : sum(rainfall) : sum(rainfall) -> 함수 따로 만들지 않아도 됨. 메인에서 값 확인만 .
# 2) 강우 일수는 ? count_rain_days ount_rain_days ount_rain_days ount_rain_days (rainfall) (rainfall) (rainfall) (rainfall)
def count_rain_days(rainfall):
    total_rain_days = 0
    for i in rainfall:
        if i != 0:
            total_rain_days += 1

    return total_rain_days


# 3) 여름철 (6 월-8월) 총 강수량은 ? sumifs umifs(rainfall, months, selected=[6,7,8]) (rainfall, months, selected=[6,7,8]) (rainfall, months, selected=[6,7,8]) (rainfall, months, selected=[6,7,8]) (rainfall, months, selected=[6,7,8]) (rainfall, months, selected=[6,7,8]) (rainfall, months, selected=[6,7,8])
def sumifs(rainfall, months, selected=[6,7,8]):


    return -1


# 4) 최장연속강우일수는 ? longest_rain_days longest_rain_days longest_rain_days longest_rain_days longest_rain_days (rainfall)(rainfall)(rainfall)(rainfall) (rainfall) (rainfall)
def longest_rain_days(rainfall):
    return -1


# 5) 강우이벤트 중 최대 강수량은 ? 비가 연속으로 올 때, 하나의 강우 이벤트로 가정
def maximum_rainfall_event(rainfall):
    return -1


# 6) 일교차가 가장 큰날짜와 일교차?
def maximum_temp_gap(dates, tmax, tmin):
    return [2021, 1, 20], 23.2


# 7) 적산온도는?
def gdd(dates, tavg):
    return -1


def main():
    f = open("weather(146)_2021-2021.csv")
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
