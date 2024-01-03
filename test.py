import heapq

N = 5
M = 4

cabbage = [[0] * N for _ in range(M)]
print(cabbage)


dec = [3, 5, 9, 15, -1]
heapq.heapify(dec)
print(-dec[0])
