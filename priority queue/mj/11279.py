# https://www.acmicpc.net/problem/11279
# 메모리 : 38068 KB, 시간 : 124 ms

import heapq
import sys

N = int(sys.stdin.readline())
inList = []

for _ in range(N):
    X = int(sys.stdin.readline())

    if X == 0:
        if inList:
            print(-1*heapq.heappop(inList))
        else:
            print(0)
    else:
        heapq.heappush(inList, -1*X)
