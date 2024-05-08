from collections import deque


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    row = len(maps)
    col = len(maps[0])

    visited = [[0] * col for _ in range(row)]

    def bfs(x, y):
        visited[x][y] = 1
        q = deque()
        q.append((x, y))

        while q:
            curx, cury = q.popleft()
            for i in range(4):
                nextx = curx + dx[i]
                nexty = cury + dy[i]
                if 0 <= nextx < row and 0 <= nexty < col:
                    if maps[nextx][nexty] == 1 and visited[nextx][nexty] == 0:
                        visited[nextx][nexty] = visited[curx][cury] + 1
                        q.append((nextx, nexty))
    bfs(0, 0)

    if visited[row-1][col-1] == 0:
        return -1
    else:
        return visited[row-1][col-1]


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
