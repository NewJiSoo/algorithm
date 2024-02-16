# https://www.acmicpc.net/problem/10026
# 메모리 : 34104 KB, 시간 : 80 ms

from collections import deque

N = int(input())

graph = [list(input()) for _ in range(N)]


def bfs(x, y):
    visited[x][y] = True

    q = deque()
    q.append((x, y))

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        cur_r, cur_c = q.popleft()
        for dr, dc in direction:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < N and 0 <= next_c < N:
                if not visited[next_r][next_c] and graph[next_r][next_c] == graph[cur_r][cur_c]:
                    visited[next_r][next_c] = True
                    q.append((next_r, next_c))


cnt = 0
cnt2 = 0

# 적록색약 아닌 경우
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1

# 적록색약인 경우
visited = [[False]*N for _ in range(N)]  # 초기화
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1

print(cnt)
print(cnt2)
