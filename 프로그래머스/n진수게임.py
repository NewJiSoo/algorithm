def solution(n, t, m, p):
    answer = ''
    arr = ''
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def change(num, k):
        tenary = ''
        while num != 0:
            remain = num % k
            # 10 이상인 경우 알파벳으로 변환
            if remain >= 10:
                tenary = dic[remain] + tenary
            else:
                tenary = str(remain) + tenary
            num //= k
        return tenary if tenary else '0'

    for i in range(t * m):
        if i == 0 or i == 1:
            arr += str(i)
        else:
            arr += change(i, n)

    for j in range(t):
        answer += str(arr[j * m + (p - 1)])

    return answer


print(solution(2, 4, 2,	1))
