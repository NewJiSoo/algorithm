# https://www.acmicpc.net/problem/1927
# 메모리 : 37044 KB, 시간 : 120 ms

import heapq
import sys

N = int(sys.stdin.readline())
inList = []

for _ in range(N):
    X = int(sys.stdin.readline())

    if X == 0:
        if inList:
            print(heapq.heappop(inList))
        else:
            print(0)
    else:
        heapq.heappush(inList, X)
