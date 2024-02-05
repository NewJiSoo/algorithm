# https://www.acmicpc.net/problem/11725
# 메모리 : 64924 KB, 시간 : 340 ms
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(v):
    for i in tree[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i)


dfs(1)

for i in range(2, N+1):
    print(parent[i])
