# https://www.acmicpc.net/problem/14235
# 메모리 : 40920 KB, 시간 : 408 ms

import heapq

n = int(input())

pq = []
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if len(pq) == 0:
            print(-1)
        else:
            value = heapq.heappop(pq)
            print(-value)
    else:
        for i in range(1, a[0]+1):
            heapq.heappush(pq, -a[i])
