# https://www.acmicpc.net/problem/2075
# 메모리 : 33188 KB, 시간 : 968 ms

import heapq
import sys

input = sys.stdin.readline

N = int(input())
graph = []  # 길이를 항상 N으로 유지하고 큰 숫자들만 담기

for _ in range(N):
    x = list(map(int, input().split()))
    for i in x:
        if len(graph) < N:  # 그래프가 N개만큼 채워져 있지 않으면 일단 넣기
            heapq.heappush(graph, i)
        else:  # 그래프가 N개를 넘었다면
            if graph[0] < i:  # 그래프에 있는 숫자들 중 가장 작은 숫자graph[0]와 i를 비교해서 i가 더 크면 graph[0]를 뺴고 i를 넣기
                heapq.heappop(graph)
                heapq.heappush(graph, i)
print(graph[0])
