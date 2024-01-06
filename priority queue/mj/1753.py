# https://www.acmicpc.net/problem/1753
# 메모리 : 94848 KB, 시간 : 1228 ms

import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

INF = int(1e9)
graph = [[] * (V+1) for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))  # u에서 v로 가는 가중치 w (가중치, 다음노드)

costs = {}
pq = []
heapq.heappush(pq, (0, K))

while pq:
    cost, now = heapq.heappop(pq)

    if now not in costs:
        costs[now] = cost
        for weight, next_v in graph[now]:
            next_cost = cost + weight
            heapq.heappush(pq, (next_cost, next_v))

for i in range(1, V+1):
    if i not in costs:
        print('INF')
    else:
        print(costs[i])
