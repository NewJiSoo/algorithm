# https://www.acmicpc.net/problem/1715
# 메모리 : 33972 KB, 시간 : 188 ms

import heapq
import sys

N = int(sys.stdin.readline())
dec = []

for _ in range(N):
    X = int(sys.stdin.readline())
    heapq.heappush(dec, X)


if len(dec) == 1:
    print(0)
else:
    result = 0
    while len(dec) > 1:
        A = heapq.heappop(dec)
        B = heapq.heappop(dec)
        result += A + B
        heapq.heappush(dec, A+B)
    print(result)
