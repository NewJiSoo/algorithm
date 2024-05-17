from math import ceil


def solution(fees, records):
    # 기본 요금 정보
    basic_time, basic_fee, plus_time, plus_fee = fees

    counting = {}
    parking = {}

    for record in records:
        time, car, status = record.split()
        h, m = map(int, time.split(':'))
        mins = h * 60 + m

        if status == "IN":
            parking[car] = mins
        elif status == "OUT":
            parked_time = mins - parking.pop(car)
            if car in counting:
                counting[car] += parked_time
            else:
                counting[car] = parked_time

    # 출차 기록이 없는 차들 처리
    end_of_day = 23 * 60 + 59
    for car, in_time in parking.items():
        parked_time = end_of_day - in_time
        if car in counting:
            counting[car] += parked_time
        else:
            counting[car] = parked_time

    # 최종 요금 계산
    answer = []
    for car in sorted(counting.keys()):
        total_time = counting[car]
        if total_time <= basic_time:
            total_fee = basic_fee
        else:
            total_fee = basic_fee + \
                ceil((total_time - basic_time) / plus_time) * plus_fee
        answer.append(total_fee)

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
      "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
