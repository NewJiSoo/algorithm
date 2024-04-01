def solution(n, lost, reserve):
    answer = len(lost)
    dic = {}
    dic2 = {}
    lost.sort()
    reserve.sort()

    for j in lost:
        dic2[j] = 1

    for name in reserve:
        dic[name] = 1
        if name in dic2:
            dic[name] = 0
            dic2[name] = 0
            answer -= 1

    for i in dic2:
        if dic2[i] == 1:
            if (i-1) in dic and dic[i-1] != 0:
                dic[i-1] = 0
                answer -= 1
            elif (i+1) in dic and dic[i+1] != 0:
                dic[i+1] = 0
                answer -= 1

    return n - answer


print(solution(4, [2, 3], [3, 4]))
