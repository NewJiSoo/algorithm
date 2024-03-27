def solution(number):
    answer = 0

    def find(start, dec):
        if len(dec) == 3:
            if sum(dec) == 0:
                return 1

        cnt = 0
        for i in range(start, len(number)):
            dec.append(number[i])
            cnt += find(i+1, dec)
            dec.pop()
        return cnt

    answer += find(0, [])
    return answer


print(solution([-2, 3, 0, 2, -5]))
