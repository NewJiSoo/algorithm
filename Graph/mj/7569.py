# https://www.acmicpc.net/problem/7569
# 메모리 : 57552 KB, 시간 : 1892 ms
# 참고 코드 : https://jiwon-coding.tistory.com/98

import sys
from collections import deque

m, n, h = map(int, input().split())

graph = [[list(map(int, sys.stdin.readline().split()))
          for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

queue = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

answer = 0


def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                queue.append((nx, ny, nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1
                visited[nx][ny][nz] = True


# 모두 1이 아닐 경우
for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c] == 1 and not visited[a][b][c]:
                queue.append((a, b, c))
                visited[a][b][c] = True
bfs()


# 토마토 확인
for a in graph:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit()  # break를 쓰면 for문 하나 종료, 반복문을 전부 끝나고 싶으면 exit()사용
        answer = max(answer, max(b))  # graph 한행씩 비교

print(answer-1)  # 1(익은 토마토)부터 시작했기 때문에 -1 해주기
# 어차피 모두 1이라면 0이 출력된다.
