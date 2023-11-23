def dfs(x, y):
    # 방향
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if yard[ny][nx] == 1:
                yard[ny][nx] = 0  # 방문 여부 대신 0으로 바꿔서 중복확인 없도록 처리
                dfs(nx, ny)


t = int(input())  # 테스트 케이스

for _ in range(t):
    m, n, k = map(int, input().split())

    yard = [[0] * (m) for _ in range(n)]

    cnt = 0

    for _ in range(k):
        a, b = map(int, input().split())
        yard[b][a] = 1  # 배추밭 가로 세로를 바꾸는 대신 배추 좌표를 바꿈

    for i in range(m):
        for j in range(n):
            if yard[j][i] == 1:
                dfs(i, j)
                cnt = cnt + 1

    print(cnt)
