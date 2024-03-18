def solution(friends, gifts):
    names = {name: index for index, name in enumerate(friends)}
    # 친구 : 인덱스
    N = len(friends)  # 총 친구 수
    answer = [0] * N
    rate = [0] * N  # 친구별로 받은 설물 수

    # 친구간 선물 교환 횟수
    gifts_cnt = [[0]*N for _ in range(N)]

    for i in gifts:
        a, b = i.split()
        gifts_cnt[names[a]][names[b]] += 1

    for i in range(N):
        rate[i] = sum(gifts_cnt[i]) - sum([k[i] for k in gifts_cnt])
        # i번째 친구가 선물 준 횟수의 합 - i번째 친구가 받은 선물 수의 합

    for q in range(N):
        for w in range(N):
            # q가 w에게 선물 준 횟수가 더 많으면
            if gifts_cnt[q][w] > gifts_cnt[w][q]:
                answer[q] += 1
            # q와 w가 선물 주고 받은 횟수가 같을 때
            elif gifts_cnt[q][w] == gifts_cnt[w][q]:
                # 선물 지수가 q가 더 높다면
                if rate[q] > rate[w]:
                    answer[q] += 1

    return max(answer)
