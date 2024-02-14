# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from collections import deque


def bfs(grid):
    cnt = -1
    row = len(grid)
    col = len(grid[0])

    if grid[0][0] != 0 or grid[row-1][col-1] != 0:
        return -1

    visited = [[False]*col for _ in range(row)]
    q = deque()
    q.append((0, 0, 1))
    visited[0][0] = True

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1),
                 (1, 1), (-1, -1), (1, -1), (-1, 1)]

    while q:
        cur_r, cur_c, cur_len = q.popleft()

        if cur_r == row - 1 and cur_c == col - 1:  # 목적지에 도착했을 때
            cnt = cur_len
            break

        # 연결되어있는 vertex 확인하기
        for dr, dc in direction:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    q.append((next_r, next_c, cur_len+1))
                    visited[next_r][next_c] = True

    return cnt
