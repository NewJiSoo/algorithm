# https://www.acmicpc.net/problem/15903
# 메모리 : 33188 KB, 시간 : 56 ms

import heapq

n, m = map(int, input().split())

card = list(map(int, input().split()))
heapq.heapify(card)

for i in range(m):
    x = heapq.heappop(card)
    y = heapq.heappop(card)
    heapq.heappush(card, x+y)
    heapq.heappush(card, x+y)

print(sum(card))
