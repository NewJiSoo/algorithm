# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# 시간 초과
# for _ in range(M):
#     xy = list(map(int, input().split()))

#     cnt = 0
#     for i in range(xy[0]-1, xy[2]):
#         for j in range(xy[1]-1, xy[3]):
#             cnt += table[i][j]
#     print(cnt)


# dp
# 메모리 : 105940 KB, 시간 : 1052 ms
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + table[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)
