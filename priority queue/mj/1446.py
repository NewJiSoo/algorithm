# https://www.acmicpc.net/problem/1446
# 메모리 : 33188 KB, 시간 : 48 ms

import heapq
import sys

N, D = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(D+1)]

for i in range(D):
    graph[i].append((i+1, 1))

for i in range(N):
    start, end, length = map(int, sys.stdin.readline().split())
    if end > D:
        continue
    graph[start].append((end, length))

INF = int(1e9)
distance = [INF] * (D+1)
distance[0] = 0

pq = []
heapq.heappush(pq, (0, 0))

while pq:
    d, now = heapq.heappop(pq)

    if d > distance[now]:
        continue

    for e, l in graph[now]:
        next_cost = l + d

        if next_cost < distance[e]:
            distance[e] = next_cost
            heapq.heappush(pq, (next_cost, e))

print(distance[D])
