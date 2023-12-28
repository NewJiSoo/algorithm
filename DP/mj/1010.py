# https://www.acmicpc.net/problem/1010
# 메모리 : 31120 KB, 시간 : 92ms

def path(n, m):
    memo = [[1]*(m+1) for _ in range(m+1)]

    for i in range(2, m+1):
        memo[1][i] = i

    for i in range(2, n+1):
        for j in range(i+1, m+1):
            memo[i][j] = memo[i-1][j-1]+memo[i][j-1]

    return memo[n][m]


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(path(N, M))
