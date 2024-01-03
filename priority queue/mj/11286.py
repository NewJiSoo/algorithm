# https://www.acmicpc.net/problem/11286
# 메모리 : 39824 KB, 시간 : 144 ms

import heapq
import sys

N = int(sys.stdin.readline())
heap = []  # (절대값, 기존값)

for _ in range(N):
    X = int(sys.stdin.readline())

    if X == 0:
        if heap:
            absolute, value = heapq.heappop(heap)
            print(value)
        else:
            print(0)
    else:
        if X > 0:
            heapq.heappush(heap, (X, X))
        else:
            heapq.heappush(heap, (-1*X, X))
