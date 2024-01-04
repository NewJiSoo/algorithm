# https://www.acmicpc.net/problem/18352
# 메모리 : 161684 KB, 시간 : 1852 ms

import sys
import heapq

input = sys.stdin.readline


def dijkstra(graph, start, final):
    costs = {start: 0}  # 비용 정보, 시작 도시에서 시작도시의 길이 = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)  # 비용(길이), 현재 도시

        if cur_cost > final:  # 비용(길이)가 목표 비용(최단거리)보다 길면 탐색X
            break
        if cur_cost == final:  # 목표 발견 시 값 반환
            yield cur_v  # 도시가 여러개일 수 있으니 return 말고 yield 사용

        for cost, next_v in graph[cur_v]:  # 현재 도시와 연결된 도시 찾기
            next_cost = cur_cost + cost  # 현재까지 비용 + 다음 도시 비용(사실상 1)

            # 만약 다음 도시가 비용정보에 없거나 누적 비용이 더 작으면 업데이트
            if next_v not in costs or next_cost < costs[next_v]:
                costs[next_v] = next_cost
                heapq.heappush(pq, (next_cost, next_v))


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]  # 도로 정보 초기화

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((1, b))  # (거리길이, 도착도시)


result = list(dijkstra(graph, X, K))

if not result:
    print(-1)
else:
    for city in sorted(result):  # 오름차순 정렬
        print(city)
