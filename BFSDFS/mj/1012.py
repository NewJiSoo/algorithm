# https://www.acmicpc.net/problem/1012
# 메모리 : 34068 KB, 시간 : 308ms


from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in direction:
            next_x = cur_x + dx
            next_y = cur_y + dy
            if 0 <= next_x < M and 0 <= next_y < N and not visited[next_x][next_y] and cabbage[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True


T = int(input())  # 테스트 케이스의 개수

for _ in range(T):
    M, N, K = map(int, input().split())  # 가로, 세로, 배추 수
    cabbage = [[0] * N for _ in range(M)]  # 배추밭 초기화
    visited = [[False] * N for _ in range(M)]  # 방문 여부 초기화
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향

    # 배추 위치
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[x][y] = 1

    count = 0

    for i in range(M):
        for j in range(N):
            if cabbage[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1

    print(count)
