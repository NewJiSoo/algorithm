import heapq

N = 5
M = 4

cabbage = [[0] * N for _ in range(M)]
print(cabbage)


dec = [3, 5, 9, 15, -1]
heapq.heapify(dec)
print(-dec[0])


dic = [[] for _ in range(5)]
for _ in range(3):
    a, b = map(int, input().split())
    dic[a].append(b)
print(dic)
