# https://www.acmicpc.net/problem/1916
# 메모리 : 57372 KB, 시간 : 380 ms

import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())  # 출발, 도착, 비용
    graph[u].append((w, v))

s, e = map(int, sys.stdin.readline().split())  # 시작도시, 도착도시

costs = {}
pq = []
heapq.heappush(pq, (0, s))

while pq:
    cost, now = heapq.heappop(pq)

    if now not in costs:
        costs[now] = cost
        for weight, next_v in graph[now]:
            next_cost = cost + weight
            heapq.heappush(pq, (next_cost, next_v))

print(costs[e])
