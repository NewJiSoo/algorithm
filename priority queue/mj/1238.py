# https://www.acmicpc.net/problem/1238
# 메모리 : 34212 KB, 시간 : 1056 ms

import heapq
import sys

# 학생 N명, X번 마을
# 도로 M개
# i번째 길 T시간

N, M, X = map(int, sys.stdin.readline().split())
graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append((t, b))  # (시간*, 다음 마을)


def dijkstra(start, end):
    costs = {}
    pq = []

    heapq.heappush(pq, (0, start))
    while pq:
        cost, now = heapq.heappop(pq)

        if now == end:
            return cost

        if now not in costs:
            costs[now] = cost
            for weight, next_v in graph[now]:
                if next_v not in costs:
                    next_cost = weight + cost
                    heapq.heappush(pq, (next_cost, next_v))
    # return costs[end]


max_time = 0

for i in range(1, N+1):
    if i != X:
        go_X = dijkstra(i, X)  # 집->파티
        go_home = dijkstra(X, i)  # 파티 -> 집

        total_time = go_home + go_X
        max_time = max(total_time, max_time)
print(max_time)
