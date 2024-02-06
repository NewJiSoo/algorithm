# https://www.acmicpc.net/problem/14675
# 메모리 : 122008 KB, 시간 : 248 ms

import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


q = int(input())
# 단절점이 아닌 노드 : 자식이 하나인 루트 노드, 리프 노드
# 모든 간선은 단절선
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if (len(graph[k]) < 2):
            print("no")
        else:
            print("yes")
    else:
        print("yes")
