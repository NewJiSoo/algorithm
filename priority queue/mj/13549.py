# https://www.acmicpc.net/problem/13549
# 메모리 : 45996 KB, 시간 : 240 ms

import heapq
import sys

N, K = map(int, sys.stdin.readline().split())

costs = {}
pq = []
heapq.heappush(pq, (0, N))

while pq:
    cost, now = heapq.heappop(pq)

    if now == K:
        print(cost)
        break

    if now not in costs:
        costs[now] = cost
        for weight, next_v in [(1, now+1), (1, now-1), (0, now*2)]:
            if 0 <= next_v <= 100000 and next_v not in costs:
                next_cost = cost + weight
                heapq.heappush(pq, (next_cost, next_v))
