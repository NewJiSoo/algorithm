# https://www.acmicpc.net/problem/19638
# 메모리 : 37044 KB, 시간 : 172 ms

import heapq
import sys
input = sys.stdin.readline

N, H, T = map(int, input().split())

pq = []
for _ in range(N):
    height = int(input())
    heapq.heappush(pq, -height)

cnt = 0
for _ in range(T):
    max_height = heapq.heappop(pq)*(-1)
    if max_height == 1:
        heapq.heappush(pq, -1)
        break
    elif max_height >= H:
        heapq.heappush(pq, -(max_height//2))
        cnt += 1
    else:
        heapq.heappush(pq, -max_height)
        break


total = heapq.heappop(pq)*(-1)
if total >= H:
    print('NO')
    print(total)
else:
    print('YES')
    print(cnt)
