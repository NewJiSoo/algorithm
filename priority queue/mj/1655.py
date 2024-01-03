# https://www.acmicpc.net/problem/1655
# 메모리 : 37132 KB, 시간 : 252 ms

import heapq
import sys

N = int(sys.stdin.readline())
min_heap = []
max_heap = []

for i in range(N):
    X = int(sys.stdin.readline())

    # 현재 값 X를 최대 힙 또는 최소 힙에 추가
    if not min_heap or X <= -min_heap[0]:
        heapq.heappush(min_heap, -X)
    else:
        heapq.heappush(max_heap, X)

    # 두 힙의 크기를 맞춰줌
    # min_heap의 길이가 max_heap+1보다 크면 반복 -> 하나 이상 차이나면 반복
    while len(min_heap) > len(max_heap) + 1:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    while len(max_heap) > len(min_heap):  # max_heap의 길이가 min_heap보다 크면 반복 -> 항상 min_heap이 많도록 유지
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    print(-min_heap[0])
