# https://www.acmicpc.net/problem/9372
# 메모리 : 32268 KB, 시간 : 196 ms

import sys
input = sys.stdin.readline

t = int(input())


def minDepth(node, cnt):
    check[node] = 1

    for i in graph[node]:
        if check[i] == 0:
            cnt = minDepth(i, cnt+1)

    return cnt


for _ in range(t):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    check = [0]*(N+1)
    cnt = minDepth(1, 0)
    print(cnt)
