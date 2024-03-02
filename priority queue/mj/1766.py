# https://www.acmicpc.net/problem/1766
# 메모리 : 39604 KB, 시간 : 196 ms
# 참고 코드 : https://seongonion.tistory.com/121

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = [0] * (n + 1)  # 각 노드에 들어오는 간선의 수
graph = [[] for _ in range(n + 1)]  # 먼저 풀 수 있는 문제를 넣을 그래프

for _ in range(m):
    a, b = map(int, input().split())

    in_degree[b] += 1  # b보다 우선해야할 a가 존재하면 b간선에 +1 -> b로 가는 간선이 추가된 것을 의미
    graph[a].append(b)  # a와 연결된 b를 추가

queue = []

for i in range(1, n + 1):
    if in_degree[i] == 0:  # 간선이 0이면 queue에 i를 추가(이때 우선순위에(작은것 부터)따라서 추가됨)
        heapq.heappush(queue, i)

# 간선이 0인 것들을 queue에 전부 넣은 후
while queue:
    current = heapq.heappop(queue)
    print(current, end=" ")  # 하나씩 출력

    for g in graph[current]:  # 빼낸 숫자와 연결된 숫자 찾고 간선 -1
        in_degree[g] -= 1

        # 만약 간선이 0이라면 queue에 추가 (이때 숫자는 우선순위에 따라 순서가 결정됨)
        if in_degree[g] == 0:
            heapq.heappush(queue, g)
