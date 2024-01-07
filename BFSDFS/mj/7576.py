# https://www.acmicpc.net/problem/7576
# 메모리 : 98556KB, 시간 : 984ms

from collections import deque


# bfs
def bfs(grid, M, N):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 토마토 익는 방향
    queue = deque()

    # 토마토 돌기
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                queue.append((i, j, 0))  # 좌표 x, 좌표 y, day

    while queue:
        cur_x, cur_y, day = queue.popleft()

        for dx, dy in directions:
            next_x = cur_x + dx
            next_y = cur_y + dy
            if 0 <= next_x < N and 0 <= next_y < M:
                if grid[next_x][next_y] == 0:
                    grid[next_x][next_y] = 1  # 확인 후 익은 토마토로 바꿔주기
                    queue.append((next_x, next_y, day+1))  # 날짜 +1

    for row in grid:
        if 0 in row:  # 전부 확인 후 안익은 토마토가 있으면 -1 출력
            return -1
    return day


# 입력 받기
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


# 결과
result = bfs(grid, M, N)
print(result)
