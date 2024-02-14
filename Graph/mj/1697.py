# https://www.acmicpc.net/problem/1697
# 메모리 : 35320 KB, 시간 : 96 ms

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
Max = 10**5
visited = [0] * (Max+1)


def bfs():
    q = deque()
    q.append(N)

    while q:
        cur_v = q.popleft()
        if cur_v == K:
            print(visited[cur_v])
            break

        for v in (cur_v+1, cur_v-1, cur_v*2):
            if v >= 0 and v <= Max:
                if not visited[v]:
                    visited[v] = 1 + visited[cur_v]
                    q.append(v)


bfs()
