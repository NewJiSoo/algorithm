# https://www.acmicpc.net/problem/1260
# 메모리 : 34044 KB, 시간 : 636 ms

from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for s in graph:
    s.sort()


def bfs(V):
    q = deque()
    q.append(V)
    visited = [V]
    while q:
        cur_v = q.popleft()
        print(cur_v, end=" ")
        for i in graph[cur_v]:
            if i not in visited:
                visited.append(i)
                q.append(i)

    return visited


dfs_visi = []


def dfs(V):
    dfs_visi.append(V)
    print(V, end=" ")
    for j in graph[V]:
        if j not in dfs_visi:
            dfs(j)


dfs(V)
print()
bfs(V)
