def solution(N, stages):
    answer = []
    dic = {}
    for i in range(1, N + 2):
        dic[i] = 0
    for j in stages:
        dic[j] += 1

    cnt = 0
    for k in range(1, N + 2):
        if cnt >= len(stages):
            answer.append((k, 0))
        else:
            answer.append((k, dic[k] / (len(stages)-cnt)))
        cnt += dic[k]

    new = sorted(answer, key=lambda x: x[1], reverse=True)
    res = []

    for num, _ in new:
        if num != N+1:
            res.append(num)

    return res


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
