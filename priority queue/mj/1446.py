# https://www.acmicpc.net/problem/1446
# 메모리 : 33188 KB, 시간 : 48 ms

import heapq
import sys

N, D = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(D+1)]

for i in range(D):  # 그래프를 도착 길이만큼 만들어주기 -> 이것 자체가 너무 비효율적이라는 생각이 든다
    graph[i].append((i+1, 1))

for i in range(N):
    start, end, length = map(int, sys.stdin.readline().split())
    if end > D:  # 만약 지름길 도착 길이가 세준이가 도착하려는 길이보다 길면 그 지름길은 안쓸것
        continue
    graph[start].append((end, length))
    # 예상 그래프 모양
    # graph = {
    # 0: [(1, 1)], => 0에서 1로가는데 길이 = 1
    # 1: [(2, 1), (50, 20)], => 추가된 지름길, 1에서 50으로 가는데 길이 = 20
    # 2: [(3, 1)],
    # 3: [(4, 1)], ... }

INF = int(1e9)
distance = [INF] * (D+1)  # 추가할 거리배열 초기화
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
