# https://leetcode.com/problems/number-of-islands/description/

from collections import deque


def numIslands(grid):
    cnt = 0
    m = len(grid)  # 행
    n = len(grid[0])  # 열
    visited = [[False] * n for _ in range(m)]

    def bfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        q = deque()
        q.append((x, y))
        visited[x][y] = True
        while q:
            cur_x, cur_y = q.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    return cnt


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands(grid))
