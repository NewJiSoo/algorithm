# https://www.acmicpc.net/problem/1417
# 메모리 : 33320 KB, 시간 : 48 ms

import heapq

N = int(input())
dasom = int(input())*-1
candi = []
for _ in range(N-1):
    votes = int(input())
    heapq.heappush(candi, -votes)

cnt = 0
while candi:
    x = heapq.heappop(candi)
    if x > dasom:  # 다솜이 후보들 숫자보다 작다면 -> 음수이기 때문에 숫자가 작을 수록 사람수가 더 많은 것
        break  # while문 종료

    dasom -= 1  # 다솜의 수를 더 낮춤 -> 숫자를 더 크게 만듬
    x += 1  # 위와 반대
    heapq.heappush(candi, x)
    cnt += 1


print(cnt)
