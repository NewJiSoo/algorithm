import heapq

N = 5
M = 4

cabbage = [[0] * N for _ in range(M)]
print(cabbage)


dec = [3, 5, 9, 15, -1]
print(heapq.heappop(dec))

graph = {
    # 1번 노드와 연결된 노드 : 2, 4번, 2번 노드로 가는 비용 : 2, 4번 노드로 가는 비용 : 1
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: []
    # ...
}

if graph[6]:
    print('true')
else:
    print('false')
