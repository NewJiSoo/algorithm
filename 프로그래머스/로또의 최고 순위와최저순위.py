def solution(lottos, win_nums):
    answer = []
    max_cnt = 0
    min_cnt = 0
    for i in lottos:
        if i != 0:
            if i in win_nums:
                max_cnt += 1
                min_cnt += 1
        else:
            max_cnt += 1
    if max_cnt != 0:
        answer.append(7-max_cnt)
    else:
        answer.append(6)

    if min_cnt != 0:
        answer.append(7-min_cnt)
    else:
        answer.append(6)

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
