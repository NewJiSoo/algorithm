# https://leetcode.com/problems/unique-paths/description/


m, n = map(int, input().split())


# 완전탐색
# 시간복잡도 : if n = 100, m = 100일 때 O(2*10^58) -> 너무 큼
def dfs(r, c):
    if r == m and c == n:
        return 1

    unique_paths = 0
    if r+1 < m:
        unique_paths += dfs(r+1, c)
    if c+1 < n:
        unique_paths += dfs(r, c+1)

    return unique_paths


# dp - top down
# 시간 복잡도 : O(n*m)
def uniquePath(m, n):
    memo = [[-1]*n for _ in range(m)]

    def dp(r, c):
        unique_path = 0
        if r == 0 and c == 0:
            memo[r][c] = 1
            return memo[r][c]

        if memo[r][c] == -1:
            if (r-1) >= 0:
                unique_path += dp(r-1, c)
            if (c-1) >= 0:
                unique_path += dp(r, c-1)

            memo[r][c] = unique_path
        return memo[r][c]

    return dp(m-1, n-1)


# dp - bottom-up
# 시간복잡도 O(m*n)
def uniquePath2(m, n):
    memo = [[-1]*n for _ in range(m)]

    for r in range(m):
        memo[r][0] = 1
    for c in range(n):
        memo[0][c] = 1

    for r in range(1, m):
        for c in range(1, n):
            memo[r][c] = memo[r-1][c] + memo[r][c-1]
    return memo[m-1][n-1]
